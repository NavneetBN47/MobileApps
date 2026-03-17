from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow
from selenium.webdriver.common.keys import Keys

class PrivacyPreferences(SmartFlow):
    flow_name = "privacy_preferences"

    TERM_USE_LINK = "terms_of_use_link"
    EULA_LINK = "eula_link"
    HP_PRIVACY_STATEMENT = "hp_privacy_statement_link"
    APP_ANALYTICS = "app_analytics_toggle"
    ADVERTISING = "advertising_toggle"
    PERSONALIZED_SUGGESTIONS = "personalized_suggestions_toggle"
    GOOGLE_ANALYTICS_LINK = "google_analytics_link"
    ADOBE_ANALYTICS_LINK = "adobe_analytics_link"
    OPTIMIZELY_LINK = "optimizely_link"
    LEARN_MORE_LINK = "learn_more_link"

    GOOGLE_ANALYTICS_URL = ["google", "policies"]
    ADOBE_ANALYTICS_URL = ["adobe", "privacy", "policy"]
    OPTIMIZELY_URL = ["optimizely", "privacy"]
    LEARN_MORE_URL = ["www.hpsmart.com", "data-sharing-notice"]
    TERM_USE_URL = ["tou"]
    EULA_URL = ["support.hp.com"]

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def click_continue(self, timeout=3):
        """
        Click on "Continue" button

        - Gotham:
            If user comes from privacy settings "Manage my Privacy Preferences" link,
            there will be a "Save" button on "Manage your HP Smart privacy preferences" page.
            "Save" and "Continue" have the same locator.
        """
        self.driver.click("continue_btn", timeout=timeout)
    
    def toggle_switch(self, switch_obj: str, uncheck: bool, attribute: str="aria-checked"):
        """
        @param switch_obj:
        To toggle privacy options on manage options page 
            1. APP_ANALYTICS
            2. ADVERTISING
            3. PERSONALIZED_SUGGESTIONS
        @param uncheck: True to turn off, False to turn on
        @return:
        """
        self.driver.check_box(switch_obj, uncheck=uncheck, attribute=attribute)
    
    def click_link(self, link):
        """
        Click on a link
        :param link: use class constants:
                TERM_USE_LINK 
                EULA_LINK
                GOOGLE_ANALYTICS_LINK
                ADOBE_ANALYTICS_LINK
                OPTIMIZELY_LINK
                LEARN_MORE_LINK
        """
        if link == 'google_analytics_link':
            self.driver.send_keys("google_analytics_link", Keys.ENTER)
        else:
            self.driver.click(link)
    
    def click_back_btn(self):
        """
        CLick on Back button on privacy preferences screen

        "Continue" and "Save" button have the same locator.
        Welcome page -> privacy preference page: "Continue" button
        Home page -> Nav pane -> privacy setting -> manage my privacy preference: "Save" button
        """
        self.driver.click("back_button")

    def toggle_privacy_options(self, switch_obj: str, state: bool, attribute: str=""):
        """
        @param switch_obj:
        To toggle privacy options on manage options page 
            1. APP_ANALYTICS
            2. ADVERTISING
            3. PERSONALIZED_SUGGESTIONS
        @param state: True to turn on, False to turn off
        """
        self.driver.selenium.check_box(switch_obj, state=state, attribute=attribute)
    
    def get_switch_status(self, option: str, state: bool=True, attribute: str=""):
        """
        Get the status of toggle btn:
        @param:
            1. APP_ANALYTICS
            2. ADVERTISING
            3. PERSONALIZED_SUGGESTIONS
        """
        return self.driver.check_box(option, uncheck=state, attribute=attribute)

    # ---------------- Gotham ---------------- #
    def click_toggle(self, name):
        """
        Click the toggle.
        @param:
            1. APP_ANALYTICS
            2. ADVERTISING
            3. PERSONALIZED_SUGGESTIONS
        """
        el = self.driver.find_object(name)
        self.driver.click_by_coordinates(el)

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_privacy_preference_screen(self, timeout=10, displayed=True):
        """
        Verifying "Manage your HP Smart privacy preferences" screen

        @param displayed:
            privacy_consents_items in Gotham is_displayed() = False
        """
        self.driver.wait_for_object("manage_your_hp_smart_privacy_preference", timeout=timeout)
        if self.driver.driver_info["platform"].lower() not in ["android", "mac"]:
            self.driver.wait_for_object("privacy_consents_items", displayed=displayed)
            assert not self.driver.wait_for_object("back_arrow", raise_e=False)

class AndroidPrivacyPreferencesNative(PrivacyPreferences):
        context = "NATIVE_APP"

class MacPrivacyPreferencesNative(PrivacyPreferences):
    context = "NATIVE_APP"

    def toggle_switch(self, toggle_name):
        """
        Click the specified toggle by coordinates.
        @param:
            1. APP_ANALYTICS
            2. ADVERTISING
            3. PERSONALIZED_SUGGESTIONS
        """
        rect = self.driver.get_attribute(toggle_name, "frame")
        x = rect["x"] + rect["width"] - 60
        y = rect["y"] + rect["height"] // 2
        self.driver.click_by_coordinates(x=x, y=y)

    def click_back_btn(self):
        self.driver.click_using_frame("back_button")
    
    def click_continue(self, timeout=10):
        self.driver.click_using_frame("continue_btn", timeout=timeout)