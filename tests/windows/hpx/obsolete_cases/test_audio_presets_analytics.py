from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import logging

pytest.app_info = "HPX"
class Test_Suite_Audio_Presets_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.delete_capture_analytics_files()
        time.sleep(3)

    @pytest.mark.exclude_platform(["grogu","london"])
    def test_01_audio_presets_analytics_C33352581(self):
        self.fc.restart_app()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_preset_movie()
        self.fc.close_app()
        time.sleep(2)
        self.fc.launch_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio() 
        time.sleep(5)

        self.fc.fd["audio"].click_preset_music()
        time.sleep(2)
        self.fc.fd["audio"].click_preset_voice()
        time.sleep(2)
        self.fc.fd["audio"].click_preset_movie()
        time.sleep(2)

        event = self.fc.capture_analytics_event("AUID_PCAudio_Presets_Music_RadioButton")
        logging.info("{}".format(event))
        assert len(event)>0, "Music Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_Presets_Music_RadioButton", "AUID Field did not generate"
        time.sleep(2)

        event = self.fc.capture_analytics_event("AUID_PCAudio_Presets_Voice_RadioButton")
        logging.info("{}".format(event))
        assert len(event)>0, "Voice Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_Presets_Voice_RadioButton", "AUID Field did not generate"
        time.sleep(2)

        event = self.fc.capture_analytics_event("AUID_PCAudio_Presets_Movie_RadioButton")
        logging.info("{}".format(event))
        assert len(event)>0, "Movie Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_Presets_Movie_RadioButton", "AUID Field did not generate"
        time.sleep(2)

        
    @pytest.mark.require_platform(["grogu", "london"])
    def test_02_audio_presets_auto_analytics_C40202303(self):
        self.fc.restart_app()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_preset_music()
        self.fc.close_app()
        self.fc.launch_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio() 
        self.fc.fd["audio"].click_preset_auto()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_Presets_Auto_RadioButton")
        logging.info("{}".format(event))
        assert len(event)>0, "Auto Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] =="AUID_PCAudio_Presets_Auto_RadioButton", "AUID Field did not generate"
        time.sleep(2)