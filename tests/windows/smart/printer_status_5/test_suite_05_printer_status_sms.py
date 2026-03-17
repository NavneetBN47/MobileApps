import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_05_Printer_Status_SMS(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printer_status = cls.fc.fd["printer_status"]
        cls.serial_number = cls.p.get_printer_information()["serial number"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        cls.trigger_status = {}

    def test_01_go_home_and_add_a_printer(self):
        self.fc.go_home()
        self.fc.select_a_printer(self.p)

    def test_02_trigger_all_status(self):
        """ 
        https://hp-testrail.external.hp.com/index.php?/cases/view/31740463
        https://hp-testrail.external.hp.com/index.php?/cases/view/31740464
        https://hp-testrail.external.hp.com/index.php?/cases/view/31740465
        https://hp-testrail.external.hp.com/index.php?/cases/view/32543797
        https://hp-testrail.external.hp.com/index.php?/cases/view/27864750
        https://hp-testrail.external.hp.com/index.php?/cases/view/32147423
        https://hp-testrail.external.hp.com/index.php?/cases/view/32212250
        https://hp-testrail.external.hp.com/index.php?/cases/view/33127660
        https://hp-testrail.external.hp.com/index.php?/cases/view/33388120
        https://hp-testrail.external.hp.com/index.php?/cases/view/27864750
        https://hp-testrail.external.hp.com/index.php?/cases/view/27864751
        https://hp-testrail.external.hp.com/index.php?/cases/view/27864752
        https://hp-testrail.external.hp.com/index.php?/cases/view/27864753
        https://hp-testrail.external.hp.com/index.php?/cases/view/27864754
        https://hp-testrail.external.hp.com/index.php?/cases/view/27864755
        https://hp-testrail.external.hp.com/index.php?/cases/view/27876735

        """
        self.fc.trigger_printer_status(self.serial_number, ['66213', '66214', '66215', '66216', '66217', '66218', '66219', '66220', '66221', '66222', '66223', '66228', '66229', '66230', '66231', '66233', '66234', '66235', '66236', '66237', '66241', '66242', '66243', '66244', '66245', '66246', '66247', '66248', '66249', '66250', '66251', '66252', '66253', '66255', '66256', '66257', '66258', '66262', '66263', '66264', '66265', '66266', '66267', '66268', '66269', '66270', '66271', '66272', '66273', '66277', '66278', '66279', '66280', '66281', '66282', '66283', '66284', '66285', '66286', '66287', '66288', '66289', '66290', '66291', '66292', '66293', '66294', '66295', '66296', '66297', '66298', '66299', '66300', '66301', '66302', '66303', '66304', '66305', '66306', '66307', '66310', '66311', '66312', '66313', '66314', '66315'])
        self.trigger_status['status'] = True
    
    @pytest.mark.parametrize("ioref", ['66213', '66214', '66215', '66216', '66217', '66218', '66219', '66220', '66221', '66222', '66223', '66228', '66229', '66230', '66231', '66233', '66234', '66235', '66236', '66237', '66241', '66242', '66243', '66244', '66245', '66246', '66247', '66248', '66249', '66250', '66251', '66252', '66253', '66255', '66256', '66257', '66258', '66262', '66263', '66264', '66265', '66266', '66267', '66268', '66269', '66270', '66271', '66272', '66273', '66277', '66278', '66279', '66280', '66281', '66282', '66283', '66284', '66285', '66286', '66287', '66288', '66289', '66290', '66291', '66292', '66293', '66294', '66295', '66296', '66297', '66298', '66299', '66300', '66301', '66302', '66303', '66304', '66305', '66306', '66307', '66310', '66311', '66312', '66313', '66314', '66315'])
    def test_03_check_ioref_content(self, ioref):
        if not self.trigger_status:
            pytest.skip("Skip this test as the printer status was not successfully triggered")
        self.printer_status.check_ps_content_all(ioref)

