import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_02_Pepto_Scan_Preview_Save(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
        cls.print = cls.fc.fd["print"]

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

    def test_02_finish_scan_import_flow(self):
        """
        Scan or Import an image or file
        Select Flatten on the detect edges page
        Select to Share or Save
        Toggle Smart File Naming then select ok
        Change the file type, compression and language
        Toggle Smart File Naming
        complete Scan flow and save the image/file
        close the app 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309096
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31733569
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31740229
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31733570
        """ 
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.select_import_btn()
        self.scan.verify_import_dialog()
        self.scan.click_import_dialog_get_started_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)       
        
        # Select Flatten on the detect edges page
        self.scan.verify_import_screen()
        self.scan.click_import_flatten_btn()
        sleep(1)
        self.scan.click_import_apply_btn()

        self.scan.verify_scan_result_screen()
        self.scan.click_save_btn()

        # Change the file type, compression and language(not test)
        self.scan.verify_save_dialog()
        self.scan.select_file_type_dropdown()
        sleep(1)
        self.scan.select_searchable_type()
        sleep(1)
        self.scan.click_install_new_language_btn()
        self.scan.verify_install_language_dialog()
        self.scan.click_back_arrow()
    
        # Toggle Smart File Naming then select ok
        self.scan.click_smart_file_name_toggle("open")
        if self.scan.verify_save_text_not_detected_dialog():
            self.scan.click_save_ok_btn()
        sleep(1)
        self.scan.click_save_dialog_save_btn()
        sleep(3)

        # Toggle Smart File Naming
        self.scan.input_file_name('test.pdf')
        self.scan.verify_file_has_been_saved_dialog()
        file_path = self.scan.get_the_saved_file_path()
                             
        self.scan.click_dialog_close_btn()
        self.driver.ssh.send_command("del " + file_path)
        sleep(1)

        self.home.select_navbar_back_btn(return_home=False)
        sleep(5)
        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_home_screen()

        sleep(1)
        self.driver.terminate_app()

    def test_03_check_pepto_data(self):
        """
        Click Scan tile

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29309096
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961226
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#ScanCapture"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_04_check_pepto_data(self):
        """
        Click "Get Started" button on "New Scan Auto-Enhancements" dialog

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31733569
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27930950
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#ScanCapture"', '"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanStart#GetStarted"', '"app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/ScanCapture.flow/DocExtract"', '"app_event_actor":"user","app_event_action":"checked","app_event_object":"checkbox","app_event_object_label":"/ScanCapture.flow/ScanSetting#IsImportFlow"', '"app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/ScanCapture.flow/ScanResultsMain"', '"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanResults#Save"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
    
    def test_05_check_pepto_data(self):
        """
        Check the "Pdsmq.Data.txt" file.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31740229
        """ 
        check_event_list = ['"app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/cscr.flow/gotham/ScanResults"', '"app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/cscr.flow/ScanResults/textnotdetected-False"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_06_check_pepto_data(self):
        """
        Click on the "File Type:" control and choose the Basic PDF/Image( .jpg)/Searchable PDF/ Word Document( *.docx)/ Plain Text(.txt) .

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/31733570
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28864999
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"checked","app_event_object":"checkbox","app_event_object_label":"/ScanCapture.flow/FileType#Imagejpg"', '"app_event_actor":"user","app_event_action":"checked","app_event_object":"checkbox","app_event_object_label":"/ScanCapture.flow/FileType#SearchablePDF"', '"app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/ScanCapture.flow/ScanResults-True#OninstallNewLangugeLinkClicked"', '"app_event_details":{"is_pin_protect_enabled":"false","is_smart_filename_enabled":"false","file_type":"Searchable PDF","file_compression":"None","selected_document_language":"en","moniker":"x-cscr_gotham_report_scandocumentsave_report/1.0","schema":"app_event_report_generic/1.0.0"}'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
    
    def test_07_check_pepto_data(self):
        """
        Check Document_type & "autorotate_used" field 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27930955
        """ 
        check_event_list = ['"document_type":"PHOTO","autorotate_used":"false","moniker":"x-cscr_gotham_report_pepperresult_summary/1.0"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_08_check_pepto_data(self):
        """
        Click Scan tile -> Import tab and import a image.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961267
        """ 
        check_event_list = ['"app_event_actor":"self","app_event_action":"initiated","app_event_object":"task","app_event_object_label":"task_image_acquire"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
