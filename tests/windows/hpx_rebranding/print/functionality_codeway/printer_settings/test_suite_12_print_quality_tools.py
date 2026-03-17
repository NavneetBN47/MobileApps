import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "HPX"

@pytest.mark.usefixtures("function_setup_myhp_launch")
class Test_Suite_12_Print_Quality_Tools_Align(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devices_details_printer_mfe = cls.fc.fd["devicesDetailsMFE"]
        cls.p = load_printers_session
        cls.fc.add_a_printer(cls.p)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.printer_settings = cls.fc.fd["printersettings"]

    @pytest.mark.regression
    def test_01_verify_privacy_option_disabled_for_guest_C63939725(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devices_details_printer_mfe.verify_privacy_option_is_hidden(), "Privacy option is visible and clickable for guest user"