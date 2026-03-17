import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_02_Web(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.hpid = request.cls.fc.fd["hpid"]
        request.cls.fc.web_password_credential_delete()
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    def test_01_user_navigate_to_hp_without_cancelling_web_browser_C53303913(self):
        self._click_sideflyout_sign_in()
        assert self.hpx_support.verify_browser_login_page(), "some elements on login page are missing/failed to load login page"
        self.fc.kill_hpx_process()
        self.profile.minimize_chrome()
        self.fc.launch_myHP_command()
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        self.profile.click_devicepage_avatar_btn()
        self.profile.click_sign_in_create_account_btn()
        assert self.hpx_support.verify_browser_login_page(), "some elements on login page are missing/failed to load login page"

    @pytest.mark.regression
    def test_02_user_cancel_scenario_for_external_browser_C53303912(self):
        self._click_sideflyout_sign_in()
        assert self.hpx_support.verify_browser_login_page(), "some elements on login page are missing/failed to load login page"
        self.web_driver.close_window(self.web_driver.current_window)
        self.profile.minimize_chrome()
        self.fc.launch_myHP_command()
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon is not present after closing browser"

    @pytest.mark.regression
    @pytest.mark.parametrize("valid_inputs", ["Rcb@1234" ,"rcB12345_","cb12345R","123456cR","RCBWINc2"])
    def test_03_verify_password_creation_requirement_C67872424(self,valid_inputs):
        self._click_sideflyout_sign_in() 
        assert self.fc.add_and_switch_to_new_window(web_driver = self.web_driver, window_name="pass_requirements_test"), f"Failed to switch to browser window for password requirements test"
        self.profile.maximize_chrome()
        assert self.hpx_support.verify_browser_login_page(), "some elements on login page are missing/failed to load login page"
        self.hpid.navigate_to_password_form_on_create_account_page() 
        assert self.hpid.validate_password(valid_inputs) is True, "Password didn't meet desired requirements"
        self.web_driver.close_window(self.web_driver.current_window)

    @pytest.mark.regression
    def test_04_verify_privacy_link_on_signin_page_C53303922(self):
        self._click_sideflyout_sign_in()
        assert self.fc.add_and_switch_to_new_window(web_driver = self.web_driver, window_name="privacy link test"), f"Failed to switch to browser window for privacy link test"
        assert self.hpx_support.verify_browser_pane(), "browser pane/tab_name failed to load"
        self.profile.maximize_chrome()
        assert self.hpid.verify_privacy_link(), "Privacy link not present on sign-in page"
        self.hpid.click_privacy_link()
        assert self.hpid.verify_privacy_policy_page(), "Privacy policy page not present after clicking privacy link"
        self.web_driver.close_window(self.web_driver.current_window)


######################################################################
#                           PRIVATE FUNCTION                         #
######################################################################

    def _click_sideflyout_sign_in(self):
        self.profile.minimize_chrome()
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        assert self.profile.verify_devicepage_avatar_btn(), "device page avatar button invisible"
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_sign_in_create_account_btn(), "sign-in/create acc button invisible"
        self.profile.click_sign_in_create_account_btn()
