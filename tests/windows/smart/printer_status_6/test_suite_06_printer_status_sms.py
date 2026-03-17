import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_06_Printer_Status_SMS(object):
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
        self.fc.trigger_printer_status(self.serial_number, ['66316', '66317', '66318', '66319', '66320', '66321', '66322', '66323', '66324', '66325', '66327', '66328', '66329', '66330', '66331', '66332', '66333', '66334', '66335', '66336', '66337', '66338', '66339', '66340', '66341', '66342', '66343', '66344', '66345', '66346', '66348', '66349', '66350', '66351', '66352', '66353', '66354', '66355', '66359', '66360', '66367', '66370', '66371', '66372', '66373', '66378', '66379', '66383', '66384', '66385', '66386', '66387', '66388', '66391', '66395', '66396', '66400', '66401', '66407', '66408', '66409', '66410', '66412', '66413', '66415', '66416', '66417', '66419', '66420', '66421', '66422', '66423', '66424', '66425', '66426', '66427', '66428', '66429', '66430', '66431', '66432', '66434', '66435', '66437', '66438', '66439'])
        self.trigger_status['status'] = True
   
    @pytest.mark.parametrize("ioref", ['66316', '66317', '66318', '66319', '66320', '66321', '66322', '66323', '66324', '66325', '66327', '66328', '66329', '66330', '66331', '66332', '66333', '66334', '66335', '66336', '66337', '66338', '66339', '66340', '66341', '66342', '66343', '66344', '66345', '66346', '66348', '66349', '66350', '66351', '66352', '66353', '66354', '66355', '66359', '66360', '66367', '66370', '66371', '66372', '66373', '66378', '66379', '66383', '66384', '66385', '66386', '66387', '66388', '66391', '66395', '66396', '66400', '66401', '66407', '66408', '66409', '66410', '66412', '66413', '66415', '66416', '66417', '66419', '66420', '66421', '66422', '66423', '66424', '66425', '66426', '66427', '66428', '66429', '66430', '66431', '66432', '66434', '66435', '66437', '66438', '66439'])
    def test_03_check_ioref_content(self, ioref):
        if not self.trigger_status:
            pytest.skip("Skip this test as the printer status was not successfully triggered")
        self.printer_status.check_ps_content_all(ioref)

