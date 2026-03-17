import logging
import requests
import argparse
from datetime import datetime
from SAF.misc.ssh_utils import SSH

parser = argparse.ArgumentParser(description="Parameter for chrome updater")
parser.add_argument("--reboot", action="store_true", default=False, help="Reboot the machine or not after updating the driver")
args = parser.parse_args()



def extract_version_registry(output):
    try:
        google_version = ''
        for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
            if letter !='\n':
                google_version += letter
            else:
                break
        return (google_version.strip())
    except TypeError:
        return

def get_chrome_version(ssh):
    output = ssh.send_command('REG QUERY "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')["stdout"]
    return extract_version_registry(output)

def download_chromedriver(ssh, version):
    '''
    If you are using Chrome version 115 or newer, please consult the Chrome for Testing availability dashboard. This page provides convenient JSON endpoints for specific ChromeDriver version downloading.
    '''
    if int(version) < 115:
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_' + version
        response = requests.get(url)
        version_number = response.text

        zip_name = "chromedriver_win32.zip"
        download_url = "https://chromedriver.storage.googleapis.com/" + version_number + "/" + zip_name
    else:
        url = "https://googlechromelabs.github.io/chrome-for-testing/latest-versions-per-milestone.json"
        response = requests.get(url)
        json_data = response.json()

        version_number = json_data.get('milestones')[version]['version']
        
        zip_name = "chromedriver-win32.zip"
        download_url = "https://storage.googleapis.com/chrome-for-testing-public/" + version_number + "/win32/" + zip_name


    saved_path = "C:\\Users\\exec\\Desktop\\"
    folder_name = ".".join(zip_name.split(".")[:-1])
    ssh.windows_remote_download(download_url, saved_path + zip_name, timeout=120)
    # Unzip the file and delete zip package.
    if int(version) < 115:
        ssh.send_command("Expand-Archive " + saved_path + zip_name + " -DestinationPath " + saved_path + folder_name + " -Force", timeout=60)
    else:    
        ssh.send_command("Expand-Archive " + saved_path + zip_name + " -DestinationPath " + saved_path + " -Force", timeout=60)
    
    ssh.send_command("Remove-Item " + saved_path + zip_name)
    # Rename the original chromedriver with the old version.
    old_chromedriver_v = ssh.send_command("chromedriver --version")["stdout"].split(" ")[1].split(".")[0]

    if 'True' in ssh.send_command('Test-Path -Path "C:\\qama\\tools\\bin\\chromedriver_{}.exe"'.format(old_chromedriver_v))["stdout"]:
        ssh.send_command('Remove-Item -Path "C:\\qama\\tools\\bin\\chromedriver_{}.exe" -Force'.format(old_chromedriver_v))
    ssh.send_command('Rename-Item -Path "C:\\qama\\tools\\bin\\chromedriver.exe" -NewName ' + 'chromedriver_' + str(old_chromedriver_v) + '.exe' + ' -Force')
    # Copy the new chromedriver into the specific folder.
    ssh.send_command("Copy-Item " + saved_path + folder_name + "\chromedriver.exe" + " -Destination " + "C:\\qama\\tools\\bin\\chromedriver.exe")
    return version_number

def clear_desktop_package(ssh):
    output = [x for x in ssh.send_command("ls c:/Users/exec/Desktop | select Mode, LastWriteTime, Name, Length")["stdout"].split("\r\n") if x != '' ][3:]
    now = datetime.today()
    for file in output:
        stat = " ".join(file.split()).split(" ")
        time = datetime.strptime(stat[1], '%m/%d/%Y')
        if (now - time).days > 7:
            file_name = stat[4]
            print(f"Removing {file_name} from {ssh.address}")
            ssh.send_command("Remove-Item -r " + "c:/Users/exec/Desktop/" + file_name)
        
host_list = [
    "tgtwin4d",
    "tgtwin5d",
    "tgtwin6d",
    "tgtwin7d",
    "tgtwin8d",
    "tgtwin80d",
    "tgtwin10p",
    "tgtwin11i",
    "tgtwin12p",
    "tgtwin13i",
    "tgtwin14p",
    "tgtwin15i",
    "tgtwin16p",
    "tgtwin17i",
    "tgtwin18p",
    "tgtwin19i",
    "tgtwin20p",
    "tgtwin21i",
    "tgtwin22p",
    "tgtwin23i",
    "tgtwin10m",
    "tgtwin11m",
    "tgtwinweb1i", 
    "tgtwinweb2p",
]

for host in host_list:
    mismatch = "False"
    try:
        print(f"Checking Host: {host}...")
        ssh = SSH(host, "exec")
        clear_desktop_package(ssh)
        chrome_v_original = get_chrome_version(ssh)
        chrome_v = chrome_v_original.split(".")[0]
        chromedriver_v = ssh.send_command("chromedriver --version")["stdout"].split(" ")[1]
        if chrome_v != chromedriver_v.split(".")[0]:
            mismatch = "True"
            version_number = download_chromedriver(ssh, chrome_v)
            print(f"Host: {host} | Chrome Version: {chrome_v_original} | Chromedriver Version: {chromedriver_v} | Mismatch: {mismatch} | Download Chromedriver Version: {version_number}")
        else:
            print(f"Host: {host} | Chrome Version: {chrome_v_original} | Chromedriver Version: {chromedriver_v} | Mismatch: {mismatch}")
        if args.reboot:
            ssh.send_command("Restart-Computer -f")
        else:
            ssh.close()
    except Exception as e:
        logging.warning(f"Unable to connect the target windows {host}: " + str(e))

    