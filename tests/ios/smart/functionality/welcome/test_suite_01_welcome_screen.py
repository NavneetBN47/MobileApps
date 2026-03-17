import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.web.smart.smart_welcome import SmartWelcome
from MobileApps.resources.const.ios.const import BUNDLE_ID
from MobileApps.resources.const.web.const import WEBVIEW_URL

pytest.app_info = "SMART"

class Test_Suite_01_Ios_Smart_Welcome_Screen(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.ios_system = cls.fc.fd["ios_system"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.printers = cls.fc.fd["printers"]
        cls.welcome = cls.fc.fd["welcome"]

    @pytest.fixture(scope="function", autouse="true")
    def fresh_install(self):
        self.driver.reset(BUNDLE_ID.SMART)
        if self.stack != "pie":
            self.fc.change_stack(self.stack)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.driver.wait_for_context(WEBVIEW_URL.SMART_WELCOME(self.driver.driver_type), timeout=30)

    def test_01_verify_terms_and_conditions_screen(self):
        """
        C27796362 Precondition: fresh install
        """
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.verify_click_btn()
        self.welcome_web.verify_hp_privacy_statement_link()
        self.welcome_web.verify_terms_of_use_link()
        self.welcome_web.verify_eula_link()

    @pytest.mark.parametrize('allow', [True, False])
    def test_02_setup_new_printer(self, allow):
        """
        IOS & MAC:
        C27803200, C31298114 - Behavior by tapping "Set Up Printer" button on Value Prop screen
        C28496244 - Behavior by tapping "Set Up Printer" button on Value Prop screen > no local network
        """
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.click_accept_all_btn()
        if pytest.platform == "IOS":
            if self.welcome_web.verify_permission_for_advertising_screen() is not False:
                self.welcome_web.click_continue_btn()
            self.ios_system.handle_allow_tracking_popup(option=True, raise_e=False)
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.ows_value_prop.verify_ows_value_prop_screen(timeout=60)
        self.ows_value_prop.select_value_prop_buttons(0)
        if self.printers.verify_bluetooth_popup(raise_e=False):
            self.printers.handle_bluetooth_popup()
        self.ios_system.dismiss_hp_local_network_alert(allow=allow)
        if allow is True:
            self.printers.verify_choose_type_of_printer_screen()
            self.printers.select_get_started_button()
            if self.printers.verify_printer_not_listed_btn():
                self.printers.select_printer_not_listed_btn()
            self.printers.verify_set_up_printer_screen()
            self.printers.set_up_printer()
            self.printers.select_continue()
            if self.printers.verify_bluetooth_popup(raise_e=False):
                self.printers.handle_bluetooth_popup()
            self.printers.verify_printers_list()
        else:
            self.printers.verify_enable_local_network_permission_blocker_screen()

    @pytest.mark.parametrize('link', [SmartWelcome.TERM_USE_LINK, 
            SmartWelcome.EULA_LINK, SmartWelcome.HP_PRIVACY_STATEMENT])
    def test_04_hyperlinks(self, link):
        '''
            C27894024: Verify "HP Smart Terms of Use" hyperlink redirection
            C27894025: Verify "End User License Agreement" hyperlink redirection
        '''
        self.welcome_web.verify_welcome_screen()
        if link == SmartWelcome.EULA_LINK:
            self.welcome_web.click_manage_options()
        self.welcome_web.click_link_native(link)
        sleep(2)
        assert self.driver.wdvr.query_app_state(BUNDLE_ID.SAFARI) == 4