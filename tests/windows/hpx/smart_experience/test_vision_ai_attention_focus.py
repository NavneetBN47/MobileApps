import time
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
from SAF.misc import windows_utils
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Vision_AI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
            time.sleep(3)
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    def test_01_verify_vision_ai_on_masadan_device_C50511857(self):
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        # verify camera and presence detection action item show
        assert self.fc.fd["vision_ai"].verify_camera_and_presence_detection_action_item_show(), "Camera and presence detection action item is not displayed"
        time.sleep(3)
        # click camera and presence detection action item 
        self.fc.fd["vision_ai"].click_camera_and_presence_detection_action_item()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(2)
        # verify auto hdr text show
        assert self.fc.fd["vision_ai"].verify_auto_hdr_text_show(), "Auto HDR text is not displayed"
        time.sleep(2)
        # verify auto hdr text == "Auto HDR"
        assert self.fc.fd["vision_ai"].get_auto_hdr_text() == "Auto HDR", "Auto HDR text is not displayed"
        time.sleep(2)
        # verify auto hdr toggle show
        assert self.fc.fd["vision_ai"].verify_auto_hdr_toggle_show(), "Auto HDR toggle is not displayed"
        time.sleep(2)
        # get auto hdr toggle default status is on
        assert self.fc.fd["vision_ai"].get_auto_hdr_toggle_default_status() == "1", "Auto HDR toggle status is off"
        time.sleep(2)
        # verify auto hdr description text show
        assert self.fc.fd["vision_ai"].verify_auto_hdr_description_text_show(), "Auto HDR description text is not displayed"
        time.sleep(2)
        # verify auto hdr description text == "Automatically adjusts your screen’s high dynamic range settings based on the lighting in your environment. Disable it for a more natural or standard look."
        assert self.fc.fd["vision_ai"].get_auto_hdr_description_text() == "Automatically adjusts your screen’s high dynamic range settings based on the lighting in your environment. Disable it for a more natural or standard look.", "Auto HDR introduce text is not displayed"
        time.sleep(2)
        # verify auto hdr image show
        assert self.fc.fd["vision_ai"].verify_auto_hdr_image_show(), "Auto HDR image is not displayed"
        time.sleep(2)    
        # verify intelligent dynamic contrast text show
        assert self.fc.fd["vision_ai"].verify_intelligent_dynamic_contrast_text_show(), "Intelligent dynamic contrast text is not displayed"
        time.sleep(2)
        # verify intelligent dynamic contrast text == Intelligent Dynamic Contrast
        assert self.fc.fd["vision_ai"].get_intelligent_dynamic_contrast_text() == "Intelligent dynamic contrast", "Intelligent dynamic contrast text is incorrect"
        time.sleep(2)
        # verify intelligent dynamic contrast toggle show
        assert self.fc.fd["vision_ai"].verify_intelligent_dynamic_contrast_toggle_show(), "Intelligent dynamic contrast toggle is not displayed"
        time.sleep(2)
        # verify intelligent dynamic contrast toggle default status == 0
        assert self.fc.fd["vision_ai"].get_intelligent_dynamic_contrast_toggle_default_status() == "0", "Intelligent dynamic contrast toggle default status is incorrect"
        time.sleep(2)
        # verify intelligent dynamic contrast description text show
        assert self.fc.fd["vision_ai"].verify_intelligent_dynamic_contrast_description_text_show(), "Intelligent dynamic contrast description text is not displayed"
        time.sleep(2)
        # verify intelligent dynamic contrast description text == "Automatically adjusts your screen’s contrast while in battery mode to save power."
        assert self.fc.fd["vision_ai"].get_intelligent_dynamic_contrast_description_text() == "Automatically adjusts your screen’s contrast while in battery mode to save power.", "Intelligent dynamic contrast description text is incorrect"
        time.sleep(2)
        # verify intelligent dynamic contrast image show
        assert self.fc.fd["vision_ai"].verify_intelligent_dynamic_contrast_image_show(), "Intelligent dynamic contrast image is not displayed"
        time.sleep(2)
        # verify attention focus text show
        assert self.fc.fd["vision_ai"].verify_attention_focus_text_show(), "Attention focus text is not displayed"
        time.sleep(2)
        # verify attention focus text == Attention Focus
        assert self.fc.fd["vision_ai"].get_attention_focus_text() == "Attention focus", "Attention focus text is incorrect"
        time.sleep(2)
        # verify attention focus toggle show
        assert self.fc.fd["vision_ai"].verify_attention_focus_toggle_show(), "Attention focus toggle is not displayed"
        time.sleep(2)
        # verify attention focus toggle default status == 0
        assert self.fc.fd["vision_ai"].get_attention_focus_toggle_default_status() == "0", "Attention focus toggle default status is incorrect"
        time.sleep(2)
        # verify attention focus description text show
        assert self.fc.fd["vision_ai"].verify_attention_focus_description_text_show(), "Attention focus description text is not displayed"
        time.sleep(2)
        # verify attention focus description text == "Intelligently enables dynamic contrast to save power when you look away from the screen."
        assert self.fc.fd["vision_ai"].get_attention_focus_description_text() == "Intelligently enables dynamic contrast to save power when you look away from the screen.", "Attention focus description text is incorrect"
        time.sleep(2)
        # verify attention focus image show
        assert self.fc.fd["vision_ai"].verify_attention_focus_image_show(), "Attention focus image is not displayed"
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        # verify onlooker detection text show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_show(), "Onlooker detection text is not displayed"
        time.sleep(2)
        # verify onlooker detection text == "Onlooker Detection"
        assert self.fc.fd["vision_ai"].get_on_looker_detection_text() == "Onlooker detection", "Onlooker detection text is not displayed"
        time.sleep(2)
        # verify onlooker detection toggle show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_show(), "Onlooker detection button is not displayed" 
        time.sleep(2)
        # verify onlooker detection toggle status is off
        assert self.fc.fd["vision_ai"].get_on_looker_detection_button_state() == "0", "Onlooker detection button status should disable"
        time.sleep(2)
        # verify onlooker detection description text show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_description_text_show(), "Onlooker detection text is not displayed"
        time.sleep(2)
        # verify onlooker detection description text == "Notifies you when an onlooker is detected in the background."
        assert self.fc.fd["vision_ai"].get_on_looker_detection_description_text() == "Notifies you when an onlooker is detected in the background.", "Onlooker detection introduce text is not displayed"
        time.sleep(2)
        # verify onlooker detection image show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_image_show(), "Onlooker detection image is not displayed"
        time.sleep(2)
        # verify enable screen blur text show
        assert self.fc.fd["vision_ai"].verify_enable_screen_blur_text_show(), "Enable screen blur text is not displayed"
        time.sleep(2)
        # verify enable screen blur tips icon show
        assert self.fc.fd["vision_ai"].verify_enable_screen_blur_tips_icon_show(), "Enable screen blur tips icon is not displayed"
        time.sleep(2)
        # verify enable screen blur button show
        assert self.fc.fd["vision_ai"].verify_enable_screen_blur_button_show(), "Enable screen blur button is not displayed"
        time.sleep(2)
        # verify enable screen blur button status is grey, it is divided into 3 steps
        # verify enable screen blur button status is 0
        assert self.fc.fd["vision_ai"].get_enable_screen_blur_button_state() == "0", "Enable screen blur button status should enable"
        time.sleep(2)
        # click enable screen blur button
        self.fc.fd["vision_ai"].click_enable_screen_blur_button()
        time.sleep(2)
        # verify enable screen blur button status is 0
        assert self.fc.fd["vision_ai"].get_enable_screen_blur_button_state() == "0", "Enable screen blur button status should enable"
        time.sleep(2)
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)

    @pytest.mark.function
    @pytest.mark.commercial
    def test_02_onlooker_detection_on_screen_blur_supported_unit_C49177002(self):
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        # verify camera and presence detection action item show
        assert self.fc.fd["vision_ai"].verify_camera_and_presence_detection_action_item_show(), "Camera and presence detection action item is not displayed"
        time.sleep(2)
        # click camera and presence detection action item 
        self.fc.fd["vision_ai"].click_camera_and_presence_detection_action_item()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
        time.sleep(2)
        # verify onlooker detection text show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_show(), "Onlooker detection text is not displayed"
        time.sleep(2)
        # verify onlooker detection text == "Onlooker Detection"
        assert self.fc.fd["vision_ai"].get_on_looker_detection_text() == "Onlooker detection", "Onlooker detection text is not displayed"
        time.sleep(2)
        # verify onlooker detection toggle show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_show(), "Onlooker detection button is not displayed" 
        time.sleep(2)
        # verify onlooker detection toggle status is off
        assert self.fc.fd["vision_ai"].get_on_looker_detection_button_state() == "0", "Onlooker detection button status should disable"
        time.sleep(2)
        # click onlooker detection button
        self.fc.fd["vision_ai"].click_onlooker_detection_button()
        time.sleep(2)
        # verify onlooker detection button status is on
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_state() == "1", "Onlooker detection button status should enable"
        time.sleep(2)
        # verify enable screen blur button show
        assert self.fc.fd["vision_ai"].verify_enable_screen_blur_button_show(), "Enable screen blur button is not displayed"
        time.sleep(2)
        # verify enable screen blur button status is 0
        assert self.fc.fd["vision_ai"].get_enable_screen_blur_button_state() == "0", "Enable screen blur button status should enable"
        time.sleep(2)
        # click onlooker detection button
        self.fc.fd["vision_ai"].click_onlooker_detection_button()
        time.sleep(2)
        # verify onlooker detection button status is off
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_state() == "0", "Onlooker detection button status should enable"
        time.sleep(2)
        # verify enable screen blur button status is grey, it is divided into 3 steps
        # verify enable screen blur button status is 0
        assert self.fc.fd["vision_ai"].get_enable_screen_blur_button_state() == "0", "Enable screen blur button status should disable"
        time.sleep(2)
        # click enable screen blur button
        self.fc.fd["vision_ai"].click_enable_screen_blur_button()
        time.sleep(2)
        # verify enable screen blur button status is 0
        assert self.fc.fd["vision_ai"].get_enable_screen_blur_button_state() == "0", "Enable screen blur button status should disable"
        time.sleep(2)

    @pytest.mark.function
    @pytest.mark.commercial
    def test_03_persistent_of_auto_hdr_C49177021(self):
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        # verify camera and presence detection action item show
        assert self.fc.fd["vision_ai"].verify_camera_and_presence_detection_action_item_show(), "Camera and presence detection action item is not displayed"
        time.sleep(2)
        # click camera and presence detection action item 
        self.fc.fd["vision_ai"].click_camera_and_presence_detection_action_item()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(2)
        # verify auto hdr text show
        assert self.fc.fd["vision_ai"].verify_auto_hdr_text_show(), "Auto HDR text is not displayed"
        time.sleep(2)
        # verify auto hdr text == "Auto HDR"
        assert self.fc.fd["vision_ai"].get_auto_hdr_text() == "Auto HDR", "Auto HDR text is not displayed"
        time.sleep(2)
        # verify auto hdr toggle show
        assert self.fc.fd["vision_ai"].verify_auto_hdr_toggle_show(), "Auto HDR toggle is not displayed"
        time.sleep(2)
        # get auto hdr toggle default status is on
        assert self.fc.fd["vision_ai"].get_auto_hdr_toggle_default_status() == "1", "Auto HDR toggle status is off"
        time.sleep(2)
        # click auto hdr toggle
        self.fc.fd["vision_ai"].click_auto_hdr_toggle_button()
        time.sleep(2)
        # verify auto hdr toggle status is off
        assert self.fc.fd["vision_ai"].get_auto_hdr_toggle_default_status() == "0", "Auto HDR toggle status is on"
        time.sleep(5)
        # switch back to camera and presence detection action
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        # verify camera and presence detection action item show
        assert self.fc.fd["vision_ai"].verify_camera_and_presence_detection_action_item_show(), "Camera and presence detection action item is not displayed"
        time.sleep(2)
        # click camera and presence detection action item 
        self.fc.fd["vision_ai"].click_camera_and_presence_detection_action_item()
        time.sleep(2)
        # verify auto hdr toggle show
        assert self.fc.fd["vision_ai"].verify_auto_hdr_toggle_show(), "Auto HDR toggle is not displayed"
        time.sleep(2)
        # verify auto hdr toggle status is off
        assert self.fc.fd["vision_ai"].get_auto_hdr_toggle_default_status() == "0", "Auto HDR toggle status is on"
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=8)
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
        time.sleep(2)

    @pytest.mark.function
    @pytest.mark.commercial
    def test_04_persistent_of_onlooker_detection_C49177019(self):
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        # verify camera and presence detection action item show
        assert self.fc.fd["vision_ai"].verify_camera_and_presence_detection_action_item_show(), "Camera and presence detection action item is not displayed"
        time.sleep(2)
        # click camera and presence detection action item 
        self.fc.fd["vision_ai"].click_camera_and_presence_detection_action_item()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
        time.sleep(2)
        # verify onlooker detection text show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_show(), "Onlooker detection text is not displayed"
        time.sleep(2)
        # verify onlooker detection toggle show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_show(), "Onlooker detection button is not displayed" 
        time.sleep(2)
        # verify onlooker detection toggle status is off
        assert self.fc.fd["vision_ai"].get_on_looker_detection_button_state() == "0", "Onlooker detection button status should disable"
        time.sleep(2)
        # click onlooker detection button
        self.fc.fd["vision_ai"].click_onlooker_detection_button()
        time.sleep(2)
        # verify onlooker detection button status is on
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_state() == "1", "Onlooker detection button status should enable"
        time.sleep(2)
        # switch back to camera and presence detection action
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        # verify camera and presence detection action item show
        assert self.fc.fd["vision_ai"].verify_camera_and_presence_detection_action_item_show(), "Camera and presence detection action item is not displayed"
        time.sleep(2)
        # click camera and presence detection action item 
        self.fc.fd["vision_ai"].click_camera_and_presence_detection_action_item()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        # verify onlooker detection text show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_show(), "Onlooker detection text is not displayed"
        time.sleep(2)
        # verify onlooker detection toggle show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_show(), "Onlooker detection button is not displayed" 
        time.sleep(2)
        # verify onlooker detection toggle status is on
        assert self.fc.fd["vision_ai"].get_on_looker_detection_button_state() == "1", "Onlooker detection button status should enable"
        time.sleep(2)

    @pytest.mark.function
    @pytest.mark.commercial
    def test_05_persistent_of_attention_focus_C49177020(self):
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        # verify camera and presence detection action item show
        assert self.fc.fd["vision_ai"].verify_camera_and_presence_detection_action_item_show(), "Camera and presence detection action item is not displayed"
        time.sleep(2)
        # click camera and presence detection action item 
        self.fc.fd["vision_ai"].click_camera_and_presence_detection_action_item()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
        time.sleep(2)
        # verify attention focus text show
        assert self.fc.fd["vision_ai"].verify_attention_focus_text_show(), "Attention focus text is not displayed"
        time.sleep(2)
        # verify attention focus toggle show
        assert self.fc.fd["vision_ai"].verify_attention_focus_toggle_show(), "Attention focus toggle is not displayed"
        time.sleep(2)
        # verify attention focus toggle status is off
        assert self.fc.fd["vision_ai"].get_attention_focus_toggle_default_status() == "0", "Attention focus toggle status should disable"
        time.sleep(2)
        # click attention focus toggle
        self.fc.fd["vision_ai"].click_attention_focus_toggle_button()
        time.sleep(2)
        # verify attention focus toggle status is on
        assert self.fc.fd["vision_ai"].get_attention_focus_toggle_default_status() == "1", "Attention focus toggle status should enable"
        time.sleep(2)
        # switch back to camera and presence detection action
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        # verify camera and presence detection action item show
        assert self.fc.fd["vision_ai"].verify_camera_and_presence_detection_action_item_show(), "Camera and presence detection action item is not displayed"
        time.sleep(2)
        # click camera and presence detection action item 
        self.fc.fd["vision_ai"].click_camera_and_presence_detection_action_item()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        # verify attention focus text show
        assert self.fc.fd["vision_ai"].verify_attention_focus_text_show(), "Attention focus text is not displayed"
        time.sleep(2)
        # verify attention focus toggle show
        assert self.fc.fd["vision_ai"].verify_attention_focus_toggle_show(), "Attention focus toggle is not displayed"
        time.sleep(2)
        # verify attention focus toggle status is on
        assert self.fc.fd["vision_ai"].get_attention_focus_toggle_default_status() == "1", "Attention focus toggle status should enable"
        time.sleep(2)