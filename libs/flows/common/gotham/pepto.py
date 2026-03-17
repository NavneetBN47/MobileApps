import MobileApps.resources.const.windows.const as w_const
from selenium.common.exceptions import NoSuchElementException
import xml.etree.ElementTree as ET
import re
import time

class Pepto(object):
    def __init__(self, driver):
        self.driver = driver
    
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def verify_pepto_log_file_created(self):
        log_file = w_const.TEST_DATA.PDSMQ_DATA_PATH
        check_file = self.driver.ssh.send_command('Test-Path -path "{}"'.format(log_file))
        if check_file["stdout"]:
            return True

    def enable_pepto_log(self, build_version):
        pdsmqconfig_xml = w_const.TEST_DATA.WINDOWS_APP_PATH + "\\AD2F1837.HPPrinterControl_{}.0_x64__v10z8vjag6ke6\\PdsmqConfig.xml".format(build_version)
        if (fh := self.driver.ssh.remote_open(pdsmqconfig_xml, mode="r+", raise_e=False)):
            data = fh.read().decode("utf-8")
            fh.close()
            data = re.sub("</PdsmqConfig>", "<Log>On</Log><LogLevel>Debug</LogLevel></PdsmqConfig>", data)
            fh = self.driver.ssh.remote_open(pdsmqconfig_xml, mode="w")
            fh.write(data)
            fh.close()
            time.sleep(1)
            self.driver.terminate_app()
            time.sleep(3)
            self.driver.launch_app()
            time.sleep(3)
                
    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def check_pepto_data(self, check_event, check_data="pepto", raise_e=True):
        time.sleep(3)
        if check_data == "pepto":
            f = self.driver.ssh.remote_open(w_const.TEST_DATA.PDSMQ_DATA_PATH)
        elif check_data == "p2":
            f = self.driver.ssh.remote_open(w_const.TEST_DATA.HP_SMART_LOG_PATH)
        data = f.read().decode("utf-8").replace('\n', '')
        f.close()
        if not re.search(check_event, data):
            if raise_e is False:
                return False
            else:
                raise NoSuchElementException(
                    "Fail to found {}".format(check_event))

    def check_control_settings_data(self, value):
        time.sleep(3)
        file_path = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH + '\HPPrinterControlSettings.xml'
        f = self.driver.ssh.remote_open(file_path)
        xmlStr = f.read()
        f.close()
        root = ET.fromstring(xmlStr)
        for setting in root.iter('Setting'):
            if setting.find('SettingName').text == value:
                return setting.find('SettingValue').text
        else:
            raise NoSuchElementException("Fail to find SettingName {}".format(value))

    def check_file_spt_value(self):
        time.sleep(3)
        file_path = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH + '\RecentDeviceList.xml'
        f = self.driver.ssh.remote_open(file_path)
        xmlStr = f.read()
        f.close()
        root = ET.fromstring(xmlStr)
        for spt in root.iter('IsSptEnabled'):
            return spt.text
        else:
            raise NoSuchElementException("Fail to find IsSptEnabled in the file")
