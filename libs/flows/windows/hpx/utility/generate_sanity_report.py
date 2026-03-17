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

results_dir = "/work/exec/workspace/SHI_WINDOWS_HPX_INTEGRATION/sanity_results/"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

version_list = [version]
display_data_results = []
for item in version_list:
    html_results = {
        "Version": item,
    }
    display_data_results.append(html_results)
    

env = Environment(loader=FileSystemLoader('/work/exec/shanghai/MobileApps/resources/test_data/hpx/report_template/'))
template = env.get_template('sanity_report_template.html')
report = template.render(data=display_data_results)



with open("/work/exec/workspace/SHI_WINDOWS_HPX_INTEGRATION/sanity_results/sanity_results.html", 'w') as f:
    f.write(report)
    f.close()