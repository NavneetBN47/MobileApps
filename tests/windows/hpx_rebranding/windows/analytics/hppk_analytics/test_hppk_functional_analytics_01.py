import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_HPPK_Analytics(object):

    @pytest.mark.analytics
    def test_01_click_application_cancel_button_event_C52043375(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        self.fc.fd["hppk"].click_progkey_menucard_arrow_btn()
        self.fc.fd["hppk"].click_automation_radio_btn()

        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            #Application cancel button
            time.sleep(2)            
            self.fc.fd["hppk"].click_automation_dropbox_btn()
            self.fc.fd["hppk"].click_application_from_dropdown()
            self.fc.fd["hppk"].click_application_list_cancel_button()

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "AppCancelButton",
        "controlLabel": "AppCancelButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_02_click_website_cancel_button_event_C52043384(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            #Application cancel button
            time.sleep(2)            
            self.fc.fd["hppk"].click_automation_dropbox_btn()
            self.fc.fd["hppk"].click_website_from_dropdown()
            self.fc.fd["hppk"].click_website_cancel_button()

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "WebsiteCancelButton",
        "controlLabel": "WebsiteCancelButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_03_click_continue_button_add_application_event_C52043374(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        
        time.sleep(2)            
        self.fc.fd["hppk"].select_application_for_programable_key("Access","access_app")
        self.fc.fd["hppk"].click_add_application_continue_button()
        self.fc.fd["hppk"].select_application_for_programable_key("Calculator","calculator_app")
        self.fc.fd["hppk"].click_add_application_continue_button()
        self.fc.fd["hppk"].select_application_for_programable_key("Paint","paint_app")
        self.fc.fd["hppk"].click_add_application_continue_button()
        self.fc.fd["hppk"].select_application_for_programable_key("Clock","clock_app")
        self.fc.fd["hppk"].click_add_application_continue_button()
        self.fc.fd["hppk"].select_application_for_programable_key("Administrative Tools","automation_list_admin_tool_app")
        self.fc.fd["hppk"].click_add_application_continue_button()
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "AppContinueButton",
        "controlLabel": "AppContinueButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)

    @pytest.mark.analytics
    def test_04_click_delete_button_5_add_application_event_C52043381(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["hppk"].delete_application_list("delete_button_5")
            self.fc.fd["hppk"].select_application_for_programable_key("Administrative Tools","automation_list_admin_tool_app")
            self.fc.fd["hppk"].click_add_application_continue_button()

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "DeleteButton5",
        "controlLabel": "DeleteButton5",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)
        self.fc.fd["hppk"].delete_application_list("delete_button_5")

    @pytest.mark.analytics
    def test_05_click_delete_button_4_add_application_event_C52043380(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["hppk"].delete_application_list("delete_button_4")
            self.fc.fd["hppk"].select_application_for_programable_key("Clock","clock_app")
            self.fc.fd["hppk"].click_add_application_continue_button()

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "DeleteButton4",
        "controlLabel": "DeleteButton4",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)
        self.fc.fd["hppk"].delete_application_list("delete_button_4")

    @pytest.mark.analytics
    def test_06_click_delete_button_3_add_application_event_C52043378(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["hppk"].delete_application_list("delete_button_3")
            self.fc.fd["hppk"].select_application_for_programable_key("Paint","paint_app")
            self.fc.fd["hppk"].click_add_application_continue_button()

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "DeleteButton3",
        "controlLabel": "DeleteButton3",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)
        self.fc.fd["hppk"].delete_application_list("delete_button_3")

    @pytest.mark.analytics
    def test_07_click_delete_button_2_add_application_event_C52043377(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["hppk"].delete_application_list("delete_button_2")
            self.fc.fd["hppk"].select_application_for_programable_key("Calculator","calculator_app")
            self.fc.fd["hppk"].click_add_application_continue_button()

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "DeleteButton2",
        "controlLabel": "DeleteButton2",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)
        self.fc.fd["hppk"].delete_application_list("delete_button_2")

    @pytest.mark.analytics
    def test_08_click_delete_button_1_add_application_event_C52043376(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["hppk"].delete_application_list("delete_button_1")
            self.fc.fd["hppk"].select_application_for_programable_key("Access","access_app")
            self.fc.fd["hppk"].click_add_application_continue_button()

        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "DeleteButton1",
        "controlLabel": "DeleteButton1",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)
        self.fc.fd["hppk"].delete_application_list("delete_button_1")

    @pytest.mark.analytics
    def test_09_click_continue_button_add_website_event_C52043382(self):
        query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(2)            
            self.fc.fd["hppk"].select_website_for_programable_key("www.google.com")
            self.fc.fd["hppk"].click_add_website_continue_button()
            self.fc.fd["hppk"].delete_application_list("delete_button_1")
        serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/Progkey/DetailCard/"],
        "viewName": "DetailCard",
        "viewMode": "",
        "action": "OnClick",
        "controlName": "WebsiteContinueButton",
        "controlLabel": "WebsiteContinueButton",
        "serial_number": serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/hppk_filter.json", "hppk", 5)