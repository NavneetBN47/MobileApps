import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_01_Web(object):
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
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.css = request.cls.fc.fd["css"]
        cls.hpid = request.cls.fc.fd["hpid"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    def test_01_verify_error_message_when_user_not_fill_mandatory_fields_C67872422(self):
        self._click_sideflyout_sign_in()
        assert self.fc.add_and_switch_to_new_window(web_driver = self.web_driver, window_name="error message test"), f"Failed to switch to browser window for error message test"
        self.profile.maximize_chrome()
        self.fc.kill_hpx_process()
        assert self.hpx_support.verify_browser_login_page(), "some elements on login page are missing/failed to load login page"
        assert self.hpx_support.verify_browser_pane(), "browser pane/tab_name failed to load"
        self.profile.maximize_chrome()
        self.hpid.click_hpid_next_button()
        assert self.hpid.verify_enter_your_email_error(), "Email error message not displayed"
        self.hpid.enter_email_adress("hpx.windows_rcb@example.com")
        self.hpid.click_hpid_next_button()
        self.hpid.click_use_password_btn()
        assert self.hpid.verify_enter_your_first_name_error(), "First name error message not displayed"
        assert self.hpid.verify_enter_your_last_name_error(), "Last name error message not displayed"
        self.web_driver.close_window(self.web_driver.current_window)
        self.profile.minimize_chrome()

    @pytest.mark.regression
    def test_02_verify_forget_your_user_name_C53303923(self):
        self._click_sideflyout_sign_in()
        assert self.hpx_support.verify_browser_login_page(), "some elements on login page are missing/failed to load login page"
        assert self.hpx_support.verify_browser_pane(), "browser pane/tab_name failed to load"
        self.profile.maximize_chrome()
        assert self.hpid.verify_forgot_your_user_name_link(), "Forgot your user name link not present"
        self.hpid.click_forgot_your_user_name_link()
        self.hpid.verify_and_recover_your_user_name(self.user_name)
        self.hpid.click_recover_username_next_btn()
        assert self.hpid.verify_username_recovery_success(), "Username recovery success message not displayed"
        self.profile.minimize_chrome()

    @pytest.mark.regression
    def test_03_verify_forget_your_password_C53303924(self):
        self._click_sideflyout_sign_in()
        self.profile.minimize_hp()
        assert self.fc.add_and_switch_to_new_window(web_driver = self.web_driver, window_name="forget your password"), f"Failed to switch to browser window for forget your password"
        self.profile.maximize_chrome()
        assert self.hpx_support.verify_browser_login_page(), "some elements on login page are missing/failed to load login page"
        assert self.hpx_support.verify_browser_pane(), "browser pane/tab_name failed to load"
        self.profile.maximize_chrome()
        self.hpid.enter_username(self.user_name)
        assert self.hpid.verify_hpid_next_button(), "Next button is not present after entering username"
        self.hpid.click_hpid_next_button()
        self.hpid.click_use_password_btn()
        assert self.hpid.verify_forgot_your_password_link(), "Forgot your password link not present"
        self.hpid.click_forgot_your_password_link()
        self.web_driver.close_window(self.web_driver.current_window)

    @pytest.mark.regression
    @pytest.mark.parametrize("invalid_inputs", ["rcb123" ,"rcb12345","RCB12345","123456","RCBWIN","()_|{})"])
    def test_04_verify_password_cannot_created_if_requirements_not_met_C67872425(self,invalid_inputs):
        self._click_sideflyout_sign_in()
        assert self.fc.add_and_switch_to_new_window(web_driver = self.web_driver, window_name="pass_requirements_test"), f"Failed to switch to browser window for password requirements test"
        self.profile.maximize_chrome()
        assert self.hpx_support.verify_browser_login_page(), "some elements on login page are missing/failed to load login page"
        self.hpid.navigate_to_password_form_on_create_account_page()
        assert self.hpid.validate_password(invalid_inputs) is False , "Password didn't meet desired requirements"
        self.web_driver.close_window(self.web_driver.current_window)

    @pytest.mark.xfail(reason="HPXAPPS-39234: Profile icon not visible after external browser sign-in", strict=False)
    @pytest.mark.regression
    def test_05_verify_close_hp_app_after_external_browser_opens_C53303914(self):
        self._click_sideflyout_sign_in()
        assert self.fc.add_and_switch_to_new_window(web_driver = self.web_driver, window_name="browser launches"), f"Failed to switch to browser window for browser launches"
        assert self.hpx_support.verify_browser_login_page(), "some elements on login page are missing/failed to load login page"
        self.fc.kill_hpx_process()
        assert self.hpx_support.verify_browser_pane(), "browser pane/tab_name failed to load"
        self.profile.maximize_chrome()
        assert self.hpid.verify_hp_id_sign_in(), "HP ID Sign-In page elements are missing/failed to load sign-in page"
        self.hpid.enter_username(self.user_name)
        assert self.hpid.verify_hpid_next_button(), "Next button is not present after entering username"
        self.hpid.click_hpid_next_button()
        assert self.hpid.verify_hpid_password_textbox(), "Password textbox is not present after clicking next"
        self.hpid.enter_password(self.password)
        self.hpid.click_sign_in_button()
        if self.css.verify_open_myhp_alert():
            self.css.click_open_myhp_alert_btn()
        self.web_driver.close_window(self.web_driver.current_window)
        assert self.profile.verify_top_profile_icon_signed_in(), "Signed in Profile icon is not visible"
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.fc.close_myHP()
        self.fc.web_password_credential_delete()
        self.profile.minimize_chrome()


######################################################################
#                           PRIVATE FUNCTION                         #
######################################################################

    def _click_sideflyout_sign_in(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon not visible on device details page"
        assert self.profile.verify_devicepage_avatar_btn(), "device page avatar button invisible"
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_sign_in_create_account_btn(), "sign-in/create acc button invisible"
        self.profile.click_sign_in_create_account_btn()
