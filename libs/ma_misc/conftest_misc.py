import io
import os
import sys
import json
import base64
import pytest
import logging
import zipfile
import requests

#Web imports 


from SAF.misc import saf_misc
from SAF.driver import driver_factory
from SAF.misc import windows_utils
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.app_package.app_class_factory import app_module_factory

#Appium platform consts
import MobileApps.resources.const.ios.const as i_const
import MobileApps.resources.const.mac.const as m_const
import MobileApps.resources.const.android.const as a_const
import MobileApps.resources.const.windows.const as w_const
import MobileApps.resources.const.web.const as web_const

class BadLocaleStrException(Exception):
    pass

class UnknownDefaultLocaleException(Exception):
    pass

class MissingWifiInfo(Exception):
    pass

#Default locales please reference this webpage 
#http://www.apps4android.org/?p=3695

default_locale= {"ar": "SA",
                 "en": "US",
                 "cs": "CZ",
                 "da": "DK",
                 "de": "DE",
                 "el": "GR",
                 "es": "ES",
                 "fi": "FI",
                 "he": "IL",
                 "hu": "HU",
                 "ja": "JP",
                 "ko": "KR",
                 "nb": "NO",
                 "pl": "PL",
                 "pt": "PT",
                 "ru": "RU",
                 "sv": "SE",
                 "tr": "TR",
                 "zh": "CN",
                 "nl": "NL",
                 "fr": "FR",
                 "it": "IT"}

def get_locale(request):
    locale_parts = request.config.getoption("--locale").split("_")
    if len(locale_parts) == 2:
        return locale_parts
    elif len(locale_parts) == 1:
        if default_locale.get(locale_parts[0], None) is None:
            raise UnknownDefaultLocaleException("Cannot find a default locale for the language: " + locale_parts[0] + " please append it to the default_locale dictionary in conftest_misc.py")
        return locale_parts[0], default_locale[locale_parts[0]]
    else:
        raise BadLocaleStrException("The locale format needs to be [language]_[region]. What was passed in is: " + request.config.getoption("--locale"))

