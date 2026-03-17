import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_03_Printer_Status_SMS(object):
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
        self.fc.trigger_printer_status(self.serial_number, ['65797', '65799', '65800', '65802', '65803', '65804', '65806', '65807', '65808', '65809', '65810', '65811', '65815', '65845', '65846', '65847', '65848', '65849', '65850', '65851', '65853', '65858', '65859', '65860', '65862', '65863', '65864', '65869', '65870', '65875', '65888', '65899', '65901', '65902', '65904', '65905', '65906', '65909', '65910', '65911', '65912', '65914', '65916', '65920', '65921', '65923', '65926', '65933', '65934', '65935', '65939', '65940', '65942', '65965', '65966', '65968', '65969', '65970', '65973', '65989', '65990', '65991', '65992', '65993', '65994', '65995', '65996', '65997', '65998', '65999', '66000', '66001', '66002', '66008', '66009', '66011', '66012', '66013', '66015', '66016', '66017', '66018', '66019', '66020', '66021', '66022'])
        self.trigger_status['status'] = True
   
    @pytest.mark.parametrize("ioref", ['65797', '65799', '65800', '65802', '65803', '65804', '65806', '65807', '65808', '65809', '65810', '65811', '65815', '65845', '65846', '65847', '65848', '65849', '65850', '65851', '65853', '65858', '65859', '65860', '65862', '65863', '65864', '65869', '65870', '65875', '65888', '65899', '65901', '65902', '65904', '65905', '65906', '65909', '65910', '65911', '65912', '65914', '65916', '65920', '65921', '65923', '65926', '65933', '65934', '65935', '65939', '65940', '65942', '65965', '65966', '65968', '65969', '65970', '65973', '65989', '65990', '65991', '65992', '65993', '65994', '65995', '65996', '65997', '65998', '65999', '66000', '66001', '66002', '66008', '66009', '66011', '66012', '66013', '66015', '66016', '66017', '66018', '66019', '66020', '66021', '66022'])
    def test_03_check_ioref_content(self, ioref):
        if not self.trigger_status:
            pytest.skip("Skip this test as the printer status was not successfully triggered")
        self.printer_status.check_ps_content_all(ioref)

