import pytest
import json
from time import sleep
@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_04_Cdm_Advanced(object):

    @pytest.mark.datacollection
    def test_01_data_collection_filter_cdm_tree_parameter_missing_solution_C32335630(self):
        """
        C32335630, C29794256: Filter a valid cdm tree with all required parameter for solution
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, set asset unit as solution
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - CDM tress are displayed
        - It should return the few tree[events] based on the Filter Bindings inclusion logic
        - verifying the returned tree[events] and tree gun in the UI result with the valid cdm tree events which used as input
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=True)[0]
        assert 'tree' in result, "failed to get tree from result, result: {}".format(result)
        tree = json.loads(result['tree'])
        valid_cdm_tree_events = self.valid_cdm_tree['events']
        result_ui_event_details = tree['events']
        self.data_collection_plugin.verify_valid_cdm_tree_ui_result(result_ui_event_details, valid_cdm_tree_events)
        assert result['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'

    @pytest.mark.datacollection
    def test_02_data_collection_filter_cdm_tree_blank_gun_C32335631(self):
        """
        C32335631, C29794256: Filter a CDM tree with a blank GUN
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, leaving CDM GUN empty and select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing the cdm gun passed as missing or invalid
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', '')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()
        assert 'Error: Invalid Options: $Parameter cannot be empty or null' in result

    @pytest.mark.datacollection
    def test_03_filter_multiple_cdm_trees_C32335632(self):
        """
        C32335632, C29794258: Filter multiple valid CDM trees, expecting two trees to be filtered
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, set asset unit as solution
        - select the multiple valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - CDM tress are displayed
        - It should return the multiple json file tree[events] based on the Filter Bindings inclusion logic
        - verifying the each file returned tree[events] and tree gun in the UI result with the valid cdm tree events which used as input
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_cdm_trees(["validcdmtree.json", "second_validcdmtree.json"])
        result_1, result_2 = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=True)
        assert 'tree' in result_1, "failed to get tree from result_1, result_1: {}".format(result_1)
        assert 'tree' in result_2, "failed to get tree from result_2, result_2: {}".format(result_2)
        tree_1, tree_2 = json.loads(result_1['tree']), json.loads(result_2['tree'])
        valid_cdm_tree_events = self.valid_cdm_tree['events']
        result_ui_event_details = tree_1['events']
        result_2_ui_event_details = tree_2['events']
        self.data_collection_plugin.verify_valid_multiple_cdm_trees_ui_result(result_ui_event_details, result_2_ui_event_details, valid_cdm_tree_events)
        assert result_1['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'
        assert result_2['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'

    @pytest.mark.datacollection
    def test_04_filter_multiple_cdm_trees_variable_gun_length_C32335633(self):
        """
        C32335633, C29794259: Try filter multiple valid CDM trees with too few tree guns, expecting gun does not match error
        Then try filter one CDM trees with too many tree guns, expecting gun does not match error
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_cdm_trees(["validcdmtree.json", "second_validcdmtree.json"], tree="com.hp.cdm.service.eventing.version.1.resource.notification")
        result1 = self.data_collection_plugin.get_filter_cdm_tree_result_text() 
        assert 'The number of Tree Guns does not match the number of trees' in result1
        self.fc.filter_cdm_tree('validcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification,com.hp.cdm.service.eventing.version.1.resource.notification')
        result2 = self.data_collection_plugin.get_filter_cdm_tree_result_text()
        assert 'The number of Tree Guns does not match the number of trees' in result2

    @pytest.mark.datacollection
    def test_05_filter_valid_and_invalid_cdm_trees_C32335634(self):
        """
        C32335634, C29794260: Filter valid and invalid CDM trees, expecting one filtered result, and one invalid format error
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_cdm_trees(["validcdmtree.json", "invalidcdmtree.json"])
        failed_result, successful_result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=True)
        if 'errorType' in successful_result:
            failed_result, successful_result = successful_result, failed_result
        assert failed_result['errorType'] == 'InvalidTreeError'
        assert failed_result['reason'] == 'Failed to serialize the tree'
        successful_tree = json.loads(successful_result['tree'])
        valid_cdm_tree_events = self.valid_cdm_tree['events']
        result_ui_event_details = successful_tree['events']
        self.data_collection_plugin.verify_valid_cdm_tree_ui_result(result_ui_event_details, valid_cdm_tree_events)
        assert successful_result['treeGun'] == 'com.hp.cdm.service.eventing.version.1.resource.notification'