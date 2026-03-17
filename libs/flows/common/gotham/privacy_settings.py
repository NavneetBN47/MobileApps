from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
from selenium.webdriver.common.keys import Keys


class PrivacySettings(GothamFlow):
    flow_name = "privacy_settings"
    
    TERMS_OF_USE_LINK = "hp_smart_terms_of_use_link"
    END_USER_LICENSE_LINK = "end_user_license_agreement_link"

    ACCOUNT_DATA_LINK = "hp_print_account_data_usage_notice_link"
    DATA_COLLECTION_LINK = "data_collection_notice_link"
    PRINTER_DATA_COLLECTION_LINK = "hp_printer_data_collection_notice_link"
    PRIVACY_STATEMENT_LINK = "hp_privacy_statement_link"

    GOOGLE_ANALYTICS_LINK = "google_analytics_privacy_policy_link"
    ADOBE_ANALYTICS_LINK = "adobe_privacy_link"
    OPTIMIZELY_LINK = "optimizely_link"

    TERMS_OF_USE_URL = ["www.hpsmart.com", "tou"]
    END_USER_LICENSE_URL = ["support.hp.com", "openCLC=true"]

    ACCOUNT_DATA_URL = ["www.hpsmart.com/us/en/plain/services-data-collection-notice"]
    DATA_COLLECTION_URL = ["www.hpsmart.com/us/en/plain/data-collection-notice"]
    PRINTER_DATA_COLLECTION_URL = ["www.hpsmart.com/us/en/plain/printer-data-collection-notice"]
    PRIVACY_STATEMENT_URL = ["www.hp.com/us-en/privacy", "ww-privacy-statements"]
    
    GOOGLE_ANALYTICS_URL = ["policies.google.com"]
    ADOBE_ANALYTICS_URL = ["www.adobe.com/privacy/policy"]
    OPTIMIZELY_URL = ["www.optimizely.com/legal/privacy-notice/"]

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_link(self, link):
        """
        Click on a link
        """
        self.driver.click(link)

    def select_manage_my_privacy_preference_link(self):
        self.driver.click("manage_my_privacy_preference_link")

    def select_delete_account_data_link(self):
        self.driver.click("delete_account_data_link")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_terms_and_agreements_title(self):
        self.driver.wait_for_object("terms_and_agreements_title")
        
    def verify_hp_smart_terms_of_use_link(self):
        self.driver.wait_for_object("hp_smart_terms_of_use_link")

    def verify_end_user_license_agreement_link(self):
        self.driver.wait_for_object("end_user_license_agreement_link")

    def verify_data_collection_title(self):
        self.driver.wait_for_object("data_collection_title")

    def verify_data_collection_sub_title(self):
        self.driver.wait_for_object("data_collection_sub_title")

    def verify_hp_print_account_data_usage_notice_link(self):
        self.driver.wait_for_object("hp_print_account_data_usage_notice_link")

    def verify_data_collection_notice_link(self):
        self.driver.wait_for_object("data_collection_notice_link")

    def verify_hp_printer_data_collection_notice_link(self):
        self.driver.wait_for_object("hp_printer_data_collection_notice_link")

    def verify_hp_privacy_statement_link(self):
        self.driver.wait_for_object("hp_privacy_statement_link")

    def verify_app_improvement_title(self):
        self.driver.wait_for_object("app_improvement_title")

    def verify_app_improvement_sub_title(self):
        self.driver.wait_for_object("app_improvement_sub_title")

    def verify_google_analytics_privacy_policy_link(self):
        self.driver.wait_for_object("google_analytics_privacy_policy_link")

    def verify_adobe_privacy_link(self):
        self.driver.wait_for_object("adobe_privacy_link")

    def verify_optimizely_link(self):
        self.driver.wait_for_object("optimizely_link")

    def verify_manage_my_privacy_preference_link(self):
        self.driver.wait_for_object("manage_my_privacy_preference_link")

    def verify_delete_account_data_link(self, raise_e=True):
        return self.driver.wait_for_object("delete_account_data_link", raise_e=raise_e)

    def verify_privacy_settings_screen(self, sign_in=False):
        """
        Verify the current screen is privacy settings screen
        """
        self.verify_terms_and_agreements_title()
        self.verify_hp_smart_terms_of_use_link()
        self.verify_end_user_license_agreement_link()

        self.verify_data_collection_title()
        self.verify_data_collection_sub_title()
        self.verify_hp_print_account_data_usage_notice_link()
        self.verify_data_collection_notice_link()
        self.verify_hp_printer_data_collection_notice_link()
        self.verify_hp_privacy_statement_link()

        self.verify_app_improvement_title()
        self.verify_app_improvement_sub_title()
        self.verify_google_analytics_privacy_policy_link()
        self.verify_adobe_privacy_link()
        self.verify_optimizely_link()

        self.verify_manage_my_privacy_preference_link()
        if sign_in:
            assert self.verify_delete_account_data_link() is not False
        else:
            assert self.verify_delete_account_data_link(raise_e=False) is False

    # ---------------- Verify removed ---------------- #
    def verify_manage_my_personalized_promotion_consent_link(self, invisible=False):
        self.driver.wait_for_object("manage_my_personalized_promotion_consent_link", invisible=invisible)

    def verify_app_improvement_toggle_toggle(self, invisible=False):
        self.driver.wait_for_object("app_improvement_toggle", invisible=invisible)
    # ---------------- Verify removed ---------------- #
