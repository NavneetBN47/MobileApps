from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow


class Account(GothamFlow):
    flow_name = "account"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_cancel_btn(self):
        self.verify_cancel_btn()
        self.driver.click("cancel_btn")

    def select_sign_out_btn(self):
        self.verify_sign_out_btn()
        self.driver.click("sign_out_btn", change_check={"wait_obj": "sign_out_btn", "invisible": True})


    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_sign_out_dialog(self):
        """
        Verify the current screen is sign out dialog
        """
        self.driver.wait_for_object("sign_out_dialog_title")

    def verify_cancel_btn(self):
        self.driver.wait_for_object("cancel_btn")

    def verify_sign_out_btn(self):
        self.driver.wait_for_object("sign_out_btn")