import os
import re
import sys
import time
import json
import zipfile
import shutil
import logging
import random
import string
import requests
import csv
from io import BytesIO
from SAF.misc import saf_misc
from requests.exceptions import InvalidURL

class SystemConfigFileMissing(Exception):
    pass

class CannotSatisfyAccount(Exception):
    pass

def get_abs_path(relative_path=None, file_check=False):
    """
    Description: Find the absolute path from a relative path 
    Param:
    relative_path -- The relative path from the repo to the file
    file_check -- if set true the method will throw an exception if file does not exist
    NOTE: Due to how the __file__ works this method cannot be moved outside of the repo
          A copy in each repo is REQUIRED 
    """
    path = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-2])
    if relative_path is not None:
        if type(relative_path) != str:
            raise TypeError("relative_path must be type str")
        if relative_path[0] != "/":
            path = path + "/"
        path = path + relative_path

        if file_check and not os.path.isfile(path) and not os.path.isdir(path):
            raise IOError("The path: " + path + " is not a file or directory")

    return path

def return_apk_cache_path(apk_name):
    return get_abs_path("/resources/apk_cache/" + apk_name)

def create_dir(directory):
    """
    Create a directory
    :param directory: path of directory
    :return: absolute path of directory
    """
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        logging.debug("{} is created successfully!".format(directory))
    else:
        logging.debug("{} is already existed!".format(directory))
    return os.path.abspath(directory)

def create_file(file_path, write_mode='w', content=""):
    """
    Create a file with a content
    :param file_path: file's path
    :param write_mode: writing mode
    :param content: content in file
    """
    if not os.path.exists(file_path):
        if file_path.rfind("/") > 0:
            create_dir(file_path[:file_path.rfind("/")])
        with open(file_path, write_mode) as fi:
            fi.write(content)
    else:
        logging.debug("'{}' is already created".format(file_path))

def load_system_config_file(relative_path="config/system_config.json"):
    try:
        get_abs_path(relative_path, file_check=True)
        return load_json_file(relative_path)
    except IOError:
        logging.info("Could not find system_config.json in MobileApps, trying system path")
        if not os.path.isfile("/work/ma_config/system_config.json"):
            raise SystemConfigFileMissing("No system_config.json file in MobileApps or the system path (/work/ma_config/system_config.json)")
        else:
            return saf_misc.load_json("/work/ma_config/system_config.json")

def load_json_file(relative_path):
    file_path = get_abs_path(relative_path)
    return saf_misc.load_json(file_path)

def read_csv_file(file_path):
    """
    Reads a CSV file and returns a list of rows (each row is a list of values).
    """
    rows = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return rows

def web_localization_path_builder(driver, file_path):
    spec_path = driver.session_data["image_bank_root"]
    return os.path.join(spec_path, file_path)

def load_json_using_absolute_path(filepath):
    with open(filepath, "r", encoding="utf-8-sig") as jsondata:
        try:
            return json.load(jsondata)
        except ValueError:
            raise ValueError("Given Filepath not json readable")
        
def loop_through_directory_and_return_file_path(path):
    """
    Method for looping through the directory and returning the file path of json file
    """
    json_file_path = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".json"):
                json_file_path.append(os.path.join(root, file))
        for dir in dirs:
            loop_through_directory_and_return_file_path(os.path.join(root, dir))
    return json_file_path

def get_apk_path(apk_name):
    """
    Get absolute path of apk file via apk name
    :param apk_name: name of apk file. For example: google_drive
    :return paths: list of paths based on keyword, apk_name"
    """
    apk_folder = get_abs_path("resources/test_data/apk_files")
    for file in os.listdir(apk_folder):
        if apk_name in file:
            return os.path.join(apk_folder, file)
    raise IOError ("There is no apk file for {}".format(apk_name))


def prep_base_url(url):
    if url[-1] != "/":
        url = url + "/"

    return url

def validate_url(_str):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, _str) is not None

