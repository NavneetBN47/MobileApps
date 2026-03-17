import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "HPX"

@pytest.mark.usefixtures("function_setup_myhp_launch")
class Test_Suite_03_HP_Cloud_Scan(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, windows_test_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devices_details_printer_mfe = cls.fc.fd["devicesDetailsMFE"]
        cls.hp_cloud_scan = cls.fc.fd["hp_cloud_scan"]
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
    def test_01_verify_hP_cloud_Scan_printer_not_added_screen_C63725008(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devices_details_printer_mfe.verify_hp_cloud_scans_tile(), "Hp Cloud Scans tile not available"
        self.devices_details_printer_mfe.click_hp_cloud_scans_tile()
        assert self.hp_cloud_scan.verify_hp_cloud_scan_printer_not_added_screen(), "Hp Cloud Scan Printer Not Added Screen is not displayed"