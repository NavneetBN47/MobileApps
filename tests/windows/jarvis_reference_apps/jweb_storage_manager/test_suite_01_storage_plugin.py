from MobileApps.libs.flows.windows.jweb_storage_manager.home import Home
from MobileApps.libs.flows.windows.jweb_storage_manager.storage_plugin import StoragePlugin
from MobileApps.libs.flows.windows.jweb_storage_manager.jweb_storage_manager_flow import JwebStorageManagerFlow
import MobileApps.resources.const.windows.const as w_const
import pytest
import json

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_01_Storage_Manager(object):
    
    @pytest.mark.storageplugin
    def test_01_verify_whether_to_store_javascript_object_resource_mime_type_C57059724(self):
        """
        C57059724: Verify whether to store JavaScript Object Resource Mime Type
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("base64")
        self.storage_plugin.enter_data("eyB0aXRsZTogJ2RhdGEgdGl0bGUnLCBkZXNjcmlwdGlvbjogJ2kgYW0gc3RvcmluZyBzb21ldGhpbmcgYXdlc29tZScgfQ==")
        self.storage_plugin.enter_source("storage-manager/documents")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.enter_mime_type("application/json")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        status = stored_result["isSuccess"]
        assert status is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"

    @pytest.mark.storageplugin
    def test_02_verify_if_source_name_can_be_changed_C57059735(self):
        """
        C57059735: Verify if the source name can be changed
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("plaintext")
        self.storage_plugin.enter_data("hello world")
        self.storage_plugin.enter_source("Test")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.enter_mime_type("text/plain")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        status = stored_result["isSuccess"]
        assert status is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"

    @pytest.mark.storageplugin
    def test_03_verify_if_we_can_get_string_resource_name_and_source_of_the_resource_connected_to_network_C56978606(self):
        """
        C56978606: Verify if we can get string resource name and source of the resource connected to network
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.enter_source("storage-manager/documents")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        status = stored_result["isSuccess"]
        assert status is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"
 
    @pytest.mark.storageplugin
    def test_04_verify_whether_resource_can_store_respective_tenant_id_C59297368(self):
        """
        C59297368: Verify whether a resource can be stored in the folder with the respective tenant ID
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("base64")
        self.storage_plugin.enter_data("true")
        self.storage_plugin.enter_source("storage-manager/documents")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.enter_mime_type("application/json")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert "JarvisAuto-rcb" in stored_result["value"]["uri"]
 
    @pytest.mark.storageplugin
    def test_05_verify_error_message_when_object_is_selected_and_data_is_not_parseable_to_json_C59297229(self):
        """
        C59297229: Verify error message when when Object is selected and "Data" is not parseable to JSON
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("Object")
        invalid_json_data = '{"title": "test", "incomplete": true'
        self.storage_plugin.enter_data(invalid_json_data)
        self.storage_plugin.enter_source("storage-manager/documents")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result["errorType"] == "parameterError", "Error type should be parameterError"
        assert stored_result["reason"] == "Data is not a valid JSON", "Reason should indicate invalid JSON data"
 
    @pytest.mark.storageplugin
    def test_06_verify_we_can_store_string_resource_with_text_plain_mime_type_and_encoding_plain_text_C59297210(self):
        """
        C59297210: Verify whether we can store a string resource of mime type - text/Plain and Encoding Plain text
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("plaintext")
        self.storage_plugin.enter_data("hello world")
        self.storage_plugin.enter_source("storage-manager/documents")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.enter_mime_type("text/plain")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result["isSuccess"] is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"
 
    @pytest.mark.storageplugin
    def test_07_verify_we_can_store_string_resource_with_text_plain_mime_type_and_encoding_base64_C59297211(self):
        """
        C59297211: Verify whether we can store a string resource of mime type - text/Plain and Encoding as Base64
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("base64")
        self.storage_plugin.enter_data("bXkgcmVzb3VyY2Vz")
        self.storage_plugin.enter_source("storage-manager/documents")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.enter_mime_type("text/plain")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result["isSuccess"] is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"