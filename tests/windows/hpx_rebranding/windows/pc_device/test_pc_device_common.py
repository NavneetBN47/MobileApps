from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer as classic_FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_PC_Device_Functional_Common(object):
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_verify_install_and_launch_hpx_C42902480(self):
        time.sleep(5)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(), "Display control is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_control_card_show(), "Audio control is not displayed"


    @pytest.mark.ota
    @pytest.mark.function
    def test_02_verify_action_items_on_pc_device_C53103965(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(7)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(7)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(), "Display control is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_control_card_show(), "Audio control is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_title = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_title == "Display","Display Text is not matching."
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_verify_pc_device_card_present_C42902481(self):
        time.sleep(3)
        self.fc.restart_myHP()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device card is not present"
        assert self.fc.fd["devicesMFE"].verify_sign_in_button_show_up(), "Sign in button is not present"
        assert self.fc.fd["devicesMFE"].verify_profile_icon_show_up(), "Profile icon is not present"
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_04_verify_presence_sensing_card_on_pc_device_C53003649(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_sensing_lone_page_show(), "presence sensing card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_presence_sensing_card_lone_page()
        time.sleep(3)
        assert self.fc.fd["presence_sensing"].verify_turn_off_my_screen_btn_show(), "presence sensing title is not displayed"
        time.sleep(3)
        self.fc.close_windows_settings_panel()
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_sensing_lone_page_show(), "presence sensing card is not displayed"

    @pytest.mark.ota
    @pytest.mark.function
    def test_05_verify_the_device_name_C42902503(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_devices_name(), "Device name is not displayed"

    
    @pytest.mark.ota
    @pytest.mark.function
    def test_06_click_video_card_under_pc_device_page_C42902488(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        # verify video card is show up
        assert self.fc.fd["video_control"].verify_video_card_show_up(), "Video card is not displayed"
        # Click on the video card
        self.fc.fd["video_control"].click_video_card()
        time.sleep(2)
        # click cancel button on dialog 
        self.fc.fd["video_control"].click_cancel_button_on_video_dialog()
        time.sleep(2)
        # verify video card is show up
        assert self.fc.fd["video_control"].verify_video_card_show_up(), "Video card is not displayed"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_07_navigate_with_the_keyboard_C42902520(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["audio"].press_tab("audio_control_card")
        time.sleep(2)
        assert self.fc.fd["audio"].is_focus_on_element("audio_control_card"), "Audio control card is not focused"
        time.sleep(2)
        self.fc.fd["audio"].press_enter("audio_control_card")
        time.sleep(2)
        assert self.fc.fd["audio"].verify_output_title_show_up(), "Output title is not displayed"
