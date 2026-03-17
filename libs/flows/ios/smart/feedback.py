from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Feedback(SmartFlow):
    flow_name = "feedback"

    def verify_feedback_page_title(self):
        """
        Verify Feedback page title
        """
        return self.driver.wait_for_object("hpx_feedback_page_title",timeout=5)

    def click_feedback_five_star_rating_btn(self):
        """
        Click on 5 star rating button
        """
        self.driver.click("feedback_five_star_rating_btn", timeout=5)

    def click_why_did_you_open_the_app_today_dropdown(self):
        """
        Click on "Why did you open the app today?" dropdown
        """
        self.driver.click("feedback_why_did_you_open_the_app_today_dropdown", timeout=5)

    def select_feedback_get_tech_support_option(self, timeout=10):
        """
        Select "Get Tech Support" option from the dropdown
        """
        self.driver.click("feedback_get_tech_support_option", timeout=timeout)

    def select_feedback_configure_my_devices_option(self, timeout=10):
        """
        Select "Configure my devices" option from the dropdown
        """
        self.driver.click("feedback_configure_my_devices_option", timeout=timeout)

    def select_feedback_set_up_my_printer_option(self, timeout=10):
        """
        Select "Set up my printer" option from the dropdown
        """
        self.driver.click("feedback_set_up_my_printer_option", timeout=timeout)

    def select_feedback_print_or_scan_option(self, timeout=10):
        """
        Select "Print or Scan" option from the dropdown
        """
        self.driver.click("feedback_print_or_scan_option", timeout=timeout)

    def select_feedback_manage_my_account_option(self, timeout=10):
        """
        Select "Manage my account" option from the dropdown
        """
        self.driver.click("feedback_manage_my_account_option", timeout=timeout)

    def select_feedback_manage_my_subscriptions_option(self, timeout=10):
        """
        Select "Manage my subscriptions" option from the dropdown
        """
        self.driver.click("feedback_manage_my_subscriptions_option", timeout=timeout)

    def select_feedback_other_option(self, timeout=10):
        """
        Select "Other" option from the dropdown
        """
        self.driver.click("feedback_other_option", timeout=timeout)

    def click_whats_your_feedback_related_to_dropdown(self):
        """
        Click on "What's your feedback related to?" dropdown
        """
        self.driver.click("whats_your_feedback_related_to_dropdown", timeout=5)

    def select_feedback_load_time_option(self, timeout=10):
        """
        Select "Load time" option from the dropdown
        """
        self.driver.click("feedback_load_time_option", timeout=timeout)

    def select_feedback_ease_of_use_option(self, timeout=10):
        """
        Select "Ease of use" option from the dropdown
        """
        self.driver.click("feedback_ease_of_use_option", timeout=timeout)

    def select_feedback_bug_or_issue_option(self, timeout=10):
        """
        Select "Bug or issue" option from the dropdown
        """
        self.driver.click("feedback_bug_or_issue_option", timeout=timeout)

    def select_feedback_app_feature_request_option(self, timeout=10):
        """
        Select "App feature request" option from the dropdown
        """
        self.driver.click("feedback_app_feature_request_option", timeout=timeout)

    def is_submit_feedback_btn_enabled(self):
        """
        Check if the Submit Feedback button is enabled
        """
        return self.driver.wait_for_object("submit_feedback_btn", timeout=5).is_enabled()

    def click_submit_btn(self):
        """
        Click on Submit button
        """
        self.driver.click("submit_feedback_btn", timeout=5)

    def type_in_feedback_help_us_improve_text_area(self, text, timeout=10):
        """
        Type in the "Help us improve" text area
        """
        self.driver.click("feedback_help_us_improve_text_area", timeout=timeout)
        self.driver.send_keys("feedback_help_us_improve_text_area", text)

    def type_in_can_we_contact_you_text_box(self, text, timeout=10):
        """
        Type in the "Can we contact you?" text box
        """
        self.driver.click("can_we_contact_you_text_box", timeout=timeout)
        self.driver.send_keys("can_we_contact_you_text_box",text)

    def verify_successful_feedback_submission_text(self, timeout=10):
        """
        Verify successful feedback submission text
        """
        return self.driver.wait_for_object("successful_feedback_submission_text", timeout=10)

    def click_hp_privacy_statement_link(self, timeout=10):
        """
        Click on HP Privacy Statement link
        """
        self.driver.click("hp_privacy_statement_link", timeout=timeout)

    def get_hp_privacy_statement_link_url(self, timeout=10):
        """
        Get HP Privacy Statement link URL
        """
        self.driver.wait_for_object("hp_privacy_statement_link_url", timeout=timeout)
        return self.driver.get_text("hp_privacy_statement_link_url")

    def get_feedback_help_us_improve_text_area_char_count(self, timeout=10):
        """
        Get character count of the "Help us improve" text area
        """
        return self.driver.get_attribute("feedback_help_us_improve_text_area_char_count", "name")

    def click_feedback_back_btn(self, timeout=10):
        """
        Click on Feedback back button
        """
        self.driver.click("feedback_back_btn", timeout=timeout)

    def is_invalid_email_error_message(self, timeout=10):
        """
        Check if invalid email ID message is displayed
        """
        return self.driver.wait_for_object("invalid_email_error_message", timeout=timeout)