def delete_content_of_folder(path, time_delta=None, everything=True, recreate=True):
    #Delete folder and remake it if time_stamp is None
    #If there is a time stamp only delete anything older than the time specified
    if not os.path.isdir(path):
        logging.debug("Folder: " + path + " does not exist returning True")
        return True

    if time_delta is None:
        if os.path.isdir(path):
            shutil.rmtree(path)
    else:
        if everything and os.path.getctime(path) < (time.time() - time_delta.total_seconds()):
            shutil.rmtree(path)
        if not everything:
            content = os.listdir(path)
            for item in content:
                child_path = path+'/' + item
                if os.path.getctime(child_path) < (time.time() - time_delta.total_seconds()):
                    shutil.rmtree(child_path)

    if recreate:
        os.makedirs(path)

def download_build_to_local(url, save_path="./", auth_header=None, http_auth=None, unzip=True):
    create_dir(save_path)
    logging.debug('Downloading...')
    if auth_header:
        stream_header = auth_header.copy()
        stream_header["Accept"] = "application/octet-stream"
        req = requests.get(url, headers=stream_header)
        fname = re.findall("filename=(.+)", req.headers['content-disposition'])[0]
    else:
        req = requests.get(url, auth=http_auth)
        fname = url.split('/')[-1]
    if fname.endswith(".zip") and unzip:
        z = zipfile.ZipFile(BytesIO(req.content))
        z.extractall(save_path)
        logging.debug('Downloading and extracting Completed')
    else:
        with open(save_path + "/" + fname, "wb") as fh:
            fh.write(req.content)
            logging.debug('{} written to {}'.format(fname, save_path))
    return fname

def publish_to_junit(path):
    sys.stderr.write("\n[[ATTACHMENT|{}]]".format(path))

def truncate_printer_model_name(name, case_sensitive=True):
    """
    https://github-partner.azc.ext.hp.com/HPSmartiOS/dociOS/wiki/02.8.-%5bHome%5d-Device-Model-Name-shortening
    shortening model name for iOS app
    :param case_sensitive: bool
    """
    removed_list = [
        "Hewlett-Packard",
        "e-All-in-One",
        "All-in-One",
        "AIO",
        "Ink Advantage Ultra",
        "Ink Advantage",
        "Advantage",
        "Postscript",
        "Flowmfp",
        "Flow",
        "ePrinter",
        "Printer",
        "Series",
        "ColorMFP",
        "Color",
        "MFP",
        "Professional",
        "Premium",
        "Prem"
    ]
    if not case_sensitive:
        removed_list = [word.lower() for word in removed_list]
        name = name.lower()
    for i in removed_list:
        name = name.replace(i,"").strip()
    name = re.sub(r'\[.*?\]', "", name)
    return " ".join(name.split())

def get_subfolder_path(file_path, relative_root):
    path_list = os.path.abspath(os.path.dirname(file_path)).split("/")
    return "/".join(path_list[path_list.index(relative_root)+1:])

def _launch_driver(self, browser_type="chrome"):
    info_dict = {"server": {"url": self.system_config["web_executor_url"], "port": self.system_config["web_executor_port"]},
                            "dc": {"platform": "ANY"}}
    return driver_factory.web_driver_factory(browser_type, info_dict)

def is_int(check_str):
    try:
        int(check_str)
        return True
    except ValueError:
        return False

def get_random_str(length=8):
    """returns a random string of digits and upper/lowercase letters"""
    return "".join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])

def poll(method, timeout=10, frequency=.5, *args, **kwargs) -> bool:
    """
    Continuously poll a method until it returns True or timeout has been reached
    :param method: function obj that returns a bool
    :param timeout: int or float
    :param frequency: int or float. how often to poll
    :param args: args for method
    :param kwargs: keyword args for method
    """
    end_time = time.time() + timeout
    while time.time() < end_time:
        if method(*args, **kwargs):
            return True
        time.sleep(frequency)
    return False

def get_account_info(project):
    if project == "ECP":
        return saf_misc.load_json(get_abs_path("/resources/test_data/ecp/accounts.json"))
    elif project == "SMB": 
        return saf_misc.load_json(get_abs_path("/resources/test_data/smb/accounts.json"))
    elif project == "HPID":
        return saf_misc.load_json(get_abs_path("/resources/test_data/hpid/test_accounts.json"))
    elif project == "POOBE":
        return saf_misc.load_json(get_abs_path("resources/test_data/poobe/accounts.json"))
    elif project == "Microsoft":
        return saf_misc.load_json(get_abs_path("resources/test_data/email/account.json"))
    elif project == "HPSA":
        return saf_misc.load_json(get_abs_path("resources/test_data/hpsa/accounts.json"))
    elif project == "WEX":
        return saf_misc.load_json(get_abs_path("resources/test_data/wex/accounts.json"))

