from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_for_desktop")
class Test_MS_Store_Upgrade(object):

    #Can be run on Bopeep, Keelung 27 or Kelung 32 coz written script with the mas modules avaliable on these devices
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_ms_store_update_flow_C67840127(self):
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        # Check if device card is present on L0 page
        if self.fc.fd["devicesMFE"].verify_device_card_show_up(raise_e=False):
            logging.info("App launched on L0 page - clicking device card to navigate to L1")
            self.fc.fd["devicesMFE"].click_device_card()
        else:
            logging.info("App launched directly on L1 page or no device card present - moving forward") 
        time.sleep(3)
        #older version validation before update 
        self.fc.swipe_window(direction="down", distance=5)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(), "Display control module is not present."
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page(), "Video card is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verify_wellbeing_card_lone_page_show(), "Wellbeing card is not displayed"
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "System control card is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_sensing_lone_page_show(), "Presence sensing card is not displayed"
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_product_information_header_show(), "Product Information card is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_product_number_show(), "Product number is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_serial_number_show(), "Serial number is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_warranty_status_show(), "Warranty Status is not displayed"

        self.fc.swipe_window(direction="up", distance=5)
        #MS_Store_app_update
        self.fc.ota_app_after_update()

        self.fc.maximize_and_verify_device_card()
        time.sleep(3)
        # ms_store_after_app_update
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(), "Display control module is not present."
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verify_video_lone_page(), "Video card is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verify_wellbeing_card_lone_page_show(), "Wellbeing card is not displayed"
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "System control card is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verify_presence_sensing_lone_page_show(), "Presence sensing card is not displayed"
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.fd["devicesMFE"].maximize_app()
        self.fc.swipe_window(direction="down", distance=10)
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_product_information_header_show(), "Product Information card is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_product_number_show(), "Product number is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_serial_number_show(), "Serial number is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_warranty_status_show(), "Warranty Status is not displayed"

        # close ms store and app 
        self.fc.exit_hp_app_and_msstore()