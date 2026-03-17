import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_07_Privacy_Settings_Remote_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.welcome = cls.fc.fd["welcome_web"]
        cls.privacy_preference = cls.fc.fd["privacy_preference"]
        cls.home = cls.fc.fd["home"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.privacy_settings = cls.fc.fd["privacy_settings"]
        cls.printers = cls.fc.fd["printers"]

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

        cls.toggle_buttons = {"AppAnalytics" : cls.privacy_preference.APP_ANALYTICS, 
                              "Advertising" : cls.privacy_preference.ADVERTISING, 
                              "PersonalizedSuggestions" :cls.privacy_preference.PERSONALIZED_SUGGESTIONS }

        cls.webpages = {
                        "GOOGLE_ANALYTICS_P" : cls.privacy_preference.GOOGLE_ANALYTICS_LINK, 
                        "ADOBE_P" : cls.privacy_preference.ADOBE_ANALYTICS_LINK,
                        "OPTIMIZELY_P" : cls.privacy_preference.OPTIMIZELY_LINK,
                        "LEARN_MORE" : cls.privacy_preference.LEARN_MORE_LINK,
                        "TOU" : cls.privacy_preference.TERM_USE_LINK, 
                        "EULA" :cls.privacy_preference.EULA_LINK }
        
        cls.webpages_url = {
                            "GOOGLE_ANALYTICS_P" : cls.privacy_preference.GOOGLE_ANALYTICS_URL, 
                            "ADOBE_P" : cls.privacy_preference.ADOBE_ANALYTICS_URL,
                            "OPTIMIZELY_P" : cls.privacy_preference.OPTIMIZELY_URL,
                            "LEARN_MORE" : cls.privacy_preference.LEARN_MORE_URL,
                            "TOU" : cls.privacy_preference.TERM_USE_URL, 
                            "EULA" : cls.privacy_preference.EULA_URL}
    
    def test_01_add_remote_printer(self):
        """
        Verify OWS value prop shows after clicking the "Accept All" button in welcome page.
        Add a claimed printer to the carousel
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/29223891 
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_remote_printer()
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.click_back_btn()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_02_change_toggle_and_back(self, toggle_btn):
        """
        Change some toggle on the screen
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "privacy_open_toggle.png")
        self.privacy_preference.click_toggle(self.toggle_buttons[toggle_btn])
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "privacy_close_toggle.png")

    def test_03_click_back_btn(self):
        """
        Click "Back" button on the "Manage your Printer's privacy Preference" page after changing any toggle
        """
        self.privacy_preference.click_back_btn()
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_04_check_toggle_open_and_close_again(self, toggle_btn):
        """
        Verify changes are not saved
        Verify user come back to the previous page if you are coming from the printer information or printer status you should go back to the same page

        https://hp-testrail.external.hp.com/index.php?/cases/view/29224238
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "privacy_open_toggle.png")
        self.privacy_preference.click_toggle(self.toggle_buttons[toggle_btn])
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "privacy_close_toggle.png")

    def test_05_change_toggle_and_save(self):
        """
        Change some toggle on the screen
        Click the "Save" button on the "Manage your Printer's privacy Preference" screen

        Verify user changes are saved
        Verify user navigates to main page after clicking the save button

        https://hp-testrail.external.hp.com/index.php?/cases/view/29224239
        """
        self.privacy_preference.click_continue()
        self.home.select_app_settings_btn()
        self.home.select_privacy_settings_listview()
        self.privacy_settings.verify_privacy_settings_screen(sign_in=True)
        self.privacy_settings.select_manage_my_privacy_preference_link()
        self.privacy_preference.verify_privacy_preference_screen(displayed=False)

    @pytest.mark.parametrize("toggle_btn", ["AppAnalytics", "Advertising", "PersonalizedSuggestions"])
    def test_06_check_toggle_close(self, toggle_btn):
        """
        Verify toggle changes are saved after clicking "Save" button on the privacy preference page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29223934
        """
        self.fc.check_toggle_status(self.toggle_buttons[toggle_btn], "save_close_toggle.png")

    @pytest.mark.parametrize("webpage", ["GOOGLE_ANALYTICS_P", "ADOBE_P", "OPTIMIZELY_P", "LEARN_MORE", "TOU", "EULA"])
    def test_07_verify_links_on_manage_your_screen(self, webpage):
        """
        Click all the links on the "Manage your Printer Privacy Preference" screen

        Verify correct website opens in the external web browser
        Verify user still stay on the same page

        https://hp-testrail.external.hp.com/index.php?/cases/view/29224240s
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


        
