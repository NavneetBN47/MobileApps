import pytest
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_03_Welcome_Privacy_Toggle(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        
        cls.toggle_buttons = {"AppAnalytics" : cls.privacy_preference.APP_ANALYTICS, 
                    "Advertising" : cls.privacy_preference.ADVERTISING, 
                    "PersonalizedSuggestions" :cls.privacy_preference.PERSONALIZED_SUGGESTIONS }

    def test_01_go_to_privacy_preference_screen(self):
        """
        Click the "Manage Options" button on the welcome screen

        Verify "Manage your HP Smart privacy preferences" page shows after clicking the "Manage Options" button in welcome page.
        Verify all the time detail information is expanded for all the options on the Manage your HP Smart privacy preferences screen
       
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223893
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223897
        """
        self.welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_02_verify_privacy_preferences_toggleable(self, toggle_btn):
        """
        Verify user can change the status of the "App Analytics" toggle.
        Verify user can change the status of the "Advertising" toggle.
        Verify user can change the status of the "Personalized Suggestions" toggle.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223894
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223895
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223896
        """ 
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "welcome_close_toggle.png")  
        self.privacy_preference.click_toggle(self.toggle_buttons[toggle_btn])
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "welcome_open_toggle.png") 

    def test_03_click_back_btn(self):
        self.privacy_preference.click_back_btn()
        self.welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_04_check_toggle_open(self, toggle_btn):
        """
        Verify toggle changes are saved after clicking "Save" button on the privacy preference page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223934
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "privacy_open_toggle.png") 

    def test_05_toggle_save(self):
        """
        Verify toggle changes are saved after clicking "Save" button on the privacy preference page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223934
        """
        self.privacy_preference.click_continue()
        self.ows_value_prop.verify_windows_ows_value_prop_screen()
        self.ows_value_prop.select_native_value_prop_buttons(index=3)
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.verify_privacy_settings_screen()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_06_check_toggle_open(self, toggle_btn):
        """
        Verify toggle changes are saved after clicking "Save" button on the privacy preference page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223934
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "save_open_toggle.png") 

    def test_07_click_back_btn_agian(self):
        self.privacy_preference.click_back_btn()
        self.privacy_settings.verify_privacy_settings_screen()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_08_check_toggle_open(self, toggle_btn):
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "save_open_toggle.png") 

    def test_09_restart_app(self):
        self.driver.restart_app()
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.verify_privacy_settings_screen()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_10_check_toggle_open(self, toggle_btn):
        """
        Verify toggle changes are saved after clicking "Save" button on the privacy preference page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223934
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "save_open_toggle.png") 
