import pytest
import json
from time import sleep

@pytest.mark.usefixtures("common_class_setup")
class Test_Suite_14_Native_Parameters(object):

    @pytest.mark.datacollection
    def test_01_filter_invalid_cdm_tree_C32335626(self):
        """
        C32335626 - Filter Invalid CDM tree
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(False)
        self.settings.disable_use_batching_policy_toggle(True)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_invalid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        result = self.data_collection_plugin.get_filtered_result()
        assert 'InvalidTreeError' in result
        assert 'Failed to serialize the tree' in result

    @pytest.mark.datacollection
    def test_02_filter_valid_cdm_tree_when_asset_unit_mobile_required_parameter_is_missing_C32335629(self):
        """
        C32335629 - Filter valid CDM tree when required parameter is missing
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("mobile")
        self.settings.clear_text_from_textboxes(['asset_type_textbox', 'app_instance_id_textbox'])
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(True)
        self.settings.disable_use_batching_policy_toggle(True)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_valid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        result = self.data_collection_plugin.get_filtered_result()
        assert 'ValveControllerMetadataError' in result
        assert "AssetUnit is not 'desktop or 'solution'" in result

    @pytest.mark.datacollection
    def test_03_filter_valid_cdm_tree_when_asset_unit_solution_required_parameter_is_missing_C32335630(self):
        """
        C32335630 - Filter valid CDM tree when required parameter is missing
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("solution")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(True)
        self.settings.disable_use_batching_policy_toggle(True)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_valid_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        result = self.data_collection_plugin.get_filtered_result()
        assert 'ValveControllerMetadataError' in result
        assert "When assetUnit is solution, assetType is required" in result

    @pytest.mark.datacollection
    def test_04_filter_cdm_tree_with_invalid_gun_C32335627(self):
        """
        C32335627 - Filter CDM tree with invalid gun
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        textbox_values = [('app_instance_id_textbox', self.us_region_app_instance_id_1), ('device_id_textbox', self.us_region_device_id), ('model_number_textbox', self.model_number)]
        self.settings.send_texts_to_textboxes(textbox_values)
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(True)
        self.settings.disable_use_batching_policy_toggle(True)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_custom_tree_btn()
        with open(self.cdm_text_file) as file:
            self.data_collection_plugin.enter_custom_cdm_tree_object_textbox(file.read())
        self.data_collection_plugin.enter_custom_cdm_tree_gun_textbox("invalid_gun")
        self.data_collection_plugin.select_custom_send_tree_btn()
        self.data_collection_plugin.select_apply_filter_btn()
        result = self.data_collection_plugin.get_filtered_result()
        assert 'TreeNotAllowed' in result
        assert "Failed to retrieve filters to the current tree" in result

    @pytest.mark.datacollection
    def test_05_filter_cdm_tree_with_blank_gun_C32335631(self):
        """
        C32335631 - Filter CDM tree with blank gun
        """
        self.home.select_top_nav_button("settings_nav_btn")
        self.settings.select_asset_unit_item("desktop")
        self.settings.clear_text_from_textboxes(['asset_type_textbox'])
        self.data_collection_plugin.enable_use_custommetdatavalue_toggle(True)
        self.settings.disable_use_batching_policy_toggle(True)
        self.settings.enable_use_custom_batching_policy_toggle(True)
        self.settings.enable_verbose_logs_toggle(True)
        self.settings.click_settings_savebtn()
        self.settings.click_settings_closebtn()
        self.home.select_top_nav_button("filters_nav_btn")
        self.data_collection_plugin.select_combo_tree_list("CDM")
        self.data_collection_plugin.select_custom_tree_btn()
        with open(self.cdm_text_file) as file:
            self.data_collection_plugin.enter_custom_cdm_tree_object_textbox(file.read())
        self.data_collection_plugin.enter_custom_cdm_tree_gun_textbox("")
        self.data_collection_plugin.select_custom_send_tree_btn()
        self.data_collection_plugin.filters_error_pop_up_result() == 'Please provide a tree gun'
        self.data_collection_plugin.select_filtered_pop_up_close_btn()