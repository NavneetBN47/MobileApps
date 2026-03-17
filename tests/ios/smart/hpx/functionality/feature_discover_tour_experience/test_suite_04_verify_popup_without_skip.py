import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import re
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_04_Verify_Feature_Tour_Popup_Intact(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.hpx = True

    def test_01_verify_tour_screen_stays_intact_on_tap_outside(self):
        # As per the click the element outside the tour screen but getting no such element exception but present in the page source
        """
        C44649093
            tap anywhere outside the tour screen
        Verify the tour screen still stays intact
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=True)
        self.driver.touch_action.long_press(x=996, y=2048, duration=200).release().perform()
        self.home.verify_hpx_whats_new_popup()


    def test_02_verify_feature_tour_on_app_relaunch_after_kill(self):
        """
        C44677064
            kill the app without tapping Skip or Done button, while user is on any of the feature tour screen
            Relaunch the app
        Verifies that user is taken to the feature tour after relaunch.
        """
        self.home.verify_hpx_whats_new_popup()
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.verify_hpx_whats_new_popup()

    def test_03_verify_feature_popup_intact_after_relaunch(self):
        """
        C44678626
            Background the app while the user is on any of the feature tour screen
            foreground the app
        Verifies that user is still able to continue with feature tour after launch.            
        """
        self.driver.launch_app(i_const.BUNDLE_ID.SETTINGS)
        self.driver.terminate_app(i_const.BUNDLE_ID.SETTINGS)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.verify_hpx_whats_new_popup()
        self.driver.swipe(direction="right")
        self.home.verify_hpx_whats_new_popup_second_screen()
        self.driver.swipe(direction="right")
        self.home.verify_hpx_whats_new_popup_third_screen()
        self.driver.swipe(direction="left")
        self.home.verify_hpx_whats_new_popup_second_screen()
        self.driver.swipe(direction="left")