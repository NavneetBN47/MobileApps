import pytest

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_06_Ledm_Parameters(object):

    @pytest.mark.datacollection
    def test_01_data_collection_filter_ledm_tree_parameter_missing_mobile_C32335640(self):
        """
        C32335640, C29794266: Filter a valid LEDM tree when a required parameter (app instance id) is missing for Mobile asset unit
        """
        self.data_collection_plugin.select_asset_unit_item("mobile")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', ''),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml', '/DevMgmt/ProductConfigDyn.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'ValveControllerMetadataError'
        assert result['reason'] == "AssetUnit is not 'desktop or 'solution'."

    @pytest.mark.datacollection
    def test_02_data_collection_filter_ledm_tree_parameter_missing_solution_C32335641(self):
        """
        C32335641, C29794267: Filter a valid LEDM tree when a required parameter is missing for Solution asset unit (asset type)
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml', '/DevMgmt/ProductConfigDyn.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'ValveControllerMetadataError'
        assert result['reason'] == 'When assetUnit is solution, assetType is required'

    @pytest.mark.datacollection
    def test_03_data_collection_filter_ledm_tree_parameter_missing_solution_C32335641(self):
        """
        C32335641, C29794267: Filter a valid LEDM tree when a required parameter is missing for Solution asset unit (stratus user id)
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', ''), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml', '/DevMgmt/ProductConfigDyn.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'ValveControllerMetadataError'
        assert result['reason'] == 'The Asset Unit of Type solution needs an Asset Type and Stratus User Id Value'

    @pytest.mark.datacollection
    def test_04_data_collection_filter_ledm_tree_parameter_missing_solution_C32335641(self):
        """
        C32335641, C29794267: Filter a valid LEDM tree when a required parameter is missing for Solution asset unit (device id)
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', ''), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml', '/DevMgmt/ProductConfigDyn.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'TreeNotAllowed'
        assert result['reason'] == 'Tree has no matching filters'

    @pytest.mark.datacollection
    def test_05_data_collection_filter_ledm_tree_parameter_missing_solution_C32335641(self):
        """
        C32335641, C29794267: Filter a valid LEDM tree when a required parameter is missing for Solution asset unit (tenant id)
        """
        self.data_collection_plugin.select_asset_unit_item("solution")
        textbox_values = [('asset_type_textbox', self.asset_type), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', '')]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml', '/DevMgmt/ProductConfigDyn.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)[0]
        assert 'errorType' not in result
        assert result['resourceUri'] == '/DevMgmt/ProductConfigDyn.xml'
        assert '<prdcfgdyn2:ProductConfigDyn' in result['tree']

    @pytest.mark.datacollection
    def test_06_filter_multiple_valid_ledm_trees_C32335642(self):
        """
        C32335642, C29794268: Filter multiple valid LEDM trees
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_ledm_trees(["validledm.xml", "second_validledm.xml"])
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)
        for res in result:
            valid_ledm_tree_details = self.valid_ledm_tree
            ledm_tree_ui_result = res['tree']
            self.data_collection_plugin.verify_valid_ledm_tree_ui_result(ledm_tree_ui_result, valid_ledm_tree_details)
            assert res['resourceUri'] == '/DevMgmt/ProductConfigDyn.xml'

    @pytest.mark.datacollection
    def test_07_filter_multiple_ledm_trees_variable_uri_length_C32335643(self):
        """
        C32335643, C29794269: Filter multiple valid LEDM trees with variable uri length
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_ledm_trees(["validledm.xml", "second_validledm.xml"])
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)
        for res in result:
            valid_ledm_tree_details = self.valid_ledm_tree
            ledm_tree_ui_result = res['tree']
            self.data_collection_plugin.verify_valid_ledm_tree_ui_result(ledm_tree_ui_result, valid_ledm_tree_details)
            assert res['resourceUri'] == '/DevMgmt/ProductConfigDyn.xml'

    @pytest.mark.datacollection
    def test_08_filter_multiple_valid_and_invalid_ledm_trees_C32335644(self):
        """
        C32335644, C29794270: Filter valid and invalid LEDM trees, expecting one filtered result, and one invalid tree error
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_multiple_ledm_trees(["validledm.xml", "invalidledm.xml"])
        failed_result, successful_result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)
        if 'errorType' in successful_result:
            failed_result, successful_result = successful_result, failed_result
        assert failed_result['errorType'] == 'InvalidTreeError'
        valid_ledm_tree_details = self.valid_ledm_tree
        ledm_tree_ui_result = successful_result['tree']
        self.data_collection_plugin.verify_valid_ledm_tree_ui_result(ledm_tree_ui_result, valid_ledm_tree_details)
        assert successful_result['resourceUri'] == '/DevMgmt/ProductConfigDyn.xml'