import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "HPX"

class Test_Suite_01_Privacy_Settings(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session  
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.fc = FlowContainer(request.cls.driver)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devicesDetailsMFE = cls.fc.fd["devicesDetailsMFE"]
        request.cls.fc.web_password_credential_delete()
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]

        # Load credentials
        liveprinter_claimed_itg_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["liveprinter_claimed_itg_credentials"]
        cls.user_name, cls.password = liveprinter_claimed_itg_credentials["username"], liveprinter_claimed_itg_credentials["password"]
        
    @pytest.mark.regression
    def test_01_verify_privacy_option_in_printer_settings_C59179005(self):
        self.fc.launch_hpx_to_home_page()
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        self.fc.add_a_printer(self.p)
        self.printer_name = self.p.get_printer_information()["model name"]
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devicesDetailsMFE.verify_printer_settings_part(), "Printer settings title not found"
        assert self.devicesDetailsMFE.verify_privacy_item(), "Privacy option is not visible"