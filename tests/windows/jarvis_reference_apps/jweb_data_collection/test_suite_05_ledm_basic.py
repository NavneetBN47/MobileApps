import pytest

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_05_Ledm_Basic(object):

    @pytest.mark.datacollection
    def test_01_filter_valid_ledm_tree_C32335635(self):
        """
        C32335635, C29794261: Filter a valid LEDM tree given as a xml file
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, enter the valid and select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - It should return the few tree based on the Filter Bindings inclusion logic
        - verifying the returned tree and resource uri in the UI result with the valid ledm tree which used as input
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), 
                          ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml', '/DevMgmt/ProductConfigDyn.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)[0]
        valid_ledm_tree_details = self.valid_ledm_tree
        ledm_tree_ui_result = result['tree']
        self.data_collection_plugin.verify_valid_ledm_tree_ui_result(ledm_tree_ui_result, valid_ledm_tree_details)
        assert result['resourceUri'] == '/DevMgmt/ProductConfigDyn.xml'

    @pytest.mark.datacollection
    def test_02_filter_invalid_ledm_tree_C32335636(self):
        """
        C32335636, C29794262: Filter a LEDM tree with invalid format, should return invalid tree error
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.us_region_app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), 
                          ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('invalidledm.xml', '/DevMgmt/ProductConfigDyn.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'InvalidTreeError'

    @pytest.mark.datacollection
    def test_03_data_collection_filter_ledm_tree_invalid_uri_C32335637(self):
        """
        C32335637, C29794263: Filter a LEDM tree with an invalid URI
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, passing URI as a invalid format and select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - verify the TreeNotAllowed error in the result 
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml', 'invalid_tree_uri')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'TreeNotAllowed'
        assert result['reason'] == 'Tree has no matching filters'

    @pytest.mark.datacollection
    def test_04_data_collection_filter_ledm_tree_blank_uri_C32335638(self):
        """
        
        C32335638, C29794264: Filter a LEDM tree with a blank URI
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, leaving URI empty and select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - expecting an error message      
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', self.app_instance_id),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml', '')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text()
        assert 'Error: Invalid Options: $Parameter cannot be empty or null' in result

    @pytest.mark.datacollection
    def test_05_data_collection_filter_ledm_tree_parameter_missing_desktop_C32335639(self):
        """
        C32335639, C29794265: Filter a valid LEDM tree when a required parameter (app instance id) is missing for Desktop asset unit
        - using data collection refApp, navigate to data collection plugin
        - inform all the needed parameters, set asset unit as desktop and leave app instance id empty and leave asset type empty
        - select the valid ledm tree file
        - click on test button to apply the filtering using the parameters set and ledm file
        - an error message is displayed pointing that missing parameter is required
        """
        self.data_collection_plugin.select_asset_unit_item("desktop")
        textbox_values = [('asset_type_textbox', ''), ('app_instance_id_textbox', ''),
                          ('stratus_user_id_textbox', self.stratus_user_id), ('device_id_textbox', self.device_id), ('tenant_id_textbox', self.tenant_id)]
        self.data_collection_plugin.send_texts_to_textboxes(textbox_values)
        self.fc.filter_ledm_tree('validledm.xml', '/DevMgmt/ProductConfigDyn.xml')
        result = self.data_collection_plugin.get_filter_ledm_tree_result_text(get_json=True)[0]
        assert result['errorType'] == 'ValveControllerMetadataError'
        assert result['reason'] == 'The Asset Unit of Type desktop Needs an App Instance Id Value'