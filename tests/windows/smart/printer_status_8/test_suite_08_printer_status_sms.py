import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_08_Printer_Status_SMS(object):
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
        self.fc.trigger_printer_status(self.serial_number, ['66565', '66566', '66567', '66568', '66569', '66575', '66577', '66578', '66579', '66580', '66581', '66582', '66583', '66584', '66585', '66586', '66587', '66588', '66589', '66590', '66591', '66592', '66593', '66594', '66595', '66596', '66597', '66598', '66599', '66600', '66601', '66602', '66603', '66604', '66605', '66606', '66607', '66608', '66609', '66610', '66613', '66614', '66615', '66616', '66617', '66618', '66623', '66626', '66627', '66628', '66629', '66630', '66631', '66632', '66633', '66635', '66637', '66638', '66639', '66640', '66641', '66642', '66643', '66644', '66645', '66647', '66648', '66649', '66650', '66651', '66652', '66655', '66656', '66657', '66658', '66659', '66660', '66661', '66662', '66663', '66664', '66665', '66670', '66672', '66673', '66674'])
        self.trigger_status['status'] = True
   
    @pytest.mark.parametrize("ioref", ['66565', '66566', '66567', '66568', '66569', '66575', '66577', '66578', '66579', '66580', '66581', '66582', '66583', '66584', '66585', '66586', '66587', '66588', '66589', '66590', '66591', '66592', '66593', '66594', '66595', '66596', '66597', '66598', '66599', '66600', '66601', '66602', '66603', '66604', '66605', '66606', '66607', '66608', '66609', '66610', '66613', '66614', '66615', '66616', '66617', '66618', '66623', '66626', '66627', '66628', '66629', '66630', '66631', '66632', '66633', '66635', '66637', '66638', '66639', '66640', '66641', '66642', '66643', '66644', '66645', '66647', '66648', '66649', '66650', '66651', '66652', '66655', '66656', '66657', '66658', '66659', '66660', '66661', '66662', '66663', '66664', '66665', '66670', '66672', '66673', '66674'])
    def test_03_check_ioref_content(self, ioref):
        if not self.trigger_status:
            pytest.skip("Skip this test as the printer status was not successfully triggered")
        self.printer_status.check_ps_content_all(ioref)

