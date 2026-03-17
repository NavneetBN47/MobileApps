import pytest
class Test_Suite_03_Configuration_Service(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, jweb_configuration_service_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_configuration_service_test_setup
        cls.configuration_plugin = cls.fc.fd["configuration_service_plugin"]

    @pytest.mark.configurationservice
    def test_01_verify_launchdarkly_provider_initialization_with_invalid_sdk_key_C65243202(self):
        """
        C65243202: Verify LaunchDarkly Provider Initialization with Invalid SDK Key
        """
        self.configuration_plugin.select_provider_option("launchdarkly")
        self.configuration_plugin.enter_sdk_key(self.sdk_key)
        self.configuration_plugin.enter_context_key(self.context_key)
        self.configuration_plugin.select_initialize_configuration_provider_btn()
        initialization_message = self.configuration_plugin.get_initialization_message_text()
        assert initialization_message == "Configuration Service initialized successfully.", f"Initialization message mismatch. Expected: 'Configuration Service initialized successfully.', Got: '{initialization_message}'"
        self.configuration_plugin.select_ok_button()

    @pytest.mark.configurationservice
    def test_02_verify_provider_can_be_changed_after_initialization_C65243203(self, initialize_without_bootstrap_file):
        """
        C65243203: Verify that the provider can be changed after initialization
        """
        self.configuration_plugin.select_provider_option("unsupported_provider")
        self.configuration_plugin.select_initialize_configuration_provider_btn()
        initialization_message = self.configuration_plugin.get_initialization_message_text()
        assert initialization_message == "Selected provider is not supported.", f"Initialization message mismatch. Expected: 'Selected provider is not supported.', Got: '{initialization_message}'"
        self.configuration_plugin.select_ok_button()

    @pytest.mark.configurationservice
    def test_03_verify_provider_can_be_changed_after_initialization_C65243204(self):
        """
        C65243204: Verify configuration service initialization with 
                   provider selection, SDK key, context key, and bootstrap file
        """
        self.configuration_plugin.select_provider_option(self.provider_name)
        self.configuration_plugin.enter_sdk_key(self.sdk_key)
        self.configuration_plugin.enter_context_key(self.context_key)
        self.fc.upload_bootstrap_file("bootstrap.json")
        self.configuration_plugin.select_initialize_configuration_provider_btn()
        initialization_message = self.configuration_plugin.get_initialization_message_text()
        assert initialization_message == "Configuration Service initialized successfully.", (
            "Initialization message mismatch. Expected: 'Configuration Service initialized successfully.', "
            f"Got: '{initialization_message}'"
        )
        self.configuration_plugin.select_ok_button()

    @pytest.mark.configurationservice
    def test_04_verify_error_message_when_no_provider_selected_C65454502(self):
        """
        C65454502: Verify error message when no provider is selected during initialization
        """
        self.configuration_plugin.enter_sdk_key(self.sdk_key)
        self.configuration_plugin.enter_context_key(self.context_key)
        self.configuration_plugin.select_initialize_configuration_provider_btn()

    @pytest.mark.configurationservice
    def test_05_verify_initialization_with_invalid_context_key_C65479355(self):
        """
        C65479355: Verify initialization with provider and invalid context key
        """
        self.configuration_plugin.select_provider_option(self.provider_name)
        self.configuration_plugin.enter_sdk_key(self.sdk_key)
        self.configuration_plugin.enter_context_key("say-hello")
        self.configuration_plugin.select_initialize_configuration_provider_btn()
        initialization_message = self.configuration_plugin.get_initialization_message_text()
        assert initialization_message == "Configuration Service initialized successfully.", f"Initialization message mismatch. Expected: 'Configuration Service initialized successfully.', Got: '{initialization_message}'"
        self.configuration_plugin.select_ok_button()