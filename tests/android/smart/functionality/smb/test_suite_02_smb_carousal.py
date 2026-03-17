from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from MobileApps.resources.const.android.const import REMOTE_PRINTER_NAME

pytest.app_info = "SMART"

class Test_Suite_02_Smb_Carousal(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.smb = cls.fc.flow[FLOW_NAMES.SMB]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.printer_settings = cls.fc.flow[FLOW_NAMES.PRINTER_SETTINGS]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]

        # Define variables
        cls.fc.set_hpid_account(None, smb=True)
        cls.local_printer_name = cls.p.get_printer_information()["bonjour name"]
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_carousel_experience(self):
        """
        Description:
        C30582462, C30582463, C30582465, C30582467, C30582469, C30678398, C30582442, C30582443, C30582457, C30582449, C30582445, C30582446
         1. Launch smart app with a smb account login which has business and personal org
         2. Select a personal org
         3. Click on Add Printer on Home screen
         4. Select any printer from the printer list
         5. Click on Account button
         6. Select a business org which has printer claimed in
         7. Click on Add Printer on Home screen
         8. Select a printer from the list
         9. Click on Printer's icon on Home screen
         10. Click on Back button
         11. Click on Ink Level icon
         12. Click on Back button
         13. Click on Account button
         14. Click on Sign Out button -> SIGN OUT

        Expected Result:
        4. Verify the carousel should look as it is seen now
        6. Verify the printer from step 4 is invisible
        8. Verify the Printer from Step 4 is invisible
           Verify the Remote printer added to carousel success
        9.Verify Printer Settings page with below option:
           - Printer Information
           - All items under Preference/Reports are invisible
        11.Verify Printer Settings page with below option:
           - Printer Status
           - Printer Information
           - All items under Preference are invisible
        14.Verify the printer from Step 5 displays
           Verify Add Printer button on Home screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p, is_searched=True)
        self.home.verify_printer_model_name(self.local_printer_name, invisible=False)
        self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.smb.verify_account_menu()
        self.smb.select_business_org_from_account("euthenia_hp" if self.stack=="stage" else "Zelus_HP")
        self.home.verify_home_nav()
        self.home.verify_printer_model_name(self.local_printer_name)
        self.home.load_printer_selection()
        self.printers.select_remote_printer(REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_MFP_3303 if self.stack=="stage" else REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_3201)
        self.home.dismiss_print_anywhere_popup()
        self.home.verify_printer_model_name(REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_MFP_3303 if self.stack=="stage" else REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_3201, invisible=False)
        self.home.verify_printer_model_name(self.local_printer_name, invisible=True)
        if self.home.verify_unavailable_printer_status(raise_e=False):
            self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
            self.app_settings.click_sign_out_btn()
            self.smb.click_are_you_sure_sign_out_btn()
            self.home.verify_printer_model_name(self.local_printer_name, invisible=False)
        else:
            self.home.load_printer_info()
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.PRINTER_DISPLAY_LIGHTS, invisible=True)
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.TRAY_PAPER,invisible=True)
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.QUIET_MODE,invisible=True)
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.PRINT_QUALITY_TOOLS,invisible=True)
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.PRINT_FROM_OTHER_DEVICES,invisible=False)
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.PRINTER_INFO,invisible=False)
            self.fc.select_back()
            self.home.select_estimated_supply_levels()
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.PRINTER_DISPLAY_LIGHTS,invisible=True)
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.TRAY_PAPER, invisible=True)
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.QUIET_MODE, invisible=True)
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.PRINT_QUALITY_TOOLS, invisible=True)
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.PRINT_FROM_OTHER_DEVICES,invisible=False)
            self.printer_settings.verify_printer_report_by_name(self.printer_settings.PRINTER_INFO, invisible=False)
            self.fc.select_back()
            self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
            self.app_settings.click_sign_out_btn()
            self.smb.click_are_you_sure_sign_out_btn()
            self.home.verify_printer_model_name(self.local_printer_name, invisible=False)

    def test_02_verify_user_can_hide_printer_from_carousel(self):
        """
        Description:
        C30582471, C30582472, C30582447, C30582444
         1. Launch smart app with a smb account
         2. Click on Add Printer on Home screen
         3. Select any printer from the printer list
         4. Long press the printer
         5. Click on Hide Printer button

        Expected Result:
        4. Verify Hide this printer? popup with:
           - Hide this printer? title
           - Hide Printer button
           - Go to Dashboard button
           - Cancel button
        5. Printer is removed from Carousel
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.smb.verify_account_menu()
        self.smb.select_business_org_from_account(org_name="euthenia_hp" if self.stack=="stage" else "Zelus_HP")
        self.home.load_printer_selection()
        self.printers.select_remote_printer(REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_MFP_3303 if self.stack=="stage" else REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_3201)
        self.home.dismiss_print_anywhere_popup()
        self.home.long_press_printer()
        self.home.select_forget_this_printer(is_remote_printer=True)
        self.home.verify_printer_model_name(REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_MFP_3303 if self.stack=="stage" else REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_3201, invisible=True)

    def test_03_verify_printer_removed_from_carousel_when_switch_user_org(self):
        """
        Description:
        C30582472, C30582475, C30678399, C30582456, C30735983
         1. Launch smart app with a smb account
         2. Click on Add Printer on Home screen
         3. Select any printer from the printer list
         4. Click on Account button
         5. Click on My Printer option
         6. Click on Add Printer on Home screen
         7. Select a printer from the list
         8. Click on Account button
         9. Select a business org

        Expected Result:
        3. Verify the printer displays on carousel
         5. Verify the printer is removed from carousel
         7. Verify the printer displays on carousel
         9. Verify the printer from step7 is removed from carousel
        """
        self.fc.flow_load_home_screen(verify_signin=True)
        self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.smb.verify_account_menu()
        self.smb.select_business_org_from_account(org_name="euthenia_hp" if self.stack=="stage" else "Zelus_HP")
        self.home.load_printer_selection()
        self.printers.select_remote_printer(REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_MFP_3303 if self.stack=="stage" else REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_3201)
        self.home.dismiss_print_anywhere_popup()
        self.home.verify_printer_model_name(REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_MFP_3303 if self.stack=="stage" else REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_3201, invisible=False)
        self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.smb.select_my_printers()
        self.home.verify_printer_model_name(REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_MFP_3303 if self.stack=="stage" else REMOTE_PRINTER_NAME.HP_COLOR_LASERJET_PRO_3201, invisible=True)
        self.fc.flow_home_select_network_printer(self.p, is_searched=True)
        self.home.verify_printer_model_name(self.local_printer_name, invisible=False)
        self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.smb.verify_account_menu()
        self.smb.select_business_org_from_account(org_name="euthenia_hp" if self.stack=="stage" else "Zelus_HP")
        self.home.verify_printer_model_name(self.local_printer_name, invisible=True)