import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_01_Printer_Status_SMS(object):
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
        https://hp-testrail.external.hp.com/index.php?/cases/view/32634476
        """
        self.fc.trigger_printer_status(self.serial_number, ['65536', '65537', '65538', '65539', '65541', '65542', '65543', '65544', '65546', '65547', '65548', '65549', '65550', '65551', '65553', '65554', '65557', '65558', '65559', '65561', '65563', '65564', '65566', '65567', '65568', '65569', '65570', '65571', '65572', '65573', '65574', '65578', '65579', '65580', '65581', '65582', '65583', '65584', '65585', '65586', '65587', '65588', '65589', '65590', '65591', '65592', '65593', '65594', '65595', '65596', '65597', '65598', '65599', '65602', '65603', '65604', '65605', '65606', '65607', '65608', '65610', '65611', '65612', '65613', '65614', '65616', '65617', '65618', '65619', '65621', '65628', '65629', '65634', '65639', '65640', '65669', '65670', '65671', '65672', '65674', '65675', '65676', '65677', '65679', '65680', '65681'])
        self.trigger_status['status'] = True

    @pytest.mark.parametrize("ioref", ['65536', '65537', '65538', '65539', '65541', '65542', '65543', '65544', '65546', '65547', '65548', '65549', '65550', '65551', '65553', '65554', '65557', '65558', '65559', '65561', '65563', '65564', '65566', '65567', '65568', '65569', '65570', '65571', '65572', '65573', '65574', '65578', '65579', '65580', '65581', '65582', '65583', '65584', '65585', '65586', '65587', '65588', '65589', '65590', '65591', '65592', '65593', '65594', '65595', '65596', '65597', '65598', '65599', '65602', '65603', '65604', '65605', '65606', '65607', '65608', '65610', '65611', '65612', '65613', '65614', '65616', '65617', '65618', '65619', '65621', '65628', '65629', '65634', '65639', '65640', '65669', '65670', '65671', '65672', '65674', '65675', '65676', '65677', '65679', '65680', '65681'])
    def test_03_check_ioref_content(self, ioref):
        if not self.trigger_status:
            pytest.skip("Skip this test as the printer status was not successfully triggered")
        self.printer_status.check_ps_content_all(ioref)

