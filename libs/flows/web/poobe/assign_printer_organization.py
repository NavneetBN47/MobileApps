from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare
from selenium.webdriver.common.keys import Keys

class AssignPrinterOrganization(OWSFlow):
    """
        Contains all of the elements and flows associated with Portal OOBE Assign Printer Organization Page (/assign-organization)
        /activate, /connect, /onboard
    """
    file_path = __file__
    flow_name = "assign_printer_organization_page"
    

########################################################################################################################
#                                                  Action Flows                                                        #
########################################################################################################################

    def click_assign_organization_box(self):
        """
        Click organization button on page
        """
        self.driver.click("organization_name_box")

    def select_new_organization_option(self):
        """
        Select New organization Option on assign printer owner page.
        """
        self.driver.click("select_new_organization_radio_button", timeout=15, displayed=False)
    
    def select_already_existing_organization(self, organization):
        """
        Select Already existing organization in Assign organization page.
        """
        tess = self.driver.find_object("organization_name_group_container", multiple=True)
        for i in range(len(tess)):
            if tess[i].text == organization:
                return tess[i].click()
            
    def select_organization_country_region_seclector(self):
        self.driver.click("organization_country_region_selector")

    def select_trinidad_and_tobago_country_region(self):
        self.driver.click("trinidad_tobago_country_selector")

    def select_united_states_country_region(self):
        self.driver.click("united_states_country_selector")

    def select_orgnization_country_region_option_from_the_drop_down(self):
        # Select this to close the drop down without selecting any Country Region.
        self.driver.click("organization_country_region_option_from_the_drop_down")
    
    def click_hp_smart_terms_conditions_url(self):
        """
        click Hp smart terms and condition hyperlink
        """
        self.driver.click("hp_smart_terms_conditions_url")

    def clear_entered_name_from_the_box(self):
        """
        Clear entered name from the box
        """
        self.driver.send_keys("organization_name_box", Keys.BACKSPACE)

    def click_supported_countries_hyperlink(self):
        """
        Click supported countries hyperlink on assign printer owner page.
        """
        self.driver.click("supported_countries_hyperlink_btn")

    def click_printer_is_not_supported_in_selected_region_modal_support_btn(self):
        """
        Click support button on printer is not supported in selected region modal.
        """
        self.driver.click("printer_is_not_supported_in_selected_region_modal_support_btn")

    def click_continue_btn(self):
        """
        Click continue button on assign printer owner page.
        """
        self.driver.click("continue_button_text")

########################################################################################################################
#                                            Verification Flows                                                        #
########################################################################################################################

    @screenshot_compare(root_obj="assign_printer_owner_page")
    def verify_assign_printer_owner_page(self):
        """
        Verify Assign printer owner page
        """
        self.driver.wait_for_object("assign_printer_owner_page", timeout=30)
    
    def verify_assign_printer_owner_header(self):
        return self.driver.wait_for_object("header")
    
    def verify_assign_printer_owner_page_radiogroup(self):
        """
        Verify the radiogroup on assgn printer owner page. radiogroup is host element for radio buttons use to selete organization.
        """
        return self.driver.wait_for_object("assign_printer_owner_radiogroup", raise_e=False, timeout=20)
    
    def verify_organization_input_box_focused(self):
        """
        Verify organization input box is foucused after clicking on organization (Input box is highlighted with blue outline in UI.)
        """
        self.driver.get_attribute("organization_labels_name", "data-focused") == "true"

    def verify_organization_country_region_drop_down(self):
        """
        Verify country region drop down on the page
        """
        self.driver.wait_for_object("organization_country_region_drop_down")
    
    def verify_organization_description_box(self):
        """
        Verify organization description box on the page
        """
        self.driver.wait_for_object("organization_description_box")
    
    def verify_oranganization_option(self):
        """"
        Verify oranganization selection on the page
        """
        self.driver.wait_for_object("assign_organization", timeout=30)

    def verify_personal_printer_option(self):
        """
        Verify personal selection on the page
        """
        self.driver.wait_for_object("personal_printer_btn")

    def verify_oraganization_label(self):
        """
        Verify oranganization label on the page
        """
        self.driver.wait_for_object("organization_labels_name")

    def verify_country_region_drop_down_listbox(self, raise_e=True):
        """
        Verify country region drop down listbox on the page
        """
        return self.driver.wait_for_object("country_region_drop_down_listbox", raise_e=raise_e)
    
    def verify_organization_labels_country_error_text(self, raise_e=True):
        """
        Verify country region error text on the page
        """
        return self.driver.wait_for_object("organization_labels_country_error_text", raise_e=raise_e)
    
    def verify_organization_labels_invalid_name_text(self, raise_e=True):
        return self.driver.wait_for_object("organization_labels_invalid_name_text", raise_e=raise_e)
    
    def verify_supported_countries_modal(self):
        self.driver.wait_for_object("hp+_supported_countries_modal")

    def verify_printer_is_not_supported_in_selected_region_modal(self):
        self.driver.wait_for_object("printer_is_not_supported_in_selected_region_modal")
    
    def verify_hp_smart_terms_conditions_url(self):
        """
        Verify Hp Smart Terms and Conditions hyperurl is present on the page.
        """
        self.driver.wait_for_object("hp_smart_terms_conditions_url")
    
    def verify_existing_organization_page(self, name):
        """
        Verify already existing Assign organnization name on Assign Printer owner page.
        """
        self.driver.wait_for_object("assign_orgnazation_container")
        if name == "yada yada":
            self.driver.process_screenshot(self.file_path, ("{}_assign_organization_container").format(name), root_obj="assign_orgnazation_container")
        if name not in self.driver.wait_for_object("assign_orgnazation_container").text:
            raise ValueError("Company name mismatch")