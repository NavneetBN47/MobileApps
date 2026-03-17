from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_External_Keyboard(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        cls.fc.launch_myHP()
        cls.fc.close_myHP()

   
    #always run  test_external_kb_downgrade_fw_script.py suit first before running this test suite
    @pytest.mark.require_platform(["grogu"])
    def test_01_click_update_and_open_my_hp_button_in_toast_verify_it_can_successfully_C36836414(self):
        time.sleep(600) 
        self.fc.launch_myHP()
        time.sleep(10)
        self.fc.close_myHP()
        time.sleep(.3)
        self.fc.launch_myHP()
        
        time.sleep(.2)
        assert "New firmware available for keyboard" in self.fc.fd["external_keyboard"].get_toast_notification_title()
        self.fc.close_myHP()
        time.sleep(3)
        self.fc.launch_myHP()
        
        assert "Open myHP" in self.fc.fd["external_keyboard"].verify_open_myhp_firmware_button()
        time.sleep(3)
        self.fc.close_myHP()
        self.fc.launch_myHP()
        assert "Update" in self.fc.fd["external_keyboard"].verify_update_firmware_button()
        time.sleep(3)
        self.fc.close_myHP()
        self.fc.launch_myHP()

        time.sleep(.2)
        self.fc.fd["external_keyboard"].click_open_myhp_firmware_button()
        assert "Keyboard"== self.fc.fd["external_keyboard"].get_title_tooltips_text()
        self.fc.kill_myhp_process()
        self.fc.kill_myhp_desktopextesion_process()

    @pytest.mark.require_platform(["grogu"])
    def test_02_click_dismiss_and_open_my_hp_button_in_toast_verify_it_can_successfully_C36836414(self):
        time.sleep(.2)
        self.fc.launch_myHP()
        time.sleep(.2)
        assert "Open myHP" in self.fc.fd["external_keyboard"].verify_open_myhp_firmware_button()
        self.fc.close_myHP()
        time.sleep(.2)
        self.fc.launch_myHP()
        time.sleep(.3)
        self.fc.fd["external_keyboard"].click_open_myhp_firmware_button()
        assert "Keyboard"==self.fc.fd["external_keyboard"].get_title_tooltips_text()
        assert "Update now"==self.fc.fd["external_keyboard"].get_update_now_button_in_the_app()
        self.fc.fd["external_keyboard"].click_update_now_button_in_the_app()
        timeout = time.time() + 60*7
        while True:
            if self.fc.fd["external_keyboard"].verify_open_myhp_firmware_button_present() or time.time() > timeout:
                dismiss_button = self.fc.fd["external_keyboard"].get_dismiss_button_on_toast_notification()
                assert "Dismiss" in dismiss_button, "Dismiss is not in the toast notification new_fw_notification - {}".format(dismiss_button)
                self.fc.fd["external_keyboard"].click_dismiss_button_on_toast_notification()
                break
            time.sleep(1)
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()
        time.sleep(10)
        self.fc.fd["external_keyboard"].click_info_icon()
        time.sleep(2)
        firmware_version = self.fc.fd["external_keyboard"].get_firmware_version_text_show()
        assert firmware_version=="1.04.0","1.04.0 is not updated to latest version - {}".format(firmware_version)
        self.fc.close_myHP()
