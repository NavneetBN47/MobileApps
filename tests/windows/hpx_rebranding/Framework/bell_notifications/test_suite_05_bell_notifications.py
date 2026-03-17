import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_05_Bell_Notifications(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.bell_icon = request.cls.fc.fd["bell_icon"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_01_verify_notification_tile_ellipsis_clickable_C60339095(self):
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        if not logged_in:
            self.css.click_sign_in_button()
            self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.profile.verify_top_profile_icon_signed_in(), "Profile icon isn't showing initials after sign-in"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_notifications_title(), "notification title invisible"
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_notification_tile_ellipsis(), "notification tile ellipsis invisible"
        self.bell_icon.click_notification_tile_ellipsis()
        assert self.bell_icon.verify_notification_dropdown_revealed(), "notification drop down invisible"
        assert self.bell_icon.verify_dropdown_mark_as_read_option_present(), "mark as read option not visible in dropdown"
        assert self.bell_icon.verify_dropdown_delete_option_present(), "delete option not found in dropdown"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_02_verify_mark_as_read_option_enabled_for_all_notification_types_C60339094(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        self.profile.verify_top_profile_icon_signed_in()
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_notifications_title(), "notification title invisible"
        self.bell_icon.click_notification_account()

        urgent_unread_notifs_name = self.bell_icon.verify_unread_urgent_notifs_name()
        logging.info(f"Notification Name: {urgent_unread_notifs_name}")
        assert self.bell_icon.verify_urgent_unread_notification_ellipsis(), "urgent unread notification ellipsis invisible"
        self.bell_icon.click_urgent_unread_notification_ellipsis()
        self.bell_icon.verify_notifs_and_mark_as_read()
        self.bell_icon.swipe_till_read_notifs()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        assert self.bell_icon.verify_urgent_notifications(), "urgent notifications not found"
        read_urgent_notifs_name = self.bell_icon.get_urgent_notifications_name()
        logging.info(f"read urgent notifs name: {read_urgent_notifs_name}")
        assert urgent_unread_notifs_name == read_urgent_notifs_name, "urgent msg did not get marked as read after opening the notification"
        self.bell_icon.swipe_to_top_notifs_section()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()

        unread_informative_notifs_name = self.bell_icon.verify_unread_informative_notifs_name()
        logging.info(f"informative unread notifs name: {unread_informative_notifs_name}")
        assert self.bell_icon.verify_informative_unread_notification_ellipsis(), "informative unread notification ellipsis invisible"
        self.bell_icon.click_informative_unread_notification_ellipsis()
        self.bell_icon.verify_notifs_and_mark_as_read()
        self.bell_icon.swipe_till_read_notifs()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        assert self.bell_icon.verify_informative_notifications(), "informative notifications not found"
        read_informative_notifs_name = self.bell_icon.get_informative_notifications_name()
        logging.info(f"read informative notifs name: {read_informative_notifs_name}")
        assert unread_informative_notifs_name == read_informative_notifs_name, "informative msg did not get marked as read after opening the notification"
        self.bell_icon.swipe_to_top_notifs_section()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()

        unread_warning_notifs_name = self.bell_icon.verify_unread_warning_notifs_name()
        logging.info(f"warning unread notifs name: {unread_warning_notifs_name}")
        assert self.bell_icon.verify_warning_unread_notification_ellipsis(), "warning unread notification ellipsis not found"
        self.bell_icon.click_warning_unread_notification_ellipsis()
        self.bell_icon.verify_notifs_and_mark_as_read()
        self.bell_icon.swipe_till_read_notifs()
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        assert self.bell_icon.verify_warning_notifications(), "warning notifications not found"
        read_warning_notifs_name = self.bell_icon.get_warning_notifications_name()
        logging.info(f"read warning notifs name: {read_warning_notifs_name}")
        assert unread_warning_notifs_name == read_warning_notifs_name, "warning msg did not get marked as read after opening the notification"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_03_verify_unread_read_notifications_C53303701(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.profile.verify_top_profile_icon_signed_in(), "Profile icon isn't showing initials after sign-in"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_notifications_title(), "notification title invisible"
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_unread_text(), "unread notifications category invisible"

        notification_type = self.bell_icon.verify_informative_unread_notifs()
        assert notification_type == "informative notification", "informative unread msgs not found"

        notification_type = self.bell_icon.verify_warning_unread_notifs()
        assert notification_type == "warning notification", "warning unread msgs not found"

        notification_type = self.bell_icon.verify_urgent_unread_notifs()
        assert notification_type == "urgent notification", "urgent unread msgs not found"

        self.driver.swipe("read_text")
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        assert self.bell_icon.verify_read_text(), "read notifications category invisible"
        assert self.bell_icon.verify_informative_notifications(), "informative read notifications invisible"
        assert self.bell_icon.verify_warning_notifications(), "warning read notifications invisible"
        assert self.bell_icon.verify_urgent_notifications(), "urgent read notifications invisible"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_04_verify_elements_in_notifs_title_C60339091(self):
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        if not logged_in:
            self.css.click_sign_in_button()
            self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        assert self.profile.verify_top_profile_icon_signed_in(), "Profile icon isn't showing initials after sign-in"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_notifications_title(), "notification title invisible"
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_unread_text(), "unread notifications category invisible"

        self.driver.swipe("read_text")
        self.hpx_settings.minimize_and_click_hp_from_taskbar()
        assert self.bell_icon.verify_notification_tile_ellipsis(), "notification ellipsis not found"

        assert self.bell_icon.verify_urgent_notifications(), "urgent notifications not found"
        read_urgent_notifs_name = self.bell_icon.get_urgent_notifications_name()
        logging.info(f"read urgent notifs name: {read_urgent_notifs_name}")
        self.bell_icon.click_urgent_read_notifs()
        detailed_read_notifs_name = self.bell_icon.get_detailed_notification_title()
        logging.info(f"detailed read notifs name: {detailed_read_notifs_name}")
        assert read_urgent_notifs_name == detailed_read_notifs_name, "urgent notif name mismatch between list view and detailed view"

        assert self.bell_icon.verify_urgent_msg_icon(), "urgent msg icon invisible"
        description = self.bell_icon.get_notif_description()
        logging.info(f"Message detailed view: {description}")
        assert self.bell_icon.verify_time_stamp(), "message time stamp not present"
        timestamp = self.bell_icon.get_time_stamp()
        logging.info(f"Timestamp: {timestamp}")
        assert 'ago' in timestamp.lower(), f"Timestamp should contain 'ago', got: '{timestamp}'"
        assert any(char.isdigit() for char in timestamp), f"Timestamp should contain a number. Got: '{timestamp}'"

        detailed_notif_back_btn_text = self.bell_icon.verify_detailed_notification_back_btn()
        assert detailed_notif_back_btn_text == "Account", "detailed notification back btn text mismatch"

        self.bell_icon.click_detailed_notification_back_btn()
        self.bell_icon.click_notifications_back_btn()
        self.bell_icon.click_notifications_panel_close_btn()
        assert self.profile.verify_top_profile_icon_signed_in(), "Profile icon isn't showing initials after sign-in"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.device_card.verify_pc_devices_back_button(), "device back button not found"
        assert self.device_card.verify_homepage_plus_button(), "homepage plus button is not found"
