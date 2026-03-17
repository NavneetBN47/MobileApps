import pytest
from MobileApps.libs.ma_misc import ma_misc
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_02_Privacy_Settings_Link(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack = cls.stack, a_type = "ucde")

        cls.webpages = {"TERMS" : cls.privacy_settings.TERMS_OF_USE_LINK,
                        "EULA_1" : cls.privacy_settings.END_USER_LICENSE_LINK,
                        "ACCOUNT" : cls.privacy_settings.ACCOUNT_DATA_LINK, 
                        "DATA_COLLECTION" : cls.privacy_settings.DATA_COLLECTION_LINK, 
                        "PRINTER_DATA" : cls.privacy_settings.PRINTER_DATA_COLLECTION_LINK, 
                        "PRIVACY" : cls.privacy_settings.PRIVACY_STATEMENT_LINK, 
                        "GOOGLE" :cls.privacy_settings.GOOGLE_ANALYTICS_LINK,
                        "ADOBE" :cls.privacy_settings.ADOBE_ANALYTICS_LINK,
                        "OPTIMIZELY" :cls.privacy_settings.OPTIMIZELY_LINK,
                        "GOOGLE_ANALYTICS_P" : cls.privacy_preference.GOOGLE_ANALYTICS_LINK, 
                        "ADOBE_P" : cls.privacy_preference.ADOBE_ANALYTICS_LINK,
                        "OPTIMIZELY_P" : cls.privacy_preference.OPTIMIZELY_LINK,
                        "LEARN_MORE" : cls.privacy_preference.LEARN_MORE_LINK,
                        "TOU" : cls.privacy_preference.TERM_USE_LINK, 
                        "EULA_2" :cls.privacy_preference.EULA_LINK }
        
        cls.webpages_url = {"TERMS" : cls.privacy_settings.TERMS_OF_USE_URL, 
                            "EULA_1" : cls.privacy_settings.END_USER_LICENSE_URL,
                            "ACCOUNT" : cls.privacy_settings.ACCOUNT_DATA_URL,
                            "DATA_COLLECTION" : cls.privacy_settings.DATA_COLLECTION_URL,
                            "PRINTER_DATA" : cls.privacy_settings.PRINTER_DATA_COLLECTION_URL, 
                            "PRIVACY" : cls.privacy_settings.PRIVACY_STATEMENT_URL,
                            "GOOGLE" : cls.privacy_settings.GOOGLE_ANALYTICS_URL, 
                            "ADOBE" : cls.privacy_settings.ADOBE_ANALYTICS_URL,
                            "OPTIMIZELY" : cls.privacy_settings.OPTIMIZELY_URL,
                            "GOOGLE_ANALYTICS_P" : cls.privacy_preference.GOOGLE_ANALYTICS_URL, 
                            "ADOBE_P" : cls.privacy_preference.ADOBE_ANALYTICS_URL,
                            "OPTIMIZELY_P" : cls.privacy_preference.OPTIMIZELY_URL,
                            "LEARN_MORE" : cls.privacy_preference.LEARN_MORE_URL,
                            "TOU" : cls.privacy_preference.TERM_USE_URL, 
                            "EULA_2" : cls.privacy_preference.EULA_URL}

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)

    def test_01_go_home_and_sign_in(self):
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])

    def test_02_link_removed(self):
        """
        w/ account signed in

        Verify "Manage my Personalized Promotion consent" link is removed.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223926
        """
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.verify_privacy_settings_screen(sign_in=True)
        self.privacy_settings.verify_manage_my_personalized_promotion_consent_link(invisible=True)

    @pytest.mark.parametrize("webpage", ["TERMS", "EULA_1", "ACCOUNT", "DATA_COLLECTION", "PRINTER_DATA", "PRIVACY", "GOOGLE", "ADOBE", "OPTIMIZELY"])
    def test_03_verify_links_on_privacy_settings_screen(self, webpage):
        """
        Verify the correct page open after clicking "HP Smart Terms of Use" link on the Privacy Settings page.
        Verify the correct page open after clicking "End User License Agreement" link on the Privacy Settings page.
        Verify the correct page open after clicking "HP Print Account Data Usage Notice" link on the Privacy Settings page.
        Verify the correct page open after clicking "Data Collection Notice for the HP Smart Experience" link on the Privacy Settings page.
        Verify the correct page open after clicking "HP Printer Data Collection Notice" link on the Privacy Settings page.
        Verify the correct page open after clicking "HP Privacy statement" link on the Privacy Settings page.
        Verify the correct page open after clicking  "Google Analytics Privacy Policy" link on the Privacy Settings page.
        Verify the correct page open after clicking "Adobe Privacy" link on the Privacy Settings page.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28001818
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28001819
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28001820
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28001821
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28001822
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33631789
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33631790
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33631791
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33631792
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33631793
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/33631788

        """
        self.privacy_settings.click_link(self.webpages[webpage])
        self.web_driver.add_window(webpage)

        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.privacy_settings.click_link(self.webpages[webpage])
            self.web_driver.add_window(webpage)
        sleep(3)
        self.web_driver.switch_window(webpage)
        sleep(3)
        current_url = self.web_driver.get_current_url()

        for sub_url in self.webpages_url[webpage]:
            assert sub_url in current_url

    def test_04_go_to_privacy_preference_screen(self):
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("webpage", ["GOOGLE_ANALYTICS_P", "ADOBE_P", "OPTIMIZELY_P", "LEARN_MORE", "TOU", "EULA_2"])
    def test_05_verify_links_on_privacy_preference_screen(self, webpage):
        """
        Verify the correct website opens after clicking the "Google Analytics" link.
        Verify the correct website opens after clicking the "Adobe Analytics" link.
        Verify the correct website opens after clicking the "Optimizely" link.
        Verify the correct website opens after clicking the "Learn more" link.
        Verify the correct website opens after clicking the "Terms of Use" link.
        Verify the correct website opens after clicking the "End User License Agreement" link.

        Verify app is still showing the "Manage your HP Smart privacy preferences" page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223899
          -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223898
          -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223938
          -> https://hp-testrail.external.hp.com/index.php?/cases/view/33631789
        """
        self.privacy_preference.click_link(self.webpages[webpage])
        self.web_driver.add_window(webpage)

        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.privacy_preference.click_link(self.webpages[webpage])
            self.web_driver.add_window(webpage)
        sleep(3)
        self.web_driver.switch_window(webpage)
        sleep(3)
        current_url = self.web_driver.get_current_url()

        for sub_url in self.webpages_url[webpage]:
            assert sub_url in current_url
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

