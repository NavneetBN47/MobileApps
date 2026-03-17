import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import HOME_TILES
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer


pytest.app_info = "SMART"


class Test_Suite_04_Value_Prop(object):
    
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.home = cls.fc.fd["home"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.printers = cls.fc.fd["printers"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_create_account(self):
        """
        IOS & MAC:
        C33556902, C33556892, C33556894 - Click "Create Account" button on the account creation, verify email verification shows next
        C33556895 - Click "Skip for now" link on the yeti value prop screen, verify user navigates to main UI

        """
        self.fc.go_home(stack=self.stack, button_index=2)
        self.home.verify_sign_in_icon()
        self.home.verify_create_account_icon()
        self.home.select_tile_by_name(HOME_TILES.TILE_SMART_TASK)
        if pytest.platform == "MAC":
            self.fc.create_account_from_tile(native=True)
        else:
            self.fc.create_account_from_tile()
        self.home.verify_home()
    
    def test_02_create_account_from_hpid_sign_in(self):
        """
        C33556901, C33556900 - User onboarding Sign Up flow
        """
        self.fc.go_home(reset=True, stack=self.stack, create_account=True)
    
    def test_03_setup_printer(self):
        """
        C33556897 - Click "Set Up printer" button on the ows value prop screen
        """
        self.fc.go_home(reset=True, stack=self.stack, button_index=0)
        self.printers.verify_printer_options_screen()