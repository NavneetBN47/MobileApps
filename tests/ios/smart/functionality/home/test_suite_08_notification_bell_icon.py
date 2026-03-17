import pytest
import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import HOME_TILES
from MobileApps.resources.const.ios import const as i_const
pytest.app_info = "SMART"

class Test_Suite_08_Notification_Bell_Icon(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.notification = cls.fc.fd["notifications"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.fax_history = cls.fc.fd["softfax_fax_history"]
        cls.shortcuts_notification = cls.fc.fd["shortcuts_notification"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.scan = cls.fc.fd["scan"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.softfax_offer = cls.fc.fd["softfax_offer"]
    
    def test_01_verify_bell_icon_without_hpid_login(self):
        """
        IOS & MAC:
        C31297136, C31297155
        Description:
          1. Load to Home screen without HPID login
          2. Click on Notification bell icon
          3. Click on Account button
          4. Click on Close button
          5. Click on Mobile Fax button

        Expected Result:
          3. Verify HPID login screen
          4. Verify Notification screen
          5. Verify HPID login screen

        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_notification_bell()
        self.notification.verify_notifications_screen()
        self.notification.select_close()
        self.home.verify_home()
        self.home.select_notification_bell()
        self.notification.verify_notifications_screen()
        self.notification.select_account_button()
        if pytest.platform == "IOS":
            self.ows_value_prop.select_value_prop_buttons(index=1)
        else:
            self.ows_value_prop.select_native_value_prop_buttons(1)
            self.fc.switch_window_and_modify_wn("hpid", "web_login")
        self.hpid.verify_hp_id_sign_in()
        if pytest.platform == "IOS":
            self.home.select_cancel()
        else:
            self.fc.delete_window_and_activate_hp_smart("web_login", close_window=True)
        self.notification.verify_notifications_screen()
        self.notification.select_mobile_fax_button()
        if pytest.platform == "IOS":
            self.ows_value_prop.select_value_prop_buttons(index=1)
        else:
            self.ows_value_prop.select_native_value_prop_buttons(1)
            self.fc.switch_window_and_modify_wn("hpid", "web_login")
        self.hpid.verify_hp_id_sign_in()
        if pytest.platform == "MAC":
            self.fc.delete_window_and_activate_hp_smart("web_login", close_window=True)        

    def test_02_verify_mobile_fax_screen_without_sign_in(self):
        """
        IOS & MAC:
        C31297150
        Description:
          1. Tap on Notification bell icon from the Home page to go to Notification page
          2. Tap on "Mobile Fax" option.
          3. Click on Get Started and Verify the users is prompted to enter the Username and password.
          4. Enter the Username and click Next
          5. Enter the Password and click Next
          6. Verify the user is taken to "Welcome to Mobile Fax" screen.
        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_notification_bell()
        self.notification.verify_notifications_screen()
        self.notification.select_mobile_fax_button()
        if pytest.platform == "IOS":
            self.fc.login_value_prop_screen()
        else:
            self.fc.login_value_prop_screen(webview=False)
        self.fax_history.verify_fax_history_screen(timeout=20)
    
    def test_03_verify_notification_shortcuts_list(self):
        """
        IOS & MAC:
        C31297137, C31297138, C31297139, C31297140, C31297142, C31297145,
        C33610701, C33611220, C33611222, C33611224
        Description:
          1. Create a new account and go to home screen
          2. Click on Notification bell icon
          3. Click on Notification shortcuts list
          4. Create shortcut

        Expected Result:
          1. Verify "No Smart task activity available" message
          2. Verify the shortcut in the list (Status, Name, Date)
          3. Verify Back button on the shortcut screen redirects the user to the notification screen
        """
        shortcuts_name = self.test_03_verify_notification_shortcuts_list.__name__
        self.fc.go_home(reset=True, stack=self.stack, create_account=True)
        self.home.select_notification_bell()
        self.notification.verify_notifications_screen()
        self.notification.select_shortcuts_button()
        self.shortcuts_notification.verify_no_shortcut_activity_available_msg()
        self.shortcuts_notification.navigate_back()
        if pytest.platform == "IOS":
            self.notification.verify_notifications_screen()
            self.notification.select_close()
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_email_btn()
        self.shortcuts.verify_add_email_screen()
        self.shortcuts.enter_email_receiver(self.driver.session_data["hpid_user"])
        self.fc.save_shortcut(shortcuts_name=shortcuts_name, invisible=False, is_first_time=True)
        if self.home.verify_close(raise_e=False) and pytest.platform == "IOS":
            self.home.select_close()
        self.home.select_rootbar_view_and_print_icon()
        self.fc.select_photo_from_photo_picker(select_all_files=False)
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHORTCUTS_BTN)
        if pytest.platform == "MAC":
          self.common_preview.expand_shortcuts_pan_view_btn()
        self.common_preview.verify_an_element_and_click("single_shortcut_task", format_specifier=[shortcuts_name])
        self.common_preview.select_activity_center_button_on_popup()
        self.notification.verify_notifications_screen()
        self.notification.select_shortcuts_button()
        self.shortcuts_notification.verify_shortcuts_list_from_notification()
        self.__wait_until_shortcut_ready(1)
        self.shortcuts_notification.verify_job_status_date_and_name_by_number(1, "Shortcut Completed", shortcuts_name, "Today")
        self.shortcuts_notification.select_job_by_number(1)
        self.shortcuts_notification.verify_shortcut_complete_screen()
        self.shortcuts_notification.select_email_completed_item()
        self.shortcuts_notification.verify_email_sent_screen()
        self.shortcuts_notification.navigate_back()
        self.shortcuts_notification.navigate_back()
        self.shortcuts_notification.navigate_back()
        if pytest.platform == "IOS":
            self.notification.select_close()
        self.home.verify_home()
        self.home.select_notification_bell()
        self.notification.verify_notifications_screen()
        self.notification.select_shortcuts_button()
        self.shortcuts_notification.select_job_by_number(1)
        self.shortcuts_notification.select_delete_button()
        self.shortcuts_notification.verify_no_shortcut_activity_available_msg()
    
    @pytest.mark.parametrize("print_mode",["color", "greyscale"])
    def test_04_smart_task_for_print(self, print_mode):
        """
        IOS & MAC:
        C31297143, C31297144
        Description:
          1. Create and execute Shortcuts for Print in Greyscale/color mode
          2. Tap on Notification bell icon
          3. Tap on 'Shortcuts' available under "Notifications"
          4. Click on the Shortcuts created for Print
          5. Click on 'Print' with green arrow.
        
        Expected Result:
          4. Verify the Shortcut Completed screen
          5. Verify the print screen
        """
        color_option = {
            "color": self.shortcuts.COLOR_BTN,
            "greyscale": self.shortcuts.GRAYSCALE_BTN
        }
        shortcuts_name = f"{self.test_04_smart_task_for_print.__name__}_{print_mode}"
        self.fc.go_home(reset=True, stack=self.stack, create_account=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.navigate_to_add_shortcuts_screen()
        self.shortcuts.click_print_btn()
        self.shortcuts.select_color(color_btn=color_option[print_mode])
        self.fc.save_shortcut(shortcuts_name, invisible=True, is_first_time=True)
        self.home.close_organize_documents_pop_up()
        self.home.select_rootbar_view_and_print_icon()
        self.fc.select_photo_from_photo_picker(select_all_files=False)
        self.common_preview.select_print_size(raise_e=False)
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHORTCUTS_BTN)
        if pytest.platform == "MAC":
            self.common_preview.expand_shortcuts_pan_view_btn()
        self.common_preview.verify_an_element_and_click("single_shortcut_task", format_specifier=[shortcuts_name])
        self.common_preview.dismiss_print_preview_coachmark()
        self.common_preview.dismiss_feedback_popup()
        self.common_preview.select_finish_shortcut_btn()
        self.common_preview.select_activity_center_button_on_popup()
        self.notification.verify_notifications_screen()
        self.notification.select_shortcuts_button()
        self.shortcuts_notification.verify_shortcuts_list_from_notification()
        self.__wait_until_shortcut_ready(1)
        self.shortcuts_notification.verify_job_status_date_and_name_by_number(1, "Shortcut Completed", shortcuts_name, "Today")
        self.shortcuts_notification.select_job_by_number(1)
        self.shortcuts_notification.verify_shortcut_complete_screen()
    
    def test_05_verify_no_print_activity(self):
        """
        IOS & MAC:
        C33626425
        Description:
          1. Load to Home screen with HPID login
          2. Click on Notification bell icon
          3. Click on Settings button
          4. Click on Back button
          5. Click on Print button
          6. Add a printer to printer carousel on Home screen
          7. Click on Notification bell icon
          8. Click on Print button

        Expected Result:
          2. Verify Notifications screen
          3. Verify notification settings screen
          4. Verify Notification screen
          5. Verify No Printer Selected screen
          8. Verify No print activity available screen
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.home.select_notification_bell()
        self.notification.verify_notifications_screen()
        self.notification.select_settings_icon()
        self.app_settings.verify_notifications_settings_screen()
        self.app_settings.select_navigate_back()
        self.notification.verify_notifications_screen()
        self.notification.select_print_button()
        self.notification.verify_no_printer_selected_screen()
        self.notification.select_navigate_back()
        self.notification.select_close()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_notification_bell()
        self.notification.verify_notifications_screen()
        self.notification.select_print_button()
        self.notification.verify_no_print_activity_available_screen()
    
    def test_06_verify_user_taps_mobile_fax_under_activity(self):
        """
        IOS & MAC:
        C31297152, C31297153
        Description:
          1. Load to Home screen with HPID login
          2. CLick on Notification bell icon
          3. Click on Mobile Fax button

        Expected Result:
          4. Verify Softfax History screen
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.home.select_notification_bell()
        self.notification.verify_notifications_screen()
        self.notification.select_mobile_fax_button()
        assert self.fax_history.verify_fax_history_screen(timeout=20, raise_e=False) or\
            self.softfax_offer.verify_get_started_screen(timeout=30, raise_e=False)

    @pytest.mark.parametrize("button",["account", "supplies"])
    def test_07_verify_tapping_on_accounts_n_supplies_btn_hp_plus(self, button):
        """
        IOS & MAC:
        C33626429, C33626430
        Description:
          1. Load to Home screen with hp+ account login
          2. Click on Notification bell icon
          3. If button==account, then click on Account button
             If button==supplies, then click on Supplies button

        Expected Result:
          3. Verify View Notification screen
        """
        login_info = ma_misc.get_hpid_account_info(stack=self.stack, a_type="hp+", instant_ink=True)
        username, password = login_info["email"], login_info["password"]
        self.fc.go_home(reset=True, button_index=1, username=username, password=password, stack=self.stack, remove_default_printer=False)
        self.home.select_notification_bell()
        self.notification.verify_notifications_screen()
        if button == "account":
            self.notification.select_account_button()
        else:
            self.notification.select_supplies_button()
        self.home.verify_an_element_and_click(self.home.VIEW_NOTIFICATIONS_TITLE, click=False)

    def test_08_notification_print_screen(self):
        """
        IOS & MAC:
        C33626426 - Verify the Print screen UI after some printing is done.
        C33626427 - Verify the Job printed screen after tapping on right arrow on Print screen.
        C33626428 - Verify the behavior of Clear Notification button on Job Printed screen.

        Description:
          - Launch the app.
          - Go through all the consents and navigate to Home screen.
          - Print am image/document through Print Photos/Print Document tiles.
          - Tap on Bell icon on top left of Home screen.
          - Tap on Print on Notifications screen.
          - Tap on right arrow on top right of Print screen.
          - Tap on Clear Notification button.
          - Tap on back arrow on Print screen.
        
        Expected Result:
          - Verify the user is taken back to Print screen showing no Print activity available.
          - Verify there is no red dot showing next to Print button on Notifications screen.
        """
        self.fc.go_home(reset=True, stack=self.stack, create_account=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.dismiss_tap_account_coachmark()
        self.home.select_rootbar_view_and_print_icon()
        self.fc.select_photo_from_photo_picker(select_all_files=False)
        self.common_preview.select_print_size(raise_e=False)
        self.common_preview.verify_preview_screen()
        self.common_preview.select_bottom_nav_btn(self.common_preview.PRINT_BTN)
        self.fc.select_print_button_and_verify_print_job(self.p)
        self.common_preview.select_done()
        self.home.close_organize_documents_pop_up()
        if pytest.platform == "MAC":
            self.home.verify_home()
        self.home.select_notification_bell()
        self.notification.verify_notifications_screen()
        self.notification.select_print_button()
        self.__wait_until_job_printed(timeout=30)
        self.notification.verify_job_completed_on_print_screen(timeout=30)
        job_name = self.notification.get_printed_file_name()
        self.notification.select_print_job_by_number()
        self.notification.verify_job_printed_screen()
        self.notification.verify_job_printed_screen_date_and_job_name(job_name)
        self.notification.select_clear_notification_btn()
        self.notification.verify_no_print_activity_available_screen()

    def __wait_until_shortcut_ready(self, shortcut_number, job_status="Shortcut Completed", timeout=30):
        """
        Wait until the shortcut status is completed
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.shortcuts_notification.verify_job_status(shortcut_number, job_status, raise_e=False):
                return True
            else:
                self.shortcuts_notification.navigate_back()
                self.notification.verify_notifications_screen()
                time.sleep(5)
                self.notification.select_shortcuts_button()
        raise TimeoutError("Shortcut is not ready after 30s")
    
    def __wait_until_job_printed(self, timeout):
        """
        Wait until the job is printed
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.notification.verify_completed_status_on_print_screen(timeout=10, raise_e=False):
                return True
            else:
                self.notification.select_navigate_back()
                time.sleep(5)
                self.notification.select_print_button()
        raise TimeoutError("Job is not printed after 30s")