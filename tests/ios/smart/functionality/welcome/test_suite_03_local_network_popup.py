import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import BUNDLE_ID
from MobileApps.resources.const.web.const import WEBVIEW_URL

pytest.app_info = "SMART"

class Test_Suite_03_Local_Network_Popup(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.printers = cls.fc.fd["printers"]
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.home = cls.fc.fd["home"]
        cls.ios_system = cls.fc.fd["ios_system"]
        cls.welcome = cls.fc.fd["welcome"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.privacy_preferences = cls.fc.fd["privacy_preferences"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def fresh_install(self, index=2):
        self.driver.reset(BUNDLE_ID.SMART)
        if self.stack != "pie":
            self.fc.change_stack(self.stack)
        self.ios_system.clear_safari_cache()
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.welcome.allow_notifications_popup(raise_e=False)
        self.driver.wait_for_context(WEBVIEW_URL.SMART_WELCOME(self.driver.driver_type), timeout=30)
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.click_accept_all_btn()
        if self.welcome_web.verify_permission_for_advertising_screen() is not False:
            self.welcome_web.click_continue_btn()
        self.ios_system.handle_allow_tracking_popup(raise_e=False)
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        if index == 2:
            self.ows_value_prop.verify_ows_value_prop_screen(timeout=60)
            self.ows_value_prop.select_value_prop_buttons(index=index)
        elif index == 1:
            self.fc.login_value_prop_screen(tile=False, timeout=60)
            self.home.allow_notifications_popup(timeout=15, raise_e=False)
            self.home.close_smart_task_awareness_popup()
            self.home.dismiss_tap_account_coachmark()

    def test_01_dont_allow_network(self):
        '''
        C28270924: local network popup message(don't allow)
        C28270932: restart app
        C28270926: don't enable get back
        '''
        self.fresh_install()
        self.ios_system.dismiss_hp_local_network_alert(allow=False, timeout=10)
        self.ios_system.verify_local_network_screen(timeout=30)
        self.ios_system.select_open_permissions()
        self.ios_system.verify_hp_smart_title()
        # do not enable and get back
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.ios_system.verify_local_network_screen()
        # do not enable and restart
        self.driver.restart_app(BUNDLE_ID.SMART)
        self.ios_system.verify_local_network_screen()

    def test_02_permit_local_network(self):
        '''
        C28270925: tapping enable permission
        '''
        self.fresh_install()
        self.dismiss_popup_and_enable_local_network()
        self.ios_system.switch_smart_app_local_network(on=True)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.home.verify_home()
        
    def test_03_permit_and_deny_add_printer_local_network(self):
        '''
        C28387081: "No Local Network" on Add Printer flow
        '''
        self.fresh_install(index=1)
        self.dismiss_popup_and_enable_local_network()
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.home.verify_home()
        self.home.select_settings_icon()
        self.ios_system.switch_smart_app_local_network(on=False)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.home.select_home_icon()
        self.home.select_add_your_first_printer()
        self.printers.select_open_permissions_button()
        self.ios_system.toggle_local_network_switch(on=True)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.printers.verify_choose_printer_screen_ui()

    def dismiss_popup_and_enable_local_network(self):
        self.ios_system.dismiss_hp_local_network_alert(allow=False, timeout=10)
        self.ios_system.verify_local_network_screen()
        self.ios_system.select_open_permissions()
        self.ios_system.verify_hp_smart_title()
        self.ios_system.toggle_local_network_switch(on=True)