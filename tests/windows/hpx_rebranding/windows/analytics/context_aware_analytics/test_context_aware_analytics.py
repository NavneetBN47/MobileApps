import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Context_Aware_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app(False)

    #This test case will fail due to https://hp-jira.external.hp.com/browse/HPXWC-30395
    @pytest.mark.analytics
    def test_01_click_next_arrow_button_event_C52044218(self):
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(10)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()    
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Calculator","calculator_app_on_install_modal")
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Access", "access_app_on_install_modal")
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Clock", "clock_app_on_install_modal")
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Copilot", "copilot_app_on_install_modal")
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Excel", "excel_app_on_install_modal")
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Paint", "paint_app_on_install_modal")
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Camera", "camera_app_on_install_modal")
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Notepad", "notepad_app_on_install_modal")
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("News", "news_app_on_install_modal")
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Photos", "photos_app_on_install_modal")
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("Journal", "journal_app_on_install_modal")
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["context_aware"].click_next_button_arrow_for_carousel_item()

        pytest.serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewName": "Carousel", 
        "action": "OnClick",
        "controlName": "NextButton",
        "controlLabel": "NextButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", "context_aware", 5)
        self.fc.fd["context_aware"].delete_app("notepad_app_carousel")
        self.fc.fd["context_aware"].delete_app("news_app_carousel")
        self.fc.fd["context_aware"].delete_app("photos_app_carousel")
        self.fc.fd["context_aware"].delete_app("access_app_carousel")
        self.fc.fd["context_aware"].delete_app("clock_app_carousel")
        self.fc.fd["context_aware"].delete_app("paint_app_carousel")
        self.fc.fd["context_aware"].delete_app("excel_app_carousel")
        self.fc.fd["context_aware"].delete_app("camera_app_carousel")
        self.fc.fd["context_aware"].delete_app("copilot_app_carousel")
        self.fc.fd["context_aware"].delete_app("journal_app_carousel")

    @pytest.mark.analytics
    def test_02_click_on_all_apps_button_event_C52044189(self):
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            time.sleep(3)
            self.fc.fd["context_aware"].click_all_application_button_ltwo_page()
            self.fc.fd["context_aware"].click_calculator_app_carousel()
            self.fc.fd["context_aware"].click_add_button_ltwo_page()
            self.fc.fd["context_aware"].click_add_app_cancel_button_ltwo_page()

        pytest.serial_number = self.fc.get_windows_serial_number()
        custom_filter = {
        "version": "2.0.0",
        "viewName": "Carousel", 
        "action": "OnClick",
        "controlName": "AllAppsButton",
        "controlLabel": "AllAppsButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", "context_aware", 5)

    @pytest.mark.analytics
    def test_03_click_first_carousel_item_button_event_C52044217(self):
        custom_filter = {    
        "version": "2.0.0",
        "viewName": "Carousel", 
        "action": "OnClick",
        "controlName": "CarouselItem0",
        "controlLabel": "CarouselItem0",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", "context_aware", 5)

    @pytest.mark.analytics
    def test_04_click_add_button_event_C52044219(self):
        custom_filter = {    
        "version": "2.0.0",
        "viewName": "Carousel", 
        "action": "OnClick",
        "controlName": "AddButton",
        "controlLabel": "AddButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", "context_aware", 5)

    @pytest.mark.analytics
    def test_05_click_cancel_event_C52044291(self):
        custom_filter = {    
        "version": "2.0.0",
        "viewName": "InstalledAppsModal", 
        "action": "OnClick",
        "controlName": "CancelButton",
        "controlLabel": "CancelButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", "context_aware", 5)

    @pytest.mark.analytics
    def test_06_click_continue_event_C52044220(self):
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            # using only letter "C" due to : https://hp-jira.external.hp.com/browse/HPXWC-30395 will spell "calculator" once bug is resolved
            self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("C", "calculator_app_on_install_modal")
            time.sleep(3)
        pytest.serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewName": "InstalledAppsModal", 
        "action": "OnClick",
        "controlName": "ContinueButton",
        "controlLabel": "ContinueButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", "context_aware", 5)
   
    @pytest.mark.analytics
    def test_07_click_delete_button_event_C52044292(self):
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):         
            time.sleep(3)
            self.fc.fd["context_aware"].click_delete_profile_button()            
            self.fc.fd["context_aware"].click_add_app_cancel_button_ltwo_page()
            
        custom_filter = {    
        "version": "2.0.0",
        "viewName": "Carousel", 
        "action": "OnClick",
        "controlName": "DeleteProfileButton",
        "controlLabel": "DeleteProfileButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", "context_aware", 5)

    def test_08_click_do_not_show_checkbox_button_event_C52044293(self):
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        self.fc.fd["context_aware"].click_delete_profile_button()
        for _ in range(5):            
            self.fc.fd["context_aware"].click_do_not_show_again_check_box()
        custom_filter = {    
        "version": "2.0.0",
        "viewName": "DeleteProfileModal", 
        "action": "OnChange",
        "controlName": "ConfirmationCheckbox",
        "controlLabel": "ConfirmationCheckbox",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", "context_aware", 5)
        if self.fc.fd["context_aware"].verify_do_not_show_again_check_box_state() == "1":
            self.fc.fd["context_aware"].click_do_not_show_again_check_box()
        self.fc.fd["context_aware"].click_add_app_cancel_button_ltwo_page() 

    @pytest.mark.analytics
    def test_09_click_delete_profile_continue_event_C52044294(self):
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("C", "calculator_app_on_install_modal")
            self.fc.fd["context_aware"].click_delete_profile_button()
            self.fc.fd["context_aware"].click_add_app_continue_button_ltwo_page()
            time.sleep(3)

        pytest.serial_number = self.fc.get_windows_serial_number()
        custom_filter = {    
        "version": "2.0.0",
        "viewName": "DeleteProfileModal", 
        "action": "OnClick",
        "controlName": "ContinueButton",
        "controlLabel": "ContinueButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", "context_aware", 5)

    def test_10_click_delete_profile_cancel_button_event_C52044296(self):
        self.fc.fd["context_aware"].enter_app_name_in_add_app_search_bar_ltwo_page("C", "calculator_app_on_install_modal")    
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()
        for _ in range(5):
            self.fc.fd["context_aware"].click_delete_profile_button()
            self.fc.fd["context_aware"].click_add_app_cancel_button_ltwo_page()
        custom_filter = {    
        "version": "2.0.0",
        "viewName": "DeleteProfileModal",
        "action": "OnClick",
        "controlName": "CancelButton",
        "controlLabel": "CancelButton",
        "serial_number": pytest.serial_number
        }
        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/context_aware_filter.json", "context_aware", 5)     