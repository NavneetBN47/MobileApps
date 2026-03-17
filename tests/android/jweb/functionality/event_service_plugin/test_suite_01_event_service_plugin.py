import pytest
from MobileApps.resources.const.web.const import TEST_DATA 
from time import sleep

pytest.app_info = "JWEB"

class Test_Suite_01_Event_Service_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.console = cls.fc.fd["console"]
        cls.event_service_plugin = cls.fc.fd["event_service_plugin"]

    @pytest.fixture(scope="function")
    def create_and_select_new_subscriber(self):
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.enter_create_subscriber_id_text("new subscriber")
        self.event_service_plugin.select_create_subscriber_btn()
        self.event_service_plugin.select_first_subscriber()

    def test_01_subscribe_to_valid_event(self, create_and_select_new_subscriber):
        """
        C29361605: Subscribe to an event using valid eventName and publisherID, expecting 'Subscription was created' toast notification
        C29361607: Subscribe to the same event twice, expecting 'Subscription was created' toast notification
        """
        self.event_service_plugin.enter_subscribe_event_name_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.reference.app.newpublisher")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        assert 'com.hp.jarvis.event.newevent' == self.event_service_plugin.get_subscription_generated_event_name_text()
        assert 'com.hp.jarvis.reference.app.newpublisher' == self.event_service_plugin.get_subscription_generated_publisher_id_text()
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        assert 'com.hp.jarvis.event.newevent' == self.event_service_plugin.get_subscription_generated_event_name_text(index=1)
        assert 'com.hp.jarvis.reference.app.newpublisher' == self.event_service_plugin.get_subscription_generated_publisher_id_text(index=1)

    @pytest.mark.parametrize("subscription_options", [("", "com.hp.jarvis.reference.app.newpublisher"), ("com.hp.jarvis.event.newevent", ""), ("", "")])
    def test_02_subscribe_to_event_without_names(self, create_and_select_new_subscriber, subscription_options):
        """
        C29361609: Subscribe to an event using empty eventName, expecting 'not informed' error toast notification
        C29361610: Subscribe to an event using an empty publisher, expecting 'Subscription was created' toast notification
        C29457917: Subscribe to an event using empty eventName and empty publisherId, expecting 'provided eventName and publisherId is null or empty' toast notification
        """
        self.event_service_plugin.enter_subscribe_event_name_text(subscription_options[0])
        self.event_service_plugin.enter_subscribe_publisher_id_text(subscription_options[1])
        self.event_service_plugin.select_subscribe_btn()
        if subscription_options[0] == "" and subscription_options[1] == "":
            assert "empty" in self.event_service_plugin.get_toast_text().lower()
        else:
            assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
            expected_event_name = "not informed" if subscription_options[0] == "" else subscription_options[0]
            expected_publisher_id = "not informed" if subscription_options[1] == "" else subscription_options[1]
            assert expected_event_name == self.event_service_plugin.get_subscription_generated_event_name_text().lower()
            assert expected_publisher_id == self.event_service_plugin.get_subscription_generated_publisher_id_text().lower()

    @pytest.mark.parametrize("unsubscription_options", [("com.hp.jarvis.event.newevent", "com.hp.jarvis.reference.app.newpublisher"), ("com.hp.jarvis.event.newevent", ""),\
                                                        ("", "com.hp.jarvis.reference.app.newpublisher"), ("", "")])
    def test_03_unsubscribe_to_valid_event(self, create_and_select_new_subscriber, unsubscription_options):
        """
        C29361611: Unsubscribe from an event with specific eventName and specific publisherId
        C29361612: Unsubscribe from an event only using eventName
        C29361613: Unsubscribe from an event only using publisherId
        C29361614: Unsubscribe from all events

        For all tests, expecting "unsubscribed" toast notification
        """
        self.event_service_plugin.enter_subscribe_event_name_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.reference.app.newpublisher")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        assert 'com.hp.jarvis.event.newevent' == self.event_service_plugin.get_subscription_generated_event_name_text()
        assert 'com.hp.jarvis.reference.app.newpublisher' == self.event_service_plugin.get_subscription_generated_publisher_id_text()
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        assert 'com.hp.jarvis.event.newevent' == self.event_service_plugin.get_subscription_generated_event_name_text(index=1)
        assert 'com.hp.jarvis.reference.app.newpublisher' == self.event_service_plugin.get_subscription_generated_publisher_id_text(index=1)
        self.event_service_plugin.enter_unsubscribe_event_name_text(unsubscription_options[0])
        self.event_service_plugin.enter_unsubscribe_publisher_id_text(unsubscription_options[1])
        self.event_service_plugin.select_unsubscribe_btn()
        assert "unsubscribed" in self.event_service_plugin.get_toast_text().lower()
        assert False is self.event_service_plugin.get_subscription_generated_publisher_id_text(raise_e=False)
        assert False is self.event_service_plugin.get_subscription_generated_event_name_text(raise_e=False)

    @pytest.mark.parametrize("publish_options", [("com.hp.jarvis.event.newevent", '{"name1": "Tony", "name2": "Bruce"}'), ("", '{"name1": "Tony", "name2": "Bruce"}'), \
                                                 ("com.hp.jarvis.event.newevent", '{Guys:"name1":"Tony","name2":"Bruce"}'), ("com.hp.jarvis.event.newevent", '')])
    def test_04_publish_an_event(self, publish_options):
        """
        C29361618: Publish an event with valid eventName and eventName, expecting recieved event in app console
        C29361619: Publish an event with a blank eventName, expecting an 'invalidIdentifier' error toast message
        C29361621: Publish an event not using formatted JSON, expeting a 'EventData should be in JSON' error toast message
        C29376250: Publish an event using blank event data, expecting recieved event in app console
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.select_create_publisher_btn()
        self.event_service_plugin.select_first_publisher()
        self.event_service_plugin.enter_publisher_event_name_text(publish_options[0])
        self.event_service_plugin.enter_publisher_event_data_text(publish_options[1])
        self.event_service_plugin.select_publish_btn()
        if publish_options[0] == "":
            assert "invalididentifier" in self.event_service_plugin.get_toast_text().lower()
        elif publish_options[1] != '{"name1": "Tony", "name2": "Bruce"}':
            "eventdata should be in json format" in self.event_service_plugin.get_toast_text().lower()
        elif publish_options[1] == '':
            assert "event published" in self.event_service_plugin.get_toast_text().lower()
            assert "received an event" in self.console.get_console_text()
            assert '{}' in self.console.get_console_text()
        else:
            assert "event published" in self.event_service_plugin.get_toast_text().lower()
            assert "received an event" in self.console.get_console_text()
            assert '{"name1":"Tony","name2":"Bruce"}' in self.console.get_console_text()

    @pytest.mark.parametrize("subscribers_list", [("subscriber1"), ("subscriber2"), ("subscriber3")])
    def test_05_create_two_or_more_subscribers(self, subscribers_list):
        """
        C29223592: Create a subscriber
        C44278950: Create two or more subscribers
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers_list[0])
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()

    def test_06_delete_a_subscriber(self):
        """
        C29223593: Delete a subscriber, expecting 'Subscriber Destroyed!' toast notification
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.enter_create_subscriber_id_text("new subscriber")
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_delete_subscriber_btn()
        assert "subscriber destroyed!" in self.event_service_plugin.get_toast_text().lower()

    @pytest.mark.parametrize("subscribers", [("subscriber1", "subscriber2")])
    def test_07_delete_first_subscriber_from_subscriber_list(self, subscribers):
        """
        C29408724: Delete first subscriber from subscriber list, expecting 'Subscriber Destroyed' toast notification
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers[0])
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_delete_subscriber_btn()
        assert "subscriber destroyed!" in self.event_service_plugin.get_toast_text().lower()

    def test_08_subscribe_event_using_valid_eventName_publisherID_and_callback_option(self, create_and_select_new_subscriber):
        """
        C29223599: Subscribe to an event using valid eventName, publisherID and callback option
        """
        self.event_service_plugin.enter_subscribe_event_name_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.reference.app.newpublisher")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        assert 'com.hp.jarvis.event.newevent' == self.event_service_plugin.get_subscription_generated_event_name_text()
        assert 'com.hp.jarvis.reference.app.newpublisher' == self.event_service_plugin.get_subscription_generated_publisher_id_text()

    @pytest.mark.parametrize("subscribers", [("subscriber1", "subscriber2", "subscriber3")])
    def test_09_create_three_subscriber_with_same_valid_fields_with_persistant_value_false(self, subscribers):
        """
        C44278966: Create two or three subscriber with same valid fields with persistant value as false
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers[0])
        self.event_service_plugin.select_persistent_drop_down_menu()
        self.event_service_plugin.select_persistent_option_from_menu("false")
        self.event_service_plugin.select_create_subscriber_btn() 
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()

    @pytest.mark.parametrize("subscribers", [("subscriber1", "subscriber2", "subscriber3")])
    def test_10_create_three_subscriber_with_same_valid_fields_with_persistant_value_true(self, subscribers):
        """
        C44279013: Create two or three subscriber with same valid fields with persistant value as true
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers[0])
        self.event_service_plugin.select_persistent_drop_down_menu()
        self.event_service_plugin.select_persistent_option_from_menu("true")
        self.event_service_plugin.select_create_subscriber_btn() 
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()  

    def test_11_verify_pause_resume_options_ispersistent_if_false(self):
        """
        C32374244: Verify pause and resume options if isPersistent is false
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.enter_create_subscriber_id_text("test123")
        self.event_service_plugin.select_persistent_drop_down_menu()
        self.event_service_plugin.select_persistent_option_from_menu("false")
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_create_publisher_btn()
        assert "publisher was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_first_subscriber()
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.new.app.publisher")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        sleep(3)
        self.event_service_plugin.select_pause_btn()
        assert "subscribernotpersistent" in self.event_service_plugin.get_toast_text().lower()
        sleep(3)
        self.event_service_plugin.select_resume_btn()
        assert "subscribernotpersistent" in self.event_service_plugin.get_toast_text().lower()

    def test_12_verify_pause_resume_options_ispersistent_if_true(self):
        """
        C32374245: Verify pause and resume options if isPersistent is true
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.enter_create_subscriber_id_text("test123")
        self.event_service_plugin.select_persistent_drop_down_menu()
        self.event_service_plugin.select_persistent_option_from_menu("true")
        self.event_service_plugin.select_create_subscriber_btn() 
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_create_publisher_btn()
        assert "publisher was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_first_subscriber()
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        sleep(3)
        self.event_service_plugin.select_pause_btn()
        assert "events paused!" in self.event_service_plugin.get_toast_text().lower()
        sleep(3)
        self.event_service_plugin.select_resume_btn()
        assert "events resumed!" in self.event_service_plugin.get_toast_text().lower()

    def test_13_create_publisher_using_valid_and_invalid_publisher_id(self):
        """
        C32374230: Create a publisher using a valid publisherId, expecting 'Publisher was created!' toast notification
        C32374232: Create a publisher using a blank publisherId, expecting 'invalididentifier' toast notification
        C32374231: Create a publisher using a existing publisherID, expecting 'Publisher was created!' toast notification
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.enter_create_publisher_id_text("com.hp.jarvis.new.app.publisher")
        self.event_service_plugin.select_create_publisher_btn()
        assert "publisher was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.enter_create_publisher_id_text("com.hp.jarvis.new.app.publisher")
        self.event_service_plugin.select_create_publisher_btn()
        assert "already exists!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.enter_create_publisher_id_text(" ")
        self.event_service_plugin.select_create_publisher_btn()
        assert "invalididentifier" in self.event_service_plugin.get_toast_text().lower()

    def test_14_delete_a_publisher(self):
        """
        C32374233: Delete a publisher, expecting 'Publisher Destroyed!' toast notification
        """
        self.fc.flow_load_home_screen()
        self.home.select_plugin_from_home("event_service")
        self.event_service_plugin.select_create_publisher_btn()
        assert "publisher was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_delete_publisher_btn()
        assert "publisher destroyed!" in self.event_service_plugin.get_toast_text().lower()  

    def test_15_subscribe_event_using_valid_eventName_publisherID_and_callback_option(self, create_and_select_new_subscriber):
        """
        C32374234: Subscribe to an event using valid eventName and publisherID
        """
        self.event_service_plugin.enter_subscribe_event_name_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.reference.app.newpublisher")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        assert 'com.hp.jarvis.event.newevent' == self.event_service_plugin.get_subscription_generated_event_name_text()
        assert 'com.hp.jarvis.reference.app.newpublisher' == self.event_service_plugin.get_subscription_generated_publisher_id_text()