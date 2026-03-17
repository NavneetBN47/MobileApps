import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_01_Printer_Device_Page(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()["serial number"]     


    @pytest.mark.regression
    def test_01_verify_supply_guage_ink_levaes_C48455718(self):
        """
        Verify the printer status messages are displayed properly

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/48455718
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].verify_supply_levels_card()

    @pytest.mark.regression
    def test_02_verify_printer_background_image_C44026596(self):
        """
        Verify the 'Background image' in printer device page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44026596
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=25)
    
    @pytest.mark.regression
    def test_03_check_header_icons_C44256232(self):
        """
        Verify the 'Header' in the printer device page.
        1.'Plus' icon should be displayed.
        2.'Notification' button should be displayed.
        3.'Profile' icon should be displayed.
        4.'Shop Pills' button should be displayed.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44256232
        """
        #TODO: Add more test to check Plus icon and Shop Pills Button when features implemented.
        self.fc.fd["devicesMFE"].verify_bell_icon_show_up()
        self.fc.fd["devicesMFE"].verify_profile_icon_show_up()
        self.fc.fd["devicesMFE"].verify_sign_in_button_show_up()

    @pytest.mark.regression
    def test_04_check_tile_icon_C44225832_C44226447_C44244521(self):
        """
        Verify the 'Scan' icon and 'Position' in the scan tile.
        Verify the 'icon' and 'Position' in the 'Print PDFs' tile.
        Verify the 'icon and 'Position' in the print photo tile.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44225832
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/44226447
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/44244521
        """
        self.fc.fd["devicesDetailsMFE"].verify_scan_tile()
        self.fc.fd["devicesDetailsMFE"].verify_print_pdfs_tile()
        self.fc.fd["devicesDetailsMFE"].verify_print_photos_tile()

    @pytest.mark.regression
    def test_05_check_product_information_card_C44223652_C44223653(self):
        """
        Verify the 'Product information card' in the printer device page.
        Verify the 'Product number' in the product information card.	

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44223652
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/44223653
        """
        self.fc.maximize_window()
        product_number = self.fc.get_printer_info_from_xml_file()[self.serial_number]['ProductNumber']
        self.fc.fd["devicesDetailsMFE"].verify_serial_number_info(self.serial_number)
        self.fc.fd["devicesDetailsMFE"].verify_product_number_info(product_number)
        self.fc.fd["devicesDetailsMFE"].verify_network_discovery_name_info(self.printer_name)

    @pytest.mark.regression
    def test_06_check_warranty_status_option_C44255921(self):
        """
        Verify the 'Warranty status' in the product information card

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44255921
        """
        self.fc.fd["devicesDetailsMFE"].verify_warranty_status_info()

    @pytest.mark.regression
    def test_07_check_more_info_and_reports_option_C44255922(self):
        """
        Verify the 'More information and reports' in the product information card

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/44255922
        """
        self.fc.fd["devicesDetailsMFE"].verify_more_info_and_reports_info()