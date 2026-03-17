from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Pen_Control_Unsupport(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
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
            time.sleep(2)
            cls.fc.launch_myHP()
        time.sleep(5)
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_unsupported_systems_C38426160(self):
        self.fc.reset_myhp_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        #verify pen control not show in navigation bar in commercial
        assert bool(self.fc.fd["pen_control"].verify_pen_control_not_show_in_navigation_bar_commercial()) is False, "Pen control should not show navgation bar"
        time.sleep(1)


    @pytest.mark.ota
    def test_02_unsupported_systems_C38430295(self):
        #restart app
        self.fc.restart_myHP()
        #maximize window
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        #verify pen control is not visible in navigation bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        assert bool(self.fc.fd["pen_control"].verify_pen_control_not_show_in_navigation_bar_commercial()) is False, "Pen control should not show navigation bar"