import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow
from selenium.common.exceptions import NoSuchElementException
from SAF.misc.excel import Excel
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from selenium.webdriver.common.keys import Keys
import pytest
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

class IorefData():
    @staticmethod
    def get_ioref_list(num):
        all_ioref_list = ['65536', '65537', '65538', '65539', '65541', '65542', '65543', '65544', '65546', '65547', '65548', '65549', '65550', '65551', '65553', '65554', '65557', '65558', '65559', '65561', '65563', '65564', '65566', '65567', '65568', '65569', '65570', '65571', '65572', '65573', '65574', '65578', '65579', '65580', '65581', '65582', '65583', '65584', '65585', 
'65586', '65587', '65588', '65589', '65590', '65591', '65592', '65593', '65594', '65595', '65596', '65597', '65598', '65599', '65602', '65603', '65604', '65605', '65606', '65607', '65608', '65610', '65611', '65612', '65613', '65614', '65616', '65617', '65618', '65619', '65621', '65628', '65629', '65634', '65639', '65640', '65660', '65669', '65670', '65671', '65672', '65674', '65675', '65676', '65677', '65679', '65680', '65681', '65682', '65683', '65684', '65685', '65686', '65687', '65688', '65689', '65690', '65691', '65692', '65693', '65694', '65695', '65696', '65697', '65698', '65699', '65701', '65702', '65703', '65709', '65710', '65711', '65712', '65713', '65716', '65717', '65719', '65723', '65724', '65725', '65726', '65728', '65729', '65730', '65732', '65733', '65734', '65736', '65737', '65738', '65739', '65740', '65741', '65742', '65743', '65744', '65746', '65747', '65748', '65749', '65750', '65751', '65760', '65763', '65764', '65765', '65766', '65767', '65768', '65769', '65770', '65771', '65772', '65773', '65774', '65776', '65777', '65778', '65779', '65780', '65781', '65782', '65783', '65784', '65785', '65786', '65787', '65788', '65789', '65790', '65791', '65792', '65794', '65796', '65797', '65799', '65800', '65802', '65803', '65804', '65805', '65806', '65807', '65808', '65809', '65810', '65811', '65815', '65845', '65846', '65847', '65848', '65849', '65850', '65851', '65853', '65858', '65859', '65860', '65862', '65863', '65864', '65869', '65870', '65875', '65888', '65899', '65901', '65902', '65904', '65905', '65906', '65909', '65910', '65911', '65912', 
'65914', '65916', '65920', '65921', '65923', '65926', '65933', '65934', '65935', '65939', '65940', '65942', '65965', '65966', '65968', '65969', '65970', '65973', '65989', '65990', '65991', '65992', '65993', '65994', '65995', '65996', '65997', '65998', '65999', '66000', '66001', '66002', '66008', '66009', '66011', '66012', '66013', '66015', '66016', '66017', '66018', '66019', '66020', '66021', '66022', '66023', '66024', '66025', '66026', '66027', '66028', '66029', '66030', '66031', '66032', '66033', '66034', '66035', '66036', '66037', '66038', '66039', '66040', '66042', '66043', '66044', '66045', '66046', '66047', '66049', '66050', '66051', '66052', '66053', '66054', '66055', '66056', '66057', '66058', '66059', '66060', '66061', '66063', '66064', '66065', '66066', '66067', '66068', '66069', '66071', '66072', '66073', '66074', '66081', '66084', '66085', '66086', '66087', '66089', '66090', '66092', '66093', '66095', '66096', '66098', '66099', '66101', '66121', '66128', '66129', '66130', '66131', '66135', '66136', '66137', '66155', '66156', '66157', '66158', '66159', '66160', '66161', '66162', '66168', '66169', '66170', '66171', '66172', '66173', '66174', '66175', '66176', '66177', '66207', '66208', '66209', '66211', '66212', '66213', '66214', '66215', '66216', '66217', '66218', '66219', '66220', '66221', '66222', '66223', '66228', '66229', '66230', '66231', '66233', '66234', '66235', '66236', '66237', '66241', '66242', '66243', '66244', '66245', '66246', '66247', '66248', '66249', '66250', '66251', '66252', '66253', '66255', '66256', '66257', '66258', '66259', 
'66260', '66261', '66262', '66263', '66264', '66265', '66266', '66267', '66268', '66269', '66270', '66271', '66272', '66273', '66275', '66276', '66277', '66278', '66279', '66280', '66281', '66282', '66283', '66284', '66285', '66286', '66287', '66288', '66289', '66290', '66291', '66292', '66293', '66294', '66295', '66296', '66297', '66298', '66299', '66300', '66301', '66302', '66303', '66304', '66305', '66306', '66307', '66310', '66311', '66312', '66313', '66314', '66315', '66316', '66317', '66318', '66319', '66320', '66321', '66322', '66323', '66324', '66325', '66327', '66328', '66329', '66330', '66331', '66332', '66333', '66334', '66335', '66336', '66337', '66338', '66339', '66340', '66341', '66342', '66343', '66344', '66345', '66346', '66348', '66349', '66350', '66351', '66352', '66353', '66354', '66355', '66359', '66360', '66367', '66370', '66371', '66372', '66373', '66378', '66379', '66383', '66384', '66385', '66386', '66387', '66388', '66391', '66395', '66396', '66400', '66401', '66407', '66408', '66409', '66410', '66412', '66413', '66415', '66416', '66417', '66419', '66420', '66421', '66422', '66423', '66424', '66425', '66426', '66427', '66428', '66429', '66430', '66431', '66432', '66434', '66435', '66437', '66438', '66439', '66440', '66441', '66442', '66443', '66444', '66445', '66446', '66447', '66448', '66449', '66450', '66451', '66452', '66453', '66455', '66458', '66459', '66460', '66461', '66462', '66463', '66465', '66466', '66467', '66468', '66469', '66470', '66471', '66472', '66473', '66474', '66475', '66476', '66477', '66478', '66479', '66481', 
'66483', '66484', '66485', '66486', '66488', '66489', '66490', '66491', '66492', '66493', '66494', '66495', '66496', '66497', '66498', '66499', '66500', '66501', '66502', '66503', '66504', '66505', '66506', '66507', '66508', '66509', '66510', '66511', '66512', '66513', '66514', '66515', '66516', '66524', '66526', '66527', '66529', '66535', '66537', '66538', '66539', '66540', '66548', '66549', '66551', '66553', '66555', '66557', '66560', '66562', '66564', '66565', '66566', '66567', '66568', '66569', '66575', '66577', '66578', '66579', '66580', '66581', '66582', '66583', '66584', '66585', '66586', '66587', '66588', '66589', '66590', '66591', '66592', '66593', '66594', '66595', '66596', '66597', '66598', '66599', '66600', '66601', '66602', '66603', '66604', '66605', '66606', '66607', '66608', '66609', '66610', '66613', '66614', '66615', '66616', '66617', '66618', '66623', '66626', '66627', '66628', '66629', '66630', '66631', '66632', '66633', '66635', '66637', '66638', '66639', '66640', '66641', '66642', '66643', '66644', '66645', '66647', '66648', '66649', '66650', '66651', '66652', '66653', '66655', '66656', '66657', '66658', '66659', '66660', '66661', '66662', '66663', '66664', '66665', '66668', '66670', '66672', '66673', '66674', '66675', '66676', '66677', '66678', '66679', '66680', '66681', '66682', '66683', '66684', '66685', '66687', '66688', '66689', '66690', '66692', '66693', '66694', '66695', '66696', '66699', '66700', '66701', '66703', '66705', '66708', '66709', '66710', '66711', '66712', '66713', '66714', '66716', '66717', '66718', '66719', '66720', 
'66721', '66723', '66726', '66727', '66731', '66732', '66733', '66734', '66735', '66736', '66737', '66738', '66745', '66746', '66747', '66748', '66749', '66750', '66752', '66753', '66754', '66755', '66756', '66758', '66759', '66760', '66761', '66762', '66763', '66791', '66792', '66795', '66797', '66798', '66799', '66805', '66806', '66807', '66813', '66817', '66818', '66820', '66821', '66822', '66823', '66824', '66825', '66826', '66827', '66828', '66829', '66830', '66831', '66832', '66833', '66837', '66838', '66841', '66842', '66843', '66844', '66845', '66846', '66847', '66848', '66850', '66851', '66852', '66853', '66854', '66855', '66856', '75000', '75001', '75010', '75011', '75015', '75016', '75020', '75021', '75025', '75026', '75030', '75031', '75035', '75036', '75040', '75041', '75045', '75060', '75065', '75066', '75067', '75068', '75070', '75085', '75095', '75096', '75100', '75105', '75106', '75115', '75120', '75125', '75135', '75136', '75145', '75170', '75171', '75172', '75175', '75190', '75191', '75200', '85001', '85002', '85003', '85004', '85005', '85006', '85007', '85008', '85009', '85010', '85011', '85012', '85013', '85014', '85015', '85016', '85017', '85018', '85019']
        split_size = len(all_ioref_list) // 15
        if num == 15:
            return all_ioref_list[split_size * (num-1) : ]
        else:
            return all_ioref_list[split_size * (num-1) : split_size * num]
    
    
    #OK/Get More Help/Get Supplies/Continue
    list_error_btn = ['66040', '65679']
    # OK/Get More Help/Get Supplies/Yes/No/Later
    list_info_btn = ['65553', '66720']
    # "OK/Get More Help/Get Supplies/Yes/No/Align/Later/view Information/Retry/Continue/Use Black Only/Use Color Only
    list_warning_btn = ['65593', '65595', '65611', '65685', '65914', '65691', '65692', '66267', '66495']

    '''
    Error:
    65543: HP Support
    65674: www.hp.com/recycle   HP Instant Ink
    65699: HP
    65765: www.hpinstantink.com
    65790: www.hp.com/go/anticounterfeit
    65965: www.hpinstantink.com/enroll
    65966: www.hpinstantink.com/bundle
    66039: HP Supplies Recycling
    66169: hp.com/plus-support
    66213: www.support.hp.com
    66251: www.hpsmart.com
    66317: www.hp.com/contactHP
    66329: https://instantink.hpconnected.com/
    66339: www.hp.com/learn/ds
    66360: www.hp.com/recycle   View HP Privacy Statement Online
    66435: hpsmart.com/activate    hp.com/support/printer-setup
    66820: HP All-In Plan account
    66824: HP All-In Plan
    '''
    list_error_link = ['65543', '65674', '65699', '65765', '65790', '65966', '66039', '66169', '66213', '66251', '66317', '66329', '66339', '66360', '66435', '66820', '66824']
    '''
    Info:
    65559: www.hp.com/go/anticounterfeit
    65698: www.hp.com/recycle    HP Instant Ink
    65851: www.hpinstantink.com
    66321: www.hp.com/recycle   www.hpsmart.com
    66350: www.hp.com/learn/ds   here
    66419: https://www8.hp.com/us/en/privacy/limited_warranty.html
    66653: www.hpsmart.com/wireless-printing
    '''
    list_info_link = ['65559', '65698', '65851', '66321', '66350', '66419', '66653']
    '''
    Warning:
    65593: www.hp.com/go/anticounterfeit
    65595: More Information   View HP Privacy Statement Online
    65805: www.hp.com/recycle  HP Instant Ink
    65912: View More Information online
    65934: www.hpinstantink.com/enroll
    66168: hp.com/plus-support
    66252: www.hpsmart.com
    66316: www.hp.com/contactHP
    66328: https://instantink.hpconnected.com/
    66438: hp.com/support/printer-setup
    66798: print quality tools
    '''
    list_warning_link = ['65593', '65595', '65805', '65912', '66168', '66252', '66316', '66328', '66438', '66798']

