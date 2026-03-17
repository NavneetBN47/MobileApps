from MobileApps.libs.flows.windows.jweb_storage_manager.home import Home
from MobileApps.libs.flows.windows.jweb_storage_manager.storage_plugin import StoragePlugin
from MobileApps.libs.flows.windows.jweb_storage_manager.jweb_storage_manager_flow import JwebStorageManagerFlow
import MobileApps.resources.const.windows.const as w_const
import pytest
import json
 
@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_03_Storage_Manager(object):
    
    @pytest.mark.storageplugin
    def test_01_verify_wether_stored_resource_can_be_deleted_using_source_name_C59297243(self):
        """
        C59297243: Verify whether the stored resource can be deleted using source name
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
        self.storage_plugin.remove_resource_enter_source("Test")
        self.storage_plugin.click_remove_resource_test_button()
        result = self.storage_plugin.get_remove_resource_result()
        remove_result_content = json.loads(result)
        assert remove_result_content['isSuccess'] is True, "Remove resource operation failed"

    @pytest.mark.storageplugin
    def test_02_verify_wether_we_can_get_the_list_of_multiple_resources_C59297253(self):
        """
        C59297253: Verify whether we can get the list of multiple resources by giving multiple names
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
        self.storage_plugin.click_get_list_test_button()
        get_list = self.storage_plugin.get_list_result()
        get_list_result = json.loads(get_list)
        assert get_list_result["isSuccess"] is True, "Get list operation failed"
        assert "value" in get_list_result, "Response should contain 'value' key"
        assert "items" in get_list_result["value"], "Value should contain 'items' key"
        value_item = get_list_result["value"]["items"][0]
        assert value_item["name"] == "my-resource.txt", "Item name should match the stored resource name"
        assert value_item["source"] == "storage-manager/documents", "Item source should match the stored resource source"
        assert value_item["uri"] != "", "URI should not be empty"
        assert value_item["guid"] != "", "GUID should not be empty"
        assert value_item["tenantId"] == "JarvisAuto-rcb", "Tenant ID should match the expected value"

    @pytest.mark.storageplugin
    def test_03_verify_whether_resources_are_getting_retrieved_C59297254(self):
        """
        C59297254: Verify whether resources are getting retrieved
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
        self.storage_plugin.get_list_enter_name("")
        self.storage_plugin.click_get_list_test_button()
        get_list = self.storage_plugin.get_list_result()
        get_list_result = json.loads(get_list)
        assert get_list_result["isSuccess"] is True, "Get list operation failed"
        assert "value" in get_list_result, "Response should contain 'value' key"
        assert "items" in get_list_result["value"], "Value should contain 'items' key"
        value_item = get_list_result["value"]["items"][0]
        assert value_item["name"] == "my-resource.txt", "Item name should match the stored resource name"
        assert value_item["source"] == "storage-manager/documents", "Item source should match the stored resource source"
        assert value_item["uri"] != "", "URI should not be empty"
        assert value_item["guid"] != "", "GUID should not be empty"
        assert value_item["tenantId"] == "JarvisAuto-rcb", "Tenant ID should match the expected value"

    @pytest.mark.storageplugin
    def test_04_verify_the_response_when_source_name_is_capitalized_C59297256(self):
        """
        C59297256: Verify the response when the source name is passed in capital letters
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
        self.storage_plugin.get_list_enter_source("DEVICES-MFE")
        self.storage_plugin.click_get_list_test_button()
        get_list = self.storage_plugin.get_list_result()
        get_list_result = json.loads(get_list)
        assert get_list_result["isSuccess"] is True, "Get list operation failed"
        assert "value" in get_list_result, "Response should contain 'value' key"

    @pytest.mark.storageplugin
    def test_05_verify_if_we_can_get_object_resource_by_specifying_name_and_source_connected_to_network_C59297252(self):
        """
        C59297252 - Verify if we can get a Object resource by specifying the Type, Name and source of the resource - connected to network
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
 
    @pytest.mark.storageplugin
    def test_06_verify_we_can_get_list_resource_by_specifying_source_when_connected_to_network_C59297275(self):
        """
        C59297275 - Verify whether can get the list of the resources by giving a specific source - connected to network
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
        self.storage_plugin.get_list_enter_source("storage-manager/documents")
        self.storage_plugin.click_get_list_test_button()
        get_list = self.storage_plugin.get_list_result()
        get_list_result = json.loads(get_list)
        assert get_list_result["isSuccess"] is True, "Get list operation failed"
        assert "value" in get_list_result, "Response should contain 'value' key"
        assert "items" in get_list_result["value"], "Value should contain 'items' key"
        value_item = get_list_result["value"]["items"][0]
        assert value_item["name"] == "my-resource.txt", "Item name should match the stored resource name"
        assert value_item["source"] == "storage-manager/documents", "Item source should match the stored resource source"
        assert value_item["uri"] != "", "URI should not be empty"
        assert value_item["guid"] != "", "GUID should not be empty"
        assert value_item["tenantId"] == "JarvisAuto-rcb", "Tenant ID should match the expected value"