import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Set_Up_New_Printer(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_add_setup_printer_option(self):
        """
        IOS & MAC:
        C33405096
        Description:
            1. Launch the app
            2. Select 'App Settings' option
            3. Select 'Add / Set Up a Printer' option
        Expected Result:
            Verify the user is taken to Adding/ Finish setting up the printer screen with a Back button.
        """
        self.fc.go_home(stack=self.stack)
        self.home.select_app_settings()
        self.app_settings.select_set_up_new_printer_cell()
        if not pytest.platform == "MAC" and self.printers.verify_bluetooth_popup(raise_e=False):
            self.printers.handle_bluetooth_popup()
        self.printers.verify_choose_type_of_printer_screen()
        self.printers.select_get_started_button()
        self.printers.verify_set_up_printer_screen()