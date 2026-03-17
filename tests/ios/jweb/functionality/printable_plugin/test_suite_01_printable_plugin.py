import pytest
from time import sleep
from MobileApps.libs.ma_misc.conftest_misc import get_package_url

pytest.app_info = "JWEB"

class Test_Suite_01_Printable_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        cls.p = load_printers_session
        # Define flows
        cls.ios_system = cls.fc.fd["ios_system"]
        cls.home = cls.fc.fd["home"]
        cls.printable_plugin = cls.fc.fd["printable_plugin"]
        cls.print = cls.fc.fd["printer"]

    @pytest.fixture(scope="function", autouse=True)
    def navigate_to_printable_plugin(self):
        """
        If not at printable plugin, navigate to printable plugin, and accept any pop-up message
        """
        self.fc.flow_load_home_screen()
        if not self.printable_plugin.verify_at_printable_plugin():
            self.home.select_plugin_from_home("printer")
        if self.print.verify_continue_popup():
            self.print.select_continue()

    def test_01_verify_print_operation(self):
        """ 
        C28698119: Verify Printer Method Operation When Printer Providers Are Available
            - Navigate to Printer Plugin, leave URL in DocSourceType.URL as is, and click Print
            - Select a printer from the pop up dialog, and select print
            - expecting "printInitiated": true as a result of printing
        """
        self.printable_plugin.select_open_print_page_btn()
        self.ios_system.dismiss_hp_local_network_alert()
        self.print.select_printer_from_list(self.p.get_printer_information()['bonjour name'])
        self.ios_system.dismiss_hp_local_network_alert()
        self.print.select_print_btn()
        if self.print.verify_continue_popup():
            self.print.select_continue()
        assert self.printable_plugin.get_print_text_result(timeout=35)['printInitiated'] == True

    def test_02_verify_valid_printability_of_url(self):
        """ 
        C28698122: Verify Printability Functionality for a Valid File
            - Navigate to Printer Plugin, leave URL in DocSourceType.URL as is, and click 'Determine Printability'
            - expecting "itemPrintability": printable as a result
        """
        self.printable_plugin.select_determine_printability_btn()
        assert self.printable_plugin.get_print_text_result()['itemPrintability'] == 'printable'

    def test_03_verify_invalid_printability_of_url(self):
        """ 
        C28711673: Verify Printability Functionality for a Invalid File (HTTP URL)
            - Navigate to Printer Plugin, change URLin DocSourceType.URL, remove https with http, and click 'Determine Printability'
            - expecting Requires Https Scheme Error
        """
        url = self.printable_plugin.get_text_from_event_url_text_field()
        self.printable_plugin.insert_text_into_event_url_text_field("http" + url[5:]) 
        self.printable_plugin.select_determine_printability_btn()
        printability_result = self.printable_plugin.get_print_text_result()
        assert printability_result['type'] == 'invalidParameters'
        assert printability_result['reason'] == 'The url does not use the required https scheme'
    
    def test_04_verify_invalid_printability_of_empty_url(self):
        """ 
        C28711674: Verify Printability Functionality for a Invalid File (Empty URL)
            - Navigate to Printer Plugin, change URLin DocSourceType.URL to an empty value, and click 'Determine Printability'
            - expecting Invalid Parameter Error
        """
        self.printable_plugin.insert_text_into_event_url_text_field(" ") 
        self.printable_plugin.select_determine_printability_btn()
        printability_result = self.printable_plugin.get_print_text_result()
        assert printability_result['type'] == 'invalidParameters'
        assert 'URL' in printability_result['reason']