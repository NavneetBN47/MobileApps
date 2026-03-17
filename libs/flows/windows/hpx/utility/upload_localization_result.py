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
parser.add_argument('--case_id',action='store_true')
parser.add_argument('file')
parser.add_argument('xml_file')
parser.add_argument('case_id')
report_file = str(parser.parse_args().file)
report_file_xml = str(parser.parse_args().xml_file)
case_id = parser.parse_args().case_id
case_id_list = [int(x.strip()) for x in case_id.split(',')]

xml_tree = ET.parse(report_file_xml)
xml_root = xml_tree.getroot()

testsuite = xml_root.find('testsuite')
fail_case_language = []
fail_case_reason = []


for testcase in testsuite:
    for fail_case in testcase:
        if fail_case.tag == "failure" or fail_case.tag == "error":
            fail_case_reason.append(fail_case.get('message'))
            fail_case = str(testcase.attrib)
            if "screenshot" in fail_case:
                pattern = r'screenshot-([a-zA-Z]+(?:-[a-zA-Z]+)*)'
            else:
                pattern = r'\[([a-zA-Z-]+)\]'
            result = re.search(pattern, fail_case)
            try:
                fail_case_result = result.group(1)
                fail_case_language.append(fail_case_result)
                break
            except:
                fail_case_result = " "

languages_fail_result = dict(zip(fail_case_language, fail_case_reason))


def get_fail_case_comment(config_lanuage):

    if not languages_fail_result:
        comment = " "
        return comment

    for language, fail_result in languages_fail_result.items():

        if language.upper() == config_lanuage:
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
platform_name = environment['PLATFORM'].split('&&')[2:][-1]


logs = []
for v in tree.xpath('//tbody[contains(@class, "results-table-row")]'):
    log = {
        "log": v.xpath('.//*[@class="log"]/text()')
    }
    logs.append(log)


for i in logs:
    v_str = ''.join(i["log"]).replace("\n", "")
    if "RESO = " in v_str:
        pattern = r'C:\\Users\\exec\\Desktop\\(.*?)_TRACK'
    else:
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




def get_hpx_automation_milestone_id():

    today = datetime.date.today()
    response = requests.get(base_url + 'get_milestones/' + str(441), headers=headers)
    
    if response.status_code != 200:
        print("Failed to get plan. Status code:", response.status_code)
        return None

    milestones = response.json()

    for milestone in milestones:
        if milestone['id'] == 16781:
            for i in milestone["milestones"]:
                pattern = str(today.strftime('%B'))
                match = re.match(pattern, i['name'])
                if match:
                    id = i["id"]

    return id




def get_plans_for_hpx_milestone():
    milestone_id = get_hpx_automation_milestone_id()


    response = requests.get(base_url + 'get_plans/' + str(441), headers=headers)
    
    if response.status_code != 200:
        print("Failed to get plan. Status code:", response.status_code)
        return None
    
    all_plans = response.json()
    plans_for_milestone = [plan for plan in all_plans if plan['milestone_id'] == milestone_id]


    return plans_for_milestone



