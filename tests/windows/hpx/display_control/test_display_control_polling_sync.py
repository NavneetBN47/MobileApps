from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Display_Control_HDR_Portrait(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
            time.sleep(3)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)

    #This suite should run in any display module with HDR.
    @pytest.mark.ota
    def test_01_hdr_toggle_on_windows_settings_C41042200(self):

        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        self.fc.fd["display_control"].click_windows_display_settings()

        if self.sf.get_windows_hdr_button_status() == "0":
            self.sf.click_windows_hdr_button()
        else:
            self.sf.click_windows_hdr_button()
            time.sleep(5)
            self.sf.click_windows_hdr_button()

        time.sleep(5)
        self.fc.close_windows_settings_panel()

        time.sleep(2)
        assert self.fc.fd["display_control"].verify_app_out_of_sync_show() is True, "App out of sync is not shown"
        time.sleep(5)
        self.fc.fd["display_control"].click_see_more_link()
        time.sleep(3)
        assert self.fc.fd["display_control"].verify_not_synchronized_title() is True, "Not synchronized title is not shown"
        assert self.fc.fd["display_control"].verify_discard_changes_button_show() is True, "Discard changes button is not shown"
        assert self.fc.fd["display_control"].verify_keep_new_changes_button_show() is True, "Keep new changes button is not shown"
    

    @pytest.mark.ota
    def test_02_hdr_toggle_off_windows_settings_C41042201(self):

        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()

        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=4)
        self.fc.fd["display_control"].click_windows_display_settings()

        if self.sf.get_windows_hdr_button_status() == "0":
            self.sf.click_windows_hdr_button()
            time.sleep(5)
            self.sf.click_windows_hdr_button()
        else:
            self.sf.click_windows_hdr_button()

        time.sleep(5)
        self.fc.close_windows_settings_panel()

        time.sleep(2)
        assert self.fc.fd["display_control"].verify_app_out_of_sync_show() is True, "App out of sync is not shown"
        time.sleep(5)
        self.fc.fd["display_control"].click_see_more_link()
        time.sleep(3)
        assert self.fc.fd["display_control"].verify_not_synchronized_title() is True, "Not synchronized title is not shown"
        assert self.fc.fd["display_control"].verify_discard_changes_button_show() is True, "Discard changes button is not shown"
        assert self.fc.fd["display_control"].verify_keep_new_changes_button_show() is True, "Keep new changes button is not shown"
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(5)
