import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_01_Device_List_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

    @pytest.mark.regression   
    def test_01_verify_add_device_panel_C53168691(self):
        """
        Verify Add a Device panel shows after clicking Plus button.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53168691
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.fd["devicesMFE"].click_add_button()
        self.fc.fd["addprinter"].verify_add_device_panel()
        self.fc.fd["addprinter"].click_choose_printer_button()

    @pytest.mark.regression
    def test_02_add_device_screen_shows_C53168821(self):
        """
        Add Device screen should be displayed.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53168821
        """
        self.fc.fd["addprinter"].verify_add_device_screen()
        
    @pytest.mark.regression
    def test_03_printers_load_one_by_one_C53170783(self):
        """
        Printers should be listed one by one with a horizontal loading indicator
        on the "Add a Printer" page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53170783
        """
        self.fc.fd["addprinter"].verify_search_printers_card()

    @pytest.mark.regression
    def test_04_click_search_again_functionality_C53170851(self):
        """
        Verify the "Search Again" Functionality.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53170851
        """
        self.fc.fd["addprinter"].click_search_again_link()
        self.fc.fd["addprinter"].verify_add_device_screen()
        self.fc.fd["addprinter"].verify_progress_bar(timeout=60)
        self.fc.fd["addprinter"].verify_search_printers_card()

    @pytest.mark.regression
    def test_05_printer_listed_C53196241(self):
        """
        Verify "No Result Found for Invalid IP" Message.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53196241
        """
        self.fc.fd["addprinter"].click_input_textbox()
        self.fc.fd["addprinter"].input_ip_address(ip= "1111")
        self.fc.fd["addprinter"].verify_no_results_messgae()

    

    

        
