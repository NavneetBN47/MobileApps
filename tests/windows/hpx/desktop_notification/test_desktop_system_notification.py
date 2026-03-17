from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Desktop_System_Notification(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.sf = SystemFlow(cls.driver)
        cls.fc = FlowContainer(cls.driver)
        
        
    def test_01_verify_if_windows_notifications_are_turned_off_all_toggle_buttons_got_disabled_C32050342(self):
        self.sf.click_system_notification()
        logging.info("toggle notification "+ str(self.sf.get_toggle_notification_state()))
        if self.sf.get_toggle_notification_state()== "1":
            self.sf.turn_off_toggle_notification()
        self.sf.click_on_system_notification_close() 

        self.fc.launch_myHP()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].navigate_to_settings()
        self.fc.fd["settings"].click_notification_module()
        
        assert self.sf.verify_device_and_account()==False,"device and account notification is on"
        assert self.sf.verify_tips_and_tutorials()==False,"Tips and Tutorials notification is on"
        assert self.sf.verify_news_and_offers()==False,"News and Offers notification is on"
        assert self.sf.verify_share_your_feedback()==False,"share your feedback notification is on"

        self.sf.click_external_link()
        self.sf.click_confirmation_pop_up()
        logging.info("toggle notification "+ str(self.sf.get_toggle_notification_state()))
        if self.sf.get_toggle_notification_state()== "0":
            self.sf.turn_off_toggle_notification()
        self.sf.click_on_system_notification_close()   
       
        assert self.sf.verify_device_and_account()==True,"device and account notification isn't turned on"
        assert self.sf.verify_tips_and_tutorials()==True,"Tips and Tutorials notification isn't turned on"
        assert self.sf.verify_news_and_offers()==True,"News and Offers notification isn't turned on"
        assert self.sf.verify_share_your_feedback()==True,"share your feedback notification isn't turned on"

        self.sf.close_myhp_app()  
        
        
    
    
