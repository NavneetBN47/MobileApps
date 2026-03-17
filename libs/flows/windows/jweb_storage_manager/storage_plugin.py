import json
from selenium.common.exceptions import *
from time import time
from MobileApps.libs.flows.windows.jweb_storage_manager.jweb_storage_manager_flow import JwebStorageManagerFlow
from time import sleep
import logging
import time

class StoragePlugin(JwebStorageManagerFlow):
    flow_name = "storage_plugin"

    def navigate_to_storage_plugin(self):
        """
        Navigate to Storage Manager weblet
        """
        try:
            self.driver.click("storage_manager_weblet")
            sleep(2)
            return True
        except Exception as e:
            logging.error(f"Failed to navigate to storage plugin: {str(e)}")
            return False
    
    def expand_store_object_resource_method(self):
        """
        Expand the Storage.storeObjectResource()/store.storeStringResource() method
        """
        try:
            self.driver.click("store_object_resource_method")
            sleep(2)
            return True
        except Exception as e:
            logging.error(f"Failed to expand store object resource method: {str(e)}")
            return False
    
    def expand_store_method_section(self):
        """
        Expand the method Storage.storeObjectResource()/store.storeStringResource()
        """
        self.driver.click("store_method_section_chevron")

    def expand_storage_manager_methods(self, method):
        """
        Expand the Storage Manager method dropdown by clicking as soon as it is found and visible.
        """
        for _ in range(10):
            obj = self.driver.wait_for_object("expand_storage_manager_method", format_specifier=[method], timeout=3, raise_e=False)
            if obj:
                self.driver.click("expand_storage_manager_method", format_specifier=[method])
                return
            self.driver.swipe(direction="down", distance=5)
            sleep(5)
        logging.error(f"Could not find or click drop down for {method}")

    def select_store_type(self, store_type):
        """
        Select store type (String or Object)
        :param store_type: "String" or "Object"
        """
        if store_type not in ["String", "Object"]:
            raise ValueError(f"Invalid store_type: {store_type}. Must be 'String' or 'Object'")
        
        self.driver.click("store_type_combobox")
        self.driver.click("store_type_option", format_specifier=[store_type])

    def select_encoding(self, encoding):
        """
        Select encoding type (Base64, plaintext)
        :param encoding: "Base64" or "plaintext"
        """
        if encoding not in ["base64", "plaintext"]:
            raise ValueError(f"Invalid encoding: {encoding}. Must be 'base64' or 'plaintext'")
        
        self.driver.click("encoding_combobox")
        self.driver.click("encoding_option", format_specifier=[encoding])
        sleep(5)

    def enter_data(self, data):
        """
        Enter data in the data field
        :param data: String data to enter
        """
        self.driver.click("data_field")
        self.driver.clear_text("data_field")
        self.driver.send_keys("data_field", data)

    def enter_source(self, source):
        """
        Enter source value (keep as default or custom value)
        :param source: Source namespace value
        """
        if source:
            self.driver.clear_text("source_field")
            sleep(2)
            self.driver.click("source_field")
            sleep(1)
            self.driver.send_keys("source_field", source)
            sleep(2)

    def enter_name(self, name):
        """
        Enter resource name (should end with .txt as per requirement)
        :param name: Resource name ending with file extension
        """
        self.driver.clear_text("name_edit")
        sleep(2)
        self.driver.click("name_edit")
        self.driver.send_keys("name_edit", name)

    def enter_mime_type(self, mime_type):
        """
        Enter MIME type (e.g., application/json)
        :param mime_type: MIME type string
        """
        self.driver.click("mime_type_edit", displayed=False)
        self.driver.clear_text("mime_type_edit")
        self.driver.send_keys("mime_type_edit", mime_type)

    def select_retention_policy(self, policy_type):
        """
        Select retention policy type
        :param policy_type: "time", "never", etc.
        """
        if policy_type not in ["time", "ephemeral", "manualRemoval"]:
            raise ValueError(f"Invalid policy_type: {policy_type}. Must be 'time', 'ephemeral', or 'manualRemoval'")

        self.driver.click("retention_type_combobox")
        sleep(3)
        self.driver.click("retention_policy_option", format_specifier=[policy_type])

    def enter_retention_expiration_time(self, text):
        """
        Enter retention expiration time in minutes
        :param minutes: Number of minutes for retention
        """
        self.driver.click("retention_expiration_field")
        self.driver.clear_text("retention_expiration_field")
        sleep(5)
        self.driver.send_keys("retention_expiration_field", text)
        sleep(2)

    def click_store_button(self):
        """
        Click the Store/Execute button to store the resource
        """
        self.driver.click("store_execute_button", displayed=False)

    def get_store_result(self):
        """
        Get the result of the store operation
        :return: Result text from the operation
        """
        return self.driver.get_attribute("result_block", "text", displayed=False, raise_e=False)

    def remove_resource_enter_source(self, text):
        """
        send text parameter value to the source textbox under remove resource
        """
        self.driver.click("remove_resource_source_textbox", displayed=False, timeout=5)
        self.driver.clear_text("remove_resource_source_textbox")
        self.driver.send_keys("remove_resource_source_textbox", text)

    def click_remove_resource_test_button(self):
        """
        clicks the storage manager remove resource test button
        :return: 
        """
        self.driver.click("remove_resource_test_btn", displayed=False)

    def get_remove_resource_result(self):
        """
        Gets the result content under storageManager.removeResource
        :return: Text content from the result area
        """
        return self.driver.get_attribute("remove_resource_result_content", "text", displayed=False)

    def click_get_list_test_button(self):
        """
        Click the Get List Test button to retrieve the resource
        """
        self.driver.click("get_list_test_button", displayed=False)

    def get_list_result(self):
        """
        Get the result of the get list operation
        :return: Result text from the operation
        """
        return self.driver.get_attribute("get_list_result", "text", raise_e=False, displayed=False)
    
    def get_list_enter_name(self, text):
        """
        send text parameter value to the name textbox under get resource list
        """
        self.driver.click("get_resource_list_name_textbox", displayed=False, timeout=5)
        self.driver.clear_text("get_resource_list_name_textbox")
        self.driver.send_keys("get_resource_list_name_textbox", text)

    def get_list_enter_source(self, source):
        """
        Under get list enter source value (keep as default or custom value)
        :param source: Source namespace value
        """
        if source:
            self.driver.click("get_list_source_field", displayed=False, timeout=5)
            self.driver.clear_text("get_list_source_field")
            self.driver.send_keys("get_list_source_field", source)