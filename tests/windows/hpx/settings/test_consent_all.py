from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities


pytest.app_info = "HPX"
class Test_Suite_ConsentAll(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup,utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        re = RegistryUtilities(cls.driver.ssh)
        return re
    
    def test_01_click_privacy_consents_C31681023(self):

        self.fc.re_install_app_and_skip_fuf(self.driver.session_data["installer_path"])

        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_url()
        privacy_consent_title = self.fc.fd["settings"].verify_privacy_title()
        assert privacy_consent_title == "Review privacy options"

        self.fc.fd["settings"].click_warranty_yes_button()  
        warranty_status = self.driver.wait_for_object("warranty_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert warranty_status == "true"

        self.fc.fd["settings"].click_sysinfo_yes_button()  
        sysinfo_status = self.driver.wait_for_object("sysinfo_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert sysinfo_status == "true"

        self.fc.fd["settings"].click_marketing_yes_button()  
        marketing_status = self.driver.wait_for_object("marketing_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert marketing_status == "true"

        self.fc.fd["settings"].click_warranty_no_button()
        warranty_status = self.driver.wait_for_object("warranty_consent_no_button").get_attribute("SelectionItem.IsSelected")
        assert warranty_status == "true"

        self.fc.fd["settings"].click_sysinfo_no_button()  
        sysinfo_status = self.driver.wait_for_object("sysinfo_consent_no_button").get_attribute("SelectionItem.IsSelected")
        assert sysinfo_status == "true"

        self.fc.fd["settings"].click_marketing_no_button()  
        marketing_status = self.driver.wait_for_object("marketing_consent_no_button").get_attribute("SelectionItem.IsSelected")
        assert marketing_status == "true"

        self.fc.fd["settings"].click_yes_to_all()
        warranty_status = self.driver.wait_for_object("warranty_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert warranty_status == "true"
        sysinfo_status = self.driver.wait_for_object("sysinfo_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert sysinfo_status == "true"
        marketing_status = self.driver.wait_for_object("marketing_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert marketing_status == "true"
        self.fc.fd["settings"].click_done_button()
    

    def test02_click_marketing_yes_C31681024(self, class_setup):
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_url()
        privacy_consent_title = self.fc.fd["settings"].verify_privacy_title()
        assert privacy_consent_title == "Review privacy options"
        self.fc.fd["settings"].click_privacy_url()

        self.fc.fd["settings"].click_marketing_yes_button()  
        marketing_status = self.driver.wait_for_object("marketing_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert marketing_status == "true"
        self.fc.fd["settings"].click_done_button()
        assert class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowMarketing", "Accepted") is True

    def test_03_click_support_yes_C31681025(self, class_setup):
        self.fc.fd["settings"].click_privacy_url()

        self.fc.fd["settings"].click_warranty_yes_button()  
        warranty_status = self.driver.wait_for_object("warranty_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert warranty_status == "true"
        self.fc.fd["settings"].click_done_button()
        assert class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowSupport", "Accepted") is True
    
    def test_04_click_product_yes_C31681026(self, class_setup):
        self.fc.fd["settings"].click_privacy_url()

        self.fc.fd["settings"].click_sysinfo_yes_button()  
        sysinfo_status = self.driver.wait_for_object("sysinfo_consent_yes_button").get_attribute("SelectionItem.IsSelected")
        assert sysinfo_status == "true"
        self.fc.fd["settings"].click_done_button()
        assert class_setup.get_value("HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\HP\\Consent", "AllowProductEnhancement", "Accepted") is True

    def test_05_verify_settings_module_display_C31733056(self):
        self.fc.fd["navigation_panel"].navigate_to_settings()
        settings_header  = self.fc.fd["settings"].verify_settings_header()
        assert settings_header == "Settings"

    
    def test_06_turn_on_off_notification_module_btn_C32050282(self):
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_notification_module()

        if self.fc.fd["settings"].verify_device_and_account_state() == "0":
            self.fc.fd["settings"].click_device_and_account()
            assert self.fc.fd["settings"].verify_device_and_account_state() == "1"
        else:
            self.fc.fd["settings"].click_device_and_account()
            assert self.fc.fd["settings"].verify_device_and_account_state() == "0"
        
        if self.fc.fd["settings"].verify_tips_and_tutorials() == "0":
            self.fc.fd["settings"].click_tips_and_tutorials()
            assert self.fc.fd["settings"].verify_tips_and_tutorials() == "1"
        else:
            self.fc.fd["settings"].click_tips_and_tutorials()
            assert self.fc.fd["settings"].verify_tips_and_tutorials() == "0"
        
        if self.fc.fd["settings"].verify_news_and_offers() == "0":
            self.fc.fd["settings"].click_news_and_offers()
            assert self.fc.fd["settings"].verify_news_and_offers() == "1"
        else:
            self.fc.fd["settings"].click_news_and_offers()
            assert self.fc.fd["settings"].verify_news_and_offers() == "0"
        
        if self.fc.fd["settings"].verify_share_your_feedback() == "0":
            self.fc.fd["settings"].click_share_your_feedback()
            assert self.fc.fd["settings"].verify_share_your_feedback() == "1"
        else:
            self.fc.fd["settings"].click_share_your_feedback()
            assert self.fc.fd["settings"].verify_share_your_feedback() == "0"
    
    def test_07_check_settings_UI_C31681021(self):
        self.fc.fd["navigation_panel"].navigate_to_settings()
        settings_header  = self.fc.fd["settings"].verify_settings_header()
        assert settings_header == "Settings"
        time.sleep(2)
        self.fc.fd["settings"].click_privacy_tab()
        time.sleep(2)
        assert self.fc.fd["settings"].verify_privacy_tab() is True
        assert self.fc.fd["settings"].verify_notfications_tab() is True
        assert self.fc.fd["settings"].verify_about_tab() is True

        privacy_title = self.fc.fd["settings"].verify_privacy_title()
        assert privacy_title == "Review privacy options"

        assert self.fc.fd["settings"].verify_click_here_link_show() is True
        assert self.fc.fd["settings"].verify_system_info_link_show() is True


    def test_08_hp_system_information_data_collection_C31681027(self):
        webpage = "TELEMETRY"
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_privacy_tab()
        link_name =self.fc.fd["settings"].verify_hp_system_link()
        assert link_name=="HP System Information Data Collection External Link","Link is not visible"
        self.fc.fd["settings"].click_hp_system_info_sys_data_collection_url()
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        current_url = self.web_driver.get_current_url()
        assert current_url == "https://www.hppstelemetry.com/"
  
    def test_09_about_defaultcheck_C32009900(self):
        print("Clicking on about tab")
        self.fc.fd["settings"].click_about_tab()
        print("Check default")
        myHPtext_display=self.fc.fd["settings"].verify_about_myHPtext() 
        assert  myHPtext_display=="myHP"
        privacylink_display= self.fc.fd["settings"].verify_about_privacyPolicy_link()
        assert privacylink_display=="HP Privacy Policy External Link"
        useraggrementlink_display=self.fc.fd["settings"].verify_about_userLicenceAgreement_link() 
        assert  useraggrementlink_display=="HP End User License Agreement External Link"
  
    def test_10_verify_about_links_C32010199(self):
        self.fc.fd["settings"].click_about_tab()
        self.fc.fd["settings"].click_privacyink()
        webpage = "PRIVACY"
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        current_url = self.web_driver.get_current_url()
        assert current_url == "https://www.hp.com/us-en/privacy/privacy-central.html"
        self.fc.fd["settings"].click_useragreement()
        webpage = "USERAGREEMENT"
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        current_url = self.web_driver.get_current_url()
        assert current_url == "https://support.hp.com/us-en/document/ish_4416646-4390016-16?openCLC=true"

        
