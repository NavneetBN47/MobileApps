import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_02_Bell_Notifications(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.bell_icon = request.cls.fc.fd["bell_icon"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    def test_01_verify_back_button_visible_on_navigation_side_panel_C42631068(self):
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_notifications_title(), "notification title invisible"
        assert self.bell_icon.verify_notifications_panel_sign_in_btn(), "sign-in button in notification panel invisible"
        assert self.profile.verify_avatar_close_btn(), "avatar close button invisible"

    @pytest.mark.regression
    def test_02_verify_back_button_named_as_close_can_be_clicked_C42631069(self):
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_notifications_title(), "notification title invisible"
        assert self.bell_icon.verify_notifications_panel_sign_in_btn(), "sign-in button in notification panel invisible"
        close_btn_text = self.bell_icon.verify_notifications_panel_close_btn()
        assert close_btn_text == "Close", "Text on Close button is not matching or its incorrect"
        self.bell_icon.click_notifications_panel_close_btn()
        assert self.devicesMFE.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
