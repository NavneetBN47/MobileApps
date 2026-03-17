import pytest
from MobileApps.libs.ma_misc import ma_misc
import re
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_03_Verify_Tour_On_Relaunch_Skip(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.device_mfe = cls.fc.hpx_fd["devicesMFE"]
        cls.fc.hpx = True
    
    def test_01_verify_tour_on_relaunch_skip(self):
        """
        C44677059
            Perform steps under pre-condition
            Tap Done button on the last screen of feature tour
            Kill & Relaunch the app
        Verifies that user is NOT taken through feature tour after relaunch.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.device_mfe.verify_hpx_whats_new_popup()
        self.driver.swipe(direction="right")
        self.driver.swipe(direction="right")
        self.device_mfe.verify_hpx_whats_new_popup_third_screen()
        self.device_mfe.click_hpx_whats_new_popup_done_btn()
        self.fc.terminate_and_relaunch_smart()
        self.device_mfe.verify_hpx_home()