# encoding: utf-8
'''
Description: It defines miscellaneous which are used in the MAC code.

@author: Sophia
@create_date: July 25, 2019
'''

import os
import shutil
import datetime
import json
import subprocess
from MobileApps.resources.const.ios.const import BUNDLE_ID
from SAF.misc.saf_misc import *
from SAF.misc.ssh_utils import SSH, CommandFailedException
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.mac.const import TEST_DATA


def delete_all_files(folder_path):
    '''
    This is a method to delete all files in a folder.
    :parameter:
    :return:
    '''
    try:
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
    except OSError as e:
        raise ("Error: %s - %s." % (e.filename, e.strerror))


def install_app(url, node_ip, save_path='/tmp/temp_package', username='exec'):
    app_package_file = download_file(url, save_path)
    file_name = url.split("/")[-1]
    client = SSH(node_ip, username)
    unique_file_path = '/Users/'+username+'/Downloads/'+file_name
    client.send_file(app_package_file, unique_file_path)
    client.send_command('installer -pkg ' + unique_file_path + ' -target CurrentUserHomeDirectory')


def kill_browser(browser_name):
    '''
    This is a method to kill browser process.
    :parameter:
    :return:
    '''
    os.system("pkill " + browser_name)


def change_sys_language_region(language_region_value=None):
    '''
    This is a method to change OSX system language and region.
    defaults read NSGlobalDomain AppleLanguages
    :parameter:
    :return:
    '''
    if language_region_value is None:
        os.system('defaults write NSGlobalDomain AppleLanguages "(en-US)"')
        # os.system('defaults write NSGlobalDomain AppleLocale "(en_US)"')
    else:
        os.system('defaults write NSGlobalDomain AppleLanguages "(' + language_region_value + ')"')


def setup_computer_network_status(hardware_port_type, hardware_port_status):
    '''
    This is a method to setup computer WiFi network.
    :parameter:
    :return:
    '''
    os.system("networksetup -setairportpower " + hardware_port_type + hardware_port_status)


def setup_computer_ethernet_network_status(hardware_port_type, hardware_port_status, os_sys_pw):
    '''
    This is a method to setup computer Ethernet network
    :parameter:
    :return:
    '''
    os.system('echo ' + os_sys_pw + ' | sudo -S ifconfig ' + hardware_port_type + hardware_port_status)


def switch_other_network(hardware_port_type, network_name, network_password):
    '''
    This is a method to switch networks
    :parameter:
    :return:
    '''
    os.system("networksetup -setairportnetwork " + hardware_port_type + network_name + " " + network_password)


def delete_pw_from_keychain(printer_key_id, os_sys_pw):
    '''
    This is a method to delete passwords which printer saved in Keychain.
    :parameter:
    :return:
    '''

    os.system('echo ' + os_sys_pw + ' | sudo -S security delete-generic-password -l "HP Smart-HP Printer-' + printer_key_id + '"')


def open_app(filepath):
    '''
    This is a method to open applications
    :parameter:
    :return:
    '''
    os.system('open ' + filepath)


def change_system_time(os_sys_pw, date_time_value=None):
    '''
    This is a method to change current system time to a specific time.
    :parameter:
    :return:
    '''

    if date_time_value is None:
        date_time_value = datetime.datetime.now() + datetime.timedelta(days=2)

    date_str_value = date_time_value.strftime("%m%d%H%M%y")
    os.system('echo ' + os_sys_pw + ' | sudo -S date ' + date_str_value)


def restore_system_time(os_sys_pw):
    '''
    This is a method to restore system time with time.apple.com.
    :parameter:
    :return:
    '''
    os.system('echo ' + os_sys_pw + ' | sudo -S sntp -sS time.asia.apple.com')

