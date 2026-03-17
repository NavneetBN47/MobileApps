import pytest
class Test_Suite_06_Configuration_Service(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, jweb_configuration_service_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_configuration_service_test_setup
        cls.configuration_plugin = cls.fc.fd["configuration_service_plugin"]

    @pytest.mark.configurationservice
    def test_01_verify_retrival_of_configuration_for_valid_key_C65243302(self, initialize_without_bootstrap_file):
        """
        C65243302: Verify retrieval of configuration for a valid key
        """
        self.configuration_plugin.enter_configuration_key("say-hello")
        self.configuration_plugin.select_get_configuration_btn()
        configuration_value = self.configuration_plugin.get_configuration_message_text()
        expected_value = "Result : {say-hello: True}"
        assert configuration_value == expected_value, f"Expected configuration value: '{expected_value}', but got: '{configuration_value}'"

    @pytest.mark.configurationservice
    def test_02_verify_error_message_for_invalid_configuration_key_C65243304(self, initialize_without_bootstrap_file):
        """
        C65243304: Verify error message for an invalid configuration key
        """
        self.configuration_plugin.enter_configuration_key("test@123")
        self.configuration_plugin.select_get_configuration_btn()
        configuration_value = self.configuration_plugin.get_configuration_message_text()
        expected_value = "Result : {test@123: null}"
        assert configuration_value == expected_value, f"Expected configuration value: '{expected_value}', but got: '{configuration_value}'"

    @pytest.mark.configurationservice
    def test_03_verify_error_when_retrieving_after_clearing_initialization_C65454021(self):
        """
        C65454021: Verify error handling when retrieving all configurations after clearing initialization details
        """
        self.configuration_plugin.click_get_all_configuration_btn()
        all_config_text = self.configuration_plugin.get_all_configuration_list_text()
        assert all_config_text is not None and all_config_text != "", "Failed to retrieve all configuration keys; the list is empty."
        self.configuration_plugin.select_weblet_tab()
        self.configuration_plugin.select_configuration_service_tab()
        self.configuration_plugin.click_get_all_configuration_btn()
        all_config_text = self.configuration_plugin.get_all_configuration_list_text()
        assert all_config_text is not None and all_config_text != "", "Failed to retrieve all configuration keys; the list is empty."

    @pytest.mark.configurationservice
    def test_04_verify_error_message_when_unsubscribing_without_active_subscription_C65377518(self, initialize_without_bootstrap_file):
        """
        C65377518: Verify error message when unsubscribing without an active subscription
        """
        self.configuration_plugin.select_unsubscribe_configuration_btn()
        result = self.configuration_plugin.get_unsubscription_pop_up_message_text()
        assert "Unsubscription failed: Subscription ID cannot be null" in result, \
            f"Expected error message for unsubscribing without active subscription, but got: {result}"
        
    @pytest.mark.configurationservice
    def test_05_verify_unsubscription_of_specific_configuration_key_C65246628(self, initialize_without_bootstrap_file):
        """
        C65246628: Verify unsubscription of specific configuration key
        """
        self.configuration_plugin.enter_subscribe_configuration_key("BooleanFlag")
        self.configuration_plugin.select_subscribe_configuration_btn()
        subscription_message = self.configuration_plugin.get_subscription_pop_up_message_text()
        self.configuration_plugin.select_ok_button()
        subscription_id = ""
        if "SubscriptionId" in subscription_message:
            subscription_id = subscription_message.split("SubscriptionId", 1)[-1].replace(":", "").strip()

        assert subscription_id, f"Expected a SubscriptionId in subscription message, but got: '{subscription_message}'"

        self.configuration_plugin.enter_unsubscribe_configuration_key(subscription_id)
        self.configuration_plugin.select_unsubscribe_configuration_btn()
        unsubscription_message = self.configuration_plugin.get_unsubscription_pop_up_message_text()
        expected_unsubscription_message = "Unsubscribed successfully."
        assert expected_unsubscription_message in unsubscription_message, f"Expected unsubscription message to contain: '{expected_unsubscription_message}', but got: '{unsubscription_message}'"
        self.configuration_plugin.select_ok_button()