import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_25_Sanity_Printer_Settings_Offline_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)

        cls.printer_name = cls.p.get_printer_information()['model name']


    @pytest.mark.smoke
    def test_01_verify_printer_settings_with_offline_status_C57462418_C57462421_C57462423_C57462425_C57404813(self):
        """
        Trigger the offline status for printer.
        Verify "Printer settings" tile is enabled.
        Click the View all button.
        Verify "Printer Information" screen opens with minimum item.
        Verify Printer Reports tab/Print Quality Tools tab/Network Information tab are disabled.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462418
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462421
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462423
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462425
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/57404813
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        host_name = self.fc.get_printer_info_from_xml_file()['HostName']
        self.fc.trigger_printer_offline_status(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_printer_information_opt()
        self.fc.fd["printersettings"].verify_network_information_is_disable()
        self.fc.fd["printersettings"].verify_printer_reports_is_disable()
        self.fc.fd["printersettings"].verify_printer_quality_tools_is_disable()
        self.fc.fd["printersettings"].verify_printer_info_page_with_offline_printer(host_name, self.printer_name)

    @pytest.mark.smoke
    # [HPXG-3113] Remove Printer settings phase 2 options for Beta 1 - HP-Jira
    def test_02_verify_status_section_with_offline_status_C57462419(self):
        """
        Click "Printer settings" tile, verify correct option shows under Status Section

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462419
        """
        self.fc.fd["printersettings"].select_printer_status_item()
        self.fc.fd["printer_status"].verify_ps_offline_screen()
        if self.driver.session_data['request'].config.getoption("--stack") in ["rebrand_pie"]:
            self.fc.fd["printersettings"].select_supply_status_option()
            if self.fc.fd["printersettings"].verify_supply_status_page(timeout=10) is False and self.fc.fd["printersettings"].verify_lets_finish_setting_up_page(timeout=3) is False:
                self.web_driver.add_window_and_switch("supply_levels")
                sleep(2)
                current_url = self.web_driver.get_current_url()
                assert "https://www.hp.com/" in current_url
                sleep(2)
                self.web_driver.set_size('min')
        else:
            pytest.skip("Beta 1 has no this feature")
  
    @pytest.mark.smoke
    def test_03_restore_printer_status(self):
        """
        Restore printer online status.
        """
        self.fc.restore_printer_online_status(self.p)