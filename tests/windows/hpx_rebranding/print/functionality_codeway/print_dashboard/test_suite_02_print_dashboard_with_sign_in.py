import pytest
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from SAF.misc.windows_utils import resolve_to_abs_path
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_02_Print_Dashboard_With_Sign_In(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session, chrome_account_data_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]

    @pytest.mark.regression
    def test_01_print_dashboard_with_sign_in(self):
        """
        Pre-step: sign-in to the HPX app.

        """
        self.fc.launch_hpx_to_home_page()
        self.fc.hpx_sign_in_flow(web_driver=self.web_driver)
        self.fc.chrome_data_cleanup()

    @pytest.mark.regression
    def test_02_print_dashboard_with_sign_in_C58418034_C58612106(self):
        """
        Sign-in screen shows with an external browser.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/58418034
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/58612106
        """
        self.fc.add_a_printer(self.p)
        self.web_driver = self.relaunch_web_driver()
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_print_dashboard()
        try:
            self.check_and_select_account_stack()
            self.fc.sign_in(self.sign_in_email, self.sign_in_password, self.web_driver, user_icon_click=False, send_before_click=False, min_win=True)
        finally:
            if self.driver.driver_type.lower() == "windows":
                self.driver.swipe(direction="up", distance=6)
            self.fc.sign_out(hpx_logout=True)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
   
    def relaunch_web_driver(self):
        """
        Relaunch and return a new Chrome WebDriver session.
        """
        request = self.driver.session_data['request']
        ssh = self.driver.ssh
        executor_url = request.config.getoption("--mobile-device")
        profile_path = resolve_to_abs_path(ssh, "~/AppData/Local/Google/chrome/") + "User Data"
        ssh.send_command('Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force', raise_e=False)
        sleep(3)
        try:
            web_driver = c_misc.utility_web_driver(
                browser_type="chrome",
                executor_url=executor_url,
                executor_port=4444,
                profile_path=profile_path,
                request=request
        )
            return web_driver
        except Exception as e:
           print(f"Failed to relaunch web driver: {e}")
        raise
   
    def check_and_select_account_stack(self):
        """
        Check and select account stack if prompted.
        The login account type depends on build stack.
        """
        detected_stack = self.fc.check_hpx_default_stack()
        if detected_stack == "Stage":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["stage"]
        elif detected_stack == "Prod":
           onboarded_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        self.sign_in_email, self.sign_in_password = onboarded_credentials["username"], onboarded_credentials["password"]