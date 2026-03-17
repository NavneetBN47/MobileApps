import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.resources.const.ios.const import TEST_DATA
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_12_Pepto_Shortcuts_Multiple_Option(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.build_version = (cls.driver.session_data["app_info"])[pytest.app_info].split('-')[1]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

    def test_01_go_home_and_enable_pepto(self):
        """
        Enable the Pepto log.
        Launch the app to Main UI
        """  
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        sleep(3)

        self.pepto.enable_pepto_log(self.build_version)
        assert self.pepto.verify_pepto_log_file_created() == True
        
    def test_02_create_a_print_shortcut(self):
        """
        Click "Smart Tasks" tile on the Main UI -> verify "Create smart tasks" screen shows
        Click the "Print" option and create smart tasks with just Print -> Verify smart tasks created successfully
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14101116   
        """
        self.home.select_shortcuts_tile()
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_add_shortcut()
        self.shortcuts.verify_add_shortcuts_screen()
        self.shortcuts.click_create_your_own_shortcut_btn()
        self.shortcuts.verify_save_shortcut_screen()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_01)
        self.shortcuts.click_print_btn()
        self.shortcuts.select_copies(copies_num=self.shortcuts.SINGLE_COPIES_BTN)

    def test_03_create_a_email_shortcut(self):
        """
        Click "Smart Tasks" tile on the Main UI -> verify "Create smart tasks" screen shows
        Click the "Email" option and create smart tasks with just Email with OCR turned on - verify smart tasks created successfully 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14101116
        """ 
        sleep(2)
        email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        self.shortcuts.click_email_btn()
        self.shortcuts.enter_email_receiver(email_address)

    def test_04_create_a_save_to_shortcut(self):
        """
        Click "Smart Tasks" tile on the Main UI -> verify "Create smart tasks" screen shows
        Click the "Save To" option and create smart tasks with any Save to destination -> Verify smart tasks created successfully

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14101116
        """ 
        sleep(2)
        self.shortcuts.click_save_btn()
        self.shortcuts.click_first_checkbox_for_saving()
        self.shortcuts.click_save_shortcut_btn()
        if self.shortcuts.verify_file_already_exists_dialog():
            self.shortcuts.click_already_exists_no_btn()
        self.shortcuts.verify_shortcut_saved_screen()

    def test_05_edit_the_shortcut(self):
        """
        Edit the Shortcut.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17128884
        """ 
        sleep(2)
        self.shortcuts.click_my_shortcuts_btn()
        self.shortcuts.click_shortcut_option_btn()
        self.shortcuts.click_edit_btn()
        self.shortcuts.enter_shortcut_name(w_const.TEST_TEXT.TEST_TEXT_02)
        self.shortcuts.click_save_shortcut_btn()

        sleep(1)
        self.driver.terminate_app()

    def test_06_check_pepto_data(self):
        """
        Verify correct properties entry shows as you have selected during the creation of the smart task.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14101116
        """ 
        check_event_list = ['"print_selected":"true"', '"email_selected":"true"', '"saveto_selected":"true"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_07_check_pepto_data(self):
        """
        Edit the Shortcut

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17128884
        """ 
        check_event_list = ['"app_event_object_label":"/SmartTasks.flow/SmartTasks#SmartTaskEditBtn"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_08_check_pepto_data(self):
        """
        Click Shortcuts tile on Main UI for the first time

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17128887
        """ 
        check_event_list = ['"app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#SmartTasks"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_09_shortcuts_cleanup(self):
        self.fc.del_shortcuts(w_const.TEST_TEXT.TEST_TEXT_01)
        self.fc.del_shortcuts(w_const.TEST_TEXT.TEST_TEXT_02)
   