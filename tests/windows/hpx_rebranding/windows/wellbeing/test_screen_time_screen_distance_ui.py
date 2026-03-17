import time
import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Suite_Screen_Time_UI(object):
    
    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_01_check_screen_time_ui_C43876435(self):
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)

        assert self.fc.fd["wellbeing"].verify_screen_time_title_show_up(), "Screen time title is not displayed"
        assert self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "0", "Screen time toggle is not off"
        assert self.fc.fd["wellbeing"].verify_screen_time_bar_chart_show_up(), "Screen time bar chart is not displayed"
        assert self.fc.fd["wellbeing"].verify_send_a_reminder_toogle_status() == "0", "Send a reminder toggle is not off"
    

    @pytest.mark.ota
    @pytest.mark.function
    @pytest.mark.integration
    def test_02_check_screen_distance_ui_C43876480(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(1)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=10)
        time.sleep(2)

        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen Distance title is not displayed"
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "0", "Screen time toggle is not off"
        assert self.fc.fd["wellbeing"].verify_alert_options_title_show_up(), "Alert options is not displayed"
        assert self.fc.fd["wellbeing"].verify_set_preferred_distance_icon_show_up(), "Set preferred distance icon is not displayed"

    @pytest.mark.ota
    @pytest.mark.function
    def test_03_check_turn_off_screen_time_toggle_verify_toggle_is_off_C44005835(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        # click on wellbeing card
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=14)
        time.sleep(2)
        # click restore default button
        self.fc.fd["wellbeing"].click_restore_default_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=14)
        time.sleep(2)
        # verify screen time UI
        assert self.fc.fd["wellbeing"].verify_screen_time_title_show_up(), "Screen time title is not displayed"
        # verify screen time default toggle is off
        assert self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "0", "Screen time toggle is not off"
        time.sleep(2)
        # verify screen time bar chart is displayed
        assert self.fc.fd["wellbeing"].verify_screen_time_bar_chart_show_up(), "Screen time bar chart is not displayed"
        # verify send a reminder default toggle is off
        assert self.fc.fd["wellbeing"].verify_send_a_reminder_toogle_status() == "0", "Send a reminder toggle is not off"
        time.sleep(2)
        # click screen time toggle
        self.fc.fd["wellbeing"].click_screen_time_toggle()
        time.sleep(2)
        # verify if camera dialog show
        if self.fc.fd["hpx_fuf"].verify_camera_yes_button_show():
            self.fc.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
        time.sleep(3) 
        # verify screen time toggle is on
        assert self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "1", "Screen time toggle is not on"
        time.sleep(2)
        # click send a reminder toggle
        self.fc.fd["wellbeing"].click_send_a_reminder_toggle()
        time.sleep(2)
        # verify send a reminder toggle is on
        assert self.fc.fd["wellbeing"].verify_send_a_reminder_toogle_status() == "1", "Send a reminder toggle is not on"
        time.sleep(2)
        # click screen time toggle
        self.fc.fd["wellbeing"].click_screen_time_toggle()
        time.sleep(2)
        # verify screen time toggle is off
        assert self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "0", "Screen time toggle is not off"
        time.sleep(2)   
        # verify send a reminder default toggle is off
        assert self.fc.fd["wellbeing"].verify_send_a_reminder_toogle_status() == "0", "Send a reminder toggle is not off"
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_04_check_screen_time_tooltips_C43876436(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        # click on wellbeing card
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        # verify screen time UI
        assert self.fc.fd["wellbeing"].verify_screen_time_title_show_up(), "Screen time title is not displayed"
        # click screen time tooltip
        self.fc.fd["wellbeing"].click_screen_time_tooltip()
        time.sleep(2)
        # verify screen time tooltip is displayed
        assert self.fc.fd["wellbeing"].get_screen_time_tooltip() =="This feature only works when your built-in camera is facing you. This feature does not support external monitors. If Screen Time is turned off, daily data will not be collected.", "Screen time tooltip is not displayed"
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        # click send a reminder tooltip
        self.fc.fd["wellbeing"].click_send_a_reminder_tooltip()
        time.sleep(2)
        # verify send a reminder tooltip is displayed
        assert self.fc.fd["wellbeing"].get_send_a_reminder_tooltip() =="Time intervals are measured by how much time is spent in front of the display.", "Send a reminder tooltip is not displayed"
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_05_check_screen_distance_tooltips_C43876481(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        # click on wellbeing card
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=13)
        # verify screen distance UI
        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen Distance title is not displayed"
        time.sleep(2)
        # click alert options tooltip
        self.fc.fd["wellbeing"].click_alert_options_tooltip()
        time.sleep(2)
        # verify alert options tooltip is displayed
        assert self.fc.fd["wellbeing"].get_alert_options_tooltip() =="Nudge: Receive a minor notification. Alert: More options to snooze or dismiss are included." , "Alert options tooltip is not displayed"
        time.sleep(2)

    @pytest.mark.ota
    @pytest.mark.function
    def test_06_check_screen_distance_will_be_restore_C43876482(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        # click on wellbeing card
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=13)
        # verify screen distance UI
        assert self.fc.fd["wellbeing"].verify_screen_distance_title_show_up(), "Screen Distance title is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["wellbeing"].click_restore_default_button()
        time.sleep(5)
        # click screen distance toggle
        self.fc.fd["wellbeing"].click_screen_distance_toggle()
        time.sleep(2)
        # verify if camera dialog show
        if self.fc.fd["hpx_fuf"].verify_camera_yes_button_show():
            self.fc.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
        time.sleep(3)
        # verify screen distance toggle is on
        assert self.fc.fd["wellbeing"].verify_screen_distance_toogle_status() == "1", "Screen distance toggle is not on"
        time.sleep(2)
        # verify alert option title is displayed
        assert self.fc.fd["wellbeing"].verify_alert_options_title_show_up(), "Alert options is not displayed"
        time.sleep(2)
        # verify defaut alert options drop down list is nudge
        assert self.fc.fd["wellbeing"].get_alert_options() == "Nudge", "Alert options is not nudge"
        time.sleep(2)
        # click alert options drop down list
        self.fc.fd["wellbeing"].click_alert_options()
        time.sleep(2)
        # verify alert options show drop down list 
        assert self.fc.fd["wellbeing"].verify_alert_options_show_on_drop_down_list(), "Alert options drop down list is not displayed"
        time.sleep(2)
        # select alert options in drop down list
        self.fc.fd["wellbeing"].select_alert_options()
        time.sleep(2)
        # verify alert options is selected
        assert self.fc.fd["wellbeing"].get_alert_options() == "Alert", "Alert options is not alert"
        time.sleep(2)
        # verify perferrred distance title is displayed
        assert self.fc.fd["wellbeing"].verify_set_preferred_distance_title_show_up(), "Preferred distance title is not displayed"
        time.sleep(2)
        # verify perferred distance toggle is displayed
        assert self.fc.fd["wellbeing"].verify_set_preferred_distance_toggle_show_up(), "Set preferred distance icon is not displayed"
        time.sleep(2)
        # click  perferred distance toggele
        self.fc.fd["wellbeing"].click_set_preferred_distance_toggle()
        time.sleep(2)
        # verify current set disance dialog show
        assert self.fc.fd["wellbeing"].verify_current_set_distance_image_show_up(), "Current set distance dialog is not displayed"
        time.sleep(2)
        # verify set button show
        assert self.fc.fd["wellbeing"].verify_set_button_show_up(), "Set button is not displayed"
        time.sleep(2)
        # click set button
        self.fc.fd["wellbeing"].click_set_button()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        # verify restore default button show
        assert self.fc.fd["wellbeing"].verify_restore_default_button_show_up(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["wellbeing"].click_restore_default_button()
        time.sleep(5)
        # verify defaut alert options drop down list is nudge
        assert self.fc.fd["wellbeing"].get_alert_options() == "Nudge", "Alert options is not nudge"
        time.sleep(2)


    @pytest.mark.ota
    @pytest.mark.function
    def test_07_click_reminder_interval_ccombobox_verify_all_time_can_select_C43876440(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        # click on wellbeing card
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(3)
        self.fc.fd["wellbeing"].click_screen_time_title()
        time.sleep(2)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=12)
        time.sleep(2)
        # verify restore default button is displayed
        assert self.fc.fd["wellbeing"].verify_restore_default_button_show_up(), "Restore default button is not displayed"
        time.sleep(2)
        # click restore default button
        self.fc.fd["wellbeing"].click_restore_default_button()
        time.sleep(3)
        self.fc.swipe_window(direction="up", distance=12)
        time.sleep(2)
        # verify screen time UI
        assert self.fc.fd["wellbeing"].verify_screen_time_title_show_up(), "Screen time title is not displayed"
        time.sleep(1)
        # verify screen time default toggle is off
        assert self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "0", "Screen time toggle is not off"
        time.sleep(1)
        # verify screen time bar chart is displayed
        assert self.fc.fd["wellbeing"].verify_screen_time_bar_chart_show_up(), "Screen time bar chart is not displayed"
        time.sleep(1)
        # verify send a reminder default toggle is off
        assert self.fc.fd["wellbeing"].verify_send_a_reminder_toogle_status() == "0", "Send a reminder toggle is not off"
        time.sleep(1)
        # click screen time toggle
        self.fc.fd["wellbeing"].click_screen_time_toggle()
        time.sleep(2)
        # verify if camera dialog show
        if self.fc.fd["hpx_fuf"].verify_camera_yes_button_show():
            self.fc.fd["hpx_fuf"].click_camera_yes_button_on_let_myhp_access_dialog()
        time.sleep(2)
        # verify screen time toggle is on
        assert self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "1", "Screen time toggle is not on"
        time.sleep(2)
        # click send a reminder toggle
        self.fc.fd["wellbeing"].click_send_a_reminder_toggle()
        time.sleep(2)
        # verify send a reminder toggle is on
        assert self.fc.fd["wellbeing"].verify_send_a_reminder_toogle_status() == "1", "Send a reminder toggle is not on"
        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=12)
        time.sleep(2)
        # click reminder interval drop down list
        self.fc.fd["wellbeing"].click_reminder_interval()
        time.sleep(2)
        # verify 1 hour show on reminder interval drop down list
        assert self.fc.fd["wellbeing"].verify_reminder_interval_1_hour_show_up(), "1 hour is not displayed"
        time.sleep(2)
        # select 1 hour on reminder interval drop down list
        self.fc.fd["wellbeing"].click_reminder_interval_1_hour()
        time.sleep(2)
        # verify default reminder interval is 1 hour
        assert self.fc.fd["wellbeing"].get_reminder_interval() == "1 hour", "Reminder interval is not 1 hour"
        time.sleep(2)
        # click reminder interval drop down list
        self.fc.fd["wellbeing"].click_reminder_interval()
        time.sleep(2)
        # verify 2 hours show on reminder interval drop down list
        assert self.fc.fd["wellbeing"].verify_reminder_interval_2_hour_show_up(), "2 hours is not displayed"
        time.sleep(2)
        # select 2 hours on reminder interval drop down list
        self.fc.fd["wellbeing"].click_reminder_interval_2_hour()
        time.sleep(2)
        # verify default reminder interval is 2 hours
        assert self.fc.fd["wellbeing"].get_reminder_interval() == "2 hours", "Reminder interval is not 2 hours"
        time.sleep(2)
        # click reminder interval drop down list
        self.fc.fd["wellbeing"].click_reminder_interval()
        time.sleep(2)
        # verify 4 hours show on reminder interval drop down list
        assert self.fc.fd["wellbeing"].verify_reminder_interval_4_hour_show_up(), "4 hours is not displayed"
        time.sleep(2)
        # select 4 hours on reminder interval drop down list
        self.fc.fd["wellbeing"].click_reminder_interval_4_hour()
        time.sleep(2)
        # verify default reminder interval is 4 hours
        assert self.fc.fd["wellbeing"].get_reminder_interval() == "4 hours", "Reminder interval is not 4 hours"
        time.sleep(2)
        # click reminder interval drop down list
        self.fc.fd["wellbeing"].click_reminder_interval()
        time.sleep(2)
        # verify 30 mins show on reminder interval drop down list
        assert self.fc.fd["wellbeing"].verify_reminder_interval_30_mins_show_up(), "30 mins is not displayed"
        time.sleep(2)
        # select 30 mins on reminder interval drop down list
        self.fc.fd["wellbeing"].click_reminder_interval_30_mins()
        time.sleep(2)
        # verify default reminder interval is 30 mins
        assert self.fc.fd["wellbeing"].get_reminder_interval() == "30 minutes", "Reminder interval is not 30 mins"
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=12)
        time.sleep(2)
        # turn off screen time toggle
        self.fc.fd["wellbeing"].click_screen_time_toggle()
        time.sleep(2)
        # verify screen time toggle is off
        assert self.fc.fd["wellbeing"].verify_screen_time_toggle_status() == "0", "Screen time toggle is not off"
        time.sleep(2)
        # verify send a reminder default toggle is off
        assert self.fc.fd["wellbeing"].verify_send_a_reminder_toogle_status() == "0", "Send a reminder toggle is not off"
        time.sleep(2)
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_08_navigate_to_each_button_use_tab_C51909700(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        time.sleep(1)
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)

        self.fc.fd["wellbeing"].press_tab("screen_time_toggle")
        time.sleep(2)
        assert self.fc.fd["wellbeing"].is_focus_on_element("screen_time_toggle"), "Screen time title is not focused"
        time.sleep(2)
        self.fc.fd["wellbeing"].press_tab("send_a_reminder_toggle")
        time.sleep(2)
        assert self.fc.fd["wellbeing"].is_focus_on_element("send_a_reminder_toggle"), "Send a reminder toggle is not focused"
        time.sleep(2)
        self.fc.fd["wellbeing"].press_tab("screen_distance_toggle")
        time.sleep(2)
        assert self.fc.fd["wellbeing"].is_focus_on_element("screen_distance_toggle"), "Screen distance title is not focused"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_09_press_alt_f4_from_keyboard_C51909709(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].swipe_to_wellbeing_card()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_wellbeing_card_lone_page_show(), "Wellbeing card not found"

        self.fc.fd["wellbeing"].press_alt_f4_to_close_app()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_wellbeing_card_lone_page_show() is False, "Wellbeing card is displayed after alt+f4" 
