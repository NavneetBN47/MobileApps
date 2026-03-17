import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_01_Add_Spt_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.pepto = cls.fc.fd["pepto"]
        
        cls.check_printer = {}

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_add_a_spt_printer(self):
        """
        Add a SPT supported printer to carousel
        wait for 30 seconds on Main UI
        Close the app
        Go to C:\Users[Username]\AppData\Local\Packages\AD2F1837.HPPrinterControl_v10z8vjag6ke6\LocalState and check RecentDeviceList.xml file
        
        Verify IsSptEnabled value shows in the RecentDeviceList.xml file.

        https://hp-testrail.external.hp.com/index.php?/cases/view/39969224
        https://hp-testrail.external.hp.com/index.php?/cases/view/40774003
        """
        self.fc.go_home(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        sleep(30)
        self.driver.terminate_app()
        self.check_printer['spt'] = (self.pepto.check_file_spt_value()).lower()
        if self.check_printer['spt'] == 'false':
            raise ValueError('IsSptEnabled value is false')


        
