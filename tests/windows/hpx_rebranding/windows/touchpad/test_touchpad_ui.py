import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx_rebranding.utility.restart_machine import restart_machine
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Touchpad_UI(object):


    def verify_images(self, image_compare_result, image_name, percentage):
        logging.info(f"Image comparison result at {percentage}% text size: {image_compare_result}")
        if image_compare_result is not None:
            assert image_compare_result, f"{image_name} doesn't match with baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
    
    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_01_check_touchpad_show_on_pc_device_C43876468(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_touch_pad_lone_page(), "Touchpad card is not displayed"


    @pytest.mark.ota
    @pytest.mark.function
    def test_02_verify_touchpad_default_setting_C43876469(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)
        assert self.fc.fd["touchpad"].verify_touchpad_title_show(), "Touchpad title is not shown"
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_text_show(), "Enable gesture control text is not shown"
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "0", "Enable gesture control button is on" 
        assert self.fc.fd["touchpad"].verify_adjust_feedback_intensity_link_show(), "Adjust feedback intensity link is not shown"
        assert self.fc.fd["touchpad"].verify_restore_default_button_show(), "Restore default button is not shown"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_restart_touchpad_verify_touchpad_function_C63989650(self, request):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)
        assert self.fc.fd["touchpad"].verify_touchpad_title_show(), "Touchpad title is not shown"
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_text_show(), "Enable gesture control text is not shown"
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "0", "Enable gesture control button is on" 
        assert self.fc.fd["touchpad"].verify_adjust_feedback_intensity_link_show(), "Adjust feedback intensity link is not shown"
        assert self.fc.fd["touchpad"].verify_restore_default_button_show(), "Restore default button is not shown"

        restart_machine(self, request)

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
        self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
        time.sleep(3)
        assert self.fc.fd["touchpad"].verify_touchpad_title_show(), "Touchpad title is not shown"
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_text_show(), "Enable gesture control text is not shown"
        assert self.fc.fd["touchpad"].verify_enable_gesture_control_button_state() == "0", "Enable gesture control button is on" 
        assert self.fc.fd["touchpad"].verify_adjust_feedback_intensity_link_show(), "Adjust feedback intensity link is not shown"
        assert self.fc.fd["touchpad"].verify_restore_default_button_show(), "Restore default button is not shown"


    # @pytest.mark.ota
    # @pytest.mark.function
    # def test_04_verify_touchpad_module_increase_text_size_C51909718(self):
    #     try: 
    #         platform=self.platform.lower()
    #         self.fc.close_myHP()
    #         self.fc.fd["touchpad"].update_text_size_in_system_settings(225)

    #         self.fc.launch_myHP()

    #         self.fc.fd["devicesMFE"].click_device_card()
    #         time.sleep(2)
    #         self.fc.fd["devices_details_pc_mfe"].swipe_to_touchpad_card()
    #         self.fc.fd["devices_details_pc_mfe"].click_touchpad_card()
    #         time.sleep(3)

    #         image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["touchpad"].verify_touchpad_title_show_image, machine_name=platform, page_number=1, element="touchpad_title", text_size=225)
    #         self.verify_images(image_compare_result, "Touchpad Title", 225)

    #         image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["touchpad"].verify_enable_gesture_control_text_show_image, machine_name=platform, page_number=2, element="enable_gesture_text", text_size=225)
    #         self.verify_images(image_compare_result, "Touchpad Enable Gesture Text", 225)

    #         image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["touchpad"].verify_adjust_feedback_intensity_link_show_image, machine_name=platform, page_number=3, element="adjust_feedback_intensity_link", text_size=225)
    #         self.verify_images(image_compare_result, "Touchpad Adjust Feedback Intensity Link", 225)

    #     finally: 
    #         self.fc.fd["touchpad"].update_text_size_in_system_settings(100)