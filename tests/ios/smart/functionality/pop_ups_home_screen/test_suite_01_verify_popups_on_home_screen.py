import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.web import const as w_const

pytest.app_info = "SMART"

class Test_Suite_01_Verify_Popups_On_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.photos = cls.fc.fd["photos"]
        cls.home = cls.fc.fd["home"]
        cls.camera = cls.fc.fd["camera"]
        cls.printers = cls.fc.fd["printers"]
        cls.welcome = cls.fc.fd["welcome"]
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.ios_system = cls.fc.fd["ios_system"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_allow_notifications_pop_up(self):
        """
        C28217233 - Allow notifications pop up
        C28217231 - Device connection permission pop up - iOS 14 onwards
        C28217232 - Smart Task awareness pop up on Home screen
        """
        self.fc.go_home(stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(i_const.HOME_TILES.TILE_CAMERA_SCAN)
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        if self.camera.verify_second_close_btn():
            self.camera.select_second_close_btn()
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.select_print_button_and_verify_print_job(self.p)
        self.common_preview.select_navigate_back()
        self.common_preview.select_navigate_back()
        self.photos.select_navigate_back()
        self.photos.select_navigate_back()
        self.home.select_home_icon()
        assert self.home.verify_smart_task_awareness_popup(raise_e=False), "smart task awareness popup failed to appear"

    def test_02_verify_bluetooth_popup(self):
        """
        C28279579 - Bluetooth Pop Up on Add Printer screen
        C28281910 - Location Permission Pop Up
        """
        self.go_home_local(reset=True, stack=self.stack)
        self.home.select_get_started_by_adding_a_printer()
        if self.home.verify_bluetooth_popup(raise_e=False):
            self.home.handle_bluetooth_popup()
        self.printers.add_printer_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.handle_location_popup(raise_e=False)
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()

    def go_home_local(self, stack="pie", reset=False, username="", password=""):
        stack = stack.lower()
        self.ios_system.clear_safari_cache()
        if reset:
            self.driver.reset(i_const.BUNDLE_ID.SMART)
        if stack != "pie":  # pie stack is default server on iOS HP Smart
            self.fc.change_stack(stack)
        self.driver.launch_app(i_const.BUNDLE_ID.SMART)
        # TEMP work around for def-#AIOI-11315
        self.welcome.allow_notifications_popup(raise_e=False)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.SMART_WELCOME(self.driver.driver_type), timeout=30)
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.click_accept_all_btn()
        if self.welcome_web.verify_permission_for_advertising_screen():
            self.welcome_web.click_continue_btn()
        self.ios_system.handle_allow_tracking_popup(raise_e=False)
        self.driver.wait_for_context(w_const.WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.ows_value_prop.verify_ows_value_prop_screen(timeout=60)
        self.fc.login_value_prop_screen(tile=False, username=username, password=password)
        self.welcome.allow_notifications_popup(timeout=15, raise_e=True)
        self.ios_system.dismiss_hp_local_network_alert(timeout=10)
        self.home.close_smart_task_awareness_popup()
        self.home.dismiss_tap_account_coachmark()
        self.fc.remove_default_paired_printer()