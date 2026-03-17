import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_07_Printer_Status_SMS(object):
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
        self.fc.trigger_printer_status(self.serial_number, ['66440', '66441', '66442', '66443', '66444', '66445', '66446', '66447', '66448', '66449', '66450', '66451', '66452', '66453', '66455', '66458', '66459', '66460', '66461', '66462', '66463', '66465', '66467', '66468', '66469', '66470', '66471', '66472', '66473', '66474', '66475', '66476', '66477', '66478', '66479', '66481', '66483', '66484', '66485', '66486', '66488', '66489', '66490', '66491', '66492', '66493', '66494', '66495', '66496', '66497', '66498', '66499', '66500', '66501', '66502', '66503', '66504', '66505', '66506', '66507', '66508', '66509', '66510', '66511', '66512', '66513', '66514', '66515', '66516', '66524', '66526', '66527', '66529', '66535', '66537', '66538', '66539', '66540', '66548', '66549', '66553', '66555', '66557', '66560', '66562', '66564'])
        self.trigger_status['status'] = True
   
    @pytest.mark.parametrize("ioref", ['66440', '66441', '66442', '66443', '66444', '66445', '66446', '66447', '66448', '66449', '66450', '66451', '66452', '66453', '66455', '66458', '66459', '66460', '66461', '66462', '66463', '66465', '66467', '66468', '66469', '66470', '66471', '66472', '66473', '66474', '66475', '66476', '66477', '66478', '66479', '66481', '66483', '66484', '66485', '66486', '66488', '66489', '66490', '66491', '66492', '66493', '66494', '66495', '66496', '66497', '66498', '66499', '66500', '66501', '66502', '66503', '66504', '66505', '66506', '66507', '66508', '66509', '66510', '66511', '66512', '66513', '66514', '66515', '66516', '66524', '66526', '66527', '66529', '66535', '66537', '66538', '66539', '66540', '66548', '66549', '66553', '66555', '66557', '66560', '66562', '66564'])
    def test_03_check_ioref_content(self, ioref):
        if not self.trigger_status:
            pytest.skip("Skip this test as the printer status was not successfully triggered")
        self.printer_status.check_ps_content_all(ioref)

