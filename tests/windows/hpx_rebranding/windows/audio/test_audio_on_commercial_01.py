import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Control_Commercial_01(object):


    @pytest.mark.function
    @pytest.mark.commercial
    @pytest.mark.ota
    def test_01_check_audio_control_will_not_show_on_commercial_machine_cycle_less_24c1_C42197740(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(4)
        # verify audio card will not display on commercial machine which cycle less than 24C1
        try:
            self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up()
            assert False, "Audio card is displayed on commercial machine with cycle < 24C1"
        except Exception:
            pass
