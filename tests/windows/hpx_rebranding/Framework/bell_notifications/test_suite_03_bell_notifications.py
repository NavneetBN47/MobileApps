import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_clear_sign_out")
class Test_Suite_03_Bell_Notifications(object):
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
        request.cls.fc.web_password_credential_delete()
        cls.user_name = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]["username"]
        cls.password = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]["password"]

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_01_verify_the_color_of_the_urgent_messages_C60336080(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        notification_type = self.bell_icon.verify_urgent_unread_notifs()
        assert notification_type == "urgent notification", "urgent unread msgs not found"
        self.bell_icon.click_urgent_unread_notifs()
        assert self.bell_icon.verify_urgent_msg_icon(), "urgent msg icon invisible"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_02_verify_the_color_of_the_warning_messages_C60336081(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_warning_unread_notifs(), "warning unread msgs not found"
        self.bell_icon.click_warning_unread_notifs()
        assert self.bell_icon.verify_warning_msg_icon(), "warning msg icon invisible"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_03_verify_the_color_of_the_informative_messages_C60336082(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_informative_unread_notifs(), "informative unread msgs not found"
        self.bell_icon.click_informative_unread_notifs()
        assert self.bell_icon.verify_info_msg_icon(), "informative msg icon invisible"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_04_notifications_panel_opens_on_bell_click_C67874087(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.device_card.verify_pc_devices_back_button(), "device back button not found"
        assert self.profile.verify_devicepage_avatar_btn(), "avatar button is not found"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon is not found"
        assert self.device_card.verify_homepage_plus_button(), "homepage plus button is not found"
        assert self.profile.verify_navbar_sign_in_button(), "sign-in button is not found"
        self.device_card.click_bell_icon()
        self.bell_icon.verify_notifications_sidebar_ui()

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_05_no_notifications_when_logged_out_C60336139(self):
        assert self.css.verify_sign_in_button_show_up(), "sign-in button invisible"
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon invisible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_sign_in_to_view_msgs(), "sign in or create an account to view all of your messages is invisible"
        notifs_title_name = self.bell_icon.verify_notifications_sidebar_ui()
        assert notifs_title_name == "Notifications", "notifications title name mismatch"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_06_only_account_messages_displayed_C58684361(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.device_card.verify_bell_icon_present(), "bell icon invisible"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        account_title = self.bell_icon.verify_account_category()
        assert account_title == "Account", "account title name mismatch"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_07_sort_order_of_messages_C58684367(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_unread_text(), "unread messages category not found"
        assert self.bell_icon.verify_read_text(), "read messages category not found"
