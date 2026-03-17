from MobileApps.libs.flows.windows.jweb_configuration_service_winui.configuration_service_plugin import ConfigurationServicePlugin
from MobileApps.libs.flows.windows.jweb_data_collection.files import Files

class FlowContainer(object):

    @property
    def flow(self):
        return self.fd

    def __init__(self, driver):
        self.driver = driver
        self.fd ={"configuration_service_plugin": ConfigurationServicePlugin(driver),
                    "files": Files(driver)}
        
    def initialize_configuration_service_without_bootstrap_file(self, provider_name, sdk_key, context_key):
        """
        Initialize configuration service without bootstrap file
        """
        self.fd["configuration_service_plugin"].select_provider_option(provider_name)
        self.fd["configuration_service_plugin"].enter_sdk_key(sdk_key)
        self.fd["configuration_service_plugin"].enter_context_key(context_key)
        self.fd["configuration_service_plugin"].select_initialize_configuration_provider_btn()
        initialization_message = self.fd["configuration_service_plugin"].get_initialization_message_text()
        assert initialization_message == "Configuration Service initialized successfully.", f"Initialization message mismatch. Expected: 'Configuration Service initialized successfully.', Got: '{initialization_message}'"
        self.fd["configuration_service_plugin"].select_ok_button()

    def initialize_configuration_service_with_bootstrap_file(self, provider_name, sdk_key, context_key):
        """
        Initialize configuration service with bootstrap file
        """
        self.fd["configuration_service_plugin"].select_provider_option(provider_name)
        self.fd["configuration_service_plugin"].enter_sdk_key(sdk_key)
        self.fd["configuration_service_plugin"].enter_context_key(context_key)
        self.upload_bootstrap_file("bootstrap.json")
        self.fd["configuration_service_plugin"].select_initialize_configuration_provider_btn()
        initialization_message = self.fd["configuration_service_plugin"].get_initialization_message_text()
        assert initialization_message == "Configuration Service initialized successfully.", f"Initialization message mismatch. Expected: 'Configuration Service initialized successfully.', Got: '{initialization_message}'"
        self.fd["configuration_service_plugin"].select_ok_button()

    def upload_bootstrap_file(self, file):
        """
        Upload bootstrap file for configuration service
        """
        self.fd["configuration_service_plugin"].click_browse_button()
        self.fd["files"].click_downloads_list_item()
        self.fd["files"].send_text_file_name_textbox(file)
        self.fd["files"].click_open_btn()