def get_hpid_account_info(stack, a_type, claimable=None, instant_ink=None, smart_advance=None, pro=None, driver=None, shared=None, cloud_scan=None):
    f = get_account_info("HPID")
    try:
        account_info = f[stack][a_type]
    except KeyError:
        raise

    account_key = {"claimable": claimable,
                   "instant_ink": instant_ink,
                   "smart_advance": smart_advance,
                   "shared": shared,
                   "pro": pro,
                   "cloud_scan": cloud_scan}

    for account in account_info:
        is_found = True
        for key, val in account_key.items():
            if val is not None:
                if val != account[key]:
                    is_found = False
                    break
        if is_found:
            if driver is not None:
                driver.session_data["hpid_user"] = account["email"]
                driver.session_data["hpid_pass"] = account["password"]
                driver.session_data["hpid_type"] = a_type
                driver.session_data["hpid_ii"] = instant_ink
                driver.session_data["smart_advance"] = smart_advance
                driver.session_data["pro"] = pro
                driver.session_data["shared"] = shared
                driver.session_data["cloud_scan"] = cloud_scan
                return True
            return account
    raise CannotSatisfyAccount(f"No account for: stack={stack}, type={a_type}, claimable={str(claimable)}, shared={str(shared)}, cloud_scan={str(cloud_scan)}")

def get_ecp_account_info(stack):
    f = get_account_info("ECP")
    try:
        return f[stack]
    except KeyError:
        raise CannotSatisfyAccount("No account for: stack=" + stack)    

def get_poobe_account_info(key):
    f = get_account_info("POOBE")
    try:
        return f[key]
    except KeyError:
        raise CannotSatisfyAccount("No Account found for key:{}".format(key))

def get_smb_account_info(stack):
    f = get_account_info("SMB")
    try:
        return f[stack]
    except KeyError:
        raise CannotSatisfyAccount("No account for: stack=" + stack)  

def get_microsoft_account_info():
    f = get_account_info("Microsoft")
    try:
        return f["email"]["Microsoft_account"]
    except KeyError:
        raise CannotSatisfyAccount("No account for: Microsoft")    

def get_hpsa_account_info(stack):
    f = get_account_info("HPSA")
    try:
        return f[stack]
    except KeyError:
        raise CannotSatisfyAccount("No account for: stack=" + stack)

def get_wex_account_info(stack):
    f = get_account_info("WEX")
    try:
        return f[stack]
    except KeyError:
        raise CannotSatisfyAccount("No account for: stack=" + stack)         

def get_newest_application_version(version_list):
    """
    Given a list of string values designating an application version, return the newest value as a string
    The list must contain an equal number of values for each version level
    ex// ['133.0.4100', '134.0.4136', '134.0.1421'] -> '134.0.4136'
    """
    if not version_list:
        raise ValueError("version_list cannot be empty")

    return max(version_list, key=lambda x: tuple(map(int, x.split('.'))))

def format_printer_name(printer_name):
    """
    Given a printer's complete bonjour name, format and shorten printer name 
    HP Smart Tank 530 series [32C13A] -> HP Smart Tank 530
    """
    if any(c.isdigit() for c in printer_name):
        found_num = False
        for i, c in enumerate(printer_name):
            if c.isdigit():
                found_num = True
            if found_num and not c.isdigit():
                return printer_name[:i+1].rstrip()
    else:
        return printer_name
            
def create_localization_screenshot_folder(folder_name, attachment_path):

    if not os.path.isdir(attachment_path + folder_name + "/"):
        try:
            os.makedirs(attachment_path + folder_name + "/")
        except Exception as e:

            logging.info(f"Error occurred while creating folder: {e}")   

def get_hpx_webview_context(release_type=None):
    webview_dict = {"debug": 'WEBVIEW_com.hp.printercontrol.debug'}
    return webview_dict[release_type if release_type is not None else "debug"]

#Test code for debugging
if __name__ == "__main__":
    pass