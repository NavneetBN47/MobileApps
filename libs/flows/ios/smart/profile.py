import logging
import pytest
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Profile(SmartFlow):
    flow_name = "profile"


    def click_profile_close_btn(self):
        """
        Click on Close button from Profile screen
        """
        self.driver.click("hpx_profile_close_btn",timeout=5)

    
    def verify_profile_close_btn(self):
        """
        Verify Close button from Profile screen
        """
        return self.driver.wait_for_object("hpx_profile_close_btn",timeout=5)
    
    def verify_profile_link(self):
        """
        Verify Profile link from Profile screen
        """
        return self.driver.wait_for_object("hpx_profile_link",timeout=5)
    
    def click_profile_settings_btn(self):
        """
        Click on Settings button from Profile screen
        """
        self.driver.click("hpx_settings_btn",timeout=5)
    
    def click_profile_feedback_btn(self):
        """
        Click on Feedback button from Profile screen
        """
        self.driver.click("hpx_feedback_btn",timeout=5)
    
    def verify_hpx_profile_feedback_btn(self, timeout=10):
        """
        Verify Feedback button from Profile screen
        """
        return self.driver.wait_for_object("hpx_feedback_btn",timeout=timeout)
    
    def click_profile_settings_page_back_btn(self):
        """
        Click on Back button from Settings page
        """
        self.driver.click("hpx_profile_settings_page_back_btn",timeout=5)
    
    def verify_settings_page_title(self):
        """
        Verify Settings page title
        """
        return self.driver.wait_for_object("hpx_profile_settings_page_title")
    
    def verify_feedback_page_title(self):
        """
        Verify Feedback page title
        """
        return self.driver.wait_for_object("hpx_feedback_page_title",timeout=5)
    
    def verify_global_nav_bar(self):
        """
        Verify Global Navigation bar
        """
        return self.driver.wait_for_object("hpx_global_nav_bar",timeout=5)
    
    def verify_profile_support_link(self):
        """
        Verify Support link from Profile screen
        """
        return self.driver.wait_for_object("hpx_profile_support_link",timeout=5)
    
    def verify_profile_subcription_link(self):
        """
        Verify Subscription link from Profile screen
        """
        return self.driver.wait_for_object("hpx_profile_subcription_link",timeout=5)
    
    def verify_profile_settings_link(self):
        """
        Verify Settings link from Profile screen
        """
        return self.driver.wait_for_object("hpx_profile_settings_link",timeout=5)

    def click_delete_your_account_link(self):
        """
        Click on delete your account link from Profile settings screen
        """
        self.driver.click("hpx_profile_delete_account_btn",timeout=5)

    def verify_profile_settings_page_back_btn(self):
        """
        Verify on Back button from Settings page
        """
        self.driver.wait_for_object("hpx_profile_settings_page_back_btn",timeout=5)

    def verify_profile_settings_btn(self):
        """
        verify on Settings button from Profile screen
        """
        self.driver.wait_for_object("hpx_settings_btn",timeout=5)
    
    def click_support_link(self):
        """
        Click on Support link from Profile screen
        """
        self.driver.click("hpx_profile_support_link",timeout=5)
    
    def click_goto_hp_support(self):
        """
        Click on Go to HP Support link from Profile screen
        """
        self.driver.click("hpx_goto_hp_support_link",timeout=5)

    def get_support_page_url(self):
        """
        Get Support page URL
        """
        return self.driver.get_attribute("hpx_support_page_url","value",timeout=5)
    
    def click_subcription_link(self):
        """
        Click on Subscription link from Profile screen
        """
        self.driver.click("hpx_profile_subcription_link",timeout=5)
    
    def click_support_back_btn(self):
        """
        Click on Back button from Support page
        """
        self.driver.click("hpx_support_back_btn",timeout=5)

    def click_profile_manage_privacy_settings_btn(self):
        """
        Click on manage privacy settings button from Profile screen
        """
        self.driver.click("hpx_manage_privacy_settings_btn",timeout=5)

    def click_profile_view_privacy_resources_btn(self):
        """
        Click on view privacy resources button from Profile screen
        """
        self.driver.click("hpx_view_privacy_resources_btn",timeout=5)

    def click_hp_privacy_statement_link(self):
        """
        Click on hp privacy statment link from Profile screen
        """
        self.driver.click("hpx_privacy_statement_link",timeout=5)

    def verify_hp_privacy_statement_link_title(self):
        """
        Verify hp privacy statement link title from Profile screen
        """
        self.driver.wait_for_object("hpx_privacy_statement_link_title")

    def click_google_analytics_policy_link(self):
        """
        click on Google Analytics privacy policy link from Profile screen
        """
        self.driver.click("hpx_google_analytics_policy_link")

    def verify_google_analytics_policy_link_title(self):
        """
        Verify on google analytics policy link from Profile screen
        """
        self.driver.wait_for_object("hpx_google_analytics_policy_link_title")

    def click_adobe_privacy_link(self):
        """
        click on Adobe privacy link from Profile screen
        """
        self.driver.click("hpx_adobe_privacy_link")

    def verify_adobe_privacy_link_title(self):
        """
        Verify on adobe privacy link from Profile screen
        """
        self.driver.wait_for_object("hpx_adobe_privacy_link_title")

    def click_optimizing_link(self):
        """
        click on optimizing link from Profile screen
        """
        self.driver.click("hpx_optimizing_link")

    def verify_optimizing_link_title(self):
        """
        Verify on optimizing link from Profile screen
        """
        self.driver.wait_for_object("hpx_optimizing_link_title")

    def click_term_of_use(self):
        """
        click on term of use link from about screen
        """
        self.driver.click("hpx_term_of_use")

    def verify_term_of_use_title(self):
        """
        click on term of use link from about screen
        """
        self.driver.click("hpx_term_of_use_link_title")

    def click_end_user_license_agreement(self):
        """
        click on End User License Agreement Link from about screen
        """
        self.driver.click("hpx_end_user_license_agreement")

    def click_legal_information(self):
        """
        click on Legal information from about screen
        """
        self.driver.click("hpx_legal_info")