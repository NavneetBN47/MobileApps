from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare
from selenium.webdriver.common.keys import Keys


class HpPlusOfferAndBenefits(OWSFlow):
    """
        Contains all of the elements and flows associated with Portal OOBE Hp+ Requirments and Benefits Page as of 10/11/2023 only for /onboard flow users is show this offer to accept or decline hp+ offer just before printer activation page
    """
    file_path = __file__
    flow_name = "hp_plus_offer_and_benefits"
    

########################################################################################################################
#                                                  Action Flows                                                        #
########################################################################################################################

    def click_decline_hp_plus(self):
        """
        Click decline hp plus on HP plus printer smart requirments page.
        """
        self.driver.click("decline_hp_plus")

    def click_continue_btn(self):
        """
        Click Continue btn on Hp Plus smart printer benefits page.
        """
        self.driver.click("hp_plus_continue_btn")
    
    def click_learn_more_btn(self):
        self.driver.click("learn_more_btn")
    
    def click_hp_plus_overview_card(self):
        self.driver.click("hp_plus_overview_card")

    def click_hp_plus_requirements_card(self):
        self.driver.click("hp_plus_requirements_card")

    def click_instant_ink_card(self):
        self.driver.click("instant_ink_card")

    def click_forest_first_printing(self):
        self.driver.click("forest_first_printing")

    def click_hp_smart_advance_card(self):  
        self.driver.click("hp_smart_advance_card")

    def click_smart_security_card(self):
        self.driver.click("smart_security_card")
    
    def click_decline_hp_plus_offer(self):
        self.driver.click("decline_hp_plus_offer_btn")

    def click_back_to_hp_plus_offer_btn(self):
        self.driver.click("back_to_hp_plus_offer_btn")

    def click_card_back_button(self):
        self.driver.click("card_back_button")

    def click_close_btn(self):
        self.driver.click("close_btn")
    
