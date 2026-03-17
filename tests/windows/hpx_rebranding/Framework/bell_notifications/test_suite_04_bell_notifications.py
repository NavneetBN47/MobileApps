import logging
import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_04_Bell_Notifications(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.css = request.cls.fc.fd["css"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.bell_icon = request.cls.fc.fd["bell_icon"]
        cls.profile = request.cls.fc.fd["profile"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        request.cls.fc.web_password_credential_delete()
        cls.user_name = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]["username"]
        cls.password = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]["password"]

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_01_verify_bell_notifications_displayed_when_logged_in_C60339087(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon is not present"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()

        notification_type = self.bell_icon.verify_urgent_unread_notifs()
        assert notification_type == "urgent notification", "urgent unread msgs not found"
        urgent_notifs_name = self.bell_icon.verify_unread_urgent_notifs_name()
        logging.info(f"Notification Name: {urgent_notifs_name}")

        notification_type = self.bell_icon.verify_informative_unread_notifs()
        assert notification_type == "informative notification", "informative unread msgs not found"
        informative_notifs_name = self.bell_icon.verify_unread_informative_notifs_name()
        logging.info(f"Notification Name: {informative_notifs_name}")

        notification_type = self.bell_icon.verify_warning_unread_notifs()
        assert notification_type == "warning notification", "warning unread msgs not found"
        warning_notifs_name = self.bell_icon.verify_unread_warning_notifs_name()
        logging.info(f"Notification Name: {warning_notifs_name}")

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_02_verify_transition_from_empty_bell_to_notification_bell_on_login_C60339089(self):
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon not visible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_notifications_panel_sign_in_btn(), "sign-in button in notification panel is not present"
        self.bell_icon.click_notifications_panel_close_btn()
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up(), "Device details page not loaded"
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        self.css.click_sign_in_button()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        notification_type = self.bell_icon.verify_urgent_unread_notifs()
        assert notification_type == "urgent notification", "urgent unread msgs not found"
        notification_type = self.bell_icon.verify_informative_unread_notifs()
        assert notification_type == "informative notification", "informative unread msgs not found"
        notification_type = self.bell_icon.verify_warning_unread_notifs()
        assert notification_type == "warning notification", "warning unread msgs not found"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_03_verify_login_using_sign_in_option_in_bell_flyout_C60372196(self):
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon not visible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_notifications_panel_sign_in_btn(), "sign-in button in notification panel is not present"
        self.bell_icon.click_notifications_panel_sign_in_btn()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        user_initials = self.profile.get_user_initials_after_signin()
        assert user_initials in ("RG", "RP"), "User not signed in/credentials not matching"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_04_verify_delete_option_for_urgent_unread_msg_is_disabled_C60336470(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon not visible"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_unread_text(), "unread messages category not found"
        assert self.bell_icon.verify_urgent_unread_notifs(), "urgent unread notifications is not present"
        self.bell_icon.click_urgent_unread_notification_ellipsis()
        assert self.bell_icon.verify_delete_disabled_urgent_unread_notifs(), "delete option is enabled"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_05_verify_delete_option_for_warning_unread_msg_is_enabled_C60336471(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon not visible"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_unread_text(), "unread messages category not found"
        notification_type = self.bell_icon.verify_warning_unread_notifs()
        assert notification_type == "warning notification", "warning unread msgs not found"
        warning_notifs_name = self.bell_icon.verify_unread_warning_notifs_name()
        logging.info(f"Notification Name: {warning_notifs_name}")
        self.bell_icon.click_warning_unread_notifs_ellipsis()
        self.bell_icon.click_delete_warning_unread_notifs()
        assert not self.bell_icon.verify_warning_unread_notifs(), "Warning notification still present"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_06_verify_delete_option_for_informative_unread_msg_is_enabled_C60336472(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_unread_text(), "unread messages category not found"
        assert self.bell_icon.verify_informative_unread_notifs(), "informative unread notifications is not present"
        self.bell_icon.click_informative_unread_notifs_ellipsis()
        self.bell_icon.click_delete_informative_unread_notifs()
        assert not self.bell_icon.verify_informative_unread_notifs(), "informative notification still present"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_07_verify_user_can_navigate_back_to_navigation_side_panel_C60370254(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_unread_text(), "unread messages category not found"
        assert self.bell_icon.verify_informative_unread_notifs(), "informative unread notifications is not present"
        informative_notifs_name = self.bell_icon.verify_unread_informative_notifs_name()
        logging.info(f"Notification Name: {informative_notifs_name}")
        self.bell_icon.click_informative_unread_notifs()
        detailed_notifs_back_btn_text = self.bell_icon.verify_detailed_notification_back_btn()
        assert detailed_notifs_back_btn_text == "Account", "Back button not present OR text incorrect on detailed notification page"
        self.bell_icon.click_detailed_notification_back_btn()
        assert self.bell_icon.verify_notification_side_panel(), "notifications side panel invisible"