def uninstall_app(driver, application_path=None, raise_e=False, clean_catalyst_cached_data=True):
    """
    param:
    - application_path: the path to the application, if not provided, will remove Catalyst app
    - raise_e: whether to raise exception if uninstall failed
    - clean_catalyst_cached_data: whether to clean cached data for Catalyst app
    """
    if not application_path:
        application_path = driver.session_data["ssh"].send_command("echo ~/Applications/")["stdout"].strip()
    driver.session_data["ssh"].send_command(f"rm -rf {application_path}*.app", timeout=40, raise_e=raise_e)
    if clean_catalyst_cached_data:
        clean_cataylst_cached_data(ssh=driver.session_data["ssh"], raise_e=raise_e)

def clean_cataylst_cached_data(ssh, raise_e=False):
    """
    Clean cached data for Catalyst app
    """
    user = ssh.send_command("id -un")["stdout"].strip()
    ssh.send_command(f"rm -rf /Users/{user}/Library/Group\ Containers/*{BUNDLE_ID.SMART}", raise_e=raise_e)
    ssh.send_command(f"rm -rf /Users/{user}/Library/Containers/{BUNDLE_ID.SMART}", raise_e=raise_e)
    ssh.send_command(f"rm -rf /Users/{user}/Library/Application\ Scripts/{BUNDLE_ID.SMART}", raise_e=raise_e)

def install_hp_smart(driver):
    resolved_path = driver.session_data["ssh"].send_command("echo ~/Downloads/")["stdout"].strip()
    hp_smart_path = driver.session_data["ssh"].send_command("echo ~/Applications/")["stdout"].strip()
    app_unzipped_folder_name = f"{hp_smart_path}{driver.session_data['cached_app_name']}"
    #Download the app, The file is 300+ mg will take sometime to download depending on speed
    driver.session_data["ssh"].send_command(f"curl {driver.session_data['app_url']} --output {resolved_path}{driver.session_data['zip_name']}", timeout=900)
    #Unzip the file
    driver.session_data["ssh"].send_command(f"unzip {resolved_path}{driver.session_data['zip_name']} -d {resolved_path}", timeout=60)
    #Move it to the ~/Applications folder with the full name
    driver.session_data["ssh"].send_command(f'mv \"{resolved_path}HP Smart.app\" {app_unzipped_folder_name}')
    #Delete the original zip to avoid clutter
    driver.session_data["ssh"].send_command("rm " + resolved_path + driver.session_data['zip_name'])
    # Reset HP Smart permissions
    driver.session_data["ssh"].send_command(f"tccutil reset All {BUNDLE_ID.SMART}")

# extract pdsmq data
def process_file_by_line(line):
    data_list = []
    if 'schema' in line:
        data_list=line[line.find('{'):].replace('}{','}\n{').split('\n')
    return data_list


# extract pdsmq data
def get_file_data_to_dict(file_path):
    with open(os.path.expanduser(file_path)) as f:
        data_list = []
        for line in f:
            data_list = data_list + process_file_by_line(line)
    return data_list


def get_local_strings_from_table(screen_name, language_region_value=None):
    '''
    This is a method to get local strings from string table.
    :parameter:
    :return:
    '''
    if language_region_value is None:
        return ma_misc.load_json_file(TEST_DATA.MAC_SMART_LOCAL_STRINGS_INFO)["ENU"][screen_name]
    else:
        return ma_misc.load_json_file(TEST_DATA.MAC_SMART_LOCAL_STRINGS_INFO)[language_region_value][screen_name]

def handle_photos_access_popup(driver, button_number):
    """
    Handle Photos access popup using AppleScript because the popup is not
    being captured in the page source.
    button_number: 2 for Don't Allow, 3 for Allow, 4 for Select photos to access
    """
    try:
        driver.session_data["ssh"].send_command(f"osascript -e 'tell application \"System Events\" to tell process \"UserNotificationCenter\" to click button {button_number} of window 1'")
    except CommandFailedException:
        return False

def get_all_windows(ssh, timeout=60):
    """
    Get all windows of all processes using AppleScript on mac
    """
    return ssh.send_command("osascript -e 'tell application \"System Events\" to return every window of every process'", timeout=timeout)["stdout"]

def verify_app_store_opened(driver):
    """
    Verify App Store app is opened
    """
    return "App Store" in get_all_windows(driver.session_data["ssh"])

