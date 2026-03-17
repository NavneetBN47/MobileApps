import base64
import json
import requests
from lxml import html
import re
import argparse
from datetime import datetime, timedelta, timezone
import logging

parser = argparse.ArgumentParser()
parser.add_argument('--f', action='store_true')
parser.add_argument('--build_type',action='store_true') # ITG \ STG
parser.add_argument('--test_type',action='store_true') # Functionality \ Smoke&Sanity
parser.add_argument('--plan_id',action='store_true')
parser.add_argument('--suite_id',action='store_true') # 198686
parser.add_argument('file')
parser.add_argument('build_type')
parser.add_argument('test_type')
parser.add_argument('plan_id')
parser.add_argument('suite_id')

report_file = str(parser.parse_args().file)
build_type = str(parser.parse_args().build_type)
test_type = str(parser.parse_args().test_type)
plan_id = str(parser.parse_args().plan_id)
suite_id = int(parser.parse_args().suite_id)


def get_format_date(delay=0):
    utc_time = datetime.now(timezone.utc)
    offset = timedelta(hours=8)
    local_time = utc_time + offset
    final_time = local_time - timedelta(days=delay)
    format_date = final_time.strftime("%Y-%m-%d")
    return format_date


def get_test_plan():
    response = requests.get(base_url + 'get_plan/' + plan_id, headers=headers)
    if response.status_code != 200:
        print("Failed to get plan. Status code:", response.status_code)
        return None
    
    plan = response.json()
    runs_list = [entry['runs'] for entry in plan['entries']]
    run_name_list = [run['name'] for run_list in runs_list for run in run_list]
    
    # Find the test run that with the same build version and test type
    existing_run = None
    for each_plan in run_name_list[::-1]:
        if version_num in each_plan and f"[{build_type.upper()}]{test_type.capitalize()}" in each_plan:
            existing_run = each_plan
            print(f"Found existing test run for version {version_num}: {existing_run}")
            break
    
    if existing_run:
        # Found the test run for this version, reuse it directly
        test_plan = existing_run
    else:
        # Create a new test run if No existing test run found for this version
        print(f"No existing test run found for version {version_num}, will create a new test run")
        test_plan = '[{0}][{1}]{2}_{3}'.format(format_time, build_type.upper(), test_type.capitalize(), version_num)
    
    return test_plan


def get_report_result():
    logging.info(f"Parsing report file: {report_file}")
    with open(report_file, "r") as f:
        tree = html.fromstring(f.read())
    results_table = tree.xpath('//tbody[contains(@class, "results-table-row")]')
 
    version = None
    for row in results_table:
        for log_text in row.xpath('.//*[@class="log"]/text()'):
            log_str = ''.join(log_text).replace("\n", "")
            pattern_1 = r'App Info: (.*?)\.zip'
            pattern_2 = r'RESO = (.*?)_Test'
            result_1 = re.search(pattern_1, log_str)
            
            if result_1 is not None:
                version = result_1.group(1)
                break
            elif result_1 is None:
                result_2 = re.search(pattern_2, log_str)
                if result_2 is not None:
                    version = result_2.group(1).split('\\')[-2]
                    break
        if version is not None:
            break
    else:
        version = "no version in this build log"

    printer_info = None
    for row in results_table:
        for log_text in row.xpath('.//*[@class="log"]/text()'):
            log_str = ''.join(log_text).replace("\n", "")
            pattern = r'Created simulator printer from API response: \[(.*?)\]'
            result = re.search(pattern, log_str)
            if result is not None:
                printer_info = result.group(1)
                break
        if printer_info is not None:
            break
    else:
        printer_info = 'None'

    results = []
    for row in results_table:
        test = row.xpath('.//*[@class="col-name"]/text()')
        case_id_list = re.findall(r"[Cc](\d+)", str(test))
        if len(case_id_list)!=0:
            for case_id in case_id_list:
                comment = row.xpath('.//*[@class="log"]/span[@class="error"]/text()')
                Skipped_comment = re.search("'Skipped:(.*?)\\)", str(row.xpath('.//*[@class="log"]/text()')))
                if Skipped_comment:
                    comment = Skipped_comment.group().replace("')", "'")
                    if "ONESIM printer limitation" in str(comment):
                        continue
                result = {
                    "Result": row.xpath('.//*[@class="col-result"]/text()')[0],
                    "Test": test[0],
                    "Case_id": case_id,
                    "Duration": row.xpath('.//*[@class="col-duration"]/text()')[0],
                    "Version": version,
                    "Comment": comment
                }
                if result["Result"] != []:
                    results.append(result)
    return version, printer_info, results

def get_case_id_result():
    id_result = {}
    id_comment = {}
    for i in results:
        if "ONESIM printer limitation" not in i['Comment']:
            if i["Case_id"] not in id_result:
                if str(i["Result"]) == "Failed" or str(i["Result"]) == "Error":
                    id_result[i["Case_id"]] = 5
                elif str(i["Result"]) == "Skipped":
                    id_result[i["Case_id"]] = 6
                else:
                    id_result[i["Case_id"]] = 1
                id_comment[i["Case_id"]] = i["Comment"]
            else:
                if str(i["Result"]) == "Failed" or str(i["Result"]) == "Error":
                    id_result[i["Case_id"]] = 5
                    id_comment[i["Case_id"]]=i["Comment"]

    return id_result, id_comment

