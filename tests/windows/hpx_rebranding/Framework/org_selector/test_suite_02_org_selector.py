import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_02_Org_Selector(object):
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

        stack = request.config.getoption("--stack")
        if stack == "rebrand_pie":
            cls.user_name, cls.password = orgid_itg_credentials["username"], orgid_itg_credentials["password"]
        elif stack == "rebrand_stage":
            cls.user_name, cls.password = orgid_stg_credentials["username"], orgid_stg_credentials["password"]
        elif stack == "rebrand_production":
            pytest.skip("Skipping suite 02 org selector tests for prod stack")
        else:
            raise RuntimeError("Please provide valid stack")
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    @pytest.mark.skip_in_stg
    def test_01_change_org_via_org_selector_menu_itg_C55685887(self):
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        assert self.profile.verify_personal_tenant_is_default(), "Personal is not the default tenant"
        self.profile.click_org_selector_button()
        assert self.profile.verify_l2_screen_of_org_selector(), "L2 Screen of org selector is not visible"
        assert self.profile.verify_smb_tenant(), "smb tenant is not present"
        self.profile.click_smb_tenant()
        assert self.profile.verify_smb_tenant_is_default(), "user is not able to change the tenant to SMB"

    @pytest.mark.regression
    @pytest.mark.skip_in_pie
    def test_02_change_org_via_org_selector_menu_stg_C66683250(self):
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        assert self.profile.verify_personal_tenant_is_default(), "Personal is not the default tenant"
        self.profile.click_org_selector_button()
        assert self.profile.verify_l2_screen_of_org_selector(), "L2 Screen of org selector is not visible"
        assert self.profile.verify_hulk_tenant(), "Hulk tenant is not present"
        self.profile.click_hulk_tenant()
        assert self.profile.verify_hulk_tenant_is_default(), "user is not able to change the tenant to hulk"

    @pytest.mark.regression
    @pytest.mark.skip_in_stg
    def test_03_verify_selected_org_persistence_after_hpx_relaunch_itg_C58949232(self):
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        assert self.profile.verify_personal_tenant_is_default(), "Personal is not the default tenant"
        self.profile.click_org_selector_button()
        assert self.profile.verify_smb_tenant(), "smb tenant is not present"
        self.profile.click_smb_tenant()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        assert self.profile.verify_smb_tenant_is_default(), "user is not able to change the tenant to SMB"
        self.fc.launch_myHP_command()
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        assert self.profile.verify_smb_tenant_is_default(), "SMB is not the default tenant after app relaunch"

    @pytest.mark.regression
    @pytest.mark.skip_in_pie
    def test_04_verify_selected_org_persistence_after_hpx_relaunch_stg_C66683544(self):
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        assert self.profile.verify_personal_tenant_is_default(), "Personal is not the default tenant"
        self.profile.click_org_selector_button()
        assert self.profile.verify_hulk_tenant(), "Hulk tenant is not present"
        self.profile.click_hulk_tenant()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        assert self.profile.verify_hulk_tenant_is_default(), "user is not able to change the tenant to hulk"
        self.fc.launch_myHP_command()
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_l1_screen_global_sidebar(), "L1 screen of global side bar is not visible"
        assert self.profile.verify_hulk_tenant_is_default(), "hulk is not the default tenant after app relaunch"