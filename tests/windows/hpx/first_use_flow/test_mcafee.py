import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
from SAF.misc import windows_utils
import pytest


pytest.app_info = "HPX"
class Test_Suite_McAfee(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)

    def test_01_show_email_error_message_C32239080(self, install_app):
        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()

        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()
        assert self.fc.fd["hp_registration"].verify_skip_button_show() is True
        self.fc.fd["hp_registration"].click_skip_button()
        assert self.fc.fd["dropbox"].verify_dropbox_header_show() is True
        self.fc.fd["dropbox"].click_skip_button()
        assert self.fc.fd["express_vpn"].verify_skip_button_show() is True
        self.fc.fd["express_vpn"].click_skip_button()
        time.sleep(2)
        self.fc.fd["mcafee"].enter_email("<><>></")
        time.sleep(2)
        assert self.fc.fd["mcafee"].get_invalid_data_message() == "A valid email is required."

    def test_02_skipButton_C32266672(self, install_app):

        time.sleep(5)
        self.fc.fd["mcafee"].click_skip_button()
        assert self.fc.fd["navigation_panel"].verify_welcome_module_show() is True

    def test_03_complete_registration_C32152116(self, install_app):
        
        self.fc.re_install_app(install_app)
        time.sleep(5)
        self.fc.launch_app()

        self.fc.click_login_page()

        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()
        assert self.fc.fd["hp_registration"].verify_skip_button_show() is True
        self.fc.fd["hp_registration"].click_skip_button()
        assert self.fc.fd["dropbox"].verify_dropbox_header_show() is True
        self.fc.fd["dropbox"].click_skip_button()
        assert self.fc.fd["express_vpn"].verify_skip_button_show() is True
        self.fc.fd["express_vpn"].click_skip_button()

        time.sleep(2)
        self.fc.fd["mcafee"].complete_register("hptest001@gmail.com")
        assert self.fc.fd["mcafee"].verify_register_success() is True
        
        generate_file = "C:\\ProgramData\\HP\\registration\\registration_subset.xml"
        assert windows_utils.check_path_exist(self.driver.ssh, generate_file) is True
        time.sleep(2)
        self.fc.intial_environment()


    def test_04_nextButtonStatus_C32152103(self,install_app): 
        self.fc.re_install_app_and_skip_login_page(self.driver.session_data["installer_path"])
        if self.fc.fd["hp_privacy_setting"].verify_hp_privacy_subtitle_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()
        assert self.fc.fd["hp_registration"].verify_skip_button_show() is True
        self.fc.fd["hp_registration"].click_skip_button()
        assert self.fc.fd["dropbox"].verify_dropbox_header_show() is True
        self.fc.fd["dropbox"].click_skip_button()
        assert self.fc.fd["express_vpn"].verify_skip_button_show() is True
        self.fc.fd["express_vpn"].click_skip_button()
        self.fc.fd["mcafee"].verify_next_btn_is_disabled()
        self.fc.fd["mcafee"].enter_email("test@gmail.com")
        self.fc.fd["mcafee"].verify_next_btn_is_enabled() 
