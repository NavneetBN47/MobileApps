from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow

class AddDevice(HPXRebrandingFlow):
    flow_name = "add_device"

    def verify_add_device_page(self):
        if self.driver.wait_for_object("add_device_page_side_bar"):
            self.driver.wait_for_object("add_device_title")
            self.driver.wait_for_object("add_printer_section")
            self.driver.wait_for_object("missing_device_section")
            return True
        else:
            return False

    def verify_open_hp_smart_link(self):
        return self.driver.wait_for_object("open_hp_smart_link")

    def verify_microsoft_store_opened(self):
        return self.driver.wait_for_object("microsoft_store")

    def verify_search_by_serial_number_btn(self):
        return self.driver.wait_for_object("search_by_serial_number_btn")

    def verify_serial_number_textbox(self):
        return self.driver.wait_for_object("serial_number_textbox")

    def verify_need_help_finding_your_serial_number_link(self):
        return self.driver.wait_for_object("need_help_finding_your_serial_number_link")

    def verify_add_a_device_back_btn(self):
        return self.driver.wait_for_object("add_a_device_back_btn")

    def verify_close_button_on_add_device_page(self):
        return self.driver.wait_for_object("close_button_on_add_device_page")

    def verify_add_printer_content(self):
        return self.driver.wait_for_object("add_printer_content")

    def verify_missing_device_content(self,timeout=15):
        return self.driver.wait_for_object("missing_device_content",timeout=timeout)
    
    def verify_hp_smart_text(self):
        return self.driver.wait_for_object("hp_smart_text")
    
    def verify_hp_smart_open_btn(self):
        return self.driver.wait_for_object("hp_smart_open_btn")

    def verify_newly_added_devicename(self, raise_e=False):
        return self.driver.wait_for_object("newly_added_device_card_name", raise_e=raise_e, timeout=10)

    def input_enter_product_number(self, product_number):
        self.driver.send_keys("product_number_textbox", product_number)
 
    def verify_product_number_textbox(self, raise_e=False):
        return self.driver.wait_for_object("product_number_textbox", raise_e=raise_e, timeout=10)


############################################# Action flows #############################################

    def click_open_hp_smart_link(self):
        self.driver.click("open_hp_smart_link", timeout = 10)

    def click_search_by_serial_number_btn(self):
        self.driver.click("search_by_serial_number_btn", timeout = 10)

    def click_need_help_finding_your_serial_number_link(self):
        self.driver.click("need_help_finding_your_serial_number_link", timeout = 10)

    def click_add_a_device_back_btn(self):
        self.driver.click("add_a_device_back_btn", timeout = 10)

    def click_close_button_on_add_device_page(self):
        self.driver.click("close_button_on_add_device_page", timeout = 10)

    def click_close_microsoft_store(self):
        self.driver.click("close_microsoft_store", timeout = 10)

    def input_enter_serial_number(self, serial_number):
        self.driver.send_keys("serial_number_textbox", serial_number)

    def get_entered_serial_number(self):
        return self.driver.get_attribute("serial_number_textbox", "Value.Value")

    def click_add_device_hyperlink(self):
        self.driver.click("add_device_hyperlink", timeout=10)
 
    