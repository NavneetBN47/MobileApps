import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_02_Signed_In(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.web_driver = utility_web_session
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.css = request.cls.fc.fd["css"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.hpx_fuf = request.cls.fc.fd["hpx_fuf"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_user_able_to_sign_in_C42631241_C53303892(self):
        self.profile.click_devicepage_avatar_btn()
        self.profile.click_sign_in_from_avatar_sideflyout()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        user_initials = self.profile.get_user_initials_after_signin()
        assert user_initials in ("RG", "RP"), "User not signed in/credentials not matching"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_02_verify_signin_state_C42631242_C53303894(self):
        self.profile.click_devicepage_avatar_btn()
        self.profile.click_sign_in_from_avatar_sideflyout()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        user_initials = self.profile.get_user_initials_after_signin()
        assert user_initials in ("RG", "RP"), "User not signed in/credentials not matching"
        self.profile.click_signed_in_profile_icon()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_sign_out_btn()
        self.hpx_settings.go_home_from_settings_and_support()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
    
    @pytest.mark.regression
    def test_03_verify_profile_menu_item_is_replaced_with_account_C58443404(self):
        self.profile.click_devicepage_avatar_btn()
        self.profile.click_sign_in_from_avatar_sideflyout()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_top_profile_icon_signed_in(), "Profile icon not showing signed in state"

    @pytest.mark.regression
    def test_04_verify_redirection_of_account_link_to_https_account_hp_com_profile_C58467662(self):
        self.profile.click_devicepage_avatar_btn()
        self.profile.click_sign_in_from_avatar_sideflyout()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        self.profile.click_top_profile_icon_signed_in()
        self.profile.click_account_link()
        stack = pytest.getoption("--stack")
        if stack == "rebrand_pie":
            assert "myaccount.stage.portalshell.int.hp.com/us/en/profile" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect Webpage URL the expected url is {} but got {}".format("/us/en/profile", self.fc.fd["energy_consumption"].get_webpage_url())
        if stack == "rebrand_stage" or stack == "rebrand_production":
            assert "account.hp.com/us/en/profile" in self.fc.fd["energy_consumption"].get_webpage_url(), "Incorrect Webpage URL the expected url is {} but got {}".format("/us/en/profile", self.fc.fd["energy_consumption"].get_webpage_url())

    @pytest.mark.regression
    def test_05_verify_signin_on_welcome_navbar_sidebar_C57113512(self):
        self.profile.click_devicepage_avatar_btn()
        self.profile.click_sign_in_from_avatar_sideflyout()
        self.hpx_support.verify_browser_pane()
        assert self.hpx_support.verify_username_or_email_placeholder(), "Username or email placeholder is not present"
        self.fc.kill_hpx_process()
        self.fc.reset_myHP_app_through_command()
        self.fc.launch_myHP_and_skip_fuf()
        self.css.maximize_hp()
        self.profile.click_navbar_sign_in_button()
        self.hpx_support.verify_browser_pane()
        assert self.hpx_support.verify_username_or_email_placeholder(), "Username or email placeholder is not present"
        self.fc.kill_hpx_process()
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.app_consents.click_accept_all_button()
        self.css.maximize_hp()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.css.verify_sign_in_btn_welcome_page(), "Sign-In button on welcome screen is not present"
        self.css.click_sign_in_btn_welcome_page()
        self.hpx_support.verify_browser_pane()
        assert self.hpx_support.verify_username_or_email_placeholder(), "Username or email placeholder is not present"

    @pytest.mark.regression
    def test_06_verify_end_to_end_signin_signout_C60336441(self):
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.css.maximize_hp()
        assert self.app_consents.verify_accept_all_button_show_up()
        assert self.app_consents.verify_decline_optional_data()
        self.app_consents.click_accept_all_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        assert self.css.verify_sign_in_btn_welcome_page(), "Sign-In button on welcome screen is not present"
        self.css.click_sign_in_btn_welcome_page()
        assert self.hpx_support.verify_username_or_email_placeholder(), "Username or email placeholder is not present"
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.devicesMFE.click_profile_button()
        self.profile.verify_profile_settings_btn()
        self.profile.click_profile_settings_btn()
        self.hpx_settings.verify_sign_out_btn()
        self.hpx_settings.click_sign_out_btn()
        self.fc.close_myHP()
        self.fc.launch_myHP_and_skip_fuf()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.profile.verify_navbar_sign_in_button(), "nav bar sign-in button missing"