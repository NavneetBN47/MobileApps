import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES

pytest.app_info = "Smart"

class Test_Suite_01_Verify_Tile_Redirections(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_sessions
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        # Enable HPX Flag
        cls.fc.hpx = True
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.account = cls.fc.fd[FLOW_NAMES.HP_CONNECT_ACCOUNT]

    def test_01_verify_click_scan_tile_redirection_C66253865(self):
        """
        Description: C66253865
        Install and launch app.
        Skip sign in 
        Add printer as device. 
        Tap on Printer card and navigate to Device Details page.
        Tap on scan tile and observe.
        Expected Result:
        - User should be navigated to Sign in screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # Add the printer
        # self.fc.flow_home_select_network_printer(self.p)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_scan_tile(raise_e=False)
        self.account.verify_tiles_not_signed_in_page()

    def test_02_verify_click_print_documents_tile_redirection_C66253866(self):
        """
        Description: C66253866
        Install and launch app.
        Skip sign in  
        Add printer as device. 
        Tap on Printer card and navigate to Device Details page.
        Tap on print documents tile and observe.
        Expected Result:
        - User should be navigated to Sign in screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # Add the printer
        # self.fc.flow_home_select_network_printer(self.p)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_documents_tile(raise_e=False)
        self.account.verify_tiles_not_signed_in_page()

    def test_03_click_camera_scan_tile_redirection_C66253867(self):
        """
        Description: C66253867
        Install and launch app. 
        Skip sign in 
        Add printer as device. 
        Tap on Printer card and navigate to Device Details page.
        Tap on camera scan tile and observe.
        Expected Result:
        - User should be navigated to Sign in screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # Add the printer
        # self.fc.flow_home_select_network_printer(self.p)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.account.verify_tiles_not_signed_in_page()

    def test_04_click_print_photos_tile_redirection_C66253868(self):
        """
        Description: C66253868
        Install and launch app.  
        Skip sign in
        Add printer as device. 
        Tap on Printer card and navigate to Device Details page.
        Tap on print photos tile and observe.
        Expected Result:
        - User should be navigated to Sign in screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # Add the printer
        # self.fc.flow_home_select_network_printer(self.p)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.account.verify_tiles_not_signed_in_page()

    def test_05_click_copy_tile_redirection_C66253869(self):
        """
        Description: C66253869
        Install and launch app.
        skip sign in  
        Add printer as device. 
        Tap on Printer card and navigate to Device Details page.
        Tap on copy tile and observe.
        Expected Result:
        - User should be navigated to Sign in screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # Add the printer
        # self.fc.flow_home_select_network_printer(self.p)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.account.verify_tiles_not_signed_in_page()

    def test_06_click_mobilefax_tile_redirection_C66253870(self):
        """
        C66253870
        Install and launch app.
        Skip sign in
        Add printer as device.
        Tap on Printer card and navigate to Device Details page.
        Tap on mobile fax tile and observe.
        Expected Result:
        - User should be navigated to Sign in screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # Add the printer
        # self.fc.flow_home_select_network_printer(self.p)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_mobilefax_tile(raise_e=False)
        self.account.verify_tiles_not_signed_in_page()

    def test_07_click_shortcuts_tile_redirection_C66253871(self):
        """
        Description: C66253871
        Install and launch app.
        Skip sign in
        Add printer as device.
        Tap on Printer card and navigate to Device Details page.
        Tap on shortcuts tile and observe.
        Expected Result:
        - User should be navigated to Sign in screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # Add the printer
        # self.fc.flow_home_select_network_printer(self.p)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.account.verify_tiles_not_signed_in_page()

    def test_08_click_printable_apps_tile_redirection_C66253864(self):
        """
        Description: C66253864
        Install and launch app.
        Skip sign in
        Add printer as device.
        Tap on Printer card and navigate to Device Details page.
        Tap on printable apps tile and observe.
        Expected Result:
        - User should be navigate to printable screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # Add the printer
        # self.fc.flow_home_select_network_printer(self.p)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_printable_apps_tile(raise_e=False)
        self.account.verify_tiles_not_signed_in_page()