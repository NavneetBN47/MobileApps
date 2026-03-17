import pytest

pytest.app_info = "JWEB"

class Test_Suite_01_Eventing_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.event_plugin = cls.fc.fd["event_plugin"]
        cls.console = cls.fc.fd["console"]
        
    def test_01_verify_event_plugin(self):
        """
        C28698085: Validating the Eventing API to send the information from a JWebView to the native side of the application
            - After navigating to Eventing Plugin, click on "Test" button under Eventing.dispatchEvent()
            - Expecting "Event Sent" message to be displayed under result
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("eventing")
        self.event_plugin.select_eventing_plugin_test()
        assert self.event_plugin.eventing_test_result() == "Event Sent!"

    def test_02_verify_event_plugin_plugin_jarvis_event(self):
        """
        C28698087: Verify whether Eventing plugin can send reserved Jarvis events from Jweb to the native side
            - Navigate to Eventing Plugin 
            - Under Eventing.DispatchEvents() Reserved Jarvis Events, ensure a Reserved Jarvis event is chosen
            - Click on "Test" button 
            - Expecting "Event Sent!" message to be displayed under result
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("eventing")
        self.event_plugin.select_jarvis_event_option_test()
        assert self.event_plugin.jarvis_event_option_test_result() == "jarvisEventFinished Event Sent!"

    def test_03_verify_event_plugin_plugin_add_listener(self):
        """
        C28698086: Verify whether Eventing plugin can add an event listener for events sent from the native side.
            - After navigating to the Eventing plugin, go to addListener() and type the name of the event (updateDeviceInfo) and click "Test"
            - Add same Event Name under Eventing.dispatchEvent() section and click on "Test" button 
            - Expecting toast message with the event received from Native
        C28698088: Verify whether Eventing plugin can add an event listener for events sent from the native side -Jarvis reserved events
            - After navigating to Eventing Plugin, go to addListener() and type the name of the Jarvis Reserved Event (jarvisEventFinished)
            - Click on "Test" button under Eventing.dispatchEvent() Reserved Jarvis Events 
            - Expecting "jarvisEventFinished Event Sent! message to be displayed under result
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("eventing")
        self.event_plugin.enter_add_listener_event(option="UpdateDeviceInfo")
        self.event_plugin.select_add_listener_test_btn()
        assert self.event_plugin.add_listener_test_result() == "Listener for UpdateDeviceInfo has been added"
        self.event_plugin.select_eventing_plugin_test()
        assert "UpdateDeviceInfo" in self.console.get_console_text()
        assert '["deviceId": abcdef123456, "status": exploded]' in self.console.get_console_text() or '["status": exploded, "deviceId": abcdef123456]' in self.console.get_console_text()
        self.event_plugin.select_add_listener_pop_up_close_btn()
        assert self.event_plugin.add_listener_event_result() == {"deviceId":"abcdef123456","status":"exploded"}
        self.event_plugin.enter_event_name_dispatch_event("jarvisEventFinished")
        self.event_plugin.enter_add_listener_event(option="jarvisEventFinished")
        self.event_plugin.select_add_listener_test_btn()
        assert self.event_plugin.add_listener_test_result() == "Listener for jarvisEventFinished has been added"
        self.event_plugin.select_jarvis_event_option_test()
        assert "jarvisEventFinish" in self.console.get_console_text()
        assert '["status": userFinishedFlow]' in self.console.get_console_text()