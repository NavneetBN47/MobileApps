import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_05_Welcome_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.welcome = cls.fc.fd["welcome_web"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]
        cls.home = cls.fc.fd["home"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.pepto = cls.fc.fd["pepto"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_verify_app_installation_and_launch(self):
        """
        Verify the app is installed and launched successfully
        Close the app by clicking X
        Relaunch the app
        Verify the welcome screen shows up
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223889
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13220506
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223887 (US/ENU)
        """
        self.welcome.verify_welcome_screen()  
        self.gotham_utility.click_close()
        assert "HP.Smart" not in self.driver.ssh.send_command('Get-Process -Name "*HP.Smart*"')["stdout"]
        self.driver.launch_app()
        self.welcome.verify_welcome_screen()

    def test_02_verify_privacy_preference_page(self):
        """
        Verify "Manage your HP Smart privacy preferences" page shows after clicking the "Manage Options" button in welcome page.
        Verify back arrow is not available on the title bar/shell title bar.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223893
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223935
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29224241
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223890
        """
        self.welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)
        self.fc.restart_hp_smart()
        self.welcome.verify_welcome_screen()
        self.welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)
        self.privacy_preference.click_back_btn()
        self.welcome.verify_welcome_screen() 

    def test_03_sign_in_with_a_owner_account(self):
        """
        Click "Decline All" button on the welcome screen
        Sign in with owner account

        Verify user land on the OWS value prop.

        https://hp-testrail.external.hp.com/index.php?/cases/view/29223913 
        """
        self.welcome.click_decline_all_btn()
        self.ows_value_prop.verify_windows_ows_value_prop_screen()
        self.ows_value_prop.select_native_value_prop_buttons(index=1)
        self.fc.handle_web_login(self.login_info["email"], self.login_info["password"])
        self.home.verify_home_screen(timeout=30)

    def test_04_check_pivacy_preference(self):
        """
        Click on the printer settings tile
        Observe "Privacy preference" option in the master view

        Verify "Privacy Preferences" option is not available 

        https://hp-testrail.external.hp.com/index.php?/cases/view/29224235
        https://hp-testrail.external.hp.com/index.php?/cases/view/29224253
        """
        self.fc.select_a_printer(self.p)
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        assert self.printer_settings.verify_privacy_preferences_tile(raise_e=False) is False

    def test_05_check_file_settings_value(self):
        """
        Check the HPPrinterControlSettings.xml" file under the localstate folder

        https://hp-testrail.external.hp.com/index.php?/cases/view/26959435
        """
        assert self.pepto.check_control_settings_data('WebServicesOptin') == 'True'
        assert self.pepto.check_control_settings_data('PrinterRegistrationOptin') == 'True'
