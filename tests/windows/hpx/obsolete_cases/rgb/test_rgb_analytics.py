from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
from SAF.misc import saf_misc
import pytest
import logging
from SAF.misc.ssh_utils import SSH
import time


pytest.app_info = "HPX"
class Test_Suite_RGB_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        cls.driver.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx/properties.json"),cls.remote_artifact_path+"properties.json")
        cls.fc.close_app()
        cls.fc.launch_app()    

    def test_01_analytics_C33328106(self):
        self.driver.swipe(direction="down", distance=3) 
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        self.fc.fd["settings"].click_hp_privacy_settings()
        time.sleep(2)
        self.fc.fd["settings"].click_yes_to_all()
        self.fc.fd["settings"].click_done_button()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        pc_Device_Menu_text = self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        rgb_keyboard_text = self.fc.fd["rgb_keyboard"].verify_rgb_keyboard()
        assert rgb_keyboard_text=="RGB keyboard","RGB keyboard is not visible at PC Device - {}".format(rgb_keyboard_text)
        self.fc.fd["rgb_keyboard"].click_rgb_keyboard()
        event = self.fc.capture_analytics_event("AUID_PCDevicePage_FeatureCard_rgbkeyboard-core")
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcdevice-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_PCDevicePage_FeatureCard_rgbkeyboard-core","AUID Field did not generate"

    def test_02_analytics_for_toggle_button_on_C33328111(self):   
        self.fc.fd["rgb_keyboard"].click_RGB_lighting_toggle_button()
        self.fc.fd["rgb_keyboard"].click_RGB_lighting_toggle_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Switch_Toggle_ON")
        logging.info("{}".format(event))
        assert len(event)>0,"Toggle on Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onValueChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Switch_Toggle_ON","AUID Field did not generate"

    def test_03_analytics_for_toggle_button_off_C33328113(self):
        self.fc.fd["rgb_keyboard"].click_RGB_lighting_toggle_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Switch_Toggle_OFF")
        logging.info("{}".format(event))
        assert len(event)>0,"Toggle off Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onValueChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Switch_Toggle_OFF","AUID Field did not generate"
        self.fc.fd["rgb_keyboard"].click_RGB_lighting_toggle_button() 

    def test_04_analytics_for_brightness_slider_C33328115(self):
        self.fc.fd["rgb_keyboard"].set_slider_value_increase(50)
        self.fc.fd["rgb_keyboard"].set_slider_value_decrease(10)
        self.fc.fd["rgb_keyboard"].set_slider_value_increase(50)
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Slider_Brightness")
        logging.info("{}".format(event))
        assert len(event)>0,"Brightness Slider Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onChangeEnd", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Slider_Brightness","AUID Field did not generate" 

    def test_05_analytics_for_static_effect_C33328116(self):
        static_text=self.fc.fd["rgb_keyboard"].get_static_text()
        assert static_text=="Static","Static tile is not present in RGB keyboard module"
        self.fc.fd["rgb_keyboard"].click_static_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Effects_Static")
        logging.info("{}".format(event))
        assert len(event)>0,"Static Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Effects_Static","AUID Field did not generate"     

    def test_06_analytics_for_wave_effect_C33328118(self):
        wave_text=self.fc.fd["rgb_keyboard"].get_wave_text()
        assert wave_text=="Wave","Wave tile is not present in RGB keyboard module"
        self.fc.fd["rgb_keyboard"].click_wave_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Effects_Wave")
        logging.info("{}".format(event))
        assert len(event)>0,"Wave Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Effects_Wave","AUID Field did not generate"     

    def test_07_analytics_for_ripple_effect_C33328119(self):
        ripple_text=self.fc.fd["rgb_keyboard"].get_ripple_text()
        assert ripple_text=="Ripple","Ripple tile is not present in RGB keyboard module"
        self.fc.fd["rgb_keyboard"].click_ripple_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Effects_Ripple")
        logging.info("{}".format(event))
        assert len(event)>0,"Ripple Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Effects_Ripple","AUID Field did not generate"    

    def test_08_analytics_for_raindrops_effect_C33328132(self):
        raindrops_text=self.fc.fd["rgb_keyboard"].get_raindrops_text()
        assert raindrops_text=="Raindrops","Raindrops tile is not present in RGB keyboard module"
        self.fc.fd["rgb_keyboard"].click_raindrops_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Effects_Raindrops")
        logging.info("{}".format(event))
        assert len(event)>0,"Raindrops Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Effects_Raindrops","AUID Field did not generate"  

    def test_09_analytics_for_breathing_effect_C33328135(self):
        breathing_text=self.fc.fd["rgb_keyboard"].get_breathing_text()
        assert breathing_text=="Breathing","Breathing tile is not present in RGB keyboard module"
        self.fc.fd["rgb_keyboard"].click_breathing_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Effects_Breathing")
        logging.info("{}".format(event))
        assert len(event)>0,"Breathing Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Effects_Breathing","AUID Field did not generate"   

    def test_10_analytics_for_color_cycle_effect_C33328135(self):
        colorcycle_text=self.fc.fd["rgb_keyboard"].get_colorcycle_text()
        assert colorcycle_text=="Color Cycle","Color Cycle tile is not present in RGB keyboard module"
        self.fc.fd["rgb_keyboard"].click_color_cycle_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Effects_ColorCycle")
        logging.info("{}".format(event))
        self.fc.fd["rgb_keyboard"].click_raindrops_button()
        assert len(event)>0,"Color Cycle Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Effects_ColorCycle","AUID Field did not generate"   

    def test_11_analytics_for_blue_color_C33328137(self):
        self.fc.fd["rgb_keyboard"].click_blue_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Color Presets_blue")
        logging.info("{}".format(event))
        assert len(event)>0,"Blue color Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Color Presets_blue","AUID Field did not generate"        

    def test_12_analytics_for_red_color_C33328411(self):
        self.fc.fd["rgb_keyboard"].click_red_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Color Presets_red")
        logging.info("{}".format(event))
        assert len(event)>0,"Red Color Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Color Presets_red","AUID Field did not generate"

    def test_13_analytics_for_purple_color_C33328412(self):
        self.fc.fd["rgb_keyboard"].click_purple_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Color Presets_purple")
        logging.info("{}".format(event))
        assert len(event)>0,"Purple Color Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Color Presets_purple","AUID Field did not generate"    

    def test_14_analytics_for_yellow_color_C33328413(self):  
        self.fc.fd["rgb_keyboard"].click_yellow_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Color Presets_yellow")
        logging.info("{}".format(event))
        assert len(event)>0,"Yellow Color Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Color Presets_yellow","AUID Field did not generate" 

    def test_15_analytics_for_green_color_C33328414(self):
        self.fc.fd["rgb_keyboard"].click_green_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Color Presets_green")
        logging.info("{}".format(event))
        assert len(event)>0,"Green Color Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Color Presets_green","AUID Field did not generate"      

    def test_16_analytics_for_white_color_C33328415(self):
        self.fc.fd["rgb_keyboard"].click_white_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Color Presets_white")
        logging.info("{}".format(event))
        assert len(event)>0,"White Color Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Color Presets_white","AUID Field did not generate"  

    def test_17_analytics_for_cyan_color_C33328467(self):
        self.fc.fd["rgb_keyboard"].click_cyan_button()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Color Presets_cyan")
        logging.info("{}".format(event))
        assert len(event)>0,"Cyan Color Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Color Presets_cyan","AUID Field did not generate"    

    def test_18_analytics_for_restore_settings_button_C33328500(self):
        self.driver.swipe(direction="down", distance=2)   
        self.fc.fd["rgb_keyboard"].click_restore_default_tab()
        event = self.fc.capture_analytics_event("AUID_RGB_KEYBOARD_Home_Btn_Restore_default_settings")
        logging.info("{}".format(event)) 
        assert len(event)>0,"Restore Defaults Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="rgbkeyboard-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_RGB_KEYBOARD_Home_Btn_Restore_default_settings","AUID Field did not generate"  
        self.fc.close_app()
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
