import pytest
from datetime import datetime as Datetime
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES


pytest.app_info = "Smart"

class Test_Suite_05_Shortcut_Settings(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.scan = cls.fc.fd[FLOW_NAMES.SCAN]
        cls.print_preview = cls.fc.fd[FLOW_NAMES.PRINT_PREVIEW]
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_verify_shortcut_setting_screen_when_user_clicks_add_button_of_shortcut_color_setting(self):
        """
        Description: C51953811
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Click on the '+' button in Shortcut color in 'Shortcut setting' screen.
           Verify the shortcut color option.
        Expected Result:
           User should be able view the additional color.[TBD]
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_add_button()

    def test_02_verify_shortcut_setting_screen_when_user_clicks_add_button_and_selects_color(self):
        """
         Description: C51953812
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Click on the '+' button and select the color.
           Verify the shortcut color option.
        Expected Result:
           User should be able to select the color after clicking on the '+' button  
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_add_button()
        self.hpx_shortcuts.click_color_card_by_index(index=1)
        assert self.hpx_shortcuts.verify_color_card_selection(index=1), "First color card should be selected"

    def test_03_verify_the_screen_when_the_user_clicks_the_save_shortcut_button_after_selecting_settings_from_the_shortcut_settings_screen(self):
        """
        Description: C51953814
            Install and Launch the HPX app.
            Navigate to printer details screen.
            Click on the shortcuts tile.
            Click on 'Add new Shortcut'.
            Navigate to 'Add print' screen.
            Click on the Add to shortcut button.
            Select the desired settings from shortcut setting screen.
            Click on the Save shortcut button.
            Verify the screen.
        Expected Result:
            User shoul be able to save the desired settings successfully without any issue.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_print_copies_dropdown_btn()
        self.hpx_shortcuts.select_copies_number(copies_number="three")
        assert self.hpx_shortcuts.verify_select_copies_number(copies_number="three")
        self.hpx_shortcuts.click_select_color_dropdown_btn()
        self.hpx_shortcuts.select_color_option(color_option="grayscale")  
        assert self.hpx_shortcuts.verify_select_color_option(color_option="grayscale")
        self.hpx_shortcuts.click_two_sided_dropdown_btn()
        self.hpx_shortcuts.select_two_sided_option(two_sided_option="long_edge")
        assert self.hpx_shortcuts.verify_select_two_sided_option(two_sided_option="long_edge")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_done_btn()
        assert self.hpx_shortcuts.verify_shortcut_present_in_list(shortcut_name), f"The created shortcut '{shortcut_name}' should be present in the shortcuts list"

    def test_04_verify_the_screen_when_the_user_clicks_on_run_this_shortcut_button(self):
        """
        Description: C51953815
            Install and Launch the HPX app.
            Navigate to printer details screen.
            Click on the shortcuts tile.
            Click on 'Add new Shortcut'.
            Navigate to 'Add print' screen.
            Click on the Add to shortcut button.
            Select the desired settings from shortcut setting screen.
            Click on the Save shortcut button.
            Click on Run this Shortcut button.
            Verify the screen.
        Expected Result:
            User should be navigated to the 'Select a source' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_print_copies_dropdown_btn()
        self.hpx_shortcuts.select_copies_number(copies_number="three")
        assert self.hpx_shortcuts.verify_select_copies_number(copies_number="three")
        self.hpx_shortcuts.click_select_color_dropdown_btn()
        self.hpx_shortcuts.select_color_option(color_option="grayscale")  
        assert self.hpx_shortcuts.verify_select_color_option(color_option="grayscale")
        self.hpx_shortcuts.click_two_sided_dropdown_btn()
        self.hpx_shortcuts.select_two_sided_option(two_sided_option="long_edge")
        assert self.hpx_shortcuts.verify_select_two_sided_option(two_sided_option="long_edge")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        assert self.camera_scan.verify_select_scan_source_screen(), "scan source screen should be displayed after clicking 'Run this Shortcut' button"

    def test_05_verify_screen_when_user_clicks_shortcuts_button(self):
        """
        Description: C51953816
            Install and Launch the HPX app.
            Navigate to printer details screen.
            Click on the shortcuts tile.
            Click on 'Add new Shortcut'.
            Navigate to 'Add print' screen.
            Click on the Add to shortcut button.
            Select the desired settings from shortcut setting screen.
            Click on the Save shortcut button.
            Click on Run this Shortcut button.
            Verify the screen.
        Expected Result:
            The Shortcut should be saved and user should be navigated to the Shortcuts screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_print_copies_dropdown_btn()
        self.hpx_shortcuts.select_copies_number(copies_number="three")
        assert self.hpx_shortcuts.verify_select_copies_number(copies_number="three")
        self.hpx_shortcuts.click_select_color_dropdown_btn()
        self.hpx_shortcuts.select_color_option(color_option="grayscale")  
        assert self.hpx_shortcuts.verify_select_color_option(color_option="grayscale")
        self.hpx_shortcuts.click_two_sided_dropdown_btn()
        self.hpx_shortcuts.select_two_sided_option(two_sided_option="long_edge")
        assert self.hpx_shortcuts.verify_select_two_sided_option(two_sided_option="long_edge")
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_done_btn()
        assert self.hpx_shortcuts.verify_shortcut_present_in_list(shortcut_name), f"The created shortcut '{shortcut_name}' should be present in the shortcuts list"
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()

    def test_06_verify_already_created_shortcut_when_user_runs_it_for_save_destination(self):
        """
        Description: C51953817
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on the created Shortcuts.
           Run the shortcut.
           Capture a file.
           Click on the 'Next' on detect edges page and click Next.
           Go tp preview screen.
           Click on the Shortcuts button.
           Select Email shortcut.
           Verify the behavior.
        Expected Result:
           Your file is processing' pop up should be dsiplayed.
           Your Shortcut is on its way' pop up should be displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_quick_run_toggle_btn()
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)
        self.hpx_shortcuts.click_save_shortcut_btn()
        self.hpx_shortcuts.click_run_this_shortcut_btn()
        self.camera_scan.click_camera_scan_source_btn()
        self.camera_scan.select_camera_access_allow()
        self.camera_scan.select_camera_permission_allow_btn()
        self.scan.dismiss_coachmark()
        self.camera_scan.click_shutter()
        self.camera_scan.select_adjust_next_btn()
        self.print_preview.click_print_btn()
        assert self.print_preview.verify_alert_message() == f"{self.p.name} waiting", f"Expected '{self.p.name} waiting' but got '{self.print_preview.verify_alert_message()}'"

    def test_07_verify_shortcut_settings_screen_for_email_option(self):
        """
        Description: C51953820
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add Email' screen.
           Click on the Add to shortcut button.
            Verify the Shortcut settings screen.
        Expected Result:
           The 'Shortcut Settings' screen should contains the below fields as shown on the screen below.
           'Shortcut Setting' title
           Shortcut name field
           Quick Run toggle
           Smart file name toggle
           'File Type' title
           File Type, where different file types can be choosen.
           Shortcut Color with different color options and '+' button.
           Continue button.
           ShortcutColor with different color options and '+' button.
           Save Shortcuts button
           Note: Only 'File types' apper when the user selects 'Save' or 'Email' option.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@gmail.com')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen()
        assert self.hpx_shortcuts.verify_img_file_type()
        assert self.hpx_shortcuts.verify_pdf_file_type()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()    
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)   
        assert self.hpx_shortcuts.verify_quick_run_toggle()
        assert self.hpx_shortcuts.verify_add_button()
        assert self.hpx_shortcuts.verify_save_shortcut_btn()

    def test_08_verify_shortcut_settings_screen_for_save_option_supported_printer(self):
        """
        Description: C51953821
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add Email' screen.
           Click on the Add to shortcut button.
            Verify the Shortcut settings screen.
        Expected Result:
           The 'Shortcut Settings' screen should contains the below fields as shown on the screen below.
           'Shortcut Setting' title
           Shortcut name field
           Quick Run toggle
           Smart file name toggle
           'File Type' title
           File Type, where different file types can be choosen.
           Shortcut Color with different color options and '+' button.
           Continue button.
           ShortcutColor with different color options and '+' button.
           Save Shortcuts button
           Note: Only 'File types' apper when the user selects 'Save' or 'Email' option.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()    
        self.hpx_shortcuts.click_google_drive_signin_link()
        self.hpx_shortcuts.click_account_selection()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn() 
        self.hpx_shortcuts.click_edit_shortcut_continue_btn() 
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@gmail.com')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen()
        assert self.hpx_shortcuts.verify_img_file_type()
        assert self.hpx_shortcuts.verify_pdf_file_type()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()    
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)   
        assert self.hpx_shortcuts.verify_quick_run_toggle()
        assert self.hpx_shortcuts.verify_add_button()
        assert self.hpx_shortcuts.verify_save_shortcut_btn()
             
    def test_09_verify_shortcut_settings_screen_with_all_options_supported_printer(self):
        """
        Description: C51953822
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add Email' screen.
           Click on the Add to shortcut button.
            Verify the Shortcut settings screen.
        Expected Result:
           The 'Shortcut Settings' screen should contains the below fields as shown on the screen below.
           'Shortcut Setting' title
           Shortcut name field
           Quick Run toggle
           Smart file name toggle
           'File Type' title
           File Type, where different file types can be choosen.
           Shortcut Color with different color options and '+' button.
           Continue button.
           ShortcutColor with different color options and '+' button.
           Save Shortcuts button
           Note: Only 'File types' apper when the user selects 'Save' or 'Email' option.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_create_your_own_shortcut()
        self.hpx_shortcuts.click_edit_shortcut_print_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_save_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@gmail.com')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_google_drive_signin_link()
        self.hpx_shortcuts.click_account_selection()
        self.driver.swipe(direction='down')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn() 
        self.hpx_shortcuts.click_edit_shortcut_continue_btn() 
        self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen()
        assert self.hpx_shortcuts.verify_img_file_type()
        assert self.hpx_shortcuts.verify_pdf_file_type()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()    
        shortcut_name = "shortcut_test"+str(Datetime.now().strftime("%Y%m%d%H%M%S"))
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name)   
        assert self.hpx_shortcuts.verify_quick_run_toggle()
        assert self.hpx_shortcuts.verify_add_button()
        assert self.hpx_shortcuts.verify_save_shortcut_btn()