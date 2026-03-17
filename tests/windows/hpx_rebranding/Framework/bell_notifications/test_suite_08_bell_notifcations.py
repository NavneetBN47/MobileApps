import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_clear_sign_out")
class Test_Suite_08_Bell_Notifications(object):
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
    def test_01_verify_bell_notifications_device_details_screen_blur_displayed_C60336359(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon is not present"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_background_blur(), "background blur is not displayed on device details screen"

    @pytest.mark.regression
    def test_02_verify_support_on_urgent_info_warning_unread_notifications_C60369962(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon is not present"
        self.device_card.click_bell_icon()
        self.bell_icon.verify_account_category()
        self.bell_icon.verify_shortcuts_category()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_urgent_unread_notifs(), "urgent unread msgs not found"
        assert self.bell_icon.verify_informative_unread_notifs(), "informative unread msgs not found"
        assert self.bell_icon.verify_warning_unread_notifs(), "warning unread msgs not found"

    @pytest.mark.regression
    def test_03_verify_support_on_urgent_unread_notifications_C60370064(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon is not present"
        self.device_card.click_bell_icon()
        self.bell_icon.verify_account_category()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_urgent_unread_notification_ellipsis(), "urgent unread notification ellipsis not found"
        self.bell_icon.click_urgent_unread_notification_ellipsis()
        assert self.bell_icon.verify_delete_disabled_urgent_unread_notifs(),"delete disabled urgent unread notifs not found"
        self.bell_icon.verify_notifs_and_mark_as_read()

    @pytest.mark.regression
    def test_04_verify_support_on_important_unread_notifications_C60370065(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon is not present"
        self.device_card.click_bell_icon()
        self.bell_icon.verify_account_category()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_informative_unread_notification_ellipsis(), "informative unread notification ellipsis not found"
        self.bell_icon.click_informative_unread_notification_ellipsis()
        assert self.bell_icon.verify_notification_dropdown_revealed(), "notification drop down invisible"
        assert self.bell_icon.verify_dropdown_mark_as_read_option_present(), "mark as read option not visible in dropdown"
        assert self.bell_icon.verify_dropdown_delete_option_present(), "delete option not visible in dropdown"
        
    @pytest.mark.regression
    def test_05_verify_bell_good_to_know_notifications_C60370067(self):
        self.fc.sign_in(self.user_name, self.password, self.web_driver)
        assert self.devicesMFE.verify_bell_icon_show_up(), "bell icon is not present"
        self.device_card.click_bell_icon()
        self.bell_icon.verify_account_category()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_warning_unread_notification_ellipsis(), "warning unread notification ellipsis not found"
        self.bell_icon.click_warning_unread_notification_ellipsis()
        assert self.bell_icon.verify_notification_dropdown_revealed(), "notification drop down invisible"
        assert self.bell_icon.verify_dropdown_mark_as_read_option_present(), "mark as read option not visible in dropdown"
        assert self.bell_icon.verify_dropdown_delete_option_present(), "delete option not visible in dropdown"