def close_app_store(driver):
    """
    Dismiss App Store popup and Close App Store app using AppleScript
    """
    driver.session_data["ssh"].send_command("osascript -e 'tell application \"System Events\" to tell its application process \"App Store\" to tell its window 1 to click button \"OK\"'", raise_e=False)
    driver.session_data["ssh"].send_command("osascript -e 'tell application \"App Store\" to quit'")

def clear_mac_popups(ssh, timeout=5, raise_e=False, retry=3):
    """
    Clear popups on Mac
    """
    for _ in range(retry):
        terminate_loop = False
        if "UserNotificationCenter" in get_all_windows(ssh):
            ssh.send_command("osascript -e 'tell application \"System Events\" to tell application \"UserNotificationCenter\" to quit'",
                            timeout=timeout, raise_e=raise_e)
        else:
            terminate_loop = True
        if terminate_loop:
            break

def dismiss_wda_popup(ssh, timeout=1, raise_e=False):
    """
    Dismisses the WebDriverAgentRunner-Runner popup on Mac after an appium reset
    Currently just facing the popup on tgtmac2i
    """
    ssh.send_command("osascript /Users/exec/dismiss_wda_popup.applescript", timeout=timeout, raise_e=raise_e)

def delete_all_hp_smart_files(ssh):
    """
    Delete all HP Smart files on Mac
    """
    user = ssh.send_command("id -un")["stdout"].strip()
    path = ssh.send_command(f'find /Users/{user}/Library/Mobile\ Documents -d -name "*com~hp~printer~control" 2>/dev/null')["stdout"].strip()
    ssh.send_command(f"rm -rf '{path}/Documents/'", raise_e=False)

def create_hp_smart_file(ssh, file_name, create_new_file=True, file_path=None):
    """
    Create a file that can be accessed through HP Smart files
    create_new_file: whether to create a new file or use an existing one
    file_path: path to the desried file to move if create_new_file is False
    """
    user = ssh.send_command("id -un")["stdout"].strip()
    hostname = ssh.send_command("hostname")["stdout"].strip()
    path = ssh.send_command(f'find /Users/{user}/Library/Mobile\ Documents -d -name "*com~hp~printer~control" 2>/dev/null')["stdout"].strip()
    if create_new_file:
        ssh.send_command(f"touch '{path}/Documents/{file_name}'")
    else:
        if not file_path:
            raise ValueError("file_path is required if create_new_file is False")
        subprocess.run(["scp", file_path, f"{user}@{hostname}:'{path}/Documents/{file_name}'"])

def compose_and_send_email(ssh, to_email, subject_text="", body_text=""):
    """
    Compose and send email using AppleScript because the new message prompt is not showing up in the page source
    Each command is sending keys to the email fields and then switching to the next field using tab key
    The last command is sending command+shift+d to send the email
    """
    ssh.send_command(f"osascript -e 'tell application \"System Events\" to tell process \"Mail\" to keystroke \"{to_email}\"'")
    # Extra tab to skip the CC field
    ssh.send_command(f"osascript -e 'tell application \"System Events\" to tell process \"Mail\" to keystroke tab'")
    if subject_text:
        ssh.send_command(f"osascript -e 'tell application \"System Events\" to tell process \"Mail\" to keystroke tab'")
        ssh.send_command(f"osascript -e 'tell application \"System Events\" to tell process \"Mail\" to keystroke \"{subject_text}\"'")
    if body_text:
        ssh.send_command(f"osascript -e 'tell application \"System Events\" to tell process \"Mail\" to keystroke tab'")
        ssh.send_command(f"osascript -e 'tell application \"System Events\" to tell process \"Mail\" to keystroke \"{body_text}\"'")
    ssh.send_command("osascript -e 'tell application \"System Events\" to tell process \"Mail\" to keystroke \"d\" using {command down, shift down}'")

def close_mail_app(ssh):
    """
    Close Mail app using AppleScript
    """
    ssh.send_command("osascript -e 'tell application \"Mail\" to quit'")

if __name__ == "__main__":
    pass
