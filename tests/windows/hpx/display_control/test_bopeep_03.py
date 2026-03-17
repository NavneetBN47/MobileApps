from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import pytest
import re
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()

class Test_Suite_Bopeep(object):
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
    
    #this suite should run on bopeep
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_drag_rgb_slider_with_mouse_C34324894(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(10)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "The advanced settinng button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "The advanced settings string is incorrect"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # increase 1 for red color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # increase 1 for green color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)
        # increase 1 for blue color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"blue_slider")
        time.sleep(1)
        # get blue color slider value is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_rgb_slider_visual_for_neutral_modes_C34324897(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(10)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify neutral image mode show
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "The neutral image mode is not show"
        time.sleep(1)
        # click neutral image mode
        self.fc.fd["display_control"].click_natural_mode()
        time.sleep(1)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "The neutral image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "The advanced setting button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "The advanced settings string is incorrect"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # increase 1 for red color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # increase 1 for green color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)
        # increase 1 for blue color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"blue_slider")
        time.sleep(1)
        # get blue color slider value is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify neutral image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "The neutral image mode is not selected"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_rgb_slider_visual_for_gaming_modes_C34324898(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(10)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify gaming image mode show
        assert bool(self.fc.fd["display_control"].verify_game_mode_title()) is True, "The gaming image mode is not show"
        time.sleep(1)
        # click gaming image mode
        self.fc.fd["display_control"].click_game_mode()
        time.sleep(1)
        # verify gaming image mode is selected
        assert bool(self.fc.fd["display_control"].get_game_mode()) is True, "The gaming image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "The advanced setting button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "The advanced settings string is incorrect"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # increase 1 for red color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # increase 1 for green color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)
        # increase 1 for blue color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"blue_slider")
        time.sleep(1)
        # get blue color slider value is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify gaming image mode is selected
        assert bool(self.fc.fd["display_control"].get_game_mode()) is True, "The gaming image mode is not selected"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_rgb_slider_visual_for_reading_modes_C34324899(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(10)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify reading image mode show
        assert bool(self.fc.fd["display_control"].verify_reading_mode_title()) is True, "The reading image mode is not show"
        time.sleep(1)
        # click reading image mode
        self.fc.fd["display_control"].click_reading_mode()
        time.sleep(1)
        # verify reading image mode is selected
        assert bool(self.fc.fd["display_control"].verify_reading_mode_title()) is True, "The reading image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "The advanced setting button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "The advanced settings string is incorrect"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # increase 1 for red color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # increase 1 for green color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)
        # increase 1 for blue color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"blue_slider")
        time.sleep(1)
        # get blue color slider value is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify reading image mode is selected
        assert bool(self.fc.fd["display_control"].verify_reading_mode_title()) is True, "The reading image mode is not selected"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_rgb_slider_visual_for_night_modes_C34324900(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(10)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify night image mode show
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "The night image mode is not show"
        time.sleep(1)
        # click night image mode
        self.fc.fd["display_control"].click_night_mode()
        time.sleep(1)
        # verify night image mode is selected
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "The night image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "The advanced setting button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "The advanced settings string is incorrect"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # increase 1 for red color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # increase 1 for green color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)
        # increase 1 for blue color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"blue_slider")
        time.sleep(1)
        # get blue color slider value is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify night image mode is selected
        assert bool(self.fc.fd["display_control"].verify_night_mode_title()) is True, "The night image mode is not selected"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_06_rgb_slider_visual_for_movie_modes_C34324901(self):
        time.sleep(3)
        self.fc.restart_app()
        time.sleep(10)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify movie image mode show
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "The movie image mode is not show"
        time.sleep(1)
        # click movie image mode
        self.fc.fd["display_control"].click_movie_mode()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "The movie image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "The advanced setting button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "The advanced settings string is incorrect"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 90
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # increase 1 for red color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # increase 1 for green color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)
        # increase 1 for blue color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"blue_slider")
        time.sleep(1)
        # get blue color slider value is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify movie image mode is selected
        assert bool(self.fc.fd["display_control"].verify_movie_mode_title()) is True, "The movie image mode is not selected"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_rgb_slider_visual_for_hp_enhance_modes_C34324902(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        time.sleep(10)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()
        time.sleep(1)
        # verify hp enhance+ image mode show
        assert bool(self.fc.fd["display_control"].verify_enhanceplus_mode_title()) is True, "The hp enhance+ image mode is not show"
        time.sleep(1)
        # click hp enhance+ image mode
        self.fc.fd["display_control"].click_enhanceplus_mode()
        time.sleep(1)
        # verify hp enhance+ image mode is selected
        assert bool(self.fc.fd["display_control"].verify_enhanceplus_mode_title()) is True, "The hp enhance+ image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "The advanced setting button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "The advanced settings string is incorrect"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].is_red_slider_visible()) is False, "The red color slider is visible"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].is_green_slider_visible()) is False, "The green color slider is visible"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].is_blue_slider_visible()) is False, "The blue color slider is visible"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verify hp enhance+ image mode is selected
        assert bool(self.fc.fd["display_control"].verify_enhanceplus_mode_title()) is True, "The hp enhance+ image mode is not selected"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_rgb_slider_visual_for_native_modes_C34324904(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        time.sleep(10)
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify native image mode show
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "The native image mode is not show"
        time.sleep(1)
        # click native image mode
        self.fc.fd["display_control"].click_natural_mode()
        time.sleep(1)
        # verifyhp native image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "The native image mode is not selected"
        time.sleep(1)
        # verify settings button show
        assert bool(self.fc.fd["display_control"].verify_advaced_setting_visible()) is True, "The advanced setting button is not show"
        time.sleep(1)
        # click settings button
        self.fc.fd["display_control"].click_advaced_setting()
        time.sleep(1)
        # verify string of "advanced settings" show
        assert self.fc.fd["display_control"].verify_advanced_settings_title() == "Advanced Settings", "The advanced settings string is incorrect"
        time.sleep(1)
        # verify red color slider show
        assert bool(self.fc.fd["display_control"].verify_red_slider()) is True, "The red color slider is not show"
        time.sleep(1)
        # verify red color slider value default is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # decrease 1 for red color slider 
        self.fc.fd["display_control"].set_red_slider_value_decrease(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # verify green color slider show
        assert bool(self.fc.fd["display_control"].verify_green_slider()) is True, "The green color slider is not show"
        time.sleep(1)
        # verify green color slider value default is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # decrease 1 for green color slider
        self.fc.fd["display_control"].set_green_slider_value_decrease(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # verify blue color slider show
        assert bool(self.fc.fd["display_control"].verify_blue_slider()) is True, "The blue color slider is not show"
        time.sleep(1)
        # verify blue color slider value default is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # decrease 1 for blue color slider
        self.fc.fd["display_control"].set_blue_slider_value_decrease(1,"blue_slider")   
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(3)
        # get red color slider value is 99
        assert self.fc.fd["display_control"].verify_red_slider_value() == "99", "The red color slider value is not 99"
        time.sleep(1)
        # increase 1 for red color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"red_slider")
        time.sleep(1)
        # get red color slider value is 100
        assert self.fc.fd["display_control"].verify_red_slider_value() == "100", "The red color slider value is not 100"
        time.sleep(1)
        # get green color slider value is 99
        assert self.fc.fd["display_control"].verify_green_slider_value() == "99", "The green color slider value is not 99"
        time.sleep(1)
        # increase 1 for green color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"green_slider")
        time.sleep(1)
        # get green color slider value is 100
        assert self.fc.fd["display_control"].verify_green_slider_value() == "100", "The green color slider value is not 100"
        time.sleep(1)
        # get blue color slider value is 99
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "99", "The blue color slider value is not 99"
        time.sleep(1)
        # increase 1 for blue color slider
        self.fc.fd["display_control"].set_slider_value_increase(1,"blue_slider")
        time.sleep(1)
        # get blue color slider value is 100
        assert self.fc.fd["display_control"].verify_blue_slider_value() == "100", "The blue color slider value is not 100"
        time.sleep(1)
        # click "x" button in advanced settings
        self.fc.fd["display_control"].click_close_btn_advanced_settings()
        time.sleep(1)
        # verifyhp native image mode is selected
        assert bool(self.fc.fd["display_control"].verify_natural_mode_title()) is True, "The native image mode is not selected"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_09_relaunch_brightness_C34324934(self):
        time.sleep(3)
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get default brightness slider value 
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "76", "The default brightness slider value is not 76"
        time.sleep(1)
        # drag brightness slider to maximum value
        self.fc.fd["display_control"].set_slider_value_increase(24,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 100
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "100", "The brightness slider value is not 100"
        time.sleep(1)
        # close application and Relaunch
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 100
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "100", "The brightness slider value is not 100"
        time.sleep(1)
        # drag brightness slider to minimum value
        self.fc.fd["display_control"].set_slider_value_decrease(100,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 0
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "0", "The brightness slider value is not 0"
        time.sleep(1)
        # close application and Relaunch
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 0
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "0", "The brightness slider value is not 0"
        time.sleep(1)
        # drag brightness slider to medium value
        self.fc.fd["display_control"].set_slider_value_increase(50,"Brightness_slider")
        time.sleep(3)
        # get brightness slider value is 50
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "50", "The brightness slider value is not 50"
        # close application and Relaunch
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify brightness slider present
        assert self.fc.fd["display_control"].verify_brightness_slider_is_present() == True, "The brightness slider is not present"
        time.sleep(1)
        # get brightness slider value is 50
        assert self.fc.fd["display_control"].get_brightness_slider_value("Brightness_slider") == "50", "The brightness slider value is not 50"
        time.sleep(1)

    @pytest.mark.consumer
    @pytest.mark.function
    def test_10_relaunch_contrast_C34324935(self):
        time.sleep(3)
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify restore default button show
        assert bool(self.fc.fd["display_control"].verify_restore_default_button()) is True, "The restore default button is not show"
        time.sleep(1)
        # click restore default button
        self.fc.fd["display_control"].click_restore_defaults_button()
        time.sleep(1)
        # click "continue" button
        self.fc.fd["display_control"].click_restore_pop_up_continue_button()
        time.sleep(10)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get default contrast slider value 
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The default contrast slider value is not 100"
        time.sleep(1)
        # so do not need to drag to maximum value
        # close application and Relaunch
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 100
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "100", "The contrast slider value is not 100"
        time.sleep(1)
        # drag contrast slider to minimum value
        self.fc.fd["display_control"].set_slider_value_decrease(100,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 0
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "0", "The contrast slider value is not 0"
        time.sleep(1)
        # close application and Relaunch
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 0
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "0", "The contrast slider value is not 0"
        time.sleep(1)
        # drag contrast slider to medium value
        self.fc.fd["display_control"].set_slider_value_increase(50,"Contrast_slider")
        time.sleep(3)
        # get contrast slider value is 50
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "50", "The contrast slider value is not 50"
        # close application and Relaunch
        self.fc.restart_app()
        # verify_navigationicon_show
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        # go to navigated bar
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        time.sleep(1)
        # click pc device menu
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        time.sleep(1)
        # click display control card
        self.fc.fd["devices"].click_display_control()       
        time.sleep(1)
        # verify contrast slider present
        assert self.fc.fd["display_control"].verify_contrast_slider_is_present() == True, "The contrast slider is not present"
        time.sleep(1)
        # get contrast slider value is 50
        assert self.fc.fd["display_control"].get_contrast_slider_value("Contrast_slider") == "50", "The contrast slider value is not 50"
        time.sleep(1)