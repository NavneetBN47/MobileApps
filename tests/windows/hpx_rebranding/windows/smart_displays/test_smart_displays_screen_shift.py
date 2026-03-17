import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
# This test suite only available ITG and STG build now
class Test_Smart_Displays_Screen_Shift(object):
        
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_01_verify_smart_displays_show_pc_device_page_C57812967(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_lone_page(), "Smart Displays L1 card is not displayed"
    
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_02_verify_smart_displays_can_be_enable_and_disable_C57803859(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_lone_page(), "Smart Displays L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_lone_page()
        time.sleep(2)
        if self.fc.fd["smart_displays"].verify_screen_shift_button_status() == "1":
            self.fc.fd["smart_displays"].click_screen_shift_button()
            time.sleep(2)
            self.fc.fd["smart_displays"].click_screen_shift_button()
        else:
            self.fc.fd["smart_displays"].click_screen_shift_button()
        time.sleep(2)
        assert self.fc.fd["smart_displays"].verify_screen_shift_button_status() == "1", "Smart Display (Screen Shift) is not enabled"
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_lone_page()
        time.sleep(2)
        assert self.fc.fd["smart_displays"].verify_screen_shift_button_status() == "1", "Smart Display (Screen Shift) is not enabled, expected disable"
        time.sleep(2)
        self.fc.fd["smart_displays"].click_screen_shift_button()
        time.sleep(2)
        assert self.fc.fd["smart_displays"].verify_screen_shift_button_status() == "0", "Smart Display (Screen Shift) is enabled, expected disable"
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_03_verify_restore_button_C57803862(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_lone_page(), "Smart Displays L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_lone_page()
        time.sleep(2)
        if self.fc.fd["smart_displays"].verify_screen_shift_button_status() == "1":
            self.fc.fd["smart_displays"].click_screen_shift_button()
            time.sleep(2)
            self.fc.fd["smart_displays"].click_screen_shift_button()
        else:
            self.fc.fd["smart_displays"].click_screen_shift_button()
        time.sleep(2)
        self.fc.fd["smart_displays"].click_screen_shift_restore_button()
        time.sleep(2)
        assert self.fc.fd["smart_displays"].verify_screen_shift_button_status() == "0", "Screen Shift restore button is not worked, expected disable"
    

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.integration
    def test_04_verify_smart_display_default_UI_C57812969(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_smart_displays_lone_page(), "Smart Displays L1 card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_smart_displays_lone_page()
        time.sleep(2)
        self.fc.fd["smart_displays"].verify_feature_notice_show(), "Feature notice is not displayed"
        self.fc.fd["smart_displays"].verify_banner_image_show(), "Banner image is not displayed"
        desc_text = self.fc.fd["smart_displays"].get_screen_shift_description_text()
        assert desc_text == "Drag and drop app windows into preset layouts to easily organize your workspace across multiple external monitors.", f"Screen Shift description text is incorrect, expected 'Drag and drop app"
        assert self.fc.fd["smart_displays"].verify_restore_default_button_show(), "Restore default button is not displayed"