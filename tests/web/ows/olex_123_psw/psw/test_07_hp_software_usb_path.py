import pytest
from MobileApps.libs.flows.web.ows.olex_123_and_psw.connect_usb import USBPrinterDisplayTrafficDirector

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_psw_test_setup, request):
        self = self.__class__
        self.driver, self.fc, self.printer_profile, self.hpid, self.ssh_client = olex_123_psw_test_setup
        self.stack = request.config.getoption("--stack")
        self.printer_type = request.config.getoption("--printer-operation")
        self.connect_printer_with_usb = self.fc.fd["td_live_ui"].fd["connect_usb"]
        self.usb_printer_display = USBPrinterDisplayTrafficDirector(self.driver)
        self.driver_download = self.fc.fd["td_live_ui"].fd["driver_download"]
        self.hp_software = self.fc.fd["td_live_ui"].fd["hp_software"]
        
        """
        testRail: https://hp-testrail.external.hp.com/index.php?/suites/view/3624&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3809236 
        """
    def test_01_traffic_director_connect_printer_with_usb_flow(self):
        if self.printer_profile.startswith(("cherry", "lotus")):
            pytest.skip("Skipping test - only cherry/lotus specific tests should run on cherry/lotus profiles")
        self.fc.navigate_traffic_director_live_ui(self.printer_profile)
        self.hp_software.click_use_usb_instead_btn()
        self.hp_software.verify_connect_printer_to_internet_modal()
        self.hp_software.click_connect_printer_to_internet_modal_close_btn()
        self.hp_software.verify_personal_use_hp_software_page(self.printer_profile)
        self.hp_software.click_use_usb_instead_btn()
        self.hp_software.verify_connect_printer_to_internet_modal()
        self.hp_software.click_connect_printer_to_internet_continue_with_usb_btn()
        self.connect_printer_with_usb.verify_connect_usb_page()
        self.fc.fd["traffic_director"].verify_veneer_stepper()
        self.fc.fd["traffic_director"].click_next_btn()
        self.usb_printer_display.verify_continue_usb_setup_printer_display_modal()
        self.fc.fd["traffic_director"].verify_veneer_stepper()
        self.fc.fd["traffic_director"].click_back_btn()
        self.connect_printer_with_usb.verify_connect_usb_page()
        self.fc.fd["traffic_director"].verify_veneer_stepper()
        self.fc.fd["traffic_director"].click_next_btn()
        self.usb_printer_display.verify_continue_usb_setup_printer_display_modal()
        self.fc.fd["traffic_director"].verify_veneer_stepper()