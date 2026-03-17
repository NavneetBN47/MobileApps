import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import re
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_01_Verify_Whats_New_Popup_Feature_Tour(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.hpx = True

    def test_01_pre_conditions(self):
        """
        C44649086
        Preconditions:
            Clear cache and uninstall the old app
            Fresh install the latest version of the app
            Make sure the debug switches 'Enable Web MFE' is turned ON
        Steps:
            Install and launch app.
            Accept consents
            Skip sign in and navigate to rootview
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
    
    def test_02_verify_whats_new_popup_displayed(self):
        """
        C55693112
            Install and launch the app.
            Accept consents
            Skip sign in and navigate to rootview
            Observe the device list/root view screen
        Verifies the What's new popup screen is displayed
        """
        self.home.verify_hpx_whats_new_popup()
        assert self.home.get_hpx_whats_new_popup_title() == "See what’s new!", "Title is not as expected"
        assert self.home.get_hpx_whats_new_popup_sub_title() == "Your menu options are now easier to find. Add devices, view notifications, and access account settings all in one area.", "Sub title is not as expected"
    
    def test_03_verify_second_screen_of_feature_tour_displayed(self):
        """
        C55693131
            Perform steps under pre-condition
            swipe to second screen
            Observe the 2nd screen of Feature tour
        Verifies the second screen of Feature tour is displayed
        Verifies the title and sub title of the second screen
        """
        self.driver.swipe(direction="right")
        self.home.verify_hpx_whats_new_popup_second_screen()
        assert self.home.get_hpx_whats_new_popup_second_screen_title() == "A new home for all your HP printers", "Title is not as expected"
        assert self.home.get_hpx_whats_new_popup_second_screen_sub_title() == "Simply select your printer to dive deeper into its settings and utilities, or get support when you need it.", "Sub title is not as expected"


    
    def test_04_verify_third_screen_of_feature_tour_displayed(self):
        """
        C55693153
            Perform steps under pre-condition
            swipe to second screen and then to 3rd screen
            Observe the 3rd screen of Feature tour
        Verifies the third screen of Feature tour is displayed
        Verifies the title and sub title of the third screen
        """
        self.driver.swipe(direction="right")
        self.home.verify_hpx_whats_new_popup_third_screen()
        assert self.home.get_hpx_whats_new_popup_third_screen_title() == "Discover new possibilities", "Title is not as expected"
        assert self.home.get_hpx_whats_new_popup_third_screen_sub_title() == "Check out your personalized selection of products and services—all designed to meet your unique needs.", "Sub title is not as expected"


    def test_05_verify_swipe_behavior_of_whats_new_popup(self):
        """
        C44649089
            Perform steps under pre-condition
            Swipe left and right anywhere above the buttons
        Verifies the swipe behaviour of the What's new popup by verifying the screen titles and subtitles 
        using verify_hpx_whats_new_popup_second_screen() and verify_hpx_whats_new_popup_third_screen()
        """
        self.driver.swipe(direction="left")
        self.home.verify_hpx_whats_new_popup_second_screen()
        self.driver.swipe(direction="left")
        self.home.verify_hpx_whats_new_popup()
    
    def test_06_verify_navigation_to_next_screen_of_feature_tour(self):
        """
        C56298650
            Perform steps under pre-condition
            Tap the 'Next' button on feature tour screen
            observe the behavior
        Verify the user is taken to next screen of Feature tour.
        Verfies the title and sub title of second and third screen
        """
        self.home.click_hpx_whats_new_popup_next_btn()
        self.home.verify_hpx_whats_new_popup_second_screen()
        self.home.click_hpx_whats_new_popup_next_btn()
        self.home.verify_hpx_whats_new_popup_third_screen()
    
    def test_07_verify_navigation_to_previous_screen_of_feature_tour(self):
        """
        C56298651
            Perform steps under pre-condition
            Tap the 'Back' button on feature tour screen
            observe the behavior
        Verifies the user is taken to previouse screen of Feature tour.
        Verifies the second and first screen of the feature tour
        """
        self.home.click_hpx_whats_new_popup_back_btn()
        self.home.verify_hpx_whats_new_popup_second_screen()
        self.home.click_hpx_whats_new_popup_back_btn()
        self.home.verify_hpx_whats_new_popup()

    def test_08_verify_skip_button_closes_feature_tour_and_navigates_to_rootview(self):
        """
        C56298649
            Perform steps under pre-condition
            Tap the 'Skip' button on feature tour screen (1st screen)
            observe the behaviour
        Verify the Feature tour screen is closed, and the user is taken to rootview.
        """
        self.home.dismiss_hpx_whats_new_popup()
        self.home.verify_hpx_home()
        