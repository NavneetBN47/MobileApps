import pytest
import time
import logging
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_for_desktop")
class Test_Suite_Smart_Experience(object):

    @pytest.mark.function
    def test_01_smart_experience_vision_ai_fusion_service_stopped_C51244777(self):
        self.fc.close_myHP()
        if self.platform.lower() in ["masadansku5", "masadanxsku4","ultron"]:
            logging.info(f"Platform {self.platform.lower()}")
            self.fc.stop_hp_apphelpercap_exe()
            self.fc.launch_myHP()
            time.sleep(5)
            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=5)
            if self.platform.lower()!="ultron":
                Presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
                assert Presence_detection_card_lone_page==False, "Presence detection card is present."
            if self.platform.lower()=='ultron':
                presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
                assert presence_detection_card_lone_page == False, "Presence detection card is present."
                
    @pytest.mark.function
    def test_02_smart_experience_vision_ai_fusion_service_started_C51244778(self):
        if self.platform.lower() in ["masadansku5", "masadanxsku4","ultron"]:
            self.fc.close_myHP()
            logging.info(f"Platform {self.platform.lower()}")
            self.fc.start_hp_apphelpercap_exe()
            self.fc.launch_myHP()
            time.sleep(5)
            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=5)
        if self.platform.lower()!="ultron":
            presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
            assert presence_detection_card_lone_page, "Presence detection card is not present."
        if self.platform.lower()=='ultron':
            presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
            assert presence_detection_card_lone_page, "Presence detection card is not present."

    @pytest.mark.function
    def test_03_camera_driver_disable_C51244779(self):
        self.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/locale/disable_camera.ps1"),r"C:\Users\exec\desktop\disable_camera.ps1")
        
        if self.platform.lower() in ["masadansku5", "masadanxsku4"]:
            logging.info(f"Platform {self.platform.lower()}")
            self.fc.close_myHP()
            self.fc.disable_windows_camera()
            self.fc.launch_myHP(False)
            time.sleep(5)
            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=5)
            presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
            assert presence_detection_card_lone_page == False, "Presence detection card is present."
            self.driver.ssh.remove_file_with_suffix("C:\\Users\\exec\\desktop\\",".ps1")
    
    @pytest.mark.function
    def test_04_camera_driver_enable_C51244781(self):
        self.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/locale/enable_camera.ps1"),r"C:\Users\exec\desktop\enable_camera.ps1")
        
        if self.platform.lower() in ["masadansku5", "masadanxsku4"]:
            logging.info(f"Platform {self.platform.lower()}")
            self.fc.close_myHP()
            self.fc.enable_windows_camera()
            self.fc.launch_myHP(False)
            time.sleep(5)
            self.fc.maximize_and_verify_device_card()
            self.fc.swipe_window(direction="down", distance=5)
            presence_detection_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page()
            assert presence_detection_card_lone_page, "Presence detection card is not present."
            self.driver.ssh.remove_file_with_suffix("C:\\Users\\exec\\desktop\\",".ps1")
            self.fc.close_myHP()