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
from MobileApps.libs.ma_misc import ma_misc


pytest.app_info = "HPX"
class Test_Suite_Home(object):
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
    
    def test_01_welcome_page_C31823807(self,request):
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        redefining_your_PC_experience = self.fc.fd["home"].verify_welcome_message_on_homepage()
        assert redefining_your_PC_experience=="Redefining your PC experience","Not on home page because welcome message is not matching"
     
    def test_02_audio_control_homePage_C32088187(self):
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        redefining_your_PC_experience = self.fc.fd["home"].verify_welcome_message_on_homepage()
        assert redefining_your_PC_experience=="Redefining your PC experience","Not on home page because welcome message is not matching" 
        audio_control_text = self.fc.fd["home"].verify_audio_control()
        assert audio_control_text=="Audio control","Audio Control is not visible at Home Page - {}".format(audio_control_text)
      
    def test_03_video_control_homePage_C32088287(self):
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        redefining_your_PC_experience = self.fc.fd["home"].verify_welcome_message_on_homepage()
        assert redefining_your_PC_experience=="Redefining your PC experience","Not on home page because welcome message is not matching"   
        video_control_text = self.fc.fd["home"].verify_video_control()
        assert video_control_text=="Video control","Video Control is not visible at Home Page" 
       
# # Commenting out lines as Network booster is  currently enable in dev build only
    def test_04_view_all_control_link_homepage_C32088389(self):
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        redefining_your_PC_experience = self.fc.fd["home"].verify_welcome_message_on_homepage()
        assert redefining_your_PC_experience=="Redefining your PC experience","Not on home page because welcome message is not matching" 
        view_all_control_link = self.fc.fd["home"].verify_view_all_controls()
        assert view_all_control_link=="View all controls","View all controls is not visible at Home Page - {}".format(view_all_control_link) 
        self.fc.fd["home"].click_view_all_controls()
        audio_control_text = self.fc.fd["home"].verify_audio_control()
        assert audio_control_text=="Audio control","Audio Control is not visible at Home Page - {}".format(audio_control_text)
        video_control_text = self.fc.fd["home"].verify_video_control()
        assert video_control_text=="Video control","Video Control is not visible at Home Page" 
        support_icon_text = self.fc.fd["home"].verify_support_icon()
        assert support_icon_text=="Support Icon","Support is not visible at Home Page" 
        #network_booster_text = self.fc.fd["home"].verify_network_booster_item()
        #assert network_booster_text=="Network Booster","Network Booster is not visible at Home Page" 
        programmable_key_text = self.fc.fd["home"].verify_programmable_key()
        assert programmable_key_text=="Programmable Key Action Item","Programmable Key is not visible at Home Page" 
        self.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")

    def test_05_programmableKey_screen_visible_C32872393(self):
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        programmable_key_text = self.fc.fd["home"].verify_programmable_key()
        self.fc.fd["home"].click_programmable_key_card()
        programmable_key_text = self.fc.fd["home"].verify_programmable_keyNavTitle()
        assert programmable_key_text == "Programmable Key"

    def test_06_support_screen_visible_C32872396(self):
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        support_title_text = self.fc.fd["home"].verify_support_card_title()
        assert support_title_text == "Support"
        self.fc.fd["home"].click_support_card()
        support_header_title_text = self.fc.fd["home"].verify_support_screen_header_title()
        assert support_header_title_text == "Support"
