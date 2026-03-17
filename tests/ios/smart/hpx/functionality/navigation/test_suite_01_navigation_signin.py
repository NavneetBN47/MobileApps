import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Navigation_Signin(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.fc.hpx = True
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.notifications = cls.fc.fd["notifications"]
        cls.printers = cls.fc.fd["printers"]


    def test_01_verify_ui_mobilefax_C66290705(self):
        """
        Description : C66290705
        Install and launch the app.
        Accept consents
        sign in and navigate to rootview
        Tap on Bell icon on top bar
        Tap on Mobile fax option
        Observe
        
        Expected: Verify the Mobile Fax screen UI is as per figma. Verify the layout, icons, font, strings and buttons are as per the requirement.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.allow_notifications_popup(raise_e=False)
        self.home.select_notification_bell()
        self.notifications.select_mobile_fax_button()
        self.notifications.verify_hpx_mobilefax_sent_txt()
        self.notifications.verify_hpx_mobilefax_draft_txt()
        self.notifications.verify_hpx_fax_history_notification_screen_title()

    def test_02_verify_ui_supplies_signin(self):
        """
        Description : C41578713
        Install and launch the app.
        Accept consents
        sign in and navigate to rootview
        Tap on Bell icon on top bar
        Tap on Supplies option
        Observe

        Expected: Verify user is navigated to Supplies screen & existing functionality is working as expected.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.allow_notifications_popup(raise_e=False)
        self.home.select_notification_bell()
        self.notifications.select_supplies_button()
        self.notifications.verify_hpx_on_supplies_notification_screen_title()
        self.notifications.verify_hpx_on_supplies_page_close_btn()

    def test_03_verify_ui_shortcuts_signin_C66290697(self):
        """
        Description : C66290697
        Install and launch the app.
        Accept consents
        sign in and navigate to rootview
        Tap on Bell icon on top bar
        Tap on Shortcuts option
        Observe

        Expected: Verify user is navigated to Shortcuts screen & existing functionality is working as expected.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.allow_notifications_popup(raise_e=False)
        self.home.select_notification_bell()
        self.notifications.select_shortcuts_button()
        self.notifications.verify_hpx_notification_shortcuts_txt()

    def test_04_verify_ui_print_signin(self):
        """
        Description : C41578716
        Install and launch the app.
        Accept consents
        sign in and navigate to rootview
        Tap on Bell icon on top bar
        Tap on Print option
        Observe

        Expected: Verify user is navigated to Shortcuts screen & existing functionality is working as expected.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.allow_notifications_popup(raise_e=False)
        self.home.select_notification_bell()
        self.notifications.select_print_button()
        self.notifications.verify_hpx_on_printer_page()
        self.notifications.verify_hpx_on_printer_page_no_printer_selected()

    def test_05_verify_ui_bell_icon_close_btn(self):
        """
        Description : C42316421
        Install and launch the app.
        Accept consents
        Tap on Bell icon on top bar
        Tap on Close button
        Observe

        Expected: Verify user is navigated to Home screen & existing functionality is working as expected.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_notification_bell()
        self.notifications.hpx_notification_close_btn()
        self.home.verify_hpx_home()