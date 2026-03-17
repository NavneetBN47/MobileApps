import pytest
from MobileApps.libs.ma_misc import ma_misc
import re
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_02_Verify_Feature_Tour_Skip_and_App_Relaunch_Behavior(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.fc.hpx = True

    def test_01_verify_feature_tour_skip_and_app_relaunch_behavior(self):
        """
        C44649094
            Perform steps under pre-condition
            Tap skip on the screen1 of the feature tour
            kill & Relaunch the app
        Verifies that user is NOT taken through feature tour after relaunch.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.device_mfe.verify_hpx_whats_new_popup()
        self.fc.flow_hpx_skip_new_hp_app_popup()
        self.fc.terminate_and_relaunch_smart()
        self.device_mfe.verify_hpx_home()