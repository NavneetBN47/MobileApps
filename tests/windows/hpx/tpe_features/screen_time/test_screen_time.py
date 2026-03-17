from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Screen_Time(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
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
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_platform(["bopeep"])
    def test_01_screen_time_UI_C33706930(self):
        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_screen_time()

        assert self.fc.fd["screen_time"].verify_screen_time_title_show() == "Screen Time"
        assert self.fc.fd["screen_time"].verify_screen_time_subtitle_show() == "Manage and track the time you spend on your PC. This feature requires access to your camera."
        assert self.fc.fd["screen_time"].verify_active_screen_title_show() == "Activate Screen Time to Gather Data"
        time.sleep(2)
        self.fc.fd["screen_time"].click_screen_time_button()
        time.sleep(3)
        self.fc.fd["screen_time"].click_send_reminder_button()
        time.sleep(3)
        assert self.fc.fd["screen_time"].verify_send_reminder_title_show() == "Send a Reminder"
        assert self.fc.fd["screen_time"].verify_send_reminder_subtitle_show() == "Receive a reminder to take a break from looking at your screen."
        assert self.fc.fd["screen_time"].verify_reminder_interva_title_show() == "Reminder Interval"
    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_verify_screen_time_tooltips_C36328260(self):
        time.sleep(2)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_screen_time()

        time.sleep(2)
        self.fc.fd["screen_time"].click_screen_time_tootlips()
        assert self.fc.fd["screen_time"].verify_screen_time_tooltips_show() == "This feature only works when your built-in camera is facing you. This feature does not support external monitors. If Screen Time is turned off, daily data will not be collected."
        time.sleep(3)
        self.fc.fd["screen_time"].click_send_reminder_tootlips()
        assert self.fc.fd["screen_time"].verify_send_reminder_tooltips_show() == "Time intervals are measured by how much time is spent in front of the display."

    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.require_platform(["bopeep"])
    def test_03_check_screen_time_toggles_buttons_work_well_C42778666(self):
        time.sleep(2)
        self.fc.restart_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_screen_time()

        if self.fc.fd["screen_time"].is_screen_time_toggle_selected() == "1":
            time.sleep(3)
            assert self.fc.fd["screen_time"].is_screen_time_toggle_selected() == "1", "Screen time toggle button is not selected"
        else:
            self.fc.fd["screen_time"].click_screen_time_button()
            time.sleep(3)
            assert self.fc.fd["screen_time"].is_screen_time_toggle_selected() == "1", "Screen time toggle button is selected"
        
        if self.fc.fd["screen_time"].is_send_reminder_toggle_selected() == "1":
            time.sleep(3)
            assert self.fc.fd["screen_time"].is_send_reminder_toggle_selected() == "1", "Screen time toggle button is not selected"
        else:
            self.fc.fd["screen_time"].click_send_reminder_button()
            time.sleep(3)
            assert self.fc.fd["screen_time"].is_send_reminder_toggle_selected() == "1", "Screen time toggle button is selected"
        time.sleep(3)
        self.fc.fd["screen_time"].click_reminder_interval_combobox()
        time.sleep(3)

        all_time = self.fc.fd["screen_time"].get_all_time_from_time_list()
        time_list = ["every hour", "4 hours", "8 hours", "12 hours"]
        for all_time in time_list:
            assert all_time in time_list

        self.fc.fd["screen_time"].open_dropdown_list()
        self.fc.fd["screen_time"].click_4_hours()
        assert self.fc.fd["screen_time"].verify_4_hours_selected() == "4 hours"
        time.sleep(2)
        counter = 0
        while self.fc.fd["screen_time"].is_screen_time_toggle_selected() == "1" and counter < 5:
            self.fc.fd["screen_time"].click_screen_time_button()
            counter += 1
            time.sleep(2)
        time.sleep(4)
        assert self.fc.fd["screen_time"].is_screen_time_toggle_selected() == "0", "Screen time toggle button is selected"
        assert self.fc.fd["screen_time"].is_send_reminder_toggle_selected() == "0", "Send reminder toggle button is selected"