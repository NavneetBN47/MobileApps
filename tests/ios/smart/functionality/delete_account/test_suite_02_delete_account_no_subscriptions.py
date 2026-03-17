import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
import SPL.driver.driver_factory as p_driver_factory

pytest.app_info = "SMART"

class Test_Suite_02_Delete_Account_No_Subscriptions(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.stack = request.config.getoption("--stack")
        cls.sys_config = ma_misc.load_system_config_file()
        cls.db_info = cls.sys_config.get("database_info", None)
        cls.printer = p_driver_factory.get_printer(cls.sys_config["printer_power_config"], db_info=cls.db_info)
        cls.home = cls.fc.fd["home"]
        cls.settings = cls.fc.fd["app_settings"]
        cls.hp_connect = cls.fc.fd["hp_connect"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        if pytest.platform == "IOS":
            cls.safari = cls.fc.fd["safari"]
        else:
            cls.mac_browser_popup_flow = cls.fc.fd["mac_browser_popup_flow"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_home(self):
        self.fc.go_home(reset=True, stack=self.stack, create_account=True)

    def test_01_verify_delete_account_ui(self):
        """
        TESTRAIL: 
        C33416292: Verify Privacy Settings URLs (Delete Account) under Notifications and Privacy
        C31738107: Verify toast menu is not shown on Delete Account screen
        C31504378: End to End Flow
        C31504379: Both Users End to End flow
        C31504386: Redirected to home screen
        C31504394: "Delete account data" screen GUI and functionality
        """
        self.home.select_app_settings()
        self.settings.select_notification_n_privacy_option()
        self.settings.select_delete_account_option()
        self.hp_connect.verify_delete_hp_smart_account_screen()
        self.home.verify_toggle_menu(invisible=True, timeout=15)
        self.hp_connect.select_no_keep_account_btn(timeout=15)
        self.settings.select_delete_account_option()
        # TODO: Uncomment this section when defect https://hp-jira.external.hp.com/browse/SDASH-7090 is resolved
        # self.hp_connect.click_link_native("here_link")
        # self.hp_connect.verify_account_summary()
        # self.settings.select_close()
        self.hp_connect.verify_delete_hp_smart_account_screen()
        self.hp_connect.select_delete_account_btn()
        self.hp_connect.verify_hp_smart_account_has_been_deleted_title()
        if pytest.platform == "IOS":
            self.hp_connect.select_done_btn(delay=5)
            self.settings.verify_privacy_settings_screen()
        else:
            self.hp_connect.select_done_btn()
            self.home.verify_home()

    def test_02_delete_account_privacy_office(self):
        """
        TESTRAIL:
        C31504393: Verify Privacy Settings GUI
        C31504395: Account Deleted GUI
        """
        self.home.select_app_settings()
        self.settings.select_notification_n_privacy_option()
        self.settings.select_delete_account_option()
        self.hp_connect.verify_delete_hp_smart_account_screen()
        self.hp_connect.select_delete_account_btn()
        self.hp_connect.click_link_native("here_link")
        if pytest.platform == "IOS":
            self.safari.select_hp_privacy_office_accept_btn()
            self.safari.verify_hp_privacy_office_page(timeout=20)
        else:
            sleep(2)
            self.web_driver.update_window_table("main")
            self.web_driver.switch_window()
            sleep(2)
            self.mac_browser_popup_flow.verify_an_element_and_click("hp_privacy_office_title")
        self.__go_back_to_app()
        if pytest.platform == "IOS":
            self.hp_connect.select_done_btn(delay=5)
            self.settings.verify_privacy_settings_screen()
        else:
            self.hp_connect.select_done_btn()
            self.home.verify_home()

    def test_03_post_delete_account(self):
        """
        TESTRAIL:
        C31504385: Logged out post deletion
        C31504387: No shortcuts post deletion
        C31504389: local printer available
        C31504390: Can login with HPID post deletion
        C31504391: Cannot create new user with same HPID post deletion
        C31504392: Reconsent Process
        C31504397: Data Deleted and user is singed out
        C31504398: App does not react as a Grandfather user
        C35104399: User is only showed general messages that doesn't require consent
        """
        self.__add_printer_and_shortcut(is_first_time=False if pytest.platform == "IOS" else True)
        self.home.close_organize_documents_pop_up()
        self.home.select_app_settings()
        self.settings.select_notification_n_privacy_option()
        self.settings.select_delete_account_option()
        self.hp_connect.verify_delete_hp_smart_account_screen()
        self.hp_connect.select_delete_account_btn()
        self.hp_connect.verify_hp_smart_account_has_been_deleted_title()
        self.hp_connect.select_done_btn()
        if pytest.platform == "IOS":
            self.settings.verify_privacy_settings_screen()
            self.settings.verify_delete_account_option(invisible=True)
            self.settings.select_navigate_back()
            self.home.select_home_icon()
        self.home.verify_sign_in_icon()
        if pytest.platform == "IOS":
            self.home.scroll_to_carousel()
        self.home.verify_printer_added()
        self.home.select_tile_by_name(self.home.SHORTCUTS_BTN)
        self.fc.login_value_prop_screen(tile=True, webview=True if pytest.platform == "IOS" else False)
        # Uncomment the following two lines when defect https://hp-jira.external.hp.com/browse/AIOI-20339 is solved
        # self.shortcuts.dismiss_coachmark()
        # assert self.shortcuts.select_shortcut(shortcut_name="test_shortcut", click_obj=False, raise_e=False) == False
        self.__add_shortcut(navigate_to_shortcuts=False, shortcuts_name="test_shortcuts2")
        self.home.select_app_settings()
        self.settings.sign_out_from_hpc()
        if pytest.platform == "MAC":
            self.home.select_app_settings()
        self.settings.select_create_account_btn(delay=5)
        self.__verify_unable_to_create_account(email=self.driver.session_data["hpid_user"], password=self.driver.session_data["hpid_pass"])

    def __go_back_to_app(self):
        self.driver.activate_app(i_const.BUNDLE_ID.SMART)
    
    def __add_printer_and_shortcut(self, is_first_time=False):
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(printer_ip=self.printer.get_printer_information()["ip address"])
        self.__add_shortcut(navigate_to_shortcuts=True, is_first_time=is_first_time)
    
    def __add_shortcut(self, navigate_to_shortcuts=True, shortcuts_name="test_shortcut", is_first_time=False):
        if navigate_to_shortcuts:
            self.fc.navigate_to_add_shortcuts_screen()
        else:
            self.shortcuts.verify_shortcuts_screen(timeout=35)
            self.shortcuts.click_add_shortcut()
            self.shortcuts.verify_add_shortcuts_screen()
            self.shortcuts.click_create_your_own_shortcut_btn()
            self.shortcuts.verify_add_your_own_shortcut_screen()
        self.shortcuts.click_email_btn()
        self.shortcuts.verify_add_email_screen()
        self.shortcuts.enter_email_receiver(self.driver.session_data["hpid_user"])
        self.fc.save_shortcut(shortcuts_name=shortcuts_name, invisible=False, is_first_time=is_first_time)
        if self.home.verify_close(raise_e=False) and pytest.platform == "IOS":
            self.home.select_close()
    
    def __verify_unable_to_create_account(self, email, password):
        if pytest.platform == "MAC":
            self.fc.switch_window_and_modify_wn("hpid", "web_login")
        self.hpid.verify_unable_to_create_account(email=email, password=password)
        if pytest.platform == "MAC":
            self.web_driver.close_window("web_login")
            self.web_driver.switch_window()
            self.__go_back_to_app()