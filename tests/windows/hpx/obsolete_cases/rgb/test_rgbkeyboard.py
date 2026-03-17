import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
from SAF.misc import saf_misc
import pytest
import os,sys
import shutil
import logging
from SAF.misc.ssh_utils import SSH



pytest.app_info = "HPX"
class Test_Suite_RGBKeyboard(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
        cls.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        cls.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx/properties.json"),cls.remote_artifact_path+"properties.json")    
        cls.fc.close_app()
        cls.fc.launch_app()
        # cls.fc.close_app()
        # cls.fc.launch_app()

   # only for Grogu
    def test_01_launch_C32230428(self):  
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        rgb_keyboard_text = self.fc.fd["rgb_keyboard"].verify_rgb_keyboard()
        assert rgb_keyboard_text=="RGB Keyboard Action Item","RGB keyboard is not visible at PC Device - {}".format(rgb_keyboard_text)
        self.fc.fd["rgb_keyboard"].click_rgb_keyboard()
        time.sleep(5)
        self.fc.fd["devices"].click_pc_device_title()
        rgb_keyboard_text = self.fc.fd["rgb_keyboard"].verify_rgb_keyboard()
        assert rgb_keyboard_text=="RGB Keyboard Action Item","RGB keyboard is not visible at PC Device - {}".format(rgb_keyboard_text)


    def test_02__verify_rgbkeyboard_module_C33568897(self):
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["rgb_keyboard"].click_rgb_keyboard()
        rgb_keyboard_text=self.fc.fd["rgb_keyboard"].get_rgb_keyboard_text()
        assert rgb_keyboard_text=="RGB KeyBoard","RGB KeyBoard text not present in the header"
        enable_rgb_lighting_text=self.fc.fd["rgb_keyboard"].get_enable_rgb_lighting_text()
        assert enable_rgb_lighting_text=="Enable RGB Lighting","Enable RGB Lighting not present in the RGB Keyboard module"
        static_text=self.fc.fd["rgb_keyboard"].get_static_text()
        assert static_text=="Static","Static tile is not present in RGB keyboard module"
        wave_text=self.fc.fd["rgb_keyboard"].get_wave_text()
        assert wave_text=="Wave","Wave tile is not present in RGB keyboard module"
        ripple_text=self.fc.fd["rgb_keyboard"].get_ripple_text()
        assert ripple_text=="Ripple","Ripple tile is not present in RGB keyboard module"
        breathing_text=self.fc.fd["rgb_keyboard"].get_breathing_text()
        assert breathing_text=="Breathing","Breathing tile is not present in RGB keyboard module"
        raindrops_text=self.fc.fd["rgb_keyboard"].get_raindrops_text()
        assert raindrops_text=="Raindrops","Raindrops tile is not present in RGB keyboard module"
        colorcycle_text=self.fc.fd["rgb_keyboard"].get_colorcycle_text()
        assert colorcycle_text=="Color Cycle","Color Cycle tile is not present in RGB keyboard module"


    def test_03_rgb_lighting_toggle_button_enable_and_Disable_state_C32230429(self): 
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["rgb_keyboard"].click_rgb_keyboard()
        state = self.fc.fd["rgb_keyboard"].get_RGB_lighting_toggle_button_state()
        if state=='0':
            self.fc.fd["rgb_keyboard"].click_RGB_lighting_toggle_button()

        self.fc.fd["rgb_keyboard"].click_RGB_lighting_toggle_button()
        state = self.fc.fd["rgb_keyboard"].get_RGB_lighting_toggle_button_state()
        assert state=='0',"RBG Lighting is not turned off"
        logging.info("IS enable" +str(self.fc.fd["rgb_keyboard"].is_enable_restore_default_tab()) )
        assert self.fc.fd["rgb_keyboard"].is_enable_restore_default_tab()==False,"Restore button is enabled"
        self.fc.fd["rgb_keyboard"].click_RGB_lighting_toggle_button()
        state = self.fc.fd["rgb_keyboard"].get_RGB_lighting_toggle_button_state()
        assert state=='1',"RBG Lighting is not turned off"
        assert self.fc.fd["rgb_keyboard"].is_enable_restore_default_tab()==True,"Restore button is disabled"
        logging.info("IS enable" +str(self.fc.fd["rgb_keyboard"].is_enable_restore_default_tab()) )


    #This test case is blocked due to missing brightness value property This script is only increasing and decresing to max and min
    def test_04_rgb_brightness_state_C32230430(self):
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["rgb_keyboard"].click_rgb_keyboard()    
        logging.info(str(self.fc.fd["rgb_keyboard"].get_slider_value()))
        self.fc.fd["rgb_keyboard"].set_slider_value_increase(50)
        self.fc.fd["rgb_keyboard"].set_slider_value_decrease(10)
        self.fc.fd["rgb_keyboard"].set_slider_value_increase(50)
        logging.info("Curremt Brightness Level " + str(type(self.fc.fd["rgb_keyboard"].get_brightness_level())))
        for txt in self.fc.fd["rgb_keyboard"].get_brightness_level().split("\n"):
            logging.info(str(txt))
        logging.info("Current Brightness Level " + str(self.fc.fd["rgb_keyboard"].get_brightness_level()[1]))
        self.fc.fd["rgb_keyboard"].click_restore_default_tab()
        self.fc.close_app()
        self.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
