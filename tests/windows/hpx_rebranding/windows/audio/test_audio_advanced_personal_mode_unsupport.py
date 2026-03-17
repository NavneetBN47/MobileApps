import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Advanced_Personal_Mode(object):


    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_01_apm_mode_will_not_show_on_unspupport_device_C58308520(self):
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=6)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=9)
        time.sleep(2)
        # verify apm mode title will not show
        assert bool(self.fc.fd["audio"].verify_apm_mode_title_show()) is False, "APM mode is showing on unsupported device"
        time.sleep(2)
        # verify apm mode toggle will not show
        assert bool(self.fc.fd["audio"].verify_apm_mode_toggle_show()) is False, "APM mode toggle is showing on unsupported device"
        time.sleep(2)