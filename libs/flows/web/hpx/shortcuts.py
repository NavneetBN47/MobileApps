
from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow

class Shortcuts(HPXFlow):
    flow_name = "shortcuts"


    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_create_account_btn(self):
        self.driver.click("create_account_btn", change_check={"wait_obj": "create_account_btn", "invisible": True}, retry=2, delay=1)

    def click_add_new_shortcuts(self):
        self.driver.click("add_new_shortcuts")

    def click_back_btn_on_new_shortcuts(self):
        self.driver.click("top_back_btn", change_check={"wait_obj": "add_new_shortcuts_title", "invisible": True}, retry=3, delay=1)
    
    def click_back_btn_on_shortcuts(self):
        self.driver.click("top_back_btn")

    def click_email_shortcut_tile(self):
        self.driver.click("email_shortcut_tile")
    
    def click_print_shortcut_btn(self, timeout=10, raise_e=True):
        self.driver.wait_for_object("print_shortcut_btn", timeout=timeout, raise_e=raise_e)
        self.driver.click("print_shortcut_btn")
 
    def click_save_btn(self):
        self.driver.click("save_btn_shortcut")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    
    def verify_add_new_shortcuts_screen(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("add_new_shortcuts_title", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("popular_shortcuts", timeout=timeout, raise_e=raise_e)
 
    def verify_shortcuts_screen(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("shortcuts_tile_header", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("add_new_shortcuts", timeout=timeout, raise_e=raise_e)

    def verify_default_email(self, timeout=30):
        self.driver.wait_for_object("start_email_button", timeout=timeout)
        return self.driver.get_attribute("start_email_button", "text")
 
    def verify_sign_in_to_use_shortcuts_screen(self, raise_e=False):
        return self.driver.wait_for_object("sign_in_shortcut", timeout=10, raise_e=raise_e)
 
    def verify_add_new_shortcuts(self, raise_e=False):
        return self.driver.wait_for_object("add_new_shortcuts", timeout=20, raise_e=raise_e)
 
    def verify_create_your_own_shortcut(self, timeout=10, raise_e=False):
        return self.driver.wait_for_object("create_your_own_shortcut", timeout=timeout, raise_e=raise_e)
 
    def click_create_your_own_shortcut(self, timeout=10, raise_e=True):
        self.driver.wait_for_object("create_your_own_shortcut", timeout=timeout, raise_e=raise_e)
        self.driver.click("create_your_own_shortcut")
 
    def enter_shortcut_name(self, shortcut_name, timeout=10, raise_e=True):
        input_field = self.driver.wait_for_object("shortcut_name_box", timeout=timeout, raise_e=raise_e)
        input_field.clear()
        input_field.send_keys(shortcut_name)
 
    def verify_save_shortcut_btn(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("save_shortcut_btn", timeout=timeout, raise_e=raise_e)
 
    def click_save_shortcut_btn(self, timeout=10, raise_e=True):
        self.driver.wait_for_object("save_shortcut_btn", timeout=timeout, raise_e=raise_e)
        self.driver.click("save_shortcut_btn")
 
    def verify_one_drive_signin_link(self, raise_e=False):
        return self.driver.wait_for_object("one_drive_signin_link", raise_e=raise_e)
 
    def click_one_drive_signin_link(self):
        self.driver.click("one_drive_signin_link")
       
    def sign_in_and_verify_account_listed(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("verify_account", timeout=timeout, raise_e=raise_e)
             
    def verify_email_shortcut_tile(self, raise_e=False):
        return self.driver.wait_for_object("email_shortcut_tile", raise_e=raise_e, timeout=10)
    
    def verify_you_just_created_a_shortcut_popup(self, timeout=30):
        return self.driver.wait_for_object("you_just_created_a_shortcut_popup", timeout=timeout)
 
    def verify_save_btn(self, timeout=30):
        self.win_scroll_element("save_btn_shortcut")
        return self.driver.wait_for_object("save_btn_shortcut", timeout=timeout)
 
    def verify_print_shortcut_btn(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("print_shortcut_btn", timeout=timeout, raise_e=raise_e)
    
    def verify_edit_btn(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("edit_btn", timeout=timeout, raise_e=raise_e)
    
    def verify_delete_icon(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("delete_icon", timeout=timeout, raise_e=raise_e)

    def verify_delete_cancel_popup(self, raise_e=False):
        return self.driver.wait_for_object("delete_cancel_popup", timeout=20, raise_e=raise_e)
    
    # ***********************************************************************************************
    #                                      Action FLOWS                                       *
    # ***********************************************************************************************

    def click_edit_btn(self, timeout=10, raise_e=True):
        self.driver.wait_for_object("edit_btn", timeout=timeout, raise_e=raise_e)
        self.driver.click("edit_btn",timeout=timeout)

    def click_delete_icon(self, timeout=10, raise_e=True):
        self.driver.wait_for_object("delete_icon", timeout=timeout, raise_e=raise_e)
        self.driver.click("delete_icon",timeout=timeout)

    def click_delete_cancel_button(self, timeout=10, raise_e=True):
        self.driver.wait_for_object("cancel_button", timeout=timeout, raise_e=raise_e)
        self.driver.click("cancel_button",timeout=timeout)