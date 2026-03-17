import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest


pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Wellbeing_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()


    def test_01_check_restore_default_button_on_wellbeing_analytics_C52047677(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)
        # verify restore default button is displayed
        assert self.fc.fd["wellbeing"].verify_restore_default_button_show_up(), "Restore default button is not displayed"
        time.sleep(2)


        # Get the current time as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        time.sleep(3)

        # Click restore default button 5 times
        for _ in range(5):
            self.fc.fd["wellbeing"].click_restore_default_button()
            time.sleep(3)
        
        serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "viewName": "Wellbeing", 
        "action": "OnClick", 
        "controlName": "RestoreDefaultButton",
        "controlAuxParams": "",
        "serial_number": serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/wellbeing_filter.json", custom_filter)

        analytics_test.execute_analytics_test_and_validate_result(query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/wellbeing_filter.json", "wellbeing", 5)
