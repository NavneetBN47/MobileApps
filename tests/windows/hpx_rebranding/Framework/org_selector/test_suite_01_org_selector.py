import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_01_Org_Selector(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.web_driver = utility_web_session
        cls.profile= request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        request.cls.fc.web_password_credential_delete()
        orgid_itg_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["orgid_itg"]
        orgid_stg_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["orgid_stg"]
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]

        stack = request.config.getoption("--stack")
        if stack == "rebrand_pie":
            cls.user_name1, cls.password1 = orgid_itg_credentials["username"], orgid_itg_credentials["password"]
        elif stack == "rebrand_stage":
            cls.user_name1, cls.password1 = orgid_stg_credentials["username"], orgid_stg_credentials["password"]
        elif stack == "rebrand_production":
            pytest.skip("Skipping suite 01 org selector tests for prod stack")
        else:
            raise RuntimeError("Please provide valid stack")
        cls.user_name2, cls.password2 = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    @pytest.mark.skip_in_pie
    def test_01_global_sidebar_ui_visibility_for_signed_in_users_stg_build_C55685882(self):
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name1, self.password1, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"

    @pytest.mark.regression
    def test_02_global_side_bar_ui_visibility_with_signed_out_users_C55685883(self):
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_profile_side_panel(), "global side bar UI is not visible"
        assert self.profile.verify_org_selector_button() is False

    @pytest.mark.regression
    def test_03_global_sidebar_ui_signed_in_with_single_tenant_account_C55685884(self):
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name2, self.password2, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_global_sidebar_signed_in(), "global side bar UI invisible"
        assert self.profile.verify_org_selector_button() is False

    @pytest.mark.regression
    def test_04_signed_in_with_multi_tenant_account_C55685885(self):
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name1, self.password1, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        assert self.profile.verify_org_selector_button() is not False, "org selector button is not functional"

    @pytest.mark.regression
    def test_05_by_default_org_selected_as_personal_C55685886(self):
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name1, self.password1, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        assert self.profile.verify_personal_tenant_is_default(), "Personal is not the default tenant"

    @pytest.mark.regression
    def test_06_l2_screen_visibility_in_org_selector_menu_C55685888(self):
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name1, self.password1, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        self.profile.click_org_selector_button()
        assert self.profile.verify_l2_screen_of_org_selector(), "L2 Screen of org selector is not visible"

    @pytest.mark.regression
    def test_07_revert_to_global_sidebar_screen_from_org_selector_l2_screen_C55685890(self):
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name1, self.password1, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        self.profile.click_org_selector_button()
        assert self.profile.verify_l2_screen_of_org_selector(), "L2 Screen of org selector is not visible"
        self.profile.click_org_selector_menu_back_button()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"

    @pytest.mark.regression
    @pytest.mark.skip_in_stg
    def test_08_global_sidebar_ui_visibility_for_signed_in_users_itg_build_C65903590(self):
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name1, self.password1, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"