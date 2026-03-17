import pytest
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_04_Welcome_Privacy_Link(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.welcome = cls.fc.fd["welcome_web"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]

        cls.webpages = {"PRIVACY" : cls.welcome.HP_PRIVACY_STATEMENT, 
                        "TOU_W" : cls.welcome.TERM_USE_LINK, 
                        "EULA_W" :cls.welcome.EULA_LINK,
                        "GOOGLE_ANALYTICS" : cls.privacy_preference.GOOGLE_ANALYTICS_LINK, 
                        "ADOBE" : cls.privacy_preference.ADOBE_ANALYTICS_LINK,
                        "OPTIMIZELY" : cls.privacy_preference.OPTIMIZELY_LINK,
                        "LEARN_MORE" : cls.privacy_preference.LEARN_MORE_LINK,
                        "TOU_P" : cls.privacy_preference.TERM_USE_LINK, 
                        "EULA_P" :cls.privacy_preference.EULA_LINK } 
        
        cls.webpages_url = {"PRIVACY" : cls.welcome.HP_PRIVACY_URL, 
                            "TOU_W" : cls.welcome.TOU_URL, 
                            "EULA_W" : cls.welcome.EULA_URL,
                            "GOOGLE_ANALYTICS" : cls.privacy_preference.GOOGLE_ANALYTICS_URL, 
                            "ADOBE" : cls.privacy_preference.ADOBE_ANALYTICS_URL,
                            "OPTIMIZELY" : cls.privacy_preference.OPTIMIZELY_URL,
                            "LEARN_MORE" : cls.privacy_preference.LEARN_MORE_URL,
                            "TOU_P" : cls.privacy_preference.TERM_USE_URL, 
                            "EULA_P" : cls.privacy_preference.EULA_URL }

    def test_01_verify_app_installation_and_launch(self):
        self.welcome.verify_manage_options()
        
    @pytest.mark.parametrize("webpage", ["PRIVACY", "TOU_W", "EULA_W"])
    def test_02_verify_links_on_welcome_screen(self, webpage):
        """
        Verify the correct website opens after clicking the "HP Privacy Statement" link.
        Verify the correct website opens after clicking the "Term of USE" link.
        Verify the correct website opens after clicking the "End User License Agreement" link.
        Verify app is still on the welcome screen.        

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223888
        """
        self.welcome.click_link(self.webpages[webpage])
        self.web_driver.add_window(webpage)

        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.welcome.click_link(self.webpages[webpage])
            self.web_driver.add_window(webpage)
        sleep(3)
        self.web_driver.switch_window(webpage)
        sleep(3)
        current_url = self.web_driver.get_current_url()

        for sub_url in self.webpages_url[webpage]:
            assert sub_url in current_url
        self.welcome.verify_welcome_screen()
    
    def test_03_go_to_privacy_preference_screen(self):
        """
        Verify "Manage your HP Smart privacy preferences" page shows after clicking the "Manage Options" button in welcome page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223893
        """
        self.welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("webpage", ["GOOGLE_ANALYTICS", "ADOBE", "OPTIMIZELY", "LEARN_MORE", "TOU_P", "EULA_P"])
    def test_04_verify_links_on_privacy_preference_screen(self, webpage):
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

