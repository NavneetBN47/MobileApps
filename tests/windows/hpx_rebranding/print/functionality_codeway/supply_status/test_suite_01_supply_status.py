import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "HPX"

@pytest.mark.usefixtures("function_setup_myhp_launch")
class Test_Suite_01_Supply_Status(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.fc.add_a_printer(cls.p)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devicesDetailsMFE = cls.fc.fd["devicesDetailsMFE"]
        cls.printersettings = cls.fc.fd["printersettings"]
        cls.printer_name = cls.p.get_printer_information()["model name"]

    @pytest.mark.regression
    def test_01_verify_supply_status_screen_C52826654(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        self.devicesDetailsMFE.click_view_all_on_printer_settings()
        self.printersettings.select_supply_status_option()
        assert self.printersettings.verify_supply_status_page(), "Supply status page is not present"
