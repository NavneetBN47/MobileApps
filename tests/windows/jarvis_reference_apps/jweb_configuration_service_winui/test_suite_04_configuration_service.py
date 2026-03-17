import pytest

class Test_Suite_04_Configuration_Service(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, jweb_configuration_service_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_configuration_service_test_setup
        cls.configuration_plugin = cls.fc.fd["configuration_service_plugin"]

    @pytest.mark.configurationservice
    def test_01_verify_initialization_with_invalid_bootstrap_file_C65479389(self):
        """
        C65479389: Verify initialization with provider and invalid bootstrap file
        """
        self.configuration_plugin.select_provider_option(self.provider_name)
        self.configuration_plugin.enter_sdk_key(self.sdk_key)
        self.configuration_plugin.enter_context_key(self.context_key)
        self.fc.upload_bootstrap_file("invalid_bootstrap.json")
        self.configuration_plugin.select_initialize_configuration_provider_btn()
        self.configuration_plugin.dismiss_initialization_popup_if_present()

    @pytest.mark.configurationservice
    def test_02_verify_error_message_when_no_provider_selected_C65479793(self):
        """
        C65479793: Verify error message when initializing configuration service without selecting a provider
        """
        self.configuration_plugin.select_initialize_configuration_provider_btn()
        self.configuration_plugin.dismiss_initialization_popup_if_present()

    @pytest.mark.configurationservice
    def test_03_verify_successful_de_initialization_of_configuration_service_C66219353(self):
        """
        C66219353: Verify successful de-initialization of configuration service
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
        self.configuration_plugin.select_de_initialize_configuration_provider_btn()
        de_initialization_message = self.configuration_plugin.get_initialization_message_text()
        assert de_initialization_message == "Configuration Service deinitialized successfully.", f"De-Initialization message mismatch. Expected: 'Configuration Service deinitialized successfully.', Got: '{de_initialization_message}'"
        self.configuration_plugin.select_ok_button()

    @pytest.mark.configurationservice
    def test_04_verify_de_initialization_service_is_not_initialized_C66219418(self):
        """
        C66219418: Verify de-initialization when service is not initialized
        """
        self.configuration_plugin.select_de_initialize_configuration_provider_btn()
        de_initialization_message = self.configuration_plugin.get_initialization_message_text()
        assert de_initialization_message == "Configuration Service deinitialized successfully.", f"De-Initialization message mismatch. Expected: 'Configuration Service deinitialized successfully.', Got: '{de_initialization_message}'"
        self.configuration_plugin.select_ok_button()

    @pytest.mark.configurationservice
    def test_05_verify_re_initialization_after_de_initialization_C66221400(self):
        """
        C66221400: Verify re-initialization after de-initialization
        """
        self.configuration_plugin.select_de_initialize_configuration_provider_btn()
        de_initialization_message = self.configuration_plugin.get_initialization_message_text()
        assert de_initialization_message == "Configuration Service deinitialized successfully.", f"De-Initialization message mismatch. Expected: 'Configuration Service deinitialized successfully.', Got: '{de_initialization_message}'"
        self.configuration_plugin.select_ok_button()
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