import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.resources.const.ios.const import TEST_DATA
from selenium.common.exceptions import NoSuchElementException

pytest.app_info = "GOTHAM"
class Test_Suite_01_Send_Mobile_Fax_E2E(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc= windows_smart_setup
        cls.p = load_printers_session
        
        cls.home = cls.fc.fd["home"]
        cls.mobile_fax = cls.fc.fd["softfax_home"]
        cls.print = cls.fc.fd["print"]
        cls.softfax_landing = cls.fc.fd["softfax_landing"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_06"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    def test_01_send_mobile_fax(self):
        """
        Click Mobile Fax tile on main UI
        Follow the attached flow
        Verify flow
        Verify Mobile Fax sent successfully.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17854783  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17135179
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17264505
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17411210
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/16861532
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_mobile_fax_tile()
        # self.softfax_landing.skip_landing_screen()
        self.mobile_fax.verify_mobile_fax_home_screen()
        self.mobile_fax.select_compose_fax_menu()
        self.mobile_fax.enter_recipient_information(self.recipient_info["phone"])
        self.mobile_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.mobile_fax.click_add_files_option_btn(self.mobile_fax.FILES_PHOTOS_BTN)
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.mobile_fax.verify_add_files_successfully()
        self.mobile_fax.click_send_fax()
        self.mobile_fax.verify_job_is_sending()
        self.mobile_fax.verify_job_sent_successfully()

    def test_02_check_gotham_log(self):
        """
        Check Gotham log 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24275138 
        GOTH-24317 
        """
        event_msg_1 = "/sws/api/v1/session"
        event_msg_2 = "/sws/api/v1/upload"
        event_msg_3 = "upload_id"
        f = self.driver.ssh.remote_open(w_const.TEST_DATA.HP_SMART_LOG_PATH)
        data = f.read().decode("utf-8")
        f.close()
        if str(event_msg_1) and str(event_msg_2) and str(event_msg_3) in data:
            return True
        raise NoSuchElementException(
            "Fail to found {} or {} or {}".format(event_msg_1, event_msg_2, event_msg_3))
   
    def test_03_delete_mobile_fax_job(self):
        """
        clear the job
        """
        self.mobile_fax.click_delete_this_fax_btn()
        self.mobile_fax.verify_are_you_sure_dialog()
        self.mobile_fax.click_delete_btn()