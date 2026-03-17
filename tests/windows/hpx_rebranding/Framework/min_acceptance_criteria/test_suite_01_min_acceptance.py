import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression")
class Test_Suite_01_Min_Acceptance(object):
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
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.bell_icon = request.cls.fc.fd["bell_icon"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.add_device= request.cls.fc.fd["add_device"]
        cls.profile.minimize_chrome()
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.fixture(scope="function", autouse=True)
    def function_setup(self):
        yield
        self.fc.close_myHP()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_01_hpx_launch_C51788442(self):
        for _ in range(4):
            self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
            self.css.maximize_hp()
            assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
            self.fc.close_myHP()

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_02_device_list_C51788457(self):
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up(), "Back button on device details page not present/loaded"
        assert self.device_card.verify_device_name_pc(), "pc device name invisible"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.ota
    def test_03_navigation_action_card_C51788461(self):
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        self.css.maximize_hp()
        self.device_card.click_pc_devices_back_button()
        self.devicesMFE.click_device_card()
        device_type_name = self.device_card.verify_devices_back_button()
        self.device_card.verify_device_name_pc()
        self.fc.swipe_window(direction="down", distance=11)
        self.device_card.verify_warrenty_status()
        self.profile.minimize_hp()
        self.hpx_settings.click_myhp_on_task_bar()
        self.device_card.click_warrenty_status_btn()
        self.device_card.verify_status_in_warranty_status()
        warranty_back_btn_text = self.device_card.verify_warranty_status_button_and_text()
        logging.info(f"Warranty Back Btn Text: '{warranty_back_btn_text}'")
        logging.info(f"Device Serial Number: '{device_type_name}'")
        assert warranty_back_btn_text == device_type_name, "The text on the back btn is incorrect"
        self.device_card.click_pc_devices_back_button()
        self.driver.swipe(direction="up", distance=11)
        assert 'button' == self.device_card.verify_devices_back_button()
        assert self.device_card.verify_device_name_pc(), "PC device name invisible "
        self.devicesMFE.click_back_button_rebranding()
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.profile.verify_devicepage_avatar_btn(), "avatar button in device page invisible"

    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.skip_in_prod
    def test_04_sidebar_functions_C51788462(self):
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        self.css.maximize_hp()
        self.profile.click_devicepage_avatar_btn()
        assert self.profile.verify_profile_side_panel(), "Profile side panel invisible"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_settings_side_panel(), "settings side panel invisible"
        assert self.hpx_settings.go_home_from_settings_and_support(), "Failed to navigate back to homepage from settings"
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up(), "Back button on device details page not present/loaded"
        self.device_card.click_bell_icon()
        notifications_title = self.bell_icon.verify_notifications_sidebar_ui()
        self.bell_icon.click_notifications_panel_close_btn()
        assert notifications_title == "Notifications"
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up(), "Back button on device details page not present/loaded"
        self.device_card.click_homepage_plus_button()
        assert self.add_device.verify_close_button_on_add_device_page(), "Close button not present on add device page"
        self.add_device.click_close_button_on_add_device_page()