########################################################################################################################
#                                            Verification Flows                                                        #
########################################################################################################################
        
    def verify_hp_plus_hp_plus_learn_more_modal(self, account_type):
        self.driver.wait_for_object("hp_plus_learn_more_modal")
        self.driver.wait_for_object("hp_plus_overview_card")
        self.driver.wait_for_object("hp_plus_requirements_card")
        self.driver.wait_for_object("instant_ink_card")
        self.driver.wait_for_object("forest_first_printing")
        self.driver.wait_for_object("hp_smart_advance_card" if account_type == "personal" else "hp_smart_pro_card")
        self.driver.wait_for_object("smart_security_card")
        self.driver.wait_for_object("close_btn")
    
    def validate_hp_plus_overview_card(self, spec_data):
        res=[]
        res.append(self.string_validation(spec_data, "hp_plus_overview_card_header", raise_e=False))
        res.append(self.string_validation(spec_data, "hp_plus_overview_what_is_hp_plus", raise_e=False))
        self.driver.click("hp_plus_overview_what_is_hp_plus")
        res.append(self.string_validation(spec_data, "hp_plus_overview_what_is_hp_plus_desc", raise_e=False))
        res.append(self.string_validation(spec_data, "hp_plus_overview_is_hp_plus_subscription", raise_e=False))
        self.driver.click("hp_plus_overview_is_hp_plus_subscription")
        res.append(self.string_validation(spec_data, "hp_plus_overview_is_hp_plus_subscription_desc", raise_e=False))
        res.append(self.string_validation(spec_data, "hp_plus_overview_cost_for_hp_plus", raise_e=False))
        self.driver.click("hp_plus_overview_cost_for_hp_plus")
        res.append(self.string_validation(spec_data, "hp_plus_overview_cost_for_hp_plus_desc", raise_e=False))
        res.append(self.string_validation(spec_data, "hp_plus_overview_cancel_hp_plus", raise_e=False))
        self.driver.click("hp_plus_overview_cancel_hp_plus")
        res.append(self.string_validation(spec_data, "hp_plus_overview_cancel_hp_plus_desc", raise_e=False))
        res.append(self.string_validation(spec_data, "hp_plus_overview_same_as_instant_ink", raise_e=False))
        self.driver.click("hp_plus_overview_same_as_instant_ink")
        res.append(self.string_validation(spec_data, "hp_plus_overview_same_as_instant_ink_desc", raise_e=False))
        res.append(self.string_validation(spec_data, "hp_plus_activate_later", raise_e=False))
        self.driver.click("hp_plus_activate_later")
        res.append(self.string_validation(spec_data, "hp_plus_activate_later_desc", raise_e=False))
        res.append(self.string_validation(spec_data, "hp_plus_overview_setup_someone_else", raise_e=False))
        self.driver.click("hp_plus_overview_setup_someone_else")
        res.append(self.string_validation(spec_data, "hp_plus_overview_setup_someone_else_desc", raise_e=False))
        return False if False in res else True
    
    def validate_instant_ink_card(self, spec_data):
        res=[]
        res.append(self.string_validation(spec_data, "what_is_instant_ink", raise_e=False))
        self.driver.click("what_is_instant_ink")
        res.append(self.string_validation(spec_data, "ii_what_is_instant_ink_desc", raise_e=False))
        res.append(self.string_validation(spec_data, "ii_instant_work_after_trial", raise_e=False))
        self.driver.click("ii_instant_work_after_trial")
        res.append(self.string_validation(spec_data, "ii_instant_work_after_trial_desc", raise_e=False))
        res.append(self.string_validation(spec_data, "ii_how_soon_ink_after_enroll", raise_e=False))
        self.driver.click("ii_how_soon_ink_after_enroll")
        res.append(self.string_validation(spec_data, "ii_how_soon_ink_after_enroll_desc", raise_e=False))
        res.append(self.string_validation(spec_data, "ii_plans_costs", raise_e=False))
        self.driver.click("ii_plans_costs")
        res.append(self.string_validation(spec_data, "ii_plans_costs_desc", raise_e=False))
        res.append(self.string_validation(spec_data, "ii_cancel_instant_ink", raise_e=False))
        self.driver.click("ii_cancel_instant_ink")
        res.append(self.string_validation(spec_data, "ii_cancel_instant_ink_desc", raise_e=False))
        self.driver.click("ii_credit_card_required_to_enroll")
        res.append(self.string_validation(spec_data, "ii_credit_card_required_to_enroll_desc", raise_e=False))
        return False if False in res else True
    
    def validate_forest_first_printing_card(self, spec_data):
        res=[]
        res.append(self.string_validation(spec_data, "forest_first_printing_header", raise_e=False))
        res.append(self.string_validation(spec_data, "what_forest_first_printing", raise_e=False))
        res.append(self.string_validation(spec_data, "what_forest_first_printing_desc", raise_e=False))
        return False if False in res else True
    
    def validate_hp_smart_pro(self, spec_data):
        res=[]
        res.append(self.string_validation(spec_data, "hp_smart_pro_header", raise_e=False))
        res.append(self.string_validation(spec_data, "what_is_hp_smart_pro", raise_e=False))
        return False if False in res else True
    
    def validate_hp_smart_advance_card(self, spec_data):
        res=[]
        res.append(self.string_validation(spec_data, "hp_smart_advance_header", raise_e=False))
        res.append(self.string_validation(spec_data, "what_is_hp_smart_advance", raise_e=False))
        res.append(self.string_validation(spec_data, "what_is_hp_smart_advance_desc", raise_e=False))
        return False if False in res else True

    def validate_smart_security_card(self, spec_data):
        res=[]
        res.append(self.string_validation(spec_data, "smart_security_header", raise_e=False))
        res.append(self.string_validation(spec_data, "smart_security_with_hp_plus", raise_e=False))
        return False if False in res else True
    
    def verify_close_btn(self):
        self.driver.wait_for_object("close_btn")
    
    def verify_card_back_button(self):
        self.driver.wait_for_object("card_back_button")
    
    def verify_hp_plus_continue_btn(self):
        self.driver.wait_for_object("hp_plus_continue_btn")    
    
    def verify_learn_more_btn(self):
        self.driver.wait_for_object("learn_more_btn")
    
    def verify_learn_more_modal_card_content(self):
        self.driver.wait_for_object("card_content")
    
    def verify_single_question_card_content(self):
        self.driver.wait_for_object("single_question_card_content")
    
    def verify_hp_plus_benefits_page(self):
        """
        Verify HP PLus benefits page url: https://smb.stage.portalshell.int.hp.com/us/en/hp-plus-benefits
        """
        self.driver.wait_for_object("hp_plus_printer_benefits_page")

    @screenshot_compare(root_obj="printer_activation_hp_plus_benefits")
    def verify_printer_activation_hp_plus_benefits(self):
        """
        Verify HP+ Benefits shown on printer Activation.
        """
        self.driver.wait_for_object("printer_activation_hp_plus_benefits")

    def verify_decline_exclusive_hp_plus_offer_modal(self):
        self.driver.wait_for_object("exclusive_hp_plus_offer_overlay_modal")
        self.driver.wait_for_object("decline_hp_plus_offer_btn")
        self.driver.wait_for_object("back_to_hp_plus_offer_btn")