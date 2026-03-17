import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"

@pytest.mark.usefixtures("function_setup_myhp_launch")
class Test_Suite_01_e2e_flows(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.fc.add_a_printer(cls.p)  
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devicesDetailsMFE = cls.fc.fd["devicesDetailsMFE"]
        cls.diagnosefix = cls.fc.fd["diagnosefix"]
        cls.print = cls.fc.fd["print"]
        cls.printer_name = cls.p.get_printer_information()["model name"]
    
        
    @pytest.mark.regression
    def test_01_check_diagnosing_Fixing_screen_ui_C60951282(self):
        assert self.devicesMFE.verify_windows_dummy_printer(self.printer_name, timeout=30), "Printer was not added successfully"
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        self.devicesDetailsMFE.verify_printer_device_page(self.printer_name)
        self.devicesDetailsMFE.verify_diagnose_and_fix_item()
        self.devicesDetailsMFE.click_diagnose_and_fix_btn()  
        assert self.diagnosefix.verify_diagnose_and_fix_page(), "Diagnose & Fix page was not displayed as expected"
        self.diagnosefix.click_start_btn()
        assert self.diagnosefix.verify_diagnosing_and_fixing_screen_display(), "Diagnosing and Fixing screen was not displayed as expected"    