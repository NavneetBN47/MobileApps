from MobileApps.libs.flows.windows.hpx_rebranding.utility.rebrand_analytics_test import RebrandAnalyticsTest
from datetime import datetime, timezone
import time
import pytest
import logging

pytest.app_info = "HPX"
analytics_test = RebrandAnalyticsTest()
json_file = "resources/test_data/hpx_rebranding/analytics_opensearch_filter/pen_control_filter.json"

@pytest.mark.usefixtures("class_setup_fixture")
class Test_Suite_Pen_Control_Analytics(object):

    @pytest.fixture(autouse=True)
    # Must Run on Machu13x with Roo connected for one step inking to work
    def setup(self):
        # Ensure each test starts on the "My Pen" page, if not, navigate to the page before each test
        self.fc.check_and_navigate_to_my_pen_page()

        # Get the current time before each test as the starting time for an open search query.
        query_start_time = datetime.now(timezone.utc).isoformat()
        serial_number = self.fc.get_windows_serial_number()
        logging.info(f"Query Start time is: {query_start_time}")
        yield query_start_time, serial_number

    def create_custom_filter_and_verify_analytics(self, serial_number, view_name, view_module, action, control_name, query_start_time):
        custom_filter = analytics_test.create_custom_filter(serial_number, view_name, view_module, action, control_name)
        analytics_test.verify_analytics(json_file, custom_filter,  query_start_time, "pen_control", 5)

    @pytest.mark.analytics
    def test_01_pen_control_click_redial_menu_analytics_C52080019(self,setup):
        query_start_time, serial_number = setup
        for _ in range(5):
            self.fc.fd["pen_control"].click_radial_menu_button()
            time.sleep(1)
            self.fc.swipe_to_top()
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.create_custom_filter_and_verify_analytics(serial_number,"PencontrolHome",  "RootPencontrol", "OnCardClick","RadialMenuCard", query_start_time)

    @pytest.mark.analytics
    def test_02_pen_control_click_external_display_menu_analytics_C52080021(self,setup):
        query_start_time, serial_number = setup
        for _ in range(5):
            self.fc.fd["pen_control"].swipe_down_to_external_display_card()
            self.fc.fd["pen_control"].click_external_display_card()
            time.sleep(1)
            self.fc.swipe_to_top()
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.fc.swipe_to_top()
        self.create_custom_filter_and_verify_analytics(serial_number,"PencontrolHome",  "RootPencontrol", "OnCardClick","ExternalDisplayCard", query_start_time)

    @pytest.mark.analytics
    def test_03_pen_control_click_sensitivity_card_menu_analytics_C52080023(self, setup):
        query_start_time, serial_number = setup
        for _ in range(5):
            self.fc.fd["pen_control"].swipe_down_to_pen_sensitivity_card()
            self.fc.fd["pen_control"].click_pen_sensitivity_card()
            time.sleep(1)
            self.fc.swipe_window(direction="up", distance=10)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.fc.swipe_to_top()
        self.create_custom_filter_and_verify_analytics(serial_number,"PencontrolHome",  "RootPencontrol", "OnCardClick","PenSensitivityCard", query_start_time)

    @pytest.mark.analytics
    def test_04_pen_control_click_customize_buttons_analytics_C52080009(self,setup):
        query_start_time, serial_number = setup
        for _ in range(5):
            self.fc.fd["pen_control"].click_customize_buttons()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.create_custom_filter_and_verify_analytics(serial_number,"PencontrolHome",  "RootPencontrol", "OnCardClick","CustomizeButtonCard", query_start_time)

    @pytest.mark.analytics
    def test_05_pen_control_click_restore_defaults_analytics_C52080036(self,  setup):
        query_start_time, serial_number = setup
        self.fc.fd["pen_control"].swipe_down_to_restore_default_lone_button()
        for _ in range(5):
            self.fc.fd["pen_control"].click_restore_default_button_lone_page()
            time.sleep(1)
            self.fc.fd["pen_control"].click_restore_default_continue_button_lone_page()
            time.sleep(1)
        self.fc.swipe_to_top()
        self.create_custom_filter_and_verify_analytics(serial_number,"PencontrolHome",  "RootPencontrol", "OnClick", "RestoreDefaultsButton", query_start_time)

    @pytest.mark.analytics
    def test_06_pen_control_click_restore_defaults_customize_button_analytics_C52081562(self,setup):
        query_start_time, serial_number = setup
        self.fc.fd["pen_control"].click_customize_buttons()
        for _ in range(5):
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_customize_buttons_restore_default_continue_button()
            time.sleep(1)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.create_custom_filter_and_verify_analytics(serial_number,"Customizebuttons",  "PcPencontrol", "OnClick", "RestoreDefaultsButton", query_start_time)

    @pytest.mark.analytics
    def test_07_pen_control_click_restore_defaults_radial_menu_analytics_C52081563(self,setup):
        query_start_time, serial_number = setup
        self.fc.fd["pen_control"].click_radial_menu_button()
        for _ in range(5):
            self.fc.fd["pen_control"].click_restore_default_radial_menu_ltwo_page()
            time.sleep(1)
            self.fc.fd["pen_control"].click_restore_default_continue_radial_menu_ltwo_page()
            time.sleep(1)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.create_custom_filter_and_verify_analytics(serial_number,"Radialmenu",  "PcPencontrol", "OnClick", "RestoreDefaultsButton", query_start_time)

    @pytest.mark.analytics
    def test_08_pen_control_click_restore_defaults_pen_sensitivity_analytics_C52081598(self,setup):
        query_start_time, serial_number = setup
        self.fc.fd["pen_control"].swipe_down_to_pen_sensitivity_card()
        self.fc.fd["pen_control"].click_pen_sensitivity_card()
        for _ in range(5):
            self.fc.fd["pen_control"].click_pen_sensitivity_restore_defaults_button()
            time.sleep(1)
            self.fc.fd["pen_control"].click_restore_default_continue_pen_sensitivity_ltwo_page()
            time.sleep(1)
        self.fc.swipe_to_top()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.create_custom_filter_and_verify_analytics(serial_number,"Pensensitivity",  "PcPencontrol", "OnClick", "RestoreDefaultsButton", query_start_time)
        
    @pytest.mark.analytics
    def test_09_pen_control_click_restore_defaults_external_display_analytics_C52081592(self,setup):
        query_start_time, serial_number = setup
        self.fc.fd["pen_control"].swipe_down_to_external_display_card()
        self.fc.fd["pen_control"].click_external_display_card()
        self.fc.fd["pen_control"].swipe_down_to_restore_default_external_display_ltwo_page()
        for _ in range(5):
            self.fc.fd["pen_control"].click_restore_default_external_display_ltwo_page()
            time.sleep(1)
            self.fc.fd["pen_control"].click_restore_default_continue_external_display_ltwo_page()
            time.sleep(1)
        self.fc.swipe_to_top()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.create_custom_filter_and_verify_analytics(serial_number,"Penforexternaldisplay", "PcPencontrol", "OnClick", "RestoreDefaultsButton", query_start_time)

    @pytest.mark.analytics
    def test_10_pen_control_click_one_step_inking_card_analytics_C52080020(self,setup):
        query_start_time, serial_number = setup
        for _ in range(5):
            self.fc.fd["pen_control"].swipe_down_to_one_step_inking_card()
            self.fc.fd["pen_control"].click_one_step_inking_card()
            time.sleep(1)
            self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
            time.sleep(1)
        self.create_custom_filter_and_verify_analytics(serial_number,"Penforexternaldisplay", "PcPencontrol", "OnClick", "RestoreDefaultsButton", query_start_time)