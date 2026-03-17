import pytest
from time import sleep
from MobileApps.libs.flows.common.gotham.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "GOTHAM"
class Test_Suite_01_Uninstall_App(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_smart_setup, install_app):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.sf = SystemFlow(cls.driver)
        cls.install_app_path = install_app
        cls.sp = cls.sf.sp
        
        cls.check_path = "C:\\Users\\exec\\AppData\\Local\\Packages\\AD2F1837.HPPrinterControl_v10z8vjag6ke6"

    def test_01_uninstall_app(self):
        """
        Right click on app logo in Start menu.
        Select "Uninstall" to uninstall app.

        Verify app is uninstalled and cannot be launched anymore.
        Verify app folder is no longer seen under localstate.

        https://hp-testrail.external.hp.com/index.php?/cases/view/16929240
        """    
        for _ in range(2):
            self.sp.unextend_win_start_list()
        self.sp.extend_win_start_list()
        self.sp.verify_win_start_display()
        self.sp.click_win_app_head_letter()
        self.sp.click_win_h_app_letter()
        self.sp.right_click_win_hp_app_item()
        self.sp.verify_win_hp_right_opt_display()
        self.sp.click_win_app_uninstall_btn()
        if self.sp.verify_win_app_uninstall_info_dialog():
            self.sp.click_win_app_uninstall_info_btn()
        sleep(10)
        assert self.sp.check_hp_app_exist(self.check_path) is False

    def test_02_launch_app(self):
        for _ in range(2):
            self.sp.unextend_win_start_list()
        self.driver.ssh.send_command(self.install_app_path + "\\Install.ps1 -Force", timeout=180)
        self.sf.launch_app_on_win_start()
        self.fc.go_home()
        assert self.sp.check_hp_app_exist(self.check_path) is not False

    def test_03_settings_and_store_cleanup(self):
        self.sf.settings_and_store_cleanup()
        