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
    def test_01_launching_hpx_and_verify_camera_and_presence_detection_action_item_show_C49176979(self):
        time.sleep(5)
        self.fc.restart_app()
        time.sleep(5)
        self.fc.fd["vision_ai"].verify_let_myhp_access_your_camear_dialog_show(), "Let myHP access your camera dialog is not displayed"
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        assert self.fc.fd["vision_ai"].verify_camera_and_presence_detection_action_item_show(), "Camera and presence detection action item is not displayed"
    
    @pytest.mark.function
    @pytest.mark.commercial    
    def test_02_default_values_of_features_C49176992(self):
        time.sleep(5)
        self.fc.restart_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_presence_detection()
        time.sleep(2)
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_show(), "Onlooker detection item is not displayed"
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_state() == "0", "Onlooker detection button status should disable"
        assert self.fc.fd["vision_ai"].verify_enable_sureview_button_state() == "0", "Enable sureview button status should disable"

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_verify_vision_ai_on_masadanx_device_C50511861(self):
        time.sleep(5)
        self.fc.restart_app()
        time.sleep(5)
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
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
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
        # verify enable sureview text show
        assert self.fc.fd["vision_ai"].verify_enable_sureview_text_show(), "Enable sureview text is not displayed"
        time.sleep(2)
        # verify enable sureview tips icon show
        assert self.fc.fd["vision_ai"].verify_enable_sureview_tips_icon_show(), "Enable sureview tips icon is not displayed"
        time.sleep(2)
        # verify enable sureview button show
        assert self.fc.fd["vision_ai"].verify_enable_sureview_button_show(), "Enable sureview button is not displayed"
        time.sleep(2) 
        # verify enable sureview button status is grey, it is divided into 3 steps
        # verify enable sureview button status is 0
        assert self.fc.fd["vision_ai"].get_enable_sureview_button_state() == "0", "Enable sureview button status should enable"
        # time.sleep(2)
        assert self.fc.fd["vision_ai"].click_enable_sureview_button
        time.sleep(2)
        # verify enable sureview button status is 0
        assert self.fc.fd["vision_ai"].get_enable_sureview_button_state() == "0", "Enable sureview button status should enable"
        time.sleep(2)
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
    
    @pytest.mark.function
    @pytest.mark.commercial
    def test_04_verify_auto_hdr_C49176994(self):
        time.sleep(5)
        self.fc.restart_app()
        time.sleep(5)
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
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
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

    @pytest.mark.function
    @pytest.mark.commercial
    def test_05_verify_auto_on_off_state_C49176995(self):
        time.sleep(5)
        self.fc.restart_app()
        time.sleep(5)
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
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
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
        # click auto hdr toggle button
        self.fc.fd["vision_ai"].click_auto_hdr_toggle_button()
        time.sleep(2)
        # get auto hdr toggle status is off
        assert self.fc.fd["vision_ai"].get_auto_hdr_toggle_default_status() == "0", "Auto HDR toggle status is on"
        time.sleep(2)

    @pytest.mark.function
    @pytest.mark.commercial
    def test_06_onlooker_detection_on_sure_view_support_unit_C49176999(self):
        time.sleep(5)
        self.fc.restart_app()
        time.sleep(5)
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
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
        time.sleep(2)
        # verify onlooker detection text show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_show(), "Onlooker detection item is not displayed"
        time.sleep(2)
        # verify onlooker detection button status is off
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_state() == "0", "Onlooker detection button status should disable"
        time.sleep(2)
        # click onlooker detection button
        self.fc.fd["vision_ai"].click_onlooker_detection_button()
        time.sleep(2)
        # verify onlooker detection button status is on
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_state() == "1", "Onlooker detection button status should enable"
        time.sleep(2)
        # verify enable sureview button show
        assert self.fc.fd["vision_ai"].verify_enable_sureview_button_show(), "Enable sureview button is not displayed"
        time.sleep(2)
        # verify enable sureview button status is off
        assert self.fc.fd["vision_ai"].get_enable_sureview_button_state() == "0", "Enable sureview button status should disable"
        time.sleep(2)
        # click onlooker detection button
        self.fc.fd["vision_ai"].click_onlooker_detection_button()
        time.sleep(2)
        # verify onlooker detection button status is off
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_state() == "0", "Onlooker detection button status should disable"
        time.sleep(2)
        # verify enable sureview button status is grey, it is divided into 3 steps
        # verify enable sureview button status is 0
        assert self.fc.fd["vision_ai"].get_enable_sureview_button_state() == "0", "Enable sureview button status should enable"
        time.sleep
        # click enable sureview button 
        self.fc.fd["vision_ai"].click_enable_sureview_button()
        time.sleep(2)
        # verify enable sureview button status is 0
        assert self.fc.fd["vision_ai"].get_enable_sureview_button_state() == "0", "Enable screen blur button status should enable"
        time.sleep(2)
        
    def test_07_verify_vision_ai_auto_hdr_on_C49176997(self):
        time.sleep(5)
        self.fc.restart_app()
        time.sleep(5)
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
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
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

    def test_08_verify_vision_ai_auto_hdr_vs_windows_auto_hdr_C49177011(self):
        time.sleep(5)
        self.fc.restart_app()
        time.sleep(5)
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
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
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
        self.fc.fd["vision_ai"].click_auto_hdr_toggle_button()
        # get auto hdr toggle default status is off
        assert self.fc.fd["vision_ai"].get_auto_hdr_toggle_default_status() == "0", "Auto HDR toggle status is on"
        time.sleep(2)
        self.fc.open_hdr_setting()
        time.sleep(1)
        # get windows auto hdr toggle default status is off
        assert self.fc.fd["vision_ai"].get_toggle_windows_hdr_state() == "0", "Windows Auto HDR toggle status is on"
        self.fc.close_windows_settings_panel()
        self.fc.fd["vision_ai"].click_restore_default_button()
        time.sleep(2)
        self.fc.close_myHP()

    @pytest.mark.function
    @pytest.mark.commercial
    def test_09_restore_default_button_for_non_attention_focus_device_C51215689(self):
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
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
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
        # click auto hdr toggle button
        self.fc.fd["vision_ai"].click_auto_hdr_toggle_button()
        # get auto hdr toggle default status is off
        assert self.fc.fd["vision_ai"].get_auto_hdr_toggle_default_status() == "0", "Auto HDR toggle status is on"
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
        # verify enable sureview button show
        assert self.fc.fd["vision_ai"].verify_enable_sureview_button_show(), "Enable sureview button is not displayed"
        time.sleep(2)
        # verify enable sureview button status is off
        assert self.fc.fd["vision_ai"].get_enable_sureview_button_state() == "0", "Enable sureview button status should disable"
        time.sleep(2)
        # click enable sureview button
        self.fc.fd["vision_ai"].click_enable_sureview_button()
        time.sleep(2)
        # verify enable sureview button status is on
        assert self.fc.fd["vision_ai"].get_enable_sureview_button_state() == "1", "Enable sureview button status should enable"
        time.sleep(2)
        # verify restore default button show
        assert self.fc.fd["vision_ai"].verify_restore_default_button_show(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["vision_ai"].click_restore_default_button()
        time.sleep(2)
        # verify auto hdr toggle show
        assert self.fc.fd["vision_ai"].verify_auto_hdr_toggle_show(), "Auto HDR toggle is not displayed"
        time.sleep(2)
        # get auto hdr toggle default status is on
        assert self.fc.fd["vision_ai"].get_auto_hdr_toggle_default_status() == "1", "Auto HDR toggle status is off"
        time.sleep(2)
        # verify onlooker detection toggle show
        assert self.fc.fd["vision_ai"].verify_on_looker_detection_button_show(), "Onlooker detection button is not displayed"
        time.sleep(2)
        # verify onlooker detection toggle status is off
        assert self.fc.fd["vision_ai"].get_on_looker_detection_button_state() == "0", "Onlooker detection button status should disable"
        time.sleep(2)
        # verify enable sureview button show
        assert self.fc.fd["vision_ai"].verify_enable_sureview_button_show(), "Enable sureview button is not displayed"
        time.sleep(2)
        # verify enable sureview button status is grey, it is divided into 3 steps
        # verify enable sureview button status is 0
        assert self.fc.fd["vision_ai"].get_enable_sureview_button_state() == "0", "Enable sureview button status should enable"
        # time.sleep(2)
        self.fc.fd["vision_ai"].click_enable_sureview_button()
        time.sleep(2)
        # verify enable sureview button status is 0
        assert self.fc.fd["vision_ai"].get_enable_sureview_button_state() == "0", "Enable sureview button status should enable"
        time.sleep(2)