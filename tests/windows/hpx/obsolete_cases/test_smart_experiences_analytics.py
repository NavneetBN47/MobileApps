from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import logging
import time

pytest.app_info = "HPX"
class Test_Suite_Smart_Experiences_Analytics(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.web_driver = utility_web_session
        time.sleep(10)
        cls.fc.close_app()
        time.sleep(2)
        cls.fc.launch_app()

    def test_01_privacy_alert_switch_on_analytics_C36084434(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
        self.fc.fd["smart_experience"].click_privacy_alert_restore_default_btn()
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_PRIVACY_ALERT_SWITCH_ON")
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onValueChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="privacyalert-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_SMARTEXPERIENCE_PRIVACY_ALERT_SWITCH_ON","AUID Field did not generate"
        self.fc.fd["smart_experience"].click_privacy_alert_dialogue_cancel_btn()
        self.fc.delete_capture_analytics_files()

    def test_02_analytics_privacy_alert_dialogue_cancel_btn_C36094559(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
        self.fc.fd["smart_experience"].click_privacy_alert_restore_default_btn()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_privacy_alert_dialogue_cancel_btn()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_PRIVACY_ALERT_MODALDLG_CANCEL_BTN")
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="privacyalert-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_SMARTEXPERIENCE_PRIVACY_ALERT_MODALDLG_CANCEL_BTN","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()

    def test_03_do_not_show_checkbox_analytics_C36165612(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
        self.fc.fd["smart_experience"].click_privacy_alert_restore_default_btn()
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(5)
        self.fc.fd["smart_experience"].click_do_not_show_checkbox()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_do_not_show_checkbox()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_PRIVACY_ALERT_MODALDLG_CHECKBOX")
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="privacyalert-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_SMARTEXPERIENCE_PRIVACY_ALERT_MODALDLG_CHECKBOX","AUID Field did not generate"
        self.fc.fd["smart_experience"].click_privacy_alert_dialogue_cancel_btn()
        self.fc.delete_capture_analytics_files()

    def test_04_privacy_link_analytics_C36094557(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
        self.fc.fd["smart_experience"].click_privacy_alert_restore_default_btn()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(2)
        webpage = "Privacy Statement"
        time.sleep(5)
        self.fc.fd["smart_experience"].click_privacy_alert_link()
        time.sleep(3)
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_PRIVACY_ALERT_MODALDLG_PRIVACYLINK_BTN")
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="privacyalert-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_SMARTEXPERIENCE_PRIVACY_ALERT_MODALDLG_PRIVACYLINK_BTN","AUID Field did not generate"
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        self.fc.fd["smart_experience"].click_privacy_alert_dialogue_cancel_btn()
        self.fc.delete_capture_analytics_files()

    def test_05_privacy_alert_continue_btn_analytics_C36165628(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
        self.fc.fd["smart_experience"].click_privacy_alert_restore_default_btn()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_do_not_show_checkbox()
        self.fc.fd["smart_experience"].click_continue_button()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_PRIVACY_ALERT_MODALDLG_CONTINUE_BTN")
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="privacyalert-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_SMARTEXPERIENCE_PRIVACY_ALERT_MODALDLG_CONTINUE_BTN","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()

    def test_06_privacy_alert_switch_off_analytics_C36084391(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_PRIVACY_ALERT_SWITCH_OFF")
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onValueChange", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="privacyalert-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_SMARTEXPERIENCE_PRIVACY_ALERT_SWITCH_OFF","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()

    def test_07_privacy_alert_restore_default_btn_analytics_C36165623(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
        self.fc.fd["smart_experience"].click_privacy_alert_restore_default_btn()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_PRIVACY_ALERT_RESTORE_DEFAULT_SETTINGS_BUTTON")
        logging.info("{}".format(event))
        assert len(event)>0,"Analytics Event not found."
        assert event["2"]=="Navigation","EventCategory field name did not generate"
        assert event["3"]=="onPress", "EventType field name did not generate"
        assert event["4"]=="UserEngaged","EventName field name did not generate"
        assert event["11"]=="privacyalert-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_SMARTEXPERIENCE_PRIVACY_ALERT_RESTORE_DEFAULT_SETTINGS_BUTTON","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()

    def test_08_autoscreen_dimming_switch_btn_on_analytics_C36248631(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(3)
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_SWITCH_ON")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"]== "Navigation","EventCategory field name did not generate"
        assert event["3"]== "onValueChange", "EventType field name did not generate"
        assert event["4"]== "UserEngaged","EventName field name did not generate"
        assert event["11"]== "autoscreendimming-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_SWITCH_ON","AUID Field did not generate"
        self.fc.fd["smart_experience"].click_auto_screen_dimming_dialogue_cancel_btn()
        self.fc.delete_capture_analytics_files()

    def test_09_autoscreen_dimming_privacy_link_analytics_C36248593(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        webpage = "Privacy Statement"
        time.sleep(2)
        self.fc.fd["smart_experience"].click_autoscreen_dimming_link()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_MODALDLG_PRIVACYLINK_BTN")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"]== "Navigation","EventCategory field name did not generate"
        assert event["3"]== "onPress", "EventType field name did not generate"
        assert event["4"]== "UserEngaged","EventName field name did not generate"
        assert event["11"]== "autoscreendimming-core","ScreenName field name  did not generate"
        assert event["12"]== "AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_MODALDLG_PRIVACYLINK_BTN","AUID Field did not generate"
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        self.fc.fd["smart_experience"].click_auto_screen_dimming_dialogue_cancel_btn()
        self.web_driver.close()
        self.fc.delete_capture_analytics_files()

    # we will have to update this test case AUID event once the bug is fixed
    def test_10_autoscreen_dimming_checbox_modal_analytics_C36248563(self):        
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        self.fc.fd["smart_experience"].click_do_not_show_dimming_chkbox()
        self.fc.fd["smart_experience"].click_do_not_show_dimming_chkbox()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_MODALDLG_CHECKBOX")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"]== "Navigation","EventCategory field name did not generate"
        assert event["3"]== "onChange", "EventType field name did not generate"
        assert event["4"]== "UserEngaged","EventName field name did not generate"
        assert event["11"]== "autoscreendimming-core","ScreenName field name  did not generate"
        assert event["12"]== "AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_MODALDLG_CHECKBOX","AUID Field did not generate"
        self.fc.fd["smart_experience"].click_auto_screen_dimming_dialogue_cancel_btn()
        self.fc.delete_capture_analytics_files()

    def test_11_autoscreen_dimming_dialogue_cancel_btn_analytics_C36248629(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_auto_screen_dimming_dialogue_cancel_btn()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_MODALDLG_CANCEL_BTN")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"]== "Navigation","EventCategory field name did not generate"
        assert event["3"]== "onPress", "EventType field name did not generate"
        assert event["4"]== "UserEngaged","EventName field name did not generate"
        assert event["11"]== "autoscreendimming-core","ScreenName field name  did not generate"
        assert event["12"]=="AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_MODALDLG_CANCEL_BTN","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()
       
    def test_12_autoscreen_dimming_continue_btn_analytics_C36248592(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_do_not_show_checkbox()
        self.fc.fd["smart_experience"].click_continue_button()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_MODALDLG_CONTINUE_BTN")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"]== "Navigation","EventCategory field name did not generate"
        assert event["3"]== "onPress", "EventType field name did not generate"
        assert event["4"]== "UserEngaged","EventName field name did not generate"
        assert event["11"]== "autoscreendimming-core","ScreenName field name  did not generate"
        assert event["12"]== "AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_MODALDLG_CONTINUE_BTN","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()

    def test_13_autoscreen_dimming_external_display_checkbox__unchecked_analytics_C36248812(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True 
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_autoscreen_checkbox()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_EXTERNAL_DISPLAY_CHECKBOX_UNCHECKED")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"]== "Navigation","EventCategory field name did not generate"
        assert event["3"]== "onValueChange", "EventType field name did not generate"
        assert event["4"]== "UserEngaged","EventName field name did not generate"
        assert event["11"]== "autoscreendimming-core","ScreenName field name  did not generate"
        assert event["12"]== "AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_EXTERNAL_DISPLAY_CHECKBOX_UNCHECKED","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()        

    def test_14_autoscreen_dimming_external_display_checkbox_Checked_analytics_C36248780(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True 
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_autoscreen_checkbox()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_EXTERNAL_DISPLAY_CHECKBOX_CHECKED")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"]== "Navigation","EventCategory field name did not generate"
        assert event["3"]== "onValueChange", "EventType field name did not generate"
        assert event["4"]== "UserEngaged","EventName field name did not generate"
        assert event["11"]== "autoscreendimming-core","ScreenName field name  did not generate"
        assert event["12"]== "AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_EXTERNAL_DISPLAY_CHECKBOX_CHECKED","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()        

    def test_15_autoscreen_dimming_switch_turn_off_analytics_C36248738(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(2)
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_SWITCH_OFF")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"]== "Navigation","EventCategory field name did not generate"
        assert event["3"]== "onValueChange", "EventType field name did not generate"
        assert event["4"]== "UserEngaged","EventName field name did not generate"
        assert event["11"]== "autoscreendimming-core","ScreenName field name  did not generate"
        assert event["12"]== "AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_SWITCH_OFF","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()

    def test_16_auto_screen_dimming_restore_btn_C36248830(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_RESTORE_DEFAULT_SETTINGS_BUTTON")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"]== "Navigation","EventCategory field name did not generate"
        assert event["3"]== "onPress", "EventType field name did not generate"
        assert event["4"]== "UserEngaged","EventName field name did not generate"
        assert event["11"]== "autoscreendimming-core","ScreenName field name  did not generate"
        assert event["12"]== "AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_RESTORE_DEFAULT_SETTINGS_BUTTON","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()

    def test_17_continue_btn_on_popup_C36248591(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        self.fc.fd["smart_experience"].click_toggle_switch_auto_dimming_popup()
        self.fc.fd["smart_experience"].click_do_not_show_checkbox()
        self.fc.fd["smart_experience"].click_continue_btn_auto_screen_dimming_popup()
        event = self.fc.capture_analytics_event("AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_MODALDLG_CONTINUE_BTN")
        logging.info("{}".format(event))
        assert len(event) > 0,"Analytics Event not found."
        assert event["2"]== "Navigation","EventCategory field name did not generate"
        assert event["3"]== "onPress", "EventType field name did not generate"
        assert event["4"]== "UserEngaged","EventName field name did not generate"
        assert event["11"]== "autoscreendimming-core","ScreenName field name  did not generate"
        assert event["12"]== "AUID_SMARTEXPERIENCE_AUTO_SCREEN_DIM_MODALDLG_CONTINUE_BTN","AUID Field did not generate"
        self.fc.delete_capture_analytics_files()