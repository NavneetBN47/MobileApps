import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
import logging


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
#This suite should be run on snowball platform
class Test_Suite_Audio_Logo_DTS_Snowball(object):


    @pytest.mark.commercial
    def test_01_verify_dts_logo_on_tower_pc_C53039339(self):
        platform=self.platform.lower()
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        if not self.fc.fd["audio"].verify_output_device_35mm_headphone_on_snowball_show_up():
            time.sleep(2)
            self.fc.fd["audio"].click_output_combobox_open_button()
            time.sleep(2)
            self.fc.fd["audio"].click_output_device_35mm_headphone_on_snowball()

        time.sleep(2)
        image_compare_result = self.fc.get_screenshot_comparison_result(self.fc.fd["audio"].wait_and_verify_dts_logo_on_tower, machine_name=platform)

        if image_compare_result is not None:
            assert image_compare_result, "DTS logo on tower PC doesn't match with baseline."
        else:
            logging.info("No screenshot comparison performed (context manager not active)")
        
        time.sleep(2)
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_device_usb_headphone_on_snowball()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_dts_logo_on_tower_show_up() is False, "DTS logo on tower PC is  displayed"

        time.sleep(2)
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].click_output_internal_speaker_on_snowball()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_dts_logo_on_tower_show_up() is False, "DTS logo on tower PC is  displayed"



