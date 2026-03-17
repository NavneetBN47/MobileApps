from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
class SupportHome(HPXFlow):
    flow_name = "support_home"

    def select_device_card(self, sn=None, displayed=False, timeout=30):
        self.driver.click("support_title_device_card", format_specifier=[sn], displayed=displayed, timeout=timeout)
            
    def click_back_btn(self):
        self.driver.click("back_btn", timeout=30)

    def verify_device_display(self, sn=None, timeout=30):
        return self.driver.wait_for_object("support_title_device_card", format_specifier=[sn], timeout=timeout, displayed=False, raise_e=False)

    def get_device_count(self):
        return len(self.driver.find_object("device_cards", multiple=True))

    def get_device_details(self, sn=None):
        return self.driver.wait_for_object("support_title_device_card", format_specifier=[sn]).get_attribute("Name")

    def verify_support_home_title(self):
        return self.driver.wait_for_object("support_home_title", timeout=20)

    def get_support_home_title(self):
        return self.driver.wait_for_object("support_home_title", timeout=20).text
    
    def verify_serial_number_text(self):
        return self.driver.wait_for_object("serial_number_text").get_attribute("Name")
    
    def verify_product_number_text(self):
        return self.driver.wait_for_object("sroduct_number_text").get_attribute("Name")
    
    def verify_visit_link_show(self):
        return self.driver.wait_for_object("visit_on_line_link", raise_e=False, timeout=20)
    
    def get_visit_link_title(self):
        return self.driver.wait_for_object("visit_on_line_link").get_attribute("Name")
    
    def get_support_dashboard_desc(self):
        return self.driver.wait_for_object("support_dashboard_desc").text

    def click_visit_on_line_link(self):
        self.driver.click("visit_on_line_link", timeout=10)

    def click_account_card(self):
        self.driver.click("account_card", displayed=False)

    def click_onedrive_card(self):
        self.driver.click("onedrive_card", displayed=False)

    def click_fiveg_card(self):
        self.driver.click("fiveg_card", displayed=False)

    def click_refresh_btn(self):
        self.driver.click("refresh_btn")

    def verify_refresh_btn_display(self):
        return self.driver.wait_for_object("refresh_btn", raise_e=False, timeout=10)
    
    def enter_keys_to_visit_link(self, text):
        self.driver.send_keys("visit_on_line_link", text, clear_text=False)

    def enter_keys_to_device_card(self, text, sn):
        self.driver.send_keys("support_title_device_card", text, clear_text=False, format_specifier=[sn])

    def right_click_serial_number(self, sn=None):
        el = self.driver.wait_for_object("sn_label", format_specifier=[sn], timeout=30)
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.05, height * 0.5 , right_click=True)

    def select_serial_number(self,sn=None):
        el = self.driver.wait_for_object("sn_label", format_specifier=[sn], timeout=30)
        width = el.rect["width"]
        self.driver.select_by_drag_and_drop(el, -width * 0.5, width * 0.05)

    def select_product_number(self,sn=None):
        el = self.driver.wait_for_object("pn_label", format_specifier=[sn], timeout=30)
        width = el.rect["width"]
        self.driver.select_by_drag_and_drop(el, -width * 0.5, width * 0.05)

    def verify_pn_label_display(self, sn=None):
        return self.driver.wait_for_object("pn_label", format_specifier=[sn], timeout=30)

    def verify_sn_label_display(self, sn=None):
        return self.driver.wait_for_object("sn_label", format_specifier=[sn], timeout=30)

    def verify_pname_label_display(self, sn=None):
        return self.driver.wait_for_object("pname_label", format_specifier=[sn], timeout=30)

    def right_click_product_number(self, pn=None):
        el = self.driver.wait_for_object("pn_label", format_specifier=[pn], timeout=30)
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.05, height * 0.5 , right_click=True)

    def enter_keys_to_serial_number(self, text):
        self.driver.send_keys("sn_label", text, clear_text=False)

    def enter_keys_to_product_number(self, text):
        self.driver.send_keys("pn_label", text, clear_text=False)

    def click_copy_menu_item(self):
        self.driver.click("copy_menu_item")

    def verify_copy_menu_item(self, timeout=10):
        return self.driver.wait_for_object("copy_menu_item",  raise_e=False, timeout=timeout)
    
    def verify_support_banner_show(self, timeout=10):
        return self.driver.wait_for_object("support_banner",  raise_e=False, timeout=timeout)
    
    def verify_guide_trlbl_show(self, timeout=10):
        return self.driver.wait_for_object("guide_trlbl", raise_e=False, timeout=timeout)
    
    def click_get_details_link(self, sn=None):
        self.driver.click("get_details_link", format_specifier=[sn], timeout=10)