import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import re
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_03_Verify_Tour_On_Relaunch_Skip(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.hpx = True
    
    def test_01_verify_tour_on_relaunch_skip(self):
        """
        C44677059
            Perform steps under pre-condition
            Tap Done button on the last screen of feature tour
            Kill & Relaunch the app
        Verifies that user is NOT taken through feature tour after relaunch.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.verify_hpx_whats_new_popup()
        self.driver.swipe(direction="right")
        self.driver.swipe(direction="right")
        self.home.verify_hpx_whats_new_popup_third_screen()
        self.home.click_hpx_whats_new_popup_done_btn()
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.verify_hpx_home()