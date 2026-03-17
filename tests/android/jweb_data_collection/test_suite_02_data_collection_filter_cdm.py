import json
import pytest
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc
from time import sleep

pytest.app_info = "JWEB_DATA_COLLECTION"

class Test_Suite_02_Filter_CDM(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_jweb_data_collection_setup):
        cls = cls.__class__
        cls.stack = request.config.getoption("--stack")
        cls.driver, cls.fc = android_jweb_data_collection_setup
        cls.home = cls.fc.fd["home"]
        cls.data_valve = cls.fc.fd["data_valve"]
        cls.data_collection_settings = cls.fc.fd["data_collection_settings"]
        cls.data_collection_service = cls.fc.fd["data_collection_service"]
        cls.data_collection_plugin = cls.fc.fd["data_collection_plugin"]
        cls.local_files = cls.fc.fd["local_files"]

        cls.data_collection_test_data = cls.fc.get_data_collection_test_data(cls.stack)
        cls.app_instance_id = cls.data_collection_test_data["app_instance_id"]
        cls.asset_type = cls.data_collection_test_data["asset_type"]
        cls.device_id = cls.data_collection_test_data["device_id"]
        cls.stratus_user_id = cls.data_collection_test_data["stratus_user_id"]
        cls.tenant_id = cls.data_collection_test_data["tenant_id"]
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
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/validcdmtree.json"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "validcdmtree.json"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/validcdmtree.json"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "second_validcdmtree.json"), overwrite=True)
        sleep(2)
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/jweb/invalidcdmtree.json"),
                              "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "invalidcdmtree.json"), overwrite=True)
        yield None
        self.driver.clean_up_device_folder(TEST_DATA.MOBILE_DOWNLOAD)

    def test_01_filter_valid_cdm_tree(self):
        """
        C29794251: Filter valid CDM tree
        - navigating to webView tab > data collection plugin, inform all the needed parameters
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - expecting a filtered tree in the result
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1), 
            ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert 'tree' in result, "failed to get tree from result, result: {}".format(result)
        tree = json.loads(result['tree'])
        assert tree['events'] == self.valid_cdm_tree['events']
        assert result['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'

    def test_02_filter_cdm_tree_invalid_format(self):
        """
        C29794252: Filter a CDM tree with invalid format
        - navigating to webView tab > data collection plugin, inform all the needed parameters
        - select invalid cdm tree file
        - click on test button to apply the filtering using the parameters set and invalid cdm file
        - expecting Failed to serialize the tree error
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
            ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('invalidcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert result['errorType'].lower() == 'invalidtreeerror'
        assert result['reason'] == 'Failed to serialize the tree'

    def test_03_filter_multiple_cdm_trees(self):
        """
        C29794258: Filter multiple valid CDM trees
        - navigating to webView tab > data collection plugin, inform all the needed parameters (including two cdm guns for the two cdm trees)
        - select both valid cdm tree files
        - click on test button to apply the filtering using the parameters set
        - expecting two filtered CDM trees as a result
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_cdm_trees(['validcdmtree.json', 'second_validcdmtree.json'])
        sleep(4)
        result_1, result_2 = self.data_collection_plugin.get_filter_cdm_tree_result_text()
        assert 'tree' in result_1, "failed to get tree from result_1, result_1: {}".format(result_1)
        assert 'tree' in result_2, "failed to get tree from result_2, result_2: {}".format(result_2)
        tree_1, tree_2 = json.loads(result_1['tree']), json.loads(result_2['tree'])
        assert tree_1['events'] == self.valid_cdm_tree['events']
        assert tree_2['events'] == self.valid_cdm_tree['events']
        assert result_1['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'
        assert result_2['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'

    def test_04_filter_multiple_cdm_trees_variable_gun_length(self):
        """
        C29794259: Filter CDM trees by passing a number of trees different than the number of Guns
        - navigating to webView tab > data collection plugin, inform all the needed parameters (only one gun for the two CDM trees)
        - Afterwords try filter one CDM trees with too many tree guns, expecting gun does not match error
        """
        self.data_collection_plugin.select_asset_unit_item('solution')
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id), 
                           ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_cdm_trees(['validcdmtree.json', 'second_validcdmtree.json'], tree="com.hp.cdm.service.eventing.version.1.resource.notification")
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=False).split('\n')
        assert result[0] == 'The number of Tree Guns does not match the number of trees'
        assert result[2] == 'Tree guns: 1'
        self.fc.filter_cdm_tree('validcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification, com.hp.cdm.service.eventing.version.1.resource.notification')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=False).split('\n')
        assert result[0] == 'The number of Tree Guns does not match the number of trees'
        assert result[2] == 'Tree guns: 2'

    def test_05_filter_valid_and_invalid_cdm_trees(self):
        """
        C29794260: Filter valid and invalid CDM trees, expecting one filtered result, and one invalid format error
        - navigating to webView tab > data collection plugin, inform all the needed parameters (including two cdm guns for the two cdm trees)
        - select both valid and invalid cdm tree files
        - click on test button to apply the filtering using the parameters set
        - expecting one tree to be filtered and one tree to return invalidTreeError
        """
        self.data_collection_plugin.select_asset_unit_item('mobile')
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_cdm_trees(['invalidcdmtree.json', 'validcdmtree.json'])
        failed_result, successful_result = self.data_collection_plugin.get_filter_cdm_tree_result_text()
        if 'errorType' in successful_result: failed_result, successful_result = successful_result, failed_result
        failed_result['reason'] == 'Failed to serialize the tree'
        failed_result['errorType'] == 'invalidTreeError'
        failed_result['exception'] == 'The data couldn’t be read because it isn’t in the correct format.'
        successful_tree = json.loads(successful_result['tree'])
        assert successful_tree['events'] == self.valid_cdm_tree['events']
        assert successful_result['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'

    def test_06_data_collection_filter_cdm_tree_parameter_missing_desktop(self):
        """
        C29794254: Filter a valid CDM tree when a required parameter is missing for Desktop asset unit
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as desktop and leave asset type empty
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing that assetUnit is differing of selected platform
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert result['reason'] == "assetUnit does not match with intrinsic platform"

    def test_07_data_collection_filter_cdm_tree_with_invalid_gun(self):
        """
        C29794253: Filter a CDM tree with an invalid GUN
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, passing cdm GUN as a invalid format and select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - expected TreeNotAllowed error under Result field
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', tree="invalid_tree_gun")
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert result['errorType'] == "TreeNotAllowed"
        assert result['reason'] == "Failed to retrieve filters to the current tree"

    def test_07_1_data_collection_filter_cdm_tree_parameter_missing_solution(self):
        """
        C29794256: Filter a valid CDM tree when asset type parameter is missing for Solution asset unit (asset type empty)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave asset type empty
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing asset type as a required data
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert result['reason'] == "Both assetType and stratusUserId are required when assetUnit is 'solution"

    def test_07_2_data_collection_filter_cdm_tree_parameter_missing_solution(self):
        """
        C29794256: Filter a valid cdm tree with a required parameter for solution missing (neither account logging id nor stratus user id)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave both account logging and stratus user id empty
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing account login id and stratus user id as a required data
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', ''), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json')
        sleep(5)
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert result['reason'] == "Both assetType and stratusUserId are required when assetUnit is 'solution"

    def test_07_3_data_collection_filter_cdm_tree_parameter_missing_solution(self):
        """
        C29794256: Filter a valid cdm tree with a required parameter for solution missing (account login id)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave account login id empty
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - CDM tress are displayed
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert 'tree' in result, "failed to get tree from result, result: {}".format(result)
        tree = json.loads(result['tree'])
        assert tree['events'] == self.valid_cdm_tree['events']
        assert result['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'

    def test_07_4_data_collection_filter_cdm_tree_parameter_missing_solution(self):
        """
        C29794256: Filter a valid cdm tree with all required parameter for solution
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - CDM tress are displayed
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert 'tree' in result, "failed to get tree from result, result: {}".format(result)
        tree = json.loads(result['tree'])
        assert tree['events'] == self.valid_cdm_tree['events']
        assert result['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'

    def test_07_5_data_collection_filter_cdm_tree_parameter_missing_solution(self):
        """
        C29794256: Filter a valid cdm tree with a required parameter for solution missing (no asset type)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution without passing the asset type parameter
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing account login id and stratus user id as a required data
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json')
        sleep(5)
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert result['reason'] == "Both assetType and stratusUserId are required when assetUnit is 'solution"

    def test_07_6_data_collection_filter_cdm_tree_parameter_missing_solution(self):
        """
        C29794256: Filter a valid cdm tree with a required parameter for solution missing (stratus user id)
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave stratus user id empty
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - CDM tress are displayed
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.us_region_app_instance_id_1), 
                          ('stratus_user_id_textbox', ''), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json')
        sleep(5)
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert result['reason'] == "Both assetType and stratusUserId are required when assetUnit is 'solution"

    def test_08_data_collection_filter_cdm_tree_parameter_missing_mobile(self):
        """
        C29794255: Filter a valid CDM tree when a required parameter is missing for Mobile asset unit
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, set asset unit as mobile and leave asset type empty
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - CDM tress are displayed
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id_1), 
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.us_region_device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()[0]
        assert 'tree' in result, "failed to get tree from result, result: {}".format(result)
        tree = json.loads(result['tree'])
        assert tree['events'] == self.valid_cdm_tree['events']
        assert result['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'

    def test_09_data_collection_cdm_tree_verify_blank_gun(self):
        """
        C29794257: Filter a CDM tree with a blank GUN
        - using data collection refApp, navigate to webView tab > data collection plugin
        - inform all the needed parameters, leaving CDM GUN empty and select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing the cdm gun passed as missing or invalid
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', tree='')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(False)
        assert result == "Error: Required parameter 'treeGun' is missing on the object with index 0."