def build_info_dict(request, _os=None):
    const = None
    system_config = ma_misc.load_system_config_file()
    try:
        project_name = pytest.app_info
    except AttributeError:
        logging.error("Please mark your class with the app you are testing ['SMART', 'HPPS', etc]")
        sys.exit()

    try:
        _os = _os if _os else pytest.platform
    except AttributeError:
        logging.error("Please mark test with a platform ['ANDROID', 'IOS', etc]")
        sys.exit()        

    lang, locale = get_locale(request)
    executor_url = system_config["executor_url"] if not request.config.getoption("--executor-url") else request.config.getoption("--executor-url")
    executor_port =  system_config["executor_port"] if not request.config.getoption("--executor-port") else request.config.getoption("--executor-port")

    info_dict = {"server": {"url": executor_url,
                                "port": executor_port},
                     "dc":{
                           "appium:platform": _os.upper(),
                           "appium:clearSystemFiles": True, 
                           "appium:language": lang
                           }}

    if _os.upper() == "ANDROID":
        const = a_const
        info_dict["dc"]["appium:locale"] = locale
        info_dict["dc"]["appium:remoteAppsCacheLimit"] = 0
        info_dict["dc"]["appium:automationName"] = "uiautomator2"
        info_dict["dc"]["appium:androidInstallPath"] = "/storage/emulated/0/Download/"
        info_dict["dc"]["appium:androidScreenshotPath"] = "/storage/emulated/0/Pictures/Screenshots/"
        info_dict["dc"]["appium:uiautomator2ServerInstallTimeout"] = 60000
        info_dict["dc"]["appium:androidInstallTimeout"] = 600000
        info_dict["dc"]["appium:unicodeKeyboard"] = True # need to install appium settings_apk-debug.apk on target mobile to make it work with unicode keyboard (https://github.com/appium/io.appium.settings/releases)
        info_dict["dc"]["appium:recreateChromeDriverSessions"] = True
        info_dict["dc"]["appium:appWaitForLaunch"] = True
        
        if request.config.getoption("--skip-reinstall"):
            info_dict["dc"]["appium:noReset"] = True
            info_dict["dc"]["appium:fullReset"] = False
        else:
            info_dict["dc"]["appium:noReset"] = False
            info_dict["dc"]["appium:fastReset"] = True
            info_dict["dc"]["appium:uninstallOtherPackages"] = "com.hp.printercontrol.debug"
        
        info_dict["dc"]["appium:autoLaunch"] = False
        info_dict["dc"]["appium:newCommandTimeout"] = 120  
        info_dict["dc"]["appium:skipDeviceInitialization"] = True
        info_dict["dc"]["appium:suppressKillServer"] = True 
        info_dict["dc"]["appium:allowInvisibleElements"] = True 
        info_dict["dc"]["appium:enforceXPath1"] = True
        info_dict["dc"]["appium:autoGrantPermissions"] = True
        info_dict["dc"]["appium:permissions"] = [
            "android.permission.WRITE_EXTERNAL_STORAGE",
            "android.permission.READ_EXTERNAL_STORAGE", 
            "android.permission.CAMERA",
            "android.permission.MANAGE_EXTERNAL_STORAGE",
            "android.permission.READ_MEDIA_IMAGES",
            "android.permission.READ_MEDIA_VIDEO"
        ]

        if getattr(const.OPTIONAL_INTENT_ARGUMENTS, project_name.upper(), False):
            info_dict["dc"]["appium:optionalIntentArguments"] = getattr(const.OPTIONAL_INTENT_ARGUMENTS,
                                                                 project_name.upper())
        info_dict["dc"]["appium:resetKeyboard"] = True

        if getattr(const.ANDROID_PROCESS, project_name.upper(), False):
            info_dict["dc"]["appium:chromeOptions"] = {}
            info_dict["dc"]["appium:chromeOptions"]["androidProcess"] = getattr(const.ANDROID_PROCESS, project_name.upper())

        if getattr(const.CUSTOM_CHROME_DRIVER, project_name.upper(), False):
            info_dict["dc"]["appium:chromedriverExecutable"] = getattr(const.CUSTOM_CHROME_DRIVER, project_name.upper())

    elif _os.upper() == "IOS":
        const = i_const
        info_dict["dc"]["appium:locale"] = lang + "_" +locale
        info_dict["dc"]["appium:automationName"] = "XCUITest"
        info_dict["dc"]["appium:useNewWDA"] = False
        info_dict["dc"]["appium:usePrebuiltWDA"] = True
        info_dict["dc"]["appium:derivedDataPath"] = "/work/reset_wda/appium_wda_ios/"
        info_dict["dc"]["appium:prebuiltWDAPath"] = "/work/reset_wda/appium_wda_ios/Build/Products/Debug-iphoneos/WebDriverAgentRunner-Runner.app"
        info_dict["dc"]["appium:waitForQuiescence"] = True
        info_dict["dc"]["appium:showXcodeLog"] = True
        # info_dict["dc"]["webviewConnectTimeout"] = 30000
        # info_dict["dc"]["safariLogAllCommunication"] = True

    elif _os.upper() == 'MAC':
        const = m_const
        info_dict["dc"]["appium:deviceName"] = "mac device"
        info_dict["dc"]["appium:automationName"] = "Mac2"
        info_dict["dc"]["appium:showServerLogs"] = True
        try:
            info_dict["dc"]["appium:bundleId"] = eval("const.BUNDLE_ID." + project_name.upper())
        except AttributeError:
            logging.info(f"Cannot find bundle id for project {project_name}")

    elif _os.upper() == "WINDOWS":
        const = w_const
        info_dict["dc"]["ms:experimental-webdriver"] = False
        info_dict["dc"]["appium:forceMjsonwp"]= True
        info_dict["dc"]["appium:automationName"] = "windows"

    if project_name.upper() not in const.NONE_THIRD_PARTY_APP.APP_LIST:
        if _os.upper() == "IOS":
            info_dict["dc"]["appium:bundleId"] = eval("const.BUNDLE_ID." + project_name.upper())
        elif _os.upper() == "ANDROID":
            try:
                info_dict["dc"]["appium:appWaitActivity"] = getattr(const.WAIT_ACTIVITY, project_name.upper())
            except AttributeError:
                logging.debug("Does not have a wait activity")
        info_dict["dc"]["appium:noReset"] = True
    else:
        if _os.upper() not in ["WINDOWS"]:
            if request.config.getoption("--skip-reinstall"):
                info_dict["dc"]["appium:noReset"] = True
                info_dict["dc"]["appium:fullReset"] = False
            else:
                # for downloading new build & fresh install of a new app we shd use this
                app_info = get_package_url(request, _os=_os)
                info_dict["app_info"] = {project_name: str(app_info[1])}
               
                if _os.upper() != "MAC":
                    info_dict["dc"]["appium:app"] = app_info[0]
                
            if _os.upper() == "ANDROID":
                pkg_name, act_name = get_pkg_activity_name_from_const(request, const, project_name)
                if pkg_name is not None:
                    info_dict["dc"]["appium:appPackage"] = pkg_name
                if act_name is not None:
                    info_dict["dc"]["appium:appActivity"] = act_name
        elif _os.upper() in ["WINDOWS"]:
            info_dict["dc"]["appium:app"] = eval("const.APP_NAME." + project_name.upper())
        
    if request.config.getoption("--mobile-device") is not None:
        info_dict["dc"]["appium:deviceName"] = request.config.getoption("--mobile-device")
    if request.config.getoption("--platform-version") is not None:
        info_dict["dc"]['appium:platformVersion'] = request.config.getoption("--platform-version")

    info_dict["language"], info_dict["locale"] = get_locale(request)
    if request.config.getoption("--imagebank-path") is not None:
        info_dict["image_bank_root"] = request.config.getoption("--imagebank-path")
    else:
        info_dict["image_bank_root"] = system_config.get("image_bank_root")
    info_dict["bulk_image_root"]=system_config.get("bulk_image_root")
    info_dict["start_up_project"] = project_name
    info_dict["request"] = request
    return info_dict

