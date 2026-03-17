from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import logging

pytest.app_info = "HPX"
class Test_Suite_Audio_Studio_Recording_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()

    
    def test_01_audio_studion_analytics_C38058157(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].verify_studio_recording_checkbox_show()
        self.fc.fd["audio"].select_studio_recording()
        event = self.fc.capture_analytics_event("AUID_PCAudio_MicModeComponent_Studio Recording_RadioButton")
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onChange", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"]=="AUID_PCAudio_MicModeComponent_Studio Recording_RadioButton","AUID Field did not generate"

