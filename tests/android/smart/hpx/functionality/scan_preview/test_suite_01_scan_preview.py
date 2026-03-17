import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "Smart"

class Test_suite_01_Native_Print_Scan:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_verify_the_three_dots_in_preview_page(self):
        """
        Description: C51953892
        Steps:
            1.Tap on the "Camera Scan" tile.
            2.Capture a file.
            3.Tap "Next" on the Adjust Boundaries screen.
            4.Navigate to the Preview page.
            5.Click on 3 dots
            6.Observe the behavior.
        Expected Result:
            User able to see options as Edit, Replace and Delete
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.verify_page_option_edit_btn()
        self.print_preview.verify_page_option_replace_btn()
        self.print_preview.verify_page_option_delete_btn()

    def test_02_verify_the_behavior_of_the_information_button_on_the_shortcuts_preview_page(self):
        """
        Description: C51953891
        Steps:
            1.Sign In to your account.
            2.NavIgate to the Home page.
            3.Tap on the "Camera Scan" tile and capture a file.
            4.Tap "Next" on the Adjust Boundaries screen.
            5.Tap on "Shortcuts."
            6.Swipe up to view the shortcuts list.
            7.Tap on the "i" button on any shortcut.
            8.Observe the behavior.
        Expected Result:
            The user is able to see the details or Information about the selected shortcut.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_shortcut_btn()
        self.print_preview.verify_shortcut_name_txt_btn()
        self.driver.swipe(swipe_object="shortcut_info_btn")
        self.print_preview.verify_shortcut_name_txt_btn()
        self.print_preview.click_shortcut_info_btn()
        self.print_preview.verify_shortcut_info_title()

    def test_03_verify_the_close_option_for_image_in_preview_page(self):
        """
        Description: C51953893
            1.Tap on the "Camera Scan" tile.
            2.Capture a file.
            3.Tap "Next" on the Adjust Boundaries screen.
            4.Navigate to the Preview page.
            5.Click on 3 dots and tap on "X".
            6.Observe the behavior.
        Expected Result:
            User able to see 3 dots in the preview screen and able to close the image by clicking on "X" button.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.driver.back()

    def test_04_verify_the_edit_functionality_in_the_preview_page_for_capture_image(self):
        """
        Description: C51953894
            1.Tap on the "Camera Scan" tile.
            2.Capture a file.
            3.Tap "Next" on the Adjust Boundaries screen.
            4.Navigate to the Preview page.
            5.Click on 3 dots and tap on edit button
            6.Observe the behavior.
        Expected Result:
            Verify user able to navigate to the Edit screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.verify_edit_screen_title()

    def test_05_verify_the_crop_functionality_in_the_edit_screen(self):
        """
        Description: C51953895
            1.Tap on the "Camera Scan" tile.
            2.Capture a file.
            3.Tap "Next" on the Adjust Boundaries screen.
            4.Navigate to the Preview page.
            5.Click on 3 dots and tap on edit button
            6.Select crop button Observe the behavior.
        Expected Result:
            Verify user able to navigate to the Crop screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.verify_edit_screen_title()
        self.print_preview.click_edit_screen_crop_btn()
        self.print_preview.verify_edit_screen_title()
        assert self.print_preview.get_edit_screen_title() == "Crop", "Expected edit screen title is 'Crop' but got {}".format(self.print_preview.get_edit_screen_title())
        self.print_preview.click_edit_screen_done_btn()

    def test_06_verify_the_adjust_functionality_in_the_edit_screen(self):
        """
        Description: C51953896
            1.Tap on the "Camera Scan" tile.
            2.Capture a file.
            3.Tap "Next" on the Adjust Boundaries screen.
            4.Navigate to the Preview page.
            5.Click on 3 dots and tap on edit button
            6.Select Adjust button Observe the behavior.
        Expected Result:
            Verify user able to navigate to the Adjust screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.verify_edit_screen_title()
        self.print_preview.click_edit_screen_adjust_btn()
        self.print_preview.verify_edit_screen_title()
        assert self.print_preview.get_edit_screen_title() == "Adjust", "Expected edit screen title is 'Adjust' but got {}".format(self.print_preview.get_edit_screen_title())
        self.print_preview.click_edit_screen_done_btn()

    def test_07_verify_the_filters_functionality_in_the_edit_screen(self):
        """
        Description: C51953897
            1.Tap on the "Camera Scan" tile.
            2.Capture a file.
            3.Tap "Next" on the Adjust Boundaries screen.
            4.Navigate to the Preview page.
            5.Click on 3 dots and tap on edit button
            6.Select Filters button Observe the behavior.
        Expected Result:
            Verify user able to navigate to the Filters screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.verify_edit_screen_title()
        self.print_preview.click_edit_screen_filter_btn()
        self.print_preview.verify_edit_screen_title()
        assert self.print_preview.get_edit_screen_title() == "Filters", "Expected edit screen title is 'Filters' but got {}".format(self.print_preview.get_edit_screen_title())
        self.print_preview.click_edit_screen_done_btn()

    def test_08_verify_the_text_functionality_in_the_edit_screen(self):
        """
        Description: C51953898
            1.Tap on the "Camera Scan" tile.
            2.Capture a file.
            3.Tap "Next" on the Adjust Boundaries screen.
            4.Navigate to the Preview page.
            5.Click on 3 dots and tap on edit button
            6.Select Text button Observe the behavior.
        Expected Result:
            Verify user able to navigate to the Text screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.verify_edit_screen_title()
        self.print_preview.click_edit_screen_text_btn()
        self.print_preview.verify_edit_screen_title()
        assert self.print_preview.get_edit_screen_title() == "Add Text", "Expected edit screen title is 'Add Text' but got {}".format(self.print_preview.get_edit_screen_title())
        self.print_preview.click_edit_screen_done_btn()

    def test_09_verify_the_text_functionality_in_the_edit_screen(self):
        """
        Description: C51953898
            1.Tap on the "Camera Scan" tile.
            2.Capture a file.
            3.Tap "Next" on the Adjust Boundaries screen.
            4.Navigate to the Preview page.
            5.Click on 3 dots and tap on edit button
            6.Select Text button Observe the behavior.
        Expected Result:
            Verify user able to navigate to the Markup screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_edit_btn()
        self.print_preview.verify_edit_screen_title()
        self.print_preview.click_edit_screen_markup_btn()
        assert self.print_preview.get_edit_screen_title() == "Markup", "Expected edit screen title is 'Markup' but got {}".format(self.print_preview.get_edit_screen_title())
        self.print_preview.click_edit_screen_done_btn()

    def test_10_verify_the_replace_button_functionality_in_edit_screen(self):
        """
        Description: C51953903
            2.Tap on the "Camera Scan" tile.
            3.Capture a file.
            4.Tap "Next" on the Adjust Boundaries screen.
            5.Navigate to the Preview page.
            6.Click on 3 dots and tap on Replace Button
            7.Observe the behavior.
        Expected Result:
            Verify user able to navigate to the Replace screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_page_option_btn()
        self.print_preview.click_page_option_replace_btn()
        self.camera_scan.verify_camera_scan_capture_mode()

    def test_11_verify_the_behavior_of_the_preview_scan(self):
        """
        Description: C51953906
            1.Tap on the "Camera Scan" tile.
            2.Capture a file.
            3.Tap "Next" on the Adjust Boundaries screen.
            4.Navigate to the Preview page.
            5.Click on Print Preview button
            6.Observe the behavior.
        Expected Result:
            Verify user able to navigate to the Print Preview screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_preview_button()
        self.print_preview.verify_print_preview_screen()

    def test_12_verify_the_behavior_of_the_preview_scan_first_flow_with_the_mobile_fax_option(self):
        """
        Description: C51953909
            1.Sign in to your account.
            2.Navigate to the Home page.
            3.Tap on the "Camera Scan" tile.
            4.Capture a file.
            5.Tap "Next" on the Adjust Boundaries screen.
            6.Navigate to the Preview page.
            7.Click on Mobile Fax button
            8.Observe the behavior.
        Expected Result:
            Verify user able to navigate to the Compose Fax screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_fax_btn()
        self.print_preview.verify_compose_fax_page_title()

    def test_13_verify_the_behavior_of_the_preview_scan_first_flow_with_the_share_option(self):
        """
        Description: C51953908
            1.Sign in to your account.
            2.Navigate to the Home page.
            3.Tap on the "Camera Scan" tile.
            4.Capture a file.
            5.Tap "Next" on the Adjust Boundaries screen.
            6.Navigate to the Preview page.
            7.Click on Share button
            8.Observe the behavior.
        Expected Result:s
            User able to see the share option Screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.select_share_btn()
        self.print_preview.verify_save_and_share_option_title()

    def test_14_verify_the_behavior_of_the_preview_scan_first_flow_with_the_save_option(self):
        """
        Description: C51953907
            1.Sign in to your account.
            2.Navigate to the Home page.
            3.Tap on the "Camera Scan" tile.
            4.Capture a file.
            5.Tap "Next" on the Adjust Boundaries screen.
            6.Navigate to the Preview page.
            7.Click on Save button
            8.Observe the behavior.
        Expected Result:
            User able to see the save option Screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_save_btn()
        self.print_preview.verify_save_and_share_option_title()

    def test_15_verify_the_document_name_on_the_landing_page(self):
        """
        Description: C51953910
            1.Sign in to your account.
            2.Navigate to the Home page.
            3.Tap on "Scan" and scan a file.
            4.Navigate to the Preview page and tap on "Shortcuts."
            5.Observe the behavior.
        Expected Result:
            The Name section is displayed, and the user can add a name to the shortcut.
        """
        shortcut_name = "Test_Shortcut_Name"
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_shortcut_btn()
        self.print_preview.verify_shortcut_name_txt_btn()
        self.print_preview.edit_shortcut_name(shortcut_name)
        assert self.print_preview.get_shortcut_name() == shortcut_name, f"Expected shortcut name is '{shortcut_name}' but got '{self.print_preview.get_shortcut_name()}'"

    def test_16_verify_the_behavior_of_the_scan_preview_under_the_shortcuts_option(self):
        """
        Description: C51953890
            1.Sign in to your account.
            2.Navigate to the Home page.
            3.Tap on the "Camera Scan" tile and capture a file.
            4.Tap on "Next" on the Adjust Boundaries screen.
            5.Tap on "Shortcuts."
            6.Observe the Preview page.
        Expected Result:
            The text in the textbox for naming the document in the Document Name section
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_camera_scan_tile(raise_e=False)
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_shortcut_btn()
        self.print_preview.verify_shortcut_name_txt_btn()