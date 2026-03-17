import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings
from MobileApps.resources.const.ios.const import REMOTE_PRINTER_NAME

pytest.app_info = "SMART"

class Test_Suite_02_Smb_Carousal(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()

        # Define the flows
        cls.home = cls.fc.fd["home"]
        cls.smb = cls.fc.fd["smb"]
        cls.printers = cls.fc.fd["printers"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        # Define variables
        cls.stack = request.config.getoption("--stack")
        cls.printer_info = cls.p.get_printer_information()
        login_info = ma_misc.get_smb_account_info(cls.stack)
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.local_printer_name = cls.p.get_printer_information()["bonjour name"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_home(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=1, username=self.username, password=self.password)

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
           - Print from Other device item
           - Print anywhere item
           - Select another printer item
        11.Verify Printer Settings page with below option:
           - Print from Other device item
           - Print anywhere item
           - Select another printer item
        14.Verify the printer from Step 5 displays
        """
        self.home.select_get_started_by_adding_a_printer()
        self.printers.select_add_printer()
        self.printers.select_add_printer_using_ip()
        self.printers.verify_connect_the_printer_screen()
        self.printers.search_for_printer_directly_using_ip(self.printer_info["ip address"])
        self.printers.select_is_this_your_printer(yes=True)
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()
        printer_name = self.home.get_printer_name_from_device_carousel()
        shortened_bonjour_name = ma_misc.truncate_printer_model_name(self.local_printer_name, case_sensitive=False)
        assert printer_name == self.local_printer_name or \
               all(word in printer_name.lower().split() for word in shortened_bonjour_name.split())
        self.__select_remote_printer_from_business_org(is_remote_printer=True)
        remote_printer_name = self.home.get_printer_name_from_device_carousel()
        assert (printer_name != remote_printer_name), "Remote printer should be displayed instead of Local printer"
        self.home.click_on_printer_icon()
        self.printer_settings.verify_ui_option_displayed(PrinterSettings.PS_PRINT_FROM_OTHER_DEVICES)
        self.printer_settings.verify_ui_option_displayed(PrinterSettings.PS_PRINT_ANYWHERE)
        self.printer_settings.verify_ui_option_displayed(PrinterSettings.PS_SELECT_A_DIFFERENT_PRINTER)
        self.printer_settings.verify_ui_option_displayed(PrinterSettings.PS_QUIET_MODE, invisible=True)
        self.printer_settings.select_navigate_back()
        self.home.close_print_anywhere_pop_up()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()
        self.home.select_estimated_supply_levels()
        self.printer_settings.verify_ui_option_displayed(PrinterSettings.PS_PRINT_FROM_OTHER_DEVICES)
        self.printer_settings.verify_ui_option_displayed(PrinterSettings.PS_PRINT_ANYWHERE)
        self.printer_settings.verify_ui_option_displayed(PrinterSettings.PS_SELECT_A_DIFFERENT_PRINTER)
        self.printer_settings.verify_ui_option_displayed(PrinterSettings.PS_QUIET_MODE, invisible=True)
        self.printer_settings.select_navigate_back()
        self.home.verify_home()
        self.home.select_account_icon()
        self.smb.click_sign_out_btn()
        self.smb.click_are_you_sure_sign_out_btn()
        self.home.verify_home()
        new_printer_name = self.home.get_printer_name_from_device_carousel()
        assert (new_printer_name != remote_printer_name), "Remote printer should not be displayed"

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
        self.__select_remote_printer_from_business_org(is_remote_printer=True, is_available=False)
        self.home.verify_printer_dropdown_options()
        self.home.select_hide_printer_from_menu()
        self.home.verify_hide_printer_popup()
        self.home.select_hide_printer_confirmation_btn()
        self.home.verify_add_printer_on_carousel()
        self.home.verify_printer_on_home_screen(invisible=True)

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
        self.__select_remote_printer_from_business_org(is_remote_printer=True, is_available=False)
        remote_printer_name = self.home.get_printer_name_from_device_carousel()
        assert (remote_printer_name != self.local_printer_name), "Remote printer should be displayed instead of Local printer"
        self.home.select_account_icon()
        self.smb.select_my_printers()
        self.home.verify_home()
        self.home.select_get_started_by_adding_a_printer()
        self.printers.select_add_printer()
        self.printers.select_add_printer_using_ip()
        self.printers.verify_connect_the_printer_screen()
        self.printers.search_for_printer_directly_using_ip(self.printer_info["ip address"])
        self.printers.select_is_this_your_printer(yes=True)
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()
        new_printer_name = self.home.get_printer_name_from_device_carousel()
        assert (new_printer_name != remote_printer_name), "Remote printer should be disappeared"
        self.__select_remote_printer_from_business_org()
        new_printer_name = self.home.get_printer_name_from_device_carousel()
        assert (new_printer_name == remote_printer_name), "Remote printer should be displayed"

    def __select_remote_printer_from_business_org(self, is_remote_printer=False, is_available=True):
        """
        Select smbtesting org from Account menu
        """
        self.home.select_account_icon()
        self.smb.verify_account_menu()
        self.smb.select_business_org_from_account(org_name="SMB_testing")
        self.home.close_print_anywhere_pop_up()
        self.home.verify_home()
        if is_remote_printer:
            self.home.select_get_started_by_adding_a_printer()
            if is_available:
                printers_count = len(self.printers.get_printers())
                for index in range(printers_count):
                    if not self.printers.verify_printers_nav(timeout=3, raise_e=False):
                        self.home.select_get_started_by_adding_a_printer()
                    self.printers.select_printer_by_index(index)
                    self.home.close_smart_task_awareness_popup()
                    self.home.close_use_bluetooth_pop_up()
                    self.home.close_print_anywhere_pop_up()
                    self.home.close_organize_documents_pop_up()
                    self.home.verify_home()
                    if not self.home.verify_is_printer_unavailable(self.home.get_printer_name_from_device_carousel(), raise_e=False):
                        break
                    self.home.verify_printer_dropdown_options()
                    self.home.select_hide_printer_from_menu()
                    self.home.verify_hide_printer_popup()
                    self.home.select_hide_printer_confirmation_btn()
                assert not self.home.verify_is_printer_unavailable(self.home.get_printer_name_from_device_carousel(), raise_e=False), "All printers were unavailable"
            else:
                self.printers.select_printer_by_index()
                self.home.close_smart_task_awareness_popup()
                self.home.close_use_bluetooth_pop_up()
                self.home.close_print_anywhere_pop_up()
                self.home.close_organize_documents_pop_up()
                self.home.verify_home()

