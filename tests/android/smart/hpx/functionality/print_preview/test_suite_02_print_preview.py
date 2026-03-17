import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "Smart"

class Test_Suite_02_print_preview:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        cls.photos = cls.fc.fd[FLOW_NAMES.PHOTOS]
        cls.fc.hpx = True

    def test_01_verify_print_preview_screen_ui(self):
        """
        Description: C44019115
        Steps:
            Launch the app.
            Sign in and navigate to rootview
            Add a printer and navigate to device detail page.
            Tap on Print Photo
            Select a photo and navigate to Print Preview screen.
            Observe the Print Preview screen.
        Expected Result:
            Verify the Print preview screen shows with Done button and Back arrow
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.print_photos_preview_next_btn()
        self.print_preview.verify_print_preview_screen()
    
    def test_02_verify_the_done_button_on_print_preview_screen(self):
        """
        Description: C44019117
        Steps:
            Launch the app.
            Sign in and navigate to Home screen.
            On Home screen tap "Print Photos" tile.
            Select a photo and navigate to Print Preview screen.
            Observe.
            Tap on Done button on top right.
        Expected Result:
             Verify that there is Done button
             Verify the user is navigated back
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()

    def test_03_verify_the_share_option_on_print_preview_screen(self):
        """
        Description: C44019118
        Steps:
            Launch application and perform login and proceed to Rootview.
            Add a printer and tap on printer card and navigate to Device Detail page.
            Tap "Print Photos" tile.
            Select a photo and navigate to Print Preview screen.
            In print preview screen Fully open the Print Settings panel.
            Tap on "Share" button.
        Expected Result:
            Verify that the user is able to share the photo from Print Preview screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.verify_print_preview_done_btn()
        self.print_preview.click_print_btn()
        self.print_preview.click_print_preview_share_photo_btn()
    
    def test_04_verify_the_share_button_on_the_print_preview_screen_ui(self):
        """
        Description: C44019119
        Steps:
            Launch the app.
            Sign in and navigate to rootview
            Add a printer and navigate to device detail page.
            Tap on Print Photo
            Select a photo and navigate to Print Preview screen.
            Observe the Print Preview screen.
        Expected Result:
            Verify the Print preview screen shows with Done button
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.verify_print_preview_done_btn()

    def test_05_verify_the_navigation_to_print_jobs(self):
        """
        Description: C44019120
        Steps:
            Launch application and perform login and proceed to Rootview.
            Add a printer and tap on printer card and navigate to Device Detail page.
            Tap "Print Photos" tile.
            Select a photo and navigate to Print Preview screen.
            Tap on the hamburger menu button on top right.
        Expected Result:
            Verify that the user is navigated to Print Jobs screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.click_view_print_job_list_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_jobs_title()
    
    def test_06_verify_the_share_option_on_print_preview_screen(self):
        """
        Description: C44019122
        Steps:
            Launch application and perform login and proceed to Rootview.
            Add a printer and tap on printer card and navigate to Device Detail page.
            Tap "Print Photos" tile.
            Select photo and tap on Next button
            Verify that there is no "Share" button in the top bar.
            Fully open the Print Settings panel.
            Tap on "Share" button.
        Expected Result:
            Verify that the user is able to share the photo from Print Preview screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.verify_print_preview_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.click_print_btn()
        self.print_preview.click_print_preview_share_photo_btn()
    
    def test_07_verify_print_jobs_list_screen(self):
        """
        Description: C44019121
        Steps:
            Launch application and perform login and proceed to Rootview.
            Add a printer and tap on printer card and navigate to Device Detail page.
            Tap "Print Photos" tile.
            Select a photo and navigate to Print Preview screen.
            Tap on hamburger menu button on top right.
            Observe the Print Jobs screen
        Expected Result:
            Verify the Print Jobs UI
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.verify_print_photo_preview_title()
        self.print_preview.verify_print_preview_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.click_view_print_job_list_btn()
        self.print_preview.verify_print_jobs_title()
    
    def test_08_verify_the_back_arrow_button_on_print_preview_screen(self):
        """
        Description: C44019123
        Steps:
            Launch application and perform login and proceed to Rootview.
            Add a printer and tap on printer card and navigate to Device Detail page.
            Tap "Print Photos" tile.
            Select a photo and navigate to Print Preview screen.
            Tap on Back arrow button on top left.
        Expected Result:
            Verify that the user is navigated back to Device Detail screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipaddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.select_back_btn()

    def test_09_verify_the_warning_message_for_paper_size_on_paper_settings_screen(self):
        """
        Description: C44019127
        Steps:
            Launch application.
            Perform login and proceed to Rootview.
            Add a printer
            Tap on printer card and navigate to Device Detail page
            Tap "Print Photos" tile.
            Select a photo and navigate to Print Preview screen.
            Open the Print Settings panel by tapping on up arrow on Drawer menu.
            Check the warning message under paper.
        Expected Result:
            Verify that the warning message is displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipaddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.select_5X7_paper_size()
        self.print_preview.click_print_photos_preview_next_btn()
        self.driver.swipe()
        self.print_preview.verify_paper_size_load_error()
    
    def test_09_verify_the_printer_settings_drawer_menu_ui(self):
        """
        Description: C44019128
        Steps:
            Launch application and perform login and proceed to Rootview.
            Add a printer and tap on printer card and navigate to Device Detail page.
            Tap "Print Photos" tile.
            Select a photo and navigate to Print Preview screen.
            Open the Print Settings panel by tapping on up arrow on Drawer menu.
            Observe.
        Expected Result:
            Verify that the drawer menu is displayed with Color Options
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipaddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.driver.swipe()
        self.print_preview.verify_color_options_drop_down()
    
    def test_11_verify_the_warning_message_for_paper_source_when_incorrect_paper_is_loaded(self):
        """
        Description: C44019129
        Steps:
            Launch application and perform login and proceed to Rootview.
            Add a printer and tap on printer card and navigate to Device Detail page.
            Tap "Print Photos" tile.
            Select a photo and go to DS screen.
            Select a paper size that not loaded to printer.
            Go to print preview screen.
            Check the warning message under paper source.     
        Expected Result:
               Verify that the warning message is displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipaddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.select_5X7_paper_size()
        self.print_preview.click_print_photos_preview_next_btn()
        self.driver.swipe()
        self.print_preview.verify_paper_size_load_error()
    
    def test_12_verify_print_job_is_cancelled(self):
        """
        Description: C44019133
        Steps:
            Launch application and perform login and proceed to Rootview.
            Add a printer and tap on printer card and navigate to Device Detail page.
            Tap "Print Photos" tile.
            Select a photo and navigate to Print Preview screen.
            Tap on Print.
            Navigate to Print Jobs screen.
            Click on the Cancel button on the print job.
        Expected Result:
            Verify that the print job is cancelled.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.click_print_btn()
        self.print_preview.click_view_print_job_list_btn()
        self.print_preview.verify_print_jobs_title()
        self.print_preview.click_cancel_print_job()
        self.print_preview.verify_print_job_canceled_message()
    
    def test_13_verify_the_share_button_next_to_reprint_button_after_successful_print(self):
        """
        Description: C44019140
        Steps:
            Launch application and perform login and proceed to Rootview.
            Add a printer and tap on printer card and navigate to Device Detail page.
            Tap "Print Photos" tile.
            Select a photo and navigate to Print Preview screen.
            Tap on Print.
            Observe the buttons at the bottom of Print Preview screen after successful print.
            Tap on Share.
        Expected Result:
            Verify that the user is able to share the photo from Print Preview screen after successful print.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_print_photos_tile(raise_e=False)
        self.photos.select_single_photo()
        self.photos.click_hpx_photos_select_done_btn()
        self.print_preview.click_print_photos_preview_next_btn()
        self.print_preview.click_print_btn()
        self.print_preview.click_print_preview_share_photo_btn()