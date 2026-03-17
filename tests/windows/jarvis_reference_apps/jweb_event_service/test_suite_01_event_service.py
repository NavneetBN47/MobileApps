import pytest
from time import sleep

pytest.app_info = "JWEB_EVENT_SERVICE"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, jweb_event_service_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_event_service_test_setup
        cls.home = cls.fc.fd["home"]
        cls.event_service_plugin = cls.fc.fd["event_service_plugin"]

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_event_service_plugin(self):
        self.driver.restart_app()
        self.home.select_webview_engine("webview1_edge_engine")
        self.home.select_weblet_btn()
        self.home.select_jweb_reference_btn(raise_e=False)
        self.home.select_url_go_btn(raise_e=False)
        self.home.select_plugin_from_home("Event Service")

    def test_01_subscribe_to_valid_event(self):
        """
        C32374234: Subscribe to an event using valid eventName and publisherID, expecting 'Subscription was created' toast notification
        C32374235: Subscribe to the same event twice, expecting 'Subscription was created' toast notification
        """
        self.event_service_plugin.enter_create_subscriber_id_text("new subscriber")
        self.event_service_plugin.select_create_subscriber_btn()
        self.event_service_plugin.select_first_subscriber()
        self.event_service_plugin.enter_subscribe_event_name_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.reference.app.newpublisher")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        assert 'com.hp.jarvis.event.newevent' == self.event_service_plugin.get_subscription_generated_event_name_text()
        assert 'com.hp.jarvis.reference.app.newpublisher' == self.event_service_plugin.get_subscription_generated_publisher_id_text()
        self.event_service_plugin.select_subscribe_btn()
        assert "Subscription was created!" == self.event_service_plugin.get_toast_text()

    def test_02_subscribe_to_event_without_names(self):
        """
        C29349619: Subscribe to an event using an empty publisher, expecting 'Subscription was created' toast notification
        """
        self.event_service_plugin.enter_create_subscriber_id_text("new subscriber")
        self.event_service_plugin.select_create_subscriber_btn()
        self.event_service_plugin.select_first_subscriber()
        self.event_service_plugin.enter_subscribe_publisher_id_text("")
        self.event_service_plugin.enter_subscribe_event_name_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        assert "com.hp.jarvis.event.newevent" in self.event_service_plugin.get_subscription_generated_event_name_text().lower()
        assert "not informed" == self.event_service_plugin.get_subscription_generated_publisher_id_text().lower()

    @pytest.mark.parametrize("unsubscription_options", [("com.hp.jarvis.event.newevent", "com.hp.jarvis.reference.app.newpublisher"), ("com.hp.jarvis.event.newevent", ""),\
                                                        ("", "com.hp.jarvis.reference.app.newpublisher"), ("", "")])
    def test_03_unsubscribe_to_valid_event(self, unsubscription_options):
        """
        C29223602: Unsubscribe from an event with specific eventName and specific publisherId
        C29223603: Unsubscribe from an event only using eventName
        C29223604: Unsubscribe from an event only using publisherId
        C29223605: Unsubscribe from all events

        For all tests, expecting "unsubscribed" toast notification
        """
        self.event_service_plugin.enter_create_subscriber_id_text("new subscriber")
        self.event_service_plugin.select_create_subscriber_btn()
        self.event_service_plugin.select_first_subscriber()
        self.event_service_plugin.enter_subscribe_event_name_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.reference.app.newpublisher")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created!" == self.event_service_plugin.get_toast_text().lower()
        assert 'com.hp.jarvis.event.newevent' == self.event_service_plugin.get_subscription_generated_event_name_text()
        assert 'com.hp.jarvis.reference.app.newpublisher' == self.event_service_plugin.get_subscription_generated_publisher_id_text()
        sleep(5)
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created!" == self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.enter_unsubscribe_event_name_text(unsubscription_options[0])
        self.event_service_plugin.enter_unsubscribe_publisher_id_text(unsubscription_options[1])
        sleep(5)
        self.event_service_plugin.select_unsubscribe_btn()
        assert "unsubscribed!" == self.event_service_plugin.get_toast_text().lower()
        assert False is self.event_service_plugin.get_subscription_generated_publisher_id_text(raise_e=False)
        assert False is self.event_service_plugin.get_subscription_generated_event_name_text(raise_e=False)
    
    @pytest.mark.parametrize("publish_options", [("com.hp.jarvis.event.newevent", '{"name1": "Tony", "name2": "Bruce"}'), ("com.hp.jarvis.event.newevent", '{Guys:"name1":"Tony","name2":"Bruce"}'),
                                ("com.hp.jarvis.event.newevent", '')])
    def test_04_publish_an_event(self, publish_options):
        """
        Do we expect that a subscriber is made before a publisher can publish an event that returns a toast notification?

        C29223606: Publish an event with valid eventName and eventName, expecting received event in app console
        C29349954: Publish an event not using formatted JSON, expecting a 'EventData should be in JSON' error toast message
        C32374242: Publish an event using blank event data, expecting received event in app console
        """
        self.event_service_plugin.select_create_publisher_btn()
        self.event_service_plugin.select_first_publisher()
        self.event_service_plugin.enter_publisher_event_name_text(publish_options[0])
        self.event_service_plugin.enter_publisher_event_data_text(publish_options[1])
        self.event_service_plugin.select_publish_btn()
        if publish_options[1] != '{"name1": "Tony", "name2": "Bruce"}':
            "eventdata should be in json format" in self.event_service_plugin.get_toast_text().lower()
        else:
            assert "event published" in self.event_service_plugin.get_toast_text().lower()

    @pytest.mark.parametrize("subscription_options", [("", "com.hp.jarvis.reference.app.newpublisher"), ("", "")])
    def test_05_subscribe_to_event_without_names(self, subscription_options):
        """
        C29349618: Subscribe to an event using an empty event, expecting 'Subscription was created' toast notification
        C32374238: Subscribe to an event using an empty event and publisher, expecting 'Subscription was created' toast notification
        """
        self.event_service_plugin.enter_create_subscriber_id_text("new subscriber")
        self.event_service_plugin.select_create_subscriber_btn()
        self.event_service_plugin.select_first_subscriber()
        self.event_service_plugin.enter_subscribe_event_name_text(subscription_options[0])
        self.event_service_plugin.enter_subscribe_publisher_id_text(subscription_options[1])
        self.event_service_plugin.select_subscribe_btn()
        sleep(3)
        assert "subscription was created!" == self.event_service_plugin.get_toast_text().lower()
        expected_publisher_id = "not informed" if subscription_options[1] == "" else subscription_options[1]
        assert expected_publisher_id == self.event_service_plugin.get_subscription_generated_publisher_id_text().lower()

    def test_06_publish_an_event_using_blank_event_name(self):
        """
        C29360715: Publish an event with a blank eventName, expecting an 'invalidIdentifier' error toast message
        """
        self.event_service_plugin.select_create_publisher_btn()
        self.event_service_plugin.select_first_publisher()
        self.event_service_plugin.enter_publisher_event_name_text(" ")
        self.event_service_plugin.enter_publisher_event_data_text('{"name1": "Tony", "name2": "Bruce"}')
        self.event_service_plugin.select_publish_btn()
        assert "invalididentifier" in self.event_service_plugin.get_toast_text().lower()

    @pytest.mark.parametrize("subscribers_list", [("subscriber1"), ("subscriber2"), ("subscriber3")])
    def test_07_create_two_or_more_subscribers(self, subscribers_list):
        """
        C29223592: Create a subscriber
        C44278950: Create two or more subscribers
        """
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers_list[0])
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()

    def test_08_create_publisher_using_valid_publisher_id(self):
        """
        C32374230: Create a publisher using a valid publisherId, expecting 'Publisher was created!' toast notification
        C32374232: Create a publisher using a blank publisherId, expecting 'invalididentifier' toast notification
        C32374231: Create a publisher using a existing publisherID, expecting 'Publisher was created!' toast notification 
        """
        self.event_service_plugin.enter_create_publisher_id_text("com.hp.jarvis.new.app.publisher")
        self.event_service_plugin.select_create_publisher_btn()
        assert "publisher was created!" in self.event_service_plugin.get_toast_text().lower()
        sleep(5)
        self.event_service_plugin.enter_create_publisher_id_text(" ")
        self.event_service_plugin.select_create_publisher_btn()
        assert "invalididentifier" in self.event_service_plugin.get_toast_text().lower()
        sleep(5)
        self.event_service_plugin.enter_create_publisher_id_text("com.hp.jarvis.new.app.publisher")
        self.event_service_plugin.select_create_publisher_btn()
        assert "received publisher is already on the list" in self.event_service_plugin.get_toast_text().lower()

    def test_09_delete_a_subscriber(self):
        """
        C29223593: Delete a subscriber, expecting 'Subscriber Destroyed!' toast notification
        """
        self.event_service_plugin.enter_create_subscriber_id_text("new subscriber")
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        sleep(5)
        self.event_service_plugin.select_first_delete_subscriber_btn()
        assert "subscriber destroyed!" in self.event_service_plugin.get_toast_text().lower()

    @pytest.mark.parametrize("subscribers", [("test0", "test1")])
    def test_10_delete_first_subscriber_from_subscriber_list(self, subscribers):
        """
        C29408724: Delete first subscriber from subscriber list, expecting 'Subscriber Destroyed' toast notification
        """
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers[0])
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        sleep(5)
        self.event_service_plugin.select_first_delete_subscriber_btn()
        assert "subscriber destroyed!" in self.event_service_plugin.get_toast_text().lower()

    def test_11_delete_a_publisher(self):
        """
        C32374233: Delete a publisher, expecting 'Publisher Destroyed!' toast notification
        """
        self.event_service_plugin.select_create_publisher_btn()
        assert "publisher was created!" in self.event_service_plugin.get_toast_text().lower()
        sleep(5)
        self.event_service_plugin.select_delete_first_publisher_btn()
        assert "publisher destroyed!" in self.event_service_plugin.get_toast_text().lower()

    def test_12_subscribe_event_using_valid_eventName_publisherID_and_callback_option(self):
        """
        C29223599: Subscribe to an event using valid eventName, publisherID and callback option
        """
        self.event_service_plugin.enter_create_subscriber_id_text("new subscriber")
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_first_subscriber()
        self.event_service_plugin.enter_subscribe_event_name_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.reference.app.newpublisher")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created!" in self.event_service_plugin.get_toast_text().lower()
        assert "com.hp.jarvis.event.newevent" in self.event_service_plugin.get_subscription_generated_event_name_text().lower()
        assert "com.hp.jarvis.reference.app.newpublisher" == self.event_service_plugin.get_subscription_generated_publisher_id_text().lower()
    
    @pytest.mark.parametrize("subscribers", [("test0", "test1", "test2")])
    def test_13_create_three_subscriber_with_same_valid_fields_with_persistant_value_false(self, subscribers):
        """
        C44278966: Create two or three subscriber with same valid fields with persistant value as false
        """
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers[0])
        self.event_service_plugin.select_persistent_drop_down_menu()
        self.event_service_plugin.select_persistent_option_false_from_menu()
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()

    def test_14_verify_pause_resume_options_ispersistent_is_false(self):
        """
        C32374244: Verify pause and resume options if isPersistent is false
        """
        self.event_service_plugin.select_create_publisher_btn()
        assert "publisher was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.enter_create_subscriber_id_text("test123")
        self.event_service_plugin.select_persistent_drop_down_menu()
        self.event_service_plugin.select_persistent_option_false_from_menu()
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_first_subscriber()
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created!" in self.event_service_plugin.get_toast_text().lower()
        sleep(3)
        self.event_service_plugin.select_pause_btn()
        assert "subscribernotpersistent" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_resume_btn()
        assert "subscribernotpersistent" in self.event_service_plugin.get_toast_text().lower()

    def test_15_verify_pause_resume_options_ispersistent_is_true(self):
        """
        C32374245: Verify pause and resume options if isPersistent is true
        """
        self.event_service_plugin.select_create_publisher_btn()
        assert "publisher was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.enter_create_subscriber_id_text("test123")
        self.event_service_plugin.select_persistent_drop_down_menu()
        self.event_service_plugin.select_persistent_option_true_from_menu()
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_first_subscriber()
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created!" in self.event_service_plugin.get_toast_text().lower()
        sleep(3)
        self.event_service_plugin.select_pause_btn()
        assert "events paused!" in self.event_service_plugin.get_toast_text().lower()
        sleep(5)
        self.event_service_plugin.select_resume_btn()
        assert "events resumed!" in self.event_service_plugin.get_toast_text().lower()

    @pytest.mark.parametrize("subscribers", [("test0", "test1", "test2")])
    def test_16_create_three_subscriber_with_same_valid_fields_with_persistant_value_true(self, subscribers):
        """
        C44279013: Create two or three subscriber with same valid fields with persistant value as true
        """
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers[0])
        self.event_service_plugin.select_persistent_drop_down_menu()
        self.event_service_plugin.select_persistent_option_true_from_menu()
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()