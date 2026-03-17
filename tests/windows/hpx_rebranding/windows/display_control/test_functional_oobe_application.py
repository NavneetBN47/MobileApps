import logging
import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_oobe")
class Test_Suite_Display_control(object):

    #this suite should only run in bopeep and all display supported consumer platforms
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_application_settings_oobe_default_app_settings_C42891316(self):
        self.fc.maximize_and_verify_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_card_ltwo_page = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_card_ltwo_page == "Display","Display Text is not matching."
        assert "Disney+" in self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
        assert "腾讯视频" in self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
        assert "爱奇艺" in self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_application_settings_oobe_tencent_video_china_only_application_C42891318(self):
        assert "腾讯视频" in self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
        self.fc.fd["display_control"].click_display_control_tencent_app_ltwo_page()
        time.sleep(3)
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100","Brightness slider value is not matching."
        if self.platform.lower() == "bopeep":
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie","Display mode is not matching."
        else:
            logging.info("Display mode- movie is not present in platform.")
        if self.platform.lower() in ("willie","thompson", "bucky"):
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle switch is not matching."
        else:
            logging.info("HDR toggle switch is not present in platform.")
        self.fc.close_myHP()
        assert self.process_util.check_process_running("HP.myHP.exe") == False, "myHP app is not running."

    @pytest.mark.function
    @pytest.mark.ota
    def test_03_application_settings_oobe_iqiyi_china_only_application_C42891320(self):
        self.fc.launch_myHP()
        assert self.fc.fd["devicesMFE"].verify_device_card_show_up(), "Device name verification on lzero page failed"
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        assert "爱奇艺" in self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
        self.fc.fd["display_control"].click_display_control_iqiyi_app_ltwo_page()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100","Brightness slider value is not matching."
        if self.platform.lower() == "bopeep":
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie","Display mode is not matching."
        else:
            logging.info("Display mode- movie is not present in platform.")
        if self.platform.lower() in ("willie","thompson", "bucky"):
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle switch is not matching."
        else:
            logging.info("HDR toggle switch is not present in platform.")
        self.fc.close_myHP()
        assert self.process_util.check_process_running("HP.myHP.exe") == False, "myHP app is not running."
        self.fc.fd["display_control"].launch_all_apps("爱奇艺+")#to launch iqiyi app
        assert bool(self.fc.fd["display_control"].verify_iqiyi_app_launch()) is True,"iqiyi app is not launched."
        self.fc.launch_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100","Brightness slider value is not matching."
        if self.platform.lower() == "bopeep":
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie","Display mode is not matching."
        else:
            logging.info("Display mode- movie is not present in platform.")
        if self.platform.lower() in ("willie","thompson", "bucky"):
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle switch is not matching."
        else:
            logging.info("HDR toggle switch is not present in platform.")
        self.fc.kill_iqiyi_video_process()
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_application_settings_oobe_disney_plus_application_C42891317(self):        
        #launch Disney+ app
        self.fc.fd["display_control"].launch_all_apps("Disney")#to launch Disney+ app
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        assert "Disney+" in self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
        self.fc.fd["display_control"].click_display_control_disney_plus_app()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100","Brightness slider value is not matching."
        if self.platform.lower() == "bopeep":
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie","Display mode is not matching."
        else:
            logging.info("Display mode- movie is not present in platform.")
        if self.platform.lower() in ("willie","thompson", "bucky"):
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle switch is not matching."
        else:
            logging.info("HDR toggle switch is not present in platform.")
        self.fc.kill_disney_video_process()

    @pytest.mark.function
    @pytest.mark.ota
    def test_05_win_application_settings_oobe_iQiyi_application_C42891321(self):        
        #a)iqiyi Video (China only) application should be visible in Application Settings list
        assert "爱奇艺" in self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
        self.fc.fd["display_control"].launch_all_apps("爱奇艺+")#to launch iqiyi app
        assert bool(self.fc.fd["display_control"].verify_iqiyi_app_launch()) is True,"iqiyi app is not launched."
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        #application should highlight/selected in the App settings List
        assert bool(self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page_selected()) is True,"iqiyi app is not highlighted."
        self.fc.kill_iqiyi_video_process()
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_application_settings_oobe_default_app_settings_launch_C42891322(self):        
        assert "Disney+" in self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page(),"Disney + app is not present."
        assert "腾讯视频" in self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page(),"tencent app is not present."
        assert "爱奇艺" in self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page(),"iqiyi app is not present."
        #Launch any default application--Applications should launch and at the same time application should highlight/selected in the List
        #launch Disney+ app
        self.fc.fd["display_control"].launch_all_apps("Disney+")#to launch Disney app
        #app should launched
        assert bool(self.fc.fd["display_control"].verify_disney_plus_app_launch()) is True,"Disney+ app is not launched."
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        assert bool(self.fc.fd["display_control"].verify_display_control_disney_plus_app_ltwo_page_selected()) is True,"Disney+ app is not highlighted."
        self.fc.kill_disney_video_process()
        #launch tencent app
        self.fc.fd["display_control"].launch_all_apps("腾讯视频+")#to launch tencent app
        #app should launched
        assert bool(self.fc.fd["display_control"].verify_tencent_app_launch()) is True,"tencent app is not launched."
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        assert bool(self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page_seleted()) is True,"tencent app is not highlighted."
        self.fc.kill_tencent_video_process()
        #launch iqiyi app
        self.fc.fd["display_control"].launch_all_apps("爱奇艺+")#to launch iqiyi app
        #app should launched
        assert bool(self.fc.fd["display_control"].verify_iqiyi_app_launch()) is True,"iqiyi app is not launched."
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        assert bool(self.fc.fd["display_control"].verify_display_control_iqiyi_app_ltwo_page_selected()) is True,"iqiyi app is not highlighted."
        self.fc.kill_iqiyi_video_process()
    
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_win_application_settings_oobe_tencent_video_application_C42891319(self):        
        self.fc.fd["display_control"].launch_all_apps("腾讯视频")#to launch tencent app
        assert bool(self.fc.fd["display_control"].verify_tencent_app_launch()) is True,"tencent app is not launched."
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        assert self.fc.fd["display_control"].get_brightness_slider_value() == "100","Brightness slider value is not matching."
        if self.platform.lower() == "bopeep":
            assert self.fc.fd["display_control"].get_display_control_display_modes_select_box_ltwo_page() == "Movie","Display mode is not matching."
        else:
            logging.info("Display mode- movie is not present in platform.")
        if self.platform.lower() in ("willie","thompson", "bucky"):
            assert self.fc.fd["display_control"].get_display_control_hdr_toggle_switch_ltwo_page() == "1", "HDR toggle switch is not matching."
        else:
            logging.info("HDR toggle switch is not present in platform.")
        self.fc.close_myHP()
        self.fc.launch_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        self.fc.swipe_window(direction="down", distance=6)
        display_card_lone_page = self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page()
        assert display_card_lone_page == "Display","Display module is not present."
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()

        assert bool(self.fc.fd["display_control"].validate_display_control_tencent_app_ltwo_page()) is True,"tencent app is not highlighted."
        self.fc.fd["display_control"].launch_all_apps("腾讯视频")#to launch tencent app
        assert bool(self.fc.fd["display_control"].verify_tencent_app_launch()) is True,"tencent app is not launched."
        self.fc.fd["devicesMFE"].click_myhp_on_task_bar()
        assert bool(self.fc.fd["display_control"].verify_display_control_tencent_app_ltwo_page_seleted()) is True,"tencent app is not highlighted."
        self.fc.kill_tencent_video_process()