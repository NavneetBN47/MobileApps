import pytest
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_08_Home_Diagnose_And_Fix(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)


    def test_01_verify_diagnose_and_fix_window_opened(self):
        """
        Verify Diagnose & Fix window is opened 
        after clicking on the Diagnose & Fix icon in navigation pane
        when navigation pane is opened and closed.
        Install app which version is the same or higher than the store app, verify "New Update Available" modal does not show, app is usable

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24340329
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/24844451
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/26927729
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14721552
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28217259
        """
        self.fc.go_home()
        self.home.verify_no_new_update_available_text()
        self.fc.select_a_printer(self.p)

        # collapsed navigation pane
        self.home.verify_navigation_pane_split_view(printer=True)
        self.home.select_diagnose_and_fix_btn()
        self.home.verify_diagnose_and_fix_screen()
        self.home.select_navbar_back_btn()

        # expanded navigation pane
        self.home.menu_expansion(expand=True)
        self.home.select_diagnose_and_fix_btn()
        self.home.verify_diagnose_and_fix_screen()
        self.home.select_navbar_back_btn()
