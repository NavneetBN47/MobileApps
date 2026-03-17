import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import time

pytest.app_info = "HPX"

class Test_Suite_01_Product_Information:
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_hpx_flow_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_hpx_flow_setup
        cls.p = load_printers_session
        # Define flows
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.hpx_printer_details = cls.fc.fd[FLOW_NAMES.HPX_PRINTERS_DETAILS]
        cls.printers = cls.fc.fd[FLOW_NAMES.PRINTERS]
        cls.hpx_shortcuts = cls.fc.fd[FLOW_NAMES.HPX_SHORTCUTS]
        cls.camera_scan = cls.fc.fd[FLOW_NAMES.CAMERA_SCAN]
        cls.print_quality_tools = cls.fc.fd[FLOW_NAMES.PRINT_QUALITY_TOOLS]
        # Enable HPX Flag
        cls.fc.hpx = True
    
    def test_01_verify_product_information_ui_on_printer_device_detail_page(self):
        """
        Description: C51970182
        Steps:
            1. Install and launch the app
            2. Sign in and navigate to root
            3. Add a printer as device
            4. Tap on device card to navigate to device detail page
            5. Scroll down to Product Information section and observe
        Expected Result:
            Verify the Production information UI as per design
                -strings, font, size, color, padding should be as per design
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.navigate_to_product_information_details(raise_e=False, max_swipes=4)
        self.hpx_printer_details.click_more_information_and_reports_btn()
    
    def test_02_verify_redirection_for_more_information_and_reports(self):
        """
        Description: C44018803
        Steps:
            Install and launch the app
            Sign in and navigate to root
            Add a printer as device
            Tap on device card to navigate to device detail page
            Scroll down to Product Information section
            Tap on the arrow next to 'More Information and reports'
        Expected Result:
            Verify user is redirected to Printer information page
            verify the Printer information page is as per Figma
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.navigate_to_product_information_details(raise_e=False, max_swipes=5)
        self.hpx_printer_details.click_more_information_and_reports_btn()
        self.hpx_printer_details.click_printer_information_general_btn()
        assert self.hpx_printer_details.verify_printer_information_title()
    
    def test_03_printer_information_redirection_to_general(self):
        """
        Description: C44018806
        Steps:	
            Install and launch the app
            Sign in and navigate to root
            Add a printer as device
            Tap on device card to navigate to device detail page
            Scroll down to Product Information section
            Tap on the arrow next to 'More Information and reports'
            Tap on General
            Observe
        Expected Result:
            Verify user is redirected to General section of Printer information page
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.navigate_to_product_information_details(raise_e=False, max_swipes=5)
        self.hpx_printer_details.click_more_information_and_reports_btn()
        self.hpx_printer_details.click_printer_information_network_btn()
        assert self.hpx_printer_details.verify_printer_information_title()
    
    def test_04_printer_information_redirection_to_network(self):
        """
        Description: C44018807
        Steps:
            1. Install and launch the app
            2. Sign in and navigate to root
            3. Add a printer as device
            4. Tap on device card to navigate to device detail page
            5. Scroll down to Product Information section
            6. Tap on the arrow next to 'More Information and reports'
            7. Tap on Network
            8. Observe
        Expected Result:
            Verify user is redirected to Network section of Printer information page
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.navigate_to_product_information_details(raise_e=False, max_swipes=5)
        self.hpx_printer_details.click_more_information_and_reports_btn()
        self.hpx_printer_details.click_printer_information_reports_btn()
        assert self.hpx_printer_details.verify_printer_information_title()
    
    def test_05_printer_information_verify_the_report_print_flow(self):
        """
        Description: C44018809
        Steps:
            Install and launch the app
            Sign in and navigate to root
            Add a printer as device
            Tap on device card to navigate to device detail page
            Scroll down to Product Information section
            Tap on the arrow next to 'More Information and reports'
            Tap on Reports
            Tap on any of the print report option for example "Printer status report"
            Observe
        Expected Result:
            Verify the report is printed successfully
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.hpx_printer_details.click_add_device_btn()
        self.printers.search_printer_by_ip(self.p.ipAddress)
        self.hpx_printer_details.click_printer_device_card()
        self.hpx_printer_details.navigate_to_product_information_details(raise_e=False, max_swipes=5)
        self.hpx_printer_details.click_more_information_and_reports_btn()
        self.hpx_printer_details.click_printer_information_reports_btn()
        self.hpx_printer_details.verify_printer_information_title()
        self.hpx_printer_details.click_reports_demo_page_print_btn()
        self.hpx_printer_details.verify_reports_print_progress_status()
        assert self.hpx_printer_details.verify_reports_print_success_status()