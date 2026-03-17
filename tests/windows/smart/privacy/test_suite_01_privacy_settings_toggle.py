import pytest
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_01_Privacy_Settings_Toggle(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.pepto = cls.fc.fd["pepto"]

        cls.toggle_buttons = {"AppAnalytics" : cls.privacy_preference.APP_ANALYTICS, 
                              "Advertising" : cls.privacy_preference.ADVERTISING, 
                              "PersonalizedSuggestions" :cls.privacy_preference.PERSONALIZED_SUGGESTIONS }

    def test_01_privacy_settings_listview(self):
        """
        Verify "Privacy" changed to the "Privacy Settings" in app settings pane.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17451776
        """
        self.fc.go_home()
        self.home.select_app_settings_btn()
        el = self.home.verify_privacy_settings_listview()
        assert el.text == "Privacy Settings"
        self.home.select_privacy_settings_listview()

    def test_02_data_collection(self):
        """
        Verify the "Data Collection" screen opens within the app.
        Verify toggle is removed from app improvement section.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17451777
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223925
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17451778
        """
        self.privacy_settings.verify_privacy_settings_screen()
        self.privacy_settings.verify_app_improvement_toggle_toggle(invisible=True)

    def test_03_manage_my_privacy_preference_page(self):
        """
        Verify "Manage my Privacy Preferences" link is added
        Verify "Manage your HP Smart privacy preferences" page opens in the webview within the app

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223927
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223928
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223893
        """
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)
        self.fc.check_toggle_status(self.privacy_preference.ADVERTISING, "privacy_open_toggle.png")
        self.privacy_preference.click_back_btn()

    def test_04_check_log_file(self):
        """
        Click on the "Manage my Privacy Preferences" link
        Turn on the "Advertising" toggle on the "Manage your HP Smart privacy preferences" page
        Check Gotham log file

        verify SimpeUi and System information events are sent.
        verify Gotham log shows following success string.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223932
        """
        self.driver.terminate_app()
        check_event_list = ['Ui|DataCollection:SendSimpleUiEventAction|TID:[0-9]|[\s]*SendUiEvent action:ControlButtonClicked, screen:, activity:, Path:/, mode:, control:Back, detail:, actionAuxParameters:']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_05_launch_app_to_privacy_preferences(self):
        """
        launch app and go to Privacy Preferences screen
        """
        self.driver.launch_app()
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.click_back_btn()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_06_check_toggle_open_and_close(self, toggle_btn):
        """
        Verify user can change the status of the "App Analytics" toggle.
        Verify user can change the status of the "Advertising" toggle.
        Verify user can change the status of the "Personalized Suggestions" toggle.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223894
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223895
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223896
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "privacy_open_toggle.png")
        self.privacy_preference.click_toggle(self.toggle_buttons[toggle_btn])
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "privacy_close_toggle.png")

    def test_07_click_back_btn(self):
        """
        Turn off/on few toggles on the "Manage your HP Smart privacy preferences" page
        Click Back button on the "Manage your HP Smart privacy prferences
        
        Verify changed toggle won't be restored to default after clicking "Back" button.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223902
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223933
        """
        self.privacy_preference.click_back_btn()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_08_check_toggle_open_and_close_again(self, toggle_btn):
        """
        Verify changed toggle won't be restored to default after clicking "Back" button.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223902
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "privacy_open_toggle.png")
        self.privacy_preference.click_toggle(self.toggle_buttons[toggle_btn])
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "privacy_close_toggle.png")

    def test_09_toggle_save(self):
        """
        Verify toggle changes are saved after clicking "Save" button on the privacy preference page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223934
        """
        self.privacy_preference.click_continue()
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.verify_privacy_settings_screen()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)
    
    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_10_check_toggle_close(self, toggle_btn):
        """
        Verify toggle changes are saved after clicking "Save" button on the privacy preference page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223934
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "save_close_toggle.png")

    def test_11_click_back_btn_agian(self):
        self.privacy_preference.click_back_btn()
        self.privacy_settings.verify_privacy_settings_screen()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_12_check_toggle_close(self, toggle_btn):
        """
        Verify toggle changes are saved after clicking "Save" button on the privacy preference page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223934
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "save_close_toggle.png")

    def test_13_restart_app(self):
        self.driver.restart_app()
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.verify_privacy_settings_screen()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_14_check_toggle_close(self, toggle_btn):
        """
        Verify toggle changes are saved after clicking "Save" button on the privacy preference page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223934
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "save_close_toggle.png")


    