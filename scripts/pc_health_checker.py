import time
import requests
import subprocess
from datetime import datetime
from multiprocessing import Pool
from SAF.misc.ssh_utils import SSH

now = datetime.now()
print(now)

jenkins_url = "http://hppsrv2.sdg.rd.hpicorp.net:8080"
grid_url = "http://ps0immshwin20.scs.rd.hpicorp.net:4444"
host_name_list = ["HOST-tgtwinftc1.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc02.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc03.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc04.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc05.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc06.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc08.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc09.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc10.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc11.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc12.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc13.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc14.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc16.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc17.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc18.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc19.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc20.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc21.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc22.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc23.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc24.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc26.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc27.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc28.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc29.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc30.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc32.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc33.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc34.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc36.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc46.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc57.tgt.ftc.rd.hpicorp.net",
                  "tgtwinftc59.tgt.ftc.rd.hpicorp.net",
                  "PS0IMMSHWIN06.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN08.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN11.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN12.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN13.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN14.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN15.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN16.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN17.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN18.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN20.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN21.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN22.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN23.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN24.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN25.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN26.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN27.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN28.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN29.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN30.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN31.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN32.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN33.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN34.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN35.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN36.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN37.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN38.scs.rd.hpicorp.net",
                  "PS0IMMSHWIN39.scs.rd.hpicorp.net",                  
                  ]


def get_jenkins_nodes():
    jenkins_nodes = requests.get(jenkins_url + "/computer/api/json").json()["computer"]
    jenkins_node_dict = {}
    for node in jenkins_nodes:
        for label in node["assignedLabels"]:
            if label["name"] in ["shanghai", "fortcollins"]:
                jenkins_node_dict[node["displayName"]] = {"status": "offline" if node["temporarilyOffline"] else "online", "location": label["name"]}                
    return jenkins_node_dict

def check_node_status(host, status="online"):
    if host in jenkins_nodes_dict.keys():
        return jenkins_nodes_dict[host]["status"] == status
    else:
        print(f"Host: {host} is not in Jenkins")
        return None


grid_node_not_in_host_list = ""
host_not_in_grid_node_list = ""
cannot_connect_to_host_list = ""
host_with_duplicated_ip = ""
jenkins_nodes_dict = get_jenkins_nodes()

ip_dict = {}
print(f"Total Jenkins Machine: {len(jenkins_nodes_dict.keys())}")
print(f"Total Listed Machine: {len(host_name_list)}")
grid_status = requests.get(grid_url + "/status").json()["value"]["nodes"]
grid_node_list = []
for node in grid_status:
    node_host = node["slots"][0]["stereotype"]["appium:deviceName"]
    grid_node_list.append(node_host)
    if node_host not in host_name_list:
        grid_node_not_in_host_list += "Node not in host list: " + node_host + "\n"
grid_node_list.sort()

print(f"Total Grid Machine: {len(grid_node_list)}")

def node_health_check(host):
    bad_node = False
    if host not in grid_node_list:
        bad_node = True
        print("Host not in grid: " + host + "\n")
        if check_node_status(host, status="online"):
            #Turn off the node
            print(f"Turning off node {host}")
            subprocess.check_call(f"/qama/framework/bin/jenkins_node_api.py --node {host} --disable".split(" "))
    
    for _ in range(8):  
        connected = False     
        try:
            ssh = SSH(host, username="exec", timeout=7)
            connected = True
            break
        except:
            time.sleep(30)
            
    if not connected:
        print("Failed to connect to host: " + host + "\n")
        bad_node = True
        if check_node_status(host, status="online"):
            #Turn off the node
            print(f"Turning off node {host}\n")
            subprocess.check_call(f"/qama/framework/bin/jenkins_node_api.py --node {host} --disable".split(" "))
        return 
    ssh.close()
    output = subprocess.check_output(["nslookup", host]).decode("utf-8")
    ip = output.split("\n")[-3].split("Address: ")[1]
    if ip in ip_dict.values():
        bad_node = True
        print(f"Hostname: {host} have Duplicate IP: {ip}\n")
        if check_node_status(host, status="online"):
            #Turn off the node
            print(f"Turning off node {host}\n")
            subprocess.check_call(f"/qama/framework/bin/jenkins_node_api.py --node {host} --disable".split(" "))
    ip_dict[host] = ip
    if check_node_status(host, status="offline") and not bad_node:
        #Turn on the node
        print(f"Turning on node {host}\n")
        subprocess.check_call(f"/qama/framework/bin/jenkins_node_api.py --node {host} --enable".split(" "))

print(time.time())
with Pool(10) as p:
    p.map(node_health_check, host_name_list)
print(time.time())

