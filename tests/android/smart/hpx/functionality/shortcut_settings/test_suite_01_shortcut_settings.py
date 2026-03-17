import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES


pytest.app_info = "Smart"

class Test_Suite_01_Shortcut_Settings(object):

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
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_verify_the_shortcut_settings_screen_with_only_print_option(self):
        """
        Description: C51953770
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Verify the Shortcut settings screen.
        Expected Result:
           The 'File Type' Should not be displayed in the 'Shortcut setting' screen.
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
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()
        assert not self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen(), '"File Type" should not be present on the screen'

    def test_02_verify_screen_when_user_clicks_back_button_in_shortcut_setting_screen(self):
        """
        Description: C51953771
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen and click on Add to shortcut button.
           Click on the back button.
           Verify the screen.
        Expected Result:
           User should be redirected to the 'Add Shortcut' screen.
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
        self.driver.back()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()

    def test_03_verify_the_shortcut_setting_screen_when_user_enters_a_text_into_the_shortcut_name_field(self):
        """
        Description: C51953772
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the text into the shortcut name field.
           Verify the shortcut name field.
        Expected Result:
           User should be able to enter the text into the Shortcut name field without any error.
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
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name="shortcut test")
        assert self.hpx_shortcuts.verify_save_shortcut_btn().is_enabled(),'"Save Shortcut" button should be enabled when the shortcut name is entered'

    def test_04_verify_the_shortcut_setting_screen_when_user_enters_a_numerical_value_into_the_shortcut_name_field(self):
        """
        Description: C51953773
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the numerical value into the shortcut name field..
           Verify the shortcut name field.
        Expected Result:
           User should be able to enter the text into the Shortcut name field without any error.
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
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name="12345678")
        assert self.hpx_shortcuts.verify_save_shortcut_btn().is_enabled(),'"Save Shortcut" button should be enabled when the shortcut name is entered'

    def test_05_verify_the_shortcut_setting_screen_when_user_enters_alpha_numerical_value_into_the_shortcut_name_field(self):
        """
        Description: C51953774
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the alphanumerical value into the shortcut name field..
           Verify the shortcut name field.
        Expected Result:
           User should be able to enter the text into the Shortcut name field without any error.
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
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name="A1b2c3")
        assert self.hpx_shortcuts.verify_save_shortcut_btn().is_enabled(),'"Save Shortcut" button should be enabled when the shortcut name is entered'

    def test_06_verify_the_shortcut_setting_screen_when_user_enters_special_characters_value_into_the_shortcut_name_field(self):
        """
        Description: C51953775
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Navigate to 'Add print' screen.
           Click on the Add to shortcut button.
           Enter the special characters value into the shortcut name field..
           Verify the shortcut name field.
        Expected Result:
           User should not able to enter the text into the Shortcut name field without any error.
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
        self.hpx_shortcuts.enter_shortcut_name(shortcut_name="!@#%$^&*")
        assert not self.hpx_shortcuts.verify_save_shortcut_btn().is_enabled(), '"Save Shortcut" button should be disabled when the special character shortcut name is entered'

    def test_07_verify_the_shortcut_setting_screen_when_user_clicks_on_quick_run_toggle(self):
        """
        Description: C51953776
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
   
    def test_08_verify_shortcut_setting_screen_when_user_clicks_on_smart_file_name_toggle(self):
        """
        Description: C51953777
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
        self.hpx_shortcuts.enter_edit_shortcut_email_receiver_email_id_field(email_id='testqama@')
        self.hpx_shortcuts.click_edit_shortcut_continue_btn()
        self.hpx_shortcuts.verify_file_type_in_shortcut_settings_screen()
        assert self.hpx_shortcuts.verify_img_file_type()
        assert self.hpx_shortcuts.verify_pdf_file_type()

    def test_09_verify_shortcut_setting_screen_when_user_clicks_on_desired_color(self):
        """
        Description: C51953778
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

    def test_10_verify_shortcut_setting_screen_when_user_clicks_add_button_of_shortcut_color_setting(self):
        """
        Description: C51953779
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

    def test_11_verify_shortcut_setting_screen_when_user_clicks_add_button_and_selects_color(self):
        """
         Description: C51953780
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