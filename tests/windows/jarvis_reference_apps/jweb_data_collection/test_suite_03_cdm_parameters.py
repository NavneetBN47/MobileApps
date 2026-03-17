import pytest
import json

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_03_Cdm_Parameters(object):

    @pytest.mark.datacollection
    def test_01_data_collection_filter_cdm_tree_parameter_missing_mobile_C32335629(self):
        """
        C32335629, C29794255: Filter a valid CDM tree when a required parameter is missing for Mobile asset unit
        - using data collection refApp, navigate to  data collection plugin
        - inform all the needed parameters, set asset unit as mobile and leave asset type and app instance id as empty
        - select the valid cdm tree file and enter the tree gun
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing the reason
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', ''),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'ValveControllerMetadataError'
        assert result['reason'] == "AssetUnit is not 'desktop or 'solution'."

    @pytest.mark.datacollection
    def test_02_data_collection_filter_cdm_tree_parameter_missing_solution_C32335630(self):
        """
        C32335630, C29794256: Filter a valid CDM tree when asset type parameter is missing for Solution asset unit (without asset type)
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, set asset unit as solution and don't pass the asset type parameter
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing asset type should be provided in case of asset unit is solution
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'ValveControllerMetadataError'
        assert result['reason'] == "When assetUnit is solution, assetType is required"

    @pytest.mark.datacollection
    def test_03_data_collection_filter_cdm_tree_parameter_missing_solution_C32335630(self):
        """
        C32335630, C29794256: Filter a valid cdm tree with a required parameter for solution missing (neither account login id and stratus user id)
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave account login id and stratus user id empty
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - an error message is displayed pointing that missing parameter is required
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', ''), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'ValveControllerMetadataError'

    @pytest.mark.datacollection
    def test_04_data_collection_filter_cdm_tree_parameter_missing_solution_C32335630(self):
        """
        C32335630, C29794256: Filter a valid cdm tree with a required parameter for solution missing (stratus user id)
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave stratus user id empty
        - select the valid cdm tree file
        - click on test button to apply the filtering using the parameters set and cdm file
        - CDM tress are displayed
        - It should return the few tree[events] based on the Filter Bindings inclusion logic
        - verifying the returned tree[events] and tree gun in the UI result with the valid cdm tree events which used as input
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', ''), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_cdm_tree('validcdmtree.json', 'com.hp.cdm.service.eventing.version.1.resource.notification')
        result = self.data_collection_plugin.get_filter_cdm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'ValveControllerMetadataError'

    @pytest.mark.datacollection
    def test_05_data_collection_filter_cdm_tree_parameter_missing_solution_C32335630(self):
        """
        C32335630, C29794256: Filter a valid cdm tree with a required parameter for solution missing (account login id)
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, set asset unit as solution and leave account login id empty
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