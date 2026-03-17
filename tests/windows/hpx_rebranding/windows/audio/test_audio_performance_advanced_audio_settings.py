import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Audio_Performance_Advanced_Audio_Settings(object):

    @pytest.mark.function
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.ARM
    def test_01_check_audio_cpu_and_memory_usage_audio_control_page_C42541180(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)  
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)

        assert self.fc.get_machine_cpu_usage() < 100, "CPU usage is too high before testing audio performance"
        time.sleep(2)
        assert self.fc.get_memory_usage_percentage() < 100, "Memory usage is too high before testing audio performance"


    @pytest.mark.function
    @pytest.mark.consumer
    def test_02_check_audio_cpu_and_memory_usage_advanced_audio_settings_page_C64809572(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)  
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)

        assert self.fc.get_machine_cpu_usage() < 100, "CPU usage is too high before testing audio performance"
        time.sleep(2)
        assert self.fc.get_memory_usage_percentage() < 100, "Memory usage is too high before testing audio performance"
        time.sleep(2)

        # Select internal device to enable Advanced Audio Settings
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_internal_device()
        time.sleep(3)
        assert self.fc.get_machine_cpu_usage() < 100, "CPU usage is too high before testing audio performance"
        time.sleep(2)
        assert self.fc.get_memory_usage_percentage() < 100, "Memory usage is too high before testing audio performance"
        time.sleep(2)

    
    @pytest.mark.function
    @pytest.mark.consumer
    def test_03_check_eq_ui_on_consumer_RTK_machine_C42214017(self):
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)  
        time.sleep(6)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        # make EQ will show up with internal device
        self.fc.swipe_window(direction="up", distance=3)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_output_combobox_show_up(), "Output combobox is not displayed"
        self.fc.fd["audio"].click_output_combobox_open_button()
        time.sleep(2)
        self.fc.fd["audio"].select_output_internal_device()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=11)
        time.sleep(3)
        # check EQ
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
        assert self.fc.fd["audio"].verify_vertical_axis_12_show_up(), "vertical axis 12 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_6_show_up(), "vertical axis 6 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_0_show_up(), "vertical axis 0 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_minus_6_show_up(), "vertical axis minus 6 is not displayed"
        assert self.fc.fd["audio"].verify_vertical_axis_minus_12_show_up(), "vertical axis minus 12 is not displayed"