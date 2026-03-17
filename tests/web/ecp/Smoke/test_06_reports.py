import pytest
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
import random
from time import sleep
pytest.app_info = "ECP"

#Generate test report name
report_name="auto_report"+str(random.randint(1,10))

class Test_06_ECP_Reports(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.reports = self.fc.fd["reports"]
        self.endpoint_security = self.fc.fd["endpoint_security"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        # self.customer = self.account["customer"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_reports(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_reports_menu_btn()
        return self.reports.verify_reports_table(report_name)

    def test_01_verify_reports_page_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33389414
        self.reports.verify_page_title("Reports")
        self.reports.verify_reports_search_box()
        self.reports.verify_reports_generate_button()
        self.reports.verify_reports_filter_button()
        self.reports.verify_reports_column_option_gear()

    def test_02_verify_reports_refresh_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33389414
        self.reports.verify_reports_page(table_load=False)
        cur_time = self.reports.get_sync_time_info()
        sleep(1)
        self.reports.click_refresh_button()
        new_time = self.reports.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.replace("&nbsp;", " ").split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y  %I:%M:%S %p") == True
        assert new_time != cur_time
        
    def test_03_verify_reports_contextual_footer(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33389414
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33397985
        self.reports.verify_reports_page()
        self.reports.click_reports_checkbox()
        self.reports.verify_contextual_footer()
        self.reports.verify_contextual_footer_cancel_button()
        self.reports.verify_contextual_footer_selected_item_label()
        self.reports.verify_contextual_footer_select_action_dropdown()
        self.reports.verify_contextual_footer_continue_button()

        # Cancel Functionality
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Save as PDF")
        self.reports.click_contextual_footer_cancel_button()
        self.reports.verify_contextual_footer_is_not_displayed()

    def test_04_verify_reports_contextual_footer_select_action_dropdown_options(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33389416
        expected_options=["Save as PDF","Save as XLSX","Edit","Delete"]
        self.reports.verify_reports_page()
        self.reports.click_reports_checkbox()
        self.reports.verify_contextual_footer()
        self.reports.click_contextual_footer_select_action_dropdown()
        assert expected_options == self.reports.get_contextual_footer_select_action_dropdown_options()

    def test_05_verify_reports_pagination(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33389414
        self.reports.verify_reports_page()
        self.reports.verify_all_page_size_options_new([5,25, 50, 100, 500])
        self.reports.verify_table_displaying_correctly_new(5, page=1)
        self.reports.verify_table_displaying_correctly_new(25, page=1)
        self.reports.verify_table_displaying_correctly_new(50, page=1)
        self.reports.verify_table_displaying_correctly_new(100, page=1)
        self.reports.verify_table_displaying_correctly_new(500, page=1)

    def test_06_verify_column_option_popup_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33389415
        self.reports.verify_reports_page()
        expected_options= ["Report Name", "Category", "Report Type", "Date Generated", "Status"]
        self.reports.click_reports_column_option_settings_gear_button()
        self.reports.verify_column_options_popup_title()
        self.reports.verify_column_options_popup_reset_to_default_button()
        self.reports.verify_column_options_popup_cancel_button()
        self.reports.verify_column_options_popup_save_button()
        assert expected_options == self.reports.get_column_options_popup_options()

    def test_07_verify_column_option_popup_save_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33389415
        self.reports.verify_reports_page()
        self.reports.click_reports_column_option_settings_gear_button()
        self.reports.click_column_option("Status")
        self.reports.click_column_options_popup_save_button()

        # Verify reports table Status Column
        self.reports.verify_customers_tabel_column("Status",displayed=False)

        # Reverting the Column option changes
        self.reports.click_reports_column_option_settings_gear_button()
        self.reports.click_column_option("Status")
        self.reports.click_column_options_popup_save_button()
        self.reports.verify_customers_tabel_column("Status")

    def test_08_verify_column_option_popup_cancel_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33389415
        self.reports.verify_reports_page()
        self.reports.click_reports_column_option_settings_gear_button()
        self.reports.click_column_option("Status")
        self.reports.click_column_options_popup_cancel_button()

        # Verify reports table Status Column
        self.reports.verify_customers_tabel_column("Status")
    
    def test_09_verify_generate_report_page_ui(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33395350
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()
        self.reports.verify_page_title("Generate Report")

        #verify generate report page ui 
        self.reports.verify_report_category_dropdown_title()
        self.reports.verify_report_category_dropdown()
        self.reports.verify_report_type_dropdown_title()
        self.reports.verify_report_type_dropdown(False)
        self.reports.verify_report_name_title()
        self.reports.verify_report_name_field()
        self.reports.verify_device_group_title()
        # self.reports.verify_device_group_decription()
        self.reports.verify_select_device_group_button()
        self.reports.verify_schedule_time_option_title()
        self.reports.verify_schedule_email_option_title()
        self.reports.verify_generate_report_page_cancel_button()
        self.reports.verify_generate_report_page_generate_button()
    
    def test_10_verify_generate_report_category_dropdown(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33395352
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()

        #verify report category options
        expected_options=["Security","Jobs"]
        self.reports.click_report_category_dropdown()
        self.reports.verify_report_category_dropdown_options()
        assert expected_options == self.reports.get_generate_report_category_dropdown_options()

    @pytest.mark.parametrize('report_category', ["security"])
    def test_11_verify_generate_report_type_dropdown(self,report_category):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33395353
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()

        security_options=["Executive Summary","Executive Fleet Assessment Summary","Devices Assessed","Devices Not Assessed","Policy Items Assessed","Recommendations","Remediations"]
        self.reports.verify_report_type_dropdown(False)

        #select report category dropdown option
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option(report_category)
        
        #verify report type dropdown option
        self.reports.verify_report_type_dropdown(True)
        self.reports.click_report_type_dropdown()
        self.reports.verify_report_type_dropdown_options()
        assert security_options == self.reports.get_generate_report_type_dropdown_options()
    
    def test_12_verify_generate_report_view_sample_button(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33395355
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()

        self.reports.verify_report_view_sample_button("disabled")
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("executiveSummary")
        self.reports.verify_report_view_sample_button("enabled")
        self.reports.click_report_view_sample_button()
        
        #verify sample report page ui
        self.reports.verify_generate_sample_report_page()
        self.reports.verify_sample_report_page_title("Executive Summary")
        self.reports.click_generate_sample_report_page_cancel_button()
        #navigated back to generate reports page
        self.reports.verify_page_title("Generate Report")
        
    
    def test_13_verify_select_device_group_popup(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33395356
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33397983
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()

        #verify select device group popup ui
        self.reports.click_reports_select_device_group()
        self.reports.verify_reports_select_device_group_popup()
        self.reports.verify_reports_select_device_group_popup_title()
        self.reports.verify_reports_select_device_group_popup_description()
        self.reports.verify_reports_select_device_group_popup_cancel_button()
        self.reports.verify_reports_select_device_group_popup_select_button("disabled")

        #Verify cancel button functionality
        self.reports.click_reports_device_group_popup_cancel_button()
        #navigated back to generate reports page
        self.reports.verify_page_title("Generate Report")

        #Verify select button in popup
        self.reports.select_device_group("All")
        self.reports.verify_reports_select_device_group_popup()
        self.reports.verify_reports_select_device_group_popup_select_button("enabled")

    def test_14_verify_error_messages_generate_report_page(self):
        #
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()

        self.reports.click_generate_button()
        #verify report category dropdown warning message 
        self.reports.verify_report_category_warning_message()
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")

        #verify report type dropdown warning message 
        self.reports.verify_report_type_warning_message

        #verify warning message when name field is empty
        self.reports.verify_report_name_field_empty_warning_message()

        #verify device group name warning message
        self.reports.verify_device_group_warning_message()
        
        #verify warning message when name field is with minimum characters
        self.reports.enter_report_name("at")
        self.reports.verify_report_name_field_error_warning_message()       