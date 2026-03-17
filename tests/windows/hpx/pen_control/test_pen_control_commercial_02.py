from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Pen_Control_Commercial(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
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
            time.sleep(2)
            cls.fc.launch_myHP()
            cls.fc.close_myHP()
        time.sleep(5)
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_pen_controls_ui_C35877533(self):
        self.fc.reset_myhp_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        #verify pen control show in navigation bar in commercial
        assert bool(self.fc.fd["pen_control"].verify_pen_control_show_in_navigation_bar_commercial()) is True, "Pen control is not show navigation bar"
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # verify pen control default ui
        # verify pen control default name on right side is "HP Rechargeable Active Pen G3"
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_right_side_commercial() == "HP Rechargeable Active Pen G3", "Default pen name text Mismatch"
        time.sleep(1)
        # verify pen edit icon show
        assert bool(self.fc.fd["pen_control"].verify_pen_edit_icon_show_commercial()) is True, "Pen control edit button is not show"
        time.sleep(1)
        # verify bluetooth icon show(no pen connected,so show disconnected state)
        assert bool(self.fc.fd["pen_control"].verify_bluetooth_icon_show_commercial()) is True, "Pen control bluetooth button is not show"
        time.sleep(1)
        # verify info icon show
        assert bool(self.fc.fd["pen_control"].verify_info_icon_show_commercial()) is True
        time.sleep(1)
        # verify single press text show
        assert self.fc.fd["pen_control"].get_single_press_text_commercial() == "Single press", "Single press text Mismatch"
        time.sleep(1)
        # verify single press text along with the default action is "MS whiteboard"
        assert self.fc.fd["pen_control"].get_single_press_text_along_with_default_action_commercial() == "MS whiteboard", "Single press text Mismatch"
        time.sleep(1)
        # verify double press text show
        assert self.fc.fd["pen_control"].get_double_press_text_commercial() == "Double press", "Single press text Mismatch"
        time.sleep(1)
        # verify double press text along with the default action is "Screen snipping"
        assert self.fc.fd["pen_control"].get_double_press_text_along_with_default_action_commercial() == "Screen snipping", "Screen snipping text Mismatch"
        time.sleep(1)
        # verify long press text show
        assert self.fc.fd["pen_control"].get_long_press_text_commercial() == "Long press", "Long press text Mismatch"
        time.sleep(1)
        # verify long press text along with the default action is "Sticky notes"
        assert self.fc.fd["pen_control"].get_long_press_text_along_with_default_action_commercial() == "Sticky notes", "Sticky notes text Mismatch"
        time.sleep(1)
        # verify upper_barrel__image_button show
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        time.sleep(1)
        # verify default upper_barrel__image_button is Universal select
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)
        # verify lower_barrel__image_button show
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        time.sleep(1)
        #verify default lower_barrel__image_button is Erase
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Erase text Mismatch"
        time.sleep(1)
        # verify pen sensitivity button show
        assert self.fc.fd["pen_control"].get_pen_sensitivity_commercial() == "Pen sensitivity", "Pen sensitivity text Mismatch"
        time.sleep(1)
        # verify restore defaults button show
        assert self.fc.fd["pen_control"].get_restore_defaults_button_show_commercial() == "Restore defaults", "Restore defaults text Mismatch"
        time.sleep(1)
        # verify top image button show
        assert self.fc.fd["pen_control"].get_top_image_button_show_commercial() == "Top Image", "Top Image text Mismatch"
        time.sleep(1)
        # verify pen sensitivity image button show---no such pen sensitive button
        assert self.fc.fd["pen_control"].get_pen_sensitivity_image_button_show_commercial() == "Pen Sensitivity Image", "Pen Sensitivity Image text Mismatch"
        #time.sleep(1)
    
    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_02_uninstall_and_reinstall_application_C38313942(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # verify lower_barrel_image_button show
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        time.sleep(1)
        #verify default lower_barrel__image_button is erase
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Erase Barrel Image text Mismatch"
        time.sleep(1)
        # click lower_barrel_button
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
        # verify lower_barrel_button text show
        assert self.fc.fd["pen_control"].verify_lower_barrel_button_text_show_commercial() == "Lower barrel button", "Lower Barrel button text Mismatch"
        time.sleep(1)
        # verify erase toggle text show
        assert self.fc.fd["pen_control"].get_erase_toggle_text_show_commercial() == "Erase", "Erase Barrel Image text Mismatch"
        time.sleep(1)
        # verify erase toggle is select
        assert self.fc.fd["pen_control"].get_erase_toggle_is_select_commercial() == "1", "Erase toggle is not selected"
        time.sleep(1)
        # verify middle click toggle text show
        assert self.fc.fd["pen_control"].get_middle_click_toggle_text_show_commercial() == "Middle click", "Middle click Image text Mismatch"
        time.sleep(1)
        # click middle click toggle
        self.fc.fd["pen_control"].click_middle_click_toggle_commercial()
        time.sleep(1)
        # verify middle click toggle is select
        assert self.fc.fd["pen_control"].get_middle_click_is_select_commercial() == "1", "Middle click is not selected"
        time.sleep(1)
        # click lower_barrel_button to make list disappear
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
        # verify default lower_barrel__image_button is middle click
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Middle click", "Middle click text Mismatch"
        time.sleep(1)
        # verify upper_barrel_button show
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        time.sleep(1)
        # verify default upper_barrel__image_button is Universal Select
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)
        # click upper_barrel_button
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        time.sleep(1)
        # verify upper_barrel_button text show
        assert self.fc.fd["pen_control"].verify_upper_barrel_button_text_show_commercial() == "Upper barrel button", "Upper Barrel button text Mismatch"
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
        # click upper_barrel_button to make list disappear
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        time.sleep(1)
        # verify default upper_barrel__image_button is left click
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Left click", "Left click text Mismatch"
        time.sleep(1)
        self.fc.reset_myhp_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # verify default lower_barrel__image_button is erase
        assert self.fc.fd["pen_control"].get_default_lower_barrel_button_commercial() == "Erase", "Earase text Mismatch"
        time.sleep(1)
        # verify default upper_barrel__image_button is Universal select
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)

    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_action_list_C38221486(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(10)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
		# verify single press button show
        assert self.fc.fd["pen_control"].get_single_press_button_show_commercial() == "Single press", "Single press text Mismatch"
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
        # verify restore default button not show when configure key list open
        assert bool(self.fc.fd["pen_control"].verify_restore_default_button_not_show_when_configure_key_list_show_commercial()) is False, "Restore button should not show when configure key list open"
        time.sleep(1)
        # verify pen control custom name show
        assert bool(self.fc.fd["pen_control"].get_pen_control_custom_name_show_commercial()) is True, "Pen control defaulr name is not show"
        time.sleep(1)
        # click pen control custom name
        self.fc.fd["pen_control"].click_pen_control_custom_name_commercial()
        time.sleep(1)
        # verify double press button show
        assert self.fc.fd["pen_control"].get_double_press_button_show_commercial() == "Double press", "Double press text Mismatch"
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
        assert self.fc.fd["pen_control"].get_screen_snipping_toggle_is_select_commercial() == "1"
        time.sleep(1)
        # verify restore default button not show when configure key list open
        assert bool(self.fc.fd["pen_control"].verify_restore_default_button_not_show_when_configure_key_list_show_commercial()) is False, "Restore button should not show when configure key list open"
        time.sleep(1)
        # verify pen control custom name show
        assert bool(self.fc.fd["pen_control"].get_pen_control_custom_name_show_commercial()) is True, "Pen control defaulr name is not show"
        time.sleep(1)
        # click pen control custom name
        self.fc.fd["pen_control"].click_pen_control_custom_name_commercial()
        time.sleep(1)
        # verify long press button show
        assert self.fc.fd["pen_control"].get_long_press_button_show_commercial() == "Long press", "Long press text Mismatch"
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
        # verify restore default button not show when configure key list open
        assert bool(self.fc.fd["pen_control"].verify_restore_default_button_not_show_when_configure_key_list_show_commercial()) is False, "Restore button should not show when configure key list open"
        time.sleep(1)
        # verify pen control custom name show
        assert bool(self.fc.fd["pen_control"].get_pen_control_custom_name_show_commercial()) is True, "Pen control defaulr name is not show"
        time.sleep(1)
        # click pen control custom name
        self.fc.fd["pen_control"].click_pen_control_custom_name_commercial()
        time.sleep(1)
        # verify Upper_Barrel_button show
        assert self.fc.fd["pen_control"].get_upper_barrel_image_button_show_commercial() == "Upper Barrel Image", "Upper Barrel Image text Mismatch"
        time.sleep(1)
        # verify default upper_barrel__image_button is Universal select
        assert self.fc.fd["pen_control"].get_default_upper_barrel_button_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)
        # click Upper_Barrel_button
        self.fc.fd["pen_control"].click_upper_barrel_image_button_commercial()
        time.sleep(1)
        # verify Upper_Barrel_button text show
        assert self.fc.fd["pen_control"].verify_upper_barrel_button_text_show_commercial() == "Upper barrel button", "Upper barrel button text Mismatch"
        time.sleep(1)
         # verify universal select toggle text show
        assert self.fc.fd["pen_control"].get_universal_select_toggle_text_show_commercial() == "Universal Select", "Universal Select text Mismatch"
        time.sleep(1)
        # verify universal select toggle is select
        assert self.fc.fd["pen_control"].get_universal_select_toggle_is_select_commercial() == "1", "Universal Select toggle is not selected"
        time.sleep(1)
        # verify restore default button not show when configure key list open
        assert bool(self.fc.fd["pen_control"].verify_restore_default_button_not_show_when_configure_key_list_show_commercial()) is False, "Restore button should not show when configure key list open"
        time.sleep(1)
        # verify pen control custom name show
        assert bool(self.fc.fd["pen_control"].get_pen_control_custom_name_show_commercial()) is True, "Pen control defaulr name is not show"
        time.sleep(1)
        # click pen control custom name
        self.fc.fd["pen_control"].click_pen_control_custom_name_commercial()
        time.sleep(1)
        # verify lower_barrel__image_button show
        assert self.fc.fd["pen_control"].get_lower_barrel_image_button_show_commercial() == "Lower Barrel Image", "Lower Barrel Image text Mismatch"
        time.sleep(1)
        # verify default lower_barrel__image_button is erase
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
        # verify restore default button not show when configure key list open
        assert bool(self.fc.fd["pen_control"].verify_restore_default_button_not_show_when_configure_key_list_show_commercial()) is False, "Restore button should not show when configure key list open"
        time.sleep(1)
        # click any button once in the UI when the action list is expanded, verify action list is closed
        # click lower_barrel_button to make list disappear
        self.fc.fd["pen_control"].click_lower_barrel_image_button_commercial()
        time.sleep(1)
        # then verify action list not show 
        assert bool(self.fc.fd["pen_control"].verify_action_list_not_show_commercial()) is False, "Action list should not show"
        time.sleep(1)
        # verify restore default button show when configure key list close
        assert bool(self.fc.fd["pen_control"].verify_restore_default_button_show_when_configure_key_list_close_commercial()) is True, "Restore button should not show when configure key list open"
        time.sleep(1)

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_04_pen_name_C38249883(self):
        # uninstall and reinstall the app
        self.fc.reset_myhp_app()
        time.sleep(5)
        # click maximize button
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
        # verify pen control default name on right side is "HP Rechargeable Active Pen G3"
        assert self.fc.fd["pen_control"].get_pen_control_default_name_on_right_side_commercial() == "HP Rechargeable Active Pen G3", "Default pen name text Mismatch"
        time.sleep(1)
        # verify pen eidt icon show
        assert bool(self.fc.fd["pen_control"].verify_pen_edit_icon_show_commercial()) is True, "Pen control edit button is not show"
        time.sleep(1)
        # click pen edit icon
        self.fc.fd["pen_control"].click_pen_edit_icon_commercial()
        time.sleep(1)
        # verify pen name edit box show
        assert bool(self.fc.fd["pen_control"].verify_pen_name_edit_box_show_commercial()) is True, "Pen control edit box is not show"
        time.sleep(1)
        # edit pen name with "HPXPen"
        self.fc.fd["pen_control"].enter_device_name("HPXPen")
        time.sleep(2)
        # verify pen name on right side is "HPXPen"
        assert self.fc.fd["pen_control"].get_pen_name_on_right_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        time.sleep(1)
        # verify pen name on left side is "HPXKeyboard"
        assert self.fc.fd["pen_control"].get_pen_name_on_left_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        time.sleep(1)
        assert bool(self.fc.fd["pen_control"].verify_pen_edit_icon_show_commercial()) is True, "Pen control edit button is not show"
        time.sleep(1)
        # click pen edit icon
        self.fc.fd["pen_control"].click_pen_edit_icon_commercial()
        time.sleep(1)
        # verify pen name edit box show
        assert bool(self.fc.fd["pen_control"].verify_pen_name_edit_box_show_commercial()) is True, "Pen control edit box is not show"
        time.sleep(1)
        # edit pen name with "HPXPen@@@"
        self.fc.fd["pen_control"].enter_device_name("HPXPen@@@"), "Pen name of changed text Mismatch"
        time.sleep(2)
        # verify pen name on right side is "HPXPen"
        assert self.fc.fd["pen_control"].get_pen_name_on_right_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        time.sleep(1)
        # verify pen name on left side is "HPXPen"
        assert self.fc.fd["pen_control"].get_pen_name_on_left_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        time.sleep(1)
        assert bool(self.fc.fd["pen_control"].verify_pen_edit_icon_show_commercial()) is True, "Pen control edit button is not show"
        time.sleep(1)
        # click pen edit icon
        self.fc.fd["pen_control"].click_pen_edit_icon_commercial()
        time.sleep(1)
        # verify pen name edit box show
        assert bool(self.fc.fd["pen_control"].verify_pen_name_edit_box_show_commercial()) is True, "Pen control edit box is not show"
        time.sleep(1)
        # edit empty pen name
        self.fc.fd["pen_control"].enter_device_name("")
        time.sleep(2)
        # verify pen name on right side is "HP Rechargeable Active Pen G3"
        assert self.fc.fd["pen_control"].get_pen_name_on_right_side_commercial() == "HP Rechargeable Active Pen G3", "Pen name of changed text Mismatch"
        time.sleep(1)
        # verify pen name on left side is "Pen"
        assert self.fc.fd["pen_control"].get_pen_name_on_left_side_commercial() == "Pen", "Pen name of changed text Mismatch"
        time.sleep(1)

    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_05_navigation_bar_C38252204(self):
        self.fc.reset_myhp_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
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
        # click pen edit icon
        self.fc.fd["pen_control"].click_pen_edit_icon_commercial()
        time.sleep(1)
        # verify pen name edit box show
        assert bool(self.fc.fd["pen_control"].verify_pen_name_edit_box_show_commercial()) is True, "Pen control edit box is not show"
        time.sleep(1)
        # edit pen name with "HPXPen"
        self.fc.fd["pen_control"].enter_device_name("HPXPen"), "Pen name of changed text Mismatch"
        time.sleep(2)
        # verify pen name on right side is "HPXPen"
        assert self.fc.fd["pen_control"].get_pen_name_on_right_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        time.sleep(1)
        # verify pen name on left side is "HPXPen"
        assert self.fc.fd["pen_control"].get_pen_name_on_left_side_commercial() == "HPXPen", "Pen name of changed text Mismatch"
        time.sleep(1)


    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_06_verify_double_press_action_list_C38313848(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        self.fc.fd["pen_control"].click_double_press_button_commercial()
        time.sleep(1)
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_double_press_side_menu_title_commercial(), "Top button - Double press", "double press title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_page_up_commercial(), "Page up", "Page up action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_page_down_commercial(), "Page down", "Page down action item is not visible")

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_title(), "Pen", "Pen title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_touch_on_off_commercial(), "Touch On/Off", "Touch on/off action is not visible")
        self.fc.fd["pen_control"].scroll_touch_on_off_element_commercial()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_productivity(), "Productivity", "Productivity title is not visible")

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_menu_commercial(), "Pen menu", "Pen menu action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_disabled_commercial(), "Disabled", "Disabled action item is not visible")

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_apps(), "Apps", "Apps title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_screen_snipping_commercial(), "Screen snipping", "Screen snipping action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_windows_search_commercial(), "Windows search", "Windows search action is not visible")

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_media_control(), "Media control", "Media control title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_play_pause_commercial(), "Play/Pause", "Play/pause action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_next_track_commercial(), "Next track", "Next track action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_previous_track_commercial(),"Previous track", "Previous track action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_up_commercial(), "Volume up", "Volume up action is not visible")
        self.fc.fd["pen_control"].scroll_down_volume_up_element_commercial()
        time.sleep(1)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_down_commercial(),"Volume down", "Volume down action is not visible")
        self.fc.fd["pen_control"].click_more_link_on_app_consumer()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_mute_audio_commercial(),"Mute audio", "Mute audio action is not visible")
        self.fc.fd["pen_control"].click_mute_audio_checkbox_commercial()
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_mute_audio_checkbox_is_selected()), "mute audio checkbox is not selected")
        soft_assertion.raise_assertion_errors()


    
    @pytest.mark.commercial
    @pytest.mark.function
    def test_07_verify_long_press_action_list_C38313857(self):
        self.fc.reset_myhp_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
            time.sleep(1)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        self.fc.fd["pen_control"].click_restore_button()
        self.fc.fd["pen_control"].click_long_press_button_commercial()
        time.sleep(1)
        soft_assertion = SoftAssert()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].verify_long_press_side_menu_title_commercial(), "Top button - Long press", "long press title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_page_up_commercial(), "Page up", "Page up action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_page_down_commercial(), "Page down", "Page down action item is not visible")

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_title(), "Pen", "Pen title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_touch_on_off_commercial(), "Touch On/Off", "Touch on/off action is not visible")
        self.fc.fd["pen_control"].scroll_touch_on_off_element_commercial()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_productivity(), "Productivity", "Productivity title is not visible")

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_pen_menu_commercial(), "Pen menu", "Pen menu action item is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_disabled_commercial(), "Disabled", "Disabled action item is not visible")

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_apps(), "Apps", "Apps title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_screen_snipping_commercial(), "Screen snipping", "Screen snipping action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_windows_search_commercial(), "Windows search", "Windows search action is not visible")

        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_media_control(), "Media control", "Media control title is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_play_pause_commercial(), "Play/Pause", "Play/pause action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_next_track_commercial(), "Next track", "Next track action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_previous_track_commercial(),"Previous track", "Previous track action is not visible")
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_up_commercial(), "Volume up", "Volume up action is not visible")
        self.fc.fd["pen_control"].scroll_down_volume_up_element_commercial()
        time.sleep(1)
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_volume_down_commercial(),"Volume down", "Volume down action is not visible")
        self.fc.fd["pen_control"].click_more_link_on_app_consumer()
        soft_assertion.assert_equal(self.fc.fd["pen_control"].get_mute_audio_commercial(),"Mute audio", "Mute audio action is not visible")
        self.fc.fd["pen_control"].click_mute_audio_checkbox_commercial()
        soft_assertion.assert_true(bool(self.fc.fd["pen_control"].verify_mute_audio_checkbox_is_selected()), "mute audio checkbox is not selected")
        soft_assertion.raise_assertion_errors()

    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_supported_systems_C38313943(self):
        self.fc.reset_myhp_app()
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        #verify pen control show in navigation bar in commercial
        assert bool(self.fc.fd["pen_control"].verify_pen_control_show_in_navigation_bar_commercial()) is True, "Pen control is not show navgation bar"
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)
    
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_10_launch_app_C35877527(self):
        self.fc.reset_myhp_app()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(1)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        #verify pen control show in navigation bar in commercial
        assert bool(self.fc.fd["pen_control"].verify_pen_control_show_in_navigation_bar_commercial()) is True, "Pen control is not show navgation bar"
        time.sleep(1)
        # click pen control menu
        self.fc.fd["navigation_panel"].navigate_to_pen_control_module()
        time.sleep(1)