def build_web_info_dict(request, browser_type):
    system_config = ma_misc.load_system_config_file()  
    executor_url = system_config["executor_url"] if not request.config.getoption("--executor-url") else request.config.getoption("--executor-url")
    executor_port =  system_config["executor_port"] if not request.config.getoption("--executor-port") else request.config.getoption("--executor-port")

    try:
        project_name = pytest.app_info
    except AttributeError:
        logging.error("Please mark your class with the app you are testing ['SMART', 'HPPS', etc]")
        sys.exit()
    info_dict = {"server": {"url": executor_url,
                                "port": executor_port},
                     "dc":{"platformName": request.config.getoption("--platform")
                        }}
    info_dict["language"], info_dict["locale"] = get_locale(request)
    info_dict["stack"] = request.config.getoption("--stack")
    if request.config.getoption("--imagebank-path") is not None:
        info_dict["image_bank_root"] = request.config.getoption("--imagebank-path")
    else:
        info_dict["image_bank_root"] = system_config.get("image_bank_root")
    info_dict["bulk_image_root"]=system_config.get("bulk_image_root")
    info_dict["request"] = request
    
    try:
        #Adding proxy if one is defined in the web_const for this project
        proxy = eval("web_const.PROXY." + pytest.app_info.upper())
    except AttributeError:
        proxy = None
    if proxy is not None:
        info_dict["proxy"] = proxy
    return info_dict

def create_driver(request, _os):
    info_dict = build_info_dict(request, _os)
    return driver_factory.web_driver_factory(_os, info_dict)

def utility_web_driver(browser_type="chrome", executor_url=None, executor_port=None, profile_path=None, request=None):
    system_config = ma_misc.load_system_config_file()
    executor_url = executor_url if executor_url is not None else system_config["web_executor_url"]
    executor_port = executor_port if executor_port is not None else system_config["web_executor_port"]

    info_dict = {"server": {"url": executor_url, "port": str(executor_port)},
                            "dc": {"platformName": "ANY"}}
    if request:
        info_dict["request"] = request
        
    if profile_path is not None:
        info_dict["profile_path"] = profile_path
    return driver_factory.web_driver_factory(browser_type, info_dict)

