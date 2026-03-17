import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}

class Test_Suite_00_Verify_MFE(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Enabling the HPX flag
        cls.fc.hpx = True
        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_verify_mfe_home(self):
        self.fc.flow_home_toggle_hpx()
        sleep(2)
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_hpx_skip_new_hp_app_popup()
        # When logged into app the MFE will not be loaded so commenting the code
        #assert bool(self.fc.hpx_fd["devicesMFE"].verify_app_bar_mfe()) is True, "Top Bar MFE not loaded"
        
    def test_02_verify_side_panel_mfe(self):
        pass
        """
        self.fc.hpx_fd["devicesMFE"].click_profile_button()
        import pdb 
        pdb.set_trace()
        assert bool(self.fc.hpx_fd["devicesMFE"].verify_side_panel_mfe()) is True, "Side Panel MFE not loaded" 
        # Currently cannot click this button due to UI being weirdly implimented
        #self.fc.hpx_fd["devicesMFE"].click_close_button()
        self.driver.press_key_back()
        """
        
    def test_03_verify_mfe_device_details(self):
        self.fc.flow_home_select_network_printer(self.p, is_loaded=False)
        assert bool(self.fc.hpx_fd["devicesMFE"].verify_device_status_mfe()) is True, "Device Status MFE not loaded"
    
    def test_04_verify_mfe_product_information(self):
        self.fc.hpx_fd["devicesMFE"].click_device_icon()
        assert bool(self.fc.hpx_fd["devices_details_printerMFE"].verify_product_information_mfe()) is True, "Product Information MFE not loaded"
        
    def test_05_verify_product_information_buttons(self):
        assert bool(self.fc.hpx_fd["devices_details_printerMFE"].verify_copy_product_number_btn(timeout=10)) is True, "Copy Model Number Button not loaded"
        assert bool(self.fc.hpx_fd["devices_details_printerMFE"].verify_copy_serial_number_btn()) is True, "Copy Serial Number Button not loaded"
        assert bool(self.fc.hpx_fd["devices_details_printerMFE"].verify_get_info_btn()) is True, "Get Info Button not loaded"   
    