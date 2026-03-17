import pytest
from time import sleep
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_1_Dark_Mode_Scan(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_verify_scanner_screen_in_dark_mode_c53237452(self):
        """
        Verify the UI of Scan intro screen in Dark mode

        https://hp-testrail.external.hp.com/index.php?/cases/view/53237452
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.enable_dark_mode()
        dm_scanner = self.fc.fd["hpx_rebranding_common"].compare_image_diff("myhp_window", folder_n="scan", image_n="dm_scanner.png")
        logging.info(f"Dark mode scanner screen comparison result: {dm_scanner}")
        assert dm_scanner < 0.04
        
    @pytest.mark.regression
    def test_02_check_detect_edges_on_in_dark_mode_c53231499(self):
        """
        Verify the UI of the Scan Intro Page When Detect Edges is ON

        https://hp-testrail.external.hp.com/index.php?/cases/view/53231499
        """
        dm_de_uncheck = self.fc.fd["hpx_rebranding_common"].compare_image_diff("detect_edges_checkbox", folder_n="scan", image_n="dm_de_uncheck.png")
        assert dm_de_uncheck < 0.02
        self.fc.fd["scan"].click_detect_edges_checkbox()
        assert self.fc.fd["scan"].verify_detect_edges_checkbox_status() == "1"
        dm_de_check = self.fc.fd["hpx_rebranding_common"].compare_image_diff("detect_edges_checkbox", folder_n="scan", image_n="dm_de_check.png")
        assert dm_de_check < 0.02

    @pytest.mark.regression
    def test_03_verify_scanning_screen_in_dark_mode_c53231316_c53237904(self):
        """
        Verify the loading screen in "Detect Edges" Screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/53231316

        Verify the Scanning spinner color in dark mode

        https://hp-testrail.external.hp.com/index.php?/cases/view/53237904
        """  
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_1200)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen(invisible=False)
        dm_scanning = self.fc.fd["hpx_rebranding_common"].compare_image_diff("myhp_window", folder_n="scan", image_n="dm_scanning.png")
        assert dm_scanning < 0.04

    @pytest.mark.regression
    def test_04_verify_auto_full_in_dark_mode_c53231306(self):
        """
        Verify the "Detect Edges" Option (Auto/Full)

        https://hp-testrail.external.hp.com/index.php?/cases/view/53231306
        """
        self.fc.fd["scan"].verify_scanning_screen(timeout=180)
        self.fc.fd["scan"].verify_import_screen()
        dm_select_auto = self.fc.fd["hpx_rebranding_common"].compare_image_diff("import_screen_auto_group", folder_n="scan", image_n="dm_select_auto.png")
        dm_not_select_full = self.fc.fd["hpx_rebranding_common"].compare_image_diff("import_screen_full_group", folder_n="scan", image_n="dm_not_select_full.png")
        assert dm_select_auto < 0.2
        assert dm_not_select_full < 0.2

    @pytest.mark.regression
    def test_05_verify_save_dialog_in_dark_mode_c53722309(self):
        """
        Verify the Dark mode UI of the Save Pop-up window in the Scan Result MFE screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/53722309
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.enable_dark_mode()
        if self.fc.fd["scan"].verify_detect_edges_checkbox_status() == "0":
            self.fc.fd["scan"].click_detect_edges_checkbox()
        self.fc.fd["scan"].click_scan_btn()

        self.fc.fd["scan"].verify_scanning_screen(timeout=180)
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_add_pages_btn()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_detect_edges_checkbox()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_multi_image(num=2)

        # Click on the Save button in the Gallery view.
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        dm_save_dialog = self.fc.fd["hpx_rebranding_common"].compare_image_diff("popup_dialog", folder_n="scan", image_n="dm_save_dialog.png")
        logging.info(f"Dark mode save dialog comparison result: {dm_save_dialog}")
        assert dm_save_dialog < 0.1
        self.fc.fd["scan"].click_dialog_cancel_btn()

        # Click on the Save button in the Thumbnail view.
        self.fc.fd["scan"].click_thumbnail_view_icon() 
        self.fc.fd["scan"].verify_thumbnail_view_screen(num=2)
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        dm_save_dialog = self.fc.fd["hpx_rebranding_common"].compare_image_diff("popup_dialog", folder_n="scan", image_n="dm_save_dialog.png")
        assert dm_save_dialog < 0.1

    @pytest.mark.regression
    def test_06_verify_share_dialog_in_dark_mode_c53722362(self):
        """
        Verify the Dark mode UI of the Share Pop-up window in the Scan Result MFE screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/53722362
        """
        self.fc.fd["scan"].click_dialog_cancel_btn()

        # Click on the Share button in the Thumbnail view.
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()
        dm_share_dialog = self.fc.fd["hpx_rebranding_common"].compare_image_diff("popup_dialog", folder_n="scan", image_n="dm_share_dialog.png")
        logging.info(f"Dark mode share dialog comparison result: {dm_share_dialog}")
        assert dm_share_dialog < 0.1
        self.fc.fd["scan"].click_dialog_cancel_btn()

        # Click on the Share button in the Gallery view.
        self.fc.fd["scan"].click_gallery_view_icon()
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()
        dm_share_dialog = self.fc.fd["hpx_rebranding_common"].compare_image_diff("popup_dialog", folder_n="scan", image_n="dm_share_dialog.png")
        assert dm_share_dialog < 0.1

    @pytest.mark.regression
    def test_07_verify_delete_dialog_in_dark_mode_c53722639(self):
        """
        Verify the Dark mode UI of the Delete Pop-up window in the Scan Result MFE screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/53722639
        """
        self.fc.fd["scan"].click_dialog_cancel_btn()

        # Click on the Delete button in the Gallery view.
        self.fc.fd["scan"].click_image_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()
        dm_del_dialog = self.fc.fd["hpx_rebranding_common"].compare_image_diff("popup_dialog", folder_n="scan", image_n="dm_del_dialog.png")
        assert dm_del_dialog < 0.1
        self.fc.fd["scan"].click_dialog_cancel_btn()

        # Click on the Delete button in the Thumbnail view.
        self.fc.fd["scan"].click_thumbnail_view_icon()
        self.fc.fd["scan"].select_thumbnail_item(num=1)
        self.fc.fd["scan"].click_thumbnail_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()
        dm_del_dialog = self.fc.fd["hpx_rebranding_common"].compare_image_diff("popup_dialog", folder_n="scan", image_n="dm_del_dialog.png")
        assert dm_del_dialog < 0.1

    @pytest.mark.regression
    def test_08_verify_edit_dialog_in_dark_mode_c55054944(self):
        """
        Verify the Dark mode UI of the Scan Edit MFE screen from Gallery view

        https://hp-testrail.external.hp.com/index.php?/cases/view/55054944
        """
        self.fc.fd["scan"].click_dialog_cancel_btn()

        # Click the Edit button in the Gallery view.
        self.fc.fd["scan"].click_gallery_view_icon()
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        dm_edit_dialog = self.fc.fd["hpx_rebranding_common"].compare_image_diff("tool_navigation_menu", folder_n="scan", image_n="dm_edit_dialog.png")
        assert dm_edit_dialog < 0.02

    @pytest.mark.regression
    def test_09_verify_edit_dialog_in_dark_mode_c55053162(self):
        """
        Verify the Dark mode UI of the Scan Edit MFE screen from Thumbnail view

        https://hp-testrail.external.hp.com/index.php?/cases/view/55053162
        """
        self.fc.fd["scan"].click_edit_cancel_btn()
        self.fc.fd["scan"].verify_thumbnail_icon()
        # Click the Edit button in the Thumbnail view.
        self.fc.fd["scan"].click_thumbnail_view_icon()
        self.fc.fd["scan"].select_thumbnail_item(num=1)
        self.fc.fd["scan"].click_thumbnail_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        dm_edit_dialog = self.fc.fd["hpx_rebranding_common"].compare_image_diff("tool_navigation_menu", folder_n="scan", image_n="dm_edit_dialog.png")
        assert dm_edit_dialog < 0.025

    @pytest.mark.regression
    def test_10_verify_new_scan_dialog_in_dark_mode_c53723289(self):
        """
        Verify the Dark mode UI of the New Scan Pop-up window in the Scan Result MFE screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/53723289
        """
        self.fc.fd["scan"].click_edit_cancel_btn()
        # Wait for the screen to transition back to scan result screen
        sleep(2)

        # Click on the New Scan button in the Thumbnail view.
        self.fc.fd["scan"].click_new_scan_btn()
        self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog()
        dm_new_scan_dialog = self.fc.fd["hpx_rebranding_common"].compare_image_diff("popup_dialog", folder_n="scan", image_n="dm_new_scan_dialog.png")
        assert dm_new_scan_dialog < 0.02
        self.fc.fd["scan"].click_cancel_btn()

        # Click on the New Scan button in the Gallery view.
        self.fc.fd["scan"].click_gallery_view_icon()
        self.fc.fd["scan"].click_new_scan_btn()
        self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog()

        # Message: An element command failed because the referenced element is no longer attached to the DOM
        # dm_new_scan_dialog = self.fc.fd["hpx_rebranding_common"].compare_image_diff("popup_dialog", folder_n="scan", image_n="dm_new_scan_dialog.png")
        # assert dm_new_scan_dialog < 0.025
        self.fc.fd["scan"].click_cancel_btn()

    @pytest.mark.regression
    def test_11_disable_dark_mode(self):
        """
        Verify UI Switches from Dark Mode to Light Mode
        """
        self.fc.disable_dark_mode()
