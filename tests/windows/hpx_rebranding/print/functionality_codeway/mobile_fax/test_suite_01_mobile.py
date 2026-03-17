import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "HPX"
 
@pytest.mark.usefixtures("function_setup_myhp_launch")
class Test_Suite_01_Mobile_Fax_Functionality(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.devicesDetailsMFE = cls.fc.fd["devicesDetailsMFE"]
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.scan = cls.fc.fd["scan"]
        cls.mobilefax = cls.fc.fd["mobilefax"]
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()['serial number']
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.devicesMFE.click_home_loggedin()
        cls.fc.sign_in(cls.user_name, cls.password, cls.web_driver, user_icon_click=False)
        cls.fc.add_a_printer(cls.p)
 
   
    @pytest.mark.regression
    def test_01_select_Mobile_fax_C49553207(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devicesDetailsMFE.verify_scan_tile(), "Scan tile is not visible"
        self.devicesDetailsMFE.click_scan_tile()
        self.scan.select_source_dropdown()
        self.scan.select_source_document_feeder()
        assert self.scan.verify_scan_btn(), "scan button is not visible"
        self.scan.click_scan_btn()
        assert self.scan.verify_scan_result_screen(), "scan result screen is not displayed"
        self.scan.click_fax_btn()
        assert self.mobilefax.verify_compose_fax_menu_screen(), "Compose fax screen is not visible"
 