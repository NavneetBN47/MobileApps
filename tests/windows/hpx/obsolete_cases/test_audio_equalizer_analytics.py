from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time
import logging

pytest.app_info = "HPX"
soft_assertion = SoftAssert()
class Test_Suite_Audio_Equalizer_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.delete_capture_analytics_files()
        time.sleep(3)
    
    @pytest.mark.consumer
    @pytest.mark.analytics
    def test_01_analytics_for_equalizer_10bar_C40287790(self):
        self.fc.restart_app()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.driver.swipe(direction="down", distance=4)
        time.sleep(2)
        #Equalizer 10 band
        #32
        self.fc.fd["audio"].set_EQ_slider_value(20,"equalizer_slider_32volume")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BandEqComponent_32Slider")
        time.sleep(2)
        logging.info("{}".format(event))
        soft_assertion.assert_true(len(event) > 0, "32 Slider event not found")
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onSlidingComplete", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcaudio-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCAudio_BandEqComponent_32Slider", "AUID Field did not generate")
        time.sleep(2)
        #64
        self.fc.fd["audio"].set_EQ_slider_value(20,"equalizer_slider_64volume")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BandEqComponent_64Slider")
        time.sleep(2)
        logging.info("{}".format(event))
        soft_assertion.assert_true(len(event) > 0, "64 Slider event not found")
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onSlidingComplete", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcaudio-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCAudio_BandEqComponent_64Slider", "AUID Field did not generate")
        time.sleep(2)
        #125
        self.fc.fd["audio"].set_EQ_slider_value(20,"equalizer_slider_125volume")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BandEqComponent_125Slider")
        logging.info("{}".format(event))
        soft_assertion.assert_true(len(event) > 0, "125 Slider event not found")
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onSlidingComplete", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcaudio-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCAudio_BandEqComponent_125Slider", "AUID Field did not generate")
        time.sleep(2)
        #250
        self.fc.fd["audio"].set_EQ_slider_value(20,"equalizer_slider_250volume")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BandEqComponent_250Slider")
        logging.info("{}".format(event))
        soft_assertion.assert_true(len(event) > 0, "250 Slider event not found")
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onSlidingComplete", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcaudio-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCAudio_BandEqComponent_250Slider", "AUID Field did not generate")
        time.sleep(2)
        #500
        self.fc.fd["audio"].set_EQ_slider_value(20,"equalizer_slider_500volume")       
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BandEqComponent_500Slider")
        logging.info("{}".format(event))
        soft_assertion.assert_true(len(event) > 0, "500 Slider event not found")
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onSlidingComplete", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcaudio-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCAudio_BandEqComponent_500Slider", "AUID Field did not generate")
        time.sleep(2)
        #1k
        self.fc.fd["audio"].set_EQ_slider_value(20,"equalizer_slider_1kvolume")
        time.sleep(2) 
        event = self.fc.capture_analytics_event("AUID_PCAudio_BandEqComponent_1kSlider")
        logging.info("{}".format(event))
        soft_assertion.assert_true(len(event) > 0, "1k Slider event not found")
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onSlidingComplete", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcaudio-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCAudio_BandEqComponent_1kSlider", "AUID Field did not generate")
        time.sleep(2)
        #2k
        self.fc.fd["audio"].set_EQ_slider_value(20,"equalizer_slider_2kvolume")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BandEqComponent_2kSlider")
        time.sleep(2)
        logging.info("{}".format(event))
        soft_assertion.assert_true(len(event) > 0, "2k Slider event not found")
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onSlidingComplete", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcaudio-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCAudio_BandEqComponent_2kSlider", "AUID Field did not generate")
        time.sleep(2)
        #4k
        self.fc.fd["audio"].set_EQ_slider_value(20,"equalizer_slider_4kvolume")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BandEqComponent_4kSlider")
        time.sleep(2)
        logging.info("{}".format(event))
        soft_assertion.assert_true(len(event) > 0, "4k Slider event not found")
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onSlidingComplete", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcaudio-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCAudio_BandEqComponent_4kSlider", "AUID Field did not generate")
        time.sleep(2)
        #8k
        self.fc.fd["audio"].set_EQ_slider_value(20,"equalizer_slider_8kvolume")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BandEqComponent_8kSlider")
        time.sleep(2)
        logging.info("{}".format(event))
        soft_assertion.assert_true(len(event) > 0, "8k Slider event not found")
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onSlidingComplete", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcaudio-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCAudio_BandEqComponent_8kSlider", "AUID Field did not generate")
        time.sleep(2)
        #16k
        self.fc.fd["audio"].set_EQ_slider_value(20,"equalizer_slider_16kvolume")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BandEqComponent_16kSlider")
        time.sleep(2)
        logging.info("{}".format(event))
        soft_assertion.assert_true(len(event) > 0, "16k Slider event not found")
        soft_assertion.assert_equal(event["2"], "Navigation", "EventCategory field name did not generate")
        soft_assertion.assert_equal(event["3"], "onSlidingComplete", "EventType field name did not generate")
        soft_assertion.assert_equal(event["4"], "UserEngaged", "EventName field name did not generate")
        soft_assertion.assert_equal(event["11"], "pcaudio-core", "ScreenName field name did not generate")
        soft_assertion.assert_equal(event["12"], "AUID_PCAudio_BandEqComponent_16kSlider", "AUID Field did not generate")

        self.fc.fd["audio"].set_EQ_slider_value(50,"equalizer_slider_32volume")
        self.fc.fd["audio"].set_EQ_slider_value(50,"equalizer_slider_64volume")
        self.fc.fd["audio"].set_EQ_slider_value(50,"equalizer_slider_125volume")
        self.fc.fd["audio"].set_EQ_slider_value(50,"equalizer_slider_250volume")
        self.fc.fd["audio"].set_EQ_slider_value(50,"equalizer_slider_500volume")
        self.fc.fd["audio"].set_EQ_slider_value(50,"equalizer_slider_1kvolume")
        self.fc.fd["audio"].set_EQ_slider_value(50,"equalizer_slider_2kvolume")
        self.fc.fd["audio"].set_EQ_slider_value(50,"equalizer_slider_4kvolume")
        self.fc.fd["audio"].set_EQ_slider_value(50,"equalizer_slider_8kvolume")
        self.fc.fd["audio"].set_EQ_slider_value(50,"equalizer_slider_16kvolume")

        soft_assertion.raise_assertion_errors()
        
    @pytest.mark.consumer
    @pytest.mark.analytics
    # @pytest.mark.require_platform(["grogu", "london"])
    #Currently automation is blocked by HPXWC-18613, skip this case and set status to “in progress” in TestRail.
    @pytest.mark.require_platform(["block"])
    def test_02_analytics_for_equalizer_3bar_C33352583(self):
        self.fc.restart_app()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.driver.swipe(direction="down", distance=4)
        time.sleep(2)
        #Bass
        self.fc.fd["audio"].click_preset_music()
        self.fc.fd["audio"].set_slider_value(50,"bass_slider")
        self.fc.fd["audio"].set_slider_value(20,"bass_slider")
        time.sleep(5)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BasicEQ_bassSlider")
        logging.info("{}".format(event))
        assert len(event)>0, "Bass Analytics event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onSlidingComplete", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCAudio_BasicEQ_bassSlider", "AUID Field did not generate"
        #Width
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value(75,"width_slider")
        self.fc.fd["audio"].set_slider_value(15,"width_slider")
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_PCAudio_BasicEQ_widthSlider")
        logging.info("{}".format(event))
        assert len(event)>0, "Width event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onSlidingComplete", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCAudio_BasicEQ_widthSlider", "AUID Field did not generate"
        #Treble
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value(45,"treble_slider")
        self.fc.fd["audio"].set_slider_value(20,"treble_slider")
        event = self.fc.capture_analytics_event("AUID_PCAudio_BasicEQ_trebleSlider")
        time.sleep(2)
        logging.info("{}".format(event))
        assert len(event)>0, "Treble event not found"
        assert event["2"] == "Navigation", "EventCategory field name did not generate"
        assert event["3"] == "onSlidingComplete", "EventType field name did not generate"
        assert event["4"] == "UserEngaged", "EventName field name did not generate"
        assert event["11"] == "pcaudio-core", "ScreenName field name did not generate"
        assert event["12"] == "AUID_PCAudio_BasicEQ_trebleSlider", "AUID Field did not generate"
