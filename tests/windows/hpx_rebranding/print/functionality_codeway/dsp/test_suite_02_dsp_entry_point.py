import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "HPX"
 
@pytest.mark.usefixtures("function_setup_myhp_launch") 
class Test_Suite_02_Dsp_Entry_Tile(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.fc.add_a_printer(cls.p)  
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devicesDetailsMFE = cls.fc.fd["devicesDetailsMFE"]
        cls.supplies_status = cls.fc.fd["supplies_status"]  
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()['serial number']
 
 
    @pytest.mark.regression
    def test_01_click_get_supplies_tile_verify_dsp_p2_page_shows_C60641901(self):
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        assert self.devicesMFE.verify_windows_dummy_printer(self.printer_name), "Printer not found in Devices Card"
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        self.devicesDetailsMFE.verify_printer_device_page(self.printer_name)
        self.devicesDetailsMFE.verify_all_tiles_printer_device_pages(self.printer_name)
        self.supplies_status.click_get_supplies_btn()
        assert self.supplies_status.verify_get_supplies_page(), "Get Supplies page not displayed correctly"