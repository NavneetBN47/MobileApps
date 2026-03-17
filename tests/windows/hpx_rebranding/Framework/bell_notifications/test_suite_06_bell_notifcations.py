import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_clear_sign_out")
class Test_Suite_06_Bell_Notifications(object):
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
        request.cls.fc.web_password_credential_delete()
        cls.user_name = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]["username"]
        cls.password = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]["password"]


    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_01_open_detailed_view_from_message_C58684404(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        self.driver.swipe("read_text", direction="down")
        assert self.bell_icon.verify_urgent_notifications(), "urgent notifications not found"
        self.bell_icon.click_urgent_read_notifs()
        description = self.bell_icon.get_notif_description()
        logging.info(f"Message detailed view: {description}")

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_02_mark_message_as_read_by_opening_C58684406(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_unread_text(), "unread messages category not found"
        self.bell_icon.verify_informative_unread_notifs(), "info unread msgs not found"
        unread_informative_notifs_name = self.bell_icon.verify_unread_informative_notifs_name()
        logging.info(f"informative unread notifs name: {unread_informative_notifs_name}")
        self.bell_icon.click_informative_unread_notifs()
        description = self.bell_icon.get_notif_description()
        logging.info(f"msg description: {description}")
        self.bell_icon.click_detailed_notification_back_btn()
        assert self.bell_icon.verify_informative_notifications(), "informative notifications not found"
        read_informative_notifs_name = self.bell_icon.get_informative_notifications_name()
        logging.info(f"read informative notifs name: {read_informative_notifs_name}")
        assert unread_informative_notifs_name == read_informative_notifs_name, "informative msg did not get marked as read after opening the notification"

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_03_verify_unread_notifs_description_C60336160(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_unread_text(), "unread messages category not found"

        informative_notifs_name = self.bell_icon.verify_unread_informative_notifs_name()
        logging.info(f"Notification Name: {informative_notifs_name}")
        assert self.bell_icon.verify_informative_unread_notifs(), "informative unread notifications is not present"
        self.bell_icon.click_informative_unread_notifs()
        description = self.bell_icon.get_notif_description()
        logging.info(f"Informative unread notification description: {description}")
        self.bell_icon.click_detailed_notification_back_btn()

        urgent_notifs_name = self.bell_icon.verify_unread_urgent_notifs_name()
        logging.info(f"Notification Name: {urgent_notifs_name}")
        assert self.bell_icon.verify_urgent_unread_notifs(), "urgent unread msgs not found"
        self.bell_icon.click_urgent_unread_notifs()
        description = self.bell_icon.get_notif_description()
        logging.info(f"Urgent unread notification description: {description}")
        self.bell_icon.click_detailed_notification_back_btn()

        assert self.bell_icon.verify_warning_unread_notifs(), "warning unread notifications is not present"
        warning_notifs_name = self.bell_icon.verify_unread_warning_notifs_name()
        logging.info(f"Notification Name: {warning_notifs_name}")
        assert self.bell_icon.verify_warning_unread_notifs(), "warning unread msgs not found"
        self.bell_icon.click_warning_unread_notifs()
        description = self.bell_icon.get_notif_description()
        logging.info(f"Warning unread notification description: {description}")

    @pytest.mark.regression
    @pytest.mark.skip_in_prod
    @pytest.mark.skip_in_stg
    def test_04_verify_read_notifs_description_C60336161(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        self.devicesMFE.verify_bell_icon_show_up()
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        self.driver.swipe("read_text")
        self.hpx_settings.minimize_and_click_hp_from_taskbar()

        assert self.bell_icon.verify_informative_notifications(), "informative read msgs not found"
        self.bell_icon.click_informative_read_notifs()
        description = self.bell_icon.get_notif_description()
        logging.info(f"Informative read notification description: {description}")

        self.bell_icon.click_notifications_back_btn()
        assert self.bell_icon.verify_urgent_notifications(), "urgent read msgs not found"
        self.bell_icon.click_urgent_read_notifs()
        description = self.bell_icon.get_notif_description()
        logging.info(f"Urgent read notification description: {description}")

        self.bell_icon.click_notifications_back_btn()
        assert self.bell_icon.verify_warning_notifications(), "warning read msgs not found"
        self.bell_icon.click_warning_read_notifs()
        description = self.bell_icon.get_notif_description()
        logging.info(f"Warning read notification description: {description}")
