import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Video_Control(object):
   
    #To run these test cases need to run on newer consumer devices like =24H2 like Enstrom, or devices with feature byte as "s4"
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_poly_camera_contextual_text_C55188739(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()
        assert video_control_card.text == "Video", "Video card is not displayed"
        poly_camera_contextual_text = self.fc.fd["video_control"].get_poly_camera_contextual_text()
        assert poly_camera_contextual_text == "Poly Camera Pro", "Video card is not displayed"
        

    @pytest.mark.function
    def test_02_new_user_for_poly_camera_pro_C42915210(self):
        video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()
        assert video_control_card.text == "Video", "Video card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_video_card_lone_page()
        assert self.fc.fd["video_control"].verify_camera_pop_up(), "Camera Pop up is not displayed"
        assert self.fc.fd["video_control"].verify_camera_description_text(), "Camera Description text is not displayed"

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_install_poly_camera_pro_C42915211(self):
        try:
            assert self.fc.fd["video_control"].verify_camera_pop_up(), "Camera Pop up is not displayed"
            assert self.fc.fd["video_control"].verify_camera_pop_up_continue_button(), "Camera Pop up continue button is not displayed"
            self.fc.fd["video_control"].click_camera_pop_up_continue_button()    
            time.sleep(5)
            self.fc.install_camera_apps_from_ms_store()
            self.fc.fd["video_control"].click_to_install_poly_camera_app()
            time.sleep(60)
        finally:
            self.fc.fd["video_control"].click_signout_button_on_sign_in_page()
            self.fc.kill_msstore_process()

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_existing_user_for_poly_camera_pro_C42915212(self):
        try:
            self.fc.fd["devices_details_pc_mfe"].click_video_card_lone_page()
            time.sleep(20)
            self.fc.fd["video_control"].click_camera_pop_up_yes_button()
            assert self.fc.fd["video_control"].verify_poly_camera_window_pop_up(), "Poly Camera Pro Pop up is not displayed"
        finally:
            self.fc.kill_poly_camera_lens()
            self.fc.close_myHP()
            self.fc.windows_setting_page_to_unistall_apps("Poly Camera Pro")