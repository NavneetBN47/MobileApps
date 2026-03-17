import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "HPX"

@pytest.mark.usefixtures("function_setup_myhp_launch")
class Test_Suite_13_Printer_Reports(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        cls.devicesDetailsMFE = cls.fc.fd["devicesDetailsMFE"]
        cls.printersettings = cls.fc.fd["printersettings"]
        cls.p = load_printers_session
        cls.fc.add_a_printer(cls.p)
        cls.printer_name = cls.p.get_printer_information()["model name"]

    @pytest.mark.regression
    def test_01_verify_not_available_message_displays_C57706998(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devicesDetailsMFE.verify_printer_settings_part(), "Printer settings part is not present"
        self.devicesDetailsMFE.click_view_all_button()
        assert self.printersettings.verify_tools_tile(), "Tools section is not visible"
        self.printersettings.select_print_quality_tools()
        assert self.printersettings.verify_this_feature_is_not_available_screen(), "This feature is not available for the selected printer text is not displayed"
        feature_text = "This feature is not available for your selected printer through the HPX. To perform print quality actions, use the full featured software, or see the printer's control panel."
        feature_screen = self.printersettings.get_feature_screen_text()
        assert feature_text == feature_screen

    @pytest.mark.regression
    def test_02_navigate_printer_settings_verify_print_anywhere_hidden_C57462907(self):
        self.devicesMFE.click_windows_dummy_printer(self.printer_name)
        assert self.devicesDetailsMFE.verify_printer_settings_part(), "printer settings title not found"
        assert self.devicesDetailsMFE.verify_settings_view_all_item(), "Settings view all is not present"
        self.devicesDetailsMFE.click_view_all_button()
        assert self.printersettings.verify_print_anywhere_option_is_hidden(), "Print anywhere option is enabled"
