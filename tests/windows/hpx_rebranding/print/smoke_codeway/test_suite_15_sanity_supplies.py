import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_15_Sanity_Supplies(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_check_supply_guage_on_device_card_C48458862(self):
        """
        Verify that the supply gauge on the device card page.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48458862
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_supply_levels_card()

    @pytest.mark.smoke
    def test_02_check_supply_guage_on_printer_device_C48460141_C64203535(self):
        """
        Verify the supply gauge in the printer device page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48460141
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/64203535
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        if self.driver.session_data['request'].config.getoption("--stack") in ["rebrand_pie"]:
            self.fc.fd["devicesDetailsMFE"].click_supply_levels_link()
            if self.fc.fd["printersettings"].verify_supply_status_page(timeout=20):
                self.fc.fd["printersettings"].click_top_back_arrow()
            else:
                self.web_driver.add_window_and_switch("supply_levels")
                sleep(2)
                current_url = self.web_driver.get_current_url()
                assert "https://www.hp.com/" in current_url
                sleep(2)
                self.web_driver.set_size('min')
        self.fc.fd["devicesDetailsMFE"].click_top_back_btn()
