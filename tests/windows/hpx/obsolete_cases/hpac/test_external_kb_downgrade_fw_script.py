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
    
    @pytest.mark.require_platform(["grogu"])
    def test_01_downgrade_the_firmware_C36836414(self):
        self.fc.launch_myHP()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_external_keyboard_module()
        if self.fc.fd["external_keyboard"].verify_update_now_button_in_the_app():
            self.fc.fd["external_keyboard"].click_update_now_button_in_the_app()
            time.sleep(420)            
        self.fc.kill_myhp_process()
        time.sleep(2)
        self.fc.kill_myhp_desktopextesion_process()
        time.sleep(2)
        p_count = self.fc.get_cmd_console_process()
        self.sf.click_start_btn()
        self.sf.click_search_box()
        time.sleep(3)
        self.sf.enter_search_box("kb_downgrade.bat")
        time.sleep(3)
        self.fc.fd["external_keyboard"].click_runas_admin()
        time.sleep(420)
        if self.fc.get_cmd_console_process() > p_count:
            self.fc.kill_cmd_console_process()
            time.sleep(10)
            self.fc.fd["external_keyboard"].click_ok_to_close_console_popup()
        time.sleep(15)    
        self.fc.launch_myHP()    
        self.fc.kill_myhp_process()
        time.sleep(1500)
        self.fc.launch_myHP()
        time.sleep(5)
        self.fc.close_myHP()