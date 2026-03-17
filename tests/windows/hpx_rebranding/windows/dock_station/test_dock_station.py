import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Dock_Station(object):

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_product_information_dock_connected_C53035116(self):
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(2)
        assert bool(self.fc.fd["devicesMFE"].verify_dock_station_card_show()) is True, "Dock station card is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_dock_station_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(2)
        assert self.fc.fd["dock_station"].verify_product_information_txt_show_up(), "Product information txt is not displayed"
        assert self.fc.fd["dock_station"].verify_serial_number_value_show_up(), "Serial number value is not displayed"
        assert self.fc.fd["dock_station"].verify_firewall_version_show_up(), "Firewall version is not displayed"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_consistency_C53039256(self):
        time.sleep(2)
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devicesMFE"].verify_window_maximize():
            self.fc.fd["devicesMFE"].maximize_app()
        time.sleep(2)
        if bool(self.fc.fd["devicesMFE"].verify_dock_station_card_show()) is False:
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            time.sleep(2)
            self.fc.fd["devicesMFE"].click_back_button_rebranding()
            time.sleep(2)
        assert bool(self.fc.fd["devicesMFE"].verify_dock_station_card_show()) is True, "Dock station card is not displayed"
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_dock_station_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(2)
        assert self.fc.fd["dock_station"].verify_product_information_txt_show_up(), "Product information txt is not displayed"
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=30)
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        assert bool(self.fc.fd["devicesMFE"].verify_dock_station_card_show()) is True, "Dock station card is not displayed"

