import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_04_Printer_Status_SMS(object):
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
        self.fc.trigger_printer_status(self.serial_number, ['66023', '66024', '66025', '66026', '66027', '66028', '66029', '66030', '66031', '66032', '66033', '66034', '66035', '66036', '66037', '66038', '66039', '66040', '66042', '66043', '66044', '66045', '66046', '66047', '66049', '66050', '66051', '66052', '66053', '66054', '66055', '66056', '66057', '66058', '66059', '66060', '66061', '66064', '66065', '66066', '66067', '66068', '66069', '66071', '66072', '66073', '66074', '66081', '66084', '66085', '66086', '66087', '66089', '66090', '66092', '66093', '66095', '66096', '66098', '66099', '66101', '66128', '66129', '66130', '66131', '66135', '66136', '66155', '66156', '66157', '66162', '66168', '66169', '66170', '66171', '66172', '66173', '66174', '66175', '66176', '66177', '66207', '66208', '66209', '66211', '66212'])
        self.trigger_status['status'] = True
   
    @pytest.mark.parametrize("ioref", ['66023', '66024', '66025', '66026', '66027', '66028', '66029', '66030', '66031', '66032', '66033', '66034', '66035', '66036', '66037', '66038', '66039', '66040', '66042', '66043', '66044', '66045', '66046', '66047', '66049', '66050', '66051', '66052', '66053', '66054', '66055', '66056', '66057', '66058', '66059', '66060', '66061', '66064', '66065', '66066', '66067', '66068', '66069', '66071', '66072', '66073', '66074', '66081', '66084', '66085', '66086', '66087', '66089', '66090', '66092', '66093', '66095', '66096', '66098', '66099', '66101', '66128', '66129', '66130', '66131', '66135', '66136', '66155', '66156', '66157', '66162', '66168', '66169', '66170', '66171', '66172', '66173', '66174', '66175', '66176', '66177', '66207', '66208', '66209', '66211', '66212'])
    def test_03_check_ioref_content(self, ioref):
        if not self.trigger_status:
            pytest.skip("Skip this test as the printer status was not successfully triggered")
        self.printer_status.check_ps_content_all(ioref)

