import pytest
from MobileApps.resources.const.web.const import TEST_DATA 

pytest.app_info = "JWEB"

class Test_Suite_01_Eventing_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, jweb_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_test_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.eventing_plugin = cls.fc.fd["eventing_plugin"]

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_eventing_plugin(self):
        if not self.eventing_plugin.verify_at_eventing_plugin():
            self.home.select_webview_mode(raise_e=False)
            self.home.select_jweb_reference_btn(raise_e=False)
            self.home.select_url_go_btn(raise_e=False)
            self.home.select_plugin_from_home("eventing")

    def test_01_verify_event_plugin(self):
        """
        C28698085: Validating the Eventing API to send the information from a JWebView to the native side of the application
            - After navigating to Eventing Plugin, click on "Test" button under Eventing.dispatchEvent()
            - Expecting "Event Sent" message to be displayed under result
        """
        self.eventing_plugin.select_eventing_plugin_test()
        assert self.eventing_plugin.eventing_test_result() == "Event Sent!"
    
    def test_02_verify_event_plugin_jarvis_event(self):
        """
        C28698087: Verify whether Eventing plugin can send reserved Jarvis events from Jweb to the native side
            - after navigating to Eventing Plugin 
            - Under Eventing.DispatchEvents() Reserved Jarvis Events ensure a Reserved Jarvis event is chosen
            - Click on "Test" button 
            - Expecting "Event Sent!" message to be displayed under result
        """
        self.eventing_plugin.select_jarvis_event_option_test()
        assert self.eventing_plugin.jarvis_event_option_test_result() == "Event Sent!"
        
    def test_03_verify_event_plugin_add_listener(self):
        """
        C28698086: Verify whether Eventing plugin can add an event listener for events sent from the native side.
            - After navigating to the Eventing plugin, go to addListener() and type the name of the event (updateDeviceInfo) and click "Test"
            - Add same Event Name under Eventing.dispatchEvent() section and click on "Test" button 
            - Expecting toast message with the event received from Native
        """
        self.eventing_plugin.enter_add_listener_event(option="UpdateDeviceInfo")
        self.eventing_plugin.select_add_listener_test_btn()
        assert self.eventing_plugin.add_listener_test_result() == "Listener for UpdateDeviceInfo has been added"
        self.eventing_plugin.select_eventing_plugin_test()
        toast_notification_text = self.eventing_plugin.get_add_listener_pop_up_toast_text()
        self.eventing_plugin.close_all_toast_notification()
        assert toast_notification_text == {"deviceId":"abcdef123456","status":"exploded"}
        assert self.eventing_plugin.add_listener_event_result() == {'deviceId': 'abcdef123456', 'status': 'exploded'}
    
    def test_04_verify_event_plugin_(self):
        """
        C28698088: Verify whether Eventing plugin can add an event listener for events sent from the native side -Jarvis reserved events
            - After navigating to Eventing Plugin, go to addListener() and type the name of the Jarvis Reserved Event (jarvisEventFinished)
            - Click on "Test" button under Eventing.dispatchEvent() Reserved Jarvis Events 
            - Expecting "jarvisEventFinished Event Sent! message to be displayed under result
        """
        self.eventing_plugin.enter_add_listener_event(option="jarvisEventFinished")
        self.eventing_plugin.select_add_listener_test_btn()
        assert self.eventing_plugin.add_listener_test_result() == "Listener for jarvisEventFinished has been added"
        self.eventing_plugin.select_jarvis_event_option_test()
        toast_notification_text = self.eventing_plugin.get_add_listener_pop_up_toast_text()
        assert toast_notification_text == {"status":"userFinishedFlow"}