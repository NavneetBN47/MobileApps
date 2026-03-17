import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Signed_Out(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.css = request.cls.fc.fd["css"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_verify_avatar_icon_present_C67872421(self):
        self.devicesMFE.verify_bell_icon_show_up()
        assert self.profile.verify_devicepage_avatar_btn(), "avatar icon missing"
        self.css.verify_sign_in_button_show_up()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_02_verify_avatar_icon_clickable_C53303884(self):
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "sign-in on avatar flyout missing"
        assert self.profile.verify_avatar_close_btn(), "close button missing on profile side panel"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_03_verify_avatar_side_panel_open_C53303885(self):
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_profile_side_panel(), "profile side panel invisible"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_04_verify_close_btn_on_avatar_side_panel_C53303886(self):
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_profile_side_panel(), "profile side panel invisible"
        self.profile.click_close_avatar_btn()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_05_verify_homepage_upon_close_btn_C53303887(self):
        self.profile.click_devicepage_avatar_btn()
        self.profile.verify_profile_side_panel()
        self.profile.click_close_avatar_btn()
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon missing"
        assert self.profile.verify_devicepage_avatar_btn(), "avatar button missing"
        assert self.css.verify_sign_in_button_show_up(), "sign-in button missing"

    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.regression
    def test_06_verify_sign_in_btn_on_avatar_side_panel_C53303888(self):
        self.profile.click_devicepage_avatar_btn()
        self.profile.verify_profile_side_panel()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "sign-in on avatar flyout missing"

    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.regression
    def test_07_verify_sign_in_btn_clicked_C53303889(self):
        self.profile.click_devicepage_avatar_btn()
        self.profile.verify_profile_side_panel()
        self.profile.click_sign_in_from_avatar_sideflyout()
        self.device_card.handle_feature_unavailable_popup()
        assert self.devicesMFE.verify_browser_webview_pane(), "browser not opened on clicking sign-in"
        self.profile.minimize_chrome()

    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.regression
    def test_08_verify_user_redirected_browser_C53303890(self):
        self.profile.click_devicepage_avatar_btn()
        self.profile.verify_profile_side_panel()
        self.profile.click_sign_in_from_avatar_sideflyout()
        self.device_card.handle_feature_unavailable_popup()
        tab_name = self.hpx_support.get_browser_tab_name()
        expected_tab_name = "HP account - Google Chrome"
        assert expected_tab_name in tab_name, f"tab name mismatch: got '{tab_name}', expected tab name is {expected_tab_name}"
        self.fc.kill_chrome_process()