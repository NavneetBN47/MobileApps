import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Top_Bar_Notifications:

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
        cls.printers = cls.fc.fd["printers"]
        cls.notification = cls.fc.fd["notifications"]

    def test_01_verify_sign_in_from_top_bar_C66253853(self):
        """
        Description: C66253853
        Install and launch the app.
        Accept consents
        Skip sign in and navigate to rootview
        Tap on "Sign in" on top navigation bar
        Expected Result:
        Verify the user is directed to sign in page and is able to sign in successfully. After sign in, user will be returned to root view.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.verify_home(raise_e=False)


    def test_02_verify_sign_in_device_details_C66253858(self):
        """
        C66253858
        Install and launch the app.
        Accept consents
        Skip sign in and navigate to rootview
        Tap on any printer and navigate to device details page
        Tap on "Sign in" on top navigation bar
        Expected Result:
        Verify the user is directed to sign in page and is able to sign in successfully. After sign in, user will be returned to device details page
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_hpx_add_printer_btn()
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.home.click_sign_btn_hpx()
        assert self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.verify_home(raise_e=False)

    def test_03_verify_sign_in_Unsuccessful_sign_in(self):
        """
        C53558057
        Install and launch the app.
        Accept consents
        Skip sign in and navigate to rootview
        Tap on "Sign in" on top navigation bar
        Tap cancel on sign in page or create error by disconnecting n/w and then tap cancel
        Observe
        Expected Result:Verify after cancelling the sign in, user is brought back to root. User can then tap Sign in again and sign in successfully
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        self.hpid.verify_hp_id_sign_in()
        self.driver.back()
        self.home.verify_home(raise_e=False)
        self.home.click_sign_btn_hpx()
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login()
        self.home.verify_home(raise_e=False)


    def test_04_verify_sign_in_from_bell_mobile_fax_C66253855(self):
        """
        C66253855
        Install and launch the app.
        Accept consents
        Skip sign in and navigate to rootview
        Tap on Bell icon on top bar
        Tap on Mobile fax option
        Observe
        
        Expected Result: verify user is navigated to a value prop page related to Mobile Fax. This value prop has three options Create Account, Sign In and Close.
        
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_notification_bell()
        self.notification.select_mobile_fax_button()
        self.notification.verify_hpx_notification_mobile_fax_txt()
        self.home.verify_create_account_icon()
        self.home.verify_sign_in_icon()

    def test_05_verify_sign_in_from_bell_shortcuts_C66253856(self):
        """
        C66253856
        Install and launch the app.
        Accept consents
        Skip sign in and navigate to rootview
        Tap on Bell icon on top bar
        Tap on Shortcuts option
        Observe
        Expected Result: verify user is navigated to a value prop page related to Shortcuts. This value prop has three options Create Account, Sign In and Close.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_notification_bell()
        self.notification.select_shortcuts_button()
        self.notification.verify_hpx_notification_shortcuts_txt()
        self.home.verify_create_account_icon()
        self.home.verify_sign_in_icon()


    def test_06_verify_sign_in_from_bell_supplies_C66253857(self):
        """
        C66253857
        Install and launch the app.
        Accept consents
        Skip sign in and navigate to rootview
        Tap on Bell icon on top bar
        Tap on Supplies option
        Observe
        Expected Result: verify user is navigated to a value prop page related to Supplies. This value prop has three options Create Account, Sign In and Close.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_notification_bell()
        self.notification.select_supplies_button()
        self.notification.verify_hpx_notification_supplies_txt()
        self.home.verify_create_account_icon()
        self.home.verify_sign_in_icon()

    def test_07_verify_sign_in_from_bell_account_C66253860(self):
        """
        C66253860
        Install and launch the app.
        Accept consents
        Skip sign in and navigate to rootview
        Tap on Bell icon on top bar
        Tap on Account option
        Observe
        Expected Result: verify user is navigated to a value prop page related to Account. This value prop has three options Create Account, Sign In and Close.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_notification_bell()
        self.notification.select_account_button()
        self.notification.verify_hpx_notification_account_txt()
        self.home.verify_create_account_icon()
        self.home.verify_sign_in_icon()

    def test_08_verify_unsuccessfull_Sign_in_from_bell(self):
        """
        C53558055
        Install and launch the app.
        Accept consents
        Skip sign in and navigate to rootview
        Tap on Bell icon on top bar
        Tap on Mobile fax
        Tap Sign in or create account to invoke HPID flow
        Tap cancel on HPID screen to cancel the sign in flow
        Expected Result: Verify user is back to the bell notification screen.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.select_notification_bell()
        self.notification.select_mobile_fax_button()
        self.home.click_sign_in_icon()
        self.hpid.verify_hp_id_sign_in()
        self.driver.back()
        self.notification.verify_hpx_notification_mobile_fax_txt()
        self.driver.back()
        self.notification.verify_hpx_notification_screen()