def add_plan_to_hpx_milestone():

    for i in results:
        version = str(i["Version"])
        break
        

    date = str(datetime.date.today()).replace('-', '_')
    plans_for_milestone = get_plans_for_hpx_milestone()
    if len(plans_for_milestone) == 0:
        milestone_id = get_hpx_automation_milestone_id()
        
        data = {
            "name": "[Automation][HPX][WinClient] Localization_" + version,
            "description": "HPX Localization Automation ",
            "milestone_id": milestone_id
        }
        response = requests.post(base_url + 'add_plan/' + str(441), headers=headers, data=json.dumps(data))

        if response.status_code != 200:
            print("Failed to add plan to milestone. Status code:", response.status_code)
            return None
    
        return response.json()
    
    else:
        for plan in plans_for_milestone:
            if  plan['name'] == "[Automation][HPX][WinClient] Localization_" + version and plan['is_completed'] == False:
                return plan['id']
        
        milestone_id = get_hpx_automation_milestone_id()
        data = {

            "name": "[Automation][HPX][WinClient] Localization_" + version,
            "description": "HPX Localization Automation ",
            "milestone_id": milestone_id
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

    plan_info = add_plan_to_hpx_milestone()

    if type(plan_info) == int:
        plan_id = plan_info
    else:
        plan_id = plan_info["id"]

    plan = get_plan(plan_id)
    runs_in_plan = [entry['runs'] for entry in plan['entries']]
    
    if not runs_in_plan:

        test_case_amount = []

        platform_name = environment['PLATFORM'].split('&&')[2:][-1]
        if platform_name == "grogu492":
            platform_name = "grogu"

        for i in results:
            pattern = r'test_\d{2}_(.*?)_localization.py'
            match = re.search(pattern, str(i["Test"]))
            if match:
                module = match.group(1)
                test_case_amount.append(module)


        plan_info = add_plan_to_hpx_milestone()

        if type(plan_info) == int:
            plan_id = plan_info

        else:
            plan_id = plan_info["id"]


        config_id_list = [12242, 12243, 12244, 12245, 12246, 12247, 12248, 12249, 11294, 12250, 12251, 12252, 12253, 12254, 12255, 12256, 12257, 12258, 12259, 12260, 13284, 12261, 12262, 12263, 12264, 12265, 12266, 12267, 12268, 12269, 12270, 12271, 12272, 12273, 12274, 12275, 12276, 12277, 12278, 12279, 12280, 12281, 12282]
        if len(test_case_amount) == 1:
            config_id_list = [11294]

        data = {
                "name": "hpx_win_localization",
                "suite_id": 58419,
                "include_all": False,
                "case_ids": case_id_list,
                "config_ids": config_id_list,
                "runs": [

                ]
            }

        
        for i in range(len(config_id_list)):
            runs = {"include_all": False, "case_ids": case_id_list, "config_ids": [config_id_list[i]]}
            data["runs"].append(runs)
        
        response = requests.post(base_url + 'add_plan_entry/' + str(plan_id), headers=headers, data=json.dumps(data))

        if response.status_code != 200:
            print("Failed to get plan. Status code:", response.status_code)

        return response.json()


def get_config_case_id():

    for i in results:
        case_id_pattern = r'_C(\d+)'
        match_case_id = re.search(case_id_pattern, str(i["Test"]))
        if match_case_id:
            case_id = match_case_id.group(1)
    case_id_list = [case_id for _ in range(43)]
    plan_info = add_plan_to_hpx_milestone()

    if type(plan_info) == int:
        plan_id = plan_info

    else:
        plan_id = plan_info["id"]

    plan = get_plan(plan_id)
    runs_in_plan = [entry['runs'] for entry in plan['entries']]
    runs_in_plan_ids = [run['id'] for run_list in runs_in_plan for run in run_list]
    runs_in_plan_config = [run['config'] for run_list in runs_in_plan for run in run_list]
    config_case_id = dict(zip(runs_in_plan_config, case_id_list))
    return config_case_id
    

def get_tests_id(language, case_id):

    plan_info = add_plan_to_hpx_milestone()

    if type(plan_info) == int:
        plan_id = plan_info

    else:
        plan_id = plan_info["id"]

    plan = get_plan(plan_id)
    runs_in_plan = [entry['runs'] for entry in plan['entries']]
    runs_in_plan_ids = [run['id'] for run_list in runs_in_plan for run in run_list]
    runs_in_plan_config = [run['config'] for run_list in runs_in_plan for run in run_list]
    config_run_id = dict(zip(runs_in_plan_config, runs_in_plan_ids))
    
    for config, run_id in config_run_id.items():
        if config == language:
            response = requests.get(base_url + 'get_tests/' + str(run_id), headers=headers)
            test_info = response.json()
            for tests_id in test_info:
                if tests_id['case_id'] == case_id:
                    return tests_id['id']



def log_results_to_testrail():

    if version != "no version in this build log":
    
        add_plan_entry()
        config_cases_id = get_config_case_id()

        languages_list = []
        result_list = []


        for i in results:
            if "screenshot" in str(i['Test']):
                language_pattern = r'screenshot-([a-zA-Z]+(?:-[a-zA-Z]+)*)'
            else:
                language_pattern = r'\[([a-zA-Z-]+)\]'

            match = re.search(language_pattern, str(i['Test']))
            if match:
                languages_list.append(match.group(1).upper())
                
            result_pattern = r'[A-Za-z]+'
            match = re.search(result_pattern, str(i['Result']))
            if match:
                result_list.append(match.group())
        
        for i in range(len(result_list)):
            if result_list[i] == "Failed" or result_list[i] == "Error":
                result_list[i] = 5
            else:
                result_list[i] = 1
        
        
        languages_result = dict(zip(languages_list, result_list))

        for language, result in languages_result.items():
            for config, case_id in config_cases_id.items():
                if language == config:
                    comment = get_fail_case_comment(config)
                    test_id = get_tests_id(config, int(case_id))
                    data = {
                        "status_id": result,
                        "version":version,
                        "comment": "The platform for testing is: " + platform_name + "\n" + comment
                    }

                    response = requests.post(base_url + 'add_result/' + str(test_id), headers=headers, data=json.dumps(data))
                    break





if __name__ == '__main__':
    log_results_to_testrail()

