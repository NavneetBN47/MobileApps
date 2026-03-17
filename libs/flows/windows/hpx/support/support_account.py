from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class SupportAccount(HPXFlow):
    flow_name = "support_account"

    def click_change_bill_info_link(self):
        self.driver.click("change_billing_information_link")

    def click_denial_credit_link(self):
        self.driver.click("credit_denial_link")

    def click_understanding_my_bill_link(self):
        self.driver.click("understanding_my_bill_link")

    def click_change_email_address_link(self):
        self.driver.click("change_email_address_link")

    def click_change_shipping_address_link(self):
        self.driver.click("change_shipping_address_link")

    def click_cancel_my_account_link(self):
        self.driver.click("cancel_my_account_link")

    def click_account_error_message_link(self):
        self.driver.click("account_error_message_link")

    def click_login_issues_link(self):
        self.driver.click("login_issues_link")

    def click_visit_my_account_section_link(self):
        self.driver.click("visit_my_account_section_link")

    def click_subscription_information_link(self):
        self.driver.click("subscription_information_link")

    def click_contact_hp_support_link(self):
        self.driver.click("contact_hp_support_link")

    def click_start_va_btn(self):
        self.driver.click("start_va_btn")

    def click_close_btn(self):
        self.driver.click("close_button")

    def get_start_va_btn_title(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("start_va_btn", raise_e=raise_e, timeout=timeout).text

    def get_support_account_title(self, raise_e=True, timeout=10):
        self.driver.wait_for_object("support_account_lbl", raise_e=raise_e, timeout=timeout)
        return self.driver.find_object("support_account_lbl").text
