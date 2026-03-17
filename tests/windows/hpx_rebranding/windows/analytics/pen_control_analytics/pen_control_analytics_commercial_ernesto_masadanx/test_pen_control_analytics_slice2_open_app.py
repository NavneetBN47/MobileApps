import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Pen_Control_Slice2_Apps_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    @pytest.mark.analytics
    def test_01_pen_control_apps_click_on_change_to_open_app_button_C52098422(self):
        if "Maximize HP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(3)
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_pen_card()
        time.sleep(10)
        self.fc.fd["pen_control"].click_radial_menu_button()
        time.sleep(3)        
        self.fc.fd["pen_control"].click_radial_slice2_button()      
        time.sleep(3)
        self.fc.fd["pen_control"].click_productivity_arrow_icon()
        time.sleep(3)
        self.fc.fd["pen_control"].click_pen_arrow_icon()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        time.sleep(3)
        self.fc.fd["pen_control"].click_radial_slice2_productivity_show_more_button()
        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()

        # cycle through all options five times ending on first option
        for _ in range(5): 
            self.fc.fd["pen_control"].click_customize_button_open_app_text()
            time.sleep(3)
            self.fc.fd["pen_control"].click_cancel_button()
            time.sleep(3)
            self.fc.fd["pen_control"].click_change_app_to_open_btn_slice2()
            time.sleep(3)
            self.fc.fd["pen_control"].click_cancel_button()
            time.sleep(3)
            self.fc.fd["pen_control"].click_customize_button_email_text()
            time.sleep(3)
        # Get the current serial number for an open search query.
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice2/"],
        "viewName": "Slice2", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "ChangeAppToOpenButton",
        "controlLabel": "ChangeAppToOpenButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)