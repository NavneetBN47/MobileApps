import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
from lxml import html
from lxml import etree
import re
import argparse
import json
import os

parser = argparse.ArgumentParser()
parser.add_argument('--f', action='store_true')
parser.add_argument('file')
report_file = str(parser.parse_args().file)



with open(report_file, "r") as f:
    tree = html.fromstring(f.read())


report_time = tree.xpath('//p[contains(text(), "Report generated")]/text()')
summary = tree.xpath('//p[contains(text(), "tests ran in")]/text()')
environment = {el[0].text: el[1].text for el in tree.xpath('//table[@id="environment"]//tr')}
stack = str(tree.xpath('//h1/text()')).split(",")[0].split("=")[-1]
platform = environment["WORKSPACE"].split("/")[-1]

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
        version = result.group(1).split("_")[0]
        break
    except:
        version = "no version in this build log"



results = ""
for row in tree.xpath('//tbody[contains(@class, "results-table-row")]/tr'):
    if row.xpath('.//td[@class="col-result"]/text()') != []:
        if row.xpath('.//td[@class="col-result"]/text()') ==  ['Failed'] or row.xpath('.//td[@class="col-result"]/text()') == ['Error']:
            results = "Failed"
            break
        else:
            results = "Passed"



results_dir = "/work/exec/workspace/SHI_WINDOWS_HPX_MAT/mat_results/"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

try:
    with open("/work/exec/workspace/SHI_WINDOWS_HPX_MAT/mat_results/" + platform + '_results.txt', 'r') as file:
        result_dict = json.load(file)
except FileNotFoundError:
    result_dict = {"pie": "Passed", "stage": "Passed", "production": "Passed"}

try:
    with open("/work/exec/workspace/SHI_WINDOWS_HPX_MAT/mat_results/" + 'stack_version.txt', 'r') as file:
        version_dict = json.load(file)
except FileNotFoundError:
    version_dict = {"pie": "None", "stage": "None", "production": "None"}

result_dict[stack] = results
version_dict[stack] = version

with open("/work/exec/workspace/SHI_WINDOWS_HPX_MAT/mat_results/" + platform + '_results.txt', 'w') as file:
    json.dump(result_dict, file)

with open("/work/exec/workspace/SHI_WINDOWS_HPX_MAT/mat_results/" + 'stack_version.txt', 'w') as file:
    json.dump(version_dict, file)

result_tuples = []
version_tuples = []

    
folder_path = "/work/exec/workspace/SHI_WINDOWS_HPX_MAT/mat_results/"

for file_name in os.listdir(folder_path):
    if file_name.endswith("results.txt"):
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'r') as file:
            try:

                file_data = json.load(file)
                
                for key, value in file_data.items():
                    result_tuple = (file_name.replace("_results.txt", ""), key, value)
                    result_tuples.append(result_tuple)
                    
            except json.JSONDecodeError:
                print(f"Invalid JSON format in file: {file_path}")


with open(folder_path + "stack_version.txt", 'r') as file:
    try:
        version_data = json.load(file)
        version_tuples.append(version_data)
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file")


display_data_results = []
for item in result_tuples:
    html_results = {
        "configurationMatrix": item[0],
        "stack": item[1],
        "result": item[2],
    }
    display_data_results.append(html_results)
    

env = Environment(loader=FileSystemLoader('/work/exec/shanghai/MobileApps/resources/test_data/hpx/report_template/'))
template = env.get_template('report_template.html')
report = template.render(data=display_data_results,  additional_data=version_tuples)



with open("/work/exec/workspace/SHI_WINDOWS_HPX_MAT/mat_results/mat_results.html", 'w') as f:
    f.write(report)
    f.close()