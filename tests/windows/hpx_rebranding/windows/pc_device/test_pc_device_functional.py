from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_PC_Device_Functional(object): 

    @pytest.mark.ota
    @pytest.mark.function
    # This testcase support devices - ultron, grogu, london, medusa
    def test_01_verify_hppk_card_on_pc_device_C42902486(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        assert self.fc.fd["hppk"].verify_programmabe_header_visible(), "Programmable key title is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"


    def test_03_launch_pc_device_via_deeplink_C42902523(self):
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.launch_module_using_deeplink("hpx://pcdevice")
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_back_devices_button_on_pc_devices_page_show_up(), "Device page is not displayed"


    @pytest.mark.ota
    @pytest.mark.function
    def test_04_verify_battery_card_on_pc_device_C42902491(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_battery_manager_card_lone()
        assert self.fc.fd["battery"].verify_battery_manager_title_ltwo_commercial(), "Battery manager title is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_manager_card_lone(), "Battery manager is not displayed"


    @pytest.mark.ota
    @pytest.mark.function
    def test_05_verify_system_control_card_on_pc_device_C42902490(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "System control is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_system_control_card_lone_page()
        assert self.fc.fd["system_control"].verify_system_control_title_show(), "System Control title is not displayed"
        # assert bool(self.fc.fd["system_control"].verify_system_control_title_show()) is True
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_system_control_lone_page_show(), "System control is not displayed"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_06_verify_audio_control_card_on_pc_device_C42902483(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_control_card_show(), "Audio control is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_audio_control_card()
        self.fc.fd["audio"].verify_audio_control_card_show_up(), "Audio title is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_audio_control_card_show(), "Audio control is not displayed"


    @pytest.mark.ota
    @pytest.mark.function
    def test_07_verify_energy_consumption_card_on_pc_device_C52470284(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_energy_consumption_card_show(), "energy_consumption card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_energy_consumption_card()
        self.fc.fd["energy_consumption"].verify_energy_consumption_header_text(), "Enegery consumption title is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_energy_consumption_card_show(), "Enegery consumption is not displayed"



    @pytest.mark.ota
    @pytest.mark.function
    def test_08_verify_product_info_on_pc_device_C42902496(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=25)
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_product_information_header_show(), "Product information title is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_product_number_show(), "Product number title is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_serial_number_show(), "Serial number is not displayed"
        assert self.fc.fd["devices_details_pc_mfe"].verfiy_warranty_status_show(), "Warranty status is not displayed"

    
    @pytest.mark.ota
    @pytest.mark.function
    def test_09_battery_status_when_charging_C42902484(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(3)
        assert self.fc.fd["devices_details_pc_mfe"].verify_battery_status_icon_show(), "Battery status icon is not displayed"
        assert "%" in self.fc.fd["devices_details_pc_mfe"].get_battery_status_icon_text(), "Battery status text is not correct"