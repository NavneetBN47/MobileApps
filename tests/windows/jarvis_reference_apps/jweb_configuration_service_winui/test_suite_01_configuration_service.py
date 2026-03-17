import pytest
@pytest.mark.usefixtures("initialize_without_bootstrap_file")
class Test_Suite_01_Configuration_Service(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, jweb_configuration_service_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_configuration_service_test_setup
        cls.configuration_plugin = cls.fc.fd["configuration_service_plugin"]

    @pytest.mark.configurationservice
    def test_01_verify_error_message_when_retriving_configuration_using_empty_key_C65377390(self):
        """
        C65377390: Verify error message when retrieving configuration using empty key
        """
        self.configuration_plugin.select_get_configuration_btn()
        configuration_error_text = self.configuration_plugin.get_configuration_message_text()
        expected_error_text = "Error: Key cannot be null and must have at least one visible character. (Parameter 'key')"
        assert configuration_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{configuration_error_text}'"

    @pytest.mark.configurationservice
    def test_02_verify_retrieval_of_configuration_of_specific_key_C65377365(self):
        """
        C65377365: Verify retrieval of configuration using specific key
        """
        self.configuration_plugin.enter_configuration_key("say-hello")
        self.configuration_plugin.select_get_configuration_btn()
        configuration_value = self.configuration_plugin.get_configuration_message_text()
        expected_value = "Result : {say-hello: True}"
        assert configuration_value == expected_value, f"Expected configuration value: '{expected_value}', but got: '{configuration_value}'"

    @pytest.mark.configurationservice
    def test_03_verify_subscription_of_specific_configuration_key_C65246512(self):
        """
        C65246512: Verify subscription of specific configuration key
        """
        self.configuration_plugin.enter_subscribe_configuration_key("BooleanFlag")
        self.configuration_plugin.select_subscribe_configuration_btn()
        subscription_message = self.configuration_plugin.get_subscription_pop_up_message_text()
        expected_subscription_message = "Subscribed successfully"
        assert expected_subscription_message in subscription_message, f"Expected subscription message to contain: '{expected_subscription_message}', but got: '{subscription_message}'"

    @pytest.mark.configurationservice
    def test_04_verify_unsubscription_of_specific_configuration_key_C65246628(self):
        """
        C65246628: Verify unsubscription of specific configuration key
        """
        self.configuration_plugin.enter_unsubscribe_configuration_key("BooleanFlag")
        self.configuration_plugin.select_unsubscribe_configuration_btn()
        unsubscription_message = self.configuration_plugin.get_unsubscription_pop_up_message_text()
        expected_unsubscription_message = "Unsubscribed successfully."
        assert expected_unsubscription_message in unsubscription_message, f"Expected unsubscription message to contain: '{expected_unsubscription_message}', but got: '{unsubscription_message}'"

    @pytest.mark.configurationservice
    def test_05_verify_error_message_when_retriving_configuration_using_empty_key_with_bootstrap_C65243667(self):
        """
        C65243667: Verify error message when retrieving configuration using empty key with bootstrap file
        """
        self.fc.initialize_configuration_service_with_bootstrap_file(self.provider_name, self.sdk_key, self.context_key)
        self.configuration_plugin.select_get_configuration_btn()
        configuration_error_text = self.configuration_plugin.get_configuration_message_text()
        expected_error_text = "Error: Key cannot be null and must have at least one visible character. (Parameter 'key')"
        assert configuration_error_text == expected_error_text, f"Expected error message: '{expected_error_text}', but got: '{configuration_error_text}'"