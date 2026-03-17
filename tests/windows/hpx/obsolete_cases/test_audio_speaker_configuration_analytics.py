from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import logging

pytest.app_info = "HPX"
class Test_Suite_Auido_Speaker_Configuration_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        time.sleep(5)
        cls.fc.close_app()
        cls.fc.launch_app()

    @pytest.mark.require_platform(["unico"])
    def test_01_analytics_for_speaker_configuration_C33352590(self):
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_speaker_tab()
        self.driver.swipe(direction="down", distance=4)
        time.sleep(2)
        #Stereo
        self.fc.fd["audio"].click_stereo_tab()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_externalSpeakerSettings_stereoButton")
        logging.info("{}".format(event))
        assert len(event)>0, "Speaker Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_externalSpeakerSettings_stereoButton", "AUID Field did not generate"
        time.sleep(2)
        #quad
        self.fc.fd["audio"].click_Quad_btn()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_externalSpeakerSettings_quadButton")
        logging.info("{}".format(event))
        assert len(event)>0, "Quad Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_externalSpeakerSettings_quadButton", "AUID Field did not generate"
        time.sleep(2)  
        #Fifty-One
        self.fc.fd["audio"].click_fifty_one_tab()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_externalSpeakerSettings_fiftOneButton")
        logging.info("{}".format(event))
        assert len(event)>0, "Fifty-One Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_externalSpeakerSettings_fiftOneButton", "AUID Field did not generate"
        time.sleep(2)   
        #Multistreaming On
        self.fc.fd["audio"].click_switchSetMultiStreamOn_toggle()
        self.fc.fd["audio"].click_speaker_tab()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_SetupTestSoundComponent_switchSetMultiStreamOn")
        logging.info("{}".format(event))
        assert len(event)>0, "Multi-Streaming On Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onValueChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_SetupTestSoundComponent_switchSetMultiStreamOn", "AUID Field did not generate"
        time.sleep(2)
        #Multistreaming Off
        self.fc.fd["audio"].click_speaker_tab()
        self.driver.swipe(direction="down", distance=4)
        self.fc.fd["audio"].click_switchSetMultiStreamOff_toggle()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_SetupTestSoundComponent_switchSetMultiStreamOff")
        logging.info("{}".format(event))
        assert len(event)>0, "Multi-Streaming Off Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onValueChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_SetupTestSoundComponent_switchSetMultiStreamOff", "AUID Field did not generate"
        time.sleep(2)
        #Hide caret
        self.driver.swipe(direction="down", distance=4)
        self.fc.fd["audio"].click_setup_and_test_soundhide_caret()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_ExternalSpeakerSettings_bottomCaret")
        logging.info("{}".format(event))
        assert len(event)>0, "Hide Caret Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onPress", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_ExternalSpeakerSettings_bottomCaret", "AUID Field did not generate"
        time.sleep(2)
        self.driver.swipe(direction="down", distance=4)