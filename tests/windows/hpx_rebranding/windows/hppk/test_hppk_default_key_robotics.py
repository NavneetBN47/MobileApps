import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_HPPK_Robotics(object):
        
    #this suite should run on london platform
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_default_hppk_key_S1_C42901004(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].click_hppk_card()
        time.sleep(3)
        self.fc.fd["hppk"].click_hpone_progkey_menucard_arrow_btn()
        time.sleep(3)
        self.fc.fd["hppk"].click_hp_prog_key_radio_btn()
        time.sleep(3)
        self.fc.close_myHP()
        self.vcosmos.press_hppk_key0()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        self.vcosmos.clean_up_logs()
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_default_hppk_key_S2_C42901006(self):
        self.fc.close_myHP()
        self.vcosmos.press_hppk_key1()
        assert self.fc.fd["hppk"].verify_support_card_visible(), "Support card verification on lone page failed"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_default_hppk_key_S3_C42901008(self):
        self.fc.close_myHP()
        self.vcosmos.press_hppk_key2()
        # workaround, pressing prog key takes user to empty L1 page, back button takes user to normal L1 page
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_hppk_card_show_up(), "hppk card is not displayed"
        self.vcosmos.clean_up_logs()

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_default_hppk_key_S4_C42901002(self):
        self.fc.close_myHP()
        self.vcosmos.press_hppk_key3()
        assert self.fc.fd["hppk"].verify_programmabe_header_visible(), "Programmable key title is not displayed"
        self.vcosmos.clean_up_logs()