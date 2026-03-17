import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_03_Create_Account_From_Shortcuts_Tile(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, utility_web_session, load_printers_session, logout_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.fc.web_password_credential_delete()
        cls.printer_name=cls.p.get_printer_information()["model name"]

    @pytest.mark.regression
    def test_01_add_test_printer(self):
        """
        Add a test printer.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)

    @pytest.mark.regression
    def test_02_create_a_new_account_from_shortcuts_tile_C55511629(self):
        """
        Test Case: Verify account creation from shortcuts tile in the HPX app
        
        Steps:
        Open the HPX app.
        Click shortcuts tile → Create Account.
        
        Expected Result:
        Verify Account Creation from the Shortcut Tile in the HPX App
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/55511629
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_shortcuts_tile()
        self.fc.fd["shortcuts"].click_create_account_btn()
        self.fc.create_account_from_webpage(self.web_driver)
        sleep(3)
        self.fc.fd["shortcuts"].verify_shortcuts_screen()
        self.fc.fd["shortcuts"].click_add_new_shortcuts()
        self.fc.fd["shortcuts"].verify_add_new_shortcuts_screen()
        self.fc.fd["shortcuts"].click_back_btn_on_new_shortcuts()
        self.fc.fd["shortcuts"].verify_shortcuts_screen()

 