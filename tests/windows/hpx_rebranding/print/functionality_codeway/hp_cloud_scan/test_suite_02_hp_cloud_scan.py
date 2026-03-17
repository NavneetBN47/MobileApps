import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "HPX"
 
class Test_Suite_02_HP_Cloud_Scan(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, windows_test_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devices_details_printer_mfe = cls.fc.fd["devicesDetailsMFE"]
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
       
 
    @pytest.mark.regression
    def test_01_Verify_hp_cloud_scans_tile_with_claimed_account_C63834834(self):
        self.fc.launch_hpx_to_home_page()
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        self.fc.add_a_printer(self.p)
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devices_details_printer_mfe.verify_hp_cloud_scans_tile(), "HP Cloud Scan tile is not displayed in Device Details page"
 