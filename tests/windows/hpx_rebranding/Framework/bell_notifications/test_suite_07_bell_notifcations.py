import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_clear_sign_out")
class Test_Suite_07_Bell_Notifications(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.profile= request.cls.fc.fd["profile"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.bell_icon = request.cls.fc.fd["bell_icon"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()
        hpid_credentials = saf_misc.load_json(ma_misc.get_abs_path(HPX_ACCOUNT.account_details_path))["hpid"]
        cls.user_name, cls.password = hpid_credentials["username"], hpid_credentials["password"]
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    def test_01_verify_close_button_functionality_in_bell_notification_flyout_C60339090(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        assert self.devicesMFE.verify_bell_icon_show_up(), "Bell icon not visible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_account_category(), "Account category not visible in bell notification flyout"
        self.bell_icon.verify_shortcuts_category()
        assert self.bell_icon.verify_notifications_panel_close_btn(), "Close button not visible in bell notification flyout"
        self.bell_icon.click_notifications_panel_close_btn()
 
    @pytest.mark.regression
    def test_02_verify_users_can_view_unread_messages_C60339083(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        assert self.devicesMFE.verify_bell_icon_show_up(), "Bell icon not visible"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_informative_unread_notifs(), "informative unread notifications is not present"
        self.bell_icon.click_informative_read_notifs()
        description = self.bell_icon.get_notif_description()
        logging.info(f"Message detailed view: {description}")

    @pytest.mark.regression
    def test_03_verify_users_can_view_messages_under_read_section_C60339084(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.devicesMFE.click_home_loggedin()
        self.fc.sign_in(self.user_name, self.password, self.web_driver, user_icon_click=False)
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        assert self.devicesMFE.verify_bell_icon_show_up(), "Bell icon not visible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_account_category(), "Account category not visible in bell notification flyout"
        self.bell_icon.verify_shortcuts_category()
        self.bell_icon.click_notification_account()
        self.driver.swipe("read_text", direction="down")
        assert self.bell_icon.verify_informative_notifications(), "Informative notifications not found"
        assert self.bell_icon.verify_informative_unread_notifs(), "informative unread notifications is not present"
        self.bell_icon.click_informative_read_notifs()
        description = self.bell_icon.get_notif_description()
        logging.info(f"Message detailed view: {description}")

    @pytest.mark.regression
    def test_04_verify_notifications_after_relaunching_app_C66254937(self):
        logged_in = self.profile.verify_top_profile_icon_signed_in()
        assert logged_in, "User not signed in/After signing in the 'Sign In' button failed to disappear after 20 seconds"
        assert self.devicesMFE.verify_bell_icon_show_up(), "Bell icon not visible"
        self.device_card.click_bell_icon()
        assert self.bell_icon.verify_account_category(), "Account category not visible in bell notification flyout"
        self.bell_icon.verify_shortcuts_category()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_informative_unread_notifs(), "informative unread notifications is not present"
        assert self.bell_icon.verify_informative_notifications(), "Informative read notifications not found"
        self.fc.restart_myHP()
        assert self.devicesMFE.verify_bell_icon_show_up(), "Bell icon not visible after relaunching app"
        self.device_card.click_bell_icon()
        self.bell_icon.click_notification_account()
        assert self.bell_icon.verify_informative_unread_notifs(), "informative unread notifications is not present after relaunching app"
        assert self.bell_icon.verify_informative_notifications(), "Informative read notifications not found after relaunching app"