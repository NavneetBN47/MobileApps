from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from MobileApps.resources.const.android.const import *

pytest.app_info = "SMART"

class Test_Suite_01_Smb_Org_Picker_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.smb = cls.fc.flow[FLOW_NAMES.SMB]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.ows_value_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.notification = cls.fc.flow[FLOW_NAMES.NOTIFICATION]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]

        # Define variables
        cls.stack = request.config.getoption("--stack")
        cls.fc.set_hpid_account(None, smb=True)

    def test_01_smb_org_sign_out_function_from_app_settings(self):
        """
        Description:
        C30553459, C30553467, C30553469, C30727233, C30735952, C30735953, C30735954, C30735955, C31297236
         1. Launch smart app with HPID login
         2. click on App Settings, and login HPid
         3. Select My printer option from SMB Org Picker screen
         4. Click on Continue button
         5. CLick on Back button
         6. Click on Account button
         7. Click on Sign out button
         8. Click on Cancel button
         9. CLick on Account button
         10. Click on Sign Out button
         11. Click on SIGN OUT button

        Expected Result:
        2. Verify SMB Org picker screen
        4. Verify App Settings screen with HPID account information
        6. Verify Account button
        7. Verify Sign Out popup
        8. Verify Home screen
        11. Verify Home screen without HPID information
        """
        self.fc.flow_home_sign_in_hpid_account(create_acc=False)
        self.fc.select_back()
        self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.smb.verify_account_menu()
        self.app_settings.click_sign_out_btn()
        self.smb.are_you_sure_sign_out_popup()
        self.smb.click_cancel_btn()
        self.home.verify_home_nav()
        self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.app_settings.click_sign_out_btn()
        self.smb.click_are_you_sure_sign_out_btn()
        self.home.verify_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.home.verify_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN)
        self.home.verify_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        self.home.verify_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)

    @pytest.mark.parametrize("source_path", ["from_sign_in", "from_tile", "from_notification"])
    def test_02_smb_org_picker(self, source_path):
        """
        Description:
        C30553459, C30553458, C30553460, C30553462
         1. Load Home screen without HPID login
         2. If source_path == "from_sign_in", click on Sign In button, and login HPID
            If source_apth == "from_tile", click on Any time from Home screen, and Login HPID
            If source_apth == "from_notification", click on Notification icon, and Login HPID

        Expected Result:
         2. Verify Smb org picker UI screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        if source_path == "from_sign_in":
            self.home.select_bottom_nav_btn(self.home.NAV_SIGN_IN_BTN)
            self.__select_person_org()
            self.home.verify_home_nav()
        elif source_path == "from_tile":
            self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN))
            self.ows_value_prop.verify_ows_value_prop_screen(tile=True)
            self.ows_value_prop.select_value_prop_buttons(index=1)
            self.__select_person_org()
            self.home.check_run_time_permission()
            self.scan.verify_no_camera_access_screen()
        else:
            self.home.select_notifications_icon()
            self.notification.select_account()
            self.ows_value_prop.verify_ows_value_prop_screen(tile=True)
            self.ows_value_prop.select_value_prop_buttons(index=1)
            self.__select_person_org()

    def test_03_user_can_switch_between_personal_and_business_org(self):
        """
        Description:
        C31268722, C30553473, C30553478,  C30553457, C30553455, C30553464, C30553467, C30553469, C30727233, C30553474, C30582451
         1. Launch smart app, and click on Accept All button from welcome screen
         2. Click on Sign In button, and fill HPID information
         3. Select any person Org from SMB Org Picker screen
         4. Click on Continue button
         5. Click on Add First Printer button from Home screen
         6. Click on Account button on Home screen
         7. Click on any business org option
         8. Click on Add First Printer option

         Expected Results:
         5. Verify Printer List screen, and printer can be connected success
         8. Verify no printer on the local printer list
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.load_printer_selection()
        self.printers.select_printer_option_add_printer()
        self.printers.verify_printers_screen()
        self.fc.select_back()
        self.fc.select_back()
        self.home.verify_home_nav()
        self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.smb.verify_account_menu()
        self.smb.select_business_org_from_account(org_name="euthenia_hp" if self.stack=="stage" else "Zelus_HP")
        self.home.verify_home_nav()
        self.home.load_printer_selection()
        self.printers.verify_printers_screen()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __select_person_org(self, invisible=False, personal_org=True):
        """
        - CLick on Sign In button
        - Fill in HPID information
        - Verify SMB welcome back screen
        - Select person org from SMB welcome screen
        """
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.smb.verify_welcome_back_screen(invisible=invisible, timeout=20)
        if personal_org:
            self.smb.select_my_printers()
            self.smb.select_continue()