from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow


class DiagnoseFix(HPXFlow):
    flow_name = "diagnose_fix"
    hp_support_forum_link = ["h30434.www3.hp.com"]

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_top_back_arrow(self):
        self.driver.click("back_btn", change_check={"wait_obj": "back_btn", "invisible": True}, retry=2, delay=1)

    def click_start_btn(self):
        self.driver.click("start_btn")

    def click_done_btn(self):
        self.driver.click("done_btn")

    def click_exit_btn(self):
        self.driver.click("exit_btn")

    def click_continue_btn(self):
        self.driver.click("continue_btn")

    def click_print_test_page_btn(self):
        self.driver.click("print_test_page_btn")

    def click_try_again_btn(self):
        self.driver.click("try_again_btn")

    def click_next_btn(self):
        self.driver.click("next_btn")

    def click_chat_with_virtual_agent_link(self):
        self.driver.click("chat_with_virtual_agent_link")

    def click_online_troubleshooting_link(self):
        self.driver.click("online_troubleshooting_link")

    def click_software_and_driver_downloads_link(self):
        self.driver.click("software_and_driver_downloads_link")

    def click_hp_support_forum_link(self):
        self.driver.click("hp_support_forum_link")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_diagnose_and_fix_screen(self, timeout=20):
        return self.driver.wait_for_object("back_btn", timeout=timeout) and\
        self.driver.wait_for_object("diagnose_and_fix_title", timeout=timeout) and\
        self.driver.wait_for_object("diagnose_and_fix_text", timeout=timeout) and\
        self.driver.wait_for_object("start_btn", timeout=timeout)

    def verify_no_issue_screen(self, timeout=90, raise_e=True):
        return self.driver.wait_for_object("no_issue_found_title", timeout=timeout, raise_e=raise_e) and\
        self.driver.wait_for_object("no_issue_found_text", timeout=timeout, raise_e=raise_e) and\
        self.driver.get_attribute("done_btn", attribute='Name') == 'Done' and\
        self.driver.get_attribute("print_test_page_btn", attribute='Name') == 'Print test page'

    def verify_diagnosis_complete_btn_screen(self):
        self.driver.wait_for_object("print_test_page_btn", timeout=120)
        self.driver.wait_for_object("done_btn")

    def verify_exit_diagnose_and_fix_dialog(self):
        """
        Verify the current dialog is Exit Diagnose and Fix.
        """
        return self.driver.wait_for_object("exit_diagnosing_and_fix_title")

    def verify_diagnosing_and_fixing_screen_display(self, timeout=30):
        """
        Verify "Diagnosing and fixing..." screen display.
        """
        return self.driver.wait_for_object("diagnose_and_fix_progress", timeout=timeout) and\
        self.driver.wait_for_object("diagnosing_and_fixing_text", timeout=timeout) and\
        self.driver.wait_for_object("image", timeout=timeout)

    def verify_back_btn_is_disabled(self):
        assert self.driver.get_attribute("back_btn", attribute='IsEnabled').lower() == "false"

    def verify_diagnosis_complete_fixed_screen(self, timeout=120, raise_e=True):
        """
        Verify "Diagnosis complete" test display(found issue and fixed).
        """
        self.driver.wait_for_object("diagnosis_complete_title", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("diagnosis_complete_text", timeout=timeout, raise_e=raise_e)
        self.driver.get_attribute("done_btn", attribute='Name') == 'Done' and\
        self.driver.get_attribute("print_test_page_btn", attribute='Name') == 'Print test page'

    def verify_diagnosis_complete_not_fixed_screen(self, timeout=300):
        """
        Verify "Diagnosis complete" with "Try Again" and "Next" Button test diaplay.
        """
        self.driver.wait_for_object("diagnosis_complete_title", timeout=timeout)
        self.driver.wait_for_object("not_fixed_text", timeout=timeout)
        self.driver.wait_for_object("try_again_btn")
        self.driver.wait_for_object("next_btn")

    def verify_btns_list_on_not_fixed_issue_screen(self):
        assert self.driver.get_attribute("first_btn", attribute='Name') == 'Try Again'
        assert self.driver.get_attribute("second_btn", attribute='Name') == 'Next'
    
    def verify_if_you_are_still_having_problems_screen(self):
        """
        Verify the current dialog is "If you're still having problems check out these additional resources" screen
        """
        return self.driver.wait_for_object("still_having_problems_title")

    def verify_btns_list_on_if_you_still_having_problems_screen(self):
        assert self.driver.get_attribute("1st_btn", attribute='Name') == 'Done'
        assert self.driver.get_attribute("2nd_btn", attribute='Name') == 'Test Print'

    def verify_hp_support_forum_link_display(self):
        """
        Verify "hp support forum" link diaplay
        """
        return self.driver.wait_for_object("hp_support_forum_link")

    def verify_chat_with_virtual_agent_link_diaplay(self, raise_e=True):
        """
        Verify "chat with virtual agent" link diaplay
        """
        return self.driver.wait_for_object("chat_with_virtual_agent_link", raise_e=raise_e)

    def verify_diagnose_and_fix_page(self, timeout=20, raise_e=False):
        """
        Verify Diagnose and Fix page display with all the expected elements.
        """
        return self.driver.wait_for_object("diagnose_and_fix_title", timeout=timeout)

    def verify_print_quality_tools_btn(self, raise_e=False):
        return self.driver.wait_for_object("print_quality_tools_text", raise_e=raise_e)
 
    def verify_diagnostics_view_all_button(self, raise_e=False):
        return self.driver.wait_for_object("diagnostics_view_all_btn", raise_e=raise_e)
  
