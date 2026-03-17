import pytest
from MobileApps.libs.ma_misc import ma_misc
import logging
pytest.app_info = "POOBE"

class Test_01_Portal_OOBE_Localization(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, poobe_test_setup, request):
        self = self.__class__
        self.driver, self.p_oobe, self.fc, self.printer_profile, self.biz_model, self.hpid = poobe_test_setup
        self.locale = request.config.getoption("--locale").split("_")
        self.locale = ''.join(self.locale[1]+"-"+self.locale[0].upper())
        if self.biz_model == "E2E":
            self.key = self.biz_model+"_activate"
        if self.biz_model == "Flex":
            self.key = self.biz_model+"_connect"
        self.file_key = ma_misc.load_json_file("resources/test_data/poobe/spec_key.json")
        
    def test_01_landing_value_prop_page(self):
        file_name = ma_misc.web_localization_path_builder(self.driver, self.file_key["portal_oobe"]["value_prop_page"][self.key])
        file_name = file_name.replace("bg-BG", self.locale)
        spec_data = self.fc.fd["value_prop_page"].get_key_modified_dictionary_from_spec(file_name)
        self.fc.fd["hpid"].handle_privacy_popup()
        self.fc.fd["value_prop_page"].verify_value_prop_page()
        self.fc.fd["value_prop_page"].verify_value_prop_left_panel()
        self.fc.fd["value_prop_page"].verify_value_prop_right_panel()
        self.fc.fd["value_prop_page"].verify_landing_page_header()
        self.fc.fd["value_prop_page"].verify_landing_page_subheader()
        res = []
        web_objs = ["header", "subheader"]
        for i in web_objs:
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, i, raise_e=False))
        if self.biz_model == "Flex":
            web_objs = ["stepper_steps[0]_text", "stepper_steps[1]_text", "stepper_steps[2]_text", 
                        "stepper_steps[3]_text", "stepper_steps[4]_text"]
            for i in web_objs:
                res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, i,raise_e=False))
        else:
            web_objs = ["steps[0]_text", "steps[1]_text", "steps[2]_text", "steps[3]_text","steps[4]_text"]
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, i,raise_e=False))  
        
        self.fc.fd["value_prop_page"].click_landing_page_these_featurs_btn()
        self.fc.fd["value_prop_page"].verify_landing_page_cloud_based_features_description()
        res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "these_features_modal_header",raise_e=False))
        res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "these_features_modal_description",raise_e=False))
        res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "these_features_modal_features[0]_text",raise_e=False))
        if self.biz_model == "Flex":
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "these_features_modal_features[1]_rich_text",raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "these_features_modal_observations",raise_e=False))
        else:
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "these_features_modal_features[1]_text", raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "these_features_modal_features[3]_text",raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "these_features_modal_asterisk_observation", raise_e=False))
        res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "these_features_modal_features[2]_text",raise_e=False))
        res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "these_features_modal_close_button",raise_e=False))
        self.fc.fd["value_prop_page"].click_landing_page_cloud_based_features_modal_close_btn()
        if self.biz_model == "Flex":
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "bottom_page_link",raise_e=False))
            self.fc.fd["value_prop_page"].click_landing_page_complete_without_features_modal_btn()
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "complete_without_features_modal_header",raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "complete_without_features_modal_content",raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "complete_without_features_modal_close_button",raise_e=False))
            self.fc.fd["value_prop_page"].click_complete_basic_setup_overlay_close_btn()
        self.fc.fd["value_prop_page"].verify_landing_page_steps()
        self.fc.fd["value_prop_page"].verify_landing_page_create_account_btn()
        self.fc.fd["value_prop_page"].verify_landing_page_sign_in_btn()
        if self.biz_model == "Flex":
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "right_section_content[0]_header",raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "right_section_content[0]_block_text",raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "right_section_content[0]_primary_button",raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "right_section_content[0]_tertiary_button",raise_e=False))
        else:
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "login_flow_get_started",raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "login_flow_get_started_content_text",raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "login_flow_create_account_button",raise_e=False))
            res.append(self.fc.fd["value_prop_page"].string_validation(spec_data, "login_flow_sign_in_button",raise_e=False))
        logging.info("Current URL: {}".format(self.driver.get_current_url()))
        assert False not in res, "one or multiple string validation failed Check test log for details"