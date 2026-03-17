from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import *
import pytest

pytest.app_info = "SMART"

def pytest_generate_tests(metafunc):
    metafunc.parametrize('account_type', ['hp+', 'ucde'], scope="class")

class Test_Suite_05_Printer_Connection_Information(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.help_center = cls.fc.flow[FLOW_NAMES.HELP_CENTER]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, account_type):
        self.fc.set_hpid_account(a_type=account_type, claimable=False, ii_status=True, force_reset=True)
        self.fc.load_smart_dashboard_help_center_printer_and_connection_info()

    def test_01_printer_support(self):
        """
        Description: C28387312, C28387313, C28715452, C28715453
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Printer And Connection Information item
          6. Click on Printer Support

        Expected Result:
          5. Verify Printer Support in a browser
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.PRINTER_SUPPORT)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    def test_02_finding_your_printer(self):
        """
        Description: C28387635, C28715454
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Printer And Connection Information item
          6. Click on Finding Your Printer button

        Expected Result:
          5. Verify Finding Your Printer screen
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.FINDING_YOUR_PRINTER)
        self.help_center.verify_finding_your_printer()

    def test_03_connecting_to_your_printer(self):
        """
        Description: C28387638, C28715455
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Printer And Connection Information item
          6. Click on Connecting to Your Printer button

        Expected Result:
          5. Verify Connecting to Your Printer screen
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.CONNECTING_TO_YOUR_PRINTER)
        self.help_center.verify_connecting_to_your_printer()

    def test_04_viewing_printer_information(self):
        """
        Description: C28387639, C28715456
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Printer And Connection Information item
          6. Click on Viewing Printer Information button

        Expected Result:
          5. Verify Viewing Printer Information screen
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.VIEWING_PRINTER_INFORMATION)
        self.help_center.verify_viewing_printer_information()

    def test_05_print_service_plugin(self):
        """
        Description: C28387640, C28715453
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Printer And Connection Information item
          6. Click on Print Service Plugin button

        Expected Result:
          5. Verify Print Service Plugin screen
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.PRINT_SERVICE_PLUGIN)
        self.help_center.verify_print_service_plugin()