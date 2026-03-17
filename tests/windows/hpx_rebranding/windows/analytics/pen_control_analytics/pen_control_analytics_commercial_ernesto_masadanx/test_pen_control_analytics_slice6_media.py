import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from datetime import datetime, timezone
from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()

class Test_Suite_Pen_Control_Slice6_Media_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    @pytest.mark.analytics
    def test_01_pen_control_media_playpause_radio_analytics_C52120809(self):
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(3)
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_pen_card()
        time.sleep(10)

        self.fc.fd["pen_control"].click_radial_menu_button()
        time.sleep(3)
        self.fc.fd["pen_control"].click_radial_slice6_button()
        time.sleep(3)

        #select the universal radio option under productivity to clear any previous setting before test
        self.fc.fd["pen_control"].click_radial_slice6_productivity_universal_radio_button()
        time.sleep(3)
        self.fc.fd["pen_control"].click_productivity_arrow_icon()
        time.sleep(3)
        self.fc.fd["pen_control"].click_pen_arrow_icon()
        time.sleep(3)
        self.fc.fd["pen_control"].click_apps_arrow_icon()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)
        self.fc.fd["pen_control"].click_radial_slice6_productivity_show_more_button()
        time.sleep(5)
        
        # Get the current time as the starting time for an open search query.
        pytest.query_start_time = datetime.now(timezone.utc).isoformat()

        # cycle through all options five times ending on first option
        for _ in range(5): 
            self.fc.fd["pen_control"].click_radial_slice6_media_mute_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_media_volume_down_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_media_volume_up_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_media_previous_track_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_media_next_track_radio_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_radial_slice6_media_playpause_radio_button()
            time.sleep(1)

        # Get the current serial number for an open search query.
        pytest.serial_number = self.fc.get_windows_serial_number()

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "MediacontrolPlayPause",
        "controlLabel": "MediacontrolPlayPause",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_02_pen_control_media_next_track_radio_analytics_C52121040(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "MediacontrolNexttrack",
        "controlLabel": "MediacontrolNexttrack",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_03_pen_control_media_previous_track_radio_analytics_C52121041(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "MediacontrolPrevioustrack",
        "controlLabel": "MediacontrolPrevioustrack",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_04_pen_control_media_volume_up_radio_analytics_C52121042(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "MediacontrolVolumeup",
        "controlLabel": "MediacontrolVolumeup",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)


    @pytest.mark.analytics
    def test_05_pen_control_media_volume_down_radio_analytics_C52121043(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "MediacontrolVolumedown",
        "controlLabel": "MediacontrolVolumedown",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)

    @pytest.mark.analytics
    def test_06_pen_control_media_mute_audio_radio_analytics_C52121044(self):

        custom_filter = {
        "version": "2.0.0",
        "viewHierarchy": ["base:/", "mfe:/PcPencontrol/Slice6/"],
        "viewName": "Slice6", 
        "viewMode": "",
        "viewModule": "PcPencontrol",
        "action": "OnClick", 
        "actionDetail": "",
        "actionAuxParams": "",
        "controlName": "MediacontrolMuteaudio",
        "controlLabel": "MediacontrolMuteaudio",
        "controlAuxParams": "",
        "serial_number": pytest.serial_number
        }

        analytics_test.custom_filter_json_file("resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", custom_filter)
        analytics_test.execute_analytics_test_and_validate_result(pytest.query_start_time, "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json", "pen_control", 5)