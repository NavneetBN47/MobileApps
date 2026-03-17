import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_02_Bell_Notifications_SignIn(object):

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


    def test_01_verify_accessing_bell_rootview(self):
        """
        Description : C41580454
        Install and launch the app.
        Accept consents
        Sign in and navigate to rootview
        Tap on bell icon
        Observe

        Expected Result : User should be able to access the bell notifications screen
        """
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.verify_home(raise_e=False)
        self.home.verify_notification_bell()
        self.home.select_notification_bell()
        self.notifications.verify_hpx_notification_screen()

    def test_02_verify_accessing_bell_device_details_page(self):
        """
        Description : C41580455

        Install and launch the app.
        Accept consents
        Sign in and navigate to rootview
        Add a printer as devcie and go to device details screen.
        Tap on bell icon
        Observe

        Expected: User should be navigated to notifications screen
        
        """
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.verify_home(raise_e=False)
        self.home.click.hpx_add_printer_btn()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.verify_notification_bell()
        self.home.select_notification_bell()
        self.notifications.verify_hpx_notification_screen()

    def test_03_sign_in_from_top_bar(self):
        """
        Description : C44279845
        Install and launch the app.
        Accept consents
        Skip sign in and navigate to rootview
        Tap on "Sign in" on top navigation bar
        tap "x" or swipe back on sign page and Observe
        Expected: verify the user is directed back to Device detail page when sign in is cancelled.
        """
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.home.select_cancel()
        self.home.verify_hpx_home()