def get_testrail_plan_info():
    logging.info(f"Fetching TestRail plan info for run ID: {plan_id}")
    response = requests.get(base_url + 'get_plan/' + plan_id, headers=headers)
    logging.info(f"Response Status Code: {response.status_code}")
    if response.status_code != 200:
        print("Failed to get plan. Status code:", response.status_code)
        return None

    plan = response.json()
    runs_list = [entry['runs'] for entry in plan['entries']]
    run_name_list = [run['name'] for run_list in runs_list for run in run_list]
    run_id_list = [run['id'] for run_list in runs_list for run in run_list]
    run_entry_id_list = [run['entry_id'] for run_list in runs_list for run in run_list]
    run_is_completed_list = [run['is_completed'] for run_list in runs_list for run in run_list]
    run_name_entry_id = dict(zip(run_name_list, run_entry_id_list))
    run_name_id = dict(zip(run_name_list, run_id_list))
    run_name_completed = dict(zip(run_name_list, run_is_completed_list))

    return run_name_entry_id, run_name_id, run_name_completed

def add_or_update_rail_plan():
    exist_case_id_list = []
    for name, id in run_name_id.items():
        if name == test_plan and run_name_completed[name] == False:
            response = requests.get(base_url + 'get_tests/' + str(id), headers=headers)
            test_info_list = response.json()
            for test_info in test_info_list:
                exist_case_id_list.append(str(test_info["case_id"]))

    set1 = set(exist_case_id_list)
    set2 = set(list(id_result.keys()))
    all_case_id_list = list(set1 | set2)

    if not all_case_id_list:
        logging.info(f"No test cases to add or update in the test plan.")
    else:
        data = {
            "name": test_plan,
            "suite_id": suite_id,
            "include_all": False,
            "case_ids": all_case_id_list,
            "runs": [
                {
                    "include_all": False,
                    "case_ids": all_case_id_list
                }
            ]
        }
        if test_plan not in run_name_id:
            response = requests.post(base_url + 'add_plan_entry/' + plan_id, headers=headers,
                                data=json.dumps(data))
        else:
            entry_id = run_name_entry_id[test_plan]
            response = requests.post(base_url + 'update_plan_entry/' + plan_id + "/" + str(entry_id), headers=headers,
                                    data=json.dumps(data))
        if response.status_code != 200:
            print("Failed to get plan. Status code:", response.status_code)

        return response.json()

def get_case_id_id():
    run_name_id = get_testrail_plan_info()[1]
    for name, plan_id in run_name_id.items():
        if name == test_plan:
            response = requests.get(base_url + 'get_tests/' + str(plan_id), headers=headers)
            test_info = response.json()
            case_id_list = [test['case_id'] for test in test_info]
            id_list = [test['id'] for test in test_info]
            case_id_id = dict(zip(case_id_list, id_list))
            return case_id_id

if __name__ == '__main__':
    base_url = 'https://hp-testrail.external.hp.com//index.php?/api/v2/'
    api_token = 'ivan.you@hp.com:' + '32zya2XAiOMiJf9mtWlv-4x1dznbpZoYpBizk12uz'
    token = base64.b64encode(api_token.encode()).decode()
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Basic ' + token}
    
    logging.info("Start to upload test result to TestRail")

    version, printer_info, results = get_report_result()
    
    # Check if version was found in the build log
    if version == "no version in this build log":
        logging.warning("No version found in the build log. Skipping test run creation and result upload.")
        exit(0)
    
    version_num = version.split('_')[0]

    id_result, id_comment = get_case_id_result()

    format_time = get_format_date()
    test_plan = get_test_plan()
    run_name_entry_id, run_name_id, run_name_completed = get_testrail_plan_info()
    add_or_update_rail_plan()
    case_id_id = get_case_id_id()

    # Upload test results to TestRail
    error_id = []
    for case_id, result in id_result.items():
        comment = str(id_comment[case_id]).replace("[","").replace("]","")
        try:
            test_id = case_id_id[int(case_id)]
        except KeyError:
            error_id.append(int(case_id))
            continue

        if comment:
            auto_info = "\n" + "Error Information:" + "\n" + comment
            if 'Skipped:' in comment:
                auto_info = "\n" + "Skipped Information:" + "\n" + comment
        else:
            auto_info = ''
        data = {
            "status_id": result,
            "version": version,
            "comment": "Run by Automation: " + "\n" + "Printer Information: "  + "\n" + "{" + printer_info + "}" + auto_info
        }
        response = requests.get(base_url + 'get_results/' + str(test_id), headers=headers)
        results_info_list = response.json()
        if results_info_list:    
            check_status_id = int(results_info_list[0]['status_id'])    
            check_version = str(results_info_list[0]['version'])    
            if check_status_id == 1 and check_version == str(version):        
                pass    
            else:        
                response = requests.post(base_url + 'add_result/' + str(test_id), headers=headers, data=json.dumps(data))
        else:    
            response = requests.post(base_url + 'add_result/' + str(test_id), headers=headers, data=json.dumps(data)) 

    if len(error_id) != 0:
        print("Something went wrong with these case id ", error_id)
