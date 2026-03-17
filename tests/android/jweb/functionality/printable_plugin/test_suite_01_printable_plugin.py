import pytest
from time import sleep

pytest.app_info = "JWEB"

class Test_Suite_01_Printable_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, hpps_setup, android_jweb_setup, load_printers_session):
        cls = cls.__class__
        # cls.p = load_printers_session
        cls.driver, cls.fc = android_jweb_setup
        cls.p = load_printers_session
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.printable_plugin = cls.fc.fd["printable_plugin"]
        cls.print = cls.fc.fd["print"]
        cls.hpps = cls.fc.fd["hpps"]

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_printer_plugin(self):
        """
        If not at printable plugin, navigate to printable plugin
        """
        self.fc.flow_load_home_screen()
        if not self.printable_plugin.verify_at_printable_plugin():
            self.home.select_plugin_from_home("printer")

    def test_01_verify_print_operation(self):
        """ 
        C28698119: Verify Printer Method Operation When Printer Providers Are Available
            - Navigate to Printer Plugin, leave URL in DocSourceType.URL as is, and click Print
            - Select a printer from the pop up dialog, and select print
            - expecting "printInitiated": true as a result of printing
        """
        self.printable_plugin.select_open_print_page_btn()
        self.print.select_all_printers()
        self.print.send_text_to_search_box(self.p.get_printer_information()['bonjour name'])
        self.print.select_first_printer_from_list()
        self.hpps.agree_and_accept_terms_and_condition_if_present()

        self.hpps.handle_hpps_t_and_c_notification_on_android_10_11_if_present()
        self.hpps.agree_and_accept_terms_and_condition_if_present()
        self.hpps.turn_off_wifi_direct_notification_on_android_10_11_if_present()
        
        self.print.select_print()
        self.hpps.accept_ok_for_document_passing()
        assert self.printable_plugin.get_print_text_result()['printInitiated'] == True

    @pytest.mark.parametrize('orientation_option', ["landscape", "portrait", "no_option"])
    def test_02_verify_landscape_orientation_option(self, orientation_option):
        """ 
        C29091888: Verify Print Preview Displays Document in Landscape When Chosen
            - Navigate to Printer Plugin, leave URL in DocSourceType.URL as is, chose Landscape as orientation and click Print
            - expecting Landscape orientation option in Print Dialog 
        C29091891: Verify Print Preview Displays Document in Portrait When Chosen
            - Navigate to Printer Plugin, leave URL in DocSourceType.URL as is, chose Portrait as orientation and click Print
            - expecting Portrait orientation option in Print Dialog 
        C29091893: Verify Print Preview Displays Document in Landscape When No Option Is Chosen
            - Navigate to Printer Plugin, leave URL in DocSourceType.URL as is, leave orientation as No Option and click Print
            - expecting Landscape orientation option in Print Dialog 
        """
        self.printable_plugin.select_orientation_from_plugin_page(orientation_option)
        self.printable_plugin.select_open_print_page_btn()
        orientation_goal = "Portrait" if orientation_option == "portrait" else "Landscape"
        assert self.print.get_orientation_text() == orientation_goal

    def test_03_verify_valid_printability_of_url(self):
        """ 
        C28698122: Verify Printability Functionality for a Valid File
            - Navigate to Printer Plugin, leave URL in DocSourceType.URL as is, and click 'Determine Printability'
            - expecting "itemPrintability": printable as a result
        """
        self.printable_plugin.select_determine_printability_btn()
        assert self.printable_plugin.get_print_text_result()['itemPrintability'] == 'printable'

    def test_04_verify_invalid_printability_of_url(self):
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
    
    def test_05_verify_invalid_printability_of_empty_url(self):
        """ 
        C28711674: Verify Printability Functionality for a Invalid File (Empty URL)
            - Navigate to Printer Plugin, change URLin DocSourceType.URL to an empty value, and click 'Determine Printability'
            - expecting Invalid Parameter Error
        """
        self.printable_plugin.insert_text_into_event_url_text_field("") 
        self.printable_plugin.select_determine_printability_btn()
        printability_result = self.printable_plugin.get_print_text_result()
        assert printability_result['type'] == 'invalidParameters'
        assert printability_result['reason'] == 'DocSource\'s must provide a url property'

