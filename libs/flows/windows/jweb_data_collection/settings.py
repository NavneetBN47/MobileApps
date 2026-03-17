from MobileApps.libs.flows.windows.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class Settings(JwebDataCollectionFlow):
    flow_name = "settings"

    def click_settings_savebtn(self):
        """
        In Settings tab, clicking on save button
        """
        self.driver.click("settings_savebtn", displayed=False)

    def click_settings_closebtn(self):
        """
        In Settings tab, clicking on close button
        """
        self.driver.click("settings_closebtn", displayed=False)

    def enable_verbose_logs_toggle(self, value):
        """
        In Settings tab, enable verbose logs toggle
        """
        self.driver.check_box("enable_verbose_logs", uncheck=not value)
        self.click_settings_savebtn()
        self.click_settings_closebtn()

    def enable_use_custom_metadata_toggle(self, value):
        """
        In Settings tab, enable use custom metadata values toggle
        """
        self.driver.check_box("enable_use_custom_metadata_toggle", uncheck=not value)

    def disable_use_batching_policy_toggle(self, value):
        """
        In Settings tab, disable use batching policy toggle
        """
        self.driver.check_box("use_batching_policy_toggle", uncheck=not value)

    def select_asset_unit_item(self, unit_type):
        """ 
        in settings, select the asset unit drop down and select unit_type
        """
        self.driver.click("asset_unit_menu_selector", displayed=False)
        self.driver.click("asset_unit_option", format_specifier=[unit_type])

    def clear_text_from_textboxes(self, object_ids):
        """
        In settings page, clear a textbox from the Native context (needed to clear completely clear textbox, list can be added as needed) 
        """
        for object_id in object_ids:
            if object_id not in ['asset_type_textbox', 'app_instance_id_textbox', 'device_id_textbox', 'account_login_id_textbox', 'stratus_user_id_textbox',
                             'tenant_id_textbox', 'model_number_textbox', 'batching_max_event_age_textbox', 'batching_max_event_notification_textbox',
                             'batching_min_event_notification_textbox', 'batching_evaluation_frequency_textbox']:
                raise ValueError("{}: not present within list of textboxes".format(object_id))
            else:
                self.driver.clear_text(object_id)
        return True

    def send_texts_to_textboxes(self, texts_list):
        """
        Given a list of tuples, ('textbox', 'text to send'), populate textboxes
        """
        
        for textbox, text in texts_list:
            # self.swipe_to_object(textbox)
            self.driver.click(textbox, displayed=False)
            self.send_text_to_textbox(textbox, text)

    def send_text_to_textbox(self, object_id, text):
        """
        In settings, enter text into a textbox of app_instance_id_textbox (list can be added as needed)
        """
        if object_id not in ['app_instance_id_textbox', 'batching_max_event_age_textbox', 'asset_type_textbox', 'device_id_textbox', 'model_number_textbox',
                            'batching_max_event_notification_textbox', 'batching_min_event_notification_textbox', 'batching_evaluation_frequency_textbox']:
            raise ValueError("{}: is not found within the settings".format(object_id))

        self.driver.click(object_id)
        self.driver.send_keys(object_id, text)

    def click_use_queue_policy_toggle(self):
        """ 
        in settings tab, enable/disable the queue toggle button
        """
        self.driver.click("use_queue_policy", displayed=True)

    def verify_queue_item_lists(self): 
        """ 
        in queue tab extract the content to verify whether the screen is empty
        """
        return not self.driver.wait_for_object("queue_item_lists", timeout=3, raise_e=False) is False

    def select_data_valve_stack(self, valve_stack):
        """ 
        In Settings tab, select the Data Valves Stack from any one of the drop-down list (Dev, Pie, Staging)
        """
        valve_stack = valve_stack.title()
        if valve_stack not in ["Dev", "Pie", "Staging"]:
            raise ValueError("{}: is not found within the settings".format(valve_stack))
        self.driver.click("data_valve_stack_selector")
        self.driver.click("data_valve_stack_option", format_specifier=[valve_stack])

    def select_data_ingress_stack(self, ingress_stack):
        """ 
        In Settings tab, select the Data Ingress Stack from any one of the drop-down list (Dev, Pie, Staging)
        """
        ingress_stack = ingress_stack.title()
        if ingress_stack not in ["Dev", "Pie", "Staging"]:
            raise ValueError("{}: is not found within the settings".format(ingress_stack))
        self.driver.click("data_ingress_stack_selector")
        self.driver.click("data_ingress_stack_option", format_specifier=[ingress_stack])

    def select_data_valve_and_ingress_stack_values(self, valve_stack, ingress_stack):
        """
        In Settings tab, select Data Valves Stack and Data Ingress Stack 
        """
        self.enable_use_custom_batching_policy_toggle(True)
        self.select_data_valve_stack(valve_stack)
        self.select_data_ingress_stack(ingress_stack)
        self.click_settings_savebtn()
        self.click_settings_closebtn()

    def enable_use_custom_batching_policy_toggle(self, value):
        """
        In Settings tab, enable use custom batching policy toggle
        """
        self.driver.check_box("use_custom_batching_params_toggle", uncheck=not value)