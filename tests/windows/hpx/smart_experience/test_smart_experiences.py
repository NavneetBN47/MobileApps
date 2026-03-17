from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Smart_Experiences(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.web_driver = utility_web_session
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
            time.sleep(2)
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

        

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_01_hp_smart_experience_UI_C32810441(self):
        time.sleep(5)
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()

        assert self.fc.fd["smart_experience"].verify_privacy_alert_title() == "Privacy Alert"
        assert self.fc.fd["smart_experience"].verify_privacy_alert_subtitle() == "Receive a notification when Privacy Alert detects the presence of another person that may be able to view the content on your screen. This feature requires access to your camera."
        assert self.fc.fd["smart_experience"].verify_snooze_duration_title() == "Snooze Duration"
        assert self.fc.fd["smart_experience"].verify_privacy_alert_restoreBtn() == "Restore Default Settings"

        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        assert self.fc.fd["smart_experience"].verify_auto_screen_title() == "Auto Screen Dimming"
        assert self.fc.fd["smart_experience"].verify_auto_screen_subtitle() == "Save power by dimming the built-in display when you are not looking at the screen. This feature requires access to your camera."
        assert self.fc.fd["smart_experience"].verify_external_monitor_text() == "Disable when connected to an external monitor"
        assert self.fc.fd["smart_experience"].verify_auto_screen_restoreBtn() == "Restore Default Settings"    
        time.sleep(2)
        self.fc.kill_chrome_process()

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_02_disable_do_not_show_checkbox_C32810443(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
        time.sleep(5)
        time.sleep(3)
        self.fc.fd["smart_experience"].click_privacy_alert_restore_default_btn()
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_do_not_show_privacy_chkbox()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_continue_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_privacy_alert_button()

        time.sleep(2)
        assert bool(self.fc.fd["smart_experience"].verify_cancel_button_show()) is True
        self.fc.fd["smart_experience"].click_privacy_alert_dialogue_cancel_btn()

        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        time.sleep(3)       
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_do_not_show_dimming_chkbox()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_continue_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_auto_screen_button()

        time.sleep(2)
        assert bool(self.fc.fd["smart_experience"].verify_cancel_button_show()) is True
        self.fc.fd["smart_experience"].click_auto_screen_dimming_dialogue_cancel_btn()    
    
    @pytest.mark.ota
    def test_03_enable_do_not_show_checkbox_C32810442(self):
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
        self.fc.fd["smart_experience"].click_privacy_alert_restore_default_btn()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(2)

        webpage = "PRIVACY_ALERT"
        time.sleep(2)
        self.fc.fd["smart_experience"].click_privacy_alert_link()
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        current_url = self.web_driver.get_current_url()
        assert current_url == "https://www.hp.com/us-en/privacy/privacy-central.html"
        time.sleep(2)
        assert bool(self.fc.fd["smart_experience"].verify_cancel_button_show()) is True
        time.sleep(2)
        self.fc.fd["smart_experience"].click_privacy_alert_dialogue_cancel_btn()
        assert "0" == self.fc.fd["smart_experience"].verify_privacy_alert_btn_status()
        
        time.sleep(2)
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_continue_button()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(2)
        assert bool(self.fc.fd["smart_experience"].verify_cancel_button_show()) is False

        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(2)

        webpage = "Hp_Privacy_Statement"
        time.sleep(2)
        self.fc.fd["smart_experience"].click_privacy_alert_link()
        self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        current_url = self.web_driver.get_current_url()
        assert current_url == "https://www.hp.com/us-en/privacy/privacy-central.html"
        self.web_driver.close()
        time.sleep(2)
        assert bool(self.fc.fd["smart_experience"].verify_cancel_button_show()) is True

        self.fc.fd["smart_experience"].click_auto_screen_dimming_dialogue_cancel_btn()
        assert "0" == self.fc.fd["smart_experience"].verify_auto_screen_dimming_btn_status()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_continue_button()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(2)
        assert bool(self.fc.fd["smart_experience"].verify_cancel_button_show()) is False
    
    @pytest.mark.ota
    def test_04_smart_experience_module_show_C32810453(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)

        assert bool(self.fc.fd["smart_experience"].verify_privacy_alert_item_tab_show()) is True
        assert bool(self.fc.fd["smart_experience"].verify_auto_screen_item_tab_show()) is True    

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_05_privacy_alert_ui_C32810464(self):
        time.sleep(3)
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        time.sleep(5)
       
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()

        assert self.fc.fd["smart_experience"].verify_privacy_alert_title() == "Privacy Alert"
        assert self.fc.fd["smart_experience"].verify_privacy_alert_subtitle() == "Receive a notification when Privacy Alert detects the presence of another person that may be able to view the content on your screen. This feature requires access to your camera."
        assert self.fc.fd["smart_experience"].verify_snooze_duration_title() == "Snooze Duration"
        assert self.fc.fd["smart_experience"].verify_privacy_alert_restoreBtn() == "Restore Default Settings"

        self.fc.fd["smart_experience"].click_privacy_alert_restore_default_btn()
        time.sleep(3)
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(2)

        assert self.fc.fd["smart_experience"].verify_privacy_popup_title() == "Privacy Alert"
        assert self.fc.fd["smart_experience"].verify_privacy_popup_subtitle() == "This feature requires access to your camera in order to function. Do you wish to continue?"
        assert self.fc.fd["smart_experience"].get_hp_privacy_statement_text().strip() == "HP's Privacy Statement"
        assert self.fc.fd["smart_experience"].verify_do_not_text_show() == "Do not show again"
        assert self.fc.fd["smart_experience"].get_cancle_btn_on_popup() == "Cancel"
        assert self.fc.fd["smart_experience"].get_continue_btn_on_popup() == "Continue"    

    @pytest.mark.ota
    def test_06_privacy_alert_button_C32810465(self):
        time.sleep(3)
        self.fc.re_install_app_launch_myHP(self.driver.session_data["installer_path"])
        time.sleep(3)

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()
        assert self.fc.fd["smart_experience"].verify_privacy_alert_btn_status() == '0'
        time.sleep(2)
        
        if self.fc.fd["smart_experience"].verify_privacy_alert_btn_status() == "0":
            self.fc.fd["smart_experience"].click_privacy_alert_button()
            time.sleep(2)
            self.fc.fd["smart_experience"].click_continue_button()
            time.sleep(2)
        
        assert bool(self.fc.fd["smart_experience"].verify_privacy_alert_btn_status()) == True

        self.fc.fd["smart_experience"].click_snooze_dropdown_list()
        time.sleep(2)
        assert bool(self.fc.fd["smart_experience"].verify_end_of_day_show()) is True

        self.fc.fd["smart_experience"].click_privacy_alert_button()
        self.fc.fd["smart_experience"].click_privacy_alert_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_snooze_dropdown_list()
        time.sleep(2)
        assert bool(self.fc.fd["smart_experience"].verify_end_of_day_show()) is False

    @pytest.mark.ota
    def test_07_privacy_alert_button_and_drop_list_C32810466(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()

        if self.fc.fd["smart_experience"].verify_privacy_alert_btn_status() == "0":
            self.fc.fd["smart_experience"].click_privacy_alert_button()
            time.sleep(2)
        
        self.fc.fd["smart_experience"].click_snooze_dropdown_list()
        time.sleep(2)
        assert bool(self.fc.fd["smart_experience"].verify_ten_minutes_show()) is True
    
    @pytest.mark.ota
    def test_08_snooze_duration_C32810467(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()

        if self.fc.fd["smart_experience"].verify_privacy_alert_btn_status() == "0":
            self.fc.fd["smart_experience"].click_privacy_alert_button()
            time.sleep(2)
        
        self.fc.fd["smart_experience"].click_snooze_dropdown_list()
        time.sleep(2)
        assert bool(self.fc.fd["smart_experience"].verify_five_minutes_show())  is True
        assert bool(self.fc.fd["smart_experience"].verify_ten_minutes_show())  is True
        assert bool(self.fc.fd["smart_experience"].verify_thirty_minutes_show())  is True
        assert bool(self.fc.fd["smart_experience"].verify_one_hour_show())  is True
        assert bool(self.fc.fd["smart_experience"].verify_end_of_day_show())  is True

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_09_auto_screen_dimming_ui_C32810468(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        time.sleep(2)
        assert self.fc.fd["smart_experience"].verify_auto_screen_title() == "Auto Screen Dimming", "Auto Screen Dimming title is not correct"
        assert self.fc.fd["smart_experience"].verify_auto_screen_subtitle() == "Save power by dimming the built-in display when you are not looking at the screen. This feature requires access to your camera.", "Auto Screen Dimming subtitle is not correct"
        assert self.fc.fd["smart_experience"].verify_external_monitor_text() == "Disable when connected to an external monitor", "External monitor text is not correct"
        assert self.fc.fd["smart_experience"].verify_auto_screen_restoreBtn() == "Restore Default Settings", "Restore Default Settings button is not correct"
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        time.sleep(5)
        self.fc.fd["smart_experience"].click_auto_screen_button()    
        time.sleep(2)
        assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_title() == "Auto Screen Dimming", "Auto Screen Dimming title is not correct"
        assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_subtitle() == "This feature requires access to your camera in order to function. Do you wish to continue?", "Auto Screen Dimming subtitle is not correct"
        assert self.fc.fd["smart_experience"].get_hp_privacy_link_btn_on_popup().strip() == "HP's Privacy Statement", "HP's Privacy Statement is not correct"
        assert self.fc.fd["smart_experience"].verify_do_not_text_show() == "Do not show again", "Do not show again text is not correct"
        assert self.fc.fd["smart_experience"].get_cancel_btn_auto_screen_dimming_popup() == "Cancel", "Cancel button is not correct"
        assert self.fc.fd["smart_experience"].get_continue_btn_auto_screen_dimming_popup() == "Continue", "Continue button is not correct"

    @pytest.mark.ota
    def test_10_verify_auto_dimming_toggle_C32810469(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_restore_btn_auto_dimming()
        time.sleep(5)
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_do_not_show_checkbox()
        time.sleep(2)
        self.fc.fd["smart_experience"].click_continue_button()
        time.sleep(2)

        assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_btn_status() == "1"
        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(2)
        assert self.fc.fd["smart_experience"].verify_auto_screen_dimming_btn_status() == "0"

    def test_11_persisting_auto_dimming_settings_C32810504(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)

        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        time.sleep(2)

        self.fc.fd["smart_experience"].click_auto_screen_button()
        time.sleep(3)

        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        time.sleep(2)

        assert bool(self.fc.fd["smart_experience"].verify_auto_screen_dimming_btn_status()) is True
    
    def test_12_main_screen_C32810444(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(6)

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        
        assert bool(self.fc.fd["navigation_panel"].verify_welcome_module_show()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_devices_menu_navigation()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_support_menu_navigation()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_settings_menu_navigation()) is True
    
    @pytest.mark.ota
    def test_13_application_card_ui_C32810456(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(6)

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_privacy_alert()

        assert self.fc.fd["smart_experience"].verify_privacy_alert_title() == "Privacy Alert"
        assert self.fc.fd["smart_experience"].verify_privacy_alert_subtitle() == "Receive a notification when Privacy Alert detects the presence of another person that may be able to view the content on your screen. This feature requires access to your camera."
        assert self.fc.fd["smart_experience"].verify_snooze_duration_title() == "Snooze Duration"
        assert self.fc.fd["smart_experience"].verify_privacy_alert_restoreBtn() == "Restore Default Settings"

        time.sleep(3)

        self.fc.fd["navigation_panel"].navigate_to_auto_dimming()
        assert self.fc.fd["smart_experience"].verify_auto_screen_title() == "Auto Screen Dimming"
        assert self.fc.fd["smart_experience"].verify_auto_screen_subtitle() == "Save power by dimming the built-in display when you are not looking at the screen. This feature requires access to your camera."
        assert self.fc.fd["smart_experience"].verify_external_monitor_text() == "Disable when connected to an external monitor"
        assert self.fc.fd["smart_experience"].verify_auto_screen_restoreBtn() == "Restore Default Settings"