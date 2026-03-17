from MobileApps.libs.flows.windows.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class ValueStore(JwebDataCollectionFlow):
    flow_name = "value_store"

    def clear_text_from_textboxes(self, object_ids):
        """
        In valuestore page, clear a textbox from the Native context (needed to clear completely clear textbox, list can be added as needed) 
        """
        for object_id in object_ids:
            if object_id not in ['vs_app_instance_id_textbox', 'vs_stratus_user_id_textbox', 'vs_account_login_id_textbox', 'vs_device_id_textbox', 
                              'vs_model_number_textbox', 'vs_tenant_id_textbox', 'vs_system_serial_number_textbox', 'vs_pc_device_uuid_textbox', 
                              'vs_ucde_correlation_textbox', 'vs_consent_basis_id_textbox']:
                raise ValueError("{}: not present within list of textboxes".format(object_id))
            else:
                self.driver.clear_text(object_id)
        return True

    def click_setvaluestore_btn(self):
        """
        In Valuestore tab, clicking on set valuestore button
        """
        self.driver.click("set_valuestore_btn", displayed=False)

    def click_removevaluestore_btn(self):
        """
        In Valuestore tab, clicking on remove valuestore button
        """
        self.driver.click("remove_valuestore_btn", displayed=False)

    def send_texts_to_textboxes(self, texts_list):
        """
        Given a list of tuples, ('textbox', 'text to send'), populate textboxes
        """
        for textbox, text in texts_list:
            self.driver.click(textbox, displayed=False)
            self.send_text_to_textbox(textbox, text)

    def send_text_to_textbox(self, object_id, text):
        """
        Enter text into a textbox found in valuestore page
        """
        if object_id not in ['vs_app_instance_id_textbox', 'vs_stratus_user_id_textbox', 'vs_account_login_id_textbox', 'vs_device_id_textbox', 
                              'vs_model_number_textbox', 'vs_tenant_id_textbox', 'vs_system_serial_number_textbox', 'vs_pc_device_uuid_textbox', 
                              'vs_ucde_correlation_textbox', 'vs_consent_basis_id_textbox', 'vs_remove_keys_textbox']:
            raise ValueError("{}: is not found within the Data Collection plugin".format(object_id))

        self.driver.click(object_id)
        self.driver.send_keys(object_id, text)