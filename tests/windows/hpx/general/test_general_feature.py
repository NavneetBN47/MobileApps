import logging
import re
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.libs.ma_misc.conftest_misc as c_misc
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_App_Feature(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver= windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        time.sleep(2)
        cls.fc.launch_myHP()
        time.sleep(5)
        cls.fc.close_myHP()
    
    def test_01_verify_app_features_C33352539(self):
       self.fc.close_myHP()
       self.fc.myhp_app_setting_page()
       time.sleep(2)
       self.sf.maximize_settings_app()
       #verify app name as "myHP"
       assert self.sf.get_app_name_in_app_setting()=="myHP", "my HP app name does not show on top"
       logging.info("app name as myHP")
       assert self.sf.verify_app_version_in_app_setting() is True, "version doesnot show"
       logging.info("version of myHP app = "+str(self.sf.get_app_version_in_app_setting()))
       assert self.sf.verify_app_size() is True, "app size doesnot show"
       logging.info("app size= "+str(self.sf.get_app_size_in_app_setting()))
       self.fc.swipe_window(direction="down", distance=6)
       logging.info("installed date=")
       logging.info("modify and uninstalled button")
       self.fc.swipe_window(direction="down", distance=6)
       assert self.sf.verify_reset_button() is True, "reset button doesnot show"
       logging.info("Reset button on app setting is available")
       assert self.sf.verify_uninstall_btn_on_app_setting() is True, "uninstall button doesnot show"
       logging.info("uninstalled button is available")
       self.fc.close_windows_settings_panel()
    
    #this is running on willie successfully
    def test_02_verify_app_install_and_build_C33352543(self):
        self.version=self.driver.ssh.send_command('get-appxpackage *myHP* | select Version',  raise_e=False, timeout=10)
        result = re.search("([0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5})", str(self.version))
        logging.info("version="+str(result.group(0)))
        #logging.info("version="+str(result.match))
        install_build_version=result.group(0)

        logging.info("build="+str(install_build_version))
        self.fc.open_app_launch_window(install_build_version)
        time.sleep(4)
        #check app name
        assert bool(self.sf.get_app_name_on_installer_window() == "myHP is already installed") is True
        #version
        self.full_version=self.sf.get_app_version()
        self.version=self.full_version.replace("Version: ","")
        assert bool(self.version == install_build_version) is True
        #capabilities
        self.sf.click_more_btn()
        time.sleep(10)
        assert bool(self.sf.verify_app_capabilities()) is True
        logging.info("capabilities available")
        self.sf.click_launch_btn()
        time.sleep(5)
        if self.fc.fd["hp_privacy_setting"].verify_accept_all_btn_privacy():
            self.fc.fd["hp_privacy_setting"].click_accept_all_btn_privacy()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        logging.info("app launch successfully")
        self.fc.close_myHP()
        self.fc.close_app_launch_window()

    def test_03_version_on_app_ui_C33352554(self):
        self.fc.launch_myHP()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_about_tab()
        app_version = self.fc.fd["settings"].get_version_about().strip()
        ssh_version = self.fc.fd["home"].verify_myhp_app_version().strip()
        app_version = app_version.replace("Version","").strip()
        logging.info(f"App Version: '{app_version}'")
        logging.info(f"SSH Version: '{ssh_version}'")
        assert app_version == ssh_version, f"App version mismatch: App version ({app_version}) != SSH version ({ssh_version})"
        self.fc.close_myHP()

    @pytest.mark.commercial
    @pytest.mark.function
    def test_04_myHP_app_ui_C33352555(self):
        self.fc.launch_myHP()
        time.sleep(4)
        hardwareId= str(self.fc.get_hp_hardware_id()).lower()
        logging.info(f"Hardware ID: '{hardwareId}'")
        time.sleep(1)
        # The below asserts are common for all the devices and hence is outside of if/else
        assert self.fc.fd["navigation_panel"].verify_home_menu_navigation(), "Home menu is not displayed"
        assert self.fc.fd["navigation_panel"].verify_pc_device_show(), "PC device not displayed"
        assert self.fc.fd["navigation_panel"].verify_support_menu_navigation(), "Support Menu not displayed"
        assert self.fc.fd["navigation_panel"].verify_settings_menu_navigation(), "Settings menu not displayed"
        assert self.fc.fd["navigation_panel"].verify_hamburger_menu_navigation(), "Hamburger menu is not displayed"
        time.sleep(3)
        # If hanburger is not expanded we are expanding the hamburger menu. Else we are collapsing and expanding the hamburger
        if not self.fc.fd["navigation_panel"].verify_pc_device_show():
            self.fc.fd["navigation_panel"].click_hamburger_navigation()
            assert self.fc.fd["navigation_panel"].verify_pc_device_show(), "Hamburger menu is not expanded"
        else:
            self.fc.fd["navigation_panel"].click_hamburger_navigation()
            time.sleep(1)
            self.fc.fd["navigation_panel"].click_hamburger_navigation()
            assert self.fc.fd["navigation_panel"].verify_pc_device_show(), "Hamburger menu is not expanded"
        # If device is commercial it asserts for hppk and no audio card . Else if device is consumer asserts for Audio and no hppk
        if "hpic000c".lower() in hardwareId:
            assert bool(self.fc.fd["home"].verify_Programmable_Key_card_visible()) is True, "HP Programmable Key card is not displayed"
            assert not self.fc.fd["navigation_panel"].verify_home_audio_card_show(), "Audio card is available in commercial device"
        elif "hpic0003".lower() in hardwareId:
            assert self.fc.fd["navigation_panel"].verify_home_audio_card_show(), "Audio card not available"
            assert not bool(self.fc.fd["home"].verify_Programmable_Key_card_visible()) is True, "HP Programmable Key card is displayed on a consumer device"
        # Closing hamburger menu at the last
        self.fc.fd["navigation_panel"].click_hamburger_navigation()
        assert not self.fc.fd["navigation_panel"].verify_pc_device_show(), "Hamburger menu is not collapsed"
        self.fc.close_myHP()
