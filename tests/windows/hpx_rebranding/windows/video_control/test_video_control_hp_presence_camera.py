import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Video_Control(object):


    #To run these test cases ned to run on older devices like Willie,Sammy,Goldy or devices with feature byte as "qM", "qj ", "qk"
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_new_user_for_hp_presence_video_C42915206(self):
        feature_byte_code = self.fc.capture_feature_byte()
        if "qM" in feature_byte_code or "qj " in feature_byte_code or "qk" in feature_byte_code:
           
            self.fc.fd["devicesMFE"].verify_device_card_show_up()
            self.fc.fd["devicesMFE"].click_device_card()
            self.fc.swipe_window(direction="down", distance=5)
            video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()
            assert video_control_card.text == "Video", "Video card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_video_card_lone_page()
            assert self.fc.fd["video_control"].verify_camera_pop_up(), "Camera Pop up is not displayed"
            assert self.fc.fd["video_control"].verify_camera_description_text(), "Camera Description text is not displayed"
    
    def test_02_check_cancel_button_C42915214(self):
        cancel = self.fc.fd["video_control"].verify_camera_pop_up_cancel_button()
        assert cancel.text == "Cancel", "Cancel Button not displayed"      

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_install_hp_presence_video_C42915207(self):
        assert self.fc.fd["video_control"].verify_camera_pop_up(), "Camera Pop up is not displayed"
        assert self.fc.fd["video_control"].verify_camera_pop_up_continue_button(), "Camera Pop up continue button is not displayed"
        self.fc.fd["video_control"].click_camera_pop_up_continue_button()    
        time.sleep(5)
        self.fc.install_camera_apps_from_ms_store()
        self.fc.fd["video_control"].click_to_install_hp_presence_app()
        time.sleep(80)
        self.fc.fd["video_control"].click_signout_button_on_sign_in_page()
        time.sleep(5)
        self.fc.kill_msstore_process()

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_existing_user_for_hp_presence_video_C42915208(self):
        try:
            self.fc.fd["devices_details_pc_mfe"].click_video_card_lone_page()
            assert self.fc.fd["video_control"].verify_hp_presence_window_pop_up(), "Hp Presence Pop up is not displayed"
            self.fc.kill_camera_process()
            self.fc.fd["video_control"].click_minimize()
            
        finally:
            self.fc.windows_setting_page_to_unistall_apps("HP Presence Video")    
            self.fc.close_myHP()