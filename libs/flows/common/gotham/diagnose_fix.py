from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow


class DiagnoseFix(GothamFlow):
    flow_name = "diagnose_fix"
    stage_link = ["virtualagent-dev.hpcloud.hp.com"]
    prod_link = ["virtualagent.hpcloud.hp.com"]
    online_troubleshooting_link = ["h20180.www2.hp.com"]
    hp_support_forum_link = ["h30434.www3.hp.com"]

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_done_btn(self):
        self.driver.click("done_btn")

    def click_exit_btn(self):
        self.driver.click("exit_btn")

    def click_continue_btn(self):
        self.driver.click("continue_btn")

    def click_test_print_btn(self):
        self.driver.click("test_print_btn")

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
    def verify_no_issue_screen(self, timeout=120):
        self.driver.wait_for_object("no_issue_found_title_text", timeout=timeout)
        self.driver.wait_for_object("chat_with_virtual_agent_link")
        self.driver.wait_for_object("online_troubleshooting_link")
        self.driver.wait_for_object("software_and_driver_downloads_link")
        self.driver.wait_for_object("hp_support_forum_link")
        self.driver.wait_for_object("test_print_btn")
        self.driver.wait_for_object("done_btn")

    def verify_diagnosis_complete_screen(self):
        self.driver.wait_for_object("test_print_btn", timeout=120)
        self.driver.wait_for_object("done_btn")

    def verify_exit_diagnose_and_fix_dialog(self):
        """
        Verify the current dialog is Exit Diagnose and Fix.
        """
        return self.driver.wait_for_object("exit_diagnosing_and_fix_title")

    def verify_diagnoseing_and_fixing_text_display(self):
        """
        Verify "Diagnosing and fixing..." test display
        """
        return self.driver.wait_for_object("diagnoseing_and_fixing_text")

    def verify_here_are_your_results_text_display(self):
        """
        Verify "Diagnosis complete. Here are your results." test display
        """
        return self.driver.wait_for_object("here_are_your_results_text")

    def verify_did_that_solve_the_problem_text_display(self):
        """
        Verify "Did that solve the problem?" test display
        """
        return self.driver.wait_for_object("did_that_solve_the_problem_text")

    def verify_here_are_your_results_text_2_screen(self):
        """
        Verify "Diagnosis complete. Here are your results." with "Try Again" and "Next" Button test diaplay
        """
        self.driver.wait_for_object("here_are_your_results_text", timeout=300)
        self.driver.wait_for_object("try_again_btn")
        self.driver.wait_for_object("next_btn")
    
    def verify_if_you_are_still_having_problems_screen(self):
        """
        Verify the current dialog is "If you're still having problems check out these additional resources" screen
        """
        return self.driver.wait_for_object("still_having_problems_title")

    def verify_hp_support_forum_link_diaplay(self):
        """
        Verify "hp support forum" link diaplay
        """
        return self.driver.wait_for_object("hp_support_forum_link")

    def verify_chat_with_virtual_agent_link_diaplay(self, raise_e=True):
        """
        Verify "chat with virtual agent" link diaplay
        """
        return self.driver.wait_for_object("chat_with_virtual_agent_link", raise_e=raise_e)
    