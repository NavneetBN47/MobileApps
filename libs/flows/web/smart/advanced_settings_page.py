from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow
from selenium.webdriver.common.keys import Keys

class AdvancedSettingsPage(SmartFlow):
    flow_name = "advanced_settings_page"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def get_printer_name_text(self):
        return self.driver.wait_for_object("advanced_settings_page_title").get_attribute("Name")

    def get_printer_ip_address(self):
        return self.driver.wait_for_object("printer_ip_address").get_attribute("Name")

    def get_printer_connected_router(self):
        return self.driver.wait_for_object("printer_connected_router").get_attribute("Name")

    def select_network_menu(self):
        self.driver.click("network_menu")

    def select_settings_menu(self):
        self.driver.click("settings_menu")

    def select_scan_menu(self):
        self.driver.click("scan_menu")

    def click_security_sub_item(self):
        self.driver.click("security_sub_item")

    def click_password_settings_under_security_sub_item(self):
        self.driver.click("password_settings")
    
    def input_new_password(self, n_pw):
        self.driver.send_keys("new_password", n_pw, slow_type=True, check_key_sent=True)

    def clear_new_password(self):
        self.driver.clear_text("new_password", not_input=True)

    def input_confirm_password(self, c_pw):
        self.driver.send_keys("confirm_password", c_pw, slow_type=True, check_key_sent=True)

    def clear_confirm_password(self):
        self.driver.clear_text("confirm_password", not_input=True)

    def click_apply_btn(self):
        self.driver.swipe()
        self.driver.click("apply_button")

    def click_do_not_show_check_box(self):
        self.driver.click("do_not_show_check_box")

    def click_ok_btn(self):
        self.driver.click("continuing_to_your_printer_settings_dialog_ok_btn")

    def click_cant_open_ews_dialog_ok_btn(self):
        el = self.driver.wait_for_object("cant_open_ews_dialog_ok_btn")
        el.send_keys(Keys.ENTER)

    def click_sign_in_link(self):
        self.driver.click("person_icon", raise_e=False)
        if self.driver.wait_for_object("sign_in_link", raise_e=False):
            self.driver.click("sign_in_link")

    def click_sign_out_link(self):
        self.driver.click("sign_out_link")

    # def click_ok_btn(self):
    #     self.driver.click("ok_btn")

    def trigger_hidden_url(self):
        el = self.driver.find_object("advanced_settings_page_title")
        self.driver.long_press_keys(Keys.CONTROL)
        self.driver.long_press_keys(Keys.SHIFT)
        self.driver.click_by_coordinates(el, x_offset=0.5, y_offset=1.5, right_click=True)
        self.driver.long_press_keys(Keys.CONTROL, down=False)
        self.driver.long_press_keys(Keys.SHIFT, down=False)

    def click_log_in_with_pin_dialog_submit_btn(self):
        self.driver.click("log_in_with_pin_dialog_submit_btn")

    def click_log_in_with_pin_dialog_cancel_btn(self):
        self.driver.click("log_in_with_pin_dialog_cancel_btn")

    def input_pin(self, pin):
        self.driver.send_keys("log_in_with_pin_dialog_edit_box", pin)

    def click_sign_in_btn_on_unauthorized_dialog(self):
        self.driver.click("unautorized_dialog")
    
    def click_sign_in_to_access_this_site_dialog_sign_in_btn(self):
        self.driver.click("sign_in_to_access_this_site_dialog_sign_in_btn")

    def click_sign_in_to_access_this_site_dialog_cancel_btn(self):
        self.driver.click("sign_in_to_access_this_site_dialog_cancel_btn")

    def input_username(self, username):
        self.driver.send_keys("sign_in_to_access_this_site_dialog_username_edit_box", username)

    def input_password(self, password):
        self.driver.send_keys("sign_in_to_access_this_site_dialog_password_edit_box", password)

    def make_ews_to_password_modal(self, password):
        '''
        This is a method to set password in ews only applicable to some printer
        '''
        self.select_settings_menu()
        if self.verify_continuing_to_your_printer_settings_dialog(timeout=5, raise_e=False):
            self.click_ok_btn()
        if self.verify_ews_login_state(raise_e=False):
                self.click_sign_out_link()
                self.verify_sign_out_successfuly_text()
                self.click_ok_btn()
        self.verify_ews_settings_page()
        self.click_security_sub_item()
        self.click_password_settings_under_security_sub_item()
        if self.verify_continuing_to_your_printer_settings_dialog(timeout=5, raise_e=False):
            if self.verify_redirecting_to_secure_page_dialog(raise_e=False):
                self.click_do_not_show_check_box()
            self.click_ok_btn()
        self.verify_password_settings_page(timeout=120)
        self.input_new_password(password)
        self.input_confirm_password(password)
        self.click_apply_btn()
        self.verify_password_changed_successfully_text()

    def remove_ews_password_modal(self, password):
        '''
        This is a method to remove ews password from printer settings
        '''
        self.select_settings_menu()
        if self.verify_access_secure_settings_dialog(raise_e=False):
            self.input_pin(password)
            self.click_log_in_with_pin_dialog_submit_btn()
            if self.verify_access_secure_settings_dialog(raise_e=False):
                self.input_pin("12345678")
                self.click_log_in_with_pin_dialog_submit_btn()
        if self.verify_sign_in_to_access_this_site_dialog(raise_e=False):
            self.input_username("admin")
            self.input_password(password)
            self.click_sign_in_to_access_this_site_dialog_sign_in_btn()
            if self.verify_sign_in_to_access_this_site_dialog(raise_e=False):
                self.input_username("admin")
                self.input_password("12345678")
                self.click_sign_in_to_access_this_site_dialog_sign_in_btn()
        if self.verify_continuing_to_your_printer_settings_dialog(timeout=5, raise_e=False):
            self.click_ok_btn()
        self.verify_ews_settings_page()
        self.click_security_sub_item()
        self.click_password_settings_under_security_sub_item()
        if self.verify_access_secure_settings_dialog(raise_e=False):
            self.input_pin(password)
            self.click_log_in_with_pin_dialog_submit_btn()
            if self.verify_access_secure_settings_dialog(raise_e=False):
                self.input_pin("12345678")
                self.click_log_in_with_pin_dialog_submit_btn()
        if self.verify_sign_in_to_access_this_site_dialog(raise_e=False):
            self.input_username("admin")
            self.input_password(password)
            self.click_sign_in_to_access_this_site_dialog_sign_in_btn()
            if self.verify_sign_in_to_access_this_site_dialog(raise_e=False):
                self.input_username("admin")
                self.input_password("12345678")
                self.click_sign_in_to_access_this_site_dialog_sign_in_btn()
        self.verify_password_settings_page(timeout=120)
        self.clear_new_password()
        self.clear_confirm_password()
        self.click_apply_btn()
        self.verify_password_changed_successfully_text()

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_advanced_settings_page(self, printer_obj):
        if "DunePrinterInfo" in str(printer_obj.p_obj):
            self.verify_dune_advanced_settings_page()
        else:
            self.verify_reg_advanced_settings_page()

    def verify_reg_advanced_settings_page(self, timeout=30, raise_e=True):
        if self.verify_continuing_to_your_printer_settings_dialog(raise_e=False):
            self.click_ok_btn()
        return self.driver.wait_for_object("settings_menu", timeout=timeout, raise_e=raise_e) and \
            self.driver.wait_for_object("scan_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("web_services_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("network_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("tools_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("home_menu", raise_e=raise_e)

    def verify_dune_advanced_settings_page(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("jobs_menu", timeout=timeout, raise_e=raise_e) and \
            self.driver.wait_for_object("home_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("copy_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("scan_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("print_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("supplies_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("paper_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("print_quality_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("general_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("network_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("security_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("support_tools_menu", raise_e=raise_e) and \
            self.driver.wait_for_object("accessibility_menu", raise_e=raise_e)

    def verify_cant_open_ews_dialog(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("cant_open_ews_dialog_title", timeout=timeout, raise_e=raise_e) and \
            self.driver.wait_for_object("cant_open_ews_dialog_body", raise_e=raise_e) and \
            self.driver.wait_for_object("cant_open_ews_dialog_ok_btn", raise_e=raise_e)

    def verify_continuing_to_your_printer_settings_dialog(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("continuing_to_your_printer_settings_dialog", timeout=timeout, raise_e=raise_e)

    def verify_hidden_url(self, raise_e=True):
        self.driver.wait_for_object("ews_hidden_url_edit_box", raise_e=raise_e)
        self.driver.wait_for_object("ews_hidden_url_forward_arrow", raise_e=raise_e)
        assert self.driver.wait_for_object("ews_hidden_url_text", raise_e=raise_e).text == "URL:"

    def verify_ews_sign_in_link(self, raise_e=True):
        return (self.driver.wait_for_object("sign_in_link", raise_e=raise_e) or self.driver.wait_for_object("person_icon", raise_e=raise_e))

    def verify_ews_login_state(self, raise_e=True):
        return self.driver.wait_for_object("sign_out_link", raise_e=raise_e)

    def verify_sign_out_successfuly_text(self, raise_e=True):
        return self.driver.wait_for_object("sign_out_successfuly_text", raise_e=raise_e)

    def verify_log_in_with_pin_dialog(self, raise_e=True):
        return self.driver.wait_for_object("log_in_with_pin_dialog_edit_box", raise_e=raise_e)

    def verify_unauthorized_dialog(self, raise_e=True):
        return self.driver.wait_for_object("unautorized_dialog", raise_e=raise_e)

    def verify_sign_in_to_access_this_site_dialog(self, raise_e=True):
        return self.driver.wait_for_object("sign_in_to_access_this_site_dialog_username_edit_box", raise_e=raise_e)

    def verify_ews_settings_page(self, raise_e=True):
        return self.driver.wait_for_object("settings_page", raise_e=raise_e)

    def verify_password_settings_page(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("new_password", timeout=timeout, raise_e=raise_e)

    def verify_password_changed_successfully_text(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("password_changed_successfully_text", timeout=timeout, raise_e=raise_e)

    def verify_access_secure_settings_dialog(self, raise_e=True):
        return self.driver.wait_for_object("log_in_with_pin_dialog_edit_box", raise_e=raise_e)

    def verify_redirecting_to_secure_page_dialog(self, raise_e=True):
        return self.driver.wait_for_object("do_not_show_check_box", raise_e=raise_e)

    def verify_incorrect_user_name_and_password_display(self, raise_e=True):
        self.driver.wait_for_object("incorrect_user_name_and_password_text", timeout=5, raise_e=raise_e)