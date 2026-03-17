import pytest
import json

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_02_Cdm_Basic(object):

    @pytest.mark.datacollection
    def test_01_filter_valid_cdm_tree_C32335625(self):
        """
        C32335625, C29794251: Filter a valid CDM tree given as a json file
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, enter the valid and select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
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
    def test_02_verify_response_both_cdm_tree_and_tree_gun_are_empty_C32735671(self):
        """
        C32735671: Verify cdm filter tree test result, when both tree and tree gun are blank and then it should display an error message
        - Error: Invalid Options: $Parameter cannot be empty or null.  Parameter name: Tree
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox',  self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                           ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.swipe_to_object("cdm_tree_file_selector")
        self.data_collection_plugin.expand_data_collection_method("filterCDMTrees")
        self.data_collection_plugin.select_simplified_cdm_tree_result_checkbox(True)
        self.data_collection_plugin.select_filter_cdm_tree_test_button()
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text()
        assert 'Error: Invalid Options: $Parameter cannot be empty or null' in result, "Expected error message not found in result: {}".format(result)

    @pytest.mark.datacollection
    def test_03_filter_cdm_tree_invalid_format_C32335626(self):
        """
        C32335626, C29794252: Filter a CDM tree with invalid format, should return invalid tree error
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('invalidcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'InvalidTreeError'
        assert result['reason'] == 'Failed to serialize the tree'

    @pytest.mark.datacollection
    def test_04_data_collection_filter_cdm_tree_invalid_gun_C32335627(self):
        """
        C32335627, C29794253: Filter a CDM tree with an invalid GUN
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, passing cdm GUN as a invalid format and select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - verify the TreeNotAllowed error in the result 
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', 'invalid_gun')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'TreeNotAllowed'
        assert result['reason'] == 'Failed to retrieve filters to the current tree'

    @pytest.mark.datacollection
    def test_05_data_collection_filter_cdm_tree_parameter_missing_desktop_C32335628(self):
        """
        C32335628, C29794254: Filter a valid CDM tree when a required parameter is missing for Desktop asset unit
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, set asset unit as desktop and leave asset type and app instance id as empty
        - select the valid cdm tree file and enter the tree gun
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing that missing parameter is required
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', ''),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'ValveControllerMetadataError'
        assert result['reason'] == 'The Asset Unit of Type desktop Needs an App Instance Id Value'