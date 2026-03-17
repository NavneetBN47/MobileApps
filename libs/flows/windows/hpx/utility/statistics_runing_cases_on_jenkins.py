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
test_suite_name = environment["WORKSPACE"].split("/")[-1].split(".")[0]
passed_cases = tree.xpath('//*[@class="passed"]/text()')[0].split(" ")[0]
skipped_cases = tree.xpath('//*[@class="skipped"]/text()')[0].split(" ")[0]
failed_cases = tree.xpath('//*[@class="failed"]/text()')[0].split(" ")[0]
error_cases = tree.xpath('//*[@class="error"]/text()')[0].split(" ")[0]

work_space = "/work/exec/workspace/SHI_INTEGRATION_WINDOWS_HPX_FUNCTIONALITY/statistics_cases/"

try: 
   platform_name = environment['PLATFORM'].split('&&')[-1]
except KeyError:
    platform_name = environment['JOB_NAME'].split('&&')[-1]

data = {}

with open(work_space + test_suite_name + "_" + platform_name + ".json", "w") as json_file:
    json.dump(data, json_file, indent=4)

new_data = {
    test_suite_name + "_" + platform_name: {"passed": passed_cases, "skipped": skipped_cases, "failed": failed_cases, "error": error_cases}
}


try:
    with open(work_space + test_suite_name + "_" + platform_name + ".json", "r") as json_file:
        existing_data = json.load(json_file)
except FileNotFoundError:
    existing_data = {}


for key in new_data:
    if key in existing_data:
        for sub_key in new_data[key]:
            if sub_key in existing_data[key]:
                existing_data[key][sub_key] += new_data[key][sub_key]
            else:
                existing_data[key][sub_key] = new_data[key][sub_key]
    else:
        existing_data[key] = new_data[key]


with open(work_space + test_suite_name + "_" + platform_name + ".json", "w") as json_file:
    json.dump(existing_data, json_file, indent=4)


def write_json_data_to_txt(folder_path, txt_file_path):
    with open(txt_file_path, 'w') as txt_file:
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            if filename.endswith('.json') and os.path.isfile(filepath):
                with open(filepath, 'r') as json_file:
                    data = json.load(json_file)
                    for key, value in data.items():
                        line = f"{key}  {value['passed']}  {value['skipped']}  {value['failed']}  {value['error']}\n"
                        txt_file.write(line)


folder_path = '/work/exec/workspace/SHI_INTEGRATION_WINDOWS_HPX_FUNCTIONALITY/statistics_cases'

txt_file_path = '/work/exec/workspace/SHI_INTEGRATION_WINDOWS_HPX_FUNCTIONALITY/statistics_cases/cases_results.txt'

write_json_data_to_txt(folder_path, txt_file_path)