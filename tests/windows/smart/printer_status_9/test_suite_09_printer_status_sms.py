import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_09_Printer_Status_SMS(object):
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
        self.fc.trigger_printer_status(self.serial_number, ['66675', '66676', '66677', '66678', '66679', '66680', '66681', '66682', '66683', '66684', '66685', '66687', '66688', '66689', '66690', '66692', '66693', '66694', '66695', '66696', '66699', '66700', '66701', '66705', '66708', '66709', '66714', '66716', '66721', '66723', '75000', '75001', '75010', '75011', '75015', '75016', '75020', '75021', '75025', '75026', '75030', '75031', '75035', '75036', '75040', '75041', '75045', '75060', '75065', '75066', '75067', '75068', '75070', '75085', '75095', '75096', '75100', '75105', '75106', '75115', '75120', '75125', '75135', '75136', '75145', '75170', '75171', '75172', '75175', '75190', '75191', '75200', '85001', '85002', '85003', '85004', '85005', '85006', '85007', '85008', '85009', '85010', '85011', '85012', '85013', '85014', '85015', '85016', '85017', '85018', '85019'])
        self.trigger_status['status'] = True
  
    @pytest.mark.parametrize("ioref", ['66675', '66676', '66677', '66678', '66679', '66680', '66681', '66682', '66683', '66684', '66685', '66687', '66688', '66689', '66690', '66692', '66693', '66694', '66695', '66696', '66699', '66700', '66701', '66705', '66708', '66709', '66714', '66716', '66721', '66723', '75000', '75001', '75010', '75011', '75015', '75016', '75020', '75021', '75025', '75026', '75030', '75031', '75035', '75036', '75040', '75041', '75045', '75060', '75065', '75066', '75067', '75068', '75070', '75085', '75095', '75096', '75100', '75105', '75106', '75115', '75120', '75125', '75135', '75136', '75145', '75170', '75171', '75172', '75175', '75190', '75191', '75200', '85001', '85002', '85003', '85004', '85005', '85006', '85007', '85008', '85009', '85010', '85011', '85012', '85013', '85014', '85015', '85016', '85017', '85018', '85019'])
    def test_03_check_ioref_content(self, ioref):
        if not self.trigger_status:
            pytest.skip("Skip this test as the printer status was not successfully triggered")
        self.printer_status.check_ps_content_all(ioref)

