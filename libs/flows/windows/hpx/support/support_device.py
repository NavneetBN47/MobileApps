import time
from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class SupportDevice(HPXFlow):
    flow_name = "support_device"

    USER_MAUNAL = "user_manual_guide_card"
    VIRTUAL_REPAIR = "virtual_repair_center"
    SERVICE_CENTER = "service_centor_locator"
    SUPPORT_FORUM = "support_forum_card"
    SUPPORT_CENTER = "support_center_card"
    WARRANTY_DISPUTE = "warranty_dispute"

    def click_link(self, link):
        """
        Click on a link
        :param link: use class constants:
                PRODUCT_MANUAL_LINK 
                VIRTUAL_REPAIR_LINK
                MATE_LOCATOR_LINK
                ...
        """
        self.driver.click(link, displayed=False)
    
    def verify_link_display(self, link):
        return self.driver.wait_for_object(link, raise_e=False, timeout=10) 

    def click_va(self):
        self.driver.click("va_card", displayed=False, change_check={"wait_obj": "start_virtual_agent", "flow_change": "support_va", "invisible": False}, retry=5)

    def click_run_hdware_diags(self, timeout=20):
        self.driver.click("diagnostic_card",  displayed=False, timeout=timeout)

    def click_hp_smart_btn(self, timeout=20):
        self.driver.click("hp_smart_btn", displayed=False, timeout=timeout)

    def click_HP_product_support_center(self):
        self.driver.click("support_center_card", displayed=False)

    def click_HP_support_forum(self):
        self.driver.click("support_forum_card", displayed=False)

    def click_speak_to_agent(self):
        self.driver.click("speak_to_agent", raise_e=True, displayed=False, timeout=30)

    def enter_keys_to_speak_to_agent(self, text):
        self.driver.send_keys("speak_to_agent", text, clear_text=False)

    def click_user_manuals_guide(self, timeout=10):
        self.driver.click("user_manual_guide_card", displayed=False, timeout=timeout)

    def click_virtual_repair_center(self):
        self.driver.click("virtual_repair_center", raise_e=True, displayed=False)
    
    def verify_virual_repair_center_display(self):
        return self.driver.wait_for_object("virtual_repair_center", raise_e=False, timeout=30)
    
    def enter_keys_virtual_repair_center(self, text):
        self.driver.send_keys("virtual_repair_center", text, clear_text=False)

    def click_service_center_locator(self):
        self.driver.wait_for_object("service_centor_locator", raise_e=True, displayed=False).click()

    def verify_service_center_locator_display(self):
        return self.driver.wait_for_object("service_centor_locator", raise_e=False, timeout=10)
    
    def enter_keys_service_center_locator(self, text):
        self.driver.send_keys("service_centor_locator", text, clear_text=False)

    def click_warranty_dispute(self):
        self.driver.click("warranty_dispute", raise_e=True, displayed=False)

    def verify_warranty_dispute_display(self):
        return self.driver.wait_for_object("warranty_dispute", raise_e=False, displayed=False)
    
    def enter_keys_warranty_dispute(self, text):
        self.driver.send_keys("warranty_dispute", text, clear_text=False)

    def verify_user_manuals_guide(self):
        return self.driver.wait_for_object("user_manual_guide_card", raise_e=False, timeout=20)
    
    def enter_keys_user_manuals_guide(self, text):
        self.driver.send_keys("user_manual_guide_card", text, clear_text=False)

    def verify_support_forum(self):
        return self.driver.wait_for_object("support_forum_card", raise_e=False, timeout=10)
    
    def enter_keys_support_forum(self, text):
        self.driver.send_keys("support_forum_card", text, clear_text=False)

    def verify_product_support_center(self):
        return self.driver.wait_for_object("support_center_card", raise_e=False, timeout=10)
    
    def enter_keys_product_support_center(self, text):
        self.driver.send_keys("support_center_card", text, clear_text=False)

    def verify_speak_to_agent(self):
        return self.driver.wait_for_object("speak_to_agent", raise_e=False, timeout=10)

    def click_warranty_details_link(self):
        self.driver.click("warranty_details_link", timeout=10)

    def click_warranty_details_link_subscription(self):
        self.driver.click("warranty_details_link_subscription")

    def click_view_data_collected_link(self):
        self.driver.click("view_data_collected_link")

    def click_yes_button(self):
        self.driver.click("confirmButton")
    
    def click_no_button(self):
        self.driver.click("cancelButton")

    def click_whatsapp(self):
        self.driver.click("whats_app_btn", displayed=False)
    
    def click_country_list(self):
        self.driver.click("support_country_cbx", timeout=60)

    def edit_countrysearchbox(self, text):
        self.driver.send_keys("country_searchbox",  text)
    
    def verify_country_list(self):
        return self.driver.wait_for_object("support_country_cbx", raise_e=False, timeout=10)
    
    def get_country(self):
        return self.driver.wait_for_object("support_country_cbx", raise_e=False, timeout=10).get_attribute("Name")
    
    def verify_support_section(self):
        return self.driver.wait_for_object("support_section", raise_e=False, timeout=10)

    def verify_country_selector(self):
        return self.driver.wait_for_object("country_selector", raise_e=False, timeout=10)

    def verify_support_by_region_value(self):
        return self.driver.wait_for_object("support_by_region_lbl", raise_e=False, timeout=10).text

    def select_country(self, country_index):
        self.driver.click("country_index", displayed=False, format_specifier=[country_index])

    def select_country_by_country_name(self, country_name=None):
        self.driver.click("country_option", displayed=False, format_specifier=[country_name])

    def verify_countrylbx(self):
        return self.driver.wait_for_object("country_lbx", raise_e=False, timeout=10)

    def get_countryoptions(self):
        self.verify_countrylbx()
        return self.driver.find_object("country_options", multiple=True)
    
    def verify_whatsapp_display(self):
        return self.driver.wait_for_object("whats_app_btn", raise_e=False, timeout=10)
    
    def click_fbmessenger(self):
        self.driver.click("fb_messenger_btn", displayed=False, timeout=20)

    def verify_fbmessenger_display(self):
        return self.driver.wait_for_object("fb_messenger_btn", raise_e=False, timeout=10)

    def click_wechat(self):
        self.driver.click("wechat_btn", displayed=False, timeout=20)

    def verify_wechat_display(self):
        return self.driver.wait_for_object("wechat_btn", raise_e=False, timeout=10)
    
    def click_zalo(self):
        self.driver.click("zalo_btn", displayed=False, timeout=20)

    def verify_zalo_display(self):
        return self.driver.wait_for_object("zalo_btn", raise_e=False, timeout=10)
    
    def click_kakaotalk(self):
        self.driver.click("kakao_talk_btn", displayed=False, timeout=20)

    def verify_kakaotalk_display(self):
        return self.driver.wait_for_object("kakao_talk_btn", raise_e=False, timeout=10)

    def click_line(self):
        self.driver.click("line_btn", displayed=False, timeout=20)

    def verify_line_display(self):
        return self.driver.wait_for_object("line_btn", raise_e=False, timeout=10)

    def click_twitter(self):
        self.driver.click("twitter_btn", displayed=False, timeout=20)

    def verify_twitter_display(self):
        return self.driver.wait_for_object("twitter_btn", raise_e=False, timeout=10)

    def click_call_me_back(self):
        self.driver.click("call_me_back_card")
    
    def verify_call_me_back_display(self):
        return self.driver.wait_for_object("call_me_back_card", raise_e=False, timeout=10)
    
    def verify_outside_hours_popup_display(self):
        return self.driver.wait_for_object("outside_hours_popup", raise_e=False, timeout=10)

    def click_close_btn(self):
        self.driver.click("close_btn")

    def click_chat_with_agent(self):
        self.driver.click("chat_with_agent_btn", timeout=10)
    
    def enter_keys_to_chat_with_agent(self, text):
        self.driver.send_keys("chat_with_agent_btn", text, clear_text=False)

    def verify_chat_with_agent_display(self):
        return self.driver.wait_for_object("chat_with_agent_btn", raise_e=False, timeout=10)
    
    def get_chat_with_agent_title(self):
        return self.driver.wait_for_object("chat_with_agent_btn", raise_e=False, timeout=10).get_attribute("Name")

    def verify_warranty_details_popup_display(self, raise_e=False, timeout=10):
        return self.driver.wait_for_object("support_dialog_label", raise_e=False, timeout=timeout)

    def verify_social_messaging_label_display(self, raise_e=False, timeout=10):
        return self.driver.wait_for_object("social_messaging_channels_lbl", raise_e=False, timeout=timeout)

    def click_privacy_checkbox(self):
        self.driver.click("privacy_checkbox", displayed=False,  raise_e=True)
    
    def click_case_cancel_button(self):
        self.driver.click("create_case_cancel_btn", displayed=False,  raise_e=True)

    def click_chat_cancel_button(self):
        self.driver.click("chat_cancel_btn", displayed=False, raise_e=True)

    def verify_product_image_display(self):
        return self.driver.wait_for_object("product_img", raise_e=False, timeout=10)
    
    def verify_case_cancel_button_display(self):
        return self.driver.wait_for_object("create_case_cancel_btn", raise_e=False, timeout=10)

    def get_product_number_value(self, raise_e=True, timeout=20):
        return self.driver.wait_for_object("product_number_text", raise_e=raise_e, timeout=timeout).text
    
    def double_click_product_number(self):
        self.driver.double_click("product_number_text")

    def enter_keys_to_product_number(self, text):
        self.driver.send_keys("product_number_text", text, clear_text=False)

    def enter_keys_to_warrenty_info(self, text):
        self.driver.send_keys("warranty_text", text, clear_text=False)
    
    def get_serial_number_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("serial_number_text",  raise_e=raise_e, timeout=timeout).text
    
    def enter_keys_to_serial_number(self, text):
        self.driver.send_keys("serial_number_text", text, clear_text=False)

    def select_serial_number(self):
        el = self.driver.find_object("serial_number_text")
        width = el.rect["width"]
        self.driver.select(el, x_offset=width)

    def select_warranty_info(self):
        el = self.driver.wait_for_object("warranty_text", displayed=True, timeout=30)
        width = el.rect["width"]
        self.driver.select_by_drag_and_drop(el, width * 0.5, -width )

    def right_click_serial_number(self):
        el = self.driver.find_object("serial_number_text")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.5, height * 0.5 , right_click=True)
    
    def right_click_warrenty_info(self):
        el = self.driver.find_object("warranty_text")
        width,  height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.5, height * 0.5, right_click=True)

    def click_copy_menu_item(self):
        self.driver.click("copy_menu_item", timeout=10)

    def verify_copy_menu_item(self, timeout=10):
        return self.driver.wait_for_object("copy_menu_item",  raise_e=False, timeout=timeout)
    
    def double_click_serial_number(self):
        self.driver.double_click("serial_number_text")

    def double_click_warranty_info(self):
        self.driver.double_click("warranty_text")

    def verify_warranty_info_show(self):
        return self.driver.wait_for_object("warranty_text", clickable=True, timeout=10)

    def get_product_name_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("product_name_text",  raise_e=raise_e, timeout=timeout).text

    def get_nick_name_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("nick_name_txt",  raise_e=raise_e, timeout=timeout).text 

    def verify_nick_name_show(self):
        self.driver.wait_for_object("nick_name_txt", raise_e=False, timeout=10)

    def double_click_nick_name(self):
        self.driver.double_click("nick_name_txt")

    def select_nick_name(self):
        self.verify_nick_name_show()
        el = self.driver.find_object("nick_name_txt")
        width = el.rect["width"]
        self.driver.select_by_drag_and_drop(el, -width * 0.49, width)
    
    def right_click_nick_name(self):
        el = self.driver.find_object("nick_name_txt")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.5, height * 0.5 , right_click=True)

    def get_subcription_id_value(self, raise_e=True, timeout=20):
        return self.driver.wait_for_object("subcription_id_text",  raise_e=raise_e, timeout=timeout).text

    def get_state_date_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("start_date_text",  raise_e=raise_e, timeout=timeout).text

    def get_warranty_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("warranty_text",  raise_e=raise_e, timeout=timeout).get_attribute("Name")

    def get_warranty_title_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("warranty_title_text",  raise_e=raise_e, timeout=timeout).text

    def get_warranty_details_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("warranty_details_text",  raise_e=raise_e, timeout=timeout).get_attribute("Name")

    def get_warranty_details_popup_title(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("support_dialog_label",  raise_e=raise_e, timeout=timeout).text

    def get_warranty_details_content_title(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("support_content_label",  raise_e=raise_e, timeout=timeout).text

    def verify_add_device_popup_display(self, timeout=10):
        return self.driver.wait_for_object("support_dialog_label", raise_e=False, timeout=timeout)

    def get_suppprt_dialog_link_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("view_data_collected_link",  raise_e=raise_e, timeout=timeout).get_attribute("Name")

    def get_yes_button_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("confirmButton",  raise_e=raise_e, timeout=timeout).text

    def get_no_button_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("cancelButton",  raise_e=raise_e, timeout=timeout).text

    def get_user_manual_guide_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("user_manual_guide_card", displayed=False, raise_e=raise_e, timeout=timeout).text

    def get_support_center_card_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("support_center_card", raise_e=raise_e, timeout=timeout, displayed=False).text

    def get_support_form_card_value(self, raise_e=True, timeout=30):
        return self.driver.wait_for_object("support_forum_card", raise_e=raise_e, timeout=timeout, displayed=False).text

    def get_phone_number_btn_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("get_phone_number_btn", displayed=False, raise_e=raise_e, timeout=timeout).text
    
    def get_open_case_desc(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("open_cases_desc", displayed=False, raise_e=raise_e, timeout=timeout).text
    
    def click_get_phone_number(self):
        return self.driver.click("get_phone_number_btn")
    
    def verify_get_phone_number(self, raise_e=True, timeout=30):
        return self.driver.wait_for_object("get_phone_number_btn", displayed=False, raise_e=raise_e, timeout=timeout)
    
    def verify_phonecasedonebtn_show(self, raise_e=True, timeout=30):
        return self.driver.wait_for_object("phone_casedone_btn", displayed=False, raise_e=raise_e, timeout=timeout)
    
    def get_phone_number_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("phone_number_lbl", displayed=False, raise_e=raise_e, timeout=timeout).text
    
    def get_nick_name_tip_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("nick_name_tip_lbl", displayed=False, raise_e=raise_e, timeout=timeout).text  

    def get_allinplan_label_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("allinplan_lbl", displayed=False, raise_e=raise_e, timeout=timeout).text   
    
    def get_paas_banner_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("paas_banner", displayed=False, raise_e=raise_e, timeout=timeout).text

    def get_speak_to_agent_title(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("speak_to_agent", raise_e=raise_e, timeout=timeout).get_attribute("Name")
    
    def get_phonehelptext(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("speak_to_agent", raise_e=raise_e, timeout=timeout).get_attribute("HelpText")

    def get_problem_text(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("problem_edit", raise_e=raise_e, timeout=timeout).get_attribute("Value.Value")

    def get_problem_value(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("problem_edit", raise_e=raise_e, timeout=timeout).get_attribute("Name")

    def get_chat_now_btn_title(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("chat_now_btn", raise_e=raise_e, timeout=timeout).text

    def click_chatnow_btn(self):
        self.driver.click("chat_now_btn")
    
    def verify_chat_now_btn_state(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("chat_now_btn", raise_e=raise_e, timeout=timeout).get_attribute("IsEnabled")
    
    def verify_get_phone_number_btn_state(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("get_phone_number_btn", raise_e=raise_e, timeout=timeout).get_attribute("IsEnabled")
    
    def get_support_model_sub_title(self, raise_e=True, timeout=20):
        return self.driver.wait_for_object("support_model_sub_title", raise_e=raise_e, displayed=False, timeout=timeout).text

    def get_banner_lbl_title(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("banner_lbl", raise_e=raise_e, timeout=timeout).text

    def is_privacy_status_selected(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("privacy_checkbox", displayed=False,  raise_e=raise_e, timeout=timeout).get_attribute("Toggle.ToggleState")

    def verify_edit_nick_btn_show(self):
        return self.driver.wait_for_object("nick_edit_btn", clickable=True, timeout=10)

    def click_edit_nick_btn(self, timeout=20):
        self.driver.click("nick_edit_btn", raise_e=True, timeout=timeout)

    def enter_keys_to_nick_btn(self, text):
        self.driver.send_keys("nick_edit_btn", text, clear_text=False)

    def verify_nick_edit_show(self):
        return self.driver.wait_for_object("nick_edit_txt", clickable=True, timeout=10)
    
    def get_value_nick_edit_txt(self):
        return self.driver.wait_for_object("nick_edit_txt", clickable=True, timeout=10).get_attribute("Value.Value")
    
    def enter_keys_to_nick_edit(self, text, clear_text=False):
        self.driver.send_keys("nick_edit_txt", text, clear_text)
    
    def enter_keys_to_nick_text(self, text, clear_text=False):
        self.driver.send_keys("nick_name_txt", text, clear_text)

    def input_nickname(self, text):
        self.driver.clear_text("nick_edit_txt")
        self.driver.send_keys("nick_edit_txt", text)

    def edit_nickname(self, text):
        self.driver.click("nick_edit_btn", raise_e=True)
        self.driver.send_keys("nick_edit_txt", text)

    def click_save_nick_btn(self):
        self.driver.click("nick_save_btn")
                
    def verify_save_nick_btn_state(self):
        return self.driver.wait_for_object("nick_save_btn").get_attribute("IsEnabled")

    def verify_support_device_page(self, timeout=20):
        return self.driver.wait_for_object("nick_name_txt", raise_e=False, timeout=timeout) is not False

    def verify_cancel_nick_btn_show(self):
        return self.driver.wait_for_object("nick_cancel_btn", raise_e=False, timeout=10)
    
    def enter_keys_cancel_nick_btn(self, text):
        self.driver.send_keys("nick_cancel_btn", text, clear_text=False)

    def click_cancel_nick_btn(self):
        self.driver.click("nick_cancel_btn")

    def verify_cancel_nick_btn_state(self):
        return self.driver.wait_for_object("nick_cancel_btn").get_attribute("IsEnabled")
    
    def click_back_btn(self):
        self.driver.click("back_btn")

    def edit_problem(self, text):
        self.driver.click("problem_edit", displayed=False, raise_e=True)
        self.driver.send_keys("problem_edit", text)
    
    def enter_keys_to_problem_text(self, text):
        self.verify_problem_edit()
        self.driver.send_keys("problem_edit", text, clear_text=False)

    def get_problem_helptext(self):
        return self.driver.wait_for_object("problem_edit", displayed=False).get_attribute("HelpText")
    
    def verify_problem_edit(self):
        return self.driver.wait_for_object("problem_edit", displayed=False, timeout=20)
 
    def get_troubleshooting_title(self, displayed=False, raise_e=True, timeout=10):
        return self.driver.wait_for_object("guide_troubleshooting_title_lbl", displayed=displayed, raise_e=raise_e, timeout=timeout).text
    
    def get_diagnostic_title(self, displayed=False, raise_e=True, timeout=10):
        return self.driver.wait_for_object("diagnostics_title_lbl", displayed=displayed, raise_e=raise_e, timeout=timeout).text
    
    def click_network_check_btn(self):
        self.driver.click("network_check_btn")

    def click_fix_audio_issues_btn(self):
        self.driver.click("fix_audio_issues_btn")

    def click_check_os_btn(self):
        self.driver.click("check_operating_system_btn")

    def click_done_btn(self):
        self.driver.click("done_btn")

    def click_category_cbx(self):
        self.driver.click("select_category_cbx")
    
    def verify_category_type(self):
        return self.driver.wait_for_object("select_category_cbx", displayed=False).get_attribute("Name")
    
    def click_category_opt(self, index):
        self.driver.click("type_option", format_specifier=[index])

    def get_catetory(self, index):
        return self.driver.wait_for_object("type_option", displayed=False, format_specifier=[index]).text
    
    def verify_category_selected(self, index):
        return self.driver.wait_for_object("type_option", displayed=False, format_specifier=[index]).get_attribute("SelectionItem.IsSelected")
    
    def click_pravicy_link(self):
        self.driver.click("privacy_link")
    
    def click_go_privacy_link(self):
        self.driver.click("go_privacy_link")

    def verify_promptinfo_chat_form(self):
        return self.driver.wait_for_object("prompt_info_chat", displayed=False, raise_e=False).text
    
    def verify_promptinfo_speak_form(self):
        return self.driver.wait_for_object("prompt_info_speak", displayed=False, raise_e=False).text
    
    def click_minimize_btn(self):
        self.driver.click("minimize_button")

    def click_maximize_btn(self):
        self.driver.click("maximize_button")

    def click_hpptu_btn(self):
        self.driver.click("hpptu_btn", displayed=False, timeout=10)

    def verify_hpptu_btn(self):
        return self.driver.wait_for_object("hpptu_btn", displayed=False, raise_e=False)

    def click_netcheck_btn(self):
        self.driver.click("netcheck_btn", displayed=False, timeout=10)

    def click_audiocheck_btn(self):
        self.driver.click("audiocheck_btn", displayed=False, timeout=10)

    def click_oscheck_btn(self):
        self.driver.click("oscheck_btn", displayed=False, timeout=10)

    def click_yes_personalized_btn(self):
        self.driver.click("yes_btn_personalized_support")

    def verify_resources_card_display(self):
        return self.driver.wait_for_object("resources_cards", displayed=False, raise_e=False)

    def verify_liveassistant_card_display(self):
        return self.driver.wait_for_object("liveassistant_cards", displayed=False, raise_e=False)
    
    def verify_case_card_display(self):
        return self.driver.wait_for_object("case_cards", displayed=False, raise_e=False)
    
    def click_case_dropdown(self, case_id=None):
        self.driver.click("case_card", format_specifier=[case_id], displayed=False, timeout=10)

    def get_resources_cards(self):
        resources_names = []
        self.verify_resources_card_display()
        resources_cards = self.driver.find_object("resources_cards", multiple=True)
        for resources_card in resources_cards:
            resources_names.append(resources_card.text)
        return resources_names            
    
    def get_liveassistant_cards(self):
        liveassistant_names = []
        self.verify_liveassistant_card_display()
        liveassistant_cards = self.driver.find_object("liveassistant_cards", multiple=True)
        for liveassistant_card in liveassistant_cards:
            liveassistant_names.append(liveassistant_card.text)
        return liveassistant_names
    
    def get_open_cases_cards(self):
        cases_list = []
        self.verify_case_card_display()
        time.sleep(2)
        cases_cards = self.driver.find_object("open_cases_cards", multiple=True)
        for case_card in cases_cards:
            cases_list.append(case_card.get_attribute("Name"))
        return cases_list
    
    def get_close_cases_cards(self):
        cases_list = []
        self.verify_case_card_display()
        time.sleep(2)
        cases_cards = self.driver.find_object("close_cases_cards", multiple=True)
        for case_card in cases_cards:
            cases_list.append(case_card.get_attribute("Name"))
        return cases_list
    
    def get_case_cards(self):
        cases_list = []
        self.verify_case_card_display()
        time.sleep(2)
        cases_cards = self.driver.find_object("case_cards", multiple=True)
        for case_card in cases_cards:
            cases_list.append(case_card.get_attribute("AutomationId"))
        return cases_list
    
    def get_case_created_time(self, case_id=None):
        return self.driver.wait_for_object("case_created_time", format_specifier=[case_id], displayed=False, timeout=10).text
    