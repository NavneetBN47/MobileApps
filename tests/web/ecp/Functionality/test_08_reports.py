import pytest
from MobileApps.libs.ma_misc import ma_misc
import random
pytest.app_info = "ECP"

#Generate test report name
report_name="auto_report"+str(random.randint(100,999))

#Generate test report name
auto_report_name="automation_report"+str(random.randint(1,10))

class Test_08_reports(object):

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
        return self.reports.verify_reports_table(auto_report_name)

    def test_01_verify_generate_report(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33395357        
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()
        self.reports.verify_page_title("Generate Report")
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("executiveSummary")
        self.reports.enter_report_name(report_name)
        self.reports.select_device_group("All")
        self.reports.click_select_device_group_select_button()
        self.reports.click_generate_button()
        #Two toast are present at same time, which is causing stale element reference
        self.reports.dismiss_toast()
        self.reports.dismiss_toast()
        assert True == self.reports.search_report(report_name)

    @pytest.mark.parametrize('search_string', ["Invalidreport", report_name])
    def test_02_verify_reports_search_functionality(self,search_string):
        #        
        self.reports.verify_reports_page()
        self.reports.search_report(search_string)

    def test_03_verify_reports_details_screen(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33405782       
        self.reports.verify_reports_page()
        self.reports.search_report(report_name)
        entry_detail = self.reports.get_reports_table_entry_details()
        self.reports.click_first_entry_link()
        assert entry_detail == self.reports.verify_report_details()

    def test_04_verify_edit_report_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33397988       
        self.reports.verify_reports_page()
        self.reports.search_report(report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Edit")
        self.reports.click_contextual_footer_continue_button()
        self.reports.verify_page_title("Edit Report")
        self.reports.verify_edit_report_save_button_status("disabled")
        self.reports.enter_report_name("update_"+report_name)
        self.reports.verify_edit_report_save_button_status("enabled")
        self.reports.click_edit_report_contextual_footer_save_button()
        self.reports.verify_edit_report_toast_message("update_"+report_name)

    def test_05_verify_delete_report_functionality(self):
        #         
        self.reports.verify_reports_page()
        self.reports.search_report("update_"+report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Delete")
        self.reports.click_contextual_footer_continue_button()
        self.reports.verify_delete_report_popup_title()
        self.reports.verify_delete_report_popup_descriptopn()
        self.reports.verify_delete_report_popup_cancel_button()
        self.reports.verify_delete_report_popup_delete_button()
        self.reports.click_delete_report_popup_delete_button()
        # Need to add toast verification step, but two toast message are present at same time.
        self.reports.dismiss_toast()
        assert False == self.reports.search_report(report_name)
    
    def test_06_verify_generate_report_page_cancel_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33397983       
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("executiveSummary")
        self.reports.enter_report_name(report_name)
        self.reports.select_device_group("All")
        self.reports.click_select_device_group_select_button()
        self.reports.click_generate_report_page_cancel_button()
        #Verify reports page is displayed
        self.reports.verify_reports_page(table_load=False)

        #search report name is not generated
        assert False == self.reports.search_report(report_name)

    def test_07_verify_edit_report_page_ui(self):
       #https://hp-testrail.external.hp.com/index.php?/cases/view/33397986       
        self.reports.verify_reports_page()

        #generating new report
        self.reports.click_reports_generate_button()
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("executiveSummary")
        self.reports.enter_report_name(report_name)
        self.reports.select_device_group("All")
        self.reports.click_select_device_group_select_button()
        self.reports.click_generate_button()
        self.reports.dismiss_toast()
        self.reports.dismiss_toast()

        self.reports.search_report(report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Edit")
        self.reports.click_contextual_footer_continue_button()

        #Verify edit report page ui
        self.reports.verify_edit_report_category_title()
        self.reports.verify_edit_report_category_type("Security")
        self.reports.verify_edit_report_type_title()
        self.reports.verify_edit_report_type("Executive Summary")
        self.reports.verify_edit_report_name_field_title()
        self.reports.verify_edit_report_name_field(report_name)
        self.reports.verify_edit_report_device_group_title()
        #have to verify device groups names
        self.reports.verify_edit_report_contextual_footer()
        self.reports.verify_edit_report_contextual_footer_save_button()
        self.reports.verify_edit_report_contextual_footer_cancel_button()

    def test_08_verify_edit_report_page_report_name_error_messages(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33397987       
        self.reports.verify_reports_page()
        self.reports.search_report(report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Edit")
        self.reports.click_contextual_footer_continue_button()
        self.reports.verify_edit_report_category_title()

        #verify warning message when name field is empty
        self.reports.clear_report_name_field()
        self.reports.verify_edit_report_name_field_empty_warning_message()

        #verify warning message when name field is with minimum characters
        self.reports.enter_report_name("at")
        self.reports.verify_edit_report_name_field_error_warning_message()
    
    def test_09_verify_edit_report_page_cancel_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33397988      
        self.reports.verify_reports_page()
        self.reports.search_report(report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Edit")
        self.reports.click_contextual_footer_continue_button()
        self.reports.verify_edit_report_category_title()
        self.reports.enter_report_name("update_"+report_name)
        self.reports.click_edit_report_contextual_footer_cancel_button()
        #Verify reports page is displayed
        self.reports.verify_reports_page(table_load=False)

        #search whether report name is not updated        
        assert False == self.reports.search_report("update_"+report_name)
        self.reports.click_search_clear_button()

        #delete generated report
        self.reports.search_report(report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Delete")
        self.reports.click_contextual_footer_continue_button()
        self.reports.click_delete_report_popup_delete_button()
        # Need to add toast verification step, but two toast message are present at same time.
        self.reports.dismiss_toast()
        assert False == self.reports.search_report(report_name)
    
    def test_10_verify_executive_summary_details_report_page(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33398286
        #generate executive summary report        
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("executiveSummary")
        self.reports.enter_report_name("executive_summary_"+report_name)
        self.reports.select_device_group("All")
        self.reports.click_select_device_group_select_button()
        self.reports.click_generate_button()
        #Two toast are present at same time, which is causing stale element reference
        self.reports.dismiss_toast()
        self.reports.dismiss_toast()
        assert True == self.reports.search_report("executive_summary_"+report_name)
        self.reports.click_search_clear_button()

        #navigate to reports details page
        self.reports.search_report("executive_summary_"+report_name)

        entry_detail = self.reports.get_reports_table_entry_details()
        self.reports.click_first_entry_link()
        assert entry_detail == self.reports.verify_report_details()
        assert self.customer == self.reports.get_report_details_page_customer_name()

        #verify Save as PDF button
        self.reports.verify_report_details_page_save_as_pdf_button()

        #verify_report_details_page_summary_card        
        self.reports.verify_report_details_page_device_assessment_summary_card_component()
        self.reports.verify_device_assessment_summary_card_assessed_device_status_title()
        self.reports.verify_device_assessment_summary_card_not_assessed_device_status_title()

        #Verify report_details_page_policy_items_assessed_card
        self.reports.verify_report_details_page_policy_items_assessed_card_component()
        self.reports.verify_policy_items_assessed_status_by_policy_items_title()
        self.reports.verify_policy_items_assessed_status_by_feature_category_title()

        #verify_report_details_page_risk_summary_card
        self.reports.verify_report_details_page_risk_summary_card_component()

        #verify_report_details_page_solutions_entitled_card
        self.reports.verify_report_details_page_solutions_entitled_card_component()
    
    def test_11_verify_executive_summary_details_report_page_card_expanded_collapsed(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33398286       
        self.reports.verify_reports_page()

        #navigate to reports details page
        self.reports.search_report("executive_summary_"+report_name)
        self.reports.click_first_entry_link()

        #Verify summary card can be expanded and collapsed
        self.reports.verify_report_details_page_summary_card_expanded()
        self.reports.click_report_details_page_summary_card()
        self.reports.verify_report_details_page_summary_card_expanded(expanded=False)
        self.reports.click_report_details_page_summary_card()
        self.reports.verify_report_details_page_summary_card_expanded()

        #Verify assessment summary card can be expanded and collapsed
        self.reports.verify_report_details_page_device_assessment_summary_card_expanded()
        self.reports.click_report_details_page_device_assessment_summary_card()
        self.reports.verify_report_details_page_device_assessment_summary_card_expanded(expanded=False)
        self.reports.click_report_details_page_device_assessment_summary_card()
        self.reports.verify_report_details_page_device_assessment_summary_card_expanded()

        # verify policy items assessed card can be expanded and collapsed
        self.reports.verify_report_details_page_policy_items_assessed_card_expanded()
        self.reports.click_report_details_page_policy_items_assessed_card()
        self.reports.verify_report_details_page_policy_items_assessed_card_expanded(expanded=False)
        self.reports.click_report_details_page_policy_items_assessed_card()
        self.reports.verify_report_details_page_policy_items_assessed_card_expanded()

        # verify risk summary card can be expanded and collapsed
        self.reports.verify_report_details_page_risk_summary_card_expanded()
        self.reports.click_report_details_page_risk_summary_card_card()
        self.reports.verify_report_details_page_risk_summary_card_expanded(expanded=False)
        self.reports.click_report_details_page_risk_summary_card_card()
        self.reports.verify_report_details_page_risk_summary_card_expanded()

        # verify solutions entitled summary card can be expanded and collapsed
        self.reports.verify_report_details_page_solutions_entitled_card_expanded()
        self.reports.click_report_details_page_solutions_entitled_card()
        self.reports.verify_report_details_page_solutions_entitled_card_expanded(expanded=False)
        self.reports.click_report_details_page_solutions_entitled_card()
        self.reports.verify_report_details_page_solutions_entitled_card_expanded()
        
        #delete generated report
        self.home.click_reports_menu_btn()
        self.reports.verify_reports_page()
        self.reports.search_report("executive_summary_"+report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Delete")
        self.reports.click_contextual_footer_continue_button()
        self.reports.click_delete_report_popup_delete_button()
        # Need to add toast verification step, but two toast message are present at same time.
        self.reports.dismiss_toast()
        assert False == self.reports.search_report("executive_summary_"+report_name)

    def test_12_verify_executive_fleet_assessment_summary_details_report_page(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33398287
        #generate executive summary report       
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("executiveAssessmentSummary")
        self.reports.enter_report_name("fleet_summary_"+report_name)
        self.reports.select_device_group("All")
        self.reports.click_select_device_group_select_button()
        self.reports.click_generate_button()
        #Two toast are present at same time, which is causing stale element reference
        self.reports.dismiss_toast()
        self.reports.dismiss_toast()
        assert True == self.reports.search_report("fleet_summary_"+report_name)
        self.reports.click_search_clear_button()

        #navigate to reports details page
        self.reports.search_report("fleet_summary_"+report_name)

        entry_detail = self.reports.get_reports_table_entry_details()
        self.reports.click_first_entry_link()
        assert entry_detail == self.reports.verify_report_details()
        assert self.customer == self.reports.get_report_details_page_customer_name()

        #verify Save as PDF button
        self.reports.verify_report_details_page_save_as_pdf_button()

        #verify_report_details_page_summary_card        
        self.reports.verify_report_details_page_device_assessment_summary_card_component()

        #Verify assessment summary card can be expanded and collapsed
        self.reports.verify_report_details_page_device_assessment_summary_card_expanded()
        self.reports.click_report_details_page_device_assessment_summary_card()
        self.reports.verify_report_details_page_device_assessment_summary_card_expanded(expanded=False)
        self.reports.click_report_details_page_device_assessment_summary_card()
        self.reports.verify_report_details_page_device_assessment_summary_card_expanded()
    
        #delete generated report
        self.home.click_reports_menu_btn()
        self.reports.verify_reports_page()
        self.reports.search_report("fleet_summary_"+report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Delete")
        self.reports.click_contextual_footer_continue_button()
        self.reports.click_delete_report_popup_delete_button()
        # Need to add toast verification step, but two toast message are present at same time.
        self.reports.dismiss_toast()
        assert False == self.reports.search_report("fleet_summary_"+report_name)
    
    def test_13_verify_devices_assessed_details_report_page(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33398288
        #generate executive summary report        
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("devicesAssessmentSummary")
        self.reports.enter_report_name("assessed_"+report_name)
        self.reports.select_device_group("All")
        self.reports.click_select_device_group_select_button()
        self.reports.click_generate_button()
        #Two toast are present at same time, which is causing stale element reference
        self.reports.dismiss_toast()
        self.reports.dismiss_toast()
        assert True == self.reports.search_report("assessed_"+report_name)
        self.reports.click_search_clear_button()

        #navigate to reports details page
        self.reports.search_report("assessed_"+report_name)

        entry_detail = self.reports.get_reports_table_entry_details()
        self.reports.click_first_entry_link()
        assert entry_detail == self.reports.verify_report_details()
        assert self.customer == self.reports.get_report_details_page_customer_name()

        #verify Save as PDF & XLSX button
        self.reports.verify_report_details_page_save_as_pdf_button()
        self.reports.verify_report_details_page_save_as_xlsx_button()

        #verify devices assessment summary list table 
        self.reports.verify_reports_details_page_assessment_status_list_table()
        self.reports.verify_reports_details_page_search_field()
        self.reports.verify_reports_details_page_filter_button()
        self.reports.verify_reports_details_page_column_option_button()
        self.reports.verify_page_size_btn()
        self.reports.verify_page_nav()

        #delete generated report
        self.home.click_reports_menu_btn()
        self.reports.verify_reports_page()
        self.reports.search_report("assessed_"+report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Delete")
        self.reports.click_contextual_footer_continue_button()
        self.reports.click_delete_report_popup_delete_button()
        # Need to add toast verification step, but two toast message are present at same time.
        self.reports.dismiss_toast()
        assert False == self.reports.search_report("assessed_"+report_name)

    def test_14_verify_devices_not_assessed_details_report_page(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33398289
        #generate executive summary report       
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("devicesNotAssessed")
        self.reports.enter_report_name("not_assessed_"+report_name)
        self.reports.select_device_group("All")
        self.reports.click_select_device_group_select_button()
        self.reports.click_generate_button()
        #Two toast are present at same time, which is causing stale element reference
        self.reports.dismiss_toast()
        self.reports.dismiss_toast()
        assert True == self.reports.search_report("not_assessed_"+report_name)
        self.reports.click_search_clear_button()

        #navigate to reports details page
        self.reports.search_report("not_assessed_"+report_name)

        entry_detail = self.reports.get_reports_table_entry_details()
        self.reports.click_first_entry_link()
        assert entry_detail == self.reports.verify_report_details()
        assert self.customer == self.reports.get_report_details_page_customer_name()

        #verify Save as PDF & XLSX button
        self.reports.verify_report_details_page_save_as_pdf_button()
        self.reports.verify_report_details_page_save_as_xlsx_button()

        #verify devices not assessed summary list table 
        self.reports.verify_reports_details_page_assessment_status_list_table()
        self.reports.verify_reports_details_page_search_field()
        self.reports.verify_reports_details_page_filter_button()
        self.reports.verify_reports_details_page_column_option_button()
        self.reports.verify_page_size_btn()
        self.reports.verify_page_nav()

        #delete generated report
        self.home.click_reports_menu_btn()
        self.reports.verify_reports_page()
        self.reports.search_report("not_assessed_"+report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Delete")
        self.reports.click_contextual_footer_continue_button()
        self.reports.click_delete_report_popup_delete_button()
        # Need to add toast verification step, but two toast message are present at same time.
        self.reports.dismiss_toast()
        assert False == self.reports.search_report("not_assessed_"+report_name)

    def test_15_verify_policy_items_assessed_details_report_page(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33398290
        #generate executive summary report       
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("policyItemsAssessed")
        self.reports.enter_report_name("policy_assessed_"+report_name)
        self.reports.select_device_group("All")
        self.reports.click_select_device_group_select_button()
        self.reports.click_generate_button()
        #Two toast are present at same time, which is causing stale element reference
        self.reports.dismiss_toast()
        self.reports.dismiss_toast()
        assert True == self.reports.search_report("policy_assessed_"+report_name)
        self.reports.click_search_clear_button()

        #navigate to reports details page
        self.reports.search_report("policy_assessed_"+report_name)

        entry_detail = self.reports.get_reports_table_entry_details()
        self.reports.click_first_entry_link()
        assert entry_detail == self.reports.verify_report_details()
        assert self.customer == self.reports.get_report_details_page_customer_name()

        #verify Save as PDF & XLSX button
        self.reports.verify_report_details_page_save_as_pdf_button()
        self.reports.verify_report_details_page_save_as_xlsx_button()

        #verify policy assessed count card
        self.reports.verify_policy_items_assessed_count_title()
        
        #verify policy items assessed card can be expanded and collapsed
        self.reports.verify_report_details_page_policy_items_assessed_count_expanded()
        self.reports.click_report_details_page_policy_items_assessed_count_card()
        self.reports.verify_report_details_page_policy_items_assessed_count_expanded(expanded=False)
        self.reports.click_report_details_page_policy_items_assessed_count_card()
        self.reports.verify_report_details_page_policy_items_assessed_count_expanded()

        #delete generated report
        self.home.click_reports_menu_btn()
        self.reports.verify_reports_page()
        self.reports.search_report("policy_assessed_"+report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Delete")
        self.reports.click_contextual_footer_continue_button()
        self.reports.click_delete_report_popup_delete_button()
        # Need to add toast verification step, but two toast message are present at same time.
        self.reports.dismiss_toast()
        assert False == self.reports.search_report("policy_assessed_"+report_name)
    
    def test_16_verify_recommendation_summary_details_report_page(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33398291
        #generate executive summary report         
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("devicesRecommendationSummary")
        self.reports.enter_report_name("recommendation_"+report_name)
        self.reports.select_device_group("All")
        self.reports.click_select_device_group_select_button()
        self.reports.click_generate_button()
        #Two toast are present at same time, which is causing stale element reference
        self.reports.dismiss_toast()
        self.reports.dismiss_toast()
        assert True == self.reports.search_report("recommendation_"+report_name)
        self.reports.click_search_clear_button()

        #navigate to reports details page
        self.reports.search_report("recommendation_"+report_name)

        entry_detail = self.reports.get_reports_table_entry_details()
        self.reports.click_first_entry_link()
        assert entry_detail == self.reports.verify_report_details()
        assert self.customer == self.reports.get_report_details_page_customer_name()

        #verify Save as PDF & XLSX button
        self.reports.verify_report_details_page_save_as_pdf_button()
        self.reports.verify_report_details_page_save_as_xlsx_button()

        #verify recommendation_summary_ table 
        self.reports.verify_reports_details_page_assessment_status_list_table()
        self.reports.verify_reports_details_page_search_field()
        self.reports.verify_reports_details_page_filter_button()
        self.reports.verify_reports_details_page_column_option_button()
        self.reports.verify_page_size_btn()
        self.reports.verify_page_nav()

        #delete generated report
        self.home.click_reports_menu_btn()
        self.reports.verify_reports_page()
        self.reports.search_report("recommendation_"+report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Delete")
        self.reports.click_contextual_footer_continue_button()
        self.reports.click_delete_report_popup_delete_button()
        # Need to add toast verification step, but two toast message are present at same time.
        self.reports.dismiss_toast()
        assert False == self.reports.search_report("recommendation_"+report_name)
    
    def test_17_verify_remediation_summary_details_report_page(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/33398292
        #generate executive summary report        
        self.reports.verify_reports_page()
        self.reports.click_reports_generate_button()
        self.reports.click_report_category_dropdown()
        self.reports.select_report_category_option("security")
        self.reports.click_report_type_dropdown()
        self.reports.select_report_type_option("devicesRemediationSummary")
        self.reports.enter_report_name("remediation_"+report_name)
        self.reports.select_device_group("All")
        self.reports.click_select_device_group_select_button()
        self.reports.click_generate_button()
        #Two toast are present at same time, which is causing stale element reference
        self.reports.dismiss_toast()
        self.reports.dismiss_toast()
        assert True == self.reports.search_report("remediation_"+report_name)
        self.reports.click_search_clear_button()

        #navigate to reports details page
        self.reports.search_report("remediation_"+report_name)

        entry_detail = self.reports.get_reports_table_entry_details()
        self.reports.click_first_entry_link()
        assert entry_detail == self.reports.verify_report_details()
        assert self.customer == self.reports.get_report_details_page_customer_name()

        #verify Save as PDF & XLSX button
        self.reports.verify_report_details_page_save_as_pdf_button()
        self.reports.verify_report_details_page_save_as_xlsx_button()

        #verify remediation table 
        self.reports.verify_reports_details_page_assessment_status_list_table()
        self.reports.verify_reports_details_page_search_field()
        self.reports.verify_reports_details_page_filter_button()
        self.reports.verify_reports_details_page_column_option_button()
        self.reports.verify_page_size_btn()
        self.reports.verify_page_nav()

        #delete generated report
        self.home.click_reports_menu_btn()
        self.reports.verify_reports_page()
        self.reports.search_report("remediation_"+report_name)
        self.reports.click_reports_checkbox()
        self.reports.click_contextual_footer_select_action_dropdown()
        self.reports.select_contextual_footer_select_action_dropdown_option("Delete")
        self.reports.click_contextual_footer_continue_button()
        self.reports.click_delete_report_popup_delete_button()
        # Need to add toast verification step, but two toast message are present at same time.
        self.reports.dismiss_toast()
        assert False == self.reports.search_report("remediation_"+report_name)