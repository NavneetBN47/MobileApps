import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Video_Control(object):
    
    #To run these test cases need to run on newer commercial devices like =24H2 like MasadaN, Ernesto or devices with feature byte as "s4"
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_check_for_the_poly_camera_pro_application_in_commercial_system_C57035236(self):
        self.fc.close_myHP()
        self.fc.fd["video_control"].install_poly_camera_on_commercial_system()
        self.fc.kill_msstore_process()
        self.fc.reset_hp_application()
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()
        assert video_control_card.text == "Video", "Video card is not displayed"
        poly_camera_contextual_text = self.fc.fd["video_control"].get_poly_camera_contextual_text()
        assert poly_camera_contextual_text == "Poly Camera Pro", "Video card is not displayed"
        self.fc.close_myHP()
        self.fc.windows_setting_page_to_unistall_apps("Poly Camera Pro")
        self.fc.launch_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=5)
        video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()
        assert video_control_card==False, "Video card is displayed"
        self.fc.close_myHP()