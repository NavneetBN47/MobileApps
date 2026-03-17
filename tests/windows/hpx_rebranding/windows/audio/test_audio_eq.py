import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
 
pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_EQ(object):
 
 
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.integration
    def test_01_check_eq_ui_on_consumer_DTS_machine_C66174022(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # restore default settings by clicking restore defaults button
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_restore_defaults_button_show_up(), "Restore defaults button is not displayed"
        self.fc.fd["audio"].click_restore_defaults_button()
        time.sleep(2)
        # check EQ
        self.fc.swipe_window(direction="up", distance=4)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        # check horizontal axis
        assert self.fc.fd["audio"].verify_horizontal_axis_32_show_up(), "horizontal axis 32 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_64_show_up(), "horizontal axis 64 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_125_show_up(), "horizontal axis 125 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_250_show_up(), "horizontal axis 250 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_500_show_up(), "horizontal axis 500 is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_1k_show_up(), "horizontal axis 1k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_2k_show_up(), "horizontal axis 2k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_4k_show_up(), "horizontal axis 4k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_8k_show_up(), "horizontal axis 8k is not displayed"
        assert self.fc.fd["audio"].verify_horizontal_axis_16k_show_up(), "horizontal axis 16k is not displayed"
        # check vertical axis
        assert self.fc.fd["audio"].verify_vertical_axis_15_show_up(), "vertical axis 15 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_7_show_up(), "vertical axis 7 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_0_show_up(), "vertical axis 0 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_minus_7_show_up(), "vertical axis minus 7 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_minus_15_show_up(), "vertical axis minus 15 is not displayed"
   
 
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_02_adjust_10_bar_volume_C42197631(self):
        if self.fc.fd["audio"].verify_eq_title_show_up() is False:
            self.fc.restart_myHP()
            time.sleep(3)
            self.fc.fd["devicesMFE"].click_device_card()
            time.sleep(3)
            self.fc.swipe_window(direction="down", distance=3)
            time.sleep(3)
            assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
            self.fc.fd["devices_details_pc_mfe"].click_audio_card()
            time.sleep(4)
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        self.fc.fd["audio"].set_eq_slider_value_increase("horizontal_axis_32", 10)
        time.sleep(3)
        assert self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_32") == "10", "eq horizontal_axis_32 value doesn't set to 10"
        time.sleep(3)
        self.fc.fd["audio"].set_eq_slider_value_increase("horizontal_axis_500", 10)
        time.sleep(3)
        assert self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_500") == "10", "eq horizontal_axis_500 value doesn't set to 10"
   
 
    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    def test_03_remember_10_bar_volume_value_C42197634(self):
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        # check EQ
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        # set new eq values
        self.fc.fd["audio"].set_eq_slider_value_increase("horizontal_axis_32", 10)
        time.sleep(3)
        assert self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_32") == "10", "eq value doesn't set to 10"
        time.sleep(3)
        # check eq value after restart
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(4)
        self.fc.swipe_window(direction="down", distance=15)
        time.sleep(4)
        assert self.fc.fd["audio"].verify_eq_title_show_up() is True, "EQ title is not displayed"
        time.sleep(4)
        assert self.fc.fd["audio"].get_eq_slider_value("horizontal_axis_32") == "10", "eq horizontal_axis_32 value doesn't set to 10 after restart"