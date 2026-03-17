import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "SMB"

class Test_06_04_SMB_Printers_Details_Usage(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, smb_setup, request):
        self = self.__class__
        self.driver, self.fc = smb_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        #locale will be received in language_region format
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        self.spec_file = self.driver.session_data["language"]+"-"+self.driver.session_data["locale"].upper()
        self.home = self.fc.fd["home"]
        self.printers = self.fc.fd["printers"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]
    
    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.verify_printers_menu_btn()
        self.home.click_printers_menu_btn()
        return self.printers.verify_printers_page(table_load=False)
    
    def test_01_verify_usage_tab_select_view_monthly_option_functionality(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        
        #Select monthly view from usage view dropdown
        self.printers.click_printer_details_screen_usage_tab()
        self.printers.click_printers_usage_data_select_usage_view_dropdown()
        self.printers.click_usage_data_select_usage_view_dropdown_option("monthly")

        #Select preferred year from dropdown
        self.printers.click_printers_usage_data_select_usage_view_year_dropdown()
        self.printers.click_usage_data_select_usage_view_year_dropdown_option("2023")

        #Verify Print Usage card based on selected view
        self.printers.verify_printers_usage_data_print_pages_usage_card()
        self.printers.verify_print_pages_usage_card_title()

        #Verifying y-axis of Print Usage card chart
        self.printers.verify_print_pages_usage_card_highcharts_axis_printed_pages_title()

        #Verifying x-axis of Print Usage card chart
        self.printers.verify_print_pages_usage_card_highcharts_black_and_white_button()
        self.printers.verify_print_pages_usage_card_highcharts_color_button()
        self.printers.verify_print_pages_usage_card_highcharts_average_use_button()
       
        expected_xaxis_labels = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        assert expected_xaxis_labels == self.printers.get_print_card_highcharts_xaxis_labels_options()

        #Verify Scan Usage card based on selected view
        if self.printers.verify_printers_usage_data_scan_usage_card_is_displayed() is True:

            self.printers.verify_printers_usage_data_scan_usage_card()
            self.printers.verify_scan_usage_card_title()

            #Verifying y-axis of Scan Usage card chart
            self.printers.verify_scan_usage_card_highcharts_axis_scaned_pages_title()

            #Verifying x-axis of Scan Usage card chart
            self.printers.verify_scan_usage_card_highcharts_scans_button()
            self.printers.verify_scan_usage_card_highcharts_average_use_button()

            expected_xaxis_labels = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
            assert expected_xaxis_labels == self.printers.get_print_card_highcharts_xaxis_labels_options()

    def test_02_verify_usage_tab_select_view_yearly_option_functionality(self):
        #
        self.printers.click_printer_table_view_button()
        self.printers.verify_and_click_connected_printer()
        self.printers.verify_printer_details_screen_printer_name()
        
        #Select yearly view from usage view dropdown
        self.printers.click_printer_details_screen_usage_tab()
        self.printers.click_printers_usage_data_select_usage_view_dropdown()
        self.printers.click_usage_data_select_usage_view_dropdown_option("yearly")
        self.printers.verify_select_usage_view_year_dropdown_is_displayed(displayed=False)

        #Verify Print Usage card based on selected view
        self.printers.verify_printers_usage_data_print_pages_usage_card()
        self.printers.verify_print_pages_usage_card_title()

        #Verifying y-axis of Print Usage card chart
        self.printers.verify_print_pages_usage_card_highcharts_axis_printed_pages_title()

        #Verifying x-axis of Print Usage card chart
        self.printers.verify_print_pages_usage_card_highcharts_black_and_white_button()
        self.printers.verify_print_pages_usage_card_highcharts_color_button()
        self.printers.verify_print_pages_usage_card_highcharts_average_use_button()
        # self.printers.verify_print_card_highcharts_xaxis_year_labels()

        #Verify Scan Usage card based on selected view
        if self.printers.verify_printers_usage_data_scan_usage_card_is_displayed() is True:
            self.printers.verify_printers_usage_data_scan_usage_card()
            self.printers.verify_scan_usage_card_title()

            #Verifying y-axis of Scan Usage card chart
            self.printers.verify_scan_usage_card_highcharts_axis_scaned_pages_title()

            #Verifying x-axis of Scan Usage card chart
            self.printers.verify_scan_usage_card_highcharts_scans_button()
            self.printers.verify_scan_usage_card_highcharts_average_use_button()        
            # self.printers.verify_scan_card_highcharts_xaxis_year_labels()