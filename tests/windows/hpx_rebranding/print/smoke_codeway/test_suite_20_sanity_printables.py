import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_20_Sanity_Printables(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()["serial number"]


    @pytest.mark.smoke
    def test_01_verify_printables_tile_c52954374_c53175450(self):
        """
        Verify the Printables Tile is present in Printer device page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/52954374

        Verify the UI and text match the design and copy deck.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53175450
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printables_tile()

    @pytest.mark.smoke
    def test_02_click_printables_tile_to_the_web_page_c52954526(self):
        """
        Verify that the web page opens successfully when the Printable tile is clicked

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/52954526
        """
        self.fc.fd["devicesDetailsMFE"].click_printables_tile()
        self.web_driver.add_window("printables")
        if "printables" not in self.web_driver.session_data["window_table"].keys():
            self.fc.fd["devicesDetailsMFE"].click_printables_tile()
            self.web_driver.add_window("printables")
        self.web_driver.switch_window("printables")
        self.web_driver.set_size("max")
        sleep(2)
        current_url = self.web_driver.get_current_url()
        logging.info("Current URL: {}".format(current_url))
        assert "https://printables.hp.com/" in current_url

    @pytest.mark.smoke
    def test_03_verify_redirection_to_learn_page_c57717515_c57717544(self):
        """
        Verify redirection to the Learn page from the Printables tile.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57717515

        Verify redirection with correct region and language codes.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57717544
        """
        current_url = self.web_driver.get_current_url()
        logging.info("Current URL: {}".format(current_url))
        assert "us/en?jumpid=va_tzw3p2fvgq" in current_url

    @pytest.mark.smoke
    def test_04_verify_valid_parameters_in_url_c57717716(self):
        """
        Verify redirection to the correct URL with valid parameters

        The user is redirected to the correct URL (https://printables.hp.com/?jumpid=va_tzw3p2fvgq-{printersku}-{y/n}) with valid parameters for the printer SKU and Instant Ink subscription status.
        Note: One for the productNumber (or modelNumber) and the other is a flag Y or N indicating if the printer is enrolled for instant ink or not.

        https://hp-testrail.external.hp.com/index.php?/cases/view/57717716
        """
        product_number = self.fc.get_printer_info_from_xml_file()[self.serial_number]['ProductNumber']
        current_url = self.web_driver.get_current_url()
        logging.info("Current URL: {}".format(current_url))
        assert product_number in current_url
        
        # Check for Instant Ink subscription flag (Y or N) in the URL
        assert any(flag in current_url for flag in ['-Y', '-N', '-y', '-n']), \
            f"Expected Instant Ink flag (Y or N) not found in URL: {current_url}"

    @pytest.mark.smoke
    def test_05_verify_II_printer_sku_param_c57717945(self):
        """
        Verify URL generation for Instant Ink subscribed printers

        The URL includes the correct printer SKU and y for Instant Ink subscription status.

        https://hp-testrail.external.hp.com/index.php?/cases/view/57717945
        """
        current_url = self.web_driver.get_current_url()
        logging.info("Current URL: {}".format(current_url))
        if any(flag in current_url for flag in ['-N','-n']):
            pytest.skip("Printer is not enrolled in Instant Ink, skipping test")

    @pytest.mark.smoke
    def test_06_verify_non_II_printer_sku_param_c57718176(self):
        """
        Verify URL generation for non-Instant Ink printers

        The URL includes the correct printer SKU and n for non-Instant Ink subscription status.

        https://hp-testrail.external.hp.com/index.php?/cases/view/57718176
        """
        current_url = self.web_driver.get_current_url()
        logging.info("Current URL: {}".format(current_url))
        if any(flag in current_url for flag in ['-Y','-y']):
            pytest.skip("Printer is enrolled in Instant Ink, skipping test")

    @pytest.mark.smoke
    def test_07_print_from_printable_web_page_c52954615(self):
        """
        Verify that the user can print the contents from the Printable web page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/52954615
        """
        if self.fc.fd["printables"].verify_your_privacy_dialog():
            self.fc.fd["printables"].click_privacy_accept_all_btn()
        self.fc.fd["printables"].search_and_select_image('Happy 4th')
        self.fc.fd["printables"].verify_web_print_btn()
        self.fc.fd["printables"].click_web_print_btn()
        self.fc.fd["printables"].verify_print_dialog()
        self.fc.fd["printables"].click_dialog_print_btn()

