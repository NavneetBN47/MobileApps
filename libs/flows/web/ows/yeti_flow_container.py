import pytest
import logging
import time

from SAF.decorator.saf_decorator import screenshot_compare

from MobileApps.libs.flows.web.ows import ows_utility
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.ows.ucde_offer import UCDEOffer
from MobileApps.libs.flows.web.ows.ows_welcome import OWSWelcome
from MobileApps.libs.flows.web.ows.ucde_privacy import UCDEPrivacy
from MobileApps.libs.flows.web.ows.ows_emulator import OWSEmulator
from MobileApps.libs.flows.web.ows.ucde_safety_net import UCDESafetyNet
from MobileApps.libs.flows.web.instant_ink.billing_ii import BillingII
from MobileApps.libs.flows.web.instant_ink.shipping_ii import ShippingII
from MobileApps.libs.flows.web.instant_ink.value_proposition import ValueProposition
from MobileApps.libs.flows.web.smart.smart_printer_consent import SmartPrinterConsent
from MobileApps.libs.flows.web.ows.ucde_activation_success import UCDEActivationSuccess

class YetiFlowContainer():
    printer_profile_dict ={"skyreach": "horizon", "manhattan_yeti": "manhattan", "vasari_yeti": "vasari", "taccolabaseyeti": "taccola", "novelli": "novelli", "marconi": "marconi"}
    #printer_offer_dict ={"manhattan_yeti": 1, "skyreach": 0}
    def __init__(self, driver, context=None,  url=None):
        self.driver = driver
        self.fd = {"hpid": HPID(driver, context=context, url=url),
                   "smart_printer_consent": SmartPrinterConsent(driver, context=context, url=url),
                   "ucde_offer": UCDEOffer(driver, context=context, url=url),
                   "ucde_privacy": UCDEPrivacy(self.driver, context=context, url=url),
                   "ucde_activation_success": UCDEActivationSuccess(driver, context=context, url=url),
                   "ucde_safety_net": UCDESafetyNet(driver, context=context, url=url),
                   "value_proposition": ValueProposition(driver, context=context, url=url),
                   "billing": BillingII(driver),
                   "shipping" : ShippingII(driver),
                   "ows_emulator": OWSEmulator(driver)}

    @property
    def flow(self):
        return self.fd

    def get_printer_name_from_profile(self, profile):
        return self.printer_profile_dict[profile]

    def get_printer_offer_from_profile(self, profile):
        return self.printer_offer_dict[profile]

    def emulator_start_yeti(self, stack, profile, biz_model, model_sku):
        emu_platform = self.driver.session_data["request"].config.getoption("--emu-platform")
        if profile == "skyreach":
            self.offer = 0
        else:
            self.offer = 1
        sim_printer_info = ows_utility.create_simulated_gen2_printer(stack=stack, profile=profile, biz_model=biz_model, offer=self.offer, model_sku=model_sku)
        self.flow["ows_emulator"].open_emulator(stack)
        self.flow["ows_emulator"].select_dev_menu_list_item()
        self.flow["ows_emulator"].click_hpid_login_button()
        self.flow["hpid"].verify_hp_id_sign_up(timeout=20)
        email, password = self.flow["hpid"].create_account()
        self.flow["ows_emulator"].verify_emulator_load()
        self.flow["ows_emulator"].dismiss_banner()
        self.flow["ows_emulator"].select_app_or_post_oobe_list_item()
        access_token = self.flow["ows_emulator"].get_web_auth_access_token()
        self.flow["ows_emulator"].clear_web_auth_access_token()
        id_token = self.flow["ows_emulator"].get_id_token()
        self.flow["ows_emulator"].clear_id_token()
        self.flow["ows_emulator"].toggle_app_authenticate_user(on=False)
        self.flow["ows_emulator"].select_quick_option_by_printer(profile)
        self.flow["ows_emulator"].select_device_menu_list_item()
        self.flow["ows_emulator"].enter_claim_postcard(sim_printer_info["claim_postcard"])
        self.flow["ows_emulator"].enter_uuid(sim_printer_info["uuid"])
        logging.info("UUID: " + sim_printer_info["uuid"])
        self.flow["ows_emulator"].enter_cdm_printer_fingerprint(sim_printer_info["fingerprint"])
        self.flow["ows_emulator"].enter_serial_number(sim_printer_info["serial_number"])
        self.flow["ows_emulator"].enter_sku(sim_printer_info["model_number"])
        self.flow["ows_emulator"].select_language_config_dropdown_and_choose("string:completed")
        self.flow["ows_emulator"].select_country_config_dropdown_and_choose("string:completed")
        ows_status = self.flow["ows_emulator"].return_oobe_status()
        self.flow["ows_emulator"].select_app_or_post_oobe_list_item()
        self.flow["ows_emulator"].select_app_type_dropdown_and_choose(option=emu_platform)
        self.flow["ows_emulator"].select_actions_button()
        return [ows_status, access_token, id_token, sim_printer_info, email, password]

    def navigate_yeti(self, profile, biz_model):
        time.sleep(3)
        self.flow["ucde_offer"].verify_ucde_offer()
        if profile.lower() == "skyreach" and biz_model.lower() == "flex":
            self.flow["ucde_offer"].click_decline_account_btn()
            self.flow["ucde_safety_net"].verify_ucde_safety_net()
            self.flow["ucde_safety_net"].click_back_to_account_btn()
            #self.flow["ucde_offer"].click_flex_sign_in_btn()
        elif biz_model.lower() == "decline":
            self.flow["ucde_offer"].click_decline_offer_btn()
            self.flow["ucde_offer"].click_decline_hp_plus_offer_btn()
            self.flow["ucde_offer"].verify_printer_dynamic_security_notice()
            self.flow["ucde_offer"].click_continue()
        
        # The flow in else statement works for taccola yeti
        else:
            time.sleep(5)
            self.flow["ucde_offer"].verify_ucde_hp_plus_benefits_page()
            self.flow["ucde_offer"].click_continue()
            self.flow["ucde_offer"].verify_confirm_requirements_page()
            self.flow["ucde_offer"].verify_confirm_requirments_footer()
            self.flow["ucde_offer"].click_confirm_button()
            time.sleep(10)


    def navigate_hp_plus_features_and_offer(self, hp_plus=False):
        self.flow["ucde_offer"].verify_ucde_hp_plus_benefits_page()
        self.flow["ucde_offer"].verify_learn_more_btn()
        self.flow["ucde_offer"].verify_continue_btn()
        self.flow["ucde_offer"].verify_do_not_activate_hp_plus_btn()
        self.flow["ucde_offer"].click_learn_more_btn()
        self.flow["ucde_offer"].verify_learn_more_page()
        self.flow["ucde_offer"].click_learn_more_back_btn()
        self.flow["ucde_offer"].click_decline_offer_btn()
        self.flow["ucde_offer"].verify_decline_offer_popup()
        self.flow["ucde_offer"].verify_decline_hp_plus_offer_btn()
        if hp_plus:
            self.flow["ucde_offer"].click_continue(change_check={"wait_obj": "hp_plus_benefits_page"})
            self.flow["ucde_offer"].verify_ucde_hp_plus_benefits_page()
            self.flow["ucde_offer"].verify_hp_plus_offer_page()
            self.flow["ucde_offer"].click_hp_plus_offer_page_activate_btn()
        else:
            self.flow["ucde_offer"].click_decline_hp_plus_offer_btn()
            self.flow["ucde_offer"].verify_printer_dynamic_security_notice()
            self.flow["ucde_offer"].click_printer_dynamic_security_notice_continue_btn()


    def perform_login_via_emulator(self, ows_printer, access_token, id_token):
        ows_printer.login(access_token, id_token)
        redirect_url_1 = ows_printer.get_console_data("PUT - ForceSignInHp")["params"]["continuationUrl"]+ "&completionCode=0"
        self.driver.switch_window()
        self.driver.navigate(redirect_url_1)
