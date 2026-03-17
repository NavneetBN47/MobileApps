import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest


pytest.app_info = "HPX"
class Test_Suite_ExpressVPN(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)

    def test_01_show_sigi_in_error_message(self, install_app):
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

        
        time.sleep(2)
        self.fc.fd["express_vpn"].enter_email("<><>></")
        time.sleep(2)
        assert self.fc.fd["express_vpn"].get_invalid_data_message() == "A valid email is required."

    def test_02_skipButton(self):
        time.sleep(5)
        self.fc.fd["express_vpn"].click_skip_button()
        assert self.fc.fd["mcafee"].verify_mcafee_header_show() is True
