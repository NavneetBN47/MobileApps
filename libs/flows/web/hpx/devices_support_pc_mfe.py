from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class DevicesSupportPCMFE(HPXFlow):
    flow_name = "devices_support_pc_mfe"

    def verify_support_card(self, displayed=True):
        return self.driver.wait_for_object("support_card", displayed=displayed, raise_e=False, timeout=30) is not False
    
    def send_key_to_support_card(self):
        el = self.driver.wait_for_object("support_card", displayed=False)
        el.send_keys(Keys.F5)

    def verify_start_virtual_assist_btn(self):
        return self.driver.wait_for_object("start_virtual_assist_btn", displayed=False, raise_e=False, timeout=60) is not False

    def click_start_virtual_assist_btn(self):
        # self.driver.click("start_virtual_assist_btn", change_check={"wait_obj":"endsession_btn", "invisable":False}, retry=5, displayed=False, timeout=20)
        self.driver.click("start_virtual_assist_btn", displayed=False, timeout=20)

    def verify_endsession_btn(self):
        return self.driver.wait_for_object("endsession_btn", raise_e=False, timeout=20) is not False

    def click_endsession_btn(self):
        self.driver.click("endsession_btn", timeout=20)

    def verify_endsession_btn_enabled(self):
        return self.driver.wait_for_object("endsession_btn", displayed=False, raise_e=False, timeout=20).get_attribute("IsEnabled") == "true"

    def click_close_btn(self):
        self.driver.click("close_btn", timeout=20)
    
    def click_keep_on_btn(self):
        self.driver.click("keep_on_btn", timeout=20)

    def click_keep_open_btn(self):
        self.driver.click("keep_open_btn", timeout=20)

    def click_start_new_btn(self):
        self.driver.click("start_new_btn", timeout=20)

    def click_manual_guided_btn(self):
        self.driver.click("manual_guided_btn", displayed=False, timeout=20)

    def verify_manual_guided_btn(self):
        return self.driver.wait_for_object("manual_guided_btn", displayed=False, raise_e=False, timeout=20)

    def verify_hp_service_with_wechat_btn(self):
        return self.driver.wait_for_object("hp_service_with_wechat", displayed=False, raise_e=False, timeout=20)

    def click_hp_service_with_wechat_btn(self):
        self.driver.click("hp_service_with_wechat", displayed=False, timeout=20)
    
    def get_hp_service_list(self):
        self.driver.wait_for_object("hp_support_service_list", displayed=False, timeout=20)
        return self.driver.find_object("hp_support_service_list", multiple=True)

    def verify_redirect_failure_text(self):
        return self.driver.wait_for_object("redirect_failure_text", displayed=False, raise_e=False, timeout=20) is not False

    def click_redirect_failure_confirm_btn(self):
        self.driver.click("redirect_failure_confirm_btn", displayed=False, timeout=20)

    def click_service_center_btn(self):
        self.driver.click("service_center_btn", displayed=False, timeout=20)

    def click_find_repair_center_btn(self):
        self.driver.click("find_repair_center_btn", displayed=False, timeout=20)

    def verify_find_repair_center_btn(self):
        return self.driver.wait_for_object("find_repair_center_btn", displayed=False, raise_e=False, timeout=20)

    def click_virtual_repair_center_btn(self):
        self.driver.click("virtual_repair_center_btn", displayed=False, timeout=20)

    def verify_virtual_repair_center_btn(self):
        return self.driver.wait_for_object("virtual_repair_center_btn", displayed=False, raise_e=False, timeout=20)

    def click_product_support_center_btn(self):
        self.driver.click("product_support_center_btn", displayed=False, timeout=20)

    def verify_product_support_center_btn(self):
        return self.driver.wait_for_object("product_support_center_btn", displayed=False, raise_e=False, timeout=20)

    def get_product_support_center_btn_text(self):
        return self.driver.get_attribute("product_support_center_btn", "text", displayed=False, timeout=20)

    def click_warranty_dispute_btn(self):
        self.driver.click("warranty_dispute_btn", displayed=False, timeout=20)

    def verify_contact_us_panel(self):
        return self.driver.wait_for_object("contact_us_panel", displayed=False, raise_e=False, timeout=60) is not False

    def verify_contact_us_btn(self):
        return self.driver.wait_for_object("contact_us_btn", displayed=False, raise_e=False, timeout=60) is not False

    def click_contact_us_btn(self):
        self.driver.click("contact_us_btn",  displayed=False, timeout=20)

    def click_community_btn(self):
        self.driver.click("community_btn",  timeout=20)

    def verify_community_btn(self):
        return self.driver.wait_for_object("community_btn", displayed=False, raise_e=False, timeout=20)

    def click_kakaotalk_btn(self):
        self.driver.click("kakaotalk_button",  timeout=20)

    def click_webchat_btn(self):
        self.driver.click("webchat_button",  timeout=20)

    def click_zalo_btn(self):
        self.driver.click("zalo_button",  timeout=20)

    def click_line_btn(self):
        self.driver.click("line_button",  timeout=20)

    def click_whatsapp_btn(self):
        self.driver.click("whatsapp_button",  timeout=20)

    def click_twitter_btn(self):
        self.driver.click("twitter_button",  timeout=20)

    def click_chat_agent_btn(self):
        self.driver.click("chat_agent_btn",  timeout=20)

    def verify_chat_agent_btn(self):
        return self.driver.wait_for_object("chat_agent_btn", displayed=False, raise_e=False, timeout=20)

    def click_smart_friend_btn(self):
        self.driver.click("smart_friend_btn",  timeout=20)

    def click_speak_agent_btn(self):
        self.driver.click("speak_agent_btn",  timeout=20)

    def verify_speak_agent_btn(self):
        return self.driver.wait_for_object("speak_agent_btn", displayed=False, raise_e=False, timeout=20)

    def click_hardware_issue_btn(self):
        self.driver.click("hardware_issue_btn",  timeout=20)

    def verify_hardware_issue_btn(self):
        return self.driver.wait_for_object("hardware_issue_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_instant_ink_issue_btn(self):
        self.driver.click("instant_ink_issue_btn",  timeout=20)
    
    def verify_instant_ink_issue_btn(self):
        return self.driver.wait_for_object("instant_ink_issue_btn", displayed=False, raise_e=False, timeout=20) is not False

    def verify_phone_page_title(self):
        return self.driver.wait_for_object("phone_page_title", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_create_case_profile_name(self):
        return self.driver.wait_for_object("create_case_profile_name", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_chat_page_title(self):
        return self.driver.wait_for_object("chat_page_title", displayed=False, raise_e=False, timeout=20) is not False
    
    def get_chat_page_title(self):
        return self.driver.get_attribute("chat_page_title", "text", displayed=False, timeout=20)
    
    def verify_warranty_page_title(self):
        return self.driver.wait_for_object("warranty_page_title", displayed=False, raise_e=False, timeout=20) is not False

    def click_back_btn(self):
        self.driver.click("back_btn", change_check={"wait_obj":"back_btn", "invisible":True}, timeout=20)

    def verify_warranty_detail_btn(self):
        return self.driver.wait_for_object("warranty_detail_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_warranty_detail_btn(self):
        self.driver.click("warranty_detail_btn",  displayed=False, timeout=20)

    def click_sign_in_btn(self):
        self.driver.click("sign_in_btn", timeout=20)

    def verify_support_option(self):
        return self.driver.wait_for_object("support_option", raise_e=False, timeout=20) is not False
    
    def send_key_to_support_option(self):
        el = self.driver.wait_for_object("support_option", displayed=False)
        el.send_keys(Keys.F5)
        
    def select_support_option(self):
        self.driver.click("support_option", timeout=20)

    def select_settings_option(self):
        self.driver.click("settings_option", timeout=20)

    def click_signout_btn(self):
        self.driver.click("signout_btn", displayed = False, timeout=20)

    def verify_add_device_btn(self):
        return self.driver.wait_for_object("add_device_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_add_device_btn(self):
        self.driver.click("add_device_btn", timeout=20)

    def get_add_device_btn_text(self):
        return self.driver.get_attribute("add_device_btn", "text", displayed=False, timeout=20)

    def send_keys(self, edit, text):
        self.driver.send_keys(edit, text)    

    def click_send_btn(self):
        self.driver.click("send_btn", timeout=20)

    def send_key_to_virtual_agent(self):
        el = self.driver.wait_for_object("send_btn", displayed=False)
        el.send_keys(Keys.F5)

    def verify_va_message(self, msg):
        return self.driver.wait_for_object("va_msg", format_specifier=[msg], raise_e=False, timeout=60) is not False

    def click_va_message(self, msg):
        self.driver.click("va_msg", format_specifier=[msg], displayed=False, timeout=20)

    def get_va_message(self, msg):
        return self.driver.wait_for_object("va_msg", format_specifier=[msg], displayed = False, raise_e=False, timeout=60).get_attribute("Value.Value")

    def click_startover_link(self):
        self.driver.click("startover_link", displayed=False, timeout=20)

    def click_feedback_link(self):
        self.driver.click("feedback_link", timeout=20)

    def verify_feedback_link(self):
        return self.driver.wait_for_object("feedback_link", displayed=False, raise_e=False, timeout=20) is not False

    def click_privacy_link(self):
        self.driver.click("privacy_link", timeout=20)
    
    def verify_privacy_link(self):
        return self.driver.wait_for_object("privacy_link", displayed=False, raise_e=False, timeout=20) is not False

    def verify_device_list(self):
        return self.driver.wait_for_object("device_cards", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_support_device(self):
        return self.driver.wait_for_object("support_device_card", displayed=False, raise_e=False, timeout=20) is not False

    def get_device_list(self):
        self.verify_device_list()
        return self.driver.find_object("device_cards", multiple=True)

    def get_support_device_card(self):
        self.verify_support_device()
        return self.driver.find_object("support_device_card", multiple=True)
    
    def get_support_device_list_title(self):
        return self.driver.get_attribute("support_device_list_title", "text", displayed=False, timeout=20)
    
    def verify_support_link(self):
        return self.driver.wait_for_object("support_link", displayed=False, raise_e=False, timeout=20) is not False

    def click_support_device_card(self, index=0):
        self.driver.click("support_device_card", format_specifier=[index], timeout=20)
    
    def select_my_hp_account_btn(self):
        self.driver.click("sign_in_button", timeout=30)

    def verify_back_btn_devices_title_visible(self):
        return self.driver.wait_for_object("back_btn", displayed=False, raise_e=False, timeout=20) is not False

    def verify_devices_title(self):
        return self.driver.get_attribute("back_btn_title","Name", timeout = 20)
    
    def click_device_add_btn(self):
        self.driver.click("device_add_btn", displayed=False, timeout=20)

    def get_add_device_page_title(self):
        return self.driver.get_attribute("add_device_page_title", "text", displayed=False, timeout=20)

    def click_profile_button(self):
        time.sleep(5)
        self.driver.click("top_profile_button", change_check={"wait_obj":"feedback_btn", "invisible":False}, displayed=False, timeout=10)

    def click_profile_sign_in_button(self):
        self.driver.click("top_profile_sign_in_button", timeout=10)

    def verify_country_list(self):
        return self.driver.wait_for_object("country_dropdown", displayed=False, raise_e=False, timeout=20) is not False

    def click_country_list(self):
        # self.driver.click("country_dropdown", change_check={"wait_obj":"country_list", "invisible":False}, timeout=20)
        self.driver.click("country_dropdown", timeout=20)

    def select_country(self, country_index):
        self.driver.click("country_index", displayed=False, format_specifier=[country_index])

    def select_country_by_country_name(self, country_name=None):
        self.driver.wait_for_object("country_option", displayed=False, format_specifier=[country_name]).click()

    def get_country(self):
        return self.driver.wait_for_object("country_dropdown", raise_e=False, timeout=10).get_attribute("Name")
    
    def verify_va_message_contains(self, msg):
        return self.driver.wait_for_object("va_msg_contains", format_specifier=[msg], displayed=False, raise_e=False, timeout=60) is not False
    
    def verify_warranty_info(self):
        return self.driver.wait_for_object("warranty_status_text", displayed=False, raise_e=False, timeout=20) is not False
    
    def get_warranty_status(self):
        return self.driver.get_attribute("warranty_status_text", "text", displayed=False, timeout=20)

    def get_sign_in_to_view_coverage_status_text(self):
        return self.driver.get_attribute("sign_in_to_view_coverage_status_text", "text", displayed=False, timeout=20)

    def click_sign_in_to_view_coverage_status_text(self):
        self.driver.click("sign_in_to_view_coverage_status_text", displayed=False, timeout=20)  

    def get_subscription_info(self):
        return self.driver.get_attribute("subscription_info_text", "text", displayed=False, timeout=20)

    def get_subscription_not_associated_text(self):
        return self.driver.get_attribute("subscription_not_associated_text", "text", displayed=False, timeout=20)

    def click_otherspc_btn(self):
        self.driver.click("otherspc_btn", displayed=False, timeout=20)

    def click_vashowlesspc_btn(self):
        self.driver.click("vashowlesspc_btn", displayed=False, timeout=20)

    def click_vashowmorepc_btn(self):
        self.driver.click("vashowmorepc_btn", timeout=20)

    def verify_otherpc_btn(self):
        return self.driver.wait_for_object("otherspc_btn", displayed=False, raise_e=False, timeout=20) is not False

    def verify_computerisslow_btn(self):
        return self.driver.wait_for_object("computerisslow_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_displayortouchissue_btn(self):
        return self.driver.wait_for_object("displayortouchissue_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_keyboardmousesettings_btn(self):
        return self.driver.wait_for_object("keyboardmousesettings_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_restorecomputersettings_btn(self):
        return self.driver.wait_for_object("restorecomputersettings_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_nosound_btn(self):
        return self.driver.wait_for_object("nosound_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_connectivityissue_btn(self):
        return self.driver.wait_for_object("connectivityissue_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_computerlocksorfreezes_btn(self):
        return self.driver.wait_for_object("computerlocksorfreezes_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_windowssupport_btn(self):
        return self.driver.wait_for_object("windowssupport_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_computerwillnotstart_btn(self):
        return self.driver.wait_for_object("computerwillnotstart_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_cannotlogincomputer_btn(self):
        return self.driver.wait_for_object("cannotlogincomputer_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_storgageissue_btn(self):
        return self.driver.wait_for_object("storgageissue_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_cannotconnectprinter_btn(self):
        return self.driver.wait_for_object("cannotconnectprinter_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def click_computerisslow_btn(self):
        self.driver.click("computerisslow_btn", displayed=False, timeout=20)

    def click_displayortouchissue_btn(self):
        self.driver.click("displayortouchissue_btn", displayed=False, timeout=20)

    def click_keyboardmousesettings_btn(self):  
        self.driver.click("keyboardmousesettings_btn", displayed=False, timeout=20)

    def click_restorecomputersettings_btn(self):
        self.driver.click("restorecomputersettings_btn", displayed=False, timeout=20)

    def click_nosound_btn(self):
        self.driver.click("nosound_btn", displayed=False, timeout=20)

    def click_connectivityissue_btn(self):
        self.driver.click("connectivityissue_btn", displayed=False, timeout=20)

    def click_computerlocksorfreezes_btn(self):
        self.driver.click("computerlocksorfreezes_btn", displayed=False, timeout=20)

    def click_windowssupport_btn(self):
        self.driver.click("windowssupport_btn", displayed=False, timeout=20)

    def click_computerwillnotstart_btn(self):
        self.driver.click("computerwillnotstart_btn", displayed=False, timeout=20)

    def click_cannotlogincomputer_btn(self):
        self.driver.click("cannotlogincomputer_btn", displayed=False, timeout=20)

    def click_storgageissue_btn(self):
        self.driver.click("storgageissue_btn", displayed=False, timeout=20)

    def click_cannotconnectprinter_btn(self):
        self.driver.click("cannotconnectprinter_btn", displayed=False, timeout=20)

    def get_profile_email(self):
        return self.driver.wait_for_object("create_case_profile_email_input", raise_e=False, timeout=20).text
    
    def click_issue_type_selector(self):
        self.driver.click("issue_type_selector", timeout=10)

    def verify_issue_type_option(self):
        return self.driver.wait_for_object("issue_type_option", displayed=True, raise_e=False, timeout=20) is not False

    def get_issue_type_option_count(self):
        self.verify_issue_type_option()
        return len(self.driver.find_object("issue_type_option", multiple=True))
    
    def select_issue_type_option_by_index(self, index):
        self.verify_issue_type_option()
        self.driver.click("issue_type_option", index, timeout=10)

    def verify_get_phone_number_btn_enabled(self):
        return self.driver.wait_for_object("get_phone_number_btn", displayed=False, raise_e=False, timeout=20).get_attribute("IsEnabled")
    
    def click_get_phone_number_btn(self):
        self.driver.click("get_phone_number_btn", displayed=False, timeout=20)

    def verify_input_issue_description(self):
        return self.driver.wait_for_object("issue_description_input", displayed=True, raise_e=False, timeout=20) is not False
    
    def input_issue_description(self, text):
        self.verify_input_issue_description()
        # Set focus before sending keys
        el = self.driver.wait_for_object("issue_description_input", displayed=True, timeout=20)
        el.click()  # Ensure the input is focused
        el.clear()  # Optional: clear existing text
        el.send_keys(text)

    def get_issue_description(self):
        return self.driver.wait_for_object("issue_description_input", timeout=20).get_attribute("Value.Value")
    
    def get_issue_description_tip(self):
        return self.driver.wait_for_object("issue_description_input", timeout=20).get_attribute("Name")
    
    def clear_issue_description(self):
        self.driver.clear_text("issue_description_input")

    def get_phone_number_text(self):
        return self.driver.wait_for_object("phone_number_text", raise_e=False, timeout=20).get_attribute("Name")
    
    def verify_chat_now_btn_enabled(self):
        return self.driver.wait_for_object("chat_now_btn", displayed=False, raise_e=False, timeout=20).get_attribute("IsEnabled") 
    
    def click_chat_now_btn(self):
        self.driver.click("chat_now_btn", timeout=30)

    def verify_phone_number_text(self):
        return self.driver.wait_for_object("phone_number_text", displayed=False, raise_e=False, timeout=20) is not False

    def verify_issue_type_text(self):
        return self.driver.wait_for_object("issue_type_text", displayed=False, raise_e=False, timeout=20) is not False 

    def verify_issue_description_text(self):
        return self.driver.wait_for_object("issue_type_description", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_case_history_title(self):
        return self.driver.wait_for_object("case_history_title", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_printer_setup_btn(self):
        return self.driver.wait_for_object("printer_setup_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def click_printer_setup_btn(self):
        self.driver.click("printer_setup_btn", displayed=False, timeout=20)

    def verify_printer_offline_btn(self):
        return self.driver.wait_for_object("printer_offline_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def click_printer_offline_btn(self):
        self.driver.click("printer_offline_btn", displayed=False, timeout=20)   

    def verify_printer_connectivity_issue_btn(self):
        return self.driver.wait_for_object("printer_connectivity_issue_btn", displayed=False, raise_e=False, timeout=20) is not False   
    
    def click_printer_connectivity_issue_btn(self):
        self.driver.click("printer_connectivity_issue_btn", displayed=False, timeout=20)

    def verify_printer_scanning_btn(self):
        return self.driver.wait_for_object("printer_scanning_btn", displayed=False, raise_e=False, timeout=20) is not False 

    def click_printer_scanning_btn(self):
        self.driver.click("printer_scanning_btn", displayed=False, timeout=20)

    def verify_printer_quality_btn(self):
        return self.driver.wait_for_object("printer_quality_btn", displayed=False, raise_e=False, timeout=20) is not False  

    def click_printer_quality_btn(self):
        self.driver.click("printer_quality_btn", displayed=False, timeout=20)   

    def verify_ink_cartridge_btn(self):
        return self.driver.wait_for_object("ink_cartridge_btn", displayed=False, raise_e=False, timeout=20) is not False    

    def click_ink_cartridge_btn(self):  
        self.driver.click("ink_cartridge_btn", displayed=False, timeout=20)

    def verify_print_job_stuck_in_queue_btn(self):
        return self.driver.wait_for_object("print_job_stuck_in_queue_btn", displayed=False, raise_e=False, timeout=20) is not False 

    def click_print_job_stuck_in_queue_btn(self):
        self.driver.click("print_job_stuck_in_queue_btn", displayed=False, timeout=20)  

    def verify_paper_jam_issue_btn(self):
        return self.driver.wait_for_object("paper_jam_issue_btn", displayed=False, raise_e=False, timeout=20) is not False  

    def click_paper_jam_issue_btn(self):    
        self.driver.click("paper_jam_issue_btn", displayed=False, timeout=20)

    def verify_others_printer_btn(self):
        return self.driver.wait_for_object("others_printer_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_others_printer_btn(self):   
        self.driver.click("others_printer_btn", displayed=False, timeout=20)

    def get_va_page_title(self):
        return self.driver.get_attribute("va_page_title", "Name", displayed=False, timeout=20)
    
    def click_va_show_less_printer_btn(self):
        self.driver.click("va_show_less_printer_btn", displayed=False, timeout=20)

    def click_va_show_more_printer_btn(self):
        self.driver.click("va_show_more_printer_btn", timeout=20)

    def verify_support_center_operating_hours_title(self):
        return self.driver.wait_for_object("support_center_operating_hours_title", displayed=False, raise_e=False, timeout=20) is not False
    
    def click_run_system_test_btn(self):
        self.driver.click("run_system_test_btn", displayed=False, timeout=20)

    def verify_run_system_test_btn(self):
        return self.driver.wait_for_object("run_system_test_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_check_audio_btn(self):
        self.driver.click("check_audio_btn", displayed=False, timeout=20)

    def verify_check_audio_btn(self):
        return self.driver.wait_for_object("check_audio_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_run_hardware_diagnostic_btn(self):
        self.driver.click("run_hardware_diagnostic_btn", displayed=False, timeout=20)
    
    def verify_run_hardware_diagnostic_btn(self):
        return self.driver.wait_for_object("run_hardware_diagnostic_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_audio_check_diagnostic_btn(self):
        return self.driver.wait_for_object("audio_check_diagnostic_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_audio_setting_check_audio_button(self):
        return self.driver.wait_for_object("audio_setting_check_audio_button", displayed=False, raise_e=False, timeout=20) is not False

    def verify_system_control_optimize_performance_button(self):
        return self.driver.wait_for_object("system_control_optimize_performance_button", displayed=False, raise_e=False, timeout=20) is not False

    def click_optimize_performance_btn(self):
        self.driver.click("optimize_performance_btn", displayed=False, timeout=20)

    def verify_optimize_performance_btn(self):
        return self.driver.wait_for_object("optimize_performance_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def click_aip_intents_btn(self):
        self.driver.click("aip_intents_btn", displayed=False, timeout=20)

    def get_aip_intents_btn_text(self):
        return self.driver.get_attribute("aip_intents_btn", "Name", displayed=False, timeout=20)

    def click_printer_intents_btn(self):
        self.driver.click("printer_intents_btn", displayed=False, timeout=20)
    
    def get_printer_intents_btn_text(self):
        return self.driver.get_attribute("printer_intents_btn", "Name", displayed=False, timeout=20)

    def click_instant_ink_btn(self):
        self.driver.click("instant_ink_btn", displayed=False, timeout=20)

    def click_what_is_instant_ink_plan_btn(self):
        self.driver.click("what_is_instant_ink_plan_btn", displayed=False, timeout=20)
    
    def click_cartridge_troubleshooting_btn(self):
        self.driver.click("cartridge_troubleshooting_btn", displayed=False, timeout=20)

    def click_change_credit_card_info_btn(self):
        self.driver.click("change_credit_card_info_btn", displayed=False, timeout=20)

    def click_my_bill_was_not_what_i_expected_btn(self):
        self.driver.click("my_bill_was_not_what_i_expected_btn", displayed=False, timeout=20)

    def click_page_count_explanations_btn(self):
        self.driver.click("page_count_explanations_btn", displayed=False, timeout=20)

    def click_account_related_errors_btn(self):
        self.driver.click("account_related_errors_btn", displayed=False, timeout=20)

    def click_print_quality_issues_btn(self):
        self.driver.click("print_quality_issues_btn", displayed=False, timeout=20)

    def click_connect_printer_message_btn(self):
        self.driver.click("connect_printer_message_btn", displayed=False, timeout=20)

    def click_cartridge_cannot_be_used_until_printer_is_enrolled_btn(self):
        self.driver.click("cartridge_cannot_be_used_until_printer_is_enrolled_btn", displayed=False, timeout=20)

    def click_instant_ink_change_shipping_address_btn(self):
        self.driver.click("instant_ink_change_shipping_address_btn", displayed=False, timeout=20)

    def click_change_to_a_different_plan_btn(self):
        self.driver.click("change_to_a_different_plan_btn", displayed=False, timeout=20)

    def click_trouble_logging_in_to_my_instant_ink_account_btn(self):
        self.driver.click("trouble_logging_in_to_my_instant_ink_account_btn", displayed=False, timeout=20)

    def click_show_more_instant_ink_btn(self):
        time.sleep(5)
        self.driver.click("show_more_instant_ink_btn", displayed=False, timeout=20)

    def click_what_is_hp_all_in_plan_btn(self):
        self.driver.click("what_is_hp_all_in_plan_btn", displayed=False, timeout=20)

    def verify_what_is_hp_all_in_plan_btn(self):
        return self.driver.wait_for_object("what_is_hp_all_in_plan_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def click_trouble_logging_in_btn(self):
        self.driver.click("trouble_logging_in_btn", displayed=False, timeout=20)

    def verify_trouble_logging_in_btn(self):
        return self.driver.wait_for_object("trouble_logging_in_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_change_email_btn(self):
        self.driver.click("change_email_btn", displayed=False, timeout=20)

    def verify_change_email_btn(self):
        return self.driver.wait_for_object("change_email_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_change_billing_info_btn(self):
        self.driver.click("change_billing_info_btn", displayed=False, timeout=20)

    def verify_change_billing_info_btn(self):
        return self.driver.wait_for_object("change_billing_info_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_change_shipping_address_btn(self):
        self.driver.click("change_shipping_address_btn", displayed=False, timeout=20)

    def verify_change_shipping_address_btn(self):
        return self.driver.wait_for_object("change_shipping_address_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_add_a_printer_btn(self):
        self.driver.click("add_a_printer_btn", displayed=False, timeout=20)

    def verify_add_a_printer_btn(self):
        return self.driver.wait_for_object("add_a_printer_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_where_is_my_paper_btn(self):
        self.driver.click("where_is_my_paper_btn", displayed=False, timeout=20)

    def verify_where_is_my_paper_btn(self):
        return self.driver.wait_for_object("where_is_my_paper_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_where_is_my_ink_btn(self):
        self.driver.click("where_is_my_ink_btn", displayed=False, timeout=20)

    def verify_where_is_my_ink_btn(self):
        return self.driver.wait_for_object("where_is_my_ink_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_account_error_message_btn(self):
        self.driver.click("account_error_message_btn", displayed=False, timeout=20)

    def verify_account_error_message_btn(self):
        return self.driver.wait_for_object("account_error_message_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_cancel_my_account_btn(self):
        self.driver.click("cancel_my_account_btn", displayed=False, timeout=20)

    def verify_cancel_my_account_btn(self):
        return self.driver.wait_for_object("cancel_my_account_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_others_aip_btn(self):
        self.driver.click("others_aip_btn", displayed=False, timeout=20)

    def verify_others_aip_btn(self):
        return self.driver.wait_for_object("others_aip_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_show_more_aip_btn(self):
        self.driver.click("show_more_aip_btn", displayed=False, timeout=20)

    def verify_show_more_aip_btn(self):
        return self.driver.wait_for_object("show_more_aip_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_show_less_aip_btn(self):
        self.driver.click("show_less_aip_btn", displayed=False, timeout=20)

    def verify_show_less_aip_btn(self):
        return self.driver.wait_for_object("show_less_aip_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_aip_help_with_plan_btn(self):
        self.driver.click("aip_help_with_plan_btn", displayed=False, timeout=20)

    def verify_aip_help_with_plan_btn(self):
        return self.driver.wait_for_object("aip_help_with_plan_btn", displayed=False, raise_e=False, timeout=20) is not False

    def click_aip_contact_us_btn(self):
        self.driver.click("aip_contact_us_btn", displayed=False, timeout=20)

    def verify_aip_contact_us_btn(self):
        return self.driver.wait_for_object("aip_contact_us_btn", displayed=False, raise_e=False, timeout=20) is not False
    
    def verify_contact_us_card(self):
        return self.driver.wait_for_object("contact_us_card", displayed=False, raise_e=False, timeout=20) is not False
    
    def click_va_minimize_btn(self):
        time.sleep(10)
        self.driver.find_object("va_minimize_btn", multiple=True)[1].click()

    def click_chat_minimize_btn(self):
        self.verify_chat_text_field()
        self.driver.find_object("va_minimize_btn", multiple=True)[3].click()

    def click_assistant_btn(self):
        self.driver.click("assistant_btn", displayed=True, timeout=20)

    def verify_assistant_btn(self):
        return self.driver.wait_for_object("assistant_btn", displayed=True, raise_e=False, timeout=20) is not False
    
    def verify_live_agent_btn(self):
        return self.driver.wait_for_object("live_agent_btn", displayed=True, raise_e=False, timeout=20) is not False
    
    def get_va_title(self):
        return self.driver.get_attribute("va_title", "Name", displayed=False, timeout=20)
    
    def verify_chat_text_field(self):
        return self.driver.wait_for_object("chat_text_field", displayed=False, raise_e=False, timeout=20) is not False
    
    def click_product_info_btn(self):
        self.driver.click("product_info_btn", displayed=False, timeout=60)

    def verify_product_info_btn(self):
        return self.driver.wait_for_object("product_info_btn", displayed=False, raise_e=False, timeout=20) is not False

    def verify_view_available_updates_btn(self):
        return self.driver.wait_for_object("view_available_updates_btn", displayed=False, raise_e=False, timeout=20) is not False

    def get_operatingsystem_info(self):
        return self.driver.get_attribute("operatingsystem_info", "Name", displayed=False, timeout=20)

    def get_microprocessor_info(self):
        return self.driver.get_attribute("microprocessor_info", "Name", displayed=False, timeout=20)

    def get_systemmemory_info(self):
        return self.driver.get_attribute("systemmemory_info", "Name", displayed=False, timeout=20)

    def get_memoryslot_info(self, index=1):
        return self.driver.get_attribute(f"memoryslot_info", "Name", format_specifier=[index], displayed=False, timeout=20)

    def get_systemboard_info(self):
        return self.driver.get_attribute("systemboard_info", "Name", displayed=False, timeout=20)

    def get_systembios_info(self):
        return self.driver.get_attribute("systembios_info", "Name", displayed=False, timeout=20)

    def get_video_device_info(self, index=1):
        return self.driver.get_attribute(f"video_device_info", "Name", format_specifier=[index], displayed=False, timeout=20)

    def get_video_device_resolution_info(self, index=1):
        return self.driver.get_attribute(f"video_device_resolution_info", "Name", format_specifier=[index], displayed=False, timeout=20)

    def get_video_device_refresh_rate_info(self, index=1):
        return self.driver.get_attribute(f"video_device_refresh_rate_info", "Name", format_specifier=[index], displayed=False, timeout=20)

    def get_video_device_version_info(self, index=1):
        return self.driver.get_attribute(f"video_device_version_info", "Name", format_specifier=[index], displayed=False, timeout=20)

    def get_audio_device_info(self, index=1):
        return self.driver.get_attribute(f"audio_device_info", "Name", format_specifier=[index], displayed=False, timeout=20)

    def get_audio_device_driver_info(self, index=1):
        return self.driver.get_attribute(f"audio_device_driver_info", "Name", format_specifier=[index], displayed=False, timeout=20)

    def get_audio_device_version_info(self, index=1):
        return self.driver.get_attribute(f"audio_device_version_info", "Name", format_specifier=[index], displayed=False, timeout=20)

    def verify_operatingsystem_info(self):
        return self.driver.wait_for_object("operatingsystem_info", displayed=False, raise_e=False, timeout=20) is not False

    def verify_microprocessor_info(self):
        return self.driver.wait_for_object("microprocessor_info", displayed=False, raise_e=False, timeout=20) is not False

    def verify_systemmemory_info(self):
        return self.driver.wait_for_object("systemmemory_info", displayed=False, raise_e=False, timeout=20) is not False

    def verify_memoryslot_info(self, index=1):
        return self.driver.wait_for_object(f"memoryslot_info", format_specifier=[index], displayed=False, raise_e=False, timeout=20) is not False

    def verify_systemboard_info(self):
        return self.driver.wait_for_object("systemboard_info", displayed=False, raise_e=False, timeout=20) is not False

    def verify_systembios_info(self):
        return self.driver.wait_for_object("systembios_info", displayed=False, raise_e=False, timeout=20) is not False

    def verify_video_device_info(self, index=1):
        return self.driver.wait_for_object(f"video_device_info", format_specifier=[index], displayed=False, raise_e=False, timeout=20) is not False

    def verify_video_device_resolution_info(self, index=1):
        return self.driver.wait_for_object(f"video_device_resolution_info", format_specifier=[index], displayed=False, raise_e=False, timeout=20) is not False

    def verify_video_device_refresh_rate_info(self, index=1):
        return self.driver.wait_for_object(f"video_device_refresh_rate_info", format_specifier=[index], displayed=False, raise_e=False, timeout=20) is not False

    def verify_video_device_version_info(self, index=1):
        return self.driver.wait_for_object(f"video_device_version_info", format_specifier=[index], displayed=False, raise_e=False, timeout=20) is not False

    def verify_audio_device_info(self, index=1):
        return self.driver.wait_for_object(f"audio_device_info", format_specifier=[index], displayed=False, raise_e=False, timeout=20) is not False

    def verify_audio_device_driver_info(self, index=1):
        return self.driver.wait_for_object(f"audio_device_driver_info", format_specifier=[index], displayed=False, raise_e=False, timeout=20) is not False

    def verify_audio_device_version_info(self, index=1):
        return self.driver.wait_for_object(f"audio_device_version_info", format_specifier=[index], displayed=False, raise_e=False, timeout=20) is not False
    
    def get_chat_with_agent_description(self):
        return self.driver.wait_for_object("chat_with_agent_description", raise_e=False, timeout=20).text
    
    def click_search_by_sn_button(self):
        self.driver.click("search_by_sn_button", timeout=30)

    def input_sn(self, text):
        el = self.driver.wait_for_object("enter_sn_edit", displayed=True, timeout=20)
        el.click()  # Ensure the input is focused
        el.clear()  # Optional: clear existing text
        # pyperclip.copy(text)
        el.send_keys(text)
        # el.send_keys(Keys.CONTROL, 'v')

    def click_add_device_link(self):
        self.driver.wait_for_object("add_device_link", displayed=True, clickable=True, timeout=60)
        time.sleep(5)
        self.driver.click("add_device_link")

    def return_nick_name_of_remote_device(self):
        return self.driver.get_attribute("remote_device_name", "Name", displayed=False, timeout=15)

    def verify_support_diagnostic_title(self):
        return self.driver.wait_for_object("support_diagnostics_title", displayed=False, raise_e=False, timeout=60) is not False

    def verify_specifications_button(self):
        return self.driver.wait_for_object("product_specifications_button", displayed=False, raise_e=False, timeout=60) is not False
    
    def click_back_devices_button(self):
        self.driver.click("back_devices_button_on_pc_devices_page", change_check={"wait_obj": "device_name", "invisible": False}, timeout=30)

    def get_device_name_by_back_devices_button(self):
        return self.driver.get_attribute("back_devices_button_on_pc_devices_page", "Name", displayed=False, timeout=20)

    def input_country_select_edit(self, text):
        el = self.driver.wait_for_object("support_country_select_edit", displayed=True, timeout=20)
        el.click()  # Ensure the input is focused
        el.clear()  # Optional: clear existing text
        el.send_keys(text)
    
    def get_country_select_edit_text(self):
        return self.driver.get_attribute("support_country_select_edit", "Name", displayed=False, timeout=20)
        
    def get_country_select_text(self):
        return self.driver.get_attribute("support_country_select_text", "Name", displayed=False, timeout=20)

    def click_link_need_help_sn(self):
        el = self.driver.wait_for_object("link_need_help_sn", displayed=True, timeout=20)
        self.driver.click_by_coordinates(el , el.rect['x'] + 1, el.rect['y'] + 1)
        # el.click()
        # offset_x = el.rect["width"] // 2
        # offset_y = 10
        # self.driver.click_by_coordinates(el , offset_x, offset_y)

    def verify_embargo_country_closed_btn(self):
        return self.driver.wait_for_object("embargo_country_closed_btn", displayed=False, raise_e=False, timeout=20) is not False

    def get_sn(self):
        return self.driver.get_attribute("copy_serial_number_btn", "Name", displayed=False, timeout=20)
    
    def verify_audio_control_card_show(self):
        return self.driver.wait_for_object("audio_control_card_lone_page", raise_e=False, displayed=False, timeout=10)
    
    def verify_display_control_lone_page(self):
        return self.driver.wait_for_object("display_control_card_lone_page", raise_e=False, displayed=False, timeout=10)

    def verify_system_control_lone_page_show(self):
        return self.driver.wait_for_object("system_control_card_lone_page", raise_e=False, displayed=False, timeout=10)

    def verify_wellbeing_card_lone_page_show(self):
        return self.driver.wait_for_object("wellbeing_card", raise_e=False, displayed=False, timeout=10)

    def verify_video_lone_page(self):
        return self.driver.wait_for_object("video_card_lone_page", raise_e=False, displayed=False, timeout=10)
    
    def verify_hppk_card_show_up(self):
        return self.driver.wait_for_object("hppk_card", raise_e=False, displayed=False, timeout=10)
    
    def click_audio_control_card(self):
        self.driver.click("audio_control_card_lone_page", timeout = 10)

    def click_display_control_lone_page(self):
        self.driver.click("display_control_card_lone_page", timeout=15)

    def click_system_control_card_lone_page(self):
        self.driver.click("system_control_card_lone_page", timeout = 10)

    def click_wellbeing_card(self):
        time.sleep(5)
        el = self.driver.wait_for_object("wellbeing_card", raise_e=False, timeout=10)
        el.send_keys(Keys.TAB)
        time.sleep(2)
        el.send_keys(Keys.ENTER)

    def click_video_card_lone_page(self):
        self.driver.click("video_card_lone_page", timeout=15)

    def click_hppk_card(self):
        return self.driver.click("hppk_card", timeout = 20)
    
    def click_minimize_btn(self):
        self.driver.click("minimize_btn", timeout=10)

    def click_maximize_btn(self):
        self.driver.click("maximize_btn", timeout=10)

    def right_click_device_card(self, index=0):
        el = self.driver.wait_for_object("device_card", format_specifier=[index], displayed=False, timeout=20)
        el.send_keys(Keys.SHIFT, Keys.F10)
        # action = ActionChains(self.driver.wdvr)
        # action.context_click(el).perform()

    def verify_submenu_view(self):
        return self.driver.wait_for_object("submenu_view", displayed=False, raise_e=False, timeout=20) is not False

    def verify_wechat_ok(self):
        return self.driver.wait_for_object("wechat_ok", displayed=False, raise_e=False, timeout=20) is not False

    def click_wechat_ok(self):
        self.driver.click("wechat_ok", timeout=10)

    def click_check_updates_button(self):
        self.driver.click("check_updates_button", timeout=20)

    def click_view_all_updates_button(self):
        self.driver.click("view_all_updates_button", displayed=False, timeout=20)

    def verify_update_summary_card_header_title(self):
        return self.driver.wait_for_object("update_summary_card_header_title", displayed=False, raise_e=False, timeout=20) is not False