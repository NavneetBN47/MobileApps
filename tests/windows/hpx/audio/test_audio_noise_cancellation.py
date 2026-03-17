from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Audio_Noise_Cancellation(object):
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
            time.sleep(3)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
    

    @pytest.mark.commercial
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_noise_cancellation_UI_C31728716(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_show() is True
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
        assert self.fc.fd["audio"].verify_noise_eduction_show() is True
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        assert self.fc.fd["audio"].verify_mic_mode_text_show() is True
        assert self.fc.fd["audio"].verify_conference_text_show() is True
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference is not selected"
        assert self.fc.fd["audio"].verify_personal_text_show() is True

    @pytest.mark.ota
    @pytest.mark.commercial
    def test_02_noise_cancellation_tooltips_C33431164(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].hover_noise_removal_tool_tip()
        assert bool(self.fc.fd["audio"].get_noise_removal_tool_tip()) is True
        time.sleep(2)
        self.fc.fd["audio"].hover_noise_reduction_tool_tip()
        assert bool(self.fc.fd["audio"].get_noise_reduction_tool_tip()) is True
    

    @pytest.mark.ota
    @pytest.mark.commercial
    @pytest.mark.require_sanity_check(["sanity"])
    def test_03_turn_on_off_noise_removal_button_C32377109(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        if self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0":
            self.fc.fd["audio"].click_noise_removal_toggle_to_on()
            time.sleep(1)
            assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "Noise removal toggle is off"
            self.fc.fd["audio"].click_noise_removal_toggle_to_off()
            assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
        else:
            self.fc.fd["audio"].click_noise_removal_toggle_to_off()
            time.sleep(1)
            assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
            self.fc.fd["audio"].click_noise_removal_toggle_to_on()
            assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "Noise removal toggle is off"


    @pytest.mark.ota
    @pytest.mark.commercial
    @pytest.mark.require_sanity_check(["sanity"])
    def test_04_turn_on_off_noise_reduction_button_C32377110(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()

        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        if self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1":
            self.fc.fd["audio"].click_noise_reduction_ontoggle()
            time.sleep(1)
            assert self.fc.fd["audio"].verify_noise_reduction_toggle_off() == "0", "Noise reduction toggle is on"
            self.fc.fd["audio"].click_noise_reduction_offtoggle()
            assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        else:
            self.fc.fd["audio"].click_noise_reduction_offtoggle()
            time.sleep(1)
            assert self.fc.fd["audio"].verify_noise_reduction_toggle_off() == "0", "Noise reduction toggle is on"
            self.fc.fd["audio"].click_noise_reduction_offtoggle()
            assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
    
    
    @pytest.mark.ota
    @pytest.mark.commercial
    @pytest.mark.require_sanity_check(["sanity"])
    def test_05_hide_mic_mode_C33020513(self):
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_microphone_array_in_all_devices()
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        assert self.fc.fd["audio"].verify_mic_mode_text_show() is True
        assert self.fc.fd["audio"].verify_conference_text_show() is True
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference is not be selected"
        assert self.fc.fd["audio"].verify_personal_text_show() is True
        time.sleep(2)
        self.fc.fd["audio"].click_noise_reduction_ontoggle()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_off() == "0", "Noise reduction toggle is on"
        assert self.fc.fd["audio"].verify_mic_mode_text_show() is False
        assert self.fc.fd["audio"].verify_conference_text_show() is False
        assert self.fc.fd["audio"].verify_personal_text_show() is False
        self.fc.fd["audio"].click_noise_reduction_offtoggle()
    
    
    @pytest.mark.commercial
    def test_06_noise_cancellation_settings_remembered_C32851921(self):
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference is not be selected"
        self.fc.fd["audio"].click_noise_removal_toggle_to_on()
        time.sleep(2)
        self.fc.fd["audio"].click_personal_checkbox()
        time.sleep(2)
        self.fc.fd["audio"].click_noise_reduction_ontoggle()
        time.sleep(2)

        self.fc.fd["navigation_panel"].navigate_to_settings()
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "Noise removal toggle is off"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_off() == "0", "Noise reduction toggle is on"
        self.fc.fd["audio"].click_noise_reduction_offtoggle()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_personal_checkbox_is_selected() == "1", "Personal is not be selected"

        self.fc.close_myHP()
        time.sleep(2)
        self.fc.launch_myHP()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_on_state() == "1", "Noise removal toggle is off"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        assert self.fc.fd["audio"].verify_personal_checkbox_is_selected() == "1", "Personal is not be selected"
        self.fc.fd["audio"].click_noise_reduction_ontoggle()
        
    
    @pytest.mark.commercial
    def test_07_noise_reduction_UI_C32318658(self):
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(5)
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(3)
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        self.fc.fd["audio"].click_conference_checkbox()
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference is not be selected"
        self.fc.fd["audio"].click_personal_checkbox()
        assert self.fc.fd["audio"].verify_personal_checkbox_is_selected() == "1", "Personal is not be selected"
        self.fc.fd["audio"].click_conference_checkbox()
    
    
    @pytest.mark.consumer
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_restore_defaults_work_with_noise_cancellation_C37539517(self):
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference is not be selected"
        self.fc.fd["audio"].click_noise_removal_toggle_to_on()
        self.fc.fd["audio"].click_personal_checkbox()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(3)
        self.fc.fd["audio"].click_restore_default_continue_button()
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
        assert self.fc.fd["audio"].verify_conference_checkbox_is_selected() == "1", "Conference is not be selected"
        self.fc.fd["audio"].click_noise_reduction_toggle_to_off()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(6)
        self.fc.fd["audio"].click_restore_default_continue_button()
        time.sleep(2)
        self.fc.swipe_window(direction="up", distance=6)
        time.sleep(2)
        assert self.fc.fd["audio"].verify_noise_removal_toggle_off() == "0", "Noise removal toggle is on"
        assert self.fc.fd["audio"].verify_noise_reduction_toggle_on_state() == "1", "Noise reduction toggle is off"
