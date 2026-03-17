import time
import pytest
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_AIC_Analytics(object):

    
    def analytics_events_test(self,viewName, action,controlName,query_start_time):
        custom_filters = {    
        "version": "2.0.0",   
        "viewHierarchy": ["base:/", f"mfe:/AIAgent/{viewName}/"],
        "viewName": viewName,
        "action": action,
        "viewModule": "AIAgent",
        "controlName": controlName,
        "controlLabel": controlName,
        "serial_number": self.fc.get_windows_serial_number()
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/aic_filter.json", custom_filters)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/aic_filter.json", "ai_agent",5)


    @pytest.mark.analytics
    def test_01_user_clicks_on_copy_button_C60618687(self):
        
        self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(3)
        self.fc.fd["aic"].click_wheel_of_fun_item_on_home_page("wheel_of_fun_item_on_home_page")
        time.sleep(10)
        # self.fc.fd["aic"].scroll_to_element("copy_button")
        self.fc.fd['aic'].scroll_up_down(direction="down", distance=1)
        time.sleep(10)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(6):
            time.sleep(5)
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            time.sleep(10)
            self.fc.fd["aic"].click_aic_window(5)
            self.fc.fd["aic"].click_copy_button()
            time.sleep(5)
        self.fc.close_app()
        self.analytics_events_test("AIAgentResultScreen","OnClick", "CopyButton",query_start_time)

    @pytest.mark.analytics
    def test_02_user_collapsed_the_response_card_C60618685(self):
        time.sleep(10)
        self.fc.launch_app_without_fuf()
        self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(3)
        self.fc.fd["aic"].click_wheel_of_fun_item_on_home_page("wheel_of_fun_item_on_home_page")
        time.sleep(15)
        self.fc.fd["aic"].focus_collapse_expand_chevron_lthree_page()
        time.sleep(5)
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(10):
            time.sleep(3)
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["aic"].click_collapse_expand_chevron_lthree_page()
        self.fc.close_app()
        self.analytics_events_test("AIAgentResultScreen","OnCollapse", "AIResponseCard",pytest.query_start_time)

    @pytest.mark.analytics
    def test_03_user_expands_the_response_card_C60618686(self):
        time.sleep(10)
        self.analytics_events_test("AIAgentResultScreen","OnExpand", "AIResponseCard",pytest.query_start_time)

    @pytest.mark.analytics   
    def test_04_user_click_on_wheel_of_fun_item_on_results_page_C60618684(self):
        self.fc.launch_app_without_fuf()
        self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(3)
        self.fc.fd["aic"].click_wheel_of_fun_item_on_home_page("wheel_of_fun_item_on_home_page")
        time.sleep(10)
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
        self.fc.fd["aic"].click_aic_window(7)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):         
            time.sleep(10)
            self.fc.fd["aic"].click_wheel_of_fun_item_on_result_page("wheel_of_fun_item_on_result_page")
            time.sleep(10)
        self.fc.close_app()
        self.analytics_events_test("AIAgentResultScreen","OnClick", "WheelOfFun",query_start_time)

    @pytest.mark.analytics
    def test_05_user_give_some_prompt_and_click_on_primary_arrow_button_of_result_page_C60618688(self):
        self.fc.launch_app_without_fuf()
        self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
        time.sleep(5)
        self.fc.fd["aic"].click_aic_window(3)
        self.fc.fd["aic"].click_wheel_of_fun_item_on_home_page("wheel_of_fun_item_on_home_page")
        time.sleep(10)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["aic"].click_aic_window(7)
            self.fc.fd["aic"].enter_text_in_search_box("Hello")
            time.sleep(5)
            self.fc.fd["aic"].click_ask_me_anything_searchbox_arrow_button_ltwo()
            time.sleep(5)
        self.fc.close_app()
        self.analytics_events_test("AIAgentResultScreen","OnClick", "PrimaryButton", query_start_time)             