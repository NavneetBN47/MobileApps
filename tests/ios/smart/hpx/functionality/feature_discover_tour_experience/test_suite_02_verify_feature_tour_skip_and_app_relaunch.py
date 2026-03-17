import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import re
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_02_Verify_Feature_Tour_Skip_and_App_Relaunch_Behavior(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.hpx = True

    def test_01_verify_feature_tour_skip_and_app_relaunch_behavior(self):
        """
        C44649094
            Perform steps under pre-condition
            Tap skip on the screen1 of the feature tour
            kill & Relaunch the app
        Verifies that user is NOT taken through feature tour after relaunch.
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True)
        self.home.verify_hpx_whats_new_popup()
        self.home.dismiss_hpx_whats_new_popup()
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.home.verify_hpx_home()