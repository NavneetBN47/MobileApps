import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_02_Printer_Status_SMS(object):
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
        self.fc.trigger_printer_status(self.serial_number, ['65682', '65683', '65684', '65685', '65686', '65687', '65688', '65689', '65690', '65691', '65692', '65693', '65694', '65695', '65696', '65697', '65698', '65699', '65701', '65702', '65703', '65709', '65710', '65711', '65712', '65713', '65716', '65717', '65719', '65723', '65724', '65725', '65726', '65728', '65729', '65730', '65732', '65733', '65734', '65736', '65737', '65738', '65739', '65740', '65741', '65742', '65743', '65744', '65746', '65747', '65748', '65749', '65750', '65751', '65760', '65763', '65764', '65765', '65766', '65767', '65768', '65769', '65770', '65771', '65772', '65773', '65774', '65776', '65777', '65778', '65779', '65780', '65781', '65782', '65783', '65784', '65785', '65786', '65787', '65788', '65789', '65790', '65791', '65792', '65794', '65796'])
        self.trigger_status['status'] = True
   
    @pytest.mark.parametrize("ioref", ['65682', '65683', '65684', '65685', '65686', '65687', '65688', '65689', '65690', '65691', '65692', '65693', '65694', '65695', '65696', '65697', '65698', '65699', '65701', '65702', '65703', '65709', '65710', '65711', '65712', '65713', '65716', '65717', '65719', '65723', '65724', '65725', '65726', '65728', '65729', '65730', '65732', '65733', '65734', '65736', '65737', '65738', '65739', '65740', '65741', '65742', '65743', '65744', '65746', '65747', '65748', '65749', '65750', '65751', '65760', '65763', '65764', '65765', '65766', '65767', '65768', '65769', '65770', '65771', '65772', '65773', '65774', '65776', '65777', '65778', '65779', '65780', '65781', '65782', '65783', '65784', '65785', '65786', '65787', '65788', '65789', '65790', '65791', '65792', '65794', '65796'])
    def test_03_check_ioref_content(self, ioref):
        if not self.trigger_status:
            pytest.skip("Skip this test as the printer status was not successfully triggered")
        self.printer_status.check_ps_content_all(ioref)

