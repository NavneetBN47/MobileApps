import os
import re
import sys
import time
import pytest
import logging
import traceback
import base64
import requests
from requests.auth import HTTPBasicAuth

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.ma_misc.conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.one_simulator.printer_simulation import create_simulator_printer_from_api, delete_simulator_printer

from SAF.misc import package_utils
from SAF.misc.ssh_utils import SSH
from SAF.misc.windows_utils import resolve_to_abs_path
from SAF.misc import windows_utils

pytest.platform = "WINDOWS"

def pytest_addoption(parser):
    test_option = parser.getgroup('Windows Test Parameters')
    test_option.addoption("--app-version", action="store", default=None, help="The app version you would like to run")
    test_option.addoption("--app-build", action="store", default=None, help="The build number of the app you would like to run")
    test_option.addoption("--app-update", action="store", default=None, help="Not remove previous app and install the latest app")
    test_option.addoption("--skip-reinstall", action="store_true", default=False, help="Not reinstall app just use installed app")
    test_option.addoption("--skip-app-string", action="store_true", default=False, help="Not remove previous app and install the latest app")
    test_option.addoption("--restart-fusion", action="store_true", default=False, help="Restart fusion before install build")
    test_option.addoption("--ota-build", action="store_true", help="Download OTA old build")

# ----------------      FUNCTION     ---------------------------
@pytest.fixture(scope="session")
def start_driver(request, session_setup, require_driver_session, ssh_client):
    try:
        driver = require_driver_session
        driver.ssh = ssh_client
    except:
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment)
        c_misc.save_screenshot_and_publish(driver, session_attachment+ "/windows_test_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment+ "/", file_name = "windows_test_setup_failed_page_source.txt")
        traceback.print_exc()
        driver.close()
        raise
    return driver

@pytest.fixture(scope="session")
def utility_web_session(request, start_driver, ssh_client):
    ssh = ssh_client
    if request.config.getoption("--mobile-device") is None:
        raise ValueError("You need to pass in mobile-device for this to work.")
    executor_url = request.config.getoption("--mobile-device")
    profile_path = resolve_to_abs_path(ssh, "~/AppData/Local/Google/chrome/") + "User Data"
    ssh.send_command('Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force', raise_e=False)
    web_driver = c_misc.utility_web_driver(browser_type="chrome", executor_url=executor_url, executor_port=4444, profile_path=profile_path, request=request)  
    if request.config.getoption("--performance"):
        web_driver.session_data["performance"] = start_driver.performance
    def close():
        web_driver.close()
        ssh.send_command('Remove-Item -Path ' + w_const.TEST_DATA.CHROME_CACHE_PATH + ' -Recurse -Force')
    request.addfinalizer(close)
    return web_driver
   
@pytest.fixture(scope="session")
def install_app(request, ssh_client):   
    if pytest.app_info == "DESKTOP":
        pytest.default_info = pytest.set_info
    else:
        pytest.default_info = pytest.app_info

    process_name = eval("w_const.PROCESS_NAME." + pytest.default_info)
    ssh = ssh_client

    if request.config.getoption("--skip-reinstall"):
        return ''
    
    ssh.remove_app(process_name, timeout=120)
    
    if request.config.getoption("--ota-build"):
        account = ma_misc.load_system_config_file()["database_info"]["user"]
        password = ma_misc.load_system_config_file()["database_info"]["password"]
        base_url = ma_misc.load_system_config_file()["database_info"]["url"]
        # Get OTA build document id
        doc_url = base_url + "hpx_build_cache/_design/cache_search/_view/by_name?key=\"hpx_ota\""
        doc_response = requests.get(doc_url, auth=HTTPBasicAuth(account, password))
        doc_data = doc_response.json()
        for row in doc_data['rows']:
            document_id = row['id']
        
        #Get attachment file name
        attachment_url = base_url + f"hpx_build_cache/{document_id}/"
        attachment_response = requests.get(attachment_url, auth=HTTPBasicAuth(account, password))
        attachments  = attachment_response.json()["_attachments"]
        attachment_names = list(attachments.keys())
        for name in attachment_names:
            attachment_name = name

        credentials = account + ":" + password
        encoded_credentials = base64.b64encode(credentials.encode('ascii')).decode('ascii')
        app_url = base_url + "hpx_build_cache/" + document_id + "/" + attachment_name
        zip_name = attachment_name
        folder_name = ".".join(zip_name.split(".")[:-1])
        resolved_path = resolve_to_abs_path(ssh, "~/Desktop/")

        result = ssh.send_command("Test-Path " + resolved_path  + folder_name)
        if "True" not in result["stdout"]:
            #Download the app, The file is 300+ mg will take sometime to download depending on speed
            command = (
                f"$ProgressPreference = 'SilentlyContinue'; "
                f"Invoke-WebRequest -Uri '{app_url}' "
                f"-Headers @{{ Authorization = 'Basic {encoded_credentials}' }} "
                f"-OutFile '{resolved_path}{zip_name}'"
            )
            ssh.send_command(command, timeout=1200)
            #Unzip the file
            ssh.send_command("Expand-Archive " + resolved_path + zip_name + " -DestinationPath " + resolved_path + folder_name, timeout=60)
            #Delete the original zip to avoid clutter
            ssh.send_command("Remove-Item " + resolved_path + zip_name)
        
        local_path = ssh.send_command("Resolve-Path \"" + resolved_path + folder_name + "\" | Select -ExpandProperty Path")
        cleaned_path = local_path["stdout"].replace('\n','').replace('\r','')
        result = ssh.send_command("Test-Path " + cleaned_path)
        print("RESO = " + cleaned_path)
        if "True" not in result["stdout"]:
            logging.debug("Install location was not found!")
            raise Exception("Install location was not found, build cannot be installed.")
        else:
            if "PreinstallKit" in cleaned_path:
                arr=ssh.list_all_files_in_remote_dir(cleaned_path)
                for file in arr:                        
                    if ".msixbundle" in file:
                        logging.info(f"File: {file}")
                        bundle_path = cleaned_path + "\\" + file.split("/")[-1]

                        ps_script_path = "C:\\Users\\exec\\Desktop\\install_msix.ps1"
                        ps_content = f'Add-AppxPackage -Path "{bundle_path}" -ForceApplicationShutdown'
                        ssh.send_command(f"Set-Content -Path '{ps_script_path}' -Value '{ps_content}'", timeout=30)

                        ssh.send_command(f'schtasks /create /tn "InstallMsixBundle" /tr "powershell.exe -NoProfile -ExecutionPolicy Bypass -File {ps_script_path}" /sc once /st 00:00 /f', timeout=60)
                        ssh.send_command('schtasks /run /tn "InstallMsixBundle"', timeout=60)

                        max_attempts = 30
                        for _ in range(max_attempts):
                            is_hpx_installed = ssh.send_command("Get-AppxPackage *myHP*")["stdout"]
                            if "AD2F1837.myHP" in is_hpx_installed:
                                app_status = ssh.send_command("Get-AppxPackage *myHP* | Select-Object -ExpandProperty Status")["stdout"]
                                if "Ok" in app_status:
                                    logging.info("App installed successfully")
                                    break
                            time.sleep(5)

                        ssh.send_command('schtasks /delete /tn "InstallMsixBundle" /f', timeout=60)
                        ssh.send_command(f'Remove-Item "{ps_script_path}" -Force', timeout=30, raise_e=False)
                        break                       
            else:
                ssh.send_command(cleaned_path + "\\Install.ps1 -Force", timeout=240)
            return cleaned_path

    elif request.config.getoption("--local-build") is None:
        app_url, zip_name = c_misc.get_package_url(request, _os="WINDOWS", project=pytest.default_info)
        
        folder_name = ".".join(zip_name.split(".")[:-1])
        resolved_path = resolve_to_abs_path(ssh, "~/Desktop/")

        #If the app is already downloaded then just reinstall 
        result = ssh.send_command("Test-Path " + resolved_path  + folder_name)
        if "True" not in result["stdout"]:
            #Download the app, The file is 300+ mg will take sometime to download depending on speed
            ssh.send_command(f"$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest {app_url} -OutFile {resolved_path + zip_name}", timeout=1200)     
            #Unzip the file
            ssh.send_command("Expand-Archive " + resolved_path + zip_name + " -DestinationPath " + resolved_path + folder_name, timeout=60)
            #Delete the original zip to avoid clutter
            ssh.send_command("Remove-Item " + resolved_path + zip_name)
        #Install the App
        try:
            extra_install_ls_result = [x for x in ssh.send_command("ls " + resolved_path + folder_name + " -Name -Attributes Directory")["stdout"].split("\r\n") if eval("w_const.EXTRA_INSTALLER_PATH." + pytest.default_info) in x]
            extra_installer_folder = "\\" + extra_install_ls_result[0] if len(extra_install_ls_result) >= 1 else ""
        except AttributeError:
            extra_installer_folder = ""

        if request.config.getoption("--appbundle-install") is not None:
            msixbundle_file = extra_installer_folder.replace("_Test", "_x64") + ".msixbundle"
            ssh.install_bundle(resolved_path + folder_name + extra_installer_folder + msixbundle_file)
        else:
            app_path = resolved_path + folder_name + extra_installer_folder + '\\Install.ps1'      
            if "REBRAND" in app_path:
                ssh.send_command(f'schtasks /create /tn "InstallAppNow" /tr "powershell.exe -NoProfile -ExecutionPolicy Bypass -File {app_path} -Force" /sc once /st 00:00 /f', timeout=60)   
                ssh.send_command('schtasks /run /tn "InstallAppNow"', timeout=240)
                time.sleep(10)
                file_path = '"C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.myHP_v10z8vjag6ke6\\LocalCache"'
                max_attempts = 60
                for _ in range(max_attempts):
                    file_exist = windows_utils.check_path_exist(ssh, file_path)
                    is_hpx_installed = ssh.send_command("Get-AppxPackage *myHP*")["stdout"]
                    
                    if "AD2F1837.myHP" in is_hpx_installed:
                        app_status = ssh.send_command("Get-AppxPackage *myHP* | Select-Object -ExpandProperty Status")["stdout"]
                        if file_exist and "Ok" in app_status:
                            break
                    time.sleep(10)
                time.sleep(10)
                ssh.send_command('schtasks /delete /tn "InstallAppNow" /f', timeout=60)
            else:
                ssh.install_app(resolved_path + folder_name + extra_installer_folder, retry=5, retry_sleep=30, timeout=180)

            logging.info("Copy SharedSettings.json file into publishers folder to simulate Migration flow for adding printer function.")
            ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/SharedSettings.json"), w_const.TEST_DATA.HPX_SHARED_JSON_PATH + "\\" + "SharedSettings.json")
            
            if "pie" not in request.config.getoption("--stack").lower():
                logging.info("Copy LoggingData.xml and properties.json.dat files to enable logging level for production stack")
                remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
                time.sleep(2)
                ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/properties.json.dat"), remote_artifact_path + "properties.json.dat")
                ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/LoggingData_prod.xml"), remote_artifact_path + "\\Logs\\" + "LoggingData.xml")

        return resolved_path + folder_name + extra_installer_folder
    
    else: 
        app_location = request.config.getoption("--local-build")
        #Install the App
        if request.config.getoption("--appbundle-install") is not None:
            try:
                extra_install_ls_result = [x for x in ssh.send_command("ls " + app_location + " -Name")["stdout"].split("\r\n") if ".msixbundle" in x]
                extra_installer_file = extra_install_ls_result[0]
            except AttributeError:
                extra_installer_file = ""               
            ssh.install_bundle(app_location + "\\" + extra_installer_file)
            return app_location
        else:
            resolved_path = ssh.send_command("Resolve-Path \"" + app_location + "\" | Select -ExpandProperty Path")
            cleaned_path = resolved_path["stdout"].replace('\n','').replace('\r','')
            result = ssh.send_command("Test-Path " + cleaned_path)
            print("RESO = " + cleaned_path)
            if "True" not in result["stdout"]:
                #Warn user that there is no build in the given path
                logging.debug("Install location was not found!")
                raise Exception("Install location was not found, build cannot be installed.")
            else:
                if "PreinstallKit" in cleaned_path:
                    arr=ssh.list_all_files_in_remote_dir(cleaned_path)
                    for file in arr:                        
                        if ".msixbundle" in file:
                            logging.info(f"File: {file}")
                            result = ssh.install_app(cleaned_path + "\\"+ file.split("/")[-1], timeout=180)
                            logging.info(f"Installed app successfully: {result}")
                            break                       
                else:
                    display_version = windows_utils.get_windows_display_version(ssh)
                    if display_version and (display_version[:-2].isdigit() and (int(display_version[:-2]) > 24 or (int(display_version[:-2]) == 24 and display_version[-2:] >= "H2"))):
                        # Your code for version >= 24H2
                        if "production" in request.config.getoption("--stack").lower():
                            ssh.send_command("C:\\Users\\exec\\HPX_Installer\\installer_production.ps1", timeout=240)
                        else:
                            ssh.send_command("C:\\Users\\exec\\HPX_Installer\\installer_itg.ps1", timeout=240)
                    else:
                        ssh.send_command(cleaned_path + "\\Install.ps1 -Force", timeout=240)
                    # ssh.send_command(cleaned_path + "\\Install.ps1 -Force", timeout=240)
                return cleaned_path
            
@pytest.fixture(scope="session")
def ssh_client(request):
    if request.config.getoption("--mobile-device") is None:
        raise ValueError("You need to pass in mobile-device for this to work.")
    ssh = SSH(request.config.getoption("--mobile-device"), "exec")
    def close():
        ssh.close()
    request.addfinalizer(close)
    return ssh

@pytest.fixture(scope="session")
def windows_test_setup(request, ssh_client, install_app, start_driver):
    app_location = request.config.getoption("--local-build")
    if pytest.app_info == "DESKTOP":
        pytest.default_info = pytest.set_info
    else:
        pytest.default_info = pytest.app_info
    driver = start_driver
    ssh = ssh_client
    if request.config.getoption("--restart-fusion"):
        task_utilities = TaskUtilities(ssh_client)
        task_utilities.restart_fusion_service()
    locale = request.config.getoption("--locale")
    installer_package_path = install_app
    driver.session_data["app_info"] = {pytest.default_info: installer_package_path.split("\\")[-1]}
    #Add app string
    if not request.config.getoption("--skip-app-string")and app_location is None:
        driver.load_app_strings(pytest.default_info, locale , package_utils.get_app_string_from_bundle(ssh, installer_package_path, locale, timeout=240))
    driver.session_data["installer_path"] = installer_package_path
    return driver

@pytest.fixture(scope="class")
def load_custom_printer_session(request):
    """
    Custom fixture to load specific printer profile.
    Usage: 
    1. Set printer_profile attribute on test class to use custom printer, e.g., printer_profile = "HP OfficeJet Pro 9130b Series"
    2. If printer_profile is not defined, will use default load_printers_session
    """
    if not hasattr(request.cls, "printer_profile"):
        logging.info("No printer_profile defined in test class, using default load_printers_session")
        return request.getfixturevalue("load_printers_session")
    
    printer_profile = request.cls.printer_profile
    logging.info(f"Using custom printer profile: {printer_profile}")
    
    system_cfg = ma_misc.load_system_config_file()
    
    if "oneSimulator" not in system_cfg or system_cfg["oneSimulator"].get("type") != "server":
        logging.warning(f"printer_profile '{printer_profile}' is defined but oneSimulator is not configured, falling back to load_printers_session")
        return request.getfixturevalue("load_printers_session")
    
    pp_info = system_cfg["oneSimulator"]
    p = create_simulator_printer_from_api(pp_info.get("server_ip"), printer_profile, pp_info.get("isUSB", False))
    
    def clean_up():
        try:
            printer_info = p.get_printer_information()
            delete_simulator_printer(printer_info.get("ip address"), printer_info.get("serial number"))
        except Exception as e:
            logging.info(f"Printer cleanup failed: {e}")
    
    request.addfinalizer(clean_up)
    return p
