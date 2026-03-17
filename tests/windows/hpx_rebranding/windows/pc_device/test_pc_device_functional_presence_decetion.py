from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_PC_Device_Functional_Presence_Detection(object): 


    @pytest.mark.ota
    @pytest.mark.function
    #This testcase support devices - ultron, eviee, masada
    def test_01_verify_presence_detection_card_on_pc_device_C52399342(self):
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_presence_detection_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page(), "Presence detection is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_presence_detection_card_lone_page("presence_detection_card_lone_page")
        time.sleep(2)
        assert self.fc.fd["smart_experience"].verify_camera_and_presence_detection_header_masadan_ltwo_page(), "Presence detection key title is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_presence_detection_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_detection_card_lone_page(), "Presence detection is not displayed"
