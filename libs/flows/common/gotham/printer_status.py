import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
from selenium.common.exceptions import NoSuchElementException
from SAF.misc.excel import Excel
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from selenium.webdriver.common.keys import Keys
import re
import time
import logging
import os

class NoSuchFileException(Exception):
    pass

class NoSuchIorefException(Exception):
    pass

class NotEqualException(Exception):
    pass

class PrinterStatus(GothamFlow):
    flow_name = "printer_status"
    sms_data = None
    action_center_file_path = None
    state_path = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH
    sms_path = w_const.TEST_DATA.SMS_PATH
    list_num = sms_ioref_index =sms_title_index = sms_body_index = sms_buttons_index = sms_icon_index = 0
    all_ioref_list = []

   # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def get_sms_data(self):
        file_path = ma_misc.get_abs_path(self.sms_path)
        print(file_path)
        print()
        # Make sure the latest spec file is used for the comparison
        logging.info("The latest spec file should be used for the comparison")
        for file_name in os.listdir(file_path):
            if 'sms202' in file_name:
                excel = Excel(file_path + file_name)
                print(file_path + file_name)
                excel.load_workbook()
                excel.load_sheet("Spec")
                self.sms_data = excel.current_sheet
                excel.save()
                logging.info("{} is used to compare the printer status".format(file_name))
                break
        else:
            raise NoSuchFileException("Fail to find sms file")
        
    def get_action_center_file_path(self, serial_number):
        file_name_list = ((self.driver.ssh.send_command("Get-ChildItem " + self.state_path + "| Select-Object 'name'"))["stdout"]).split('\n')
        for file_name in file_name_list:
            if re.search(r'[a-zA-Z ]+[0-9]{3,4}', file_name):
                self.action_center_file_path = self.state_path + "\\" + file_name.strip() + "\\" + serial_number + '\\' + "ActionCenter.xml"
                break
        else:
            raise NoSuchFileException("Fail to created ActionCenter.xml")

    def enable_printer_status(self, serial_number, ioref_list):
        self.get_action_center_file_path(serial_number)
        fh = self.driver.ssh.remote_open(self.action_center_file_path, mode="r+", raise_e=False)
        data = fh.read().decode("utf-8")
        fh.close()
        data = re.sub("<Flags>.*?</Flags>", "<Flags>15</Flags>", data)
        if ioref_list is not False:
            data = re.sub("<IORefSubset />", "<IORefSubset><int></int></IORefSubset>", data)
            for ioref in ioref_list:
                data = re.sub("<int></int>", "<int>{}</int><int></int>".format(ioref), data)
            data = re.sub("<int></int>", "", data)
        fh = self.driver.ssh.remote_open(self.action_center_file_path, mode="w")
        fh.write(data)
        fh.close()
        time.sleep(1)
        self.get_sms_data()
        self.get_sms_columns_index()

    def remove_action_center_file(self):
        file_name_list = ((self.driver.ssh.send_command("Get-ChildItem " + self.state_path + "| Select-Object 'name'"))["stdout"]).split('\n')
        for file_name in file_name_list:
            if re.search(r'[a-zA-Z ]+[0-9]{3,4}', file_name):
                self.driver.ssh.send_command('Remove-Item -Path "{}" -Recurse -Force'.format(self.state_path + "\\" + file_name.strip()))

    def get_sms_columns_index(self):
        check_list = ['I/O Ref', 'HP Smart (Gotham) Short Title', 'HP Smart (Gotham) Body Text', 'New Gotham button column (order, primary/secondary, etc.)', 'Header Icon']
        for row in self.sms_data.values:
            if set(check_list) <= set(list(row)):
                self.sms_ioref_index = list(row).index('I/O Ref')       
                self.sms_title_index = list(row).index('HP Smart (Gotham) Short Title')
                self.sms_body_index = list(row).index('HP Smart (Gotham) Body Text')
                self.sms_buttons_index = list(row).index('New Gotham button column (order, primary/secondary, etc.)')
                self.sms_icon_index = list(row).index('Header Icon')
                break            
        else:
            raise NoSuchElementException("columns string are incorrect")

    def get_all_ioref_list(self):
        fh = self.driver.ssh.remote_open(self.action_center_file_path, mode="r+", raise_e=False)
        data = fh.read().decode("utf-8")
        fh.close()
        self.all_ioref_list = re.findall("<IORef>([0-9]{5})</IORef>", data)
        return self.all_ioref_list

    def convert_string(self, convert_str, sms_str=True):
        if sms_str:
            convert_str = convert_str.replace('[hyperlink]', '').replace('[Hyperlink:]', '').replace('<hyperlink>', '').replace('cartidge', 'cartridge').replace('cartrigdes', 'cartridges').replace('<https://www.hpinstantink.com>', '').replace('<www.hp.com/recycle> ', '')
            convert_pattern_1 = re.compile(r'\b([A-Za-z"]+)(\s{1,2},)(.*?)', re.M)
            convert_str = re.sub(convert_pattern_1, r'\g<1>,', convert_str)
            convert_pattern_2 = re.compile(r'\b([A-Za-z"/]+)(\s){2,}(?=[A-Za-z"]+\b)', re.M)
            convert_str = re.sub(convert_pattern_2, r'\g<1> ', convert_str)
        convert_pattern_1 = re.compile(r'\b([A-Za-z"/]+)(\s){2}(?=[A-Za-z"]+\b)', re.M)
        convert_str = re.sub(convert_pattern_1, r'\g<1> ', convert_str)
        convert_pattern_2 = re.compile(r'\b([A-Za-z"]+)(,)(?=[A-Za-z"]+\b)', re.M)
        convert_str = re.sub(convert_pattern_2, r'\g<1>, ', convert_str)
        convert_pattern_3 = re.compile(r'\b([A-Za-z"]+)(,  )(?=[A-Za-z"]+\b)', re.M)
        convert_str = re.sub(convert_pattern_3, r'\g<1>, ', convert_str)
        convert_pattern_4 = re.compile(r'\b([A-Za-z"]+)(:  )(?=[A-Za-z"]+\b)', re.M)
        convert_str = re.sub(convert_pattern_4, r'\g<1>: ', convert_str)
        
        return convert_str

    def click_ps_middle_body(self):
        self.driver.click("middle_status_list")

    def click_ps_body_btn(self, btn, raise_e=True):
        return self.driver.click("right_body_btn", format_specifier=[btn], raise_e=raise_e)

    def click_more_info_ok_btn(self):
        self.driver.click("dialog_ok_btn")
    
    def click_ps_body_link(self, link):
        self.driver.click("right_body_link", format_specifier=[link], displayed=False)

    def click_info_x_btn(self, ioref):
        self.driver.click("middle_info_close_btn", format_specifier=[ioref])

    def hover_ioref_item(self, ioref):
        self.driver.hover("status_ioref_item", format_specifier=[ioref])

    def click_ps_ioref_item(self, ioref):
        if self.driver.click("status_ioref_item", format_specifier=[ioref], raise_e=False) is False:
            self.driver.click("middle_status_list")
            for _ in range(5):
                self.driver.swipe()
                time.sleep(1)
                if self.driver.click("status_ioref_item", format_specifier=[ioref], raise_e=False):
                    raise NoSuchIorefException("Fail to trigger {}".format(ioref))                 

    # *********************************************************************************
    #                                      VERIFICATION FLOWS                          *
    # *********************************************************************************
    def verify_printer_ioref_status_screen(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("middle_status_list",timeout=timeout, raise_e=raise_e)

    def verify_printer_ready_screen(self):
        self.driver.wait_for_object("printer_image")
        self.driver.wait_for_object("printer_status_icon")
        self.driver.wait_for_object("printer_status_text")
        self.driver.wait_for_object('printer_status_title_text', format_specifier=['Ready'])

    def verify_printer_offline_screen(self):
        self.driver.wait_for_object("printer_image")
        self.driver.wait_for_object("printer_status_icon")
        self.driver.wait_for_object("printer_status_text")
        self.driver.wait_for_object('printer_status_title_text', format_specifier=['Offline'])

    def verify_status_sorted_in_order(self, ioref, raise_e=True):
        return self.driver.wait_for_object("status_ioref_item", format_specifier=[ioref], timeout=3, raise_e=raise_e)

    # ********************************middle part text**************************************
    def verify_ps_middle_icon_image(self, ioref, row, sms_index):
            cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element('middle_icon_image', format_specifier=[ioref] ))
            cur_img = saf_misc.img_crop(cur_img, 0.0, 0.0, 0.0, 0.0)
            if str(list(row)[sms_index].strip()) == "Error":
                toggle_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.STATUS_IMAGE + 'error_middle_ioref.png'))
                assert self.driver.wait_for_object("middle_info_close_btn", format_specifier=[ioref], raise_e=False) is False
            elif str(list(row)[sms_index].strip()) == "Warning":
                toggle_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.STATUS_IMAGE + 'warning_middle_ioref.png'))
                assert self.driver.wait_for_object("middle_info_close_btn", format_specifier=[ioref], raise_e=False) is False
            elif str(list(row)[sms_index].strip()) in ["Inform", "OK", "Info", "Advisement"]:
                toggle_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.STATUS_IMAGE + 'inform_middle_ioref.png'))
                info_x_btn = self.driver.wait_for_object('middle_info_close_btn', format_specifier=[ioref], raise_e=False)
                if info_x_btn is False:
                    raise NoSuchElementException("{0} X button is not found".format(ioref))
            else:
                raise NoSuchElementException('{0} stautus icon is not found'.format(ioref)) 
        
            assert saf_misc.img_comp(cur_img, toggle_img) < 0.4  
                
    def verify_ps_middle_title_text(self, ioref, row, sms_index):
        title_text = self.driver.get_attribute("middle_title_text", format_specifier=[ioref] , attribute="Name", raise_e=False)
        title_text = self.convert_string(title_text, sms_str=False).strip()
        sms_text = list(row)[sms_index].strip()
        sms_text = self.convert_string(sms_text).strip()
        if title_text != sms_text:
            if ioref in ['66130']:
                logging.warning("{} title exist format issue".format(ioref))
            else:  
                raise NotEqualException('"{0}" middle title "{1}" is not equal to "{2}"'.format(ioref, title_text, list(row)[sms_index].strip()))

    def verify_ps_middle_body_text(self, ioref, row, sms_index):
        sms_text = list(row)[sms_index].strip()
        sms_text = self.convert_string(sms_text).strip()
        if ioref in ['66705']:
            sms_text = sms_text.replace('Manally', 'Manually')
        body_content = self.driver.get_attribute("middle_body_text", format_specifier=[ioref] , attribute="Name", raise_e=False)
        body_content = self.convert_string(body_content, sms_str=False)
        if body_content:
            body_content_list = []
            if '.' in body_content:
                for x in body_content.split('.'):
                    body_content_list.append(x.strip())                      
            elif body_content != "":
                body_content_list.append(body_content)
            for body_text in body_content_list:
                if ioref == '66353':
                    body_text = re.sub(r"printer([\s\S]{1})s", r"printer's", body_text)
                if ioref == '66292':
                    body_text = body_text.replace(' by HP', '')
                if body_text not in sms_text:
                    raise NotEqualException('"{0}" middle text "{1}" is not in "{2}"'.format(ioref, body_text, list(row)[sms_index].strip()))
        else:
            raise NotEqualException('"{0}" middle body text is empty'.format(ioref))
    
    # ********************************right part text**************************************
    def verify_ps_right_icon_image(self, ioref, row, sms_index):
        cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element('right_icon_image'))
        cur_img = saf_misc.img_crop(cur_img, 0.0, 0.0, 0.0, 0.0)
        if str(list(row)[sms_index].strip()) == "Error":
            toggle_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.STATUS_IMAGE + 'error_right_ioref.png'))
        elif str(list(row)[sms_index].strip()) == "Warning":
            toggle_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.STATUS_IMAGE + 'warning_right_ioref.png'))
        elif str(list(row)[sms_index].strip()) in ["Inform", "OK", "Info", "Advisement"]:
            toggle_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.STATUS_IMAGE + 'inform_right_ioref.png'))
        else:
            raise NoSuchElementException('{0} stautus icon is not found'.format(ioref))
        
        assert saf_misc.img_comp(cur_img, toggle_img) < 0.4 

    def verify_ps_right_title_text(self, ioref, row, sms_index):
        title_text = self.driver.get_attribute("right_title_text" , attribute="Name", raise_e=False)
        title_text = self.convert_string(title_text, sms_str=False).strip()
        sms_text = list(row)[sms_index].strip()
        sms_text = self.convert_string(sms_text).strip()
        if title_text != sms_text:
            if ioref in ['66130']:
                logging.warning("{} title exist format issue".format(ioref))
            else: 
                raise NotEqualException('{0} body title "{1}" is not equal to "{2}"'.format(ioref, title_text, list(row)[sms_index].strip()))

    def verify_ps_right_body_text(self, ioref, row, sms_index):
        sms_text = list(row)[sms_index].strip()
        sms_text = self.convert_string(sms_text).strip()
        if ioref in ['66325', '66360', '66371','66372', '66373', '66378', '66379']:
            sms_text = sms_text.replace('click Explore Options', 'click Get Supplies').replace('innacurate', 'inaccurate').replace('at:', 'at')
        elif ioref in ['66065']:
            sms_text = sms_text.replace('autopmatically', 'automatically')
        elif ioref in ['66066']:
            sms_text = sms_text.replace('<Power icon> (the Power button)', 'the Power button')
        elif ioref in ['66705']:
            sms_text = sms_text.replace('Manally', 'Manually')
        elif ioref in ['66430']:
            sms_text = sms_text.replace('HP ink cartridges', 'HP cartridges')
        elif ioref in ['65618', '65785']:
            sms_text = sms_text.replace('using black ink', 'using Black ink')
        elif ioref in ['65966']:
            sms_text = sms_text.replace('Enroll at hpinstantink.com/bundle', 'Enroll at www.hpinstantink.com/bundle')
        elif ioref in ['65738', '65740', '65742']:
            sms_text = sms_text.replace(' [actual URL: www.hpinstantink.com <https://www.hpinstantink.com/> ]', '')   
        body_content = self.driver.get_attribute("right_body_text", attribute="Name", raise_e=False)
        body_content = self.convert_string(body_content, sms_str=False)
        if body_content:
            temp_list = [x.strip() for x in body_content.split('\n')]
            body_content_list = []
            for body_content in temp_list:
                if '.' in body_content:
                    for x in body_content.split('.'):
                        body_content_list.append(x.strip())             
                elif body_content != "":
                    body_content_list.append(body_content)
            for body_text in body_content_list:
                if ioref == '66258':
                    body_text = body_text.replace('More Information You', 'You')
                elif ioref == '66353':
                    body_text = re.sub(r"printer([\s\S]{1})s", r"printer's", body_text)
                elif ioref in ['65906', '65910']:
                    body_text = body_text.replace(r'“', r'"').replace(r'”', r'"')
                if body_text not in sms_text:
                    raise NotEqualException('{0} body text "{1}" is not in "{2}"'.format(ioref, body_text, sms_text))
        else:
            raise NotEqualException('"{0}" right body text is empty'.format(ioref))
        
    def verify_right_body_btn(self, ioref, row, sms_index):
        btn_list = re.findall(r'"(.*?)"', list(row)[sms_index].strip())
        if ioref == '66245':
            for _ in range(5):
                self.driver.swipe()
                time.sleep(1)
        if ioref == '66495':
            btn_list.remove('Later')
        for each_btn in btn_list:
            right_btn = self.driver.wait_for_object('right_body_btn', format_specifier=[each_btn], raise_e=False)
            if right_btn is False:
                raise NoSuchElementException("{0} button {1} is not found".format(ioref, each_btn))
        if self.driver.wait_for_object('right_body_btn', format_specifier=['Estimated Supplies Levels'], raise_e=False):
            raise NoSuchElementException("'Estimated Supplies Levels' button in {} should be moved".format(ioref))

    def check_right_body_btn(self):
        all_btn = []
        check_btn_list = ['Get More Help', 'Get Supplies', 'Estimated Supply Levels']
        for check_btn in check_btn_list:
            if self.driver.wait_for_object("right_body_btn", format_specifier=[check_btn], timeout=3, raise_e=False):
                all_btn.append(check_btn)
        return all_btn

    def check_right_body_link(self):
        all_link = []
        check_link_list = ['www.hp.com/recycle', 'www.hp.com/go/anticounterfeit', 'More Information', 'View HP Privacy Statement Online', 'HP', 'HP Instant Ink', 'www.hpinstantink.com', 'View More Information online', 'www.hpinstantink.com/enroll', 'www.hpinstantink.com/bundle', 'hp.com/plus-support', 'www.support.hp.com', 'www.hpsmart.com', 'www.hp.com/contactHP', 'https://instantink.hpconnected.com/', 'www.hp.com/learn/ds', 'here', 'https://www8.hp.com/us/en/privacy/limited_warranty.html', 'hp.com/support/printer-setup', 'www.hpsmart.com/wireless-printing']
        for check_link in check_link_list:
            if self.driver.wait_for_object("right_body_link", format_specifier=[check_link], timeout=2, raise_e=False):
                all_link.append(check_link)
        return all_link

    def verify_your_privacy_is_screen(self, raise_e=True):
        return self.driver.wait_for_object('dialog_ok_btn', timeout=3, raise_e=raise_e)
    
    def verify_content_text(self, ioref):
        for row in self.sms_data.values:
            if str(ioref) in str(list(row)[self.sms_ioref_index]):
                if str(list(row)[self.sms_title_index]) not in ["NOT_USED", 'None', '', 'See the other, not-mono, version of this IOREF']:
                    if str(list(row)[self.sms_icon_index]) not in ["No Header Icon", 'None', '']:
                        self.verify_ps_middle_icon_image(ioref, row, self.sms_icon_index)
                        self.verify_ps_right_icon_image(ioref, row, self.sms_icon_index)
                    self.verify_ps_middle_title_text(ioref, row, self.sms_title_index)
                    self.verify_ps_right_title_text(ioref, row, self.sms_title_index)                  
                if str(list(row)[self.sms_body_index]) not in ["NOT_USED", 'None', '', 'Unsupported', 'See the other, not-mono, version of this IOREF']:
                    self.verify_ps_middle_body_text(ioref, row, self.sms_body_index)
                    self.verify_ps_right_body_text(ioref, row, self.sms_body_index)
                    if str(list(row)[self.sms_buttons_index]) not in ['NOT_USED', 'None']:
                        self.verify_right_body_btn(ioref, row, self.sms_buttons_index)
                break
        else:
            logging.warning("Fail to found {} in SMS".format(ioref))
        
    def check_ps_content_all(self, ioref):
        try:
            if ioref not in ['66650']:
                self.driver.click("status_ioref_item", format_specifier=[ioref], raise_e=False)
                self.verify_content_text(ioref)
        finally:
            el = self.driver.wait_for_object("status_ioref_item", format_specifier=[ioref], timeout=2)
            el.send_keys(Keys.DOWN)