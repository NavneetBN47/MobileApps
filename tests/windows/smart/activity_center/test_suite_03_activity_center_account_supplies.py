import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from time import sleep

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_03_Activity_Center_Account_Supplies(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.activity_center = cls.fc.fd["activity_center"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack = cls.stack, a_type = "ucde")
        
        """
        This is a method to ensure the PC and printer are in the same wifi.
        """
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_go_home_and_add_a_printer(self):
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

    def test_02_check_account_from_activity_center_bell(self):
        """
        Click on Bell icon on main UI
        Select 'Account' from the Activity Center flyout.

        Verify smart dashboard opens in a web view (Account -> View Notifications)
        Verify correct UI screen title "My Account"
        Verify Activity Center with "Account" shows as design.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27803563
        https://hp-testrail.external.hp.com/index.php?/cases/view/16932012
        https://hp-testrail.external.hp.com/index.php?/cases/view/27997739
        https://hp-testrail.external.hp.com/index.php?/cases/view/28572530
        https://hp-testrail.external.hp.com/index.php?/cases/view/27997740
        https://hp-testrail.external.hp.com/index.php?/cases/view/14099913
        https://hp-testrail.external.hp.com/index.php?/cases/view/28572529
        https://hp-testrail.external.hp.com/index.php?/cases/view/13890674
        """
        self.home.select_activity_btn()
        self.home.verify_activity_pane()
        self.home.click_account_listview()       

        self.activity_center.verify_my_account_screen()
        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()

    def test_03_check_supplies_from_activity_center_bell(self):
        """
        Click on Bell icon on main UI
        Select 'Supplies' from the Activity Center flyout.

        Verify smart dashboard opens in a web view(Account -> View Notifications)

        https://hp-testrail.external.hp.com/index.php?/cases/view/27803557
        https://hp-testrail.external.hp.com/index.php?/cases/view/27803558
        https://hp-testrail.external.hp.com/index.php?/cases/view/27803561
        """
        self.home.select_activity_btn()
        self.home.verify_activity_pane()
        self.home.click_supplies_listview()
        self.activity_center.verify_my_account_screen()
        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()
