import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.common.gotham.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "GOTHAM"
class Test_Suite_03_Mobile_Fax_E2E_Invalid_Information(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
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
        cls.recipient_error_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_11"]
        

    def test_01_send_mobile_fax_with_invalid_information(self):
        """
        Click "Mobile Fax" tile on the Main UI
        put invalid phone # in the To/ From field 
   
        Verify correct error message shows
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17261135 
     
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_mobile_fax_tile()
        self.softfax_landing.skip_landing_screen()
        self.mobile_fax.verify_mobile_fax_home_screen()
        self.mobile_fax.select_compose_fax_menu()
        self.mobile_fax.click_send_fax(raise_e=False)
        #put empty recipient phone
        self.mobile_fax.verify_phone_validation_message(self.mobile_fax.EMPTY_PHONE_MSG)
        #put invalid recipient phone
        self.mobile_fax.enter_recipient_information("123")
        self.mobile_fax.click_send_fax(raise_e=False)
        self.mobile_fax.verify_phone_validation_message(self.mobile_fax.INVALID_FORMAT_MSG)
        self.mobile_fax.enter_recipient_information(self.recipient_info["phone"])
        #put empty send phone
        self.mobile_fax.enter_sender_information(self.sender_info["name"], "")
        self.mobile_fax.click_send_fax(raise_e=False)
        self.mobile_fax.verify_phone_validation_message(self.mobile_fax.EMPTY_PHONE_MSG, is_sender=True)
        #put invalid send phone
        self.mobile_fax.enter_sender_information(self.sender_info["name"], "123")
        self.mobile_fax.click_send_fax(raise_e=False)
        self.mobile_fax.verify_phone_validation_message(self.mobile_fax.INVALID_FORMAT_MSG, is_sender=True)

    def test_02_send_mobile_fax_with_unreachable_number(self):
        """
        Send a Fax to the unreachable number 

        Verify proper Error message shows
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17261136
        """
        self.mobile_fax.enter_recipient_information(self.recipient_error_info["phone"])
        self.mobile_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.mobile_fax.click_add_files_option_btn(self.mobile_fax.FILES_PHOTOS_BTN)
        self.print.input_file_name(w_const.TEST_DATA.FISH_PNG)
        self.mobile_fax.verify_add_files_successfully()
        self.mobile_fax.click_send_fax()
        self.mobile_fax.verify_job_is_sending()
        self.mobile_fax.verify_job_sent_successfully(sent_result=False)