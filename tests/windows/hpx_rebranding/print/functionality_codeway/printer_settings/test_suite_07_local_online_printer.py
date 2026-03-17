import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_07_Local_Online_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_verify_printer_settings_item_C57462898_C57462900(self):
        """
        verify the Printer Settings is enabled.
        Verify Printer status and Supply status screen should be displayed
        Verify printer status screen displays.
        Verify "Advanced Settings" tab is displayed and enabled.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462898
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462900          
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].verify_status_under_status_section()
        self.fc.fd["printersettings"].verify_reports_under_tools_section()
        self.fc.fd["printersettings"].verify_advanced_settings_under_setting_section()
        self.fc.fd["printersettings"].verify_option_under_information_section()

    test_option = [("select_printer_reports", False),
                    ("select_print_quality_tools", False),
                    ("select_printer_information", True),
                    ("select_network_information", False),
                    ("select_advanced_settings_item", False)]
    @pytest.mark.parametrize("method_name, expected_result", test_option)
    @pytest.mark.regression
    def test_02_verify_printer_settings_item_C57462901_C57462902_C57462904(self, method_name, expected_result):
        """
        Verify "Print Reports" tab is displayed and enabled.
        Verify "Print Quality Tools" tab is displayed and enabled.
        Verify "Printer Information" is displayed and enabled.
        Verify "Network Information" is displayed and enabled.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462901
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462902
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462904

        """
        getattr(self.fc.fd["printersettings"], method_name)()
        sleep(3)
        assert self.fc.fd["printersettings"].verify_model_name_title() == expected_result