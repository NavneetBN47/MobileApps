import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import re
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_02_UMA_Links(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()        
        cls.p = load_printers_session
        cls.edit = cls.fc.fd["edit"]
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.profile = cls.fc.fd["profile"]
        cls.stack = request.config.getoption("--stack")
        cls.printers = cls.fc.fd["printers"]
        cls.notification = cls.fc.fd["notifications"]
        cls.help_support = cls.fc.fd["help_support"]
        cls.fc.hpx = True
        
    
    def test_01_support_link(self):
        """
        C52683960
            Sign in and navigate to rootview
            Tap on the avatar
            Tap on Subscription option
            Observe
        Verifies the support link is displayed
        """
        self.fc.reset_hp_smart()
        self.fc.go_home(stack=self.stack, skip_sign_in=False, enable_uma_links=True)
        self.home.click_profile_btn()
        self.profile.click_support_link()
        self.profile.click_goto_hp_support()
        assert bool(re.search(r'support\.hp\.com', self.help_support.get_support_link())), "Expected support.hp.com url but actual got {}".format(self.help_support.get_support_link())
    
    def test_02_subscription_link(self):
        """
        C52683962
            Tap on the subscription link.
        Verifies the subscription link is displayed
        """
        # Since the link navigated to the browser, navigating back to application by relaunching the app
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.profile.click_support_back_btn()
        self.home.click_profile_btn()
        self.profile.click_subcription_link()
        assert (bool(re.search(r'(account\.hp\.com|/subscriptions)', self.help_support.get_hp_subscriptions_url()))) or self.hpid.verify_hp_id_sign_in()