class PrinterStatus(HPXFlow):
    flow_name = "printer_status"
    sms_data = None
    action_center_file_path = None
    state_path = w_const.TEST_DATA.HPX_APP_LOG_PATH
    sms_path = w_const.TEST_DATA.SMS_PATH
    image_path = w_const.TEST_DATA.HPX_SCREENSHOT_PATH + 'printer_status/'
    list_num = sms_ioref_index = sms_title_index = sms_body_index = sms_btn_index = sms_icon_index = 0
    all_ioref_list = []
    ioref_dict = {}
    
    # ****************************sms file************************************
    def generate_sms_ioref_dict(self):
        file_path = ma_misc.get_abs_path(self.sms_path)
        # Make sure the latest spec file is used for the comparison
        for file_name in os.listdir(file_path):
            if 'Status Message Spec' in file_name:
                excel = Excel(file_path + file_name)
                logging.info(file_path + file_name)
                excel.load_workbook()
                excel.load_sheet("Spec")
                self.sms_data = excel.current_sheet
                excel.save()
                break
        else:
            raise NoSuchFileException("Fail to find sms file")
        
        # get the needed column index
        check_flag=False
        for row in self.sms_data.values:
            for i, x in enumerate(list(row)):
                if re.search(r'HP Smart(.*?)Gotham(.*?)Title(.*?)', str(x)):
                    self.sms_ioref_index = list(row).index('I/O Ref')
                    self.sms_icon_index = list(row).index('Header Icon')
                    self.sms_title_index = i
                    self.sms_body_index = i+1
                    self.sms_btn_index = i+2
                    check_flag=True
                    break       
            if check_flag:
                break
        else:
            raise NoSuchElementException("columns string are incorrect")

        # generate a dictionary for all required data
        for row in self.sms_data.values:
            ioref = str(list(row)[self.sms_ioref_index]).strip()
            if ioref.isdigit():
                temp_dict = {} 
                temp_dict['title_text']= str(list(row)[self.sms_title_index]).strip()
                temp_dict['body_text'] = str(list(row)[self.sms_body_index]).strip()
                temp_dict['btn_text'] = str(list(row)[self.sms_btn_index]).strip()
                temp_dict['icon_text'] = str(list(row)[self.sms_icon_index]).strip()
                self.ioref_dict[ioref] = temp_dict
        return self.ioref_dict
        
    # ****************************ActionCenter file************************************
    def get_action_center_file_path(self, serial_number, timeout=30):
        start_time = time.time()
        while time.time() - start_time < timeout:
            file_name_list = ((self.driver.ssh.send_command("Get-ChildItem " + self.state_path + "| Select-Object 'name'"))["stdout"]).split('\n')
            for file_name in file_name_list:
                if re.search(r'[a-zA-Z ]+[0-9]{3,4}', file_name):
                    self.action_center_file_path = self.state_path + "\\" + file_name.strip() + "\\" + serial_number + '\\' + "ActionCenter.xml"
                    # Check if the file exists
                    result = self.driver.ssh.send_command('Test-Path "{}"'.format(self.action_center_file_path))
                    if "True" in result["stdout"]:
                        logging.info(f"Found ActionCenter.xml at: {self.action_center_file_path}")
                        return
            time.sleep(2)
        raise NoSuchFileException("Fail to created ActionCenter.xml")
        
    def enable_printer_status(self, serial_number, ioref_list=None):
        self.get_action_center_file_path(serial_number, timeout=30)
        fh = self.driver.ssh.remote_open(self.action_center_file_path, mode="r+", raise_e=False)
        data = fh.read().decode("utf-8")
        fh.close()
        data = re.sub("<Flags>.*?</Flags>", "<Flags>15</Flags>", data)
        if ioref_list:
            data = re.sub("<IORefSubset />", "<IORefSubset><int></int></IORefSubset>", data)
            for ioref in ioref_list:
                data = re.sub("<int></int>", "<int>{}</int><int></int>".format(ioref), data)
            data = re.sub("<int></int>", "", data)
        fh = self.driver.ssh.remote_open(self.action_center_file_path, mode="w")
        fh.write(data)
        fh.close()
        time.sleep(1)
        self.generate_sms_ioref_dict()

    def remove_action_center_file(self):
        file_name_list = ((self.driver.ssh.send_command("Get-ChildItem " + self.state_path + "| Select-Object 'name'"))["stdout"]).split('\n')
        for file_name in file_name_list:
            if re.search(r'[a-zA-Z ]+[0-9]{3,4}', file_name):
                self.driver.ssh.send_command('Remove-Item -Path "Verify {}" -Recurse -Force'.format(self.state_path + "\\" + file_name.strip()))

    def get_all_ioref_list(self):
        fh = self.driver.ssh.remote_open(self.action_center_file_path, mode="r+", raise_e=False)
        data = fh.read().decode("utf-8")
        fh.close()
        self.all_ioref_list = re.findall("<IORef>([0-9]{5})</IORef>", data)
        return self.all_ioref_list

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_ps_ioref_list(self):
        self.driver.click("middle_status_list")

    def click_ps_ioref_item(self, ioref):
        if self.driver.click("status_ioref_item", format_specifier=[ioref], raise_e=False) is False:
            self.driver.click("middle_status_list")
            self.driver.swipe(distance=10)
            time.sleep(1)
            if self.driver.click("status_ioref_item", format_specifier=[ioref], raise_e=False):
                raise NoSuchIorefException("Fail to trigger IORef {}".format(ioref))

    def hover_ioref_item(self, ioref):
        self.driver.hover("status_ioref_item", format_specifier=[ioref])

    def click_ps_body_btn(self, btn, raise_e=True):
        return self.driver.click("right_body_btn", format_specifier=[btn], raise_e=raise_e)

    def click_more_info_ok_btn(self):
        self.driver.click("dialog_ok_btn")
    
    def click_ps_body_link(self, link):
        self.driver.click("right_body_link", format_specifier=[link], displayed=False)

    def click_info_x_btn(self, ioref):
        self.driver.click("middle_info_close_btn", format_specifier=[ioref])

    def get_ps_icon_image(self, ioref, row):
        sms_icon_text = str(list(row)[self.sms_icon_index].strip())
        cur_img_m = saf_misc.load_image_from_base64(self.driver.screenshot_element('middle_icon_image', format_specifier=[ioref]))
        cur_img_r = saf_misc.load_image_from_base64(self.driver.screenshot_element('right_icon_image'))
        
        if sms_icon_text == "Error":
            icon_img_m = 'error_middle_ioref.png'
            icon_img_r = 'error_right_ioref.png'
        elif sms_icon_text == "Warning":
            icon_img_m = 'warning_middle_ioref.png'
            icon_img_r = 'warning_right_ioref.png'
        elif sms_icon_text == "Inform":
            icon_img_m = 'inform_middle_ioref.png'
            icon_img_r = 'inform_right_ioref.png'
        save_path_m = ma_misc.get_abs_path(self.image_path + icon_img_m)
        cur_img_m.save(save_path_m)

        save_path_r = ma_misc.get_abs_path(self.image_path + icon_img_r)
        cur_img_r.save(save_path_r)
        logging.info("screenshot Folder: " + self.image_path)
                 

    # *********************************************************************************
    #                                      VERIFICATION FLOWS                          *
    # *********************************************************************************
    def verify_ps_ioref_list(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("middle_status_list", timeout=timeout, raise_e=raise_e)

    def verify_ps_ready_screen(self, timeout=15, raise_e=True):
        self.driver.wait_for_object("printer_image", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("printer_status_icon", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("printer_status_text", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object('printer_status_title_text', format_specifier=['Ready'], timeout=timeout, raise_e=raise_e)

    def verify_ps_offline_screen(self, timeout=15, raise_e=True):
        self.driver.wait_for_object("printer_image", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("printer_status_icon", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("printer_status_text", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object('printer_status_title_text', format_specifier=['Offline'], timeout=timeout, raise_e=raise_e)

    def verify_status_sorted_in_order(self, ioref, raise_e=True):
        return self.driver.wait_for_object("status_ioref_item", format_specifier=[ioref], timeout=2, raise_e=raise_e)

    def verify_your_privacy_is_screen(self, raise_e=True):
        return self.driver.wait_for_object('dialog_ok_btn', timeout=2, raise_e=raise_e)
    
    # ********************************middle part text**************************************
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
    
    # ********************************Verify head icon**************************************
    def verify_ps_head_icon(self, ioref, sms_icon_text):
        """ 
        verify if the head icon of each message matches the SMS file
        """
        sms_icon = True
        if ioref == 66703:
            sms_icon_text = "Inform"
        if sms_icon_text == "Error":
            icon_img_m = 'error_middle_ioref.png'
            icon_img_r = 'error_right_ioref.png'
            # assert self.driver.wait_for_object("middle_info_close_btn", format_specifier=[ioref], timeout=2, raise_e=False) is False
        elif sms_icon_text == "Warning":
            icon_img_m = 'warning_middle_ioref.png'
            icon_img_r = 'warning_right_ioref.png'
            # assert self.driver.wait_for_object("middle_info_close_btn", format_specifier=[ioref], timeout=2, raise_e=False) is False
        elif sms_icon_text == "Inform":
            icon_img_m = 'inform_middle_ioref.png'
            icon_img_r = 'inform_right_ioref.png'
            # info_x_btn = self.driver.wait_for_object('middle_info_close_btn', format_specifier=[ioref], timeout=2, raise_e=False)
            # if info_x_btn is False:
            #     raise NoSuchElementException("{0}({1}) X button is not found".format(ioref, sms_icon_text)) 
        else:
            sms_icon = False
            logging.info('{0}({1}) no head icon in SMS'.format(ioref, sms_icon_text)) 
    
        if sms_icon:
            cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element('middle_icon_image', format_specifier=[ioref]))
            cur_img = saf_misc.img_crop(cur_img, 0.0, 0.0, 0.0, 0.0)
            icon_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(self.image_path + icon_img_m))
            assert saf_misc.img_comp(cur_img, icon_img) < 0.2

            cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element('right_icon_image'))
            cur_img = saf_misc.img_crop(cur_img, 0.0, 0.0, 0.0, 0.0)
            icon_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(self.image_path + icon_img_r))
            if saf_misc.img_comp(cur_img, icon_img) > 0.2:
                raise NotEqualException('\n {0}({1}) head icon is incorrect'.format(ioref, sms_icon_text))

    # ********************************Verify title**************************************
    def verify_ps_short_title(self, ioref, sms_title_text, sms_icon_text):
        sms_text = self.convert_string(sms_title_text).strip()
        if sms_text not in ['NOT_USED', 'None', '', 'See the other, not-mono, version of this IOREF']:
            title_text_m = self.driver.get_attribute("middle_title_text", format_specifier=[ioref], attribute="Name")
            title_text_m = self.convert_string(title_text_m, sms_str=False).strip()
            if title_text_m != sms_text:
                raise NotEqualException('\n middle item title -- {0}({1}):\n"{2}" is not equal to "{3}"'.format(ioref, sms_icon_text, title_text_m, sms_title_text))

            title_text_r = self.driver.get_attribute("right_title_text" , attribute="Name")
            title_text_r = self.convert_string(title_text_r, sms_str=False).strip()
            if title_text_r != sms_text:
                raise NotEqualException('\n right pane title -- {0}({1}):\n"{2}" is not equal to "{3}"'.format(ioref, sms_icon_text, title_text_r, sms_title_text))
        else:
            logging.info('{0}({1}) title text not used in SMS'.format(ioref, sms_icon_text)) 
    
    # ********************************Verify body text**************************************
    def verify_ps_body_text(self, ioref, sms_body_text, sms_icon_text):
        sms_text = self.convert_string(sms_body_text).strip()
        
        if sms_text not in ["NOT_USED", 'None', '', 'See the other, not-mono, version of this IOREF']:
            if ioref in ['66325', '66360', '66371','66372', '66373', '66378', '66379']:
                sms_text = sms_text.replace('click Explore Options', 'click Get Supplies').replace('innacurate', 'inaccurate').replace('at:', 'at')
            elif ioref in ['65543', '65676', '66213', '66676']:
                sms_text = sms_text.replace('<hp.com/support> ', '')
            elif ioref in ['66283', '66284', '66285', '66833']:
                sms_text = sms_text.replace('hp.com/support', 'HP Support')
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
            elif ioref in ['66820', '66821']:
                sms_text = sms_text.replace('<hpsmart.com/all-in-plan> ', '')
            elif ioref in ['66824']:
                sms_text = sms_text.replace('<https://www.hpsmart.com/all-in-plan> ', '')
            elif ioref in ['66842']:
                sms_text = sms_text.replace('tay jam', 'tray jam')
            elif ioref in ['65691']:
                sms_text = sms_text.replace('depeted', 'depleted')

            # verify middle item body text
            body_content = self.driver.get_attribute("middle_body_text", format_specifier=[ioref] , attribute="Name")
            body_content = self.convert_string(body_content, sms_str=False)
            if body_content:
                body_content_list = []
                if '.' in body_content:
                    for x in body_content.split('.'):
                        body_content_list.append(x.strip())                      
                elif body_content != "":
                    body_content_list.append(body_content)
                for body_text in body_content_list:
                    if ioref == '66720':
                        body_text = re.sub(r"printer([\s\S]{1})s", r"printer's", body_text)
                    if ioref == '66292':
                        body_text = body_text.replace(' by HP', '')
                    if body_text not in sms_text:
                        raise NotEqualException('\n middle item body text -- {0}({1}):\n"{2}" is not in "{3}"'.format(ioref, sms_icon_text, body_text, sms_body_text))
            else:
                raise NotEqualException('\n middle item body text -- {0}({1}): not found'.format(ioref, sms_icon_text))
        
            # verify right pane body text
            body_content = self.driver.get_attribute("right_body_text", attribute="Name")
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
                    elif ioref == '66720':
                        body_text = re.sub(r"printer([\s\S]{1})s", r"printer's", body_text)
                    elif ioref in ['65906', '65910']:
                        body_text = body_text.replace(r'“', r'"').replace(r'”', r'"')
                    if body_text not in sms_text:
                        raise NotEqualException('\n right pane body text -- {0}({1}):\n"{2}" is not in "{3}"'.format(ioref, sms_icon_text, body_text, sms_body_text))
            else:
                raise NotEqualException('\n right pane body text -- {0}({1}): not found'.format(ioref, sms_icon_text))
        else:
            logging.info('{0}({1}) body text not used in SMS'.format(ioref, sms_icon_text))

    # ********************************Verify button column**************************************
    def verify_button_column(self, ioref, sms_btn_text, sms_icon_text):
        if sms_btn_text not in ["NOT_USED", 'None', '', 'See the other, not-mono, version of this IOREF']:
            btn_list = re.findall(r'"(.*?)"', sms_btn_text)
            
            if ioref == '66245':
                self.driver.swipe(distance=10)
                time.sleep(1)
            for each_btn in btn_list:
                right_btn = self.driver.wait_for_object('right_body_btn', format_specifier=[each_btn], timeout=2, raise_e=False)
                if right_btn is False:
                    raise NoSuchElementException('{0}({1}) "{2}" button is not found'.format(ioref, sms_icon_text, each_btn))
            if self.driver.wait_for_object('right_body_btn', format_specifier=['Estimated Supplies Levels'], timeout=2, raise_e=False):
                raise NoSuchElementException('"Estimated Supplies Levels" button in {0}({1}) should be moved'.format(ioref, sms_icon_text))
        else:
            logging.info('{0}({1}) button not used in SMS'.format(ioref, sms_icon_text))

    def get_pane_body_btn(self, ioref):
        sms_icon_text = self.ioref_dict[ioref]['icon_text']
        logging.info("------{0}({1})------".format(ioref, sms_icon_text))
        sms_btn_text = self.ioref_dict[ioref]['btn_text']
        btn_list = re.findall(r'"(.*?)"', sms_btn_text)
        return btn_list

    # ********************************Verify hyperlink**************************************
    def get_pane_body_link(self):
        all_link = []
        check_link_list = ['www.hp.com/recycle', 'www.hp.com/go/anticounterfeit', 'More Information', 'View HP Privacy Statement Online', 'HP', 'HP Instant Ink', 'www.hpinstantink.com', 'View More Information online', 'www.hpinstantink.com/enroll', 'www.hpinstantink.com/bundle', 'hp.com/plus-support', 'www.support.hp.com', 'www.hpsmart.com', 'www.hp.com/contactHP', 'https://instantink.hpconnected.com/', 'www.hp.com/learn/ds', 'here', 'https://www8.hp.com/us/en/privacy/limited_warranty.html', 'hp.com/support/printer-setup', 'www.hpsmart.com/wireless-printing']
        for check_link in check_link_list:
            if self.driver.wait_for_object("right_body_link", format_specifier=[check_link], timeout=2, raise_e=False):
                all_link.append(check_link)
        return all_link

    # *************************Verify printer status screen*************************
    def verify_ps_content(self, ioref, ioref_list):
        self.scroll_element(ioref, ioref_list)
        if str(ioref) in self.ioref_dict.keys():
            self.driver.click("status_ioref_item", format_specifier=[ioref])
            sms_icon_text = self.ioref_dict[ioref]['icon_text']
            sms_title_text = self.ioref_dict[ioref]['title_text']
            sms_body_text = self.ioref_dict[ioref]['body_text']
            sms_btn_text = self.ioref_dict[ioref]['btn_text']

            logging.info("------{0}({1})------".format(ioref, sms_icon_text))
            if ioref not in ['65701']:
                self.verify_ps_head_icon(ioref, sms_icon_text)
            self.verify_ps_short_title(ioref, sms_title_text, sms_icon_text)                    
            self.verify_ps_body_text(ioref, sms_body_text, sms_icon_text)
            if sms_btn_text not in ['NOT_USED', 'None', 'N/A', 'See the other, not-mono, version of this IOREF']:
                self.verify_button_column(ioref, sms_btn_text, sms_icon_text)
        else:
            pytest.skip("Fail to found IORef {} from SMS Document".format(ioref))
            logging.info("Fail to found IORef {} from SMS Document".format(ioref))

    def scroll_element(self, ioref, ioref_list):
        index = ioref_list.index(ioref)
        if index > 0:
            ioref = ioref_list[index - 1]
            el = self.driver.wait_for_object("status_ioref_item", format_specifier=[ioref], timeout=2)
            el.send_keys(Keys.DOWN)

    # *************************"Get more help" webpage*************************
    def click_webpage_dialog_close_btn(self):
        self.driver.click("webpage_close_btn", raise_e=False, timeout=5)

    def verify_webpage_chatbot(self):
        self.driver.wait_for_object("chatbot_dialog", timeout=5)
