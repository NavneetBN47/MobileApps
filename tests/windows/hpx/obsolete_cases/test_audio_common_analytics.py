from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import logging

pytest.app_info = "HPX"
class Test_Suite_Audio_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.delete_capture_analytics_files()
        time.sleep(3)
    
    def test_01_analytics_C33352572(self):
        self.driver.swipe(direction="down", distance=3) 
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCDevicePage_FeatureCard_pcaudio-core")
        time.sleep(10)
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcdevice-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCDevicePage_FeatureCard_pcaudio-core","AUID Field did not generate"
    
    def test_02_audio_level_output_slider_C33352579(self):
        self.fc.fd["audio"].set_slider_value(20,"output_slider")
        self.fc.fd["audio"].set_slider_value(50,"output_slider")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_AudioOutput_outputSlider_Master_Volume")
        time.sleep(5)
        logging.info("{}".format(event))
        assert len(event) > 0, "Audio Level output event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onSlidingComplete", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCAudio_AudioOutput_outputSlider_Master_Volume", "AUID Field did not generate"

    def test_03_audio_level_input_slider_C36935242(self):
        self.fc.fd["audio"].set_slider_value(20,"input_slider")
        self.fc.fd["audio"].set_slider_value(50,"input_slider")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_AudioInput_outputSlinputSlider_Master_Volumeider_Master_Volume")
        time.sleep(5)
        logging.info("{}".format(event))
        assert len(event) > 0, "Audio Level input event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onSlidingComplete", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCAudio_AudioInput_outputSlinputSlider_Master_Volumeider_Master_Volume", "AUID Field did not generate"
 
    def test_04_audio_level_output_mute_C36935243(self):
        self.fc.fd["audio"].click_output_mute_button()
        output_mute = self.fc.fd["audio"].get_output_mute_button_name()
        if "On" in output_mute:
            self.fc.fd["audio"].click_output_mute_button()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_AudioOutput_Button_mute")
        time.sleep(5)
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcaudio-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCAudio_AudioOutput_Button_mute","AUID Field did not generate"
        
    def test_05_audio_level_input_mute_C36935244(self):
        self.fc.fd["audio"].click_input_mute_button()
        input_mute = self.fc.fd["audio"].get_input_mute_button_name()
        if "On" in input_mute:
            self.fc.fd["audio"].click_input_mute_button()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_AudioInput_Button_mic")
        time.sleep(5)
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcaudio-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCAudio_AudioInput_Button_mic","AUID Field did not generate"

    def test_06_audio_noise_removal_C33352580(self):
        if self.fc.fd["audio"].wait_noise_removal_toggle_on() is True:
            self.fc.fd["audio"].click_noise_removal_ontoggle()
        self.fc.fd["audio"].click_noise_removal_offtoggle()
        assert self.fc.fd["audio"].wait_noise_removal_toggle_on() is True
        self.fc.fd["audio"].click_noise_removal_ontoggle()
        assert self.fc.fd["audio"].wait_noise_removal_toggle_on() is False
        event = self.fc.capture_analytics_event("AUID_PCAudio_NoiseRemovalComponent_switchNoiseRemoval_Off")
        time.sleep(5)
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onValueChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcaudio-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCAudio_NoiseRemovalComponent_switchNoiseRemoval_Off","AUID Field did not generate"
        event = self.fc.capture_analytics_event("AUID_PCAudio_NoiseRemovalComponent_switchNoiseRemoval_On")
        time.sleep(5)
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onValueChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcaudio-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCAudio_NoiseRemovalComponent_switchNoiseRemoval_On","AUID Field did not generate"

    def test_07_audio_noise_reduction_C36963426(self):
        if self.fc.fd["audio"].wait_noise_reduction_toggle_on() is False:
            self.fc.fd["audio"].click_noise_reduction_offtoggle()
        self.fc.fd["audio"].click_noise_reduction_ontoggle()
        assert self.fc.fd["audio"].wait_noise_reduction_toggle_on() is False
        self.fc.fd["audio"].click_noise_reduction_offtoggle()
        assert self.fc.fd["audio"].wait_noise_reduction_toggle_on() is True
        event = self.fc.capture_analytics_event("AUID_PCAudio_NoiseReductionComponent_switchNoiseReduction_On")
        time.sleep(5)
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onValueChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcaudio-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCAudio_NoiseReductionComponent_switchNoiseReduction_On","AUID Field did not generate"
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCAudio_NoiseReductionComponent_switchNoiseReduction_Off")
        time.sleep(5)
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onValueChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="pcaudio-core","ScreenName field name did not generate"
        assert event["12"]=="AUID_PCAudio_NoiseReductionComponent_switchNoiseReduction_Off","AUID Field did not generate"
