from MobileApps.libs.flows.windows.jweb_storage_manager.home import Home
from MobileApps.libs.flows.windows.jweb_storage_manager.storage_plugin import StoragePlugin
from MobileApps.libs.flows.windows.jweb_storage_manager.jweb_storage_manager_flow import JwebStorageManagerFlow
import MobileApps.resources.const.windows.const as w_const
import pytest
import json
 
@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_05_Storage_Manager(object):
    
    @pytest.mark.storageplugin
    def test_01_verify_if_we_retrieve_details_when_name_field_is_empty_C57240727(self):
        """
        C57240727 - Verify if we can retrieve details when name field is empty
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("Object")
        self.storage_plugin.enter_data("false")
        self.storage_plugin.enter_name(" ")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result["errorType"] == "InternalError"
        assert stored_result["reason"] == "An internal error occurred. Check inner exception for details."
        assert stored_result["innerExceptionMessage"] == "Value cannot be null.\r\nParameter name: name"

    @pytest.mark.storageplugin
    def test_02_verify_whether_stored_resource_can_be_deleted_using_file_name_C59297291(self):
        """
        C59297291: Verify whether the stored resource can be deleted using file name
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.enter_data("hello world")
        self.storage_plugin.enter_source("Test")
        self.storage_plugin.select_retention_policy("manualRemoval")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result["isSuccess"] is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"
        self.storage_plugin.expand_storage_manager_methods("removeResource")
        assert self.storage_plugin.driver.wait_for_object("remove_resource_source_textbox", timeout=5, raise_e=False), \
        "Remove Resource source textbox not found - removeResource method may not have expanded"
        self.storage_plugin.remove_resource_enter_source("")
        self.storage_plugin.click_remove_resource_test_button()
        result = self.storage_plugin.get_remove_resource_result()
        remove_result_content = json.loads(result)
        assert remove_result_content['errorType'] == "ArgumentNull"
        assert remove_result_content['reason'] == "Required parameter 'source' was not provided or is empty"
    
    @pytest.mark.storageplugin
    def test_03_verify_error_when_object_is_selected_with_invalid_data_and_empty_source_C59297228(self):
        """
        C59297228: Verify error response when Object is selected with non-JSON parseable data and empty source
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("Object")
        self.storage_plugin.enter_data("1234")
        self.storage_plugin.enter_source(" ")
        self.storage_plugin.select_retention_policy("manualRemoval")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result['errorType'] == "InvalidOperationError"
        assert stored_result['reason'] == "Invalid metadata object. Required property 'source' could not be found"

    @pytest.mark.storageplugin
    def test_04_verify_whether_we_can_filter_by_guid_C59297255(self):
        """
        C59297255: Verify whether we can filter by a guid to get the specific stored resource
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result["isSuccess"] is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"
        self.storage_plugin.expand_storage_manager_methods("getResourceList")
        assert self.storage_plugin.driver.wait_for_object("get_resource_list_name_textbox", timeout=5, raise_e=False), \
        "Get Resource List name textbox not found - getResourceList method may not have expanded"
        self.storage_plugin.get_list_enter_source(" ")
        self.storage_plugin.click_get_list_test_button()
        get_list = self.storage_plugin.get_list_result()
        get_list_result = json.loads(get_list)
        assert get_list_result['errorType'] == "ArgumentNull"
        assert get_list_result['reason'] == "Required parameter 'source' was not provided or is empty"

    @pytest.mark.storageplugin
    def test_05_verify_we_can_get_list_resource_by_specifying_source_empty_when_connected_to_network_C59297263(self):
        """
        C59297263 - Verify whether can get the list of the resources by giving a specific source is empty - connected to network
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("Object")
        self.storage_plugin.enter_source("storage-manager/documents")
        json_data = '{"title": "my resource", "type": "object", "description": "test resource for automation"}'
        self.storage_plugin.enter_data(json_data)
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result["isSuccess"] is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"
        self.storage_plugin.expand_storage_manager_methods("getResourceList")
        assert self.storage_plugin.driver.wait_for_object("get_resource_list_name_textbox", timeout=5, raise_e=False), \
        "Get Resource List name textbox not found - getResourceList method may not have expanded"
        self.storage_plugin.get_list_enter_source(" ")
        self.storage_plugin.click_get_list_test_button()
        get_list = self.storage_plugin.get_list_result()
        get_list_result = json.loads(get_list)
        assert get_list_result["errorType"] == "ArgumentNull", "Error type should be ArgumentNull"
        assert get_list_result["reason"] == "Required parameter 'source' was not provided or is empty", "Reason should indicate missing source parameter"

    @pytest.mark.storageplugin
    def test_06_verify_we_can_get_list_resource_by_specifying_source_empty_when_connected_to_network_C59297270(self):
        """
        C59297270 - Verify whether can get the list of the resources by giving a specific source is empty - connected to network
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("Object")
        self.storage_plugin.enter_source("storage-manager/documents")
        json_data = '{"title": "my resource", "type": "object", "description": "test resource for automation"}'
        self.storage_plugin.enter_data(json_data)
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        assert stored_result["isSuccess"] is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"
        self.storage_plugin.expand_storage_manager_methods("getResourceList")
        assert self.storage_plugin.driver.wait_for_object("get_resource_list_name_textbox", timeout=5, raise_e=False), \
        "Get Resource List name textbox not found - getResourceList method may not have expanded"
        self.storage_plugin.get_list_enter_source(" ")
        self.storage_plugin.click_get_list_test_button()
        get_list = self.storage_plugin.get_list_result()
        get_list_result = json.loads(get_list)
        assert get_list_result["errorType"] == "ArgumentNull", "Error type should be ArgumentNull"
        assert get_list_result["reason"] == "Required parameter 'source' was not provided or is empty", "Reason should indicate missing source parameter"