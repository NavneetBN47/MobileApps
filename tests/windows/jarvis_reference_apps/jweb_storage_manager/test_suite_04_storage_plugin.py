from MobileApps.libs.flows.windows.jweb_storage_manager.home import Home
from MobileApps.libs.flows.windows.jweb_storage_manager.storage_plugin import StoragePlugin
from MobileApps.libs.flows.windows.jweb_storage_manager.jweb_storage_manager_flow import JwebStorageManagerFlow
import MobileApps.resources.const.windows.const as w_const
import pytest
import json
 
@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_04_Storage_Manager(object):
    
    @pytest.mark.storageplugin
    def test_01_verify_whether_we_can_store_octet_using_encoding_type_as_base_64_C59297216(self):
        """
        C59297216 - Verify whether we can store octet using encoding type as base 64
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("base64")
        self.storage_plugin.enter_data("ERQVHykzPkpWY3F/jp2tvMnU3ubs8fX5+/z8/Pr39PDq5d/Y0cvCu7Oro5uTjIR9dm9pY11ZVFBMSUZEQT47O" \
                                        "TY0MjAuLSopJyUjIR8eHBsZGRcWFRUUExMSEREQDw8ODg4ODg0NDAwLCwoKCgoKCwsLDA0NDQ4ODg4ODw8QERI=")
        self.storage_plugin.enter_name("my-resource.mp4")
        self.storage_plugin.enter_mime_type("application/octet")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        status = stored_result["isSuccess"]
        assert status is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"

    @pytest.mark.storageplugin
    def test_02_verify_the_behaviour_of_retention_policy_when_the_value_is_selected_as_manual_removal_C59297223(self):
        """
        C59297223 - Verify the behaviour of retention policy when the value is selected as manual removal
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("plaintext")
        self.storage_plugin.enter_data("hello world")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.enter_mime_type("text/plain")
        self.storage_plugin.select_retention_policy("manualRemoval")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        status = stored_result["isSuccess"]
        assert status is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"
    
    @pytest.mark.storageplugin
    def test_03_verify_whether_we_can_store_a_javascript_object_resource_of_mime_type_application_json_C59297212(self):
        """
        C59297212 - Verify whether  we can store a Javascript object resource of mime type - application/json
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("plaintext")
        json_data = '{"title":"this is my data","description":"I am storing this object"}'
        self.storage_plugin.enter_data(json_data)
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        status = stored_result["isSuccess"]
        assert status is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"
    
    @pytest.mark.storageplugin
    def test_04_verify_the_behaviour_of_retention_policy_when_the_value_is_selected_as_ephermal_C59297222(self):
        """
        C59297222 - Verify the behaviour of retention policy when the value is selected as ephermal
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("plaintext")
        self.storage_plugin.enter_data("hello world")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.enter_mime_type("text/plain")
        self.storage_plugin.select_retention_policy("ephemeral")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        status = stored_result["isSuccess"]
        assert status is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"

    @pytest.mark.storageplugin
    def test_05_verify_the_behaviour_of_retention_policy_when_the_value_is_selected_as_time_C59297231(self):
        """
        C59297231 - Verify the behaviour of retention policy when the value is selected as time
        """
        self.storage_plugin.expand_storage_manager_methods("storeStringResource")
        assert self.storage_plugin.driver.wait_for_object("store_type_combobox", timeout=5, raise_e=False), \
        "Store Type combobox not found - storeStringResource method may not have expanded"
        self.storage_plugin.select_store_type("String")
        self.storage_plugin.select_encoding("plaintext")
        self.storage_plugin.enter_data("hello world")
        self.storage_plugin.enter_name("my-resource.txt")
        self.storage_plugin.enter_mime_type("text/plain")
        self.storage_plugin.select_retention_policy("time")
        self.storage_plugin.enter_retention_expiration_time("5")
        self.storage_plugin.click_store_button()
        result = self.storage_plugin.get_store_result()
        stored_result = json.loads(result)
        status = stored_result["isSuccess"]
        assert status is True, "Storage operation failed"
        assert stored_result["value"]["uri"] != "", "URI should not be empty"
        assert stored_result["value"]["guid"] != "", "GUID should not be empty"
    
    @pytest.mark.storageplugin
    def test_06_verify_whether_can_get_the_list_of_the_resources_by_giving_a_specific_source_C59297257(self):
        """
        C59297257 - Verify whether we can get the list of the resources by giving a specific source
        """
        self.storage_plugin.expand_storage_manager_methods("getResourceList")
        assert self.storage_plugin.driver.wait_for_object("get_resource_list_name_textbox", timeout=5, raise_e=False), \
        "Get Resource List name textbox not found - getResourceList method may not have expanded"
        self.storage_plugin.click_get_list_test_button()
        get_list = self.storage_plugin.get_list_result()
        get_list_result = json.loads(get_list)
        assert get_list_result["isSuccess"] is True, "Get list operation failed"
        assert "value" in get_list_result, "Response should contain 'value' key"
        assert "items" in get_list_result["value"], "Value should contain 'items' key"
    
    @pytest.mark.storageplugin
    def test_07_verify_whether_we_can_get_the_list_of_multiple_resources_by_giving_multiple_names_C59297258(self):
        """
        C59297258 - Verify whether we can get the list of multiple resources by giving multiple names
        """
        self.storage_plugin.expand_storage_manager_methods("getResourceList")
        assert self.storage_plugin.driver.wait_for_object("get_resource_list_name_textbox", timeout=5, raise_e=False), \
        "Get Resource List name textbox not found - getResourceList method may not have expanded"
        self.storage_plugin.get_list_enter_name("my-resources.txt, device-list.txt")
        self.storage_plugin.click_get_list_test_button()
        get_list = self.storage_plugin.get_list_result()
        get_list_result = json.loads(get_list)
        assert get_list_result["isSuccess"] is True, "Get list operation failed"
        assert "value" in get_list_result, "Response should contain 'value' key"
        assert "items" in get_list_result["value"], "Value should contain 'items' key"

    @pytest.mark.storageplugin
    def test_08_verify_whether_resources_are_getting_retrieved_C59297259(self):
        """
        C59297259 - Verify whether resources are getting retrieved
        """
        self.storage_plugin.expand_storage_manager_methods("getResourceList")
        assert self.storage_plugin.driver.wait_for_object("get_resource_list_name_textbox", timeout=5, raise_e=False), \
        "Get Resource List name textbox not found - getResourceList method may not have expanded"
        self.storage_plugin.get_list_enter_name(" ")
        self.storage_plugin.click_get_list_test_button()
        get_list = self.storage_plugin.get_list_result()
        get_list_result = json.loads(get_list)
        assert get_list_result["isSuccess"] is True, "Get list operation failed"
        assert "value" in get_list_result, "Response should contain 'value' key"
        assert "items" in get_list_result["value"], "Value should contain 'items' key"