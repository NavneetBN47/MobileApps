import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_03_Pepto_Scan_Preview_Edit(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.print = cls.fc.fd["print"]
        cls.check_auto_heal={}

        cls.build_version = (cls.driver.session_data["app_info"])[pytest.app_info].split('-')[1]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_add_printer_and_enable_pepto(self):
        """
        Enable the Pepto log.
        Launch the app to Main UI
        """  
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        sleep(3)

        self.pepto.enable_pepto_log(self.build_version)
        assert self.pepto.verify_pepto_log_file_created() == True

    def test_02_click_learn_more_btn(self):
        """
        Click "Learn More" button on "New Scan Auto-Enhancements" dialog

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27930951
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572537
        """ 
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_learn_more_link()
        self.home.verify_help_and_support_page()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_scanner_screen()

    def test_03_click_auto_enhancements_and_orientation_toggle(self):
        """
        Click "Auto Enhancement option
        Turn on/off the toggle of auto heal 
        Turn off/Turn on toggle for Orientation

        Tips(https://hp-testrail.external.hp.com/index.php?/cases/view/28746990):
        "Auto-Enhancements" toggle turns on automatically when Auto-Heal is toggled on
        "Auto-heal" toggle turns off automatically when "Auto-Enhancement" is toggled off 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27930952
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862855
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862856
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862857
        """ 
        self.scan.select_auto_enhancement_icon() 
        auto_heal=self.scan.verify_auto_enhancement_panel_setting_by_default()
        self.check_auto_heal['auto_heal']=auto_heal
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        
        self.scan.select_auto_enhancement_icon() 
        self.scan.click_auto_enhancements_toggle()
        self.scan.click_auto_orientation_toggle()   
        self.scan.verify_auto_enhancement_is_off()
        self.scan.verify_auto_heal_is_off()
        self.scan.verify_auto_orientation_is_on()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()

        self.scan.select_auto_enhancement_icon() 
        self.scan.click_auto_enhancements_toggle()
        sleep(2) 
        self.scan.click_auto_heal_toggle()
        sleep(2) 
        self.scan.click_auto_orientation_toggle()       
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.home.select_navbar_back_btn(return_home=False)
        self.scan.verify_exit_without_saving_dialog()
        self.scan.click_yes_btn()
        self.scan.verify_scanner_screen()
        self.scan.select_auto_enhancement_icon() 
        self.scan.verify_auto_enhancement_panel_setting_by_default()

    def test_04_preview_edit_settings(self):
        """
        Click "Scan" tile on the Main UI
        Perform scan via any available scan flow
        Land on the scan result page with scanned/Imported/camera file
        click on Edit to edit the page (cropping, adjusting, filters, add text, markup), and save the editing

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309096
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31750639
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28256856 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13159699 
        """ 
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_menu_btn()
        self.scan.click_edit_btn()
        self.scan.verify_edit_screen()

        self.scan.edit_crop_item()
        self.scan.edit_adjust_item()
        self.scan.edit_filters_item()
        self.scan.edit_text_item()
        self.scan.edit_markup_item()
     
        self.scan.click_edit_done_btn()
        self.scan.verify_scan_result_screen()

        sleep(1)
        self.driver.terminate_app()

    def test_05_check_pepto_data(self):
        """
        GO to other extension in the app and come back to Main UI
        Click on the "Edit" button

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27674427
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27930954
        """ 
        check_event_list = ['"app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/ScanCapture.flow/PhotoEditorEditPage"', '"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanResults#Edit"']
        
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_06_check_pepto_data(self):
        """
        Click "Learn More" button on "New Scan Auto-Enhancements" dialog

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27930951
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanStart#LearnMore"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_07_check_pepto_data(self):
        """
        Click "Auto Enhancement option
        Turn on/off the toggle of auto heal 
        Turn off/Turn on toggle for Orientation

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27930952
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862855
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862856
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862857
        """ 
        if self.check_auto_heal['auto_heal']:
            check_event_list = ['"IsOrientationEnabled":"false","IsFileNamingEnabled":"true","IsEnhancementEnabled":"true","IsAutoHealEnabled":"true"', '"IsOrientationEnabled":"true","IsFileNamingEnabled":"true","IsEnhancementEnabled":"false","IsAutoHealEnabled":"false"']
        else:
             check_event_list = ['"IsOrientationEnabled":"false","IsFileNamingEnabled":"true","IsEnhancementEnabled":"true"', '"IsOrientationEnabled":"true","IsFileNamingEnabled":"true","IsEnhancementEnabled":"false"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
        
    def test_08_check_pepto_data(self):
        """
        Check Document_type & "autorotate_used" field 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27930955
        """ 
        check_event_list = ['"document_type":".*","autorotate_used":"false","moniker":"x-cscr_gotham_report_pepperresult_summary/1.0"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_09_check_pepto_data(self):
        """
        Start a scanning job for printer and wait for the scan job completed

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961266
        """ 
        check_event_list = ['"app_event_actor":"self","app_event_action":"initiated","app_event_object":"task","app_event_object_label":"task_scan_acquire"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    
