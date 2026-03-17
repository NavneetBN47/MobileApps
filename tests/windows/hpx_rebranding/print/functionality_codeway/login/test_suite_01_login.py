import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_01_Login(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]

        # Initializing Printer2
        cls.p2 = cls.fc.initialize_printer(printer_config="HP Envy 6100e series")
        cls.printer_name2 = cls.p2.get_printer_information()["model name"]
        cls.serial_number2 = cls.p2.get_printer_information()["serial number"]
        cls.ip2 = cls.p2.get_printer_information()["ip address"]

        yield
        delete_simulator_printer(cls.ip2, cls.serial_number2)
        
    @pytest.mark.regression
    def test_01_verify_sign_in_with_smart_account_C55101462(self):
        """
        Test Case: Verify that existing HP Smart user credentials can log in to the HPX app
        
        Steps:
        Launch the HPX app.
        Click on the Sign-in button.
        Sign in with the existing HP Smart account.
        
        Expected Result:
        The user should be able to log in to the HPX app with an existing HP Smart account.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/55101462
        """
        self.fc.launch_hpx_to_home_page()
        # The login account type depends on build stack.
        self.fc.hpx_sign_in_flow(web_driver=self.web_driver)

    @pytest.mark.regression
    def test_02_add_multi_printers_after_login_C57870724(self):
        """
        Test Case: Add Multiple Printers After Signing into HPX App
        
        Steps:
        Launch the HPX app.
        Click on the Sign-in button.
        Sign in with the existing HP Smart account in the HPX app.
        Click on (+) Add button.
        Click on Choose a printer.
        Add multiple printers from the device picker screen.
        
        Expected Result:
        User is able to select multiple printers without errors.
        Selected printers are successfully added and appear in the HPX app under the list of connected printers.
        No unexpected crashes, UI issues, or performance lags occur during the process.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/57870724
        """
        try:
            self.fc.add_a_printer(self.p)
            self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
            self.fc.add_a_printer(self.p2)
            self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name2, timeout=10)
        finally:
            self.fc.sign_out(hpx_logout=True)