def create_web_driver(request):
    browser_type = request.config.getoption("--browser-type")
    info_dict = build_web_info_dict(request, browser_type)
    return driver_factory.web_driver_factory(browser_type, info_dict)

def get_package_url(request, _os=None, project=None, app_type=None, app_build=None, app_release=None):
    system_config = ma_misc.load_system_config_file()
    custom_location = request.config.getoption("--local-build")
    if custom_location is not None:
        if ma_misc.validate_url(custom_location) or os.path.isfile(custom_location):
            if system_config.get("database_info", None) is not None:
                # If database then cache it
                app_obj = app_module_factory("ANY", "ANY", system_config["database_info"])
                return app_obj.get_build_url(custom_location)
            # If the build is local and there is no database_info then return the location
            return custom_location
        else:
            raise RuntimeError("App Location: " + custom_location + " is not a valid location")

    actual_os = _os if _os is not None else pytest.platform
    actual_project = project if project is not None else pytest.app_info
    app_obj = app_module_factory(actual_os, actual_project, system_config.get("database_info", None))
    
    if _os.lower() == "ANDROID".lower():
        if actual_project == "HPPS":
            cmd_app_type = request.config.getoption("--hpps-app-type")
            cmd_app_version = request.config.getoption("--hpps-app-version")
            cmd_app_build = request.config.getoption("--hpps-app-build")
            cmd_app_release = request.config.getoption("--hpps-app-release")
        else:
            cmd_app_type = request.config.getoption("--app-type")
            cmd_app_version = request.config.getoption("--app-version")
            cmd_app_build = request.config.getoption("--app-build")
            cmd_app_release = request.config.getoption("--app-release")

        app_type = app_type if app_type is not None else cmd_app_type
        app_version = cmd_app_version
        
        app_build = app_build if app_build is not None else cmd_app_build
        app_release = app_release if app_release is not None else cmd_app_release
        return app_obj.get_build_url(build_type=app_type, build_version=app_version, build_number=app_build, release_type=app_release)

    elif _os.lower() == "IOS".lower():
        app_type = request.config.getoption("--app-type")
        app_version = request.config.getoption("--app-version")
        app_build = app_build if app_build is not None else request.config.getoption("--app-build")
        return app_obj.get_build_url(build_type=app_type, build_version=app_version, build_number=app_build)

    elif _os.lower() == "WINDOWS".lower():
        if actual_project == "HPX":
            #If the project type is HPX then the app-type is determined by the stack variable
            app_type = request.config.getoption("--stack")
        else:
            app_type = request.config.getoption("--app-type", default=None)
        app_version = request.config.getoption("--app-version")
        app_build = app_build if app_build is not None else request.config.getoption("--app-build")
        return app_obj.get_build_url(build_type=app_type, build_version=app_version, build_number=app_build)

    elif _os.lower() == "MAC".lower():
        app_version = request.config.getoption("--app-version")
        app_build = request.config.getoption("--app-build")
        return app_obj.get_build_url(build_version=app_version, build_number=app_build)

def get_session_result_folder_path(driver):
    info = driver.driver_info
    root_path = ma_misc.get_abs_path("/results", False)
    #TODO: For appium2 the deviceName is not the same
    if info.get("desired", False):
        device_name = info["desired"]["deviceName"].replace(" ", "_")
    else:
        device_name = info["deviceName"].replace(" ", "_")
    dir_path = str("{}/{}/{}_{}/".format(root_path, info["platformName"].lower(),
            device_name, info.get("CONFIG_UUID", info.get("udid"))))
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    return dir_path    

def get_web_session_result_folder_path(request):
    root_path = ma_misc.get_abs_path("/results", False)
    return "{}/{}/{}/{}/".format(root_path, "web", request.config.getoption("--browser-type"), request.config.getoption("--uuid"))


