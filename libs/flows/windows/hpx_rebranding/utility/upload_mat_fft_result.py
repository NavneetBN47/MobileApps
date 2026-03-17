import base64
import json
import datetime
import requests
import time
from functools import wraps


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
parser.add_argument('--test_run_id',action='store_true')
parser.add_argument('file')
parser.add_argument('xml_file')
parser.add_argument('milestone_id')
parser.add_argument('suites_id')
parser.add_argument('test_plan')
parser.add_argument('test_run')
parser.add_argument('test_run_id')

report_file = str(parser.parse_args().file)
report_file_xml = str(parser.parse_args().xml_file)
hpx_rebrand_milestone_id = int((parser.parse_args().milestone_id))
suite_id = int((parser.parse_args().suites_id))
plan_name = str(parser.parse_args().test_plan)
production_run_id = str(parser.parse_args().test_run_id)
run_name = str(parser.parse_args().test_run)


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


try:
    platform_name = tree.xpath('//h1/text()')[0].split(',')[0].split('&&')[-1]
    if "STACK=" in platform_name:
        platform_name = tree.xpath('//h1/text()')[0].split(',')[2].split('=')[1].split('.')[0].split('&&')[-1].split("_")[0]
except Exception as e:
    platform_name = "None"


version = "no version in this build log"


logs = []
for v in tree.xpath('//tbody[contains(@class, "results-table-row")]'):
    log = {
        "log": v.xpath('.//*[@class="log"]/text()')
    }
    logs.append(log)


for i in logs:
    v_str = ''.join(i["log"]).replace("\n", "")
    pattern = r'App Info: (.*?)\.zip'
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



def retry_api_call(max_retries=5, delay=5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            last_error = None
            while retries < max_retries:
                try:
                    response = func(*args, **kwargs)
                    
                    if hasattr(response, 'status_code'):
                        if response.status_code == 200:
                            return response.json()
                        last_error = f"API call failed with status code {response.status_code}"
                    else:
                        return response
                except Exception as e:
                    last_error = str(e)
                    print(f"API call failed with error: {last_error}. Retrying...")
                
                retries += 1
                if retries < max_retries:
                    time.sleep(delay)
            
            raise Exception(f"API call failed after {max_retries} attempts. Last error: {last_error}")
        return wrapper
    return decorator

@retry_api_call()
def get_plans_for_hpx_milestone_api():
    return requests.get(base_url + 'get_plans/' + str(441), headers=headers)

@retry_api_call()
def add_plan_to_hpx_milestone_api(data):
    return requests.post(base_url + 'add_plan/' + str(441), headers=headers, data=json.dumps(data))

@retry_api_call()
def get_plan_api(plan_id):
    return requests.get(base_url + 'get_plan/' + str(plan_id), headers=headers)

@retry_api_call()
def add_plan_entry_api(plan_id, data):
    return requests.post(base_url + 'add_plan_entry/' + str(plan_id), headers=headers, data=json.dumps(data))

@retry_api_call()
def update_plan_entry_api(plan_id, entry, data):
    return requests.post(base_url + 'update_plan_entry/' + str(plan_id) + "/" + str(entry), headers=headers, data=json.dumps(data))

@retry_api_call()
def get_tests_api(run_id):
    return requests.get(base_url + 'get_tests/' + str(run_id), headers=headers)

@retry_api_call()
def add_result_api(test_id, data):
    return requests.post(base_url + 'add_result/' + str(test_id), headers=headers, data=json.dumps(data))

@retry_api_call()
def get_plans_for_hpx_milestone():
    plans = get_plans_for_hpx_milestone_api()
    if plans is None:
        raise Exception("Failed to get plans for milestone")
    
    plans_for_milestone = [plan for plan in plans if plan['milestone_id'] == hpx_rebrand_milestone_id]
    return plans_for_milestone

@retry_api_call()
def add_plan_to_hpx_milestone():
    for i in results:
        version = str(i["Version"])
        break
        
    date = str(datetime.date.today()).replace('-', '_')
    plans_for_milestone = get_plans_for_hpx_milestone()
    
    if not plans_for_milestone:
        data = {
            "name": plan_name,
            "description": "HPX Automation ",
            "milestone_id": hpx_rebrand_milestone_id
        }
        response = add_plan_to_hpx_milestone_api(data)
        return response
    
    else:
        for plan in plans_for_milestone:
            if plan['name'] == plan_name and plan['is_completed'] == False:
                return plan['id']
        
        data = {
            "name": plan_name,
            "description": "HPX_Rebrand Automation ",
            "milestone_id": hpx_rebrand_milestone_id
        }
        response = add_plan_to_hpx_milestone_api(data)
        return response

@retry_api_call()
def get_plan(plan_id):
    response = get_plan_api(plan_id)
    if response is None:
        raise Exception(f"Failed to get plan {plan_id}")
    return response

@retry_api_call()
def add_plan_entry():
    exist_test_case = []
    plan_info = add_plan_to_hpx_milestone()
    
    plan_id = plan_info['id'] if isinstance(plan_info, dict) else plan_info
    
    plan = get_plan(plan_id)
    if plan is None:
        raise Exception(f"Failed to get plan {plan_id}")


    entries = plan.get('entries', [])
    runs_in_plan = [entry.get('runs', []) for entry in entries]
    runs_in_plan_ids = [run['id'] for run_list in runs_in_plan for run in run_list if 'id' in run]
    run_name_list = [run.get('name', '') for run_list in runs_in_plan for run in run_list]
    entry_id = [run.get('entry_id', '') for run_list in runs_in_plan for run in run_list]
    
    run_name_entry_id = dict(zip(run_name_list, entry_id))
    run_name_run_id = dict(zip(run_name_list, runs_in_plan_ids))

    for name, run_id in run_name_run_id.items():
        if name == run_name + "_" + version:
            tests = get_tests_api(run_id)
            if tests is None:
                continue
            for test in tests:
                if 'case_id' in test:
                    exist_test_case.append(str(test['case_id']))
    
    set1 = set(exist_test_case)
    set2 = set(case_id_list)
    all_case_id_list = list(set1 | set2)

    data = {
        "name": run_name + "_" + version,
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
    
    if not runs_in_plan:
        response = add_plan_entry_api(plan_id, data)
        if response is None:
            raise Exception("Failed to add plan entry")
        return response
    
    for runs, entry in run_name_entry_id.items():
        if run_name + "_" + version == runs:
            response = update_plan_entry_api(plan_id, entry, data)
            if response is None:
                raise Exception("Failed to update plan entry")
            return response

    response = add_plan_entry_api(plan_id, data)
    if response is None:
        raise Exception("Failed to add plan entry")
    return response

@retry_api_call()
def get_tests_id(case_id):
    if production_run_id == "None":
        plan_info = add_plan_to_hpx_milestone()
        plan_id = plan_info['id'] if isinstance(plan_info, dict) else plan_info

        plan = get_plan(plan_id)
        if plan is None:
            raise Exception("Failed to get plan")

        entries = plan.get('entries', [])
        runs_in_plan = [entry.get('runs', []) for entry in entries]
        runs_in_plan_ids = [run['id'] for run_list in runs_in_plan for run in run_list if 'id' in run]
        run_name_list = [run.get('name', '') for run_list in runs_in_plan for run in run_list]
        run_name_id = dict(zip(run_name_list, runs_in_plan_ids))

        target_run_id = None
        for name, run_id in run_name_id.items():
            if name == run_name + "_" + version:
                target_run_id = run_id
                break
        
        if target_run_id is None:
            raise Exception(f"Run not found for {run_name}_{version}")

        tests = get_tests_api(target_run_id)
        if tests is None:
            raise Exception(f"Failed to get tests for run {target_run_id}")

        for test in tests:
            if test.get('case_id') == case_id:
                test_id = test.get('id')
                if test_id is not None:
                    return test_id
                
        raise Exception(f"Test ID not found for case {case_id} in run {target_run_id}")
    else:
        tests = get_tests_api(production_run_id)
        if tests is None:
            raise Exception(f"Failed to get tests for production run {production_run_id}")
            
        for test in tests:
            if test.get('case_id') == case_id:
                test_id = test.get('id')
                if test_id is not None:
                    return test_id
        
        raise Exception(f"Test ID not found for case {case_id} in production run {production_run_id}")



def log_results_to_testrail():
    if version == "no version in this build log":
        print("No valid version found in build log")
        return

    max_retries = 5
    failed_cases = [] 

    for attempt in range(max_retries):
        try:
            if production_run_id == "None":
                add_plan_entry()

            current_failed_cases = []  
            for case_id, result in case_id_result.items():
                try:
                    comment = get_fail_case_comment(case_id)
                    test_id = get_tests_id(int(case_id))
                    
                    if test_id is None:
                        raise Exception(f"Test ID not found for case {case_id}")

                    data = {
                        "status_id": result,
                        "version": version,
                        "comment": "Run by Automation" + "\n" + 
                                  "The platform for testing is: " + platform_name + "\n" + 
                                  comment
                    }

                    response = requests.post(base_url + 'add_result/' + str(test_id), 
                                          headers=headers, 
                                          data=json.dumps(data))
                    
                    if response.status_code != 200:
                        raise Exception(f"Failed to add result. Status code: {response.status_code}")

                except Exception as e:
                    print(f"Error processing case {case_id}: {str(e)}")
                    current_failed_cases.append(case_id)  
                    continue  

            if current_failed_cases:  
                print(f"Failed to process cases: {current_failed_cases}")
                failed_cases = current_failed_cases
                raise Exception("Some cases failed to process") 
            
            print("All cases processed successfully")
            break

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt == max_retries - 1:
                print(f"Failed after {max_retries} attempts. Failed cases: {failed_cases}")
            else:
                print("Retrying from the beginning...")
                time.sleep(6)


if __name__ == '__main__':
    log_results_to_testrail()

