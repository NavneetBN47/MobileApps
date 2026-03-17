from SAF.misc import saf_misc
import logging
from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
import time
import re


class HPXRebrandingCommon(object):
    flow_name = "hpx_rebranding_common"
    log_file = w_const.TEST_DATA.HPX_APP_LOG_PATH + "\\properties.json"
    oobe_log_file = w_const.TEST_DATA.HPX_APP_LOG_PATH + "\\Logs\\Oobe.log"
    flag_dict = {
        "mobilefax": "printer-x-mobilefax",
        "shortcuts":"printer-x-shortcuts",
        "cloudscan":"printer-x-cloudscan",
        "scan":"printer-x-scan",
        "localprint":"printer-x-localprint",
        "printphotos":"printer-x-localprintphotos",
        "printpdf":"printer-x-localprintpdf",
        "dashboard":"printer-x-accountdashboard",
        "printables":"printer-x-printables",
        "diagnostics":"print-x-printer-diagnostics",
        "diagnosticsandfix":"printer-x-diagnosticsandfix",
        "quality":"printer-x-productmaintenance",
        "core":"printer-x-core",
        "settings":"printer-x-settings",
        "privacy":"printer-x-privacysettings",
        "ews":"printer-x-ews"
        }

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        self.driver = driver

    def compare_image_diff(self, ele, format_specifier=[], folder_n=None, image_n=None, pre=False):
        cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element(ele, format_specifier=format_specifier))
        if pre:
            cur_img = saf_misc.img_crop(cur_img, 0.0, 0.08, 0.0, 0.22)
        else:
            cur_img = saf_misc.img_crop(cur_img, 0.0, 0.0, 0.0, 0.0)
        
        if folder_n is None:
            save_path = w_const.TEST_DATA.HPX_SCREENSHOT_PATH + "temp/" + image_n
        else:
            save_path = w_const.TEST_DATA.HPX_SCREENSHOT_PATH  + folder_n + "/" + image_n
        
        logging.info("screenshot Results Folder: " + save_path) 
        comp_image = saf_misc.load_image_from_file(ma_misc.get_abs_path(save_path))
        return saf_misc.img_comp(cur_img, comp_image)

    def save_image(self, ele, format_specifier=[], folder_n=None, image_n=None, pre=False):
        cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element(ele, format_specifier=format_specifier))
        if pre:
            cur_img = saf_misc.img_crop(cur_img, 0.0, 0.08, 0.0, 0.22)
        else:
            cur_img = saf_misc.img_crop(cur_img, 0.0, 0.0, 0.0, 0.0)

        if folder_n is None:
            save_path = w_const.TEST_DATA.HPX_SCREENSHOT_PATH + "temp/" + image_n
        else:
            save_path = w_const.TEST_DATA.HPX_SCREENSHOT_PATH + folder_n + "/" + image_n
        
        cur_img.save(ma_misc.get_abs_path(save_path))
        logging.info("screenshot Results Folder: " + save_path)
         
    
    def change_pc_region_to_non_hpc_region(self):
        """
        Change PC region to Vatican City region 
        """
        logging.info("Set PC region to Vatican City")
        self.driver.ssh.send_command('Set-WinHomeLocation -GeoId 253')

    def change_pc_region_to_us_region(self):
        """
        Change PC region to one of the United States region
        """
        logging.info("Set PC region to United States")
        self.driver.ssh.send_command('Set-WinHomeLocation -GeoId 244')

    def change_flag_param(self, flag_list, disable=True):
        self.check_flag_param(flag_list)
        if disable:
            org_param = 'true'
            new_param = 'false'
        else:
            org_param = 'false'
            new_param = 'true'
        if (fh := self.driver.ssh.remote_open(self.log_file, mode="r+", raise_e=False)):
            data = fh.read().decode("utf-8")
            fh.close()
            for flag in flag_list:
                data = re.sub('"{}": {}'.format(self.flag_dict[flag], org_param), '"{}": {}'.format(self.flag_dict[flag], new_param), data)
                if flag in ["printphotos", "printpdf"]:
                    data = re.sub('"printer-x-localprint": {}', '"printer-x-localprint": {}'.format(org_param, new_param), data)
            fh = self.driver.ssh.remote_open(self.log_file, mode="w")
            fh.write(data)
            fh.close()

    def check_flag_state(self, flag_list):
        if (fh := self.driver.ssh.remote_open(self.log_file, mode="r+", raise_e=False)):
            data = fh.read().decode("utf-8")
            check_info = []
            for flag in flag_list:
                result = re.search('"{}": [a-z]+'.format(self.flag_dict[flag]), data)
                if result is not None:
                    check_info.append(result.group())
            fh.close()
            return check_info
    
    def check_flag_param(self, flag_list):
        if (fh := self.driver.ssh.remote_open(self.log_file, mode="r+", raise_e=False)):
            data = fh.read().decode("utf-8")
            fh.close()
            mt_list = []
            for flag in flag_list:
                if self.flag_dict[flag] not in data:
                    mt_list.append(flag)
                    data = re.sub('\n\s+}\n}', ',\n\t"{}": true\n  }}\n}}'.format(self.flag_dict[flag]), data)

            fh = self.driver.ssh.remote_open(self.log_file, mode="w")
            fh.write(data)
            fh.close()
            logging.info("Add missing param with true flag in json file: {}".format(mt_list))
    
    def check_log_event(self, check_event, check_file='oobe', raise_e=True):
        if check_file == 'oobe':
            log_file = self.oobe_log_file
        if (fh := self.driver.ssh.remote_open(log_file, mode="r+", raise_e=False)):
            data = fh.read().decode("utf-8")
            fh.close()
            if not re.search(check_event, data):
                if raise_e is False:
                    return False
                else:
                    raise NoSuchElementException(
                        "Fail to found {0} in {1}".format(check_event, log_file))