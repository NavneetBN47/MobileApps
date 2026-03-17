import pytest
import subprocess
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.resources.const.ios.const import BUNDLE_ID
from MobileApps.libs.flows.mac.smart.utility import smart_utilities


# IOS
@pytest.fixture(scope="function", autouse=True)
def ios_smart_get_app_log(request):
    if pytest.platform == "IOS":
        fc = request.cls.fc
        driver = request.cls.driver
        def get_app_log():
            attachment_root_path = c_misc.get_attachment_folder()
            c_misc.save_ios_app_log_and_publish(fc, driver, attachment_root_path, request.node.name)  
        request.addfinalizer(get_app_log)

# MAC
@pytest.fixture(scope="session", autouse=True)
def install_catalyst(request, ssh_client):
    if pytest.platform == "MAC":
        if pytest.app_info == "DESKTOP":
            pytest.default_info = pytest.set_info
        else:
            pytest.default_info = pytest.app_info
        ssh = ssh_client
        resolved_path = ssh.send_command("echo ~/Downloads/")["stdout"].strip()
        application_path = ssh.send_command("echo ~/Applications/")["stdout"].strip()
        app_url, zip_name = c_misc.get_package_url(request, _os="MAC", project=pytest.default_info)
        # app_unzipped_folder_name = f"{application_path}{zip_name[:-4]}.app"
        app_unzipped_folder_name = f"{application_path}HP\ Smart.app"
        result = ssh.check_file(app_unzipped_folder_name)
        if not result:
            smart_utilities.clean_cataylst_cached_data(ssh)
            #Delete old app copy
            ssh.send_command(f"rm -rf {application_path}*.app", timeout=40, raise_e=False)
            #Download the app, The file is 300+ mg will take sometime to download depending on speed
            ssh.send_command(f"curl {app_url} --output {resolved_path}{zip_name}", timeout=900)
            #Unzip the file
            ssh.send_command(f"unzip {resolved_path}{zip_name} -d {resolved_path}", timeout=60)
            #Move it to the ~/Applications folder with the full name
            ssh.send_command(f'mv \"{resolved_path}HP Smart.app\" {app_unzipped_folder_name}')
            #Delete the original zip to avoid clutter
            ssh.send_command("rm " + resolved_path + zip_name)
            # Reset HP Smart permissions
            ssh.send_command(f"tccutil reset All {BUNDLE_ID.SMART}")
        def clean_cached_data():
            user = ssh.send_command("id -un")["stdout"].strip()
            hostname = subprocess.run(["hostname"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
            local_user = subprocess.run(["whoami"], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
            ssh.send_command(f"scp -r /Users/{user}/Library/Containers/{BUNDLE_ID.SMART}/Data/Documents/Logs {local_user}@{hostname}:{c_misc.get_attachment_folder()}", raise_e=False)
            smart_utilities.clean_cataylst_cached_data(ssh)
        request.addfinalizer(clean_cached_data)

@pytest.fixture(scope="function", autouse=True)
def setup_driver_with_app_info(request, ssh_client):
    if pytest.platform == "MAC":
        request.cls.driver.session_data["ssh"] = ssh_client
        request.cls.driver.session_data["cached_app_name"] = "HP\ Smart.app"
        request.cls.driver.session_data["app_url"], request.cls.driver.session_data["zip_name"] = c_misc.get_package_url(request, _os="MAC", project=pytest.default_info)

# Common
@pytest.fixture(scope="class", autouse=True)
def smart_hpid_load(load_hpid_credentials):
    pass