def get_test_result_folder_path(session_result_folder, test_class_name):
    dir_path = session_result_folder + test_class_name + "/"
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    return dir_path

def get_attachment_folder():
    #This function only works after the class scope
    path = pytest.test_result_folder + "attachment/"
    if not os.path.isdir(path):
        os.makedirs(path)
    return path

def save_printer_fp_and_publish(p, file_path):
    try:
        p.printer_screen_shot(file_path)
    except: 
        logging.warning("Could not take screenshot of printer: " + file_path)
        return False
    ma_misc.publish_to_junit(file_path)    

def save_mem_stat_and_publish(driver, root_path, file_name=None):
    data = driver.wdvr.execute_script("mobile: shell", {"command": "cat", "args":["/proc/meminfo"]})
    if file_name is None:
        file_name = "mem_stat.txt"
    file_path = root_path + file_name
    with open(file_path, "w+", encoding="utf-8") as f:
        f.write(data)
    ma_misc.publish_to_junit(file_path)

def save_screenshot_and_publish(driver, file_path):
    """
    Get screen-shot of mobile device
    :param driver:
    :param file_path:
    :return:
    """
    # This is currently not proper location need to fix later
    driver.wdvr.get_screenshot_as_file(file_path)
    ma_misc.publish_to_junit(file_path)

def save_source_and_publish(driver, root_path, file_name=None):
    if file_name is None:
        file_name = "page_source.txt"
    file_path = root_path + file_name
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(driver.wdvr.page_source)
    ma_misc.publish_to_junit(file_path)

def save_session_id(driver, root_path, f_name=None):
    if f_name is None:
        f_name = "Session_id.txt"
    path = root_path + f_name
    lst = (driver.current_url).split("2F")
    if "oss%" in lst:
        ows_id = lst.index("steps%")
        with open(path,"w", encoding="utf-8") as t:
            t.write(lst[ows_id-1])
        ma_misc.publish_to_junit(path)

def save_har_and_publish(driver, root_path, file_name):
    file_path = root_path + file_name
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(driver.wdvr.har)
    ma_misc.publish_to_junit(file_path)
    del driver.wdvr.requests
    
def save_log_and_publish(driver, root_path, node_name):
    """
    Get logcat of device and save to file_path
    :param driver:
    :param root_path:
    :param node_name:
    :return:
    """
    save_file_path = "{}{}_log.txt".format(root_path, node_name)
    driver.return_device_log(save_file_path)
    ma_misc.publish_to_junit(save_file_path)

def save_app_log_and_publish(project, driver, root_path, node_name):
    try:
        zipfile = base64.b64decode(driver.wdvr.pull_folder(eval("a_const.TEST_DATA." + project + "_APP_LOG_PATH")))
        fh = open(root_path + node_name + "_app_log" + ".zip", "wb")
        fh.write(zipfile)
        fh.close()
        #Publish to junit
        ma_misc.publish_to_junit(os.path.realpath(fh.name))
    except:
        logging.warning("Unable to capture app log")

def save_windows_app_log_and_publish(project, driver, root_path, node_name):
    try:
        #Zip log folder
        remote_log_path = eval("w_const.TEST_DATA." + project + "_APP_LOG_PATH")
        remote_log_parent_path = "\\".join(remote_log_path.split("\\")[:-1])
        remote_log_path_copy = remote_log_parent_path + "\\LocalState_Copy"
        if windows_utils.check_path_exist(driver.ssh, remote_log_path_copy):
            driver.ssh.send_command('Remove-Item -Path ' + remote_log_path_copy + ' -Recurse -Force')
        driver.ssh.send_command("New-Item -ItemType 'directory' -Path " + remote_log_path_copy)
        driver.ssh.send_command("xcopy " + remote_log_path + " " + remote_log_path_copy + " /k/e/d/Y/c")
        driver.ssh.send_command("compress-archive -Force -LiteralPath " + remote_log_path_copy +  " -DestinationPath " + remote_log_parent_path + "\\app_log.zip", timeout=30)
        driver.ssh.pull_file(remote_log_parent_path + "\\app_log.zip", root_path + node_name +  "_app_log.zip")
        driver.ssh.send_command("Remove-Item -Recurse -Force " + remote_log_path_copy)
        ma_misc.publish_to_junit(root_path + node_name +  "_app_log.zip")
    except Exception as e:
        logging.warning("Unable to capture app log: " + str(e))

