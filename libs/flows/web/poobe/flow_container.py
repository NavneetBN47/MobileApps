from MobileApps.libs.flows.web.poobe.poobe import PortalOOBE
from MobileApps.libs.flows.web.poobe.ecp import ECP
from MobileApps.libs.flows.web.poobe.partner_link_page import PartnerLinkPage
from MobileApps.libs.flows.web.poobe.value_prop_page import ValuePropPage
from MobileApps.libs.flows.web.poobe.assign_printer_organization import AssignPrinterOrganization
from MobileApps.libs.flows.web.poobe.pairing_code_page import PairingCodePage
from MobileApps.libs.flows.web.poobe.account_type_page import AccountTypePage
from MobileApps.libs.flows.web.poobe.iris_firmware_update_notice import IrisFWUpdateNotice
from MobileApps.libs.flows.web.poobe.printer_name_location_page import PrinterNameAndLocation
from MobileApps.libs.flows.web.poobe.hp_plus_offer_and_benefits import HpPlusOfferAndBenefits
from MobileApps.libs.flows.web.poobe.hp_plus_smart_printer_requirements import HpPlusSmartPrinterRequirements
from MobileApps.libs.flows.web.poobe.portal_error_modal import PortalErrorModal
from MobileApps.libs.flows.web.poobe.resume_session_modal import ResumeSession
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.ows import ows_utility
from MobileApps.libs.flows.web.instant_ink.value_proposition import ValueProposition
from MobileApps.libs.flows.web.poobe.install_printing_sw import InstallPrintingSW
from MobileApps.libs.flows.web.instant_ink.billing_ii import BillingII
from MobileApps.libs.flows.web.instant_ink.shipping_ii import ShippingII
from MobileApps.libs.flows.web.ows.olex_123_and_psw.traffic_director import TrafficDirector
from MobileApps.libs.flows.email.gmail_api import GmailAPI, CONST
from MobileApps.resources.const.web.const import *
from MobileApps.libs.flows.web.smb.home import Home
from MobileApps.libs.flows.web.smb.login import Login
from MobileApps.libs.flows.web.smb.account import Account
from MobileApps.libs.flows.web.smb.printers import Printers
from MobileApps.libs.flows.web.smb.users import Users
from MobileApps.libs.flows.web.ecp.home import Home as ECPHome
from MobileApps.libs.flows.web.ecp.devices import Devices
from MobileApps.libs.flows.web.ows.olex_123_and_psw.td_live_ui import TrafficDirectorLiveUI
from MobileApps.libs.flows.web.ows.sub_flow.connected_printing_services import ConnectedPrintingServices
from MobileApps.libs.flows.web.ows.olex_123_and_psw.hp_123 import HP123
from MobileApps.libs.flows.web.hp_connect.hp_connect import HPConnect
from MobileApps.libs.flows.web.hp_connect.printers_users import PrintersUsers
from MobileApps.libs.ma_misc import ma_misc
import pytest
import time
import logging
import json, os

