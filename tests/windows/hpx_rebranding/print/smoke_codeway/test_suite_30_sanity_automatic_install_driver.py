import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_30_Sanity_Automatic_Install_Driver(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]
        cls.ip = cls.p.get_printer_information()["ip address"]


    @pytest.mark.smoke
    def test_01_verfify_driver_automatic_install_C53676659(self):
        """
        Verify "Install driver to print-Automatic Install"

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53676659
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.fd["devicesMFE"].click_add_button()
        self.fc.fd["addprinter"].verify_add_device_panel()
        self.fc.fd["addprinter"].click_choose_printer_button()
        self.fc.fd["addprinter"].verify_progress_bar(timeout=90)
        self.fc.fd["addprinter"].click_input_textbox()
        self.fc.fd["addprinter"].search_printer(self.ip)
        self.fc.fd["addprinter"].click_add_printer_btn()
        if self.fc.fd["addprinter"].verify_install_driver_to_print_screen(raise_e=False):
            pytest.skip('The test printer is already setup or requires manual driver install.')
        else:
            self.fc.fd["addprinter"].verify_auto_install_driver_done(timeout=180)

    

        
