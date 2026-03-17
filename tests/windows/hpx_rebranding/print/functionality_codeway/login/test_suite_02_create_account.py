import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_02_Create_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)

    @pytest.mark.regression
    def test_01_create_a_new_account_C55106367(self):
        """
        Test Case: Verify account creation in the HPX app
        
        Steps:
        Open the HPX app.
        Click Sign in → Create Account.
        Complete the account creation process.
        
        Expected Result:
        The user should be able to successfully create a new account in the HPX app. After completing the required details, they should receive a confirmation message or email, and be redirected to the app's home screen or login page.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/55106367
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.fd["devicesMFE"].select_my_hp_account_btn()
        self.fc.create_account_from_webpage(self.web_driver)
        self.fc.fd["devicesMFE"].verify_login_successfully()
        self.fc.sign_out(hpx_logout=True)

 