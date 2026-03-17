from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_robotics(object):
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
            cls.fc.launch_myHP()        
        yield
        cls.fc.insert_usb()
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(3)


    #only willie1 (robotics action required)
    def test_01_connected_device_will_show_up_and_selected_on_combo_box_automatically_C32316687(self):
        self.fc.remove_usb()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert bool(self.fc.fd["audio"].verify_headset_device()) is False, "input headset is visible"
        assert bool(self.fc.fd["audio"].verify_headset_tab_starts()) is False, "output headset is visible"
        self.fc.insert_usb()
        assert bool(self.fc.fd["audio"].verify_headset_device()) is True, "input headset is not visible"
        assert bool(self.fc.fd["audio"].verify_headset_tab_starts()) is True, "input headset is not visible"
        self.fc.remove_usb()

    def test_02_mute_unmute_from_keyboard_verify_the_status_of_mute_button_C31807199(self):
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        output_mute = self.fc.fd["audio"].get_output_mute_button_name()
        if "Off" in output_mute:
            self.fc.press_mute_button()
        assert "On" in self.fc.fd["audio"].get_output_mute_button_name(),"Speaker is not mute"
        output_mute = self.fc.fd["audio"].get_output_mute_button_name()
        if "On" in output_mute:
            self.fc.press_mute_button()
        assert "Off" in self.fc.fd["audio"].get_output_mute_button_name(),"Speaker is not mute"