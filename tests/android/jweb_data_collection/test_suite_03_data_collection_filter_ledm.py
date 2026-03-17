import json
import pytest
from time import sleep
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "JWEB_DATA_COLLECTION"

class Test_Suite_01_Data_Collection(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_jweb_data_collection_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_data_collection_setup
        cls.home = cls.fc.fd["home"]
        cls.data_valve = cls.fc.fd["data_valve"]
        cls.data_collection_settings = cls.fc.fd["data_collection_settings"]
        cls.data_collection_service = cls.fc.fd["data_collection_service"]
        cls.data_collection_plugin = cls.fc.fd["data_collection_plugin"]
        cls.local_files = cls.fc.fd["local_files"]
        cls.stack = request.config.getoption("--stack")

        cls.data_collection_test_data = cls.fc.get_data_collection_test_data(request.config.getoption("--stack"))
        cls.app_instance_id = cls.data_collection_test_data["app_instance_id"]
        cls.asset_type = cls.data_collection_test_data["asset_type"]
        cls.device_id = cls.data_collection_test_data["device_id"]
        cls.stratus_user_id = cls.data_collection_test_data["stratus_user_id"]
        cls.us_region_app_instance_id_1 = cls.data_collection_test_data["us_region_app_instance_id_1"]
        cls.us_region_device_id = cls.data_collection_test_data["us_region_device_id"]

        with open(ma_misc.get_abs_path("resources/test_data/jweb/validcdmtree.json")) as cdm_tree:
            cls.valid_cdm_tree = json.loads(cdm_tree.read())

    @pytest.fixture(scope="function", autouse="true")
    def data_collection_home_setup(self):
        self.fc.flow_load_home_screen()
        self.fc.select_stack(self.stack)

    @pytest.fixture(scope="class", autouse="true")
    def load_necessary_files(self):
        """
        Send files to Android Device, and delete file once tests are complete
        """
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/invalidledm.xml"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "invalidledm.xml"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/validledm.xml"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "validledm.xml"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/validledm.xml"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "second_validledm.xml"), overwrite=True)
        yield None
        self.driver.clean_up_device_folder(TEST_DATA.MOBILE_DOWNLOAD)

    def test_01_filter_valid_ledm_trees(self):
        """
        C29794261: Filter a valid LEDM tree
        - navigating to webView tab > data collection plugin, inform all the needed parameters
        - select the valid LEDM tree file
        - click on test button to apply the filtering using the parameters set and LEDM file
        - expecting a filtered tree in the result
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id),  
                          ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()[0]
        assert result['resourceUri'] == '/DevMgmt/ProductConfigDyn.xml'
        assert len(result['tree']) >= 1

    def test_02_filter_invalid_ledm_trees(self):
        """
        C29794262: Filter a LEDM tree with invalid format
        - select the valid LEDM tree file
        - click on test button to apply the filtering using the parameters set and LEDM file
        - expecting a InvalidTreeError as a result
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item('solution')
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id), 
                           ('stratus_user_id_textbox', self.stratus_user_id), 
                          ('device_id_textbox', self.device_id), ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('invalidledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()[0]
        assert result['errorType'] == 'InvalidTreeError'

    def test_03_filter_multiple_valid_ledm_trees(self):
        """
        C29794268: Filter multiple valid LEDM trees
        - navigating to webView tab > data collection plugin, inform all the needed parameters (two resource_uris to match the two LEDM trees)
        - select the both valid LEDM tree files
        - click on test button to apply the filtering using the parameters set and LEDM file
        - expecting two filtered tree in the result
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1),  
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id),  
                          ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml,/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_ledm_trees(['second_validledm.xml', 'validledm.xml'])
        result_1, result_2 = self.data_collection_plugin.get_filter_ledm_tree_result_text()
        assert result_1['resourceUri'] == '/DevMgmt/ProductConfigDyn.xml'
        assert result_2['resourceUri'] == '/DevMgmt/ProductConfigDyn.xml'
        assert len(result_1['tree']) >= 1
        assert len(result_2['tree']) >= 1

    def test_04_filter_multiple_ledm_trees_variable_uri_length(self):
        """
        C29794269: Filter LEDM trees by passing a number of trees different than the number of URIs
        - navigating to webView tab > data collection plugin, inform all the needed parameters (one resource_uris for the LEDM trees)
        - select the both valid LEDM tree files
        - click on test button to apply the filtering using the parameters set and LEDM file
        - expecting number or Resource URIs does not match number of trees in the result
        - then inform two resource_uris for one tree
        - select the one valid LEDM tree files
        - click on test button to apply the filtering using the parameters set and LEDM file
        - expecting number or Resource URIs does not match number of trees in the result
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), 
                          ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_ledm_trees(['second_validledm.xml', 'validledm.xml'])
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=False).split('\n')
        assert result[0] == 'The number of Resource URIs does not match the number of trees'
        assert result[2] == 'Resource URIs: 1'
        self.data_collection_plugin.send_text_to_textbox('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml,/DevMgmt/ProductConfigDyn.xml')
        self.fc.filter_ledm_tree('validledm.xml')
        sleep(4)
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=False).split('\n')
        assert result[0] == 'The number of Resource URIs does not match the number of trees'
        assert result[2] == 'Resource URIs: 2'

    def test_05_filter_multiple_valid_and_invalid_ledm_trees(self):
        """
        C29794270: Filter multiple valid and invalid LEDM trees at once 
        - navigating to webView tab > data collection plugin, inform all the needed parameters (two resource_uris for the two LEDM trees)
        - select the both valid and invalid LEDM tree files
        - click on test button to apply the filtering using the parameters set and LEDM file
        - expecting one filtered LEDM tree and one invalidTreeError
        """
        self.fc.flow_load_home_screen()
        self.home.select_webview_tab()
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id),  
                          ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml,/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_ledm_trees(['invalidledm.xml', 'validledm.xml'])
        failed_result, successful_result = self.data_collection_plugin.get_filter_ledm_tree_result_text()
        if 'errorType' in successful_result: failed_result, successful_result = successful_result, failed_result
        failed_result['errorType'] == 'invalidTreeError'
        assert successful_result['resourceUri'] == '/DevMgmt/ProductConfigDyn.xml'
        assert len(successful_result['tree']) >= 1

    def test_06_data_collection_ledm_tree_verify_invalid_uri(self):
        """
        C29794263: Filter a LEDM tree with an invalid URI
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, passing URI as a invalid format and select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - expected TreeNotAllowed error under Result field
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('resource_uri_textbox', 'invalid_tree_uri')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()[0]
        assert result['errorType'] == "TreeNotAllowed"

    def test_07_data_collection_ledm_tree_verify_blank_uri(self):
        """
        C29794264: Filter a LEDM tree with a blank URI
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, leaving URI empty and select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - an error message is displayed pointing the resourceUri passed as missing or invalid
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('resource_uri_textbox', '')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(False)
        assert result == "Error: Required parameter 'resourceUri' is missing on the object with index 0."

    def test_08_data_collection_filter_ledm_tree_parameter_missing_desktop(self):
        """
        C29794265: Filter a valid LEDM tree when a required parameter is missing for Desktop asset unit (app instance id)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as desktop and leave app instance id empty
        - select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - an error message is displayed pointing that missing parameter is required
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', 'hpSmart'), ('app_instance_id_textbox', ''), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()[0]
        assert result['reason'] == "appInstanceId is required when assetUnit is mobile or desktop"

    def test_09_data_collection_filter_ledm_tree_parameter_missing_mobile(self):
        """
        C29794266: Filter a valid LEDM tree when a required parameter is missing for Mobile asset unit (app instance id)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as mobile and leave asset type empty
        - select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing that missing parameter is required
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', ''), ('asset_type_textbox', ''),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()[0]
        assert result['reason'] == "appInstanceId is required when assetUnit is mobile or desktop"

    def test_10_1_data_collection_filter_ledm_tree_parameter_missing_solution(self):
        """
        C29794267: Filter a valid LEDM tree when a required parameter is missing for Solution asset unit (asset type)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave asset type empty
        - select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - an error message is displayed pointing that assetType should be provided
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()[0]
        assert result['reason'] == "Both assetType and stratusUserId are required when assetUnit is 'solution"

    def test_10_2_data_collection_filter_ledm_tree_parameter_missing_solution(self):
        """
        C29794267: Filter a valid ledm tree with a required parameter for solution missing (stratus user id textbox)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave stratus user id textbox empty
        - select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - an error message is displayed pointing that missing parameter is required
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', 'instantInk'), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', ''), ('device_id_textbox', self.device_id), ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()[0]
        assert result['reason'] == "Both assetType and stratusUserId are required when assetUnit is 'solution"

    def test_10_3_data_collection_filter_ledm_tree_parameter_missing_solution(self):
        """
        C29794267: Filter a valid LEDM tree when a required parameter is missing for Solution asset unit (stratus user id)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave stratus user id empty
        - select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - expecting a filtered tree in the result
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', 'instantInk'), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', ''), ('device_id_textbox', self.device_id), ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()[0]
        assert result['errorType'] == 'ValveControllerMetadataError'
        assert result['reason'] == "Both assetType and stratusUserId are required when assetUnit is 'solution" 

    def test_10_4_data_collection_filter_ledm_tree_parameter_missing_solution(self):
        """
        C29794267: Filter a valid LEDM tree when a required parameter is missing for Solution asset unit (account login id)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave account login id empty
        - select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - expecting a filtered tree in the result
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', 'instantInk'), ('app_instance_id_textbox', self.app_instance_id),
             ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()[0]
        assert result['resourceUri'] == '/DevMgmt/ProductConfigDyn.xml'
        assert len(result['tree']) >= 1

    def test_10_5_data_collection_filter_ledm_tree_parameter_missing_solution(self):
        """
        C29794267: Filter a valid LEDM tree when a required parameter is missing for Solution asset unit (neither account login id and stratus user id empty)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave account login id and stratus user id empty
        - select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - an error message is displayed pointing that missing parameter is required
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', 'instantInk'), ('app_instance_id_textbox', self.app_instance_id), 
              ('stratus_user_id_textbox', ''), ('device_id_textbox', self.device_id), ('resource_uri_textbox', '/DevMgmt/ProductConfigDyn.xml')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()[0]
        assert result['reason'] == "Both assetType and stratusUserId are required when assetUnit is 'solution"