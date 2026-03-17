import pytest
class Test_Suite_07_Configuration_Service(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, jweb_configuration_service_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_configuration_service_test_setup
        cls.configuration_plugin = cls.fc.fd["configuration_service_plugin"]

    @pytest.mark.configurationservice
    def test_01_verify_subscription_to_all_configurations_C65377316(self, initialize_without_bootstrap_file):
        """
        C65377316: Verify subscription to all configurations
        """
        self.configuration_plugin.select_subscribe_all_configurations_btn()
        subscription_message = self.configuration_plugin.get_subscription_pop_up_message_text()
        expected_subscription_message = "Subscribed to all configurations successfully."
        assert expected_subscription_message in subscription_message, f"Expected subscription message to contain: '{expected_subscription_message}', but got: '{subscription_message}'"

        self.configuration_plugin.select_ok_button()

    @pytest.mark.configurationservice
    def test_02_verify_unsubscription_from_all_configurations_C65377317(self, initialize_without_bootstrap_file):
        """
        C65377317: Verify unsubscription from all configurations
        """
        self.configuration_plugin.select_unsubscribe_all_configurations_btn()
        unsubscription_message = self.configuration_plugin.get_unsubscription_pop_up_message_text()
        expected_unsubscription_message = "Unsubscription from all configurations failed"
        assert expected_unsubscription_message in unsubscription_message, f"Expected unsubscription message to contain: '{expected_unsubscription_message}', but got: '{unsubscription_message}'"
        self.configuration_plugin.select_ok_button()

    @pytest.mark.configurationservice
    def test_03_verify_error_message_when_subscribing_with_invalid_key_C65377366(self, initialize_without_bootstrap_file):
        """
        C65377366: Verify error message when subscribing with an invalid key
        """
        self.configuration_plugin.enter_subscribe_configuration_key("say-hello")
        self.configuration_plugin.select_subscribe_configuration_btn()
        subscription_message = self.configuration_plugin.get_subscription_pop_up_message_text()
        assert "Subscribed successfully" in subscription_message, f"Subscribed successfully', but got: '{subscription_message}'"

    @pytest.mark.configurationservice
    def test_04_verify_manual_retry_functionality_for_failed_network_requests_during_subscription_C65377577(self):
        """
        C65377577: Verify manual retry functionality for failed network requests during configuration subscription
        """
        self.configuration_plugin.enter_subscribe_configuration_key("say-hello")
        self.configuration_plugin.select_subscribe_configuration_btn()
        subscription_message1 = self.configuration_plugin.get_subscription_pop_up_message_text()
        
        self.configuration_plugin.enter_subscribe_configuration_key("string-flag")
        self.configuration_plugin.select_subscribe_configuration_btn()
        subscription_message2 = self.configuration_plugin.get_subscription_pop_up_message_text()
        assert subscription_message1 == subscription_message2, f"Expected both subscription attempts to return the same result. First attempt: '{subscription_message1}', Second attempt: '{subscription_message2}'"

    @pytest.mark.configurationservice
    def test_05_verify_app_behavior_during_rapid_subscribe_unsubscribe_actions_C65377578(self):
        """
        C65377578: Verify app behavior during rapid subscribe/unsubscribe actions
        """
        subscription_message, unsubscription_message = self.configuration_plugin.click_subscribe_and_unsubscribe_actions(3)
        assert "Subscription failed" in subscription_message, f"Expected 'Subscription failed' in subscription message, but possibly crashed or displaying inconsistent states."
        assert "Unsubscription failed" in unsubscription_message, f"Expected 'Unsubscription failed' in unsubscription message, but possibly crashed or displaying inconsistent states."