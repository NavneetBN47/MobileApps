import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES


pytest.app_info = "Smart"

class Test_Suite_01_Shortcut_Basic_Functionality(object):

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
        # Enable HPX Flag
        cls.fc.hpx = True


    def test_01_verify_shortcuts_tile_available_on_printer_details_page(self):
        """
        Description: C51953630
           Install and Launch the HPX app.
           Click on the printer icon on the root view screen.
           Verify the shortcuts tile on device details page.
        Expected Result: 
           Shortcuts' tile should be displayed on the printer device page.    
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)

    def test_02_verify_shortcuts_feature_after_user_creates_account(self):
        """
        Description: C51953631
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on the shortcuts tile on the device details page.
            Verify the behaviour.
        Expected Result:      
            Getting information loading screen should be dispalyed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.shortcuts.verify_shortcuts_screen()

    def test_03_verify_user_can_access_shortcuts_tile_without_login(self):
        """
        Description: C51953632
           Install and Launch the HPX app.
           Click on the printer icon on the root view screen.
           Then click on shortcuts tile on the device details page.
           Verify the behaviour.
        Expected Result: 
           The user should not be able to access the shortcuts tile without logging in.   
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.account.verify_tiles_not_signed_in_page()

    def test_04_verify_screen_after_clicking_shortcuts_tile_without_login(self):
        """
        Description: C51953633
           Install and Launch the HPX app.
           Click on the printer icon on the root view screen.
           Then click on shortcuts tile on the device details page.
           .Verify the screen.
        Expected Result: 
           Dialog screen should be displayed as below screen.
           Sign in to use Shortcuts   
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.account.verify_tiles_not_signed_in_page()

    def test_05_verify_screen_when_user_clicks_back_on_sign_in_to_use_shortcuts_dialog(self):
        """
        Description: C51953634
           Install and Launch the HPX app.
           Navigate to the printer details page then click on the shortcuts tile.
           In 'Sign in to use shorcuts' dialog screen click on 'Back' button.
           Verify the screen.
        Expected Result: 
           User should be navigated to the Printer device page.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.shortcuts.click_back_btn()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.verify_shortcuts_tile()

    def test_06_verify_behavior_when_user_clicks_sign_in_to_use_shortcuts(self):
        """
        Description: C51953635
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on shortcuts tile on the device details page.
            Click on the "Sign in to use shortcuts" string and shortcuts icon.
            Verify the behavior.
        Expected Result: 
           User should not able to access the 'Sign in to use shortcuts' string and shortcuts icon.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        self.account.click_sign_in_to_use_shortcuts_string()
        self.account.verify_tiles_not_signed_in_page()

    def test_07_verify_position_of_buttons_on_sign_in_to_use_shortcuts_screen(self):
        """
        Description: C51953636
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on shortcuts tile on the device details page.
            Verify the buttons.
        Expected Result:
             The position of the buttons on the 'Sign in to use Shortcuts' screen should have 'Sign in' as the primary button and 'Create Account' as the secondary button.
            """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)
        assert self.account.verify_sign_in_btn().location['y'] < self.account.verify_create_account_btn().location['y'], "Sign In button is not above Create Account button"    

    def test_08_verify_screen_when_user_clicks_create_account_btn(self):
        """
        Description: C51953637
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on shortcuts tile on the device details page.
            Click on the Create account button.
            Verify the behavior.
        Expected Result:    
            User should be navigated to the Create account screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.account.click_create_account_btn()  
        assert self.shortcuts.verify_create_account_page()

    def test_09_verify_screen_after_user_created_account(self):
        """
        Description: C51953638
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on shortcuts tile on the device details page.
            Click on the Create account button.
            Create the account.
            Verify the screen.
        Expected Result:
            User should be navigated to the Shortcuts screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.account.click_create_account_btn()  
        self.hpid.create_account()
        self.shortcuts.verify_shortcuts_screen()

    def test_10_verify_screen_when_user_clicks_sign_in_btn(self):
        """
        Description: C51953639
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on shortcuts tile on the device details page.
            Click on the Sign in button.
            Verify the screen.
        Expected Result:
            User should be navigated to the Sign in screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.account.click_sign_in_btn()  
        assert self.shortcuts.verify_sign_in_page()

    def test_11_verify_screen_after_user_signed_in(self):
        """
        Description: C51953640
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on the shortcuts tile on the device details page.
            Click on the Sign in button.
            Enter the existing user credentials.
            Verify the screen.
        Expected Result:
            User should be navigated to the Shortcuts screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.account.click_sign_in_btn() 
        self.hpid.login()
        self.shortcuts.verify_shortcuts_screen()

    def test_12_verify_screen_when_user_clicks_back_button_in_shortcuts_screen(self):
        """
        Description: C51953641
            Install and Launch the HPX app.
            Click on the printer icon on the root view screen.
            Then click on the shortcuts tile on the device details page.
            Click on Back button in Shortcuts screen.
            Verify the screen.
        Expected Result:
            User should be navigated to the Printer device page.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.hpx_printer_details.click_add_device_btn()
        # self.printers.search_printer_by_ip(self.p.ipAddress)
        # self.device_mfe.click_device_tile()
        self.hpx_printer_details.click_feature_unavailable_popup_if_exist(raise_e=False)
        self.hpx_printer_details.click_shortcuts_tile(raise_e=False)  
        self.shortcuts.verify_shortcuts_screen()
        self.shortcuts.click_back_btn()
        self.hpx_printer_details.verify_shortcuts_tile()