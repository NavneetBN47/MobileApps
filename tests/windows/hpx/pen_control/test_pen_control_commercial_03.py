from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Pen_Control_Commercial(object):
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
            cls.fc.close_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_01_different_actions_in_the_actions_list_C38313866(self):
        self.fc.reset_myhp_app()
        time.sleep(5)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        #verify pen control show in navigation bar in commercial
        assert bool(self.fc.fd["pen_control"].verify_pen_control_show_in_navigation_bar_commercial()) is True, "Pen control module is not show navigation bar"
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # verify single press text show
        assert self.fc.fd["pen_control"].get_single_press_text_commercial() == "Single press", "Single press text Mismatch"
        time.sleep(1)
        # verify single press text along with the default action is "MS whiteboard"
        assert self.fc.fd["pen_control"].get_single_press_text_along_with_default_action_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # click single press button
        self.fc.fd["pen_control"].click_single_press_button_commercial()
        time.sleep(1)
        # verify top button single press text in configure key list show   
        assert self.fc.fd["pen_control"].get_top_button_single_press_text_in_configure_key_list_show_commercial() == "Top button - Single press", "Top button - Single press text Mismatch"
        time.sleep(1)
        # verify ms white board text in configure key list show
        assert self.fc.fd["pen_control"].get_ms_white_board_text_in_configure_key_list_show_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # verify ms white board toggle is select
        assert self.fc.fd["pen_control"].get_ms_white_board_toggle_is_select_commercial() == "1", "MS whiteboard toggle is not selected"
        time.sleep(1)
        # verify pen menu text in configure key list show
        assert self.fc.fd["pen_control"].get_pen_menu_text_in_configure_key_list_show_commercial() == "Pen menu", "Pen menu text Mismatch"
        time.sleep(1)
        # click pen menu toggle
        self.fc.fd["pen_control"].click_pen_menu_toggle_commercial()
        time.sleep(1)
        # verify pen menu toggle is select
        assert self.fc.fd["pen_control"].get_pen_menu_toggle_is_select_commercial() == "Pen menu", "Pen menu text Mismatch"
        # click single press button to make configure list disappear
        self.fc.fd["pen_control"].click_single_press_button_commercial()
        time.sleep(1)
        # verify default single press button now is "Pen menu"
        assert self.fc.fd["pen_control"].get_ms_whiteboard_commercial() == "Pen menu", "Pen menu text Mismatch"
        time.sleep(1)
        # verify double press text show
        assert self.fc.fd["pen_control"].get_double_press_text_commercial() == "Double press", "Double press text Mismatch"
        time.sleep(1)
        # verify double press text along with the default action is "Screen snipping"
        assert self.fc.fd["pen_control"].get_double_press_text_along_with_default_action_commercial() == "Screen snipping", "Screen snipping text Mismatch"
        time.sleep(1)
         # click double press button
        self.fc.fd["pen_control"].click_double_press_button_commercial()
        time.sleep(1)
        # verify top button double press text in configure key list show
        assert self.fc.fd["pen_control"].get_top_button_double_press_text_in_configure_key_list_show_commercial() == "Top button - Double press", "Top button - Double press text Mismatch"
        time.sleep(1)
        # verify screen snipping text in configure key list show
        assert self.fc.fd["pen_control"].get_screen_snipping_text_in_configure_key_list_show_commercial() == "Screen snipping", "Screen snipping text Mismatch"
        time.sleep(1)
        # verify screen snipping toggle is select
        assert self.fc.fd["pen_control"].get_screen_snipping_toggle_is_select_commercial() == "1", "Screen snipping toggle is not selected"
        time.sleep(1)
        # verify Disabled text in configure key list show
        assert self.fc.fd["pen_control"].get_disabled_text_in_configure_key_list_show_commercial() == "Disabled", "Disabled text is not shown"
        time.sleep(1)
        # click Disabled toggle
        self.fc.fd["pen_control"].click_disabled_toggle_commercial()
        time.sleep(1)
        # verify Disabled toggle is select
        assert self.fc.fd["pen_control"].get_disabled_toggle_is_select_commercial() == "1","Disabled toggle is not selected"
        time.sleep(1)
        # click double press button to make configure list disappear
        self.fc.fd["pen_control"].click_double_press_button_commercial()
        time.sleep(2)
        # verify double press button now is "Disabled"
        assert self.fc.fd["pen_control"].get_screen_snipping_commercial() == "Disabled", "Disabled text Mismatch"
        time.sleep(1)
        # verify long press text show
        assert self.fc.fd["pen_control"].get_long_press_text_commercial() == "Long press", "Long press text Mismatch"
        time.sleep(1)
        # verify long press text along with the default action is "Sticky notes"
        assert self.fc.fd["pen_control"].get_long_press_text_along_with_default_action_commercial() == "Sticky notes", "Sticky notes text Mismatch"
        time.sleep(1)
        # click long press button
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        time.sleep(1)
        # verify top button long press text in configure key list show
        assert self.fc.fd["pen_control"].get_top_button_long_press_text_in_configure_key_list_show_commercial() == "Top button - Long press", "Top button - Double press text Mismatch"
        time.sleep(1)
        # verify sticky notes text in configure key list show
        assert self.fc.fd["pen_control"].get_sticky_notes_text_in_configure_key_list_show_commercial() == "Sticky notes", "Sticky notes text Mismatch"
        time.sleep(1)
        # verify sticky notes toggle is select
        assert self.fc.fd["pen_control"].verify_sticky_notes_toggle_commer() == "1", "Sticky notes toggle is not selected"
        time.sleep(1)
        # verify Windows search text in configure key list show
        assert self.fc.fd["pen_control"].get_windows_search_text_in_configure_key_list_show_commercial() == "Windows search", "Windows search text Mismatch"
        time.sleep(1)
        # click Windows search toggle
        self.fc.fd["pen_control"].click_windows_search_toggle_commercial()
        time.sleep(1)
        # verify Windows search toggle is select
        assert self.fc.fd["pen_control"].get_windows_search_toggle_is_select_commercial() == "1", "Windows search toggle is not selected"
        time.sleep(1)
        # click long press button to make configure list disappear
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        time.sleep(1)
        # verify long press button now is "Windows search"
        assert self.fc.fd["pen_control"].get_sticky_notes_commercial() == "Windows search", "Windows search text Mismatch"
        time.sleep(1)
        # verify upper_barrel_image_button show
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        time.sleep(1)
        # verify default upper_barrel_image_button is Universal select
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)
        # click upper_barrel_button
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        time.sleep(1)
        # verify upper_barrel_button text show
        assert self.fc.fd["pen_control"].verify_upper_barrel_button_text_show_commercial() == "Upper barrel button", "Upper barrel button text Mismatch"
        time.sleep(1)
        # verify universal select toggle text show
        assert self.fc.fd["pen_control"].get_universal_select_toggle_text_show_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)
        # verify left click text show
        assert self.fc.fd["pen_control"].get_left_click_toggle_text_show_commercial() == "Left click", "Left click text Mismatch"
        time.sleep(1)
        # click left click toggle
        self.fc.fd["pen_control"].click_left_click_toggle_commercial()
        time.sleep(1)
        # verify left click toggle is select
        assert self.fc.fd["pen_control"].get_left_click_toggle_is_select_commercial() == "1", "Left click toggle is not selected"
        time.sleep(1)
        # click upper_barrel_button to make configure list disappear
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        time.sleep(1)
        # verify default upper_barrel_image_button is left click
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Left click", "Left click text Mismatch"
        time.sleep(1)
        # verify lower_barrel_image_button show
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        time.sleep(1)
        #verify default lower_barrel_image_button is right click
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Erase text Mismatch"
        time.sleep(1)
        # click lower_barrel_button
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
        # verify lower_barrel_button text show
        assert self.fc.fd["pen_control"].verify_lower_barrel_button_text_show_commercial() == "Lower barrel button", "Lower barrel button text Mismatch"
        time.sleep(1)
        # verify erase toggle text show
        assert self.fc.fd["pen_control"].get_erase_toggle_text_show_commercial() == "Erase", "Erase text Mismatch"
        time.sleep(1)
        # verify erase toggle is select
        assert self.fc.fd["pen_control"].get_erase_toggle_is_select_commercial() == "1", "Erase toggle is not selected"
        time.sleep(1)
        # verify middle click toggle text show
        assert self.fc.fd["pen_control"].get_middle_click_toggle_text_show_commercial() == "Middle click", "Middle click text Mismatch"
        time.sleep(1)
        # click middle click toggle
        self.fc.fd["pen_control"].click_middle_click_toggle_commercial()
        time.sleep(1)
        # verify middle click toggle is select
        assert self.fc.fd["pen_control"].get_middle_click_is_select_commercial() == "1", "Middle click toggle is not selected"
        time.sleep(1)
        # click lower_barrel_button to make configure list disappear
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
        # verify default lower_barrel__image_button is middle click
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Middle click", "Middle click text Mismatch"
        time.sleep(1)

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_02_same_actions_in_the_actions_list_C38313883(self):
        self.fc.reset_myhp_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        #verify pen control show in navigation bar in commercial
        assert bool(self.fc.fd["pen_control"].verify_pen_control_show_in_navigation_bar_commercial()) is True, "Pen control module is not show navigation bar"
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # verify single press text show
        assert self.fc.fd["pen_control"].get_single_press_text_commercial() == "Single press", "Single press text Mismatch"
        time.sleep(1)
        # verify single press text along with the default action is "MS whiteboard"
        assert self.fc.fd["pen_control"].get_single_press_text_along_with_default_action_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # click single press button
        self.fc.fd["pen_control"].click_single_press_button_commercial()
        time.sleep(1)
        # verify top button single press text in configure key list show   
        assert self.fc.fd["pen_control"].get_top_button_single_press_text_in_configure_key_list_show_commercial() == "Top button - Single press", "Top button - Single press text Mismatch"
        time.sleep(1)
        # verify ms white board text in configure key list show
        assert self.fc.fd["pen_control"].get_ms_white_board_text_in_configure_key_list_show_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # verify ms white board toggle is select
        assert self.fc.fd["pen_control"].get_ms_white_board_toggle_is_select_commercial() == "1", "MS whiteboard toggle is not selected"
        time.sleep(1)
        # verify double press text show
        assert self.fc.fd["pen_control"].get_double_press_text_commercial() == "Double press", "Double press text Mismatch"
        time.sleep(1)
        # verify double press text along with the default action is "Screen snipping"
        assert self.fc.fd["pen_control"].get_double_press_text_along_with_default_action_commercial() == "Screen snipping", "Screen snipping text Mismatch"
        time.sleep(1)
         # click double press button
        self.fc.fd["pen_control"].click_double_press_button_commercial()
        time.sleep(1)
        # verify top button double press text in configure key list show
        assert self.fc.fd["pen_control"].get_top_button_double_press_text_in_configure_key_list_show_commercial() == "Top button - Double press", "Top button - Single press text Mismatch"
        time.sleep(1)
        # verify screen snipping text in configure key list show
        assert self.fc.fd["pen_control"].get_screen_snipping_text_in_configure_key_list_show_commercial() == "Screen snipping", "Screen snipping text Mismatch"
        time.sleep(1)
        # verify screen snipping toggle is select
        assert self.fc.fd["pen_control"].get_screen_snipping_toggle_is_select_commercial() == "1", "Screen snipping toggle is not selected"
        time.sleep(1)
        # verify ms white board text in configure key list show
        assert self.fc.fd["pen_control"].get_ms_white_board_text_in_configure_key_list_show_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # click ms white board toggle
        self.fc.fd["pen_control"].click_ms_white_board_toggle_commercial()
        time.sleep(1)
        # verify ms white board toggle is select
        assert self.fc.fd["pen_control"].get_ms_white_board_toggle_is_select_commercial() == "1", "MS whiteboard toggle is not selected"
        time.sleep(1)
        # click double press button to make configure list disappear
        self.fc.fd["pen_control"].click_double_press_button_commercial()
        time.sleep(1)
        # verify double press button now is "MS whiteboard"
        assert self.fc.fd["pen_control"].get_double_press_button_now_is_ms_whiteboard_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # verify long press text show
        assert self.fc.fd["pen_control"].get_long_press_text_commercial() == "Long press", "Long press text Mismatch"
        time.sleep(1)
        # verify long press text along with the default action is "Sticky notes"
        assert self.fc.fd["pen_control"].get_long_press_text_along_with_default_action_commercial() == "Sticky notes", "Sticky notes text Mismatch"
        time.sleep(1)
        # click long press button
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        time.sleep(1)
        # verify top button long press text in configure key list show
        assert self.fc.fd["pen_control"].get_top_button_long_press_text_in_configure_key_list_show_commercial() == "Top button - Long press", "Top button - Single press text Mismatch"
        time.sleep(1)
        # verify sticky notes text in configure key list show
        assert self.fc.fd["pen_control"].get_sticky_notes_text_in_configure_key_list_show_commercial() == "Sticky notes", "Sticky notes text Mismatch"
        time.sleep(1)
        # verify sticky notes toggle is select
        assert self.fc.fd["pen_control"].verify_sticky_notes_toggle_commer() == "1", "Sticky notes toggle is not selected"
        time.sleep(1)
        # verify ms white board text in configure key list show
        assert self.fc.fd["pen_control"].get_ms_white_board_text_in_configure_key_list_show_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # click ms white board toggle
        self.fc.fd["pen_control"].click_ms_white_board_toggle_commercial()
        time.sleep(1)
        # verify ms white board toggle is select
        assert self.fc.fd["pen_control"].get_ms_white_board_toggle_is_select_commercial() == "1", "MS whiteboard toggle is not selected"
        time.sleep(1)
        # click long press button to make configure list disappear
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        time.sleep(1)
        # verify long press button now is "MS whiteboard"
        assert self.fc.fd["pen_control"].get_long_press_button_now_is_ms_whiteboard_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # verify upper_barrel_image_button show
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        time.sleep(1)
        # verify default upper_barrel_image_button is Universal select
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)
        # click upper_barrel_button
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        time.sleep(1)
        # verify upper_barrel_button text show
        assert self.fc.fd["pen_control"].verify_upper_barrel_button_text_show_commercial() == "Upper barrel button", "Upper barrel button text Mismatch"
        time.sleep(1)
        # verify universal select toggle text show
        assert self.fc.fd["pen_control"].get_universal_select_toggle_text_show_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)
        # verify ms white board text in configure key list show
        assert self.fc.fd["pen_control"].get_ms_white_board_text_in_configure_key_list_show_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # click ms white board toggle
        self.fc.fd["pen_control"].click_ms_white_board_toggle_commercial()
        time.sleep(1)
        # verify ms white board toggle is select
        assert self.fc.fd["pen_control"].get_ms_white_board_toggle_is_select_commercial() == "1", "MS whiteboard toggle is not selected"
        time.sleep(1)
        # click upper_barrel_button to make configure list disappear
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        time.sleep(1)
        # verify default upper_barrel_image_button is "MS whiteboard"
        assert self.fc.fd["pen_control"].get_upper_barrel_button_now_is_ms_whiteboard_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # verify lower_barrel_image_button show
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        time.sleep(1)
        #verify default lower_barrel_image_button is right click
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Erase text Mismatch"
        time.sleep(1)
        # click lower_barrel_button
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
        # verify lower_barrel_button text show
        assert self.fc.fd["pen_control"].verify_lower_barrel_button_text_show_commercial() == "Lower barrel button", "Lower barrel button text Mismatch"
        time.sleep(1)
        # verify erase toggle text show
        assert self.fc.fd["pen_control"].get_erase_toggle_text_show_commercial() == "Erase", "Erase text Mismatch"
        time.sleep(1)
        # verify erase toggle is select
        assert self.fc.fd["pen_control"].get_erase_toggle_is_select_commercial() == "1", "Erase toggle is not selected"
        time.sleep(1)
        ## verify ms white board text in configure key list show
        assert self.fc.fd["pen_control"].get_ms_white_board_text_in_configure_key_list_show_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)
        # click ms white board toggle
        self.fc.fd["pen_control"].click_ms_white_board_toggle_commercial()
        time.sleep(1)
        # verify ms white board toggle is select
        assert self.fc.fd["pen_control"].get_ms_white_board_toggle_is_select_commercial() == "1", "MS whiteboard toggle is not selected"
        time.sleep(1)
        # click lower_barrel_button to make configure list disappear
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
        # verify default lower_barrel__image_button is "MS whiteboard"
        assert self.fc.fd["pen_control"].get_lower_barrel_button_now_is_ms_whiteboard_commercial() == "MS whiteboard", "MS whiteboard text Mismatch"
        time.sleep(1)

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_copy_information_C38145228(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(2)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() 
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].verify_info_icon()
        time.sleep(2)
        self.fc.fd["pen_control"].click_info_icon()
        time.sleep(2)
        assert bool(self.fc.fd["pen_control"].verify_presenceof_productnumber_tooltip()) is True, "Product number tooltip is not shown"
        self.fc.fd["pen_control"].click_productnumber_value_tooltip()
        assert self.fc.fd["pen_control"].get_productnumber_value_tooltip_text() == "Copied", "Copied text Mismatch"
        time.sleep(1)
        self.fc.fd["pen_control"].verify_presenceof_serialnumber_tooltip()
        self.fc.fd["pen_control"].click_serialnumber_value_tooltip()
        assert self.fc.fd["pen_control"].get_serialnumber_value_tooltip_text() == "Copied", "Copied text Mismatch"
        time.sleep(1)
        self.fc.fd["pen_control"].verify_presenceof_firmware_tooltip()
        self.fc.fd["pen_control"].click_firmware_version_copy_icon()
        assert self.fc.fd["pen_control"].get_firmwareversion_value_tooltip_text() == "Copied", "Copied text Mismatch"

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_04_action_list_ui_C38238679(self):
        self.fc.reset_myhp_app()        
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial()
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_lower_barrel_btn(),"Lower barrel button","Lower barrel title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_title(), "Pen", "Pen title is not visible")
        self.fc.fd["pen_control"].click_pen_dd()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_apps(), "Apps", "Apps title is not visible")
        self.fc.fd["pen_control"].click_apps_dropdown()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_media_control(), "Media control", "Media control title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_productivity(), "Productivity", "Productivity title is not visible")
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_upper_barrel_btn_right_click(), "Upper barrel button", "upper barrel title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_productivity(), "Productivity", "Productivity title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_title(), "Pen", "Pen title is not visible")
        self.fc.fd["pen_control"].click_pen_dd()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_apps(), "Apps", "Apps title is not visible")
        self.fc.fd["pen_control"].click_apps_dropdown()
        time.sleep(3)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_media_control(), "Media control", "Media control title is not visible")
        soft_assertion.raise_assertion_errors()

    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_action_list_ui_C37819057(self):
        self.fc.reset_myhp_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        #verify pen control show in navigation bar in commercial
        assert bool(self.fc.fd["pen_control"].verify_pen_control_show_in_navigation_bar_commercial()) is True, "Pen control module is not show navigation bar"
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # verify pen control default name on left side is "Pen"
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_left_side_commercial() == "Pen", "Default pen name text Mismatch"
        time.sleep(1)
        # verify pen control default name on right side is "HP Rechargeable Active Pen G3“
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_right_side_commercial() == "HP Rechargeable Active Pen G3", "Default pen name text Mismatch"
        time.sleep(1)
        # verify pen eidt icon show
        assert bool(self.fc.fd["pen_control"].verify_pen_edit_icon_show_commercial()) is True, "Pen control edit button is not show"
        time.sleep(1)
        # hover on pen name commercial to show tooltips
        self.fc.fd["pen_control"].hover_on_pen_name_commercial()
        time.sleep(1)
        # get pen name tooltip
        assert self.fc.fd["pen_control"].get_pen_name_tooltip_commercial() == "HP Rechargeable Active Pen G3", "Pen name of tooltip text Mismatch"
        time.sleep(1)
        # verify bluetooth icon show
        assert bool(self.fc.fd["pen_control"].verify_bluetooth_icon_show_commercial()) is True, "Pen control bluetooth button is not show"
        time.sleep(1)
        # verify tips icon show
        assert bool(self.fc.fd["pen_control"].verify_info_icon_show_commercial()) is True, "Pen control info button is not show"
        time.sleep(1)

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_06_restore_button_default_settings_C38313889(self):
        time.sleep(5)
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(7)
        self.fc.fd["pen_control"].click_single_press_button_commercial()
        soft_assertion = SoftAssert()
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_ms_white_board_radio_button_is_selected()), "ms white board checkbox is not selected")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_ms_white_board_name_commercial(), "MS whiteboard", "ms white board name is not matching with default action")

        self.fc.fd["pen_control"].click_double_press_button_commercial()
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_screen_snipping_radio_button_is_selected()), "screen snipping radio button is not selected")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_screen_snipping_text_in_configure_key_list_show_commercial(), "Screen snipping", "screen snipping name is not matching with default action")

        self.fc.fd["pen_control"].click_long_press_button_commercial()
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].get_sticky_notes_text_in_configure_key_list_show_commercial()), "sticky notes radio button is not selected")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_sticky_notes_toggle_is_select_commercial(), "Sticky notes", "sticky notes name is not matching with default action")

        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(2)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_lower_barrel_erase_radio_button_consumer_is_selected(), "1", "erase radio button is not selected")
        print(self.fc.fd["pen_control"].verify_lower_barrel_erase_radio_button_consumer_is_selected())
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_erase_toggle_text_show_commercial(), "Erase", "Erase default value is not selected")
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_universal_select_toggle_text_show_commercial(),"Universal Select", "Universal Select default value is not visible")
        soft_assertion.assert_contains(self.fc.fd["pen_control"].get_pen_name_tooltips(), "HP Rechargeable", "Pen name tooltip is not matching with default value")      
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_side_menu_navigation_pen_name(), "Pen", "Default pen name is not visible in side menu")
        soft_assertion.raise_assertion_errors()

    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_pen_sensitivity_menu_visible_C38313884(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial(), "Pen sensitivity", "Pen sensitivity title is not visible")

    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_restore_default_button_hide_show_C38313888(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(2)
        pen_lower_barrel_text = self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial()
        pen_upper_barrel_text = self.fc.fd["pen_control"].get_right_click_consumer_btn_pen()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(pen_lower_barrel_text, "Erase", "Lower barrel button default setting is not visible")
        soft_assertion.assert_equal(pen_upper_barrel_text, "Universal Select", "Upper barrel button default setting is not visible")
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        if self.fc.fd["pen_control"].get_lower_barrel_btn() == "Lower barrel button":
            soft_assertion.assert_false(bool(self.fc.fd["pen_control"].verify_restore_defaults_btn()), "Restore defaults button should not show")
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        soft_assertion.assert_false(bool(self.fc.fd["pen_control"].verify_action_list_not_show_commercial()), "Action list is not show")
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_restore_defaults_btn()), "Restore defaults button is not show")
        soft_assertion.raise_assertion_errors()

    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_09_upper_lower_barrel_hover_click_tooltip_desc_C38313890(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        actual_tooltip_desc = "Enable assigned button action while hovering pen tip over screen."
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        self.fc.fd["pen_control"].click_lower_barrel_tooltip()
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_lower_barrel_tool_tip(),actual_tooltip_desc,"Lower barrel tooltip description is not visible")
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        self.fc.fd["pen_control"].click_upper_barrel_tool_tip()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_upper_barrel_tool_tip(),actual_tooltip_desc,"Lower barrel tooltip description is not visible")
        soft_assertion.raise_assertion_errors()

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_10_tilt_sensitivity_slider_C38313887(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        time.sleep(5)
        self.fc.fd["pen_control"].click_pen_sensitivity_commercial()
        time.sleep(3)
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_sensitivity_title_commercial(), "Pen sensitivity", "Pen sensitivity title is not visible")
        soft_assertion.assert_true(self.fc.fd["pen_control"].verify_pen_sensivity_slider_visible(), "Pen sensitivity slider is not visible")       
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tilt_sensitivity_slider"), "1", "Pen sensitivity slider value is not correct")
        self.fc.fd["pen_control"].set_slider_value_increase(1,"tilt_sensitivity_slider")
        print(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tilt_sensitivity_slider"))
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tilt_sensitivity_slider"), "2", "Pen sensitivity max slider value is not correct")
        self.fc.fd["pen_control"].set_slider_value_decrease(2,"tilt_sensitivity_slider")
        print(self.fc.fd["pen_control"].set_slider_value_decrease(2,"tilt_sensitivity_slider"))
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_tilt_tip_slider_value("tilt_sensitivity_slider"), "0", "Pen sensitivity min slider value is not correct")
        soft_assertion.raise_assertion_errors()
