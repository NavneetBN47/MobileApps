from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare, string_validation
from selenium.common.exceptions import ElementClickInterceptedException


class ValuePropPage(OWSFlow):
    """
        Contains all of the elements and flows associated with Portal OOBE Value Prop Page or Landing Page
        /activate, /connect, /onboard
    """
    file_path = __file__
    flow_name = "portal_value_prop_page"
    
########################################################################################################################
#                                                  Action Flows                                                        #
########################################################################################################################

    def click_landing_page_footer(self):
        """
        Click Landing page footer to scroll down the webpage.
        """
        self.driver.click("landing_page_footer")
    
    def click_landing_page_these_featurs_btn(self):
        try:
            self.driver.click("landing_page_these_featurs_btn", change_check={"wait_obj": "landing_page_cloud_based_features_modal"})
        except ElementClickInterceptedException:
            if self.verify_these_features_modal(raise_e=False) is False: # Sometime selenium executes the click and then throws a exception
                self.driver.click("landing_page_these_featurs_btn")
    
    def click_landing_page_complete_without_features_modal_btn(self):
        self.driver.click("bottom_page_link")
    
    def click_landing_page_sign_in_btn(self):
        self.driver.click("right_section_content[0]_tertiary_button", change_check={"wait_obj": "right_section_content[0]_tertiary_button", "invisible": True})
        if self.driver.check_if_browser_alert_present(raise_e=False) is True: # After Clicking the sign In button on Landing page a browser Alert may show up
            self.driver.accept_or_dismiss_browser_alert(accept=True)

    def click_landing_page_continue_btn(self):
        self.driver.click("landing_page_continue_btn")

    def click_complete_basic_setup_overlay_close_btn(self):
        self.driver.click("complete_without_features_modal_close_button")

    def click_landing_page_cloud_based_features_modal_close_btn(self):
        self.driver.click("these_features_modal_close_button")
    
    def click_setup_printer_for_personal_overlay_install_hp_smart_btn(self):
        self.driver.click("setup_printer_for_personal_overlay_install_hp_smart_btn")

    def click_hp_easy_setup_hyperlink(self):
        self.driver.click("hp_easy_setup_hyperlink")

########################################################################################################################
#                                            Verification Flows                                                        #
########################################################################################################################

    @screenshot_compare(root_obj="value_prop_page", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_value_prop_page(self, raise_e=True):
        return self.driver.wait_for_object("value_prop_page", raise_e=raise_e, timeout=10)

    @screenshot_compare(root_obj="value_prop_page_left_panel", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_value_prop_left_panel(self):
        self.driver.wait_for_object("value_prop_page_left_panel")

    @screenshot_compare(root_obj="value_prop_page_right_panel", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_value_prop_right_panel(self):
        self.driver.wait_for_object("value_prop_page_right_panel")

    @string_validation("header")
    def verify_landing_page_header(self, raise_e=False): 
        return self.driver.wait_for_object("header")

    @string_validation("subheader")
    def verify_landing_page_subheader(self, raise_e=False):
        return self.driver.wait_for_object("subheader")

    @screenshot_compare(root_obj="landing_page_cloud_based_features_modal", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_these_features_modal(self, raise_e=True):
        return self.driver.wait_for_object("landing_page_cloud_based_features_modal", raise_e=raise_e)
    
    @string_validation("these_features_modal_header")
    def verify_cloud_based_feature_header(self, raise_e=False):
        return self.driver.wait_for_object("these_features_modal_header")

    @string_validation("these_features_modal_description")
    def verify_landing_page_cloud_based_features_description(self, raise_e=False):
        return self.driver.wait_for_object("these_features_modal_description", raise_e=raise_e)

    @screenshot_compare(root_obj="bottom_page_link", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_landing_page_complete_without_features_modal_btn(self, raise_e=True):
        return self.driver.wait_for_object("bottom_page_link", raise_e=raise_e)
    
    @screenshot_compare(root_obj="landing_page_steps", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_landing_page_steps(self):
        self.driver.wait_for_object("landing_page_steps")

    @screenshot_compare(root_obj="complete_basic_setup_overlay", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_complete_basic_setup_overlay(self):
        self.driver.wait_for_object("complete_basic_setup_overlay")

    @screenshot_compare(root_obj="complete_basic_setup_content", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_complete_basic_setup_content(self):
        self.driver.wait_for_object("complete_basic_setup_content")

    @screenshot_compare(root_obj="setup_printer_for_personal_overlay_install_hp_smart_btn", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_setup_printer_for_personal_overlay_install_hp_smart_btn(self):
        self.driver.wait_for_object("setup_printer_for_personal_overlay_install_hp_smart_btn")
    
    @string_validation("right_section_content[0]_header")
    def verify_get_started_header_sub_header(self, raise_e=False):
        return self.driver.wait_for_object("right_section_content[0]_header")

    @string_validation("right_section_content[0]_block_text")
    def verify_startscan_get_started_sub_header(self, raise_e=False):
        self.driver.wait_for_object("right_section_content[0]_block_text")
    
    def verify_value_prop_page_logged_in_right_section(self):
        self.driver.wait_for_object("right_section_content[1]_block_text")
    
    @string_validation("right_section_content[0]_primary_button")
    def verify_landing_page_create_account_btn(self, raise_e=False):
        return self.driver.wait_for_object("right_section_content[0]_primary_button")

    @screenshot_compare(root_obj="landing_page_continue_btn", include_param=["--printer-profile", "--printer-biz-model", "--locale"])
    def verify_landing_page_continue_btn(self):
        self.driver.wait_for_object("landing_page_continue_btn")

    @string_validation("right_section_content[0]_tertiary_button")
    def verify_landing_page_sign_in_btn(self, raise_e=False):
        self.driver.wait_for_object("right_section_content[0]_tertiary_button")

    @string_validation("stepper_steps[1]_text")
    def verify_stepper_step_0(self, raise_e=False):
        return self.driver.wait_for_object("stepper_steps[1]_text")

    @string_validation("stepper_steps[1]_text")
    def verify_stepper_step_1(self, raise_e=False):
        return self.driver.wait_for_object("stepper_steps[1]_text")

    @string_validation("stepper_steps[2]_text")
    def verify_stepper_step_2(self, raise_e=False):
        return self.driver.wait_for_object("stepper_steps[2]_text")

    @string_validation("stepper_steps[3]_text")
    def verify_stepper_step_3(self, raise_e=False):
        return self.driver.wait_for_object("stepper_steps[3]_text")