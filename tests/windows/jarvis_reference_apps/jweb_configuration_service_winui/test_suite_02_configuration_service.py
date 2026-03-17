import pytest
class Test_Suite_02_Configuration_Service(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, jweb_configuration_service_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_configuration_service_test_setup
        cls.configuration_plugin = cls.fc.fd["configuration_service_plugin"]

    @pytest.mark.configurationservice
    def test_01_verify_the_retrieval_of_configuration_after_provider_change_C65244920(self):
        """
        C65244920: Verify the retrieval of configuration after provider change
        """
        self.configuration_plugin.select_provider_option("unsupported_provider")
        self.configuration_plugin.select_initialize_configuration_provider_btn()
        initialization_message = self.configuration_plugin.get_initialization_message_text()
        assert initialization_message == "Selected provider is not supported.", f"Initialization message mismatch. Expected: 'Selected provider is not supported.', Got: '{initialization_message}'"
        self.configuration_plugin.select_ok_button()

    @pytest.mark.configurationservice
    def test_02_verify_the_retrieval_of_all_configuration_keys_C65377312(self):
        """
        C65377312: Verify the retrieval of configuration after provider change
        """
        self.configuration_plugin.click_get_all_configuration_btn()
        all_config_text = self.configuration_plugin.get_all_configuration_list_text()
        assert all_config_text is not None and all_config_text != "", "Failed to retrieve all configuration keys; the list is empty."

    @pytest.mark.configurationservice
    def test_03_verify_the_retrieval_of_configuration_keys_after_bootstrap_file_updated_C65245007(self, initialize_without_bootstrap_file):
        """
        C65245007: Verify the retrieval of configuration after bootstrap file updated successfully
        """
        self.configuration_plugin.enter_configuration_key("say-hello")
        self.configuration_plugin.select_get_configuration_btn()
        configuration_value = self.configuration_plugin.get_configuration_message_text()
        expected_value = "Result : {say-hello: True}"
        assert configuration_value == expected_value, f"Expected configuration value: '{expected_value}', but got: '{configuration_value}'"
        self.fc.upload_bootstrap_file("bootstrap.json")
        self.configuration_plugin.select_initialize_configuration_provider_btn()
        initialization_message = self.configuration_plugin.get_initialization_message_text()
        assert initialization_message == "Configuration Service initialized successfully.", f"Initialization message mismatch. Expected: 'Configuration Service initialized successfully.', Got: '{initialization_message}'"
        self.configuration_plugin.select_ok_button()
        self.configuration_plugin.click_get_all_configuration_btn()
        all_config_text = self.configuration_plugin.get_all_configuration_list_text()
        assert all_config_text is not None and all_config_text != "", "Failed to retrieve all configuration keys; the list is empty."

    @pytest.mark.configurationservice
    def test_04_verify_provider_dropdown_displays_all_available_providers_C65243200(self):
        """
        C65243200: Verify Provider Dropdown Displays All Available Providers
        """
        self.configuration_plugin.select_provider_combobox()
        providers_list = self.configuration_plugin.get_all_providers()
        expected_providers = ["launchdarkly", "unsupported_provider"]
        assert expected_providers == self.configuration_plugin.get_all_providers(), "value is not present in the list"

    @pytest.mark.configurationservice
    def test_05_verify_initialization_with_selected_provider_as_launchdarkly_C65243201(self):
        """
        C65243201: Verify Initialization with Selected Provider as LaunchDarkly
        """
        self.configuration_plugin.select_provider_option(self.provider_name)
        self.configuration_plugin.enter_sdk_key(self.sdk_key)
        self.configuration_plugin.enter_context_key(self.context_key)
        self.configuration_plugin.select_initialize_configuration_provider_btn()
        initialization_message = self.configuration_plugin.get_initialization_message_text()
        assert initialization_message == "Configuration Service initialized successfully.", (
            "Initialization message mismatch. Expected: 'Configuration Service initialized successfully.', "
            f"Got: '{initialization_message}'"
        )
        self.configuration_plugin.select_ok_button()