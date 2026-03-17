import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import re
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_04_Verify_Feature_Tour_Popup_Intact(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.fc.hpx = True

    def test_01_verify_tour_screen_stays_intact_on_tap_outside(self):
        """
        C44649093
            Tap anywhere outside the tour screen
        Verify the tour screen still stays intact
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.driver.touch_action.long_press(x=996, y=2048, duration=200).release().perform()
        self.device_mfe.verify_hpx_whats_new_popup()


    def test_02_verify_feature_tour_on_app_relaunch_after_kill(self):
        """
        C44677064
            kill the app without tapping Skip or Done button, while user is on any of the feature tour screen
            Relaunch the app
        Verifies that user is taken to the feature tour after relaunch.
        """
        # self.fc.reset_app()
        # self.fc.flow_load_home_screen(skip_value_prop=True)
        # self.device_mfe.verify_hpx_whats_new_popup()
        self.fc.terminate_and_relaunch_smart()
        self.device_mfe.verify_hpx_whats_new_popup()

    def test_03_verify_feature_popup_intact_after_relaunch(self):
        # Getting selenium.common.exceptions.InvalidSessionIdException error after the  foreground_and_background_smart() method
        # foreground_and_background_smart() method presses the android home key and relaunches the app
        """
        C44678626
            Background the app while the user is on any of the feature tour screen
            foreground the app
        Verifies that user is still able to continue with feature tour after launch.            
        
        self.fc.foreground_and_background_smart()
        self.device_mfe.verify_hpx_whats_new_popup()
        self.driver.swipe(direction="right")
        self.device_mfe.verify_hpx_whats_new_popup_second_screen()
        self.driver.swipe(direction="right")
        self.device_mfe.verify_hpx_whats_new_popup_third_screen()
        self.driver.swipe(direction="left")
        self.device_mfe.verify_hpx_whats_new_popup_second_screen()
        self.driver.swipe(direction="left")

        """