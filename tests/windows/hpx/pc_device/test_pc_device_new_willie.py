from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_PCDevice_new_ui(object):
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


    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_check_infor_on_device_page_header_C38473813(self):
        time.sleep(2)
        self.fc.restart_myHP()    
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        assert bool(self.fc.fd["home"].verify_home_module_show_on_global_navigation_panel()) is True, "The home module is not visible on navigation panel."
        assert bool(self.fc.fd["devices"].verify_pc_device_module_show_on_global_navigation_panel()) is True, "The pc device module is not visible on navigation panel."
        assert bool(self.fc.fd["devices"].verify_pc_device_module_show_on_global_navigation()) is True, "The pc device module is not visible on navigation."
        assert bool(self.fc.fd["pen_control"].verify_pen_control_module_show_on_global_navigation_panel()) is True, "The pen control module is not visible on navigation panel."
        assert bool(self.fc.fd["navigation_panel"].verify_support_menu_navigation()) is True, "The support module is not visible on navigation."
        assert bool(self.fc.fd["settings"].verify_settings_module_show_on_global_navigation_panel()) is True, "The setting module is not visible on navigation panel." 
        assert bool(self.fc.fd["devices"].verify_infor_icon_show_on_device_page_header()) is True, "The infor icon is not visible on header."
        assert bool(self.fc.fd["devices"].verify_battery_icon_show_on_device_page_header()) is True, "The battery icon is not visible on header."

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_audio_control_under_action_title_C38474990(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header."
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        assert bool(self.fc.fd["devices"].verify_pc_device_top_title_on_audio_module()) is True, "The audio module is not visible."
        assert self.fc.fd["audio"].verify_home_audio_control() == "Audio control", "The Audio control text Mismatch."
        time.sleep(2)
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header." 

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_display_control_under_action_title_C38475154(self):
        time.sleep(2)
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header."
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert bool(self.fc.fd["devices"].verify_pc_device_top_title_on_display_control_module()) is True, "The display control module is not visible on pc device." 
        assert self.fc.fd["display_control"].get_display_control_title_text() == "Display control", "The Display control text Mismatch."
        time.sleep(2)
        self.fc.fd["devices"].click_pc_device_title_from_display_title()
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header." 

    def test_04_launch_pcdevice_via_deeplink_C49014494(self):
        self.fc.close_myHP()
        self.fc.launch_module_using_deeplink("hpx://pcdevicedetails")
        assert bool(self.fc.fd["devices"].verify_pc_device_is_selected_from_navbar()) is True,"pc device is not selected from navbar"
