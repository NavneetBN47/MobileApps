import pytest

pytest.app_info = "JWEB"

class Test_Suite_01_event_plugin_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.event_plugin = cls.fc.fd["event_plugin"]
        cls.console = cls.fc.fd["console"]

    @pytest.fixture(scope="function", autouse=True)
    def eventing_test_setup(self):
        self.fc.flow_load_home_screen()
        self.console.select_toggle_expand_console()
        self.home.select_plugin_from_home("eventing")

    def test_01_verify_event_plugin(self):
        """
        C28698085: Validating the Eventing API to send the information from a JWebView to the native side of the application
            - After navigating to Eventing Plugin, click on "Test" button under Eventing.dispatchEvent()
            - Expecting "Event Sent" message to be displayed under result
        """
        self.event_plugin.select_eventing_plugin_test()
        assert self.event_plugin.eventing_test_result() == "Event Sent!"

    def test_02_verify_event_plugin_jarvis_event(self):
        """
        C28698087: Verify whether Eventing plugin can send reserved Jarvis events from Jweb to the native side
            - After navigating to Eventing Plugin 
            - Under Eventing.DispatchEvents() Reserved Jarvis Events ensure a Reserved Jarvis event is chosen
            - Click on "Test" button 
            - Expecting "Event Sent!" message to be displayed under result
        """
        self.event_plugin.select_jarvis_event_option_test()
        self.driver.swipe(direction="down")
        assert self.event_plugin.jarvis_event_option_test_result() == "jarvisEventFinished Event Sent!"

    def test_03_verify_event_plugin_add_listener(self):
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
        self.driver.swipe(direction="down")
        self.event_plugin.enter_add_listener_event(option="UpdateDeviceInfo")
        self.event_plugin.select_add_listener_test_btn()
        assert self.event_plugin.add_listener_test_result() == "Listener for UpdateDeviceInfo has been added"
        self.event_plugin.select_eventing_plugin_test()
        toast_notification_text = self.event_plugin.get_add_listener_pop_up_toast_text()
        assert toast_notification_text['main_text'] == "Event UpdateDeviceInfo Recieved from Native"
        assert toast_notification_text['sub_text'] == '{"deviceId":"abcdef123456","status":"exploded"}'
        self.event_plugin.select_add_listener_pop_up_close_btn()
        assert self.event_plugin.add_listener_event_result() == {'deviceId': 'abcdef123456', 'status': 'exploded'}

        self.event_plugin.enter_add_listener_event(option="jarvisEventFinished")
        assert self.event_plugin.add_listener_test_result() == "Listener for jarvisEventFinished has been added"
        self.event_plugin.select_eventing_plugin_test()
        toast_notification_text = self.event_plugin.get_add_listener_pop_up_toast_text()
        assert toast_notification_text['main_text'] == "Event UpdateDeviceInfo Recieved from Native"
        assert toast_notification_text['sub_text'] == '{"deviceId":"abcdef123456","status":"exploded"}'
        self.event_plugin.select_add_listener_pop_up_close_btn()
        assert self.event_plugin.add_listener_multiple_event_results() == '{"deviceId":"abcdef123456","status":"exploded"}\n{"deviceId":"abcdef123456","status":"exploded"}'