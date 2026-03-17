import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "HPX"

@pytest.mark.usefixtures("function_setup_myhp_launch","load_custom_printer_session")
class Test_Suite_14_Network_Information(object):
    printer_profile = "HP OfficeJet 8130e series"
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls,  windows_test_setup, load_custom_printer_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_custom_printer_session
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.printersettings = cls.fc.fd["printersettings"]
        cls.devicesDetailsMFE = cls.fc.fd["devicesDetailsMFE"]
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.ip = cls.p.get_printer_information()["ip address"]
        cls.fc.add_a_printer(cls.p)
       
        
    @pytest.mark.regression
    def test_01_verify_network_information_C57462241(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devicesDetailsMFE.verify_settings_view_all_item(), "Settings view all is not present"
        self.devicesDetailsMFE.click_view_all_button()
        assert self.printersettings.verify_network_information_opt(), "network information page not loaded"
        self.printersettings.select_network_information()
        assert self.printersettings.verify_network_info_page(self.ip), "Network info page is not visible"