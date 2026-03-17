
from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow

class MobileFax(HPXFlow):
    flow_name = "mobilefax"


    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_sign_in_btn(self):
        self.driver.click("sign_in_btn", change_check={"wait_obj": "sign_in_btn", "invisible": True}, retry=2, delay=1)

    def click_compose_fax_menu(self):
        self.driver.click("compose_fax_menu", change_check={"wait_obj": "to_text", "invisible": False}, retry=2, delay=1)

    def click_back_btn(self):
        self.driver.click("top_back_btn")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    
    def verify_mobile_fax_screen(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("compose_fax_menu", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("sent_menu", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("drafts_menu", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("settings_menu", timeout=timeout, raise_e=raise_e)
    
    def verify_compose_fax_menu_screen(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("from_text", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("clear_all_fields_link", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("save_as_draft_link", timeout=timeout, raise_e=raise_e)