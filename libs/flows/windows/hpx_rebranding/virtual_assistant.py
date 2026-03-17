from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow

class VirtualAssistant(HPXRebrandingFlow):
    flow_name = "virtual_assistant"

################################# Verification Flows #####################################

    def verify_start_virtual_assistant(self):
        self.driver.swipe("start_virtual_assistant")
        return self.driver.wait_for_object("start_virtual_assistant")

    def verify_view_manuals_and_guides_link(self):
        return self.driver.wait_for_object("view_manuals_and_guides_link")

    def verify_get_more_help_on_our_website_link(self):
        return self.driver.wait_for_object("get_more_help_on_our_website_link")

    def verify_start_a_repair_order_link(self):
        return self.driver.wait_for_object("start_a_repair_order_link")

    def verify_contact_us(self):
        return self.driver.wait_for_object("contact_us")

    def verify_virtual_assistant_side_panel(self):
        self.driver.wait_for_object("va_chat_header", timeout=20)
        self.driver.wait_for_object("end_session_btn")
        self.driver.wait_for_object("feedback_va_btn")
        self.driver.wait_for_object("start_over_btn")

    def verify_how_can_i_assist_you(self):
        return self.driver.wait_for_object("how_can_i_assist_you")

    def verify_pc_btn_va(self):
        return self.driver.wait_for_object("pc_btn_va")

    def verify_product_information(self):
        self.driver.swipe("product_information")
        return self.driver.wait_for_object("product_information")

    def verify_would_like_to_get_started(self):
        self.driver.wait_for_object("yes_btn")
        self.driver.wait_for_object("rephrase_my_question_btn")

    def verify_support_gpt(self):
        self.driver.swipe("support_gpt")
        return self.driver.wait_for_object("support_gpt", timeout=60)

    def verify_great_deals_from_hp(self):
        self.driver.swipe("great_deals_from_hp")
        return self.driver.wait_for_object("great_deals_from_hp", timeout=60)

    def verify_enter_your_question(self):
        return self.driver.wait_for_object("enter_your_question")

    def verify_send_btn(self):
        return self.driver.wait_for_object("send_btn")

    def verify_i_can_help_you_with(self):
        return self.driver.wait_for_object("i_can_help_you_with")

    def verify_feedback_va_btn(self):
        return self.driver.wait_for_object("feedback_va_btn", timeout=25)

    def verify_hp_privacy_statement_link_after_feedback(self):
        return self.driver.wait_for_object("hp_privacy_statement_link_after_feedback")

    def feedback_va_satisfied_text(self):
        return self.driver.wait_for_object("how_satisfied_text")

    def verify_va_resolved_issue(self):
        return self.driver.wait_for_object("va_resolve_my_issue")

    def verify_would_like_to_tell_more(self):
        return self.driver.wait_for_object("would_like_to_tell_more")

    def verify_submit_feedback_va_btn(self):
        self.driver.swipe("submit_feedback_va_btn")
        return self.driver.wait_for_object("submit_feedback_va_btn")

    def verify_feedback_skip_va_btn(self):
        self.driver.swipe("feedback_skip_va_btn")
        return self.driver.wait_for_object("feedback_skip_va_btn")

    def verify_feedback_prompt(self):
        self.feedback_va_satisfied_text()
        self.verify_va_resolved_issue()
        self.verify_would_like_to_tell_more()
        self.driver.wait_for_object("enter_your_feedback_textbox")
        self.verify_submit_feedback_va_btn()
        self.verify_feedback_skip_va_btn()

    def verify_start_over_btn(self):
        return self.driver.wait_for_object("start_over_btn")

    def verify_start_over_form(self):
        self.driver.wait_for_object("start_over_with_a_new_issue_btn", timeout=15)
        self.driver.wait_for_object("i_would_like_to_continue_btn", timeout=15)

    def verify_bottom_privacy_btn(self):
        return self.driver.wait_for_object("va_bottom_privacy_btn")

    def verify_end_session_btn(self):
        self.driver.wait_for_object("end_session_btn")
        return self.driver.get_attribute("end_session_btn", "Name")

    def verify_end_session_overlay(self):
        self.driver.wait_for_object("close_va_popup")
        self.driver.wait_for_object("close_va_btn")
        self.driver.wait_for_object("keep_open_va_btn")

    def verify_did_this_solve_the_problem(self):
        self.driver.wait_for_object("did_this_solve_the_problem")
        self.driver.wait_for_object("yes_solved_btn")
        self.driver.wait_for_object("not_solved_btn")

    def verify_starting_msg_va(self):
        return self.driver.wait_for_object("start_msg_va")

    def verify_va_start_messages(self):
        self.driver.wait_for_object("va_chat_header", timeout=25)
        self.verify_support_gpt()
        self.verify_great_deals_from_hp()

    def verify_end_session_btn_disabled(self):
        assert self.driver.get_attribute("end_session_btn", attribute="IsEnabled").lower() == "false"

    def verify_text_on_back_btn_va(self):
        return self.driver.get_attribute("va_back_btn", "LocalizedControlType")

    def navigate_to_va_chat(self):
        self.driver.wait_for_object("what_can_we_help_you_header")
        self.driver.wait_for_object("va_back_btn")
        self.driver.wait_for_object("show_more_btn_va")
        self.driver.click("show_more_btn_va")
        self.driver.swipe(distance=7)
        self.driver.wait_for_object("show_less_va")
        self.driver.wait_for_object("other_btn_va")
        self.driver.click("other_btn_va")

    def verify_minimize_btn_va(self):
        return self.driver.wait_for_object("minimize_btn_va", timeout=20)

    def verify_chromebook_card(self):
        return self.driver.wait_for_object("chromebook_card", raise_e=False)

    def verify_hp_pc_updating_driver_link(self):
        self.driver.swipe("hp_pc_updating_driver_link")
        return self.driver.wait_for_object("hp_pc_updating_driver_link")

    def navigate_to_va_chat_window(self):
        self.verify_virtual_assistant_side_panel()
        self.navigate_to_va_chat()
        self.verify_va_start_messages()

    def verify_virtual_assistant_side_panel(self):
        self.driver.wait_for_object("what_can_we_help_you_header")
        self.driver.wait_for_object("computer_is_slow")
        self.driver.wait_for_object("display_or_touchscreen")
        self.driver.wait_for_object("keyboard_or_mouse")
        self.driver.wait_for_object("restore_computer_settings")
        self.driver.wait_for_object("no_sound")
        return True

