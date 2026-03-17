import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import re
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_04_Support:

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.fc.hpx = True
        cls.home = cls.fc.fd["home"]
        cls.profile = cls.fc.fd["profile"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.help_support = cls.fc.fd["help_support"]

    def test_01_verify_support_button_redirection(self):
        """
        Description: C41562667
                1. Install and launch the app.
                2. Accept consents
                3. sign in and navigate to rootview and tap on the avatar
                4. Tap on Support option
            Expected Result:
                4.  Verify the user is directed to correct page as per design.
        """
        self.fc.go_home(reset=True, stack=self.stack, skip_sign_in=True, enable_uma_links=True)
        self.home.dismiss_hpx_whats_new_popup()
        self.home.click_sign_btn_hpx()
        self.hpid.login()
        self.home.allow_notifications_popup(raise_e=False)
        self.home.click_avatar_btn()
        self.profile.click_support_link()
        self.profile.click_goto_hp_support()
        assert bool(re.search(r'support\.hp\.com', self.help_support.get_support_link())), "Expected support.hp.com url but actual got {}".format(self.help_support.get_support_link())