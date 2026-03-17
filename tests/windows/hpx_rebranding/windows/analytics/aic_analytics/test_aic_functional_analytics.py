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
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/aic_filter.json", "ai_agent", 5)

    
    @pytest.mark.analytics
    def test_01_user_give_some_prompt_and_click_on_primary_arrow_button_of_home_page_C60618666(self):
        time.sleep(10)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.launch_app_without_fuf()
            self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
            self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
            time.sleep(5)
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            time.sleep(5)
            self.fc.fd["aic"].click_aic_window(3)
            time.sleep(5)
            self.fc.fd["aic"].enter_hello_in_search_box("Hello")
            time.sleep(5)
            self.fc.fd["aic"].click_ask_me_anything_searchbox_arrow_button_ltwo()
            time.sleep(3)
            self.fc.close_app()
        self.analytics_events_test("AIAgentRootScreen","OnClick", "PrimaryButton",query_start_time)     

    @pytest.mark.analytics
    def test_02_user_click_on_wheel_of_fun_item_on_home_page_C60618682(self):
        time.sleep(10)
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.launch_app_without_fuf()
            self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
            self.fc.fd["devicesMFE"].click_hpai_assistant_button_on_header()
            time.sleep(5)
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            self.fc.fd["devicesMFE"].maximize_app() # Application loses focus
            time.sleep(5)
            self.fc.fd["aic"].click_aic_window(3)
            time.sleep(5)
            self.fc.fd["aic"].click_wheel_of_fun_item_on_home_page("wheel_of_fun_item_on_home_page")
            time.sleep(10)        
            self.fc.close_app()
        self.analytics_events_test("AIAgentRootScreen","OnClick", "WheelOfFun",query_start_time)