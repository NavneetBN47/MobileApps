import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_01_Layout:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        # Define flows
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_verify_behavior_of_tooltip_for_i_icon(self):
        """
        Description: C44019093
        Steps:
            1.Launch the app.
            2.Sign in and navigate to rootview and add a printer.
            3.Tap on the printer card and navigate to Device Detail page.
            4.Tap on "Print Photo" tile
            5.Select an image and navigate to DS screen.
            6.Tap on Layout option and Observe the Tooltip on top left of screen.
            7.Tap on i icon on top left of screen.
            8.Tap anywhere else on screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_layout_mode_btn()
        self.print_preview.verify_tooltip_shows_and_disappears()
        self.print_preview.click_print_photos_tool_tip_btn()
        self.print_preview.verify_print_photos_tool_tip_msg()
        self.driver.wdvr.execute_script("mobile: clickGesture", {"x": 165, "y": 1100})
        assert not self.print_preview.verify_print_photos_tool_tip_msg(raise_e=False)

    def test_02_verify_behavior_of_fit_option_on_bottom_navigation_bar(self):
        """
        Description: C44019096
        Steps:
            Launch the app.
            Sign in and navigate to rootview and add a printer.
            Tap on the printer card and navigate to Device Detail page.
            Tap on "Print Photo" tile
            Select an image
            Tap on layout button on bottom toolbar.
            Tap on Fit button on bottom navigation bar.
        Expected Result:
            The Fit button will stay highlighted.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_layout_mode_btn()
        self.print_preview.click_print_preview_fit_btn()
        assert self.print_preview.check_fit_btn_is_selected()

    def test_03_verify_behavior_of_fill_option_on_bottom_navigation_bar(self):
        """
        Description: C44019097
        Steps:
            Launch the app.
            Sign in and navigate to rootview and add a printer.
            Tap on the printer card and navigate to Device Detail page.
            Tap on "Print Photo" tile
            Select an image
            Tap on layout button on bottom toolbar.
            Tap on Fill button on bottom navigation bar.
        Expected Result:
            The Fill button will stay highlighted.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_layout_mode_btn()
        self.print_preview.click_print_preview_fill_btn()
        assert self.print_preview.check_fill_btn_is_selected()

    def test_04_verify_behavior_of_rotate_button_from_bottom_bar(self):
        """
        Description: C44019098
        Steps:
            Launch the app.
            Sign in and navigate to rootview and add a printer.
            Tap on the printer card and navigate to Device Detail page.
            Tap on "Print Photo" tile
            Select an image
            Tap on layout button on bottom toolbar.
            Tap on Fill button on bottom navigation bar.
            Tap on Rotate button from bottom navigation bar.
        Expected Result:
            The "Rotate" button shows as selected
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_layout_mode_btn()
        self.print_preview.click_print_preview_fill_btn()
        self.print_preview.click_print_preview_rotate_btn()
        assert self.print_preview.check_fill_btn_is_selected()

    def test_05_verify_behavior_of_flip_h_option_on_bottom_navigation_bar(self):
        """
        Description: C44019109
        Steps:
            Launch the app.
        Sign in and navigate to rootview and add a printer.
        Tap on the printer card and navigate to Device Detail page.
        Tap on "Print Photo" tile
        Select an image
        Tap on layout button on bottom toolbar.
        Tap on Flip H button on bottom navigation bar.
        Expected Result:
            The "Flip H" button shows as selected
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_layout_mode_btn()
        self.print_preview.click_print_preview_flip_h_btn()