def save_ios_app_log_and_publish(fc, driver, root_path, node_name, export_method="direct"):
    """
    @export method:
    1. direct: Pull app logs from iOS device using appium call
    2. files: Export zip of logs from app settings -> export zip file to Files
    3. email: Export app file via email  
    """
    try:
        if export_method == "direct":
            zipfile = base64.b64decode(driver.wdvr.pull_folder("@com.hp.printer.control.dev:documents/" + "Logs"))
        elif export_method == "files":
            zipfile = base64.b64decode(fc.export_app_log_to_files())
        elif export_method == "email":
            fc.export_app_log_to_files(export_method=export_method)
        fh = open(root_path + node_name + "_app_log" + ".zip", "wb")
        fh.write(zipfile)
        fh.close()
        ma_misc.publish_to_junit(os.path.realpath(fh.name))
    except:
        logging.warning("Unable to capture app log")

def save_video_and_publish(driver, root_path, file_name):
    file_path = root_path + file_name + ".mp4"
    fh = open(file_path, "wb+")
    data = driver.wdvr.stop_recording_screen()
    fh.write(base64.b64decode(data))
    fh.close()
    ma_misc.publish_to_junit(file_path)

def save_cms_results_and_publish(driver, root_path, file_name):
    file_path = root_path + file_name + ".json"
    if driver.session_data["context_manager_mode"] != "verify":
        logging.info("Context manager verify not activated nothing to save")
        return True
    with open(file_path, "w+", encoding="utf-8") as fh:
        json.dump(driver.session_data["context_manager_results"], fh)
    ma_misc.publish_to_junit(file_path)

def save_cms_failed_images_and_publish(driver, root_path, file_name):
    file_path = root_path + file_name + ".zip"
    file_list = []
    for key, value in driver.session_data["context_manager_failed_images"].items():
        img_file = key.replace("/", "_") + ".png"
        content = base64.b64decode(value)
        file_list.append(tuple([img_file, content]))
    if file_list == []:
        #If no failures don't post a zip file
        return True
    in_memory_zip(file_path, file_list)
    ma_misc.publish_to_junit(file_path)

def in_memory_zip(zip_file_path, content):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
        for file_name, data in content:
            zip_file.writestr(file_name, io.BytesIO(data).getvalue())
    with open(zip_file_path, "wb") as f:
        f.write(zip_buffer.getvalue())

def get_wifi_info(request, raise_e=True):
    system_cfg = ma_misc.load_system_config_file()
    if not system_cfg.get("default_wifi", False):
        ssid = request.config.getoption("--wifi-ssid")
        password = request.config.getoption("--wifi-pass")
    else:
        ssid = request.config.getoption("--wifi-ssid") if request.config.getoption("--wifi-ssid") else system_cfg["default_wifi"]["ssid"]
        password = request.config.getoption("--wifi-pass") if request.config.getoption("--wifi-pass") else system_cfg["default_wifi"]["passwd"]

    if ssid is None or password is None:
        if raise_e:
            raise MissingWifiInfo("System config file is missing 'default_wifi' info and it's not passed in")
        else:
            return None, None

    return ssid, password

def get_pkg_activity_name_from_const(request,const, project_name):
    pkg_name = getattr(const.PACKAGE, project_name.upper())
    act_name = getattr(const.LAUNCH_ACTIVITY, project_name.upper())
    pkg_type = request.config.getoption("--app-type")
    if type(pkg_name) is not str:
        pkg_name = pkg_name(pkg_type)
    return pkg_name, act_name

def save_localization_screenshot_and_publish(source_folder, output_zip_path):

    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_folder)
                zipf.write(file_path, arcname)

    ma_misc.publish_to_junit(output_zip_path)

if __name__ == "__main__":
    pass