class FlowContainer(object):

    def __init__(self, driver, endpoint, printer_profile, window="main", hp_123="123-site"):
        self.driver = driver
        self.endpoint = endpoint
        self.fd = {"hpid": HPID(driver),
                   "poobe":PortalOOBE(driver, endpoint, window_name=window),
                   "ecp": ECP(driver, endpoint),
                   "value_prop_page": ValuePropPage(driver, window_name=window),
                   "assign_printer_organization": AssignPrinterOrganization(driver, window_name=window),
                   "connected_printing_services": ConnectedPrintingServices(driver, window_name=window),
                   "pairing_code_page": PairingCodePage(driver, window_name=window),
                   "account_type_page": AccountTypePage(driver, window_name=window),
                   "printer_name_location_page": PrinterNameAndLocation(driver, window_name=window),
                   "iris_fw_update_notice": IrisFWUpdateNotice(driver, window_name=window),
                   "hp_plus_offer_and_benefits": HpPlusOfferAndBenefits(driver, window_name=window),
                   "hp_plus_smart_printer_requirements": HpPlusSmartPrinterRequirements(driver, window_name=window),
                   "portal_error_modal": PortalErrorModal(driver, window_name=window),
                   "resume_session_modal": ResumeSession(driver, window_name=window),
                   "traffic_director" : TrafficDirector(driver, printer_profile),
                   "instant_ink_value_prop": ValueProposition(driver, window_name=window),
                   "gmail_api": GmailAPI(credential_path=TEST_DATA.GMAIL_TOKEN_PATH),
                   "gmail_const": CONST,
                   "billing" : BillingII(driver),
                   "shipping" : ShippingII(driver),
                   "install_printer_sw": InstallPrintingSW(driver, window_name=window),
                   "smb_dashboard_home": Home(driver),
                   "smb_dashboard_login": Login(driver),
                   "smb_dashboard_account": Account(driver),
                   "smb_printers_tab": Printers(driver),
                   "smb_dashboard_users": Users(driver),
                   "td_live_ui":TrafficDirectorLiveUI(driver, printer_profile),
                   "hp_123": HP123(driver, hp_123),
                   "hp_connect": HPConnect(driver),
                   "printers_users": PrintersUsers(driver),
                   "partner_link_page": PartnerLinkPage(driver),
                   "ecp_home": ECPHome(driver),
                   "devices": Devices(driver)}
        
        self.dual_sku_printers = ["storm", "hulk", "yoshino", "lochsa", "ulysses", "selene"]
        self.single_sku_printers = ["marconi", "kebin"]  # '/onboard' flow is a separate flow from Traffic Director known as 'Single SKU Marconi Portal OOBE'
        self.ecp_printers = ["beam_ecp", "jupiter_ecp", "enterprise_ecp"]
        self.smb_lf_printer = ["beam"]
        self.smb_flex_printer = ["zelus", "euthinia", "marconi_pdl"]
        self.smb_flowers = ['lotus', 'cherry']
        self.file_key = ma_misc.load_json_file("resources/test_data/poobe/spec_key.json")

    def generate_simulator_printer(self, printer_profile, stack, biz_model, offer=0, country=False, language=False):
        if printer_profile in self.single_sku_printers:
            biz_model = "Flex"
            offer = 1
        elif printer_profile in self.smb_lf_printer and biz_model == "E2E":
            return None
        elif printer_profile in self.ecp_printers and biz_model == "Flex":
            printer_profile = printer_profile.split("_")[0]
        elif printer_profile in self.ecp_printers and biz_model == "E2E":
            return None
        elif printer_profile in self.smb_flex_printer and biz_model == "E2E":  # marconi_pdl, zelus and euthinia only for /connect flow so persona Flex. Skip for E2E.
            return None
        elif printer_profile in self.smb_flex_printer and biz_model == "E2E":
            return None
        elif printer_profile in self.smb_flowers and biz_model == "E2E":
            return None
        if country and language:
            return ows_utility.create_simulated_gen2_printer(stack=stack, profile=printer_profile, biz_model=biz_model, offer=offer, country=country, language=language)
        else:
            return ows_utility.create_simulated_gen2_printer(stack=stack, profile=printer_profile, biz_model=biz_model, offer=offer)
    
    
    def value_prop_page(self, biz, printer_profile, logged_in=False, raise_e=False):
        self.fd["hpid"].handle_privacy_popup(timeout=5)
        if printer_profile in ["beam", "jupiter", "enterprise"]:
            self.ecp_lf_value_prop_page(raise_e)
        else:
            self.landing_page(biz,logged_in)
     
    def landing_page(self, biz, logged_in=False, printer_profile=None, raise_e=False):
        self.ecp_lf_value_prop_page(raise_e)
        self.fd["value_prop_page"].verify_landing_page_subheader()
        self.fd["value_prop_page"].verify_landing_page_steps()
        self.fd["hpid"].handle_privacy_popup(timeout=5)
        self.fd["value_prop_page"].click_landing_page_these_featurs_btn()
        self.fd["value_prop_page"].verify_these_features_modal()
        self.fd["value_prop_page"].verify_cloud_based_feature_header(raise_e=raise_e)
        self.fd["value_prop_page"].verify_landing_page_cloud_based_features_description(raise_e=raise_e)
        self.fd["value_prop_page"].click_landing_page_cloud_based_features_modal_close_btn()
        if biz == "Flex" and printer_profile in self.dual_sku_printers:
            self.fd["value_prop_page"].click_landing_page_complete_without_features_modal_btn()
            self.fd["value_prop_page"].verify_complete_basic_setup_overlay()
            self.fd["value_prop_page"].verify_complete_basic_setup_content()
            self.fd["value_prop_page"].click_complete_basic_setup_overlay_close_btn()
        if logged_in:
            self.fd["value_prop_page"].verify_value_prop_page_logged_in_right_section()
        else:
            self.fd["value_prop_page"].verify_get_started_header_sub_header(raise_e=raise_e)
            #if printer_profile in self.smb_flowers:
                #self.fd["value_prop_page"].verify_startscan_get_started_sub_header(raise_e=raise_e)
    
    def ecp_lf_value_prop_page(self, raise_e):
        self.fd["value_prop_page"].verify_value_prop_page()
        self.fd["value_prop_page"].verify_value_prop_left_panel()
        self.fd["value_prop_page"].verify_value_prop_right_panel()
        self.fd["value_prop_page"].verify_landing_page_header(raise_e)
        self.fd["value_prop_page"].verify_landing_page_steps()    
    
    def psw_onboarding_page(self):
        self.fd["traffic_director"].verify_onboarding_center_page()
        self.fd["traffic_director"].verify_start_setup_btn()
        self.fd["traffic_director"].verify_watch_video_btn()
        self.fd["traffic_director"].click_watch_video_button()
        self.fd["traffic_director"].verify_watch_video_modal()
        self.fd["traffic_director"].verify_watch_video_subtitle()
        self.fd["traffic_director"].click_watch_video_modal_close_button()
        
    def navigate_traffic_director_live_ui(self, printer_profile):
        #self.fd["td_live_ui"].navigate_power_on_country_language_step()
        self.fd["td_live_ui"].navigate_load_paper_step(printer_profile)
        self.fd["td_live_ui"].navigate_install_ink_step(printer_profile)
        self.fd["td_live_ui"].navigate_alignment_step(printer_profile)
        if self.driver.get_browser_platform() == "linux":
            self.fc.fd["td_live_ui"].navigate_unsupported_os_page()
        else:
            self.fd["td_live_ui"].navigate_hp_software_step(printer_profile)

    def create_hpid_login_credentials(self):
        self.fd["hpid"].verify_hp_id_sign_in()
        self.email, self.pwd = self.fd["hpid"].create_account()
        return self.email, self.pwd

    def select_how_to_setup_printer_company_or_personal(self, biz, printer_type):
        self.fd["account_type_page"].verify_select_account_type_page()
        self.fd["poobe"].verify_left_panel_printer_container(biz)
        self.fd["account_type_page"].click_personal_or_business_printer(printer_type)
        if printer_type == "personal":
            self.fd["poobe"].verify_hp_tC_eula_page()
            self.fd["poobe"].click_continue_btn()

    def navigate_printer_owner_page(self, biz, name):
        self.fd["assign_printer_organization"].verify_assign_printer_owner_page()
        self.fd["poobe"].verify_left_panel_printer_container(biz)    
        self.fd["assign_printer_organization"].verify_oranganization_option()
        if self.fd["assign_printer_organization"].verify_assign_printer_owner_page_radiogroup():
            self.fd["assign_printer_organization"].select_new_organization_option()
        self.fd["assign_printer_organization"].verify_organization_country_region_drop_down()
        self.fd["assign_printer_organization"].click_assign_organization_box()
        self.fd["assign_printer_organization"].verify_organization_input_box_focused()
        self.driver.send_keys("organization_name_box", name)
        self.fd["assign_printer_organization"].click_continue_btn()

    def verify_assign_organization_step(self, biz, name, ecp=False):
        self.fd["assign_printer_organization"].verify_assign_printer_owner_page()
        self.fd["poobe"].verify_left_panel_printer_container(biz)        
        self.fd["assign_printer_organization"].verify_oranganization_option()
        if self.fd["assign_printer_organization"].verify_assign_printer_owner_page_radiogroup():
            self.fd["assign_printer_organization"].select_new_organization_option()
        self.fd["assign_printer_organization"].verify_organization_country_region_drop_down()
        self.fd["assign_printer_organization"].verify_oraganization_label()
        self.fd["poobe"].verify_continue_btn(clickable=True, raise_e=False)
        if ecp is False:
            self.fd["assign_printer_organization"].verify_hp_smart_terms_conditions_url()
            self.fd["assign_printer_organization"].click_hp_smart_terms_conditions_url()
        else:
            self.fd["ecp"].verify_command_center_terms_of_use()
            self.fd["ecp"].click_hp_command_center_terms_of_use()
        self.fd["assign_printer_organization"].click_assign_organization_box()
        self.fd["assign_printer_organization"].verify_organization_input_box_focused()
        self.fd["assign_printer_organization"].select_organization_country_region_seclector()
        self.fd["assign_printer_organization"].select_united_states_country_region()
        self.driver.send_keys("organization_name_box", name)
        self.driver.add_window("admin-tou")
        self.driver.close_window("admin-tou")

    def navigate_printer_consents_page(self, ecp=False):
        self.fd["connected_printing_services"].verify_connected_printing_services()
        if not ecp:
            self.fd["connected_printing_services"].click_connected_printing_services_manage_options_btn()
            self.fd["connected_printing_services"].click_connected_printing_services_learn_more_hyperlink()
            self.driver.add_window("data_collection_notice")
            self.driver.close_window("data_collection_notice")
            self.fd["connected_printing_services"].click_connected_printing_services_manage_options_back_btn()
        self.fd["connected_printing_services"].click_connected_printing_services()


    def navigate_pairing_code_success_page(self, printer_profile, stack, printer_info, biz):
        if self.fd["poobe"].locale not in self.driver.current_url:
            self.driver.navigate(self.driver.current_url.replace("us/en", self.fd["poobe"].locale))         # workaround until issue is fixed
        self.fd["pairing_code_page"].verify_pairing_code_screen()
        self.fd["poobe"].verify_left_panel_printer_container(biz)
        if isinstance(printer_info, dict):
            self.pairing_details = ows_utility.get_pairing_code(printer_profile, stack, printer_info["fingerprint"], printer_info["claim_postcard"], printer_info["model_number"], printer_info["uuid"])
            self.fd["pairing_code_page"].input_pairing_code(code=self.pairing_details['user_code'])
            self.pairing_code = self.pairing_details['device_code'] # Device code from DAG api response is needed to complete pairing on activating page.
        else:
            self.pairing_code = printer_info.get_pairing_code() # This is pairing code from real printer is not needed once pairing is complete.
            self.fd["pairing_code_page"].input_pairing_code(code=self.pairing_code)
        self.fd["pairing_code_page"].click_continue_btn()
        return self.pairing_code

    def handle_printer_fw_page(self):
        self.fd["iris_fw_update_notice"].verify_fw_update_modal_page()
        self.fd["iris_fw_update_notice"].click_accept_auto_fw_updates()
        if self.fd["iris_fw_update_notice"].verify_fw_update_modal_page(raise_e=False):
            self.fd["iris_fw_update_notice"].click_accept_auto_fw_updates()
    
    def incorrect_flow_modal(self, code):
        self.fd["portal_error_modal"].verify_incorrect_flow_modal()
        self.fd["portal_error_modal"].verify_incorrect_modal_change_setup_btn()
        self.fd["portal_error_modal"].verify_incorrect_modal_try_again_btn()
        self.fd["portal_error_modal"].click_incorrect_modal_try_again_btn()
        self.fd["pairing_code_page"].input_pairing_code(code)
        self.fd["poobe"].click_continue_btn()
        self.fd["portal_error_modal"].verify_incorrect_flow_modal()
        self.fd["portal_error_modal"].verify_incorrect_modal_change_setup_btn()
        self.fd["portal_error_modal"].click_change_setup_button()
    
    def navigate_printer_name_location_page(self, biz, printer_profile, skip=False):
        self.fd["printer_name_location_page"].verify_printer_name_location_page()
        self.fd["poobe"].verify_left_panel_printer_container(biz, printer_profile)
        self.fd["printer_name_location_page"].verify_printer_name_location_helper_caption_text()
        if skip == False:
            self.fd["printer_name_location_page"].enter_printer_name_and_location()
        self.fd["printer_name_location_page"].click_printer_name_and_location_continue_btn() 

    def navigate_hp_plus_benefits_and_requirments_page(self, hp_plus, printer_profile):
        """
        Cureently This is for (marconi, kebin) as flow offers users to activate HP+ or decline HP+
        """
        self.fd["hp_plus_offer_and_benefits"].verify_hp_plus_benefits_page()
        self.fd["poobe"].verify_left_panel_printer_container(biz="E2E", printer_profile=printer_profile)
        self.fd["hp_plus_offer_and_benefits"].verify_printer_activation_hp_plus_benefits()
        if hp_plus == "decline": # Decline HP plus offer
            self.fd["hp_plus_offer_and_benefits"].click_decline_hp_plus()
            self.fd["hp_plus_offer_and_benefits"].verify_decline_exclusive_hp_plus_offer_modal()
            self.fd["hp_plus_offer_and_benefits"].click_decline_hp_plus_offer()
            self.fd["traffic_director"].verify_printer_dynamic_security_notice()
            self.fd["hp_plus_offer_and_benefits"].click_back_to_hp_plus_offer_btn()
        if hp_plus == "accept": # Accept Offer and continue if Accepted then from this point on UI should be orange theme
            self.fd["hp_plus_offer_and_benefits"].click_continue_btn()
            self.fd["hp_plus_smart_printer_requirements"].verify_hp_plus_smart_printer_requirements_page()
            self.fd["poobe"].verify_left_panel_printer_container(biz="E2E", printer_profile=printer_profile)
            self.fd["traffic_director"].click_activate_hp_plus_btn()
    
    def navigate_flow_from_printer_activation_page(self, printer_profile, stack, biz, printer_info=False, device_code=None, enroll=False, ecp=False):
        if isinstance(printer_info, dict):
            ows_utility.send_complete_pairing_code(stack, device_code, printer_info['uuid'])
        self.fd["poobe"].verify_activating_printer_page()
        if printer_profile in self.smb_lf_printer and ecp is False:
            self.verify_install_printer_sw_page(biz)
        elif ecp:
            self.handle_activation_time_error_if_any(biz, printer_profile+"_ecp")
        elif printer_profile in self.smb_flowers or (printer_profile in self.dual_sku_printers and biz == "Flex"):
            self.navigate_to_printer_setup_page(biz, printer_profile, enroll)
        else:
            self.navigate_to_printer_setup_page(biz, printer_profile, enroll)
    
    def navigate_to_printer_setup_page(self, biz, printer_profile, enroll=False):
        value = self.handle_activation_time_error_if_any(biz, printer_profile)
        if value == "iioffer" and printer_profile not in ["storm","hulk","lochsa", "zelus", "euthinia", "marconi_pdl"]: # Because sometimes II offer page mfe loads for a sec and redirects to next page (Install drivers)
            self.fd["instant_ink_value_prop"].verify_value_proposition_page(timeout=30)
            self.fd["poobe"].verify_left_panel_printer_container(biz, printer_profile)
            if enroll:
                self.enroll_in_instant_ink()
            else:
                self.fd["instant_ink_value_prop"].skip_value_proposition_page(timeout=25)
            return
        
        if value:
            # For printers not II eligible II mfe might load for a sec and redirect to next page (Install drivers) 
            # because II mfe may load for sec wait for object catches ink page IDs causing handle activation time error returning 'iioffer' instead of True
            return
        elif biz == "Flex":
            # No ink offer or Drivers page for flowers printer or connect flow Flex persona
            return
        
        raise AssertionError("Ink offer page did not show up after Printer Activation")
    
    def handle_activation_time_error_if_any(self, biz_model, printer_profile=None):
        """
        Printer Actiation can take upto max 300s (5min). There are 5 Steps any error can occur at any of the 5 steps. 
        So if error occurs on step 5 that means will have to wait all 5mins untill the error is captured.
        Workaround: is to keep checking for error modal until Printer Activation so if error occured on step2 then don't have to wait 5 mins.
        """
        current_time = time.time()
        while time.time() < current_time+300:
            if  (printer_profile in self.dual_sku_printers and biz_model == "E2E") and self.fd["instant_ink_value_prop"].verify_value_proposition_page(timeout=10, raise_e=False):
                return "iioffer"
            elif (printer_profile in self.dual_sku_printers or printer_profile in self.smb_flex_printer) and self.fd["poobe"].install_printer_drivers_page_content(self.driver.get_browser_platform(), timeout=10, raise_e=False):    #lochsa SIM SKU not II eligible so flow will just skip II offer page.
                return True
            elif printer_profile == "beam" and self.fd["install_printer_sw"].verify_install_printing_sw_page(timeout=10, raise_e=False):
                return True
            elif "ecp" in printer_profile and self.fd["ecp"].verify_ecp_finish_setup_page(timeout=10, raise_e=False):
                return True
            elif printer_profile in self.smb_flowers and self.fd["smb_printers_tab"].verify_printers_tab_page(timeout=10, raise_e=False):
                return True
            elif (printer_profile != "beam" and biz_model == "Flex") and (self.fd["smb_dashboard_home"].verify_tutorial_overlay_modal(raise_e=False) or self.fd["smb_dashboard_home"].verify_new_printer_added_modal(raise_e=False) or self.fd["smb_dashboard_home"].verify_printer_email_alerts_overlay(raise_e=False)):
                return True
            else:
                self.fd["portal_error_modal"].wait_for_error_modal(timeout=10)
    
    def navigate_install_driver_page(self, biz, printer_profile):
        self.fd["poobe"].verify_install_printer_driver_page(self.driver.get_browser_platform())
        self.fd["poobe"].verify_left_panel_printer_container(biz, printer_profile)
        self.fd["poobe"].skip_install_drivers_page(self.driver.get_browser_platform())
        self.fd["poobe"].verify_left_panel_printer_container(biz, printer_profile)
    
    def firmware_update_notice_page(self, printer_profile, biz, enroll=False):
        if printer_profile in self.single_sku_printers and biz == "Flex" and enroll is False:
            self.fd["iris_fw_update_notice"].verify_fw_update_modal_page()
            self.fd["iris_fw_update_notice"].handle_auto_firmware_update_notice_page()

    def verify_install_printer_sw_page(self, biz):
        self.handle_activation_time_error_if_any(biz, "beam")
        self.fd["install_printer_sw"].verify_copy_templete_btn()
        self.fd["install_printer_sw"].verify_template_text_box()
        self.fd["install_printer_sw"].verify_install_printer_driver_link()
    
    def navigate_partner_link_page(self):
        self.fd["partner_link_page"].verify_partner_link_page()
        assert self.fd["ecp"].verify_connect_button(clickable=True, raise_e=False) is False, "Connect button should not be clickable"        
    
    def verify_hp_smart_admin(self, biz, printer_type):
        self.fd["poobe"].verify_continue_to_hp_smart_admin_page()
        self.fd["poobe"].verify_left_panel_printer_container(biz)
        if printer_type == "company":
            self.fd["poobe"].verify_hp_smart_users_management_finish_printer_setup()
            self.fd["poobe"].verify_hp_smart_scan_fax_tiles()
            self.fd["poobe"].verify_fleet_control_finish_printer_setup()
        self.fd["poobe"].verify_subscriptions_tile()

    def verify_finish_printer_setup_page(self, biz, printer_profile, ecp):
        if printer_profile == "beam" and ecp is False:
            return True
        elif ecp:
            return self.ecp_finish_setup_page_and_command_center()
        elif printer_profile in self.smb_flowers:
            self.fd["smb_dashboard_home"].handle_printer_email_alerts_overlay()
            self.fd["smb_printers_tab"].verify_printer_details_section()
            if self.fd["poobe"].verify_scan_to_email_enable_modal(raise_e=False):
                self.fd["poobe"].click_scan_setup_complete_modal_close_btn()
            self.fd["smb_dashboard_home"].click_home_menu_btn()
            if self.fd["smb_printers_tab"].verify_printers_tab_page(raise_e=False):
                self.fd["smb_dashboard_home"].click_home_menu_btn()
        if biz == "E2E":
            self.fd["poobe"].verify_continue_to_hp_smart_admin_page()
            self.fd["poobe"].click_open_hp_smart_admin_btn()
        self.verify_smb_dashboard(biz)
    
    def start_flow_and_continue_to_specific_page_in_flow(self, printer_profile, printer_type, company_name, stack, printer_info, biz, page):
        self.value_prop_page(biz, printer_profile, logged_in=True)
        self.fd["value_prop_page"].click_landing_page_continue_btn()
        time.sleep(5)
        device_code = self.navigate_pairing_code_success_page(printer_profile, stack, printer_info, biz)
        self.navigate_printer_owner_page(biz, name=company_name)
        self.fd["connected_printing_services"].verify_connected_printing_services()
        if page == "printer_consents_page": return
        self.navigate_printer_consents_page()
        if biz == "Flex" and printer_profile not in self.single_sku_printers:
            self.fd["iris_fw_update_notice"].verify_fw_update_modal_page()
        if page == "iris_fw_update_notice": return
        if biz == "Flex": self.fd["iris_fw_update_notice"].click_accept_auto_fw_updates()
        if printer_profile != "beam": 
            self.fd["printer_name_location_page"].verify_printer_name_location_page()
            self.fd["printer_name_location_page"].click_printer_name()
        if page == "printer_name_location_page": return
        self.navigate_printer_name_location_page(biz, printer_profile)
        if printer_profile not in self.single_sku_printers and biz == "E2E":
            self.fd["hp_plus_smart_printer_requirements"].verify_hp_plus_smart_printer_requirements_page()
        if page == "hp_plus_smart_printer_requirements_page": return
        if biz == "E2E": self.fd["poobe"].click_continue_btn()
        self.fd["poobe"].verify_activating_printer_page()
        self.fd["poobe"].click_activating_printer_page()
        if page == "activating_printer_page": return
        ows_utility.send_complete_pairing_code(stack, device_code, printer_info['uuid'])
        self.navigate_to_printer_setup_page(biz, printer_profile, enroll=False)
        self.fd["poobe"].verify_install_printer_driver_page(self.driver.get_browser_platform())
        if page == "install_printer_driver_page": return
    
    def verify_smb_dashboard(self, biz, timeout=15):
        time.sleep(1)
        self.fd["smb_dashboard_home"].handle_printer_email_alerts_overlay()
        self.fd["smb_dashboard_home"].handle_smb_dashboard_overlay(timeout=timeout)
        self.fd["smb_dashboard_login"].handle_intercept_survey_modal(timeout=10)
        if biz == "E2E":
            self.fd["smb_dashboard_home"].verify_solutions_menu_btn()
            self.fd["smb_dashboard_home"].verify_sustainability_menu_btn()

    def verify_ecp_command_center_dashboard(self, timeout=10):
        self.fd["ecp_home"].verify_command_center_header(timeout=timeout)
        self.fd["ecp_home"].verify_dashboard_menu_btn()
        self.fd["ecp_home"].verify_home_menu_btn()
        self.fd["ecp_home"].verify_devices_menu_btn()
        self.fd["ecp_home"].click_devices_menu_btn()
        self.fd["devices"].verify_device_page_content()
        # remove comment when PSPECP-3642 is fixed
        #self.fd["devices"].verify_and_click_online_printer()
    
    def remove_printer(self, printer_info, biz, timeout=180):
        if isinstance(printer_info, dict):
            ows_utility.remove_printer(printer_info['serial_number'])
            time.sleep(timeout) # Adding time delay to avoid 500 server error. wpp api will block calls if too many api calls done frequently.
        else:
            self.fd["smb_dashboard_home"].verify_printer_widget_title()
            self.fd["smb_dashboard_home"].click_printer_device_status_icon()
            self.fd["smb_printers_tab"].verify_printer_status()
            self.fd["smb_printers_tab"].click_printer_action_dropdown()
            self.fd["smb_printers_tab"].verify_printer_action_dropdown_options()
            self.fd["smb_printers_tab"].click_remove_printer_action()
            self.fd["smb_printers_tab"].verify_remove_printer_modal()
            self.fd["smb_printers_tab"].click_checkmark_printer_opted_out_of_privacy()
            self.fd["smb_printers_tab"].click_checkmark_users_no_longer_access_printer()
            self.fd["smb_printers_tab"].click_remove_printer_button()
            if biz == "E2E":
                self.fd["smb_printers_tab"].verify_hp_plus_benefits_removed_modal()
                self.fd["smb_printers_tab"].click_hp_plus_benefits_remove_continue_button()
            self.fd["smb_printers_tab"].verify_no_printer_added_message(timeout=60) # Sometime removing printer from Dashboard takes time

    def verify_organization_name_from_smb_dashboard_account_tab(self, organization_name):
        self.fd["smb_dashboard_home"].click_account_menu_btn()
        self.fd["smb_dashboard_account"].click_account_profile_tab()
        self.fd["smb_dashboard_account"].click_organization_tab()
        if self.fd["smb_dashboard_account"].get_organization_name() not in organization_name:
            raise ValueError("Organization name is not same as selected in assign printer owner page")
    
    def verify_printer_connected_status_and_printer_name(self):
        self.fd["smb_dashboard_home"].verify_status_widget_title()
        assert self.fd["smb_dashboard_home"].get_status_widget_connected_printer_count() == 1
        self.fd["smb_dashboard_home"].verify_printer_widget_section()
        if self.fd["smb_dashboard_home"].get_printer_name(timeout=15) != "abcdefghijklmnopqrstuvwxyz123456":
            raise AssertionError("printer name mismatch")
        if self.fd["smb_dashboard_home"].get_printer_location() != "123456abcdefghijklmnopqrstuvwxyz":
            raise AssertionError("Printer Location Mismatch")

    def navigate_users_tab_and_invite(self, invite_email):
        self.fd["smb_dashboard_home"].click_users_menu_btn() #qa.mobiauto+2024_08_29_15_06_44_05NGKC@gmail.com, qa.mobiauto+2024_09_04_16_06_33_31578K@gmail.com
        self.fd["smb_dashboard_users"].verify_users_page()
        self.fd["smb_dashboard_users"].verify_invite_btn()
        self.fd["smb_dashboard_users"].click_invite_button()
        self.fd["smb_dashboard_users"].verify_invite_users_section()
        self.fd["smb_dashboard_users"].enter_emails_to_invite_txt_box(invite_email)
        self.fd["smb_dashboard_users"].click_send_invitation_button()
        self.fd["smb_dashboard_users"].users_table_data_checkbox_load()
        self.fd["smb_dashboard_users"].verify_is_invited_user_display_in_user_table(users=[invite_email], role="user")
    
    def get_invite_link_from_email_and_launch(self, invite_email, browser_type):
        sent_time = round(time.time()) - 30
        url = self.fd["gmail_api"].get_content_from_email(self.fd["gmail_const"].INVITATION_EMAIL, invite_email, since=sent_time)
        self.clear_browsing_data_and_relaunch_flow(browser_type, url=url)
    
    def navigate_users_tab_and_verify_users(self, invitee_email, primary_account):
        self.fd["smb_dashboard_home"].click_users_menu_btn()
        self.fd["smb_dashboard_users"].verify_users_page()
        self.fd["smb_dashboard_users"].verify_invite_btn()
        self.fd["smb_dashboard_users"].users_table_data_checkbox_load()
        self.fd["smb_dashboard_users"].verify_is_invited_user_display_in_user_table(users=[invitee_email], role="Admin")
        self.fd["smb_dashboard_users"].verify_is_invited_user_display_in_user_table(users=[primary_account], role="Admin")
        
    def logout_from_dashboard_and_login_to_verify_invitee_status(self, invite_email, biz, username, password):    
        self.fd["smb_dashboard_home"].click_user_icon_top_right_txt()
        self.fd["smb_dashboard_home"].verify_profile_menu_conatiner() 
        self.fd["smb_dashboard_home"].logout()
        time.sleep(3)
        self.fd["hpid"].login(username, password)
        self.verify_smb_dashboard(biz)
        self.fd["smb_dashboard_home"].click_users_menu_btn()
        self.fd["smb_dashboard_users"].verify_users_page()
        self.fd["smb_dashboard_users"].verify_invite_btn()
        self.fd["smb_dashboard_users"].users_table_data_checkbox_load()
        assert self.fd["smb_dashboard_users"].get_user_status(invite_email) == "Active", "user status did not change to Active"
    
    def ecp_finish_setup_page_and_command_center(self):
        self.fd["ecp"].verify_ecp_finish_setup_page()
        self.fd["ecp"].click_connect_to_partner_button()
        self.navigate_partner_link_page()
        self.fd["ecp"].click_command_center_btn_partner_link_page()
        self.fd["ecp"].verify_command_center_login_page()
    
    def single_functionality_printer_set_up(self):
        self.set_up_print_test_page()
        self.invite_users_and_admins()

    def muilt_functionility_printer_set_up(self):
        self.set_up_print_test_page()
        self.set_up_scan_destinations()
        self.set_up_fax()
        self.invite_users_and_admins()
    
    def set_up_print_test_page(self):
        self.fd["poobe"].verify_set_up_print_send_test_page()
        self.fd["poobe"].click_set_up_print_send_test_page_btn()
        self.fd["poobe"].verify_set_up_print_overlay_page()
        self.fd["poobe"].verify_install_print_driver_btn()
        self.fd["poobe"].verify_already_have_driver_btn()
        self.fd["poobe"].click_already_have_driver_btn()
        self.fd["poobe"].verify_first_print_button()
        self.fd["poobe"].click_done_btn()

    def set_up_scan_destinations(self):
        self.fd["poobe"].verify_set_up_and_scan_destination()
        self.fd["poobe"].click_set_up_scan_destinations_btn()
        self.fd["poobe"].verify_set_up_scan_overlay_screen()
        self.fd["poobe"].verify_scan_to_email_section()
        self.fd["poobe"].verify_scan_to_cloud_section()
        self.fd["poobe"].click_done_btn()

    def clear_browsing_data_and_relaunch_flow(self, browser, url=False):
        if browser == "chrome":
            self.fd["poobe"].clear_chrome_browsing_data()
        if browser == "firefox":
            self.fd["poobe"].clear_browser_data_firefox()
        if browser == "edge":
            self.fd["poobe"].clear_edge_browsing_data()
        if url:
            self.driver.navigate(url)
        else:
            self.driver.navigate(self.fd["poobe"].poobe_url)
            self.fd["hpid"].handle_privacy_popup()

    def enroll_in_instant_ink(self):
        self.fd["instant_ink_value_prop"].click_continue_btn(timeout=40)
        self.fd["instant_ink_value_prop"].click_continue_on_automatic_printer_updates()
        self.fd["instant_ink_value_prop"].verify_enroll_instant_ink_page()
        self.fd["shipping"].click_add_shipping_btn()
        self.fd["shipping"].verify_shipping_overlay_modal()
        self.fd["shipping"].verify_shipping_page_load()
        self.fd["shipping"].load_address(self.fd["poobe"].locale)
        self.fd["shipping"].save_shipping_address()
        time.sleep(3) # Adding hard wait as Sometimes the Page takes couple of seconds to completely close shiping overlay modal and fully loading main page.
        self.fd["billing"].click_add_billing_btn()
        self.fd["billing"].verify_billing_overlay_modal()
        self.fd["billing"].click_continue_btn(change_check={"wait_obj":"creditcard_iframe"})
        self.fd["billing"].load_card_details(cardtype="visa")
        self.fd["instant_ink_value_prop"].click_continue_btn(clickable=True, timeout=60) # Some test fail due to timeout exception
        self.fd["instant_ink_value_prop"].handle_automatic_renewal_notice()
        self.fd["poobe"].verify_toner_is_on_the_way_page()
        self.fd["instant_ink_value_prop"].click_continue_btn()


    def verify_get_help_connectivity_content(self):
        self.fd["traffic_director"].click_get_help_connectivity_subtab_content()
        self.fd["traffic_director"].verify_software_unable_to_find_printer_content()
        self.fd["traffic_director"].verify_stay_near_the_printer()
        self.fd["traffic_director"].click_stay_near_the_printer()
        self.fd["traffic_director"].verify_stay_near_the_printer_content()
        self.fd["traffic_director"].verify_disconnect_from_vpn_drop_down()
        self.fd["traffic_director"].click_disconnect_from_vpn_drop_down()
        self.fd["traffic_director"].verify_disconnect_from_vpn_content()
        self.fd["traffic_director"].verify_turn_on_bluetooth_and_location_drop_down()
        self.fd["traffic_director"].click_turn_on_bluetooth_and_location_drop_down()
        self.fd["traffic_director"].verify_turn_on_bluetooth_and_location_content()
        self.fd["traffic_director"].verify_turn_on_wifi_during_setup()
        self.fd["traffic_director"].click_turn_on_wifi_during_setup()
        self.fd["traffic_director"].verify_turn_on_wifi_during_setup_content()
        self.fd["traffic_director"].click_software_unable_to_find_printer_content()
        self.fd["traffic_director"].click_stay_near_the_printer()
        self.fd["traffic_director"].click_disconnect_from_vpn_drop_down()
        self.fd["traffic_director"].click_turn_on_bluetooth_and_location_drop_down()
        self.fd["traffic_director"].click_turn_on_wifi_during_setup()        
        assert self.fd["traffic_director"].verify_software_unable_to_find_printer_content(raise_e=False) is False, "software unable to find printer content still shown"
        assert self.fd["traffic_director"].verify_stay_near_the_printer_content(raise_e=False) is False, "stay near the printer content still shown"
        assert self.fd["traffic_director"].verify_disconnect_from_vpn_content(raise_e=False) is False, "Disconnect from VPN during setup content still shown"        
        assert self.fd["traffic_director"].verify_turn_on_bluetooth_and_location_content(raise_e=False) is False, "Turn on Bluetooth and location content still shown"       
        assert self.fd["traffic_director"].verify_turn_on_wifi_during_setup_content(raise_e=False) is False, "Turn on Wi-Fi during setup content still shown"
    
    def verify_hp_support_button_on_get_help_btn(self):
        self.fd["traffic_director"].verify_hp_support_button_tab()
        self.fd["traffic_director"].click_hp_support_button_tab()
        self.fd["traffic_director"].verify_hp_support_product_page()
        self.fd["traffic_director"].verify_help_initial_setup()
        self.fd["traffic_director"].click_hp_support_product_page()
        self.driver.add_window("product_support")
        self.driver.switch_window("product_support")
        if "support.hp.com" not in self.driver.current_url:
            raise AssertionError("Expecting: " + "support.hp.com" + " got: " + self.driver.current_url)
        self.driver.close_window("product_support")
        self.fd["traffic_director"].click_help_initial_setup()
        self.driver.add_window("initial_setup")
        self.driver.switch_window("initial_setup")
        if "printer-setup" not in self.driver.current_url: # duplicate beacuse design has not updated on this urls yet
            raise AssertionError("Expecting: " + "Printer-Setup" + " got: " + self.driver.current_url)
        self.driver.close_window("initial_setup")
    
    def verify_traffic_director_country_language_step(self):
        self.fd["td_live_ui"].fd["Country_Language_td"].verify_web_page()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='1')
        self.fd["td_live_ui"].fd["Country_Language_td"].verify_header_title()
        self.fd["td_live_ui"].fd["Country_Language_td"].verify_country_language_card()
        self.fd["traffic_director"].verify_footer_live_ui_steps()

    def verify_traffic_director_load_paper_step(self):
        self.fd["td_live_ui"].fd["Load_paper_td"].verify_web_page()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='1')
        self.fd["traffic_director"].verify_footer_live_ui_steps()

    def verify_traffic_director_load_ink_step(self):
        self.fd["td_live_ui"].fd["load_ink_td"].verify_web_page()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='2')
        self.fd["td_live_ui"].fd["load_ink_td"].verify_install_ink_step_td()
        self.fd["traffic_director"].verify_footer_live_ui_steps()

    def verify_traffic_director_print_alignment_step(self):
        self.fd["td_live_ui"].fd["print_calibration"].verify_web_page()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='3')
        self.fd["td_live_ui"].fd["print_calibration"].verify_print_alignment_step()
        self.fd["traffic_director"].verify_footer_live_ui_steps()
    
    def verify_traffic_director_scan_alignment_step(self):
        self.fd["td_live_ui"].fd["scan_calibration"].verify_web_page()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='3')
        self.fd["td_live_ui"].fd["scan_calibration"].verify_scan_alignment_step()
        self.fd["traffic_director"].verify_footer_live_ui_steps()

    def verify_traffic_director_printer_use_setp(self):
        self.fd["td_live_ui"].fd["printer_use"].verify_web_page()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='5')
        self.fd["td_live_ui"].fd["printer_use"].verify_printer_use_step()
        self.fd["traffic_director"].verify_next_btn(raise_e=False)

    def verify_traffic_director_setup_checklist_step(self, personal=False):
        self.fd["td_live_ui"].fd["setup_checklist"].verify_web_page()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='6')
        self.fd["td_live_ui"].fd["setup_checklist"].verify_checklist_page(personal=personal)
        self.fd["traffic_director"].verify_footer_live_ui_steps()
        self.fd["traffic_director"].verify_next_btn()

    def verify_traffic_director_printer_network_page(self):
        self.fd["td_live_ui"].fd["hp_software"].verify_printer_network_page()
        self.fd["td_live_ui"].fd["hp_software"].verify_printer_network_card_image()
        self.fd["td_live_ui"].fd["hp_software"].verify_printer_network_card_instruction()
        self.fd["td_live_ui"].fd["hp_software"].verify_already_connected_to_network_btn()
        self.fd["td_live_ui"].fd["hp_software"].verify_web_page(sub_url="printer-network")

    def verify_personal_use_hp_software_step(self):
        self.fd["td_live_ui"].fd["hp_software"].verify_web_page()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='7')
        self.fd["td_live_ui"].fd["hp_software"].verify_personal_use_hp_software_page()
        
    
    def delete_email_from_main_account(self, email_to, email_from):
        msg_id = self.fd["gmail_api"].search_for_messages(q_to=email_to, q_from=email_from, q_unread=True)
        if msg_id != False:
            self.fd["gmail_api"].delete_email(msg_id)

    def add_translations_to_app_strings(self,page, biz, append=False):
        spec_key = biz+"_"+self.endpoint
        locale = self.driver.session_data["language"].lower()+"-"+self.driver.session_data["locale"].upper()
        file_name = ma_misc.web_localization_path_builder(self.driver, self.file_key["portal_oobe"][page][spec_key])
        file_name = file_name.replace("bg-BG", locale)
        try:
            spec_data = self.fd["poobe"].get_key_modified_dictionary_from_spec(file_name)
            self.driver.load_app_strings(pytest.app_info, spec_data, append=append)
        except FileNotFoundError:
            logging.warning("File not found: "+file_name)

    def load_spec_json(self, printer_profile, page_step):
        file_path = ma_misc.web_localization_path_builder(self.driver, self.file_key['psw']['animation_json'][printer_profile+'_'+page_step])
        spec_animation = json.load(open(file_path, 'r'))
        spec_json_file_name = os.path.basename(file_path)
        return spec_animation, spec_json_file_name

    def get_printer_oid_and_program(self, sku):
        file_name = ma_misc.web_localization_path_builder(self.driver, "web_localized_strings/PrinterModel.csv")
        rows = ma_misc.read_csv_file(file_name)
        for row in rows:
            if sku in row['modelNumber']:
                return row['oid'], row['programs']

    def load_all_printer_animations(self, printer_profile):
        """
        Load all animation JSON files for a specific printer.
        Returns dict with {filename: json_data} as key-value pairs.
        """
        all_animations = {}
        
        # Get file paths for this printer from spec_key
        try:
            file_paths = self.file_key['psw']['animation_json'][printer_profile]
        except KeyError:
            raise ValueError(f"Printer '{printer_profile}' not found in spec_key")
        
        # Load each file for this printer
        for file_path in file_paths:
            try:
                # Build full path
                full_path = ma_misc.web_localization_path_builder(self.driver, file_path)
                
                # Get filename
                file_name = os.path.basename(full_path)
                
                # Load JSON
                with open(full_path, 'r') as f:
                    json_data = json.load(f)
                
                # Store as {filename: json_data}
                all_animations[file_name] = json_data
                print(f"✓ Loaded: {file_name}")
            
            except FileNotFoundError:
                print(f"✗ File not found: {file_path}")
            except json.JSONDecodeError:
                print(f"✗ Invalid JSON: {file_path}")
            except Exception as e:
                print(f"✗ Error loading {file_path}: {e}")
        
        return all_animations