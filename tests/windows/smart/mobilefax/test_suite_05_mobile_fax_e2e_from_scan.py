import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.resources.const.ios.const import TEST_DATA


pytest.app_info = "GOTHAM"
class Test_Suite_05_Send_Mobile_Fax_E2E_From_Scan(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.mobile_fax = cls.fc.fd["softfax_home"]
        cls.print = cls.fc.fd["print"]
        cls.scan = cls.fc.fd["scan"]
        cls.softfax_landing = cls.fc.fd["softfax_landing"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_06"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]


    def test_01_send_mobile_fax_for_scan_landing_page(self):
        """
        Navigate to the scan result page via any available scan flow
        Click "Fax" button on the "Scan result" screen  

        Verify flow.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17411208
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17411210 
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.click_scan_btn()
        self.scan.verify_scan_result_screen()
        self.scan.click_fax_btn()
        self.softfax_landing.skip_landing_screen()
        self.mobile_fax.verify_mobile_fax_home_screen()
        self.mobile_fax.select_compose_fax_menu()
        self.mobile_fax.enter_recipient_information(self.recipient_info["phone"])
        self.mobile_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.mobile_fax.click_send_fax()
        self.mobile_fax.verify_job_is_sending()
        self.mobile_fax.verify_job_sent_successfully()
   
    def test_02_delete_mobile_fax_job(self):
        """
        clear the job
        """
        self.mobile_fax.click_delete_this_fax_btn()
        self.mobile_fax.verify_are_you_sure_dialog()
        self.mobile_fax.click_delete_btn()