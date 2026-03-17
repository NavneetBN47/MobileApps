import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const

pytest.app_info = "SMART"

class Test_Suite_03_Welcome_Flow_During_Upgarde(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_ip = cls.p.get_printer_information()["ip address"]
        cls.fc.hpx = True
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.ios_system = cls.fc.fd["ios_system"]


    def test_01_verify_user_accept_decline_before_upgrade(self):
        """
        Description : C52900620
        Install HP Smart.
        Do not accept/decline consents on welcome screen.
        Close/Kill the app on consents screen without changing anything.
        Upgrade to HPX.
        
        Expected: User will see the reskinned consents screen again on HPX app after the upgrade
        """
        self.fc.reset_app()
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.verify_click_btn()
        self.welcome_web.verify_decline_all_btn()
        self.driver.terminate_app(i_const.BUNDLE_ID.SMART)
        self.fc.go_home(stack=self.stack, skip_sign_in=True, enable_hpx_web_mfe=False)