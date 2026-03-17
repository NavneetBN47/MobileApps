import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Bell_Notifications(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.bell_icon = request.cls.fc.fd["bell_icon"]

    @pytest.mark.regression
    def test_01_verify_global_header_navigation_C60336078(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"

    @pytest.mark.regression
    def test_02_verify_global_header_navigation_includes_bellicon_C53303694(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        self.device_card.click_pc_devices_back_button()
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"

    @pytest.mark.regression
    def test_03_verify_bellicon_can_be_clicked_C53303695(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        self.device_card.click_pc_devices_back_button()
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        self.device_card.click_bell_icon()
        assert self.profile.verify_avatar_close_btn(), "avatar close button invisible"

    @pytest.mark.regression
    def test_04_verify_notifications_sidepanel_opened_upon_clicking_bellicon_C53303696(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button invisible"
        self.device_card.click_pc_devices_back_button()
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        self.device_card.click_bell_icon()
        assert self.profile.verify_avatar_close_btn(), "avatar close button invisible"
        assert self.bell_icon.verify_notifications_title(), "notification title invisible"

    @pytest.mark.regression
    def test_05_verify_empty_bell_state_when_user_not_logged_in_C53303697(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "profile icon invisible"
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_notifications_title(), "notification title invisible"
        assert self.bell_icon.verify_notifications_panel_sign_in_btn(), "sign-in button in notification panel invisible"
        assert self.profile.verify_avatar_close_btn(), "avatar close button invisible"
        self.profile.click_close_avatar_btn()

