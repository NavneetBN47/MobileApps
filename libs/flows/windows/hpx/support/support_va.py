from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow

class SupportVA(HPXFlow):
    flow_name = "support_va"

    def click_computer_is_slow(self):
        self.driver.click("computer_is_slow")

    def click_reset_your_operating_system(self):
        self.driver.click("reset_your_operating_system")

    def click_computer_will_not_start(self):
        self.driver.click("computer_will_not_start")

    def click_operating_system_issues(self):
        self.driver.click("operating_system_issues")

    def click_sound_issues(self):
        self.driver.click("sound_issues")

    def click_unable_to_login_to_windows(self):
        self.driver.click("unable_to_login_to_windows")

    def click_display_or_touchscreen_issues(self):
        self.driver.click("display_or_touchscreen_issues")

    def click_keyboard_or_mouse_issues(self):
        self.driver.click("keyboard_or_mouse_issues")

    def click_computer_lock_up_or_freezes(self):
        self.driver.click("computer_lock_up_or_freezes")

    def click_wireless_printer_issues(self):
        self.driver.click("wireless_printer_issues")

    def click_storage_issue_troubleshooting(self):
        self.driver.click("storage_issue_troubleshooting")

    def click_wireless_wired_bluetooth_networking_issue(self):
        self.driver.click("wireless_wired_bluetooth_networking_issue")

    def click_start_VA(self):
        self.driver.click("start_virtual_agent", change_check={"wait_obj": "va_page_title", "invisible": False}, retry=5)

    def click_feedback(self):
        self.driver.click("feedback_button")

    def click_startover(self):
        self.driver.click("startover_button")

    def click_privacy_link(self):
        self.driver.click("privacy_link")

    def click_maximize_button(self):
        self.driver.click("maximize_button")

    def click_minimize_button(self):
        self.driver.click("minimize_button", change_check={"wait_obj": "feedback_button", "invisible": True})

    def click_close_button(self):
        self.driver.click("close_button")

    def click_close_confirm_button(self):
        self.driver.click("confirm_button")

    def click_close_cancel_button(self):
        self.driver.click("cancel_button")

    def get_va_page_title(self, raise_e=True, timeout=10):
        self.driver.wait_for_object("privacy_link", raise_e=raise_e, timeout=timeout)
        return self.driver.wait_for_object("va_page_title", raise_e=raise_e, timeout=timeout).text

    def get_va_page_subtitle(self, raise_e=True, timeout=10):
        self.driver.wait_for_object("privacy_link", raise_e=raise_e, timeout=timeout)
        return self.driver.wait_for_object("va_page_subtitle", raise_e=raise_e, timeout=timeout).text

    def get_va_link(self, raise_e=True, timeout=10):
        self.driver.wait_for_object("va_link", raise_e=raise_e, timeout=timeout)
        return self.driver.find_object("va_link", multiple=True)[8].get_attribute("Value.Value")
    
    def verify_va_detail_page_opened(self, raise_e=True, timeout=15):
        self.driver.wait_for_object("privacy_link", raise_e=raise_e, timeout=timeout)
        self.driver.wait_for_object("feedback_button", raise_e=raise_e, timeout=timeout)
        self.driver.wait_for_object("startover_button", raise_e=raise_e, timeout=timeout)

    def verify_va_desc_window(self, raise_e=False, timeout=15):
        self.driver.wait_for_object("va_desc_window", raise_e=raise_e, timeout=timeout)

    def get_webchat_info(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("webchat_info", raise_e=raise_e, timeout=timeout).text