##################################### CLICK ACTIONS #####################################

    def click_start_virtual_assistant(self):
        for _ in range(5):
             self.driver.swipe(distance=3)
             if self.driver.wait_for_object("contact_us", timeout=5, raise_e=False) is not False:
                break
        if self.driver.wait_for_object("start_virtual_assistant", timeout=20) is not False:
            self.driver.click("start_virtual_assistant", timeout = 20)

    def click_view_manuals_and_guides_link(self):
        self.driver.click("view_manuals_and_guides_link", timeout=10)

    def click_get_more_help_on_our_website_link(self):
        self.driver.click("get_more_help_on_our_website_link", timeout=10)

    def click_start_a_repair_order_link(self):
        self.driver.wait_for_object("start_a_repair_order_link")
        self.driver.click("start_a_repair_order_link", timeout=10)

    def click_contact_us(self):
        self.driver.wait_for_object("contact_us")
        self.driver.click("contact_us", timeout=10)

    def input_your_question(self, contents):
        self.driver.click("enter_your_question")
        self.driver.send_keys("enter_your_question", contents)

    def select_pc_btn(self):
        self.driver.click("pc_btn_va", timeout=10)

    def choose_performance(self):
        self.driver.click("perfomance", timeout=10)

    def click_yes_btn(self):
        self.driver.wait_for_object("yes_btn")
        self.driver.click("yes_btn", timeout=10)

    def select_great_deals_from_hp(self):
        self.driver.wait_for_object("great_deals_from_hp")
        self.driver.click("great_deals_from_hp", timeout=10)

    def click_send_btn(self):
        self.driver.click("send_btn", timeout=10)

    def click_yes_solved_btn(self):
        self.driver.wait_for_object("yes_solved_btn")
        self.driver.click("yes_solved_btn", timeout=10)

    def click_feedback_va_btn(self):
        self.driver.click("feedback_va_btn", timeout=10)

    def click_start_over_btn(self):
        self.driver.click("start_over_btn", timeout=10)

    def click_start_over_with_a_new_issue_btn(self):
        self.driver.click("start_over_with_a_new_issue_btn", timeout=10)

    def click_would_like_to_continue(self):
        self.driver.wait_for_object("would_like_to_continue")
        self.driver.click("would_like_to_continue", timeout=10)

    def click_va_bottom_privacy_btn(self):
        self.driver.wait_for_object("va_bottom_privacy_btn")
        self.driver.click("va_bottom_privacy_btn", timeout=10)

    def click_end_session_btn(self):
        self.driver.click("end_session_btn", timeout = 10)

    def click_close_va_btn(self):
        self.driver.click("close_va_btn", timeout=10)

    def click_keep_open_va_btn(self):
        self.driver.click("keep_open_va_btn", timeout=10)

    def handle_feature_unavailable_popup(self):
        if self.driver.wait_for_object("feature_unavailable_ok_btn", raise_e=False, timeout=20) is not False:
            self.driver.click("feature_unavailable_ok_btn")

    def click_hp_pc_updating_driver_link(self):
        self.driver.click("hp_pc_updating_driver_link", timeout=10)

    def click_chromecard_no_btn(self):
        self.driver.click("chromecard_no_btn", timeout=10)
