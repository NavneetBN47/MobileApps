from MobileApps.libs.flows.android.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow
from time import sleep
from selenium.common.exceptions import *

class DataCollectionSettings(JwebDataCollectionFlow):
    flow_name = "data_collection_settings"

    def select_use_custom_metadata_values_switch(self, toggle=True):
        """
        In settings tab, enable the use_custom_metadata_values toggle
        """
        self.driver.scroll("use_custom_metadata_values_toggle")
        self.driver.check_box("use_custom_metadata_values_toggle", uncheck=not toggle)

    def select_settings_back_button(self):
        """
        In settings tab, click the back button
        """
        self.driver.click("settings_back_button")

    def select_settings_save_button(self):
        """
        In settings tab, click the save button
        """
        self.driver.click("settings_save_button")

    def open_stack_list(self):
        """
        Open data valve stack options 
        """
        self.driver.scroll("settings_data_valve_stack_label")
        self.driver.click("settings_data_valve_stack_label")

    def open_data_ingress_stack_list(self):
        """
        Open data ingress stack options
        """
        self.driver.scroll("settings_data_ingress_stack_label")
        self.driver.click("settings_data_ingress_stack_label")

    def stack_option_button(self, stack_name):
        """
        After opening data valve list, select a given stack 
        Force "Stage" into "Staging" to match other stack location text
        """
        stack_name = stack_name.title()
        stack_name = "Staging" if stack_name == "Stage" else stack_name
        if stack_name not in ['Local', 'Dev', 'Pie', 'Staging', 'Production', 'Custom']:
            raise ValueError("{} not present within the list of stack options".format(stack_name)) 
        self.driver.click("stack_option_button", format_specifier=[stack_name])
        
    def select_tree_file(self):
        """
        Open tree file selector
        """
        self.driver.click("choose_tree_file")
        
    def test_cdm_tree_button(self):
        """
        Tap the test CDM tree button
        """
        self.driver.click("test_cdm_tree")

    def select_data_valve_and_ingress_stack_values(self, stack_name):
        """
        In Settings tab, disable the value store toggle and custom metadata toggle, if it is enabled already
        Enable the custom batching toggle, if it is disabled already
        Disable the allow batch toggle, if it is enabled already
        Then, select Data Valves Stack and Data Ingress Stack 
        """
        sleep(2)
        self.select_values_store_toggle_button(False)
        self.select_use_custom_batching_switch(True)
        self.select_allow_batch_switch(False)
        self.select_use_custom_metadata_values_switch(False)
        self.open_data_ingress_stack_list()
        self.stack_option_button(stack_name)
        self.open_stack_list()
        self.stack_option_button(stack_name)
        self.select_settings_save_button()

    def clear_text_from_textboxes(self, object_ids):
        """
        In settings tab, clear a textbox from the Native context (needed to clear completely clear textbox, list can be added as needed) 
        """
        for object_id in object_ids:
            if object_id not in ['settings_vs_app_instance_id', 'settings_vs_stratus_user_id',
                                'settings_vs_account_login_id', 'settings_vs_device_id', 'settings_vs_model_number', 'settings_vs_tenant_id']:
                raise ValueError("{}: not present within list of textboxes".format(object_id))
            else:
                self.driver.clear_text(object_id)

    def select_values_store_toggle_button(self, toggle=True):
        """
        In settings tab, enable the values store toggle button
        """
        self.driver.check_box("settings_value_store", uncheck=not toggle)

    def send_text_to_textbox(self, object_id, text):
        """
        In settings tab, Enter text into the textboxes
        """
        if object_id not in ['settings_vs_app_instance_id','settings_vs_consent_basis_id', 'settings_vs_stratus_user_id','settings_vs_account_login_id', 
                            'settings_vs_device_id', 'settings_vs_model_number', 'settings_vs_tenant_id', 'settings_app_instanced_id','settings_asset_type',
                            'settings_app_instanced_id','settings_stratus_user_id', 'settings_device_id']:
            raise ValueError("{}: is not found within the Data Collection plugin".format(object_id))
        self.driver.scroll(object_id)
        self.driver.click(object_id)
        self.driver.send_keys(object_id, text)

    def send_texts_to_textboxes(self, texts_list):
        """
        Given a list of tuples, ('textbox', 'text to send'), populate textboxes
        """
        for textbox, text in texts_list:
            self.driver.scroll(textbox)
            self.driver.click(textbox, displayed=False)
            self.send_text_to_textbox(textbox, text)

    def clear_text_from_textbox(self, object_ids):
        """
        In settings, clear textboxes from the Native context (needed to completely clear textboxes).
        """
        for object_id in object_ids:
            if object_id not in ['settings_asset_type', 'settings_app_instanced_id', 'settings_stratus_user_id']:
                raise ValueError("{}: not present within the list of textboxes".format(object_id))
            self.driver.scroll(object_id)
            self.driver.clear_text(object_id)
        self.select_settings_save_button()

    def select_queue_toggle_button(self, toggle=True):
        """
        In settings tab, disable the queue toggle button
        """
        self.driver.check_box("settings_queue_toggle", uncheck=not toggle)

    def select_use_custom_batching_switch(self, toggle=True):
        """
        In settings tab, enable the use custom batching toggle
        """
        self.driver.check_box("settings_use_custom_batching_toggle", uncheck=not toggle)

    def select_allow_batch_switch(self, toggle=True):
        """
        In settings tab, disable the allow batch toggle
        """
        self.driver.check_box("settings_allow_batch_toggle", uncheck=not toggle)

    def native_select_asset_unit_item(self, unit_type):
        """ 
        in use custom metadata, select the asset unit drop down and select unit_type
        """
        if unit_type not in ['desktop', 'mobile', 'solution']:
            raise ValueError("{}: is not a unit_type. unit_type must be: 'desktop' 'mobile' or 'solution'")
        
        try:
            self.driver.click("asset_unit", raise_e=False)
        except NoSuchElementException:
            self.driver.swipe(direction="down")
            self.driver.click("asset_unit", raise_e=False)
            self.driver.click("asset_unit_selector", format_specifier=[unit_type])