import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_01_Network_Info(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.ip = cls.p.get_printer_information()["ip address"]      
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_launch_app_without_printer_c57462915(self):
        """
        Check Printer settings in the HPX app (Without printer added to the carousel), verify "Printer settings" is not accessible

        https://hp-testrail.external.hp.com/index.php?/cases/view/57462915
        """
        self.fc.launch_hpx_to_home_page()
        assert self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=5, raise_e=False) is False

    ######################################################################
    #    Simulator printer network info shows not sync for C57462242  #
    #    https://hp-testrail.external.hp.com/index.php?/cases/view/57462242   #
    ######################################################################
    @pytest.mark.skip("Skipping test suite temporarily due to ONESIM printer limitation.")
    @pytest.mark.regression
    def test_02_verify_netwrok_info_page_C57462251_C57462252(self):
        """
        (+) Click on Printer Settings > General, verify Network Information is displayed.
        Check Network Information page, verify the "Wi-Fi Direct" information is removed.
        Check Network Information page for the BLE supported printer, verify BLE information shows.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57462251
                     https://hp-testrail.external.hp.com/index.php?/cases/view/57462252

        """
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].select_network_information()
        self.fc.fd["printersettings"].verify_ip_text()
        self.fc.fd["printersettings"].verify_network_info_page(self.ip)

    