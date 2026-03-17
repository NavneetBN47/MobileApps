import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "HPX"
 
class Test_Suite_01_HP_Cloud_Scan(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, windows_test_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.profile = cls.fc.fd["profile"]
        cls.hpx_settings = cls.fc.fd["hpx_settings"]
        cls.devices_details_printer_mfe = cls.fc.fd["devicesDetailsMFE"]
        cls.hp_cloud_scan = cls.fc.fd["hp_cloud_scan"]
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.fc.web_password_credential_delete()
 
    @pytest.mark.regression
    def test_01_Verify_hp_cloud_scans_tile_with_normal_account_C63836424(self):
        self.fc.launch_hpx_to_home_page()
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        self.fc.add_a_printer(self.p)
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devices_details_printer_mfe.verify_hp_cloud_scans_tile(), "HP Cloud Scan tile is not displayed in Device Details page"
        self.driver.swipe(direction="up", distance=10)
        self.profile.click_top_profile_icon_signed_in()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.click_sign_out_btn()
        self.fc.close_myHP()


    @pytest.mark.regression
    def test_02_verify_hp_cloud_scans_tile_when_the_user_is_not_signed_in_C63834818(self):
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devices_details_printer_mfe.verify_hp_cloud_scans_tile(), "Hp Cloud Scans tile not available"
        self.fc.close_myHP()

    @pytest.mark.regression
    def test_03_verify_hp_cloud_scan_sign_in_screen_C63724820(self):
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devices_details_printer_mfe.verify_hp_cloud_scans_tile(), "Hp Cloud Scans tile not available"
        self.devices_details_printer_mfe.click_hp_cloud_scans_tile()
        assert self.hp_cloud_scan.verify_hp_cloud_scan_sign_in_screen(), "Hp cloud Scan Sign in Screen is not displayed"
        self.fc.close_myHP()
        

    

    
 
 