from MobileApps.libs.flows.windows.jweb_storage_manager.home import Home
from MobileApps.libs.flows.windows.jweb_storage_manager.storage_plugin import StoragePlugin
from MobileApps.libs.flows.windows.jweb_storage_manager.jweb_storage_manager_flow import JwebStorageManagerFlow
import MobileApps.resources.const.windows.const as w_const
import pytest
import json

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_02_Storage_Manager(object):
    
    @pytest.mark.storageplugin
    def test_01_verify_if_we_retrieve_details_when_source_field_is_empty_C57240722(self):
        """
        C57240722 - Verify if we can retrieve details when source field is empty
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("Object")
        self.storage_plugin.enter_source(" ")
        self.storage_plugin.enter_data("true")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result["errorType"] == "InvalidOperationError", "Error type should be InvalidOperationError"
        assert stored_result["reason"] == "Invalid metadata object. Required property 'source' could not be found", "Reason should indicate missing source property"
        
    @pytest.mark.storageplugin
    def test_02_verify_if_we_retrieve_details_when_source_field_is_empty_and_with_valid_name_field_C57240716(self):
        """
        C57240716 - Verify if we can retrieve details when source field is empty and with valid name field
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("Object")
        self.storage_plugin.enter_source(" ")
        self.storage_plugin.enter_data("true")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result["errorType"] == "InvalidOperationError", "Error type should be InvalidOperationError"
        assert stored_result["reason"] == "Invalid metadata object. Required property 'source' could not be found", "Reason should indicate missing source property"

    @pytest.mark.storageplugin
    def test_03_verify_wether_we_can_store_a_resource_without_providing_source_C59297217(self):
        """
        C59297217: Verify whether we can store a resource without providing source
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.enter_source(" ")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result['errorType'] == "InvalidOperationError"
        assert stored_result['reason'] == "Invalid metadata object. Required property 'source' could not be found"

    @pytest.mark.storageplugin
    def test_04_verify_wether_we_can_store_a_resource_without_providing_name_C59297218(self):
        """
        C59297218: Verify whether we can store a resource without providing a name for the resource
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.enter_name(" ")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result['errorType'] == "InternalError"
        assert stored_result['reason'] == "An internal error occurred. Check inner exception for details."
        assert stored_result['innerExceptionMessage'] == "Value cannot be null.\r\nParameter name: name"

    @pytest.mark.storageplugin
    def test_05_verify_wether_we_can_store_a_resource_without_providing_data_for_the_resource_C59297220(self):
        """
        C59297220: Verify whether we can store a resource without providing a data for the resource
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.enter_data(" ")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result['errorType'] == "ArgumentNull"
        assert stored_result['reason'] == "Required parameter data was not provided or is empty"

    @pytest.mark.storageplugin
    def test_06_verify_wether_we_can_store_a_resource_without_providing_mimetype_C59297219(self):
        """
        C59297219: Verify whether we can store a resource without providing a mimetype for the resource
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("plaintext")
        self.storage_plugin.enter_data("hello world")
        self.storage_plugin.enter_source("Test")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.enter_mime_type("")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result['errorType'] == "InvalidOperationError"
        assert stored_result['reason'] == "Invalid metadata object. Required property 'mimeType' could not be found"