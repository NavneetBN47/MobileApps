import pytest
import re
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.mac.smart.utility import smart_utilities
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_01_Ios_Smart_Send_Feedback(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.stack = request.config.getoption("--stack")
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()

    def test_01_verify_medallia_sendfeedback(self):
        """
        IOS: C33416511
        Description:
            1. Launch the app
            2. Select 'App Settings' from Bottom Navigation Bar of Home Screen
            3. Select 'Send Feedback' option under More section
        Expected Result:
            Verify that the user is directed to HP Smart Feedback page with:
                - Submit button
                - Link to HP Privacy Policy
        MAC: C39036544
        Expected Result:
            Verify that the user is directed to app store.
        """
        self.fc.go_home(stack=self.stack)
        self.home.select_app_settings()
        self.app_settings.select_send_feedback_cell()
        if pytest.platform == "MAC":
            smart_utilities.verify_app_store_opened(self.driver)
            self.driver.session_data["ssh"].send_command("pkill App\ Store")
            self.driver.activate_app(i_const.BUNDLE_ID.SMART)
            self.home.verify_home()
        else:
            self.app_settings.verify_medallia_page()
            self.app_settings.select_navigate_back()
            self.app_settings.verify_app_settings_screen()
            self.app_settings.select_send_feedback_cell()
            self.app_settings.verify_medallia_page()
            self.app_settings.select_stars()
            self.app_settings.verify_star_slider()
            stars = self.app_settings.get_star_slider_value(raise_e=False)
            if stars:
                assert float(stars) == 3
            else:
                pattern = re.compile(r'type=\"XCUIElementTypeSlider\" value=\"(\d*\.\d+|\d)\"')
                assert int(re.search(pattern, self.driver.wdvr.page_source).group(1)) == 3
            self.app_settings.verify_hp_privacy_link()
            self.app_settings.select_submit_btn()
            sleep(2)
            self.app_settings.verify_feedback_submission_popup()
            self.app_settings.select_ok()
            self.app_settings.verify_app_settings_screen()