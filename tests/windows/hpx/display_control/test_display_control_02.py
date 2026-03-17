import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
from SAF.misc import saf_misc
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Display_Control_02(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
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
            time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
    
    def round_up(self,input_value):
        return round(float(input_value))

    #this suite should run in bopeep
    def test_01_lbl_scheduler_default_value_C35370267(self):
        self.fc.reset_myhp_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        assert self.fc.fd["display_control"].verify_pcdevices_display_title() == "Display control","Display title is not present"
        time.sleep(5)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        advance_settings_for_lbl_scheduler_icon = self.fc.fd["display_control"].verify_advaced_setting_visible()
        assert advance_settings_for_lbl_scheduler_icon=="Advance Setting","Advance Setting is not visible at display control page - {}".format(advance_settings_for_lbl_scheduler_icon)
        self.fc.fd["display_control"].click_advaced_setting()
        if self.fc.fd["display_control"].toggle_notification_state()=="0":
            self.fc.fd["display_control"].click_schedule_toggle_turn_on()
        #verify Turn-On time should display (10:00/PM) and Turn-Off time should display (7:00/AM)
        assert  "10:00" in  self.fc.fd["display_control"].verify_on_hour_time(),"Time is not present"
        assert  "pm" in self.fc.fd["display_control"].verify_turn_on_default_pm_time(),"Time zone is not present"
        assert  "7:00" in self.fc.fd["display_control"].verify_off_hour_time(),"Time is not present"
        assert  "am" in self.fc.fd["display_control"].verify_turn_off_default_am_time(),"Time zone is not present"


    def test_02_low_blue_light_scheduler_toggle_button_C32194978(self):
        time.sleep(5)
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        advance_settings_for_lbl_scheduler_icon = self.fc.fd["display_control"].verify_advaced_setting_visible()
        assert advance_settings_for_lbl_scheduler_icon=="Advance Setting","Advance Setting is not visible at display control page - {}".format(advance_settings_for_lbl_scheduler_icon)
        self.fc.fd["display_control"].click_advaced_setting()
        for _ in range(5):
            self.fc.fd["display_control"].click_schedule_toggle_turn_on()
            if self.fc.fd["display_control"].toggle_notification_state()=="0":
                 #self.fc.fd["display_control"].click_schedule_toggle_turn_on()
                 assert self.fc.fd["display_control"].toggle_notification_state()=="0","Toggle button is not off"
            if self.fc.fd["display_control"].toggle_notification_state()=="1":
                 #self.fc.fd["display_control"].click_schedule_toggle_turn_on()
                 assert self.fc.fd["display_control"].toggle_notification_state()=="1","Toggle button is not on"
    
    @pytest.mark.ota
    def test_03_restore_defaults_for_app_settings_C38792779(self):
        self.fc.reset_myhp_app()
        time.sleep(2)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not present"
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        self.fc.fd["display_control"].click_restore_defaults_button()
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()

        self.fc.fd["display_control"].click_add_application_btn()
        self.fc.fd["display_control"].search_application("Calculator")
        self.fc.fd["display_control"].click_to_select_calculator_app()
        self.fc.fd["display_control"].click_add_btn()
        #step3
        self.fc.fd["display_control"].click_to_select_calculator_app()
        #select night mode for calculator
        self.fc.fd["display_control"].click_night_mode()
        
        self.fc.fd["display_control"].click_to_select_calculator_app()
        calculator_app=self.fc.fd["display_control"].verify_calculator_app()
        time.sleep(5)
        assert calculator_app == "Calculator","Calculator is not visible at Add Application"
        assert self.fc.fd["display_control"].is_night_mode_selected() == 'true',"Night mode is not selected"
        #step4
        self.fc.fd["display_control"].click_restore_defaults_button()
        assert bool(self.fc.fd["display_control"].verify_restore_pop_up_windows_title()) == True ,"Restore Pop up window is not present"
        #not able to verify check box due to-HPXAPPS-8193
        #assert self.fc.fd["display_control"].get_restore_popup_check_box_state() == '0' ,"Do not check box not checked in restore Pop up window"
        assert bool(self.fc.fd["display_control"].verify_hdr_restore_pop_up_windows_checkbox()) == True ,"check box not available on HDR Restore Pop up window"
        assert bool(self.fc.fd["display_control"].verify_hdr_restore_pop_up_windows_cancel_button()) == True ,"Cancel button not available on Restore Pop up window"
        assert bool(self.fc.fd["display_control"].verify_restore_factory_settings_continue()) == True ,"Continue button not available on Restore Pop up window"
        assert bool(self.fc.fd["display_control"].verify_close_btn_on_restore_popup()) == True ,"Close button not available on Restore Pop up window"
        #step5
        self.fc.fd["display_control"].click_restore_pop_up_windows_cancel_button()
        assert bool(self.fc.fd["display_control"].verify_restore_pop_up_windows_title()) == False ,"Restore Pop up window is present"
        assert self.fc.fd["display_control"].is_night_mode_selected() == 'true',"Night mode is not selected"
        #step6
        self.fc.fd["display_control"].click_restore_defaults_button()
        assert bool(self.fc.fd["display_control"].verify_restore_pop_up_windows_title()) == True ,"Restore Pop up window is not present"
        self.fc.fd["display_control"].click_restore_pop_up_do_not_show_checkbox()
        #step7
        self.fc.fd["display_control"].click_continue_button_dialog()
        assert bool(self.fc.fd["display_control"].verify_restore_pop_up_windows_title()) == False ,"Restore Pop up window is present"
        
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(5)
        assert self.fc.fd["display_control"].verify_neutral_mode_selected() == 'true',"Neutral mode is not selected"
        #step8
        self.fc.fd["display_control"].click_restore_defaults_button()
        assert bool(self.fc.fd["display_control"].verify_restore_pop_up_windows_title()) == False ,"Restore Pop up window is not present"
        assert self.fc.fd["display_control"].verify_neutral_mode_selected() == 'true',"Neutral mode is not selected"    
    
    @pytest.mark.ota
    def test_04_display_control_and_app_settings_global_settings_C37825791(self):
        self.fc.reset_myhp_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()

        self.fc.fd["display_control"].click_restore_defaults_button()
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(8)
        assert bool(self.fc.fd["display_control"].verify_default_global_app()) == True ,"global app icon is not present"
        assert bool(self.fc.fd["display_control"].verify_add_application_text()) is True, "Add application text is not present"
        #select display mode as "Night" b=28,c=100
        self.fc.fd["display_control"].click_night_mode()
        assert bool(self.fc.fd["display_control"].is_night_mode_selected()) == True ,"Night mode is not selected"
        #Change Brightness and contrast value
        time.sleep(5) 
        self.fc.fd["display_control"].set_slider_value_decrease(5,"Brightness_slider")
        assert self.fc.fd["display_control"].get_brightness_slider_value_100() == "23","Brightness slider value is not 23"
        self.fc.fd["display_control"].set_slider_value_decrease(10,"Contrast_slider")
        assert self.fc.fd["display_control"].get_contrast_slider_value_100() == "90","Contrast slider value is not 90"
        # Add any new application to the application list

        software_list = ["calculator", "clock", "access"]
        for software in software_list:
            self.fc.fd["context_aware"].click_add_application()
            self.fc.fd["context_aware"].click_add_application_search_box()
            self.fc.fd["context_aware"].search_application(software)
            self.fc.fd["context_aware"].click_application(software)
            self.fc.fd["context_aware"].click_add_application_add_button()
            
        self.fc.fd["display_control"].click_to_select_calculator_app()
        assert self.fc.fd["display_control"].verify_calculator_app() == "Calculator","Calculator App is not present"
        brightness_value_calulator = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        contrast_value_calculator = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        self.fc.fd["display_control"].click_global_app_icon()
        time.sleep(2)
        global_app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        global_app_contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        assert global_app_brightness_value == brightness_value_calulator,"Brightness value is not same"
        assert global_app_contrast_value == contrast_value_calculator,"Contrast value is not same"

        self.fc.fd["audio"].click_clock_app_under_application_items()
        assert self.fc.fd["audio"].get_clock_under_application_items() == "Clock","Clock App is not present"
        clock_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        clock_contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        
        self.fc.fd["display_control"].click_global_app_icon()
        global_app_brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        global_app_contrast_value = self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider")
        assert global_app_brightness_value == clock_brightness_value,"Brightness value is not same"
        assert global_app_contrast_value == clock_contrast_value,"Contrast value is not same"

        #Change RGB Color
        self.fc.fd["display_control"].verify_advaced_setting_visible()
        time.sleep(2)
        self.fc.fd["display_control"].click_advaced_setting()       
        self.fc.fd["display_control"].set_red_slider_value_decrease(5,"red_slider")
        self.fc.fd["display_control"].set_green_slider_value_decrease(5,"green_slider")
        self.fc.fd["display_control"].set_blue_slider_value_decrease(5,"blue_slider")
        
        assert self.fc.fd["display_control"].verify_red_slider_value() == "95","Red slider value is not 95"
        assert self.fc.fd["display_control"].verify_green_slider_value() == "95","Green slider value is not 95"
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "95","Blue slider value is not 95"                
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
    
    @pytest.mark.ota
    def test_05_display_control_and_app_settings_restore_to_global_settings_C37825792(self):
        self.fc.reset_myhp_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        assert bool(self.fc.fd["display_control"].verify_default_global_app()) == True ,"global app icon is not present"
        assert bool(self.fc.fd["display_control"].verify_add_application_text()) is True, "Add application text is not present"
        
        self.fc.fd["display_control"].click_restore_defaults_button()
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(8)
        assert self.fc.fd["display_control"].verify_neutral_mode_selected() == 'true',"Neutral mode is not selected"
        time.sleep(4)
        self.fc.fd["display_control"].verify_add_application_text()
        self.fc.fd["display_control"].click_add_application_btn()
        self.fc.fd["display_control"].search_application("calculator")
        self.fc.fd["display_control"].click_to_select_calculator_app()
        self.fc.fd["display_control"].click_add_btn()
        
        self.fc.fd["context_aware"].click_calculator_icon()

        #select display mode as "Night"
        self.fc.fd["display_control"].click_night_mode()
        assert bool(self.fc.fd["display_control"].is_night_mode_selected()) == True ,"Night mode is not selected"
        #Change RGB values
        self.fc.fd["display_control"].verify_advaced_setting_visible()
        self.fc.fd["display_control"].click_advaced_setting()        
        self.fc.fd["display_control"].set_red_slider_value_decrease(5,"red_slider")
        self.fc.fd["display_control"].set_green_slider_value_decrease(5,"green_slider")
        self.fc.fd["display_control"].set_blue_slider_value_decrease(5,"blue_slider")
        
        assert self.fc.fd["display_control"].verify_red_slider_value() == "95","Red slider value is not 95"
        assert self.fc.fd["display_control"].verify_green_slider_value() == "95","Green slider value is not 95"
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "95","Blue slider value is not 95"                
        self.fc.fd["display_control"].click_close_btn_advanced_settings()        

        self.fc.fd["display_control"].click_restore_defaults_button()
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()

        time.sleep(8)
        assert self.fc.fd["display_control"].verify_neutral_mode_selected() == 'true',"Neutral mode is not selected"
        self.fc.fd["display_control"].click_advaced_setting()
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100","Red value is not 100"
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100","Green value is not 100"
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100","Blue value is not 100"
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
    
    @pytest.mark.ota
    def test_06_display_control_and_app_settings_restore_to_factory_settings_C37825793(self):
        self.fc.reset_myhp_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        assert bool(self.fc.fd["display_control"].verify_default_global_app()) == True ,"global app icon is not present"
        assert self.fc.fd["display_control"].verify_add_application_text() == "Add Application","Add application text is not present"

        self.fc.fd["display_control"].click_add_application_btn()
        assert bool(self.fc.fd["display_control"].verify_applications_display()) == True ,"Applications title is not present"
        self.fc.fd["display_control"].search_application("Calculator")
        assert self.fc.fd["display_control"].verify_calculator_app() == "Calculator","Calculator App is not present"
        self.fc.fd["display_control"].click_to_select_calculator_app()
        
        self.fc.fd["display_control"].click_add_btn()
        assert self.fc.fd["display_control"].verify_calculator_app() == "Calculator","Calculator App is not present"
        #make some changes for calculator app like mode to be reading
        self.fc.fd["display_control"].click_to_select_calculator_app()
        self.fc.fd["display_control"].click_reading_mode()
        assert self.fc.fd["display_control"].is_reading_mode_selected() == 'true',"Reading mode is not selected"
        self.fc.fd["display_control"].click_to_select_calculator_app()
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "52","Brightness slider value is not 48"
        
        self.fc.fd["display_control"].click_global_app_icon()
        #Global application should be selected (not verify due to bug-20063)

        self.fc.fd["display_control"].click_restore_defaults_button()
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(8)
        assert self.fc.fd["display_control"].verify_neutral_mode_selected() == 'true',"Neutral mode is not selected"
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "76","Brightness slider value is not 50"
        assert self.fc.fd["display_control"].get_brightness_slider_value("Contrast_slider") == "100","Contrast_slider slider value is not 95"

    @pytest.mark.ota
    def test_07_display_control_and_app_settings_adding_new_application_to_the_list_C37825794(self):
        self.fc.reset_myhp_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(5)
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        assert bool(self.fc.fd["display_control"].verify_default_global_app()) == True ,"global app icon is not present"
        assert self.fc.fd["display_control"].verify_add_application_text() == "Add Application","Add application text is not present"
        
        self.fc.fd["display_control"].click_add_application_btn()
        assert bool(self.fc.fd["display_control"].verify_applications_display()) == True ,"Applications title is not present"
        self.fc.fd["display_control"].search_application("Calculator")
        assert self.fc.fd["display_control"].verify_calculator_app() == "Calculator","Calculator App is not present"
        self.fc.fd["display_control"].click_to_select_calculator_app()

        self.fc.fd["display_control"].click_add_btn()
        assert self.fc.fd["display_control"].verify_calculator_app() == "Calculator","Calculator App is not present"

    @pytest.mark.ota
    def test_08_add_application_hover_state_C37825788(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("calendar")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("calendar")), True, "Calendar is not present")
        self.fc.fd["context_aware"].click_application("calendar")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("calendar"), "Calendar", "Calendar is not added")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("camera")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("camera")), True, "Camera is not present")
        self.fc.fd["context_aware"].click_application("camera")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("camera"), "Camera", "Camera is not added")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("Access")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("access")), True, "Access is not present")
        self.fc.fd["context_aware"].click_application("access")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("access"), "Access", "Access is not added")
        #click over access app
        self.fc.fd["context_aware"].click_access_app()
        self.fc.fd["display_control"].click_access_app_delete_button()
        self.fc.fd["display_control"].click_continue_on_delete_app_setting()
        soft_assertion.assert_not_contains(self.fc.fd["display_control"].get_app_name_from_app_add_list(), "Access", "Access app is not available")
        soft_assertion.raise_assertion_errors()
    @pytest.mark.ota
    def test_09_add_any_application_C37825789(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("calendar")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("calendar")), True, "Calendar is not present")
        self.fc.fd["context_aware"].click_application("calendar")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("calendar"), "Calendar", "Calendar is not added")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("camera")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("camera")), True, "Camera is not present")
        self.fc.fd["context_aware"].click_application("camera")
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon("camera"), "Camera", "Camera is not added")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("Access")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("access")), True, "Access is not present")
        self.fc.fd["context_aware"].click_application("access")
        self.fc.fd["context_aware"].click_add_application_add_button()

        self.fc.fd["context_aware"].click_application("access")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("access")), True, "Access is not present")
        self.fc.fd["context_aware"].click_application("camera")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("camera")), True, "Camera is not present")
        self.fc.fd["context_aware"].click_application("calendar")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application("calendar")), True, "Calendar is not present")
        soft_assertion.raise_assertion_errors()

    
    def test_10_brightness_slider_value_remains_same_after_relaunch_the_app_C37210042(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")

        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        if brightness_value!=100:
            self.fc.fd["display_control"].set_slider_value_increase(100,"Brightness_slider")
        self.fc.fd["display_control"].set_slider_value_decrease(15,"Brightness_slider")
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "85"==brightness_value,"brghtness value not increased to 85"
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_display_control()
        brightness_value = self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider")
        assert "85"==brightness_value,"brghtness value not increased to 85"
