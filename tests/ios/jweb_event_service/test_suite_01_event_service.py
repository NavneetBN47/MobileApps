import pytest
pytest.app_info = "JWEB_EVENT_SERVICE"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_event_service_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_event_service_setup

        cls.home = cls.fc.fd["home"]
        cls.web_home = cls.fc.fd["web_home"]
        cls.event_service_plugin = cls.fc.fd["event_service_plugin"]
        cls.native_event_service_plugin = cls.fc.fd["native_event_service_plugin"]

    @pytest.fixture(scope="function")
    def create_and_select_new_subscriber(self):
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.event_service_plugin.enter_create_subscriber_id_text("new subscriber")
        self.event_service_plugin.select_create_subscriber_btn()
        self.event_service_plugin.select_first_subscriber()

    def test_01_subscribe_to_valid_event(self, create_and_select_new_subscriber):
        """
        C32374234: Subscribe to an event using valid eventName and publisherID, expecting 'Subscription was created' toast notification
        C32374235: Subscribe to the same event twice, expecting 'Subscription was created' toast notification
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
        C29349618: Subscribe to an event using empty eventName, expecting 'not informed' error toast notification
        C29349619: Subscribe to an event using an empty publisher, expecting 'Subscription was created' toast notification
        C32374238: Subscribe to an event using empty eventName and empty publisherId, expecting 'provided eventName and publisherId is null or empty' toast notification
        """
        self.event_service_plugin.enter_subscribe_event_name_text(subscription_options[0])
        self.event_service_plugin.enter_subscribe_publisher_id_text(subscription_options[1])
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        expected_publisher_id = "not informed" if subscription_options[1] == "" else subscription_options[1]
        assert expected_publisher_id == self.event_service_plugin.get_subscription_generated_publisher_id_text().lower()

    @pytest.mark.parametrize("unsubscription_options", [("com.hp.jarvis.event.newevent", "com.hp.jarvis.reference.app.newpublisher"), ("com.hp.jarvis.event.newevent", ""),\
                                                        ("", "com.hp.jarvis.reference.app.newpublisher"), ("", "")])
    def test_03_unsubscribe_to_valid_event(self, create_and_select_new_subscriber, unsubscription_options):
        """
        C29223602: Unsubscribe from an event with specific eventName and specific publisherId
        C29223603: Unsubscribe from an event only using eventName
        C29223604: Unsubscribe from an event only using publisherId
        C29223605: Unsubscribe from all events

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
        C29223606: Publish an event with valid eventName and eventName, expecting received event in app console
        C29360715: Publish an event with a blank eventName, expecting an 'invalidIdentifier' error toast message
        C29349954: Publish an event not using formatted JSON, expecting a 'EventData should be in JSON' error toast message
        C32374242: Publish an event using blank event data, expecting received event in app console
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.event_service_plugin.select_create_publisher_btn()
        self.event_service_plugin.select_first_publisher()
        self.event_service_plugin.enter_publisher_event_name_text(publish_options[0])
        self.event_service_plugin.enter_publisher_event_data_text(publish_options[1])
        self.event_service_plugin.select_publish_btn()
        if publish_options[0] == "":
            assert "invalididentifier" in self.event_service_plugin.get_toast_text().lower()
        elif publish_options[1] == '':
            assert "event published" in self.event_service_plugin.get_toast_text().lower()
        elif publish_options[1] != '{"name1": "Tony", "name2": "Bruce"}':
            "eventdata should be in json format" in self.event_service_plugin.get_toast_text().lower()
        else:
            assert "event published" in self.event_service_plugin.get_toast_text().lower()

    @pytest.mark.parametrize("subscribers_list", [("subscriber1"), ("subscriber2"), ("subscriber3")])
    def test_05_create_two_or_more_subscribers(self, subscribers_list):
        """
        C29223592: Create a subscriber
        C44278950: Create two or more subscribers
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers_list[0])
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()

    def test_06_create_publisher_using_valid_and_invalid_publisher_id(self):
        """
        C32374230: Create a publisher using a valid publisherId, expecting 'Publisher was created!' toast notification
        C32374232: Create a publisher using a blank publisherId, expecting 'invalididentifier' toast notification
        C32374231: Create a publisher using a existing publisherID, expecting 'Publisher was created!' toast notification
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.event_service_plugin.enter_create_publisher_id_text("com.hp.jarvis.new.app.publisher")
        self.event_service_plugin.select_create_publisher_btn()
        assert "publisher was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.enter_create_publisher_id_text("com.hp.jarvis.new.app.publisher")
        self.event_service_plugin.select_create_publisher_btn()
        assert "already exists!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.enter_create_publisher_id_text(" ")
        self.event_service_plugin.select_create_publisher_btn()
        assert "invalididentifier" in self.event_service_plugin.get_toast_text().lower()

    def test_07_pausing_event_for_active_subscriber_with_subscriptions(self):
        """
        C30661969: Pause an event for an active subscriber with subscriptions and verify the event tab is not shown with any events
        C30661970: Resume an event for an active subscriber with subscriptions and verify the event tab is shown with events
        """
        self.fc.flow_load_home_screen()
        self.fc.native_add_subscription_for_existing_subscriber("com.hp.jarvis.reference.app.newpublisher")
        self.fc.native_select_persist_events_toggle()
        self.fc.native_select_pause_events()
        self.fc.native_publish_an_event("com.hp.jarvis.reference.app.newpublisher")
        self.fc.native_verify_event_received()
        assert self.native_event_service_plugin.native_verify_event_data_table_entry() is not True
        self.fc.native_select_resume_events()
        self.fc.native_select_resume_events
        self.fc.native_verify_event_received()
        self.native_event_service_plugin.native_verify_first_publisher_id("com.hp.jarvis.reference.app.newpublisher")

    def test_08_pause_resume_an_events_for_an_active_subscriber(self):
        """
        C30661971: Pause an event for an active subscriber with subscriptions, Publish the event 3 times and verify the 3 entries in event logs
        """
        self.fc.flow_load_home_screen()
        self.home.select_subscribers_tab()
        self.fc.native_create_new_subscriber_with_is_persist_yes()
        self.fc.native_create_subscription_for_newly_created_subscriber("com.hp.jarvis.reference.app.publisher")
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_newly_created_subscriber()
        self.native_event_service_plugin.native_select_pause_events_btn()
        self.home.select_publishers_tab()
        self.native_event_service_plugin.native_select_publisher("com.hp.jarvis.reference.app.publisher")
        self.native_event_service_plugin.native_select_publish_btn()
        self.native_event_service_plugin.native_select_publisher("com.hp.jarvis.reference.app.publisher")
        self.native_event_service_plugin.native_select_publish_btn()
        self.native_event_service_plugin.native_select_publisher("com.hp.jarvis.reference.app.publisher")
        self.native_event_service_plugin.native_select_publish_btn()
        self.fc.native_verify_event_received()
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_resume_events_btn()
        self.fc.native_verify_event_received()
        self.native_event_service_plugin.native_verify_first_publisher_id("com.hp.jarvis.reference.app.publisher")
        self.native_event_service_plugin.native_verify_second_publisher_id("com.hp.jarvis.reference.app.publisher")
        self.native_event_service_plugin.native_verify_third_publisher_id("com.hp.jarvis.reference.app.publisher")

    def test_09_create_subscriber_with_enabling_persist_event_for_pause_events(self):
        """
        C31334882: Create a subscriber with enabling persist events and pause events
        """
        self.fc.flow_load_home_screen()
        self.home.select_subscribers_tab()
        self.fc.native_create_new_subscriber_with_is_persist_yes()
        self.fc.native_create_publisher("com.hp.jarvis.reference.app.newpublisher")
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_newly_created_subscriber()
        self.native_event_service_plugin.native_select_pause_events_btn()
        self.native_event_service_plugin.native_select_subscriptions_btn()
        self.home.select_publishers_tab()
        self.native_event_service_plugin.native_select_publisher("com.hp.jarvis.reference.app.newpublisher")
        self.native_event_service_plugin.native_select_publish_btn()
        self.fc.native_verify_event_received()
        assert self.native_event_service_plugin.native_verify_event_data_table_entry() is not True

    def test_10_create_subscriber_with_disabling_persist_event_for_pause_events(self):
        """
        C31336865: Create a subscriber with disabling persist events and pause events
        """
        self.fc.flow_load_home_screen()
        self.fc.native_create_new_subscriber_with_is_persist_no()
        self.fc.native_create_publisher("com.hp.jarvis.reference.app.newpublisher")
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_newly_created_subscriber()
        self.native_event_service_plugin.native_select_pause_events_btn()
        self.fc.native_create_new_subscriptions("com.hp.jarvis.reference.app.newpublisher")
        self.home.select_publishers_tab()
        self.native_event_service_plugin.native_select_publisher("com.hp.jarvis.reference.app.newpublisher")
        self.native_event_service_plugin.native_select_publish_btn()
        self.fc.native_verify_event_received()
        self.native_event_service_plugin.native_verify_first_publisher_id("com.hp.jarvis.reference.app.newpublisher")

    def test_11_create_subscriber_with_enabling_persist_event_for_resume_events(self):
        """
        C31336864: Create a subscriber with enabling persist events and resume events
        """
        self.fc.flow_load_home_screen()
        self.home.select_subscribers_tab()
        self.fc.native_create_new_subscriber_with_is_persist_yes()
        self.fc.native_create_publisher("com.hp.jarvis.reference.app.newpublisher")
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_newly_created_subscriber()
        self.native_event_service_plugin.native_select_resume_events_btn()
        self.native_event_service_plugin.native_select_subscriptions_btn()
        self.native_event_service_plugin.native_select_add_subscription_btn()
        self.native_event_service_plugin.native_enter_new_publisher_id_text("com.hp.jarvis.reference.app.newpublisher")
        self.native_event_service_plugin.native_select_subscription_btn()
        self.home.select_publishers_tab()
        self.native_event_service_plugin.native_select_publisher("com.hp.jarvis.reference.app.newpublisher")
        self.native_event_service_plugin.native_select_publish_btn()
        self.fc.native_verify_event_received()
        self.native_event_service_plugin.native_verify_first_publisher_id("com.hp.jarvis.reference.app.newpublisher")

    def test_12_verify_paused_persistent_subscriber_to_non_persistent_it_immediately_resume_paused_subscription(self):
        """
        C38252322: Verify paused persistent subscriber to non-persistent it immediately resume paused subscription
        """
        self.fc.native_create_new_subscriber_with_is_persist_yes()
        self.native_event_service_plugin.native_select_newly_created_subscriber()
        self.native_event_service_plugin.native_select_subscriptions_btn()
        self.native_event_service_plugin.native_select_add_subscription_btn()
        self.native_event_service_plugin.native_select_subscription_btn()
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_newly_created_subscriber()
        self.native_event_service_plugin.native_select_pause_events_btn()
        self.home.select_publishers_tab()
        self.native_event_service_plugin.native_select_publisher("com.hp.jarvis.reference.app.publisher")
        self.native_event_service_plugin.native_select_publish_btn()
        self.fc.native_verify_event_received()
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_resume_events_btn()
        self.fc.native_verify_event_received()
        self.native_event_service_plugin.native_verify_first_publisher_id("com.hp.jarvis.reference.app.newpublisher")

    def test_13_verify_subscription_added_for_a_paused_persisted_subscriber_will_remain_inactive(self):
        """
        C38414682: Verify subscription added for a paused persisted subscriber will remain inactive
        """
        self.fc.native_create_new_subscriber_with_is_persist_yes()
        self.native_event_service_plugin.native_select_newly_created_subscriber()
        self.native_event_service_plugin.native_select_subscriptions_btn()
        self.native_event_service_plugin.native_select_add_subscription_btn()
        self.native_event_service_plugin.native_select_subscription_btn()
        self.native_event_service_plugin.native_verify_subscription_status("Active")
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_newly_created_subscriber()
        self.native_event_service_plugin.native_select_pause_events_btn()
        self.native_event_service_plugin.native_select_subscriptions_btn()
        self.native_event_service_plugin.native_verify_subscription_status("Inactive")
        self.home.select_publishers_tab()
        self.native_event_service_plugin.native_select_publisher("com.hp.jarvis.reference.app.publisher")
        self.native_event_service_plugin.native_select_publish_btn()
        self.fc.native_verify_event_received()
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_back_btn_to_subscriber()
        self.native_event_service_plugin.native_select_resume_events_btn()
        self.native_event_service_plugin.native_select_subscriptions_btn()
        self.fc.native_verify_event_received()
        self.native_event_service_plugin.native_verify_first_publisher_id("com.hp.jarvis.reference.app.newpublisher")

    def test_14_subscriber_an_event_using_valid_event_name_and_publisher_id_and_delegate_option(self):
        """
        C29229139: Subscribe to an event using valid eventName, publisherID and delegate option
        """
        self.fc.flow_load_home_screen()
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_existing_subscriber_from_list()
        self.native_event_service_plugin.native_select_subscriptions_btn()
        self.native_event_service_plugin.native_select_add_subscription_btn()
        self.native_event_service_plugin.native_enter_new_publisher_id_text("com.hp.jarvis.reference.app.newpublisher")
        self.native_event_service_plugin.native_enter_new_event_name_text("com.hp.jarvis.event.newevent")
        self.native_event_service_plugin.native_select_subscription_callback_btn()
        self.native_event_service_plugin.native_select_subscription_btn()
        self.native_event_service_plugin.native_verify_subscription_entries("com.hp.jarvis.reference.app.newpublisher")
        self.native_event_service_plugin.native_verify_subscription_entries("com.hp.jarvis.event.newevent")

    def test_15_subscriber_an_event_using_blank_event_name_and_publisher_id(self):
        """
        C29417223: Subscribe to an event using blank eventName, publisherID
        """
        self.fc.flow_load_home_screen()
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_existing_subscriber_from_list()
        self.native_event_service_plugin.native_select_subscriptions_btn()
        self.native_event_service_plugin.native_select_add_subscription_btn()
        self.native_event_service_plugin.native_enter_new_publisher_id_text("")
        self.native_event_service_plugin.native_enter_new_event_name_text("")
        self.native_event_service_plugin.native_select_subscription_btn()
        assert "missingRequiredKeys" in self.native_event_service_plugin.native_subscription_error_pop_up_msg()
    
    def test_16_subscriber_an_event_using_blank_event_name_and_publisher_id(self):
        """
        C29349619: Subscribe to an event using valid eventName and blank publisherID
        """
        self.fc.flow_load_home_screen()
        self.home.select_subscribers_tab()
        self.native_event_service_plugin.native_select_existing_subscriber_from_list()
        self.native_event_service_plugin.native_select_subscriptions_btn()
        self.native_event_service_plugin.native_select_add_subscription_btn()
        self.native_event_service_plugin.native_enter_new_publisher_id_text("")
        self.native_event_service_plugin.native_enter_new_event_name_text("com.hp.jarvis.event.newevent")
        self.native_event_service_plugin.native_select_subscription_btn()
        self.native_event_service_plugin.native_verify_subscription_entries("com.hp.jarvis.event.newevent")
        self.native_event_service_plugin.native_verify_subscription_entries("Not informed")

    def test_17_delete_a_subscriber(self):
        """
        C29223593: Delete a subscriber, expecting 'Subscriber Destroyed!' toast notification
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.event_service_plugin.enter_create_subscriber_id_text("new subscriber")
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_delete_subscriber_btn()
        assert "subscriber destroyed!" in self.event_service_plugin.get_toast_text().lower()
    
    @pytest.mark.parametrize("subscribers", [("subscriber0", "subscriber1")])
    def test_18_delete_first_subscriber_from_subscriber_list(self, subscribers):
        """
        C29408724: Delete first subscriber from subscriber list, expecting 'Subscriber Destroyed' toast notification
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers[0])
        self.event_service_plugin.select_create_subscriber_btn()
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_delete_subscriber_btn()
        assert "subscriber destroyed!" in self.event_service_plugin.get_toast_text().lower()

    def test_19_delete_a_publisher(self):
        """
        C32374233: Delete a publisher, expecting 'Publisher Destroyed!' toast notification
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.event_service_plugin.select_create_publisher_btn()
        assert "publisher was created!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_delete_publisher_btn()
        assert "publisher destroyed!" in self.event_service_plugin.get_toast_text().lower()

    def test_20_subscribe_event_using_valid_eventName_publisherID_and_callback_option(self, create_and_select_new_subscriber):
        """
        C29223599: Subscribe to an event using valid eventName, publisherID and callback option
        """
        self.event_service_plugin.enter_subscribe_event_name_text("com.hp.jarvis.event.newevent")
        self.event_service_plugin.enter_subscribe_publisher_id_text("com.hp.jarvis.reference.app.newpublisher")
        self.event_service_plugin.select_subscribe_btn()
        assert "subscription was created" in self.event_service_plugin.get_toast_text().lower()
        assert 'com.hp.jarvis.event.newevent' == self.event_service_plugin.get_subscription_generated_event_name_text()
        assert 'com.hp.jarvis.reference.app.newpublisher' == self.event_service_plugin.get_subscription_generated_publisher_id_text()
    
    @pytest.mark.parametrize("subscribers", [("test0", "test1", "test2")])
    def test_21_create_three_subscriber_with_same_valid_fields_with_persistant_value_false(self, subscribers):
        """
        C44278966: Create two or three subscriber with same valid fields with persistant value as false
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers[0])
        self.event_service_plugin.select_persistent_drop_down_menu()
        self.event_service_plugin.select_persistent_option_from_menu("false")
        self.event_service_plugin.select_create_subscriber_btn() 
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()

    @pytest.mark.parametrize("subscribers", [("test0", "test1", "test2")])
    def test_22_create_three_subscriber_with_same_valid_fields_with_persistant_value_true(self, subscribers):
        """
        C44279013: Create two or three subscriber with same valid fields with persistant value as true
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.event_service_plugin.enter_create_subscriber_id_text(subscribers[0])
        self.event_service_plugin.select_persistent_drop_down_menu()
        self.event_service_plugin.select_persistent_option_from_menu("true")
        self.event_service_plugin.select_create_subscriber_btn() 
        assert "subscriber was created!" in self.event_service_plugin.get_toast_text().lower()

    def test_23_verify_pause_resume_options_ispersistent_if_false(self):
        """
        C32374244: Verify pause and resume options if isPersistent is false
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
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
        self.event_service_plugin.select_first_subscriber() 
        self.event_service_plugin.select_pause_btn()
        assert "subscribernotpersistent" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_resume_btn()
        assert "subscribernotpersistent" in self.event_service_plugin.get_toast_text().lower()

    def test_24_verify_pause_resume_options_ispersistent_if_true(self):
        """
        C32374245: Verify pause and resume options if isPersistent is true
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
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
        self.event_service_plugin.select_first_subscriber()
        self.event_service_plugin.select_pause_btn()
        assert "events paused!" in self.event_service_plugin.get_toast_text().lower()
        self.event_service_plugin.select_resume_btn()
        assert "events resumed!" in self.event_service_plugin.get_toast_text().lower()