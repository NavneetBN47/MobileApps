import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Top_Nav_Bar(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile= request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.css = request.cls.fc.fd["css"]
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_verify_avatar_flyout_elements_C53304002(self):
        assert self.profile.verify_devicepage_avatar_btn(), "avatar icon missing"
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_profile_side_panel(), "profile side panel not present"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_02_check_device_list_back_btn_C66678147(self):
        assert self.device_card.verify_pc_devices_back_button(), "devices back button not present"
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.profile.verify_devicepage_avatar_btn(), "avatar icon missing"
        assert self.device_card.verify_device_name_pc(), "PC device name('My Computer') not present on homepage"
        assert self.device_card.verify_battery_icon(), "battery icon not present"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_03_navigate_to_sign_in_page_C53304003(self):
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button not present"
        self.css.click_sign_in_button()
        self.device_card.handle_feature_unavailable_popup()
        assert self.devicesMFE.verify_browser_webview_pane(), "browser webview pane not present"
        self.hpx_support.verify_browser_login_page()
        tab_name = self.hpx_support.get_browser_tab_name()
        expected_tab_name = "HP account - Google Chrome"
        assert expected_tab_name in tab_name, "tab name mismatch/browser not launched"
        self.fc.kill_chrome_process()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_04_check_presence_of_device_back_button_C53304004(self):
        assert self.device_card.verify_pc_devices_back_button(), "devices homepage back button not present"
        self.device_card.click_pc_devices_back_button()
        assert self.devicesMFE.verify_device_card_show_up(), "Devices card is not present"
        self.devicesMFE.click_device_card()
        assert self.device_card.verify_pc_devices_back_button(), "devices homepage back button not present"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_05_validate_topnavbar_on_sign_out_C53303999(self):
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        if not logged_in:
            assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button not present"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    @pytest.mark.skip_in_prod
    def test_06_validate_all_buttons_on_topnavbar_C53303998(self):
        assert self.profile.verify_add_device_button(), "homepage plus button is not found"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon is not present"
        assert self.profile.verify_devicepage_avatar_btn(), "Profile icon is not present"
        assert self.css.verify_sign_in_button_show_up(), "sign-in button is not present"
