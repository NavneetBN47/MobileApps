import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import HOME_TILES

pytest.app_info = "SMART"

class Test_Suite_01_Smb_Org_Picker_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()

        # Define the flows
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.camera = cls.fc.fd["camera"]
        cls.smb = cls.fc.fd["smb"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.scan = cls.fc.fd["scan"]
        cls.printers = cls.fc.fd["printers"]

        # Define variables
        cls.printer_info = cls.p.get_printer_information()
        cls.stack = request.config.getoption("--stack")
        login_info = ma_misc.get_smb_account_info(cls.stack)
        cls.username, cls.password = login_info["email"], login_info["password"]

    def test_01_smb_org_sign_out_function_from_app_settings(self):
        """
        Description:
        C30553459, C30553467, C30553469, C30727233
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
        self.fc.go_home(stack=self.stack, button_index=2)
        self.fc.go_to_home_screen()
        self.home.select_app_settings()
        self.app_settings.select_sign_in_option()
        self.driver.wait_for_context(self.fc.hpid_url, timeout=30)
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login(self.username, self.password)
        if self.smb.select_my_printers(raise_e=False):
            self.smb.select_continue()
        self.app_settings.verify_successfull_sign_in_screen(timeout=25)
        self.home.select_home_icon()
        self.home.allow_notifications_popup(timeout=10, raise_e=False)
        self.home.dismiss_tap_account_coachmark()
        self.home.select_account_icon()
        self.smb.verify_account_menu()
        self.smb.click_sign_out_btn()
        self.smb.are_you_sure_sign_out_popup(displayed=False)
        self.smb.click_cancel_btn()
        self.smb.verify_account_menu()
        self.smb.click_sign_out_btn()
        self.smb.click_are_you_sure_sign_out_btn()
        self.home.verify_sign_in_icon()

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
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.go_to_home_screen()
        if source_path == "from_sign_in":
            self.home.select_sign_in_icon()
            self.__select_person_org(self.username, self.password, invisible=False, personal_org=True)
            self.home.allow_notifications_popup(timeout=30, raise_e=False)
            self.home.dismiss_tap_account_coachmark()
            self.home.verify_rootbar_scan_icon(invisible=False)
        elif source_path == "from_tile":
            self.home.select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
            self.ows_value_prop.verify_ows_value_prop_screen(tile=True, timeout=15)
            self.ows_value_prop.select_value_prop_buttons(index=1)
            self.__select_person_org(self.username, self.password, invisible=False, personal_org=True)
            self.camera.select_allow_access_to_camera_on_popup()
            if self.camera.verify_second_close_btn():
                self.camera.select_second_close_btn()
            self.camera.verify_camera_screen()
        else:
            self.home.select_notification_bell()
            self.home.verify_an_element_and_click(self.home.ACCOUNT_BTN)
            self.ows_value_prop.select_value_prop_buttons(index=1)
            self.__select_person_org(self.username, self.password, invisible=False, personal_org=True)

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
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.go_to_home_screen()
        self.home.select_get_started_by_adding_a_printer()
        self.printers.select_add_printer()
        self.printers.select_add_printer_using_ip()
        self.printers.verify_connect_the_printer_screen()
        self.printers.search_for_printer_directly_using_ip(self.printer_info["ip address"])
        self.printers.select_is_this_your_printer(yes=True)
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()
        self.home.select_account_icon()
        self.smb.verify_account_menu()
        self.smb.select_business_org_from_account(org_name="SMB_testing")
        self.home.verify_home()
        self.home.verify_printer_on_home_screen(invisible=True)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __select_person_org(self, username, password, invisible=False, personal_org=True):
        """
        - CLick on Sign In button
        - Fill in HPID information
        - Verify SMB welcome back screen
        - Select person org from SMB welcome screen
        """
        self.driver.wait_for_context(self.fc.hpid_url, timeout=30)
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login(username, password)
        self.smb.verify_welcome_back_screen(invisible=invisible, timeout=20)
        if personal_org:
            self.smb.select_my_printers()
            self.smb.select_continue()