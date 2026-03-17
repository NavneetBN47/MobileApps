from MobileApps.libs.flows.ios.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

class DataCollectionSettings(JwebDataCollectionFlow):
    flow_name = "data_collection_settings"
    available_textboxes = ['ios_settings_vs_app_instance_id', 'ios_settings_vs_stratus_user_id', 'ios_settings_vs_account_login_id', 
                          'ios_settings_vs_tenant_id', 'settings_app_instance_id', 'ios_settings_vs_consent_basis_id', 'ios_settings_device_id',
                          'maximum_event_count', 'minimum_event_count', 'maximum_event_age_in_seconds', 'cdm_empty_gun_textbox']

    def select_settings_back_button(self):
        """
        Selects the Settings back button in the top navigation bar
        """
        self.driver.click("settings_back_button")

    def select_use_custom_metadata_values_switch(self, value):
        """
        Select 'Use custom Metadata values' such that it matches the value parameter
        """
        self.toggle_action("use_custom_metadata_values_switch", direction='up', uncheck=not value)
                
    def select_data_valve_stack_button(self):
        """ 
        Select after scrolling and find for the Stack button under Data Valves Stack label
        """
        self.driver.scroll("data_valve_stack_button", raise_e=False, check_end=False)
        self.driver.click("data_valve_stack_button")
                
    def select_data_collection_back_button(self):
        """
        After selecting select data valve stack option selects the back button in the top navigation bar
        """
        self.driver.click("data_collection_back_button")

    def select_stack_option(self, stack_name):
        """
        After selecting select data valve stack option, select a given stack 
        """
        stack_name = stack_name.title()
        stack_name = "Staging" if stack_name == "Stage" else stack_name
        if stack_name not in ['Local', 'Dev', 'Pie', 'Staging', 'Production', 'Custom']:
            raise ValueError("{} not present within the list of stack options".format(stack_name))
        self.driver.click("stack_option_button", format_specifier=[stack_name])

    def choose_stack(self, stack_name):
        """
        Disable value store, custom metadata, batch, queue switches and enable verbose logging
        Enable custom batching parameters
        Select the stack name from the list of stack options
        """
        self.select_value_store_toggle_button(False)
        self.select_use_custom_metadata_values_switch(False)
        self.select_allow_batch_toggle_button(False)
        self.select_use_custom_batching_parameters_toggle_button(True)
        self.select_queue_toggle_button(False)
        self.select_enable_verbose_log_switch(True)
        self.select_data_valve_stack_button()
        self.select_stack_option(stack_name)
        self.select_data_collection_back_button()

    def select_mock_valve_controller_switch(self, value):
        """
        Select this switch to use mock data
        """
        self.driver.scroll("mock_option_switch", direction='up')
        self.driver.check_box("mock_option_switch", uncheck=not value)

    def select_value_store_toggle_button(self, value):
        """
        In settings tab, enable the value store toggle button
        """
        try:
            self.toggle_action("ios_settings_value_store", direction='down', uncheck=not value)
        except (NoSuchElementException):
            self.toggle_action("ios_settings_value_store", direction='up', uncheck=not value)

    def select_allow_batch_toggle_button(self, value):
        """
        In settings tab, disable the allow batch toggle button
        """
        self.toggle_action("allow_batch_switch", direction='up', uncheck=not value)

    def send_texts_to_textboxes(self, texts_list):
        """
        Given a list of tuples, ('textbox', 'text to send'), populate textboxes
        """
        for textbox, text in texts_list:
            self.driver.scroll(textbox, raise_e=False)
            self.send_text_to_textbox(textbox, text)

    def send_text_to_textbox(self, object_id, text):
        """
        Enter text into a textbox found in either the CDM or LEDM tree pages if the text value is not already present
        """
        if object_id not in self.available_textboxes:
            raise ValueError("{}: is not found within the Data Collection plugin".format(object_id))
        
        if self.driver.get_attribute(object_id, "value") != text:
            self.driver.click(object_id)
            self.driver.clear_text(object_id)
            self.driver.send_keys(object_id, f'{text}\n')

    def ios_select_data_ingress_btn(self):
        """
        From the Request Logs page, select data ingress button
        """
        self.driver.click("ios_data_ingress_btn")

    def verify_data_ingress_controller_status_code(self, status_code):
        """
        status_code: code passed into data_ingress_status_code's format specifier
        From the Request Logs page, verify the status_code from the url found in the Data ingress request
        """
        self.driver.wait_for_object("data_ingress_status_code", format_specifier=[status_code])

    def select_enable_verbose_log_switch(self, value):
        """
        In Settings tab, select 'enable verbose logging' toggle
        """
        self.toggle_action("verbose_log_switch", direction='up', uncheck=not value)
        
    def clear_textbox(self, object_id):
        self.driver.clear_text(object_id)

    def select_queue_toggle_button(self, value):
        """
        In settings tab, disable the queue toggle button
        """
        self.toggle_action("allow_queue_switch", direction='up', uncheck=not value)

    def toggle_action(self, switch_obj: str, uncheck=False, direction='down'):
        """
        Handle the toggle switch for the given switch_obj
        """
        if switch_obj not in ["ios_settings_value_store", "use_custom_metadata_values_switch", "allow_batch_switch", "verbose_log_switch",
                                "allow_queue_switch", "use_custom_batching_parameters", "send_multiple_event_toggle_btn"]:
            raise ValueError("{}: not present within list of toggle".format(switch_obj))

        try:
            self.driver.scroll(switch_obj, direction=direction, raise_e=False)
            self.driver.send_keys("keyboard_element", Keys.RETURN)
            self.driver.check_box(switch_obj, uncheck=uncheck)
        except (TimeoutException, NoSuchElementException):
            self.driver.scroll(switch_obj, direction=direction, raise_e=False)
            self.driver.check_box(switch_obj, uncheck=uncheck)
    
    def select_use_custom_batching_parameters_toggle_button(self, value):
        """
        In settings tab, enable the use custom batching parameter toggle button
        """
        self.toggle_action("use_custom_batching_parameters", direction='up', uncheck=not value)

    def send_multiple_event(self, value):
        """
        Sends multiple events under Send UI Event based on the provided value.
        """
        self.driver.click("send_multiple_event")
        for digits in str(value):  
            key_locator = f"keyboard_element_{digits}"
            self.driver.click(key_locator)

    def enable_send_multiple_event_toggle(self, value):
        """
        Enable the send multiple event toggle
        """
        self.toggle_action("send_multiple_event_toggle_btn", direction='down', uncheck=not value)

    def select_asset_unit_item(self, unit_type):
        """ 
        in settings, select the asset unit drop down and select unit_type
        """
        if unit_type not in ['Desktop', 'Mobile', 'Solution']:
            raise ValueError("{}: is not a unit_type. unit_type must be: 'Desktop' 'Mobile' or 'Solution'")
        
        self.driver.click("asset_unit_menu_selector")
        self.driver.click("asset_unit", format_specifier=[unit_type])
        self.driver.click("navigation_back_btn")