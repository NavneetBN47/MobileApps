import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_capture_logs")
class Test_Suite_Video_Control(object):

    #To run these test cases need to run on commercial devices before =2024 like Warparth or devices with feature byte as "qMqk or qjqk"
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_check_the_hp_presence_video_application_in_commercial_system_C59354112(self):
        self.fc.close_myHP()
        self.fc.fd["video_control"].install_hp_presence_commercial_system()
        self.fc.kill_msstore_process()
        self.fc.launch_myHP()
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()
        assert video_control_card.text == "Video", "Video card is not displayed"
        hp_presence_video_contextual_text = self.fc.fd["video_control"].get_hp_presence_video_contextual_text()
        assert hp_presence_video_contextual_text == "HP Presence Video", "Video card is not displayed"
        self.fc.close_myHP()
        self.fc.windows_setting_page_to_unistall_apps("Hp Presence Video")
        time.sleep(30)
        self.fc.launch_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        video_control_card = self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page()
        assert video_control_card==False, "Video card is displayed"
        self.fc.close_myHP()