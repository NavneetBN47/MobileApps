from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow
from SAF.decorator.saf_decorator import screenshot_compare

class SmartWelcome(SmartFlow):
    flow_name = "smart_welcome"

    TERM_USE_LINK = "terms_of_use_link"
    EULA_LINK = "eula_link"
    HP_PRIVACY_STATEMENT = "hp_privacy_statement_link"
    APP_ANALYTICS = "app_analytics_toggle"	
    ADVERTISING = "advertising_toggle"	
    PERSONALIZED_SUGGESTIONS = "personalized_suggestions_toggle"

    HP_PRIVACY_URL = ["privacy", "privacy-central"]
    TOU_URL = ["tou"]
    EULA_URL = ["support.hp.com"]

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    @screenshot_compare()
    def verify_welcome_screen(self, timeout=10, raise_e=True):
        """
        Verify current screen is Welcome screen
        """
        #There are 2 contents should be shows on welcome screen, but it doesn't show at same speed, one shows up later. 
        # Developer is woking on this one to improve the screen's loading experience
        return self.driver.wait_for_object("welcome_title", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("welcome_message", timeout=timeout, raise_e=raise_e)

    def verify_click_btn(self, timeout=10, raise_e=True):
        """
        Verify Accept All button on Welcome screen
        """
        return self.driver.wait_for_object("accept_all_btn", timeout=timeout, raise_e=raise_e)

    def verify_decline_all_btn(self):
        """
        Verify Decline All button on Welcome screen
        :return:
        """
        self.driver.wait_for_object("decline_all_btn", invisible=False)
    
    def verify_decline_optional_data_btn(self, timeout=10):
        """
        Verify Decline Optional Data button on Welcome screen
        :return:
        """
        self.driver.wait_for_object("decline_optional_data_btn", timeout=timeout)

    def click_decline_optional_data_btn(self, timeout=10):
        """
        Click on Decline Optional Data button on Welcome screen
        :return:
        """
        self.driver.click("decline_optional_data_btn", timeout=timeout)
        
    def verify_learn_more_link(self):
        """
        #Legacy method from old welcome flow still used by IOS
        #Locator the same as privacy_statement_link
        """
        self.verify_hp_privacy_statement_link()

    def verify_hp_privacy_statement_link(self, timeout=10, raise_e=True):
        """
        Verify HP Privacy Statement link on Welcome screen
        :return:
        """
        self.driver.swipe(direction="down")
        return self.driver.wait_for_object("hp_privacy_statement_link", timeout=timeout, raise_e=raise_e)
    
    def click_hp_privacy_statement_link(self, timeout=10, raise_e=True):
        """
        click HP Privacy Statement link on Welcome screen
        :return:
        """
        self.driver.swipe(direction="down")
        self.driver.click("hp_privacy_statement_link", timeout=timeout, raise_e=raise_e)

    def verify_terms_of_use_link(self, timeout=10):
        self.driver.wait_for_object("terms_of_use_link", timeout=timeout)

    def verify_eula_link(self, timeout=10):
        self.driver.swipe(direction="down")
        return self.driver.wait_for_object("eula_link", timeout=timeout)

    #-----------------      SOME SCREENS AFTER CLICKING ANY LINK ---------------------
    def verify_terms_of_use_page(self, timeout=10):
        """
        Verify the page of "Terms of use" opened
        """
        self.driver.wait_for_object("term_use_page_title", timeout=timeout)
        return self.driver.get_text("term_use_page_title")

    def verify_eula_page(self, timeout=10):
        """
        Verify EULA page display via title "Select a location"
        """
        self.driver.wait_for_object("select_location_title", timeout=timeout)
        return self.driver.get_text("select_location_title")

    def verify_privacy_statement_page(self, timeout=10):
        """
        Verify 'Our Approach to Privacy" page
        """
        self.driver.wait_for_object("privacy_statement_title", timeout=timeout)
        return self.driver.get_text("privacy_statement_title")
    
    def verify_manage_options(self, raise_e=True):
        return self.driver.wait_for_object("manage_options", raise_e=raise_e)
    
    def verify_back_btn(self):
        """
        Verify on Back button
        """
        return self.driver.wait_for_object("back_btn", invisible=False)

    def verify_continue_btn(self):
        """
        Verify on Continue button
        """
        return self.driver.wait_for_object("continue_btn", invisible=False)

    def verify_manage_options(self, timeout=10):
        """
        Click on "Manage Options" button on the welcome screen
        """
        return self.driver.wait_for_object("manage_options", timeout=timeout)

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_accept_all_btn(self, timeout=10, change_check=None, retry=4):
        """
        Click on "Accept All" button on the welcome screen
        """
        self.driver.click("accept_all_btn", timeout=timeout, retry=retry, change_check=change_check)

    def click_decline_all_btn(self, timeout=10, change_check=None, retry=4):
        """
        Click on "Decline All" button on the welcome screen
        """
        self.driver.click("decline_all_btn", timeout=timeout, retry=retry, change_check=change_check)

    def click_manage_options(self, timeout=10):
        """
        Click on "Manage Options" button on the welcome screen
        """
        self.driver.click("manage_options", timeout=timeout)
        
    def click_link(self, link):
        """
        Click on a link
        :param link: use class constants:
                TERM_USE_LINK 
                EULA_LINK
                HP_PRIVACY_STATEMENT
                LEARN_MORE_LINK
        """
        self.driver.click(link)
    
    def click_app_analytics_toggle(self, timeout=10):
        """ 
        Verify App Analytics toggle on Welcome screen
        """
        self.driver.click("app_analytics_toggle", timeout=timeout)

    def is_app_analytics_toggle_disabled(self, timeout=10):
        """
        Verify App Analytics toggle is disabled on Welcome screen
        """
        toggle_element = self.driver.wait_for_object("app_analytics_toggle", timeout=timeout)    
        if toggle_element.get_attribute("checked") == "true" or toggle_element.get_attribute("aria-checked") == "true":
            raise Exception("App Analytics toggle is enabled, but it should be disabled")
        return True

    def click_advertising_toggle(self, timeout=10):
        """ 
        Verify App Analytics toggle on Welcome screen
        """
        self.driver.click("advertising_toggle", timeout=timeout)

    def is_advertising_toggle_disabled(self, timeout=10):
        """
        Verify Advertising toggle is disabled on Welcome screen
        """
        toggle_element = self.driver.wait_for_object("advertising_toggle", timeout=timeout)    
        if toggle_element.get_attribute("checked") == "true" or toggle_element.get_attribute("aria-checked") == "true":
            raise Exception("Advertising toggle is enabled, but it should be disabled")
        return True

    def click_terms_of_use_link(self, timeout=10):
        """
        Verify Terms of Use link on Welcome screen
        :return:
        """
        self.driver.swipe(direction="down")
        self.driver.click("terms_of_use_link", timeout=timeout)

    def click_eula_link(self, timeout=10):
        """
        click EULA link on Welcome screen
        """
        self.driver.swipe(direction="down")
        self.driver.click("eula_link", timeout=timeout)

    def click_back_btn(self):
        """
        Click on Back button
        """
        self.driver.click("back_btn")

    def click_continue_btn(self):
        """
        Click on Continue button
        """
        self.driver.click("continue_btn")

class AndroidSmartWelcomeNative(SmartWelcome):
    context = "NATIVE_APP"

    def verify_permission_for_advertising_screen(self, raise_e=False):  
        return self.driver.wait_for_object("allow_permission_adv_text", timeout=2, raise_e=raise_e)

class IosSmartWelcomeNative(SmartWelcome):
    context = "NATIVE_APP"

    def verify_permission_for_advertising_screen(self, raise_e=False):
        return self.driver.wait_for_object("allow_permission_adv_text", timeout=2, raise_e=raise_e)
    
    def click_continue_btn(self):
        self.driver.click("continue_btn")
    
    def click_link_native(self, link):
        """
        Click on a link
        :param link: use class constants:
                TERM_USE_LINK 
                EULA_LINK
                HP_PRIVACY_STATEMENT
                LEARN_MORE_LINK
        """

        if self.driver.wait_for_object(link, timeout=10, raise_e=False):
            self.driver.scroll(link).click()
        else:
            self.driver.click(link, displayed=False)

    def click_accept_all_btn(self, timeout=10, change_check=None, retry=4):
        """
        Click on "Accept All" button on the welcome screen
        """
        super().click_accept_all_btn(timeout=timeout, change_check=change_check, retry=retry)
    
    def verify_manage_options_title(self):
        """
        Verify Manage Options screen
        """
        self.driver.wait_for_object("manage_options_title", timeout=5)

    def click_manage_options_back_btn(self):
        """
        Click on Back button on Manage Options screen
        """
        self.driver.click("manage_options_back_btn")

    def click_manage_options_continue_btn(self):
        """
        Click on Continue button on Manage Options screen
        """
        self.driver.click("manage_options_continue_btn")
