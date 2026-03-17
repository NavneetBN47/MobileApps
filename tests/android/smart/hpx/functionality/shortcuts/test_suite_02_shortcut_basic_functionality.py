import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES


pytest.app_info = "Smart"

class Test_Suite_02_Shortcut_Basic_Functionality(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.shortcuts = cls.fc.flow[FLOW_NAMES.SHORTCUTS]
        cls.account = cls.fc.fd[FLOW_NAMES.HP_CONNECT_ACCOUNT]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.hpid = cls.fc.fd[FLOW_NAMES.HPID]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        # Enable HPX Flag
        cls.fc.hpx = True

    def test_01_verify_screen_when_user_clicks_settings_icon_in_shortcuts_screen(self):
        """
        Description: C51953642
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on the shortcuts tile on the device details page.
            Click on Settings icon in Shortcuts screen.
            Verify the screen.
        Expected Result:
            User should be navigated to the Settings screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.verify_shortcuts_screen_title()
        self.hpx_shortcuts.click_shortcuts_settings_icon()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()

    def test_02_verify_screen_when_user_clicks_edit_link_in_shortcuts_screen(self):
        """
        Description: C51953643
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on the shortcuts tile on the device details page.
            Click on Edit link in shortcuts screen.
            Verify the screen.
       
        Expected Result:
            User should be navigated to the 'Shortcuts -Edit turned on' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card() 
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        assert not self.hpx_shortcuts.verify_shortcuts_edit_btn().is_enabled(), '"Edit" link should be disabled'    

    def test_03_verify_the_edit_link_and_add_new_shortcut_element_after_user_clicking_on_the_edit_link(self):
        """
        Description: C51953644
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on the shortcuts tile on the device details page.
            Click on Edit link in shortcuts screen.
            Verify the screen.
        Expected Result:
            The "Edit" link and "Add New Shortcut" element should be disabled, and the user should not be able to access them.     
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        assert not self.hpx_shortcuts.verify_shortcuts_edit_btn().is_enabled(), '"Edit" link should be disabled'    
        assert not self.hpx_shortcuts.verify_add_new_shortcut_btn().is_enabled(), '"Add New Shortcut" button should be disabled' 

    def test_04_verify_screen_when_user_clicks_back_button_in_shortcuts_edit_turned_on_screen(self):
        """
        Description: C51953645
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on the shortcuts tile on the device details page.
            Click on Edit link in shortcuts screen.
            Then click on back button.
            Verify the screen.
        Expected Result:
            User should be navigated to the Shortcuts screen.    
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        self.driver.back()
        self.hpx_printer_details.verify_shortcuts_tile()

    def test_05_verify_screen_when_user_clicks_settings_icon_in_shortcuts_edit_turned_on_screen(self):
        """
        Description: C51953646
           Install and Launch the HPX app.
           Click on the printer icon on the root view screen.
           Then click on the shortcuts tile on the device details page.
           Click on Edit link in shortcuts screen.
           Then click on settings icon.
           Verify the screen.
        Expected Result:
            User should be navigated to the Settings screen.  
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_shortcuts_edit_btn()
        self.hpx_shortcuts.click_shortcuts_settings_icon()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()

    def test_06_verify_shortcuts_screen_when_no_shortcuts_created(self):
        """
        Description: C51953647
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on the shortcuts tile on the device details page.
            Verify the Shortcuts screen.         
        Expected Result:
            By default Email shortcut should be added in shortcuts screen.[TBD]  
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        assert self.hpx_shortcuts.verify_shortcuts_email_btn()

    def test_07_verify_shortcuts_behavior_as_new_user(self):
        """
        Description: C51953652
            Install and Launch the HPX app.
            Navigate to the shortcuts screen.
            Verify the screen.
        Expected Result:
            User should be navigated to the shorcuts screen and one shorcut should be displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        assert self.hpx_shortcuts.verify_shortcuts_email_btn()

    def test_08_verify_prebuilt_shortcuts_in_shortcuts_screen(self):
        """
        Description: C51953654
            Install and Launch the HPX app.
            Navigate to the shortcuts screen.
            Verify the screen.
        Expected Result:
            Add Shortcut' screen should be displayed with pre build shortcuts as below screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        assert self.hpx_shortcuts.verify_add_new_shortcut_btn()
        assert self.hpx_shortcuts.verify_shortcuts_email_btn()

    def test_09_verify_add_new_shortcut_arrow_button_navigates_to_add_new_shortcut_screen(self):
        """
        Description: C51953655
           Install and Launch the HPX app.
           Navigate to the shortcuts screen.
           Then click on the Add new shortcut arrow button.
           Verify the screen.
        Expected Result:
           User should be navigated to the 'Add new shortcuts' screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.verify_add_new_shortcut_screen_title()

    def test_10_verify_add_new_shortcut_arrow_button_navigates_to_add_new_shortcut_screen(self):
        """
        Description: C51953656
           Install and Launch the HPX app.
           Click on the printer icon on the root view screen.
           Then click on the shortcuts tile on the device details page.
           Click on the Add new shortcut arrow button.
           Click on the back button.
           Verify the screen.
        Expected Result:
           User should be navigated to the shortcuts screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.driver.back()
        self.hpx_shortcuts.verify_shortcuts_screen_title()

    def test_11_verify_screen_when_user_clicks_settings_icon_in_add_new_shortcut_screen(self):
        """
        Description: C51953657
           Install and Launch the HPX app.
           Click on the printer icon on the root view screen.
           Then click on the shortcuts tile on the device details page.
           Click on the Add new shortcut arrow button.
           Click on the Settings icon.
           Verify the screen.
        Expected Result:
           User should be navigated to the Settings screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_shortcuts_settings_icon()
        self.hpx_shortcuts.verify_shortcut_settings_screen_title()

    def test_12_verify_the_screen_when_user_clicks_on_the_edit_link_in_add_new_shortcuts_screen(self):
        """
        Description: C51953658
           Install and Launch the HPX app.
           Click on the printer icon on the root view screen.
           Then click on the shortcuts tile on the device details page.
           Click on Add new shortcuts in shortcuts screen.
           Then click on edit link.
           Verify the screen.
        Expected Result:
           User should be able to edit in Add new Shortcuts screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_shortcuts_edit_btn()


    def test_13_verify_back_button_functionality_in_add_new_shortcuts_screen(self):
        """
        Description: C51953659
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Click on the back button.
           Verify the screen.
           Then click on the 'Go back' button.
           Verify the screen.
           Then click on the 'Yes, cancel' button.
           Verify the screen.
        Expected Result:
            User should be navigated to the 'Shortcuts' screen.
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
        self.hpx_shortcuts.click_back_btn()
        self.hpx_shortcuts.click_cancel_shortcut_yes_cancel_btn()
        self.hpx_shortcuts.verify_shortcuts_screen_title()

    def test_14_verify_back_button_functionality_in_add_new_shortcuts_screen(self):
        """
        Description: C51953660
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Click on the settings button.
           Verify the screen.
        Expected Result:
            User should be navigated to the Settings screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.hpx_shortcuts.click_add_new_shortcut_btn()
        self.hpx_shortcuts.click_shortcuts_settings_icon()
        self.hpx_printer_details.verify_shortcut_settings_screen_title()

    def test_15_verify_back_button_functionality_in_add_new_shortcuts_screen(self):
        """
        Description: C51953661
           Install and Launch the HPX app.
           Navigate to printer details screen.
           Click on the shortcuts tile.
           Click on 'Add new Shortcut'.
           Click on the Create your own shortcut'.
           Verify the screen.
        Expected Result:
            Add Shortcut' screen should be displayed with the Print, Email and Save Destinations
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
        self.hpx_shortcuts.verify_save_destination()