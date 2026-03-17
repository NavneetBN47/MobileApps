import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES


pytest.app_info = "Smart"

class Test_Suite_01_Verify_Tile_Redirections(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        cls.hpx_local_photos = cls.fc.flow[FLOW_NAMES.HPX_LOCAL_PHOTOS]
        cls.softfax_welcome = cls.fc.fd[FLOW_NAMES.SOFTFAX_WELCOME]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.printables = cls.fc.fd[FLOW_NAMES.PRINTABLES]   
        # Enable HPX Flag
        cls.fc.hpx = True


    def test_01_scan_tile_redirection_C66290668(self):
        """
        Description: C66290668
            Install and launch app.
            Sign in and add a printer.
            Tap on Printer card and navigate to Device Details page.
            Tap on Scan tile.
        Expected Result:
            Verify Scan tile is shown as per design.
            Verify the user is directed to Scan flow. (existing functionality).        
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_scan_tile(raise_e=False)
        self.scan.dismiss_coachmark()
        assert self.camera_scan.verify_scan_btn()

    def test_02_print_documents_tile_redirection_C66290670(self):
        """
        Description: C66290670
            Install and launch app.
            Sign in and add a printer.
            Tap on Printer card and navigate to Device Details page.
            Tap on Print Documents tile.
        Expected Result:
            Verify Print Documents tile is shown as per design.
            Verify the user is directed to Print Documents flow.(existing functionality).        
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_documents_tile(raise_e=False)
        assert self.camera_scan.verify_photos_pdfs_btn()

    def test_03_camera_scan_tile_redirection_C66290671(self):
        """
        Description: C66290671
            Install and launch app.
            Sign in and add a printer.
            Tap on Printer card and navigate to Device Details page.
            Tap on Camera Scan tile.
        Expected Result:
            Verify Camera Scan tile is shown as per design.
            Verify the user is directed to Camera Scan flow.(existing functionality).      
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.scan.dismiss_coachmark()
        self.camera_scan.verify_no_camera_access_title()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        assert self.camera_scan.get_capture_mode_text() == "Auto", f"Expected 'Auto' but got {self.camera_scan.get_capture_mode_text()}"

    def test_04_print_photos_tile_redirection_C66290672(self):
        """
        Description: C66290672
            Install and launch app.
            Sign in and add a printer.
            Tap on Printer card and navigate to Device Details page.
            Tap on Print Photos tile.
        Expected Result:
            Verify Print Photos tile is shown as per design.
            Verify the user is directed to Print Photos flow.(existing functionality).     
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        assert self.hpx_local_photos.verify_album_name()

    def test_05_copy_tile_redirection_C66290673(self):
        """
        Description: C66290673
           Install and launch app.
           Sign in and add a printer.
           Tap on Printer and navigate to Device Details page.
           Tap on Copy tile.
        Expected Result:
            Verify Copy tile is shown as per design.
            Verify the user is directed to Copy flow.(existing functionality).     
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_copy_tile(raise_e=False)
        self.camera_scan.verify_no_camera_access_title()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.click_shutter()
        assert self.print_preview.verify_print_preview_screen()

    def test_06_mobile_fax_tile_redirection_C66290674(self):
        """
        Description: C66290674
           Install and launch app.
           Sign in and add a printer.
           Tap on Printer and navigate to Device Details page.
           Tap on Mobile Fax tile.
        Expected Result:
            Verify Mobile Fax tile is shown as per design.
            Verify the user is directed to Mobile Fax flow.(existing functionality).
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_mobilefax_tile(raise_e=False)
        assert self.softfax_welcome.verify_welcome_screen()

    def test_07_shortcuts_tile_redirection_C66290675(self):
        """
        Description: C66290675
           Install and launch app.
           Sign in and add a printer.
           Tap on Printer and navigate to Device Details page.
           Tap on Shortcuts tile.
        Expected Result:
            Verify Shortcuts tile is shown as per design.
            Verify the user is directed to Shortcuts flow.(existing functionality).    
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.shortcuts.verify_shortcuts_screen()

    def test_08_printables_tile_redirection_C66290677(self):
        """
        Description: C66290677
           Install and launch app.
           Sign in and add a printer.
           Tap on Printer and navigate to Device Details page.
           Tap on Printables tile.
        Expected Result:
            Verify Printables tile is shown as per design.
            Verify the user is directed to Printables flow.(existing functionality).     
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_printable_apps_tile(raise_e=False)
        self.printables.verify_printables_title()