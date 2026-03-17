import base64
import json
import datetime
import requests


import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
from lxml import html
from lxml import etree
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--f', action='store_true')
parser.add_argument('--f_xml', action='store_true')
parser.add_argument('--milestone_id',action='store_true')
parser.add_argument('--suites_id',action='store_true')
parser.add_argument('--test_plan',action='store_true')
parser.add_argument('--test_run',action='store_true')
parser.add_argument('--replacement_cases',action='store_true')
parser.add_argument('--test_run_id',action='store_true')
parser.add_argument('file')
parser.add_argument('xml_file')
parser.add_argument('milestone_id')
parser.add_argument('suites_id')
parser.add_argument('test_plan')
parser.add_argument('test_run')
parser.add_argument('replacement_cases')
parser.add_argument('test_run_id')

report_file = str(parser.parse_args().file)
report_file_xml = str(parser.parse_args().xml_file)
hpx_milestone_id = int((parser.parse_args().milestone_id))
suite_id = int((parser.parse_args().suites_id))
plan_name = str(parser.parse_args().test_plan)
production_run_id = str(parser.parse_args().test_run_id)
run_name = str(parser.parse_args().test_run)
replacement = str(parser.parse_args().replacement_cases)


xml_tree = ET.parse(report_file_xml)
xml_root = xml_tree.getroot()

testsuite = xml_root.find('testsuite')
fail_case_id = []
fail_case_reason = []


for testcase in testsuite:
    for fail_case in testcase:
        if fail_case.tag == "failure" or fail_case.tag == "error":
            fail_case_reason.append(fail_case.get('message'))
            
            fail_case = str(testcase.attrib)
            pattern = r"C(\d+)"
            result = re.search(pattern, fail_case)
            try:
                fail_case = result.group(1)
                fail_case_id.append(fail_case)
                break
            except:
                fail_case = " "

fail_cases_results = dict(zip(fail_case_id, fail_case_reason))



def get_fail_case_comment(case_id):

    if not fail_cases_results:
        comment = " "
        return comment

    for case, fail_result in fail_cases_results.items():

        if int(case) == int(case_id):
            comment = fail_result
            break
        else:
            comment = " "
    return comment





with open(report_file, "r") as f:
    tree = html.fromstring(f.read())


test_case = []


report_time = tree.xpath('//p[contains(text(), "Report generated")]/text()')
summary = tree.xpath('//p[contains(text(), "tests ran in")]/text()')
environment = {el[0].text: el[1].text for el in tree.xpath('//table[@id="environment"]//tr')}
try:
    platform_name = environment['PLATFORM'].split('&&')[-1]
except KeyError:
    platform_name = environment['JOB_NAME'].split('&&')[-1]



logs = []
for v in tree.xpath('//tbody[contains(@class, "results-table-row")]'):
    log = {
        "log": v.xpath('.//*[@class="log"]/text()')
    }
    logs.append(log)


for i in logs:
    v_str = ''.join(i["log"]).replace("\n", "")
    pattern = r'App Info: (.*?)_TRACK'
    result = re.search(pattern, v_str)
    try:
        version = result.group(1)
        break
    except:
        version = "no version in this build log"
    



results = []
for row in tree.xpath('//tbody[contains(@class, "results-table-row")]/tr'):
    result = {
        "Result": row.xpath('.//td[@class="col-result"]/text()'),
        "Test": row.xpath('.//td[@class="col-name"]/text()'),
        "Duration": row.xpath('.//td[@class="col-duration"]/text()'),
        "Version": version
    }
    if result["Result"] != []:
        results.append(result)





# TestRail information
base_url = 'https://hp-testrail.external.hp.com//index.php?/api/v2/'
api_token = 'hao.an@hp.com:' + 'qauLgdE0BfeJdmA5Wpcl-o30hUXku0qOGU93Y0eFj'
token = base64.b64encode(api_token.encode()).decode()
headers = {'Content-Type': 'application/json',
           'Authorization': 'Basic ' + token}


replacement_cases_url = 'http://felix3001.auth.hpicorp.net:8011/testcases'
replacement_cases_headers = {'Content-Type': 'application/json'}

try:
    replacement_cases_response = requests.get(replacement_cases_url, headers=replacement_cases_headers)
    replacement_cases_list = replacement_cases_response.json()
except Exception as e:
    replacement_cases_list = []
    print(f"The exception is {e}")





case_id_list = []
case_result = []
for i in results:
    if i["Result"] != ['Skipped']:
        case_id_pattern = r"C(\d+)"
        match = re.search(case_id_pattern, str(i['Test']))
        if match:
            case_id_list.append(match.group(1))
            case_result.append(str(i['Result']).replace("['","").replace("']",""))

for j in range(len(case_result)):
    if case_result[j] == "Failed" or case_result[j] == "Error":
        case_result[j] = 5
    else:
        case_result[j] = 1

case_id_result = dict(zip(case_id_list, case_result))



def get_plans_for_hpx_milestone():

    response = requests.get(base_url + 'get_plans/' + str(441), headers=headers)
    
    if response.status_code != 200:
        print("Failed to get plan. Status code:", response.status_code)
        return None
    
    all_plans = response.json()
    plans_for_milestone = [plan for plan in all_plans if plan['milestone_id'] == hpx_milestone_id]
    

    return plans_for_milestone


def add_plan_to_hpx_milestone():

    for i in results:
        version = str(i["Version"])
        break
        

    date = str(datetime.date.today()).replace('-', '_')
    plans_for_milestone = get_plans_for_hpx_milestone()

    
    if len(plans_for_milestone) == 0:
        data = {
            "name": plan_name,
            "description": "HPX Automation ",
            "milestone_id": hpx_milestone_id
        }
        response = requests.post(base_url + 'add_plan/' + str(441), headers=headers, data=json.dumps(data))

        if response.status_code != 200:
            print("Failed to add plan to milestone. Status code:", response.status_code)
            return None
    
        return response.json()
    
    else:
        for plan in plans_for_milestone:
            if  plan['name'] == plan_name and plan['is_completed'] == False:
                return plan['id']
        
        data = {

            "name":  plan_name,
            "description": "HPX Automation ",
            "milestone_id": hpx_milestone_id
        }
        response = requests.post(base_url + 'add_plan/' + str(441), headers=headers, data=json.dumps(data))
        if response.status_code != 200:
            print("Failed to add plan to milestone. Status code:", response.status_code)
            return None
        return response.json()
        



def get_plan(plan_id):
    response = requests.get(base_url + 'get_plan/' + str(plan_id), headers=headers)
    
    if response.status_code != 200:
        print("Failed to get plan. Status code:", response.status_code)
        return None
    return response.json()




def add_plan_entry():

    exist_test_case = []

    plan_info = add_plan_to_hpx_milestone()
    if type(plan_info) == int:
        plan_id = plan_info
    else:
        plan_id = plan_info["id"]

    plan = get_plan(plan_id)
    runs_in_plan = [entry['runs'] for entry in plan['entries']]
    runs_in_plan_ids = [run['id'] for run_list in runs_in_plan for run in run_list]
    run_name_list = [j['name'] for i in runs_in_plan for j in i]
    entry_id = [j['entry_id'] for i in runs_in_plan for j in i]
    run_name_entry_id = dict(zip(run_name_list, entry_id))
    run_name_run_id = dict(zip(run_name_list, runs_in_plan_ids))

    for name, run_id in run_name_run_id.items():
        if name == run_name + "_" + version:
            response = requests.get(base_url + 'get_tests/' + str(run_id), headers=headers)
            test_info = response.json()
            for tests_id in test_info:
                exist_test_case.append(str(tests_id["case_id"]))
    
    set1 = set(exist_test_case)
    set2 = set(case_id_list)

    all_case_id_list = list(set1 | set2)

    if replacement == "all_replacement_cases" and replacement_cases_list:
        all_case_id_list = replacement_cases_list

    config_id_list = []

    data = {
            "name": run_name + "_" + version,
            "suite_id": suite_id,
            "include_all": False,
            "case_ids": all_case_id_list,
            "runs": [
                {
                    "include_all":False,     
                    "case_ids": all_case_id_list
                }
            ]
        }

    
    if not runs_in_plan:

        response = requests.post(base_url + 'add_plan_entry/' + str(plan_id), headers=headers, data=json.dumps(data))

        if response.status_code != 200:
            print("Failed to get plan. Status code:", response.status_code)

        return response.json()

    
    for runs, entry in run_name_entry_id.items():
        if run_name + "_" + version == runs:
            response = requests.post(base_url + 'update_plan_entry/' + str(plan_id) + "/"  + str(entry), headers=headers, data=json.dumps(data))
            if response.status_code != 200:
                print("Failed to get plan. Status code:", response.status_code)
            return response.json()


    response = requests.post(base_url + 'add_plan_entry/' + str(plan_id), headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        print("Failed to get plan. Status code:", response.status_code)

    return response.json()


def get_tests_id(case_id):

    if production_run_id == "None":
        plan_info = add_plan_to_hpx_milestone()

        if type(plan_info) == int:
            plan_id = plan_info

        else:
            plan_id = plan_info["id"]

        plan = get_plan(plan_id)
        runs_in_plan = [entry['runs'] for entry in plan['entries']]
        runs_in_plan_ids = [run['id'] for run_list in runs_in_plan for run in run_list]
        run_name_list = [j['name'] for i in runs_in_plan for j in i]
        run_name_id = dict(zip(run_name_list, runs_in_plan_ids))

        for name, run_id in run_name_id.items():
            if name == run_name + "_" + version:
                response = requests.get(base_url + 'get_tests/' + str(run_id), headers=headers)
                test_info = response.json()
                for tests_id in test_info:
                    if tests_id['case_id'] == case_id:
                        return tests_id['id']
    else:
        response = requests.get(base_url + 'get_tests/' + str(production_run_id), headers=headers)
        test_info = response.json()
        for tests_id in test_info:
            if tests_id['case_id'] == case_id:
                return tests_id['id']



def log_results_to_testrail():


    if production_run_id == "None":
        add_plan_entry()
    print(1111111111111111111111111)

    for case_id, result in case_id_result.items():

        comment = get_fail_case_comment(case_id)
        test_id = get_tests_id(int(case_id))

        data = {
            "status_id": result,
            "version":version,
            "comment": "Run by Automation" + "\n" + "The platform for testing is: " + platform_name + "\n" + comment
        }

        response = requests.post(base_url + 'add_result/' + str(test_id), headers=headers, data=json.dumps(data))




if __name__ == '__main__':
    log_results_to_testrail()

