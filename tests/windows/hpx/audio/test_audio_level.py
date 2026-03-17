from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Audio_Level(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        yield "close windows settings panel"
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        time.sleep(2)
        cls.fc.close_windows_settings_panel()
        time.sleep(2)

    
    def round_up(self,input_value):
        return round(float(input_value))
    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_audio_module_displayed_C31680840(self):
        time.sleep(3)
        self.fc.restart_app()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
            time.sleep(1)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        time.sleep(10)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        output_display = self.fc.fd["audio"].verify_output_title()
        assert output_display == True, "Output title is not displayed"
        
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_02_slide_input_slider_C32588095(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value_increase(100,"input_slider")
        time.sleep(2)
        width_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert width_value == "100", "Width value is not 100"
    
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_03_slide_output_slider_C32789781(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].set_slider_value_increase(100,"output_slider")
        time.sleep(2)
        width_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert width_value == "100", "Width value is not 100"

    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_audio_level_UI_C32313204(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert self.fc.fd["audio"].verify_output_title() is True, "Output title is not displayed"
        assert self.fc.fd["audio"].verify_output_icon() is True, "Output icon is not displayed"
        assert self.fc.fd["audio"].verify_input_icon() is True, "Input icon is not displayed"
    
    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    def test_05_verify_audio_show_home_module_C32881402(self):
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_welcome()
        time.sleep(2)

        assert bool(self.fc.fd["audio"].verify_home_audio_show()) is True, "Audio is not displayed"
        
    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_click_output_volume_slider_verify_that_position_moves_to_where_you_clicked_C31675694(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        output_value = self.fc.fd["audio"].get_slider_value("output_slider")

        if self.round_up(output_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100,"output_slider")
        input_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert "100"==input_value,"Volume not increased to 100"
        
        self.fc.fd["audio"].set_slider_value_decrease(100,"output_slider")
        input_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert "0"==input_value,"Volume not decreased to 0"

        self.fc.fd["audio"].set_slider_value_increase(50,"output_slider")
        input_value = self.fc.fd["audio"].get_slider_value("output_slider")
        assert "50"==input_value,"Volume is not 50%"
    

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_click_input_volume_slider_verify_that_position_moves_to_where_you_clicked_C31675695(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        
        if self.round_up(input_value)!=100:
            self.fc.fd["audio"].set_slider_value_increase(100,"input_slider")
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert "100"==input_value,"Volume not increased to 100"
    
        self.fc.fd["audio"].set_slider_value_decrease(100,"input_slider")
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert "0"==input_value,"Volume not decreased to 0"

        self.fc.fd["audio"].set_slider_value_increase(50,"input_slider")
        input_value = self.fc.fd["audio"].get_slider_value("input_slider")
        assert 50==self.round_up(input_value),"Volume is not 50%"