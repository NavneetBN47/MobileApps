import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_03_Top_Nav_Bar(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile= request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.css = request.cls.fc.fd["css"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.bell_icon = request.cls.fc.fd["bell_icon"]
        cls.hpx_support = request.cls.fc.fd["hpx_support"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        request.cls.fc.web_password_credential_delete()
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_validate_topnavbar_hidden_on_scrolling_to_the_bottom_C53304006(self):
        assert self.device_card.verify_device_name_pc(), "PC device name('My Computer') not present on homepage"
        for i in range(8):
            self.driver.swipe(distance=i)
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up() is False
        assert self.css.verify_bell_icon_show_up() is False
        assert self.profile.check_signin_btn_present() is False
        assert self.css.verify_profile_icon_show_up() is False

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_02_validate_topnavbar_reappears_on_scrolling_to_the_top_C53304007(self):
        assert self.device_card.verify_device_name_pc(), "PC device name('My Computer') not present on homepage"
        for i in range(15):
            self.driver.swipe(distance=i)
        for i in range(15):
            self.driver.swipe(direction="up", distance=i)
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up()
        assert self.profile.check_signin_btn_present(), "Sign-In button is not present"
        assert self.profile.verify_devicepage_avatar_btn(), "Avatar button is not present"
        assert self.device_card.verify_bell_icon_present(), "Bell Icon is not present"

    @pytest.mark.regression
    def test_03_validate_response_of_bell_button_C53304001(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.device_card.verify_bell_icon_present(), "Bell Icon is not present"
        self.device_card.click_bell_icon()
        notifications_title = self.bell_icon.verify_notifications_sidebar_ui()
        assert notifications_title == "Notifications", "Notifications side panel not opened/title mismatch"

    @pytest.mark.regression
    def test_04_navigate_to_sign_in_page_C53304012(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.device_card.handle_feature_unavailable_popup()
        assert self.devicesMFE.verify_browser_webview_pane(), "browser webview pane not present"
        self.hpx_support.verify_browser_login_page()
        self.profile.minimize_chrome()

    @pytest.mark.regression
    def test_05_validate_app_window_resize_C53304013(self):
        self.devicesMFE.restore_app()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.device_card.verify_bell_icon_present(), "Bell Icon is not present"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.device_card.handle_feature_unavailable_popup()
        assert self.devicesMFE.verify_browser_webview_pane(), "browser webview pane not present"
        self.hpx_support.verify_browser_login_page()
        self.fc.kill_chrome_process()
