from MobileApps.libs.flows.windows.jweb_configuration_service_winui.jweb_configuration_service_flow import JwebConfigurationServiceFlow
import logging
from selenium.common.exceptions import NoSuchElementException
 
class ConfigurationServicePlugin(JwebConfigurationServiceFlow):
    flow_name = "configuration_service_plugin"
 
    def select_initialize_configuration_provider_btn(self):
        """
        Select the initialize provider button in the configuration service plugin.
        Wait for popup to appear after clicking.
        """
        self.driver.click("initialize_configuration_service_btn")
        self.driver.wait_for_object("content_scroll_viewer_popup", timeout=10)

    def select_provider_combobox(self):
        """
        Select the provider combobox in the configuration service plugin.
        """
        self.driver.swipe(anchor_element="configuration_service_header_title", direction="up", distance=2)
        self.driver.click("select_provider_combobox")

    def select_get_configuration_btn(self):
        """
        Select the get configuration button in the configuration service plugin.
        """
        self.driver.scroll_element("get_configuration_btn")
        self.driver.click("get_configuration_btn")

    def select_provider_option(self, provider_name):
        """
        Select a provider option from the provider combobox dropdown.
        Args:provider_name (str): The provider name to select. 
        Options: 'launchdarkly' or 'unsupported_provider'
        """
        self.driver.click("select_provider_combobox", displayed=False)
        
        provider_locators = {
            'launchdarkly': 'launchdarkly_option',
            'unsupported_provider': 'unsupported_provider_option'
        }
        
        if provider_name not in provider_locators:
            raise ValueError(f"Invalid provider name '{provider_name}'. Valid options: {list(provider_locators.keys())}")
        
        locator_key = provider_locators[provider_name]
        self.driver.wait_for_object(locator_key, timeout=10)
        self.driver.click(locator_key)

    def enter_sdk_key(self, sdk_key):
        """
        Enter SDK key in the SDK key textbox.
        Args: sdk_key (str): The SDK key to enter in the textbox
        """
        self.driver.clear_text("sdk_key_textbox")
        self.driver.send_keys("sdk_key_textbox", sdk_key)

    def enter_context_key(self, context_key):
        """
        Enter context key in the context key textbox.
        Args: context_key (str): The context key to enter in the textbox
        """        
        self.driver.clear_text("context_key_textbox")
        self.driver.send_keys("context_key_textbox", context_key)

    def click_browse_button(self):
        """
        Click the Browse button to open file browser dialog.
        """
        self.driver.click("browse_btn")

    def get_initialization_message_text(self):
        """
        Get the text from the initialization message popup.
        Returns: str: The text content of the initialization message
        Raises: Exception: If the message element is not found or text cannot be retrieved
        """
        self.driver.wait_for_object("content_scroll_viewer_popup", timeout=10)
        self.driver.wait_for_object("initialize_message_text", timeout=5)
        return self.driver.get_text("initialize_message_text")

    def get_configuration_message_text(self):
        """
        Get the error message text from the GetConfigResultTextBlock element.
        Returns:
        str: The error message text content    
        Raises:
        Exception: If the message element is not found or text cannot be retrieved
        """
        self.driver.scroll_element("configuration_message_text", direction="down")
        self.driver.wait_for_object("configuration_message_text", timeout=10)
        return self.driver.get_text("configuration_message_text")

    def enter_configuration_key(self, configuration_key):
        """
        Enter a configuration key in the Get Configuration textbox.
        Args: configuration_key (str): The configuration key to enter in the textbox
        """
        self.driver.clear_text("get_configuration_text_box")
        self.driver.send_keys("get_configuration_text_box", configuration_key)

    def select_ok_button(self):
        """
        Select the OK button on the initialization message popup.
        """
        self.driver.click("content_scroll_viewer_popup_ok_button")

    def enter_subscribe_configuration_key(self, configuration_key):
        """
        Enter a configuration key in the Subscribe Configuration textbox.
        Args: configuration_key (str): The configuration key to enter in the subscribe textbox
        """
        self.driver.clear_text("subscribe_configuration_text_box")
        self.driver.send_keys("subscribe_configuration_text_box", configuration_key)

    def select_subscribe_configuration_btn(self):
        """
        Click the Subscribe button for configuration subscription.
        """
        self.driver.wait_for_object("subscribe_configuration_btn", timeout=5)
        self.driver.click("subscribe_configuration_btn")

    def get_subscription_pop_up_message_text(self):
        """
        Get the text from the subscription popup message.
        Returns:
        str: The text content of the subscription popup message    
        Raises:
        Exception: If the message element is not found or text cannot be retrieved
        """
        self.driver.wait_for_object("content_scroll_viewer_popup", timeout=10)
        self.driver.wait_for_object("subscription_success_message", timeout=5)
        return self.driver.get_text("subscription_success_message")

    def click_get_all_configuration_btn(self):
        """
        Click the Get All Configurations button.
        """
        self.driver.scroll_element("get_all_configuration_btn", direction="down")
        self.driver.wait_for_object("get_all_configuration_btn", timeout=5)
        self.driver.click("get_all_configuration_btn", displayed=False)

    def get_all_configuration_list_text(self):
        """
        Get the text content from the Get All Configurations list items.
        Returns:
        str: The text content of all configuration list items    
        Raises:
        Exception: If the list element is not found or text cannot be retrieved
        """
        self.driver.scroll_element("get_all_configuration_list_items", direction="down")
        self.driver.wait_for_object("get_all_configuration_list_items", timeout=10)
        return self.driver.get_text("get_all_configuration_list_items")

    def enter_unsubscribe_configuration_key(self, configuration_key):
        """
        Enter a configuration key in the Unsubscribe Configuration textbox.
        Args: configuration_key (str): The configuration key to enter in the unsubscribe textbox
        """
        self.driver.clear_text("unsubscribe_configuration_text_box")
        self.driver.send_keys("unsubscribe_configuration_text_box", configuration_key)

    def select_unsubscribe_configuration_btn(self):
        """
        Click the Unsubscribe button for configuration unsubscription.
        """
        self.driver.wait_for_object("unsubscribe_configuration_btn", timeout=5)
        self.driver.click("unsubscribe_configuration_btn")

    def get_unsubscription_pop_up_message_text(self):
        """
        Get the text from the unsubscription popup message.
        Returns:
        str: The text content of the unsubscription popup message    
        Raises:
        Exception: If the message element is not found or text cannot be retrieved
        """
        self.driver.wait_for_object("content_scroll_viewer_popup", timeout=10)
        self.driver.wait_for_object("unsubscription_success_message", timeout=5)
        return self.driver.get_text("unsubscription_success_message")

    def select_de_initialize_configuration_provider_btn(self):
        """
        Select the de-initialize provider button in the configuration service plugin.
        """
        self.driver.click("de_initialize_configuration_service_btn")

    def get_all_providers(self):
        """
        Fetch all available providers displayed in the dropdown list.
        Returns a list of provider names (text).
        """
        provider_elements = self.driver.find_object("list_item_provider", multiple=True)
        provider_list = [elem.text.strip() for elem in provider_elements if elem.text.strip()]
        unique_providers = list(dict.fromkeys(provider_list))
        return unique_providers

    def select_weblet_tab(self):
        """
        Select the Weblet tab in the configuration service plugin.
        """
        self.driver.click("weblet_tab_btn")

    def select_configuration_service_tab(self):
        """
        Select the configuration service tab in the configuration service plugin.
        """
        self.driver.click("configuration_service_tab_btn")
    
    def click_subscribe_and_unsubscribe_actions(self, iterations=3):
        """
        Perform rapid subscribe and unsubscribe actions for specified iterations.
        Captures messages on the final iteration.
        Args:iterations (int): Number of subscribe/unsubscribe cycles to perform
        Returns:tuple: (subscription_message, unsubscription_message) from final iteration
        """
        subscription_message = ""
        unsubscription_message = ""
        
        for i in range(iterations):
            self.driver.scroll_element("subscribe_configuration_btn", direction="down", distance=3, time_out=10)
            self.driver.click("subscribe_configuration_btn")
            
            if i == iterations - 1:
                subscription_message = self.get_subscription_pop_up_message_text()
            
            self.select_ok_btn()
            
            self.driver.scroll_element("unsubscribe_configuration_btn", direction="down", distance=3, time_out=10)
            self.driver.click("unsubscribe_configuration_btn")
            
            if i == iterations - 1:
                unsubscription_message = self.get_unsubscription_pop_up_message_text()
            
            self.select_ok_btn()
        
        return subscription_message, unsubscription_message