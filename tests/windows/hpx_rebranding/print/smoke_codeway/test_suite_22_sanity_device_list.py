import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_22_Sanity_Device_List(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_add_printer_to_card_C53169419(self):
        """
        Verify Printer is Added to Printer Card.
        HPXG-2726:[Function] The add a device side panel still shows after adding printer successfully.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53169419
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        
    @pytest.mark.smoke
    def test_02_verify_printer_listed_C53168822(self):
        """
        Add a printer already connected to network, Verify the printer is listed.
        Search again' and 'My Printer isn't listed' buttons should be enabled.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53168822
        """
        self.fc.fd["devicesMFE"].click_add_button()
        self.fc.fd["addprinter"].verify_add_device_panel()
        self.fc.fd["addprinter"].click_choose_printer_button()
        self.fc.fd["addprinter"].verify_progress_bar(timeout=60)
        self.fc.fd["addprinter"].verify_search_printers_card()
        self.fc.fd["addprinter"].verify_search_again_link_is_enable()
        self.fc.fd["addprinter"].verify_my_printer_isnt_listed_link_is_enable()

    @pytest.mark.smoke
    def test_03_add_printer_via_ip_C53170789(self):
        """
        Verify User Can Search Printer by IP Address.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53170789
        """
        self.fc.fd["addprinter"].click_input_textbox()
        self.fc.search_network_printer(self.p)
        self.fc.fd["addprinter"].verify_searched_printers()

        
