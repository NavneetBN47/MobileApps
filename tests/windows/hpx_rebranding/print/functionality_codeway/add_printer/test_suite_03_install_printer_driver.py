import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_03_Install_printer_driver(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.ip = cls.p.get_printer_information()["ip address"]
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_click_continue_on_driver_unavailable_screen_C53679223(self):
        """
        Verify "Continue" button functionality. 
        simulator printer doesn't support trigger offline status.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53679223
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.fd["devicesMFE"].click_add_button()
        self.fc.fd["addprinter"].verify_add_device_panel()
        self.fc.fd["addprinter"].click_choose_printer_button()
        self.fc.fd["addprinter"].verify_progress_bar(timeout=90)
        self.fc.fd["addprinter"].click_input_textbox()
        self.fc.search_network_printer(self.p)
        self.fc.fd["addprinter"].click_add_printer_btn()
        if not self.fc.fd["addprinter"].verify_install_driver_to_print_screen(timeout=60, raise_e=False):
            pytest.skip('The test printer is not an onboarded printer.')
        else:
            self.fc.trigger_printer_offline_status(self.p)
            self.fc.fd["addprinter"].verify_auto_install_driver_to_print_disappear()
            self.fc.fd["addprinter"].click_driver_unavailable_btn()
            self.fc.fd["addprinter"].verify_remove_and_add_the_printer_again_screen()
            self.fc.fd["addprinter"].click_continue_btn_on_add_printer_again()
            self.fc.fd["addprinter"].verify_connecting_to_the_printer_screen()

    @pytest.mark.regression
    def test_02_trigger_printer_online(self):
        """
        Connect network to printer.
        """
        self.fc.restore_printer_online_status(self.p)