import pytest
from datetime import datetime as Datetime
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES


pytest.app_info = "Smart"

class Test_Suite_03_Shortcut_Settings(object):

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

    def test_01_verify_the_shortcut_setting_screen_when_user_clicks_on_quick_run_toggle(self):
        """
        Description: C51953792
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Click on 'Quick run' toggle in 'Shortcut setting' screen.
           Verify the Quick run toggle option.
        Expected Result:
           User should be able to select the 'Quick run' toggle in 'Shortcut setting' screen.
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
        is_enabled = self.hpx_shortcuts.check_toggle_enabled_or_disabled("quick_run_toggle_btn")
        if not is_enabled:
            self.hpx_shortcuts.click_quick_run_toggle_btn()
        assert self.hpx_shortcuts.check_toggle_enabled_or_disabled("quick_run_toggle_btn")

    def test_02_verify_shortcut_setting_screen_when_user_clicks_on_smart_file_name_toggle(self):
        """
        Description: C51953793
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Click on 'Smart file name' toggle in 'Shortcut setting' screen.
           Verify the Quick run toogle option.
        Expected Result:
           User should be able to select the 'Smart file name' toogle in 'Shortcut setting' screen. 
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
        self.hpx_shortcuts.click_edit_shortcut_email_toggle_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@gmail.com')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.click_quick_run_toggle_btn()
        self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen()
        assert self.hpx_shortcuts.verify_img_file_type()
        assert self.hpx_shortcuts.verify_pdf_file_type()
        self.hpx_shortcuts.click_image_file_type()

    def test_03_verify_shortcut_setting_screen_when_user_clicks_on_desired_color(self):
        """
        Description: C51953794
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Click on the desired shortcut color in 'Shortcut setting' screen.
           Verify the shortcut color option.
        Expected Result:
           User should be able to select the desired shortcut color in shortcut setting screen.
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
        self.hpx_shortcuts.click_select_color_dropdown_btn()
        self.hpx_shortcuts.select_color_option(color_option="grayscale")   
        assert self.hpx_shortcuts.verify_select_color_option(color_option="grayscale")

    def test_04_verify_the_shortcut_setting_screen_when_user_clicks_on_the_add_button_of_shortcut_color_setting(self):
        """
        Description: C51953795
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

    def test_05_verify_shortcut_setting_screen_when_user_clicks_add_button_and_selects_color(self):
        """
         Description: C51953796
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

    def test_06_verify_the_screen_when_the_user_clicks_the_save_shortcut_button_after_selecting_settings_from_the_shortcut_settings_screen(self):
        """
        Description: C51953798
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

    def test_07_verify_the_screen_when_the_user_clicks_on_run_this_shortcut_button(self):
        """
        Description: C51953799
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

    def test_08_verify_screen_when_user_clicks_shortcuts_button(self):
        """
        Description: C51953800
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