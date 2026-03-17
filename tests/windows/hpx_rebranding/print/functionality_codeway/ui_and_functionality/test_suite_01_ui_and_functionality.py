import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "HPX"

@pytest.mark.usefixtures("function_setup_myhp_launch")
class Test_Suite_01_Ui_And_Functionality(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, windows_test_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devices_details_printer_mfe = cls.fc.fd["devicesDetailsMFE"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.fc.web_password_credential_delete()
        cls.devicesMFE.click_home_loggedin()
        cls.fc.sign_in(cls.user_name, cls.password, cls.web_driver, user_icon_click=False)
        cls.fc.add_a_printer(cls.p)

    @pytest.mark.regression
    def test_01_shortcuts_screen_default_email_shortcut_C50837242(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        self.devices_details_printer_mfe.click_shortcuts_tile()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        expected_email="Start Email "+hpid_credentials["username"]
        actual_email=self.shortcuts.verify_default_email()
        assert expected_email == actual_email, "Default Email shortcut is not present on Shortcuts screen by default"