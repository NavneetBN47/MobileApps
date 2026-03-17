import logging
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.ows.ucde_privacy import UCDEPrivacy
from MobileApps.libs.flows.web.ows.ows_welcome import OWSWelcome
from MobileApps.libs.flows.web.ows.ucde_safety_net import UCDESafetyNet
from MobileApps.libs.flows.web.ows.value_prop import ValueProp
from MobileApps.libs.flows.web.ows.sub_flow.ows_flow_factory import sub_flow_factory
from MobileApps.libs.flows.web.ows.ows_emulator import OWSEmulator
from MobileApps.libs.flows.web.ows.sub_flow.something_unexpected_error_modal import SUH
from MobileApps.libs.flows.web.ows.sub_flow.connected_printing_services import ConnectedPrintingServices
from MobileApps.libs.flows.web.instant_ink.billing_ii import BillingII
from MobileApps.libs.flows.web.instant_ink.shipping_ii import ShippingII
from MobileApps.libs.flows.web.instant_ink.value_proposition import ValueProposition
from MobileApps.libs.flows.web.ows.firmware_update_page import FirmwareUpdateChoice
import time

class BaseFlowContainer():

    def __init__(self, driver, ows_p_obj, context=None, url=None):
        self.driver = driver
        self.fd = {"osprey": sub_flow_factory(driver, "Osprey", context=context, url=url),
                   "welcome": OWSWelcome(driver, context=context, url=url),
                   "hpid": HPID(driver, context=context, url=url),
                   "connected_printing_services": ConnectedPrintingServices(driver, context=context, url=url),
                   "ucde_privacy": UCDEPrivacy(driver, context=context, url=url),
                   "ucde_safety_net": UCDESafetyNet(driver, context=context, url=url),
                   "value_prop": ValueProp(driver),
                   "suh": SUH(self.driver, context=context, url=url),
                   "emulator": OWSEmulator(self.driver),
                   "billing": BillingII(driver),
                   "shipping": ShippingII(driver),
                   "instant_ink_value_prop": ValueProposition(driver),
                   "firmware_update_choice": FirmwareUpdateChoice(driver)
                   }
        self.ows_p = ows_p_obj
        self.ows_method_dict = {}

    @property
    def flow(self):
        return self.fd

    def navigate_welcome(self):
        self.fd["welcome"].verify_welcome_screen()
        self.fd["welcome"].click_continue()
        #Needs refactoring as this method is moved out of hpid
        self.fd["welcome"].verify_welcome_screen()
        self.fd["welcome"].select_more_options()
        self.fd["welcome"].select_skip_option()
        self.fd["welcome"].select_yes_popup_option()

    def navigate_ows(self, p_obj, stop_at=None):
        oobe_flow_list = p_obj.return_oobe_status()
        for s_step in oobe_flow_list:
            if s_step["name"] == stop_at:
                return True
            elif s_step["state"] == "completed":
                continue 
            else:
                method = self.ows_method_dict.get(s_step["name"], None)
                if method is None:
                    logging.warning("No navigation flow for step: " + s_step["name"] + " will mark ledm completed")
                    p_obj.update_ledm(s_step["name"], "completed")
                else:
                    method()
        return True

    def invoke_suh_via_ink_completion_code(self, p_obj, fc):
        p_obj.toggle_ledm_status("insert_ink_dropbox", option_value="completed")
        p_obj.toggle_supply_ink_info(option_value="-6")
        fc.flow["load_ink"].verify_web_page()
        self.fd["suh"].verify_suh_error_modal()
        self.fd["emulator"].verify_web_page()
        p_obj.toggle_supply_ink_info(option_value="0")
        p_obj.click_get_product_status_btn()
        p_obj.update_ledm("insertInk", "completed")
        fc.flow["load_ink"].ink_click_continue()

    def invoke_suh_via_product_completion_code(self, p_obj, recover=True):
        p_obj.toggle_ledm_status("insert_ink_dropbox", option_value="completed")
        self.driver.click("supplies_info_tab")
        self.driver.click("get_supply_info_btn")
        p_obj.toggle_product_status(option_value="-6")
        self.fd["suh"].verify_suh_error_modal(recover=recover)

    def invoke_suh_via_oobe_status_code(self, p_obj, recover=True):
        p_obj.toggle_ledm_status("oobe_completion_code_dropbox", option_value="-6")
        self.fd["suh"].verify_suh_error_modal(recover=recover)
        self.fd["emulator"].verify_web_page()
        p_obj.toggle_ledm_status("oobe_completion_code_dropbox", option_value="0")

    def navigate_instant_ink(self, enroll=False, timeout=10):
        self.fd["instant_ink_value_prop"].verify_value_proposition_page(timeout=timeout)
        if not enroll:
            self.fd["instant_ink_value_prop"].skip_value_proposition_page()
        else:
            self.fd["instant_ink_value_prop"].click_continue_btn(timeout=25)
            self.fd["instant_ink_value_prop"].click_continue_on_automatic_printer_updates()
            self.fd["instant_ink_value_prop"].verify_enroll_instant_ink_page()
            self.fd["shipping"].click_add_shipping_btn()
            self.fd["shipping"].verify_shipping_overlay_modal()
            self.fd["shipping"].verify_shipping_page_load()
            self.fd["shipping"].load_address("en-us")
            self.fd["shipping"].save_shipping_address()
            time.sleep(3) # Adding hard wait as Sometimes the Page takes couple of seconds to completely close shiping overlay modal and fully loading main page.
            self.fd["billing"].click_add_billing_btn()
            self.fd["billing"].verify_billing_overlay_modal()
            self.fd["billing"].click_continue_btn()
            self.fd["billing"].verify_creditcard_iframeload()
            self.fd["billing"].load_card_details(cardtype="visa")
            self.fd["instant_ink_value_prop"].click_continue_btn(clickable=True, timeout=30)
            self.fd["instant_ink_value_prop"].handle_instant_ink_terms_of_service()
            self.fd["instant_ink_value_prop"].verify_toner_is_on_the_way()
            self.fd["instant_ink_value_prop"].click_continue_btn()


    def navigate_firmware_update_choice(self, auto=True):
        self.fd["firmware_update_choice"].verify_firmware_update_choice_page(timeout=30)
        if auto:
            self.fd["firmware_update_choice"].click_auto_update_button()
        else:
            self.fd["firmware_update_choice"].click_manual_update_btn()
        self.fd["firmware_update_choice"].click_apply_button()
            