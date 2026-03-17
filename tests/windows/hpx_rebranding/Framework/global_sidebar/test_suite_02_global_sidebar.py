import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from selenium.webdriver.common.keys import Keys

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_02_Global_Side_Bar(object):
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
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.accessibility = request.cls.fc.fd["accessibility"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.profile.minimize_chrome()
        cls.accessibility = request.cls.fc.fd["accessibility"]
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_user_signed_in_C53303682(self):
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_global_sidebar_signed_in(), "global side bar UI invisible"
        assert self.profile.verify_account_link(), "account link invisible"
        self.profile.click_account_link()
        self.device_card.handle_feature_unavailable_popup()
        tab_name = self.hpx_support.get_browser_tab_name()
        expected_tab_content = "HP Account"
        assert expected_tab_content in tab_name, "tab name mismatch/browser not launched"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_02_navigate_to_subscription_page_C53303685(self):
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_global_sidebar_signed_in(), "global side bar UI invisible"
        assert self.profile.verify_subscriptions_link(), "subscription link invisible"
        self.profile.click_subscriptions_link()
        self.device_card.handle_feature_unavailable_popup()
        self.devicesMFE.verify_browser_webview_pane()
        tab_name = self.hpx_support.get_browser_tab_name()
        expected_tab_content = "HP Account"
        assert expected_tab_content in tab_name, "tab name mismatch/browser not launched"

    @pytest.mark.regression
    def test_03_verify_right_click_after_launching_application_C60306338(self):
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up()
        el = self.driver.find_object("hp_app_window_title")
        el.send_keys("SHIFT+F10")
        assert not self.accessibility.refresh_btn_is_disabled(), "Refresh is not displayed in title bar context menu"

    @pytest.mark.regression
    def test_04_verify_global_side_flyout_C62508775(self):
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_global_sidebar_signed_in(), "global side bar UI invisible"
        assert self.profile.verify_account_link(), "account link invisible"

    @pytest.mark.regression
    def test_05_verify_account_menu_C58468872(self):
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.devicesMFE.verify_browser_webview_pane()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.profile.click_top_profile_icon_signed_in()
        assert self.profile.verify_global_sidebar_signed_in(), "global side bar UI invisible"
        assert self.profile.verify_account_link(), "account link invisible"
        username = self.driver.wait_for_object("username_text", raise_e=False, timeout=10)
        username.send_keys(Keys.TAB)
        assert self.profile.verify_account_focused_text(), "Account menu item is not focused"

    @pytest.mark.regression
    def test_06_account_link_is_not_visible_without_signin_C58468910(self):
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.profile.click_profile_icon_show_up()
        assert self.profile.verify_account_link() == False, "account link invisible"

