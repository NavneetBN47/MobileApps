import re
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Dock_Station(object):
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


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_check_dock_station_ui_C42523008(self):
        time.sleep(3)
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"

        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_edit_button_show()) is True, "Dock station title edit button is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_name_show()) is True, "Dock station module name is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_support_button_show()) is True, "Dock station support button is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_scroll_view_show()) is True, "Dock station image is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_image_show()) is True, "Dock station image is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_connection_button_show()) is True, "Dock station connection button is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_infor_button_show()) is True, "Dock station information button is not displayed"


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_rename_dock_station_name_C42523012(self):
        self.fc.reset_myhp_app()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        assert self.fc.fd["dock_station"].get_dock_station_name() == "Dock Station", "Dock station name doesn't show up"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_edit_button_show()) is True, "Dock station title edit button is not displayed"
        self.fc.fd["dock_station"].click_edit_button()
        time.sleep(2)
        self.fc.fd["dock_station"].set_new_dock_station_name("New Dock")
        time.sleep(2)
        assert self.fc.fd["dock_station"].get_dock_station_name() == "New Dock", "Dock station name is not changed"
        
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        assert self.fc.fd["dock_station"].get_dock_station_name_on_navigation_panel() == "New Dock", "Dock station name is not changed"
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert self.fc.fd["dock_station"].get_dock_station_name() == "New Dock", "Dock station name is not changed"


    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_default_dock_station_name_C42523013(self):
        self.fc.reset_myhp_app()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        assert self.fc.fd["dock_station"].get_dock_station_name() == "Dock Station", "Dock station name doesn't show up"
        
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_edit_button_show()) is True, "Dock station title edit button is not displayed"
        self.fc.fd["dock_station"].click_edit_button()
        time.sleep(2)
        self.fc.fd["dock_station"].set_new_dock_station_name("New Dock")
        time.sleep(2)
        assert self.fc.fd["dock_station"].get_dock_station_name() == "New Dock", "Dock station name is not changed"

        self.fc.fd["dock_station"].click_edit_button()
        time.sleep(2)
        
        self.fc.fd["dock_station"].set_new_dock_station_name("")
        assert self.fc.fd["dock_station"].get_dock_station_name() == "Dock Station", "Dock station name doesn't recover to original name"


    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_04_check_dock_station_connection_tooltips_C42523015(self):
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_connection_button_show()) is True, "Dock station coonection button is not displayed"
        assert self.fc.fd["dock_station"].get_dock_station_connection_tooltips() == "Connection Thunderbolt", "Dock station connection tooltips don't show up"

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_check_dock_station_support_C42523020(self):
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_support_button_show()) is True, "Dock station support button is not displayed"
        self.fc.fd["dock_station"].click_dock_station_support_button()
        time.sleep(2)
        assert bool(self.fc.fd["support_home"].verify_support_home_title()) is True, "support page is not displayed"

    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_check_ui_dock_station_page_C42523011(self):
        time.sleep(3)
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed on navigation panel"

        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_edit_button_show()) is True, "Dock station title edit button is not displayed"
        assert self.fc.fd["dock_station"].get_dock_station_name() == "Dock Station", "Dock station name doesn't show up"
        
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_name_show()) is True, "Dock station module name is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_support_button_show()) is True, "Dock station support button is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_scroll_view_show()) is True, "Dock station image is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_image_show()) is True, "Dock station image is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_connection_button_show()) is True, "Dock station connection button is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_infor_button_show()) is True, "Dock station information button is not displayed"
        
           
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_validate_dock_station_name_C42523014(self):
        self.fc.reset_myhp_app()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"

        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_edit_button_show()) is True, "Dock station title edit button is not displayed"
        assert self.fc.fd["dock_station"].get_dock_station_name() == "Dock Station", "Dock station name doesn't show up"

        new_name = ["", "New_Dock1", "1234567890123456789012345", "1234567890123456789012345dock"]
        for name in new_name:
            self.fc.fd["dock_station"].click_edit_button()
            time.sleep(1)
            self.fc.fd["dock_station"].set_new_dock_station_name(name)
            time.sleep(2)
            current_name = self.fc.fd["dock_station"].get_dock_station_name()
            new_name1 = ["Dock Station", "New_Dock1", "1234567890123456789012345", "1234567890123456789012345dock"]
            assert current_name in new_name1, f"Dock station name is not changed to {new_name}"
            time.sleep(2)
            if len(name) <= 25:
                print(f"Dock station name is less than 25 characters and is {current_name}")

        self.fc.fd["dock_station"].click_edit_button()
        time.sleep(2)
        self.fc.fd["dock_station"].set_special_dock_station_name("@")
        assert self.fc.fd["dock_station"].get_dock_station_rename_error_message() == "Dock Station name can't contain any special characters, please only use letters, hyphens, and numbers."
        self.fc.close_myHP()
        self.fc.reset_myhp_app()
        time.sleep(2)

    
    @pytest.mark.consumer
    @pytest.mark.function
    def test_08_check_keyboard_navigation_C42523029(self):
        time.sleep(3)
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed on navigation panel"
       
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
       
        self.fc.fd["dock_station"].click_edit_button()
        self.fc.fd["dock_station"].check_keyboard_focus_elements()
        time.sleep(2)
        self.fc.close_myHP()
    
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_09_dock_information_button_C42523016(self):
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        self.fc.fd["dock_station"].click_dock_station_infor_button()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_serial_number_dock_station()) is True, "Dock station serial number is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_copy_icon_dock_station()) is True, "Dock station copy icon is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_firmware_version_dock_station()) is True, "Dock station firmware version is not displayed"

    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_10_hook_image_dock_image_C42523022(self):
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_name_show()) is True, "Dock station module name is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_connection_button_show()) is True, "Dock station connection button is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_infor_button_show()) is True, "Dock station information button is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_image_show()) is True, "Dock station image is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_support_button_show()) is True, "Dock station support button is not displayed"
    
    @pytest.mark.consumer
    @pytest.mark.function
    def test_11_Consistency_C42523030(self):
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        self.fc.open_notepad()
        time.sleep(2)
        self.fc.close_notepad()
        for _ in range(10):
            self.fc.restart_myHP()
            time.sleep(5)
            assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
            assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
            self.fc.fd["dock_station"].navigate_to_dock_station_page()
            time.sleep(2)
            assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
            self.fc.open_notepad()
            time.sleep(2)
            self.fc.close_notepad()

    @pytest.mark.consumer          
    @pytest.mark.function
    @pytest.mark.ota
    def test_12_firmware_version_C42523010(self):
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        self.fc.fd["dock_station"].click_dock_station_infor_button()
        firmware_version=self.fc.fd["dock_station"].get_firmware_version_dock_station()
        f_v=re.search("([0-9\d]{1})", firmware_version).group(1)
        assert f_v == "1" , "firmware version is not 1"


    @pytest.mark.consumer          
    @pytest.mark.function
    @pytest.mark.ota
    def test_13_copy_button_check_C42523017(self):
        self.fc.restart_myHP()
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True, "Navigation icon is not visible"
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_title_show()) is True, "Dock station title is not displayed"
        self.fc.fd["dock_station"].click_dock_station_infor_button()
        time.sleep(2)
        assert bool(self.fc.fd["dock_station"].verify_serial_number_dock_station()) is True, "Dock station serial number is not displayed"
        assert bool(self.fc.fd["dock_station"].verify_copy_icon_dock_station()) is True, "Dock station copy icon is not displayed"
        self.fc.fd["dock_station"].click_copy_icon_dock_station()
        time.sleep(2)
        self.fc.fd["audio"].launch_common_apps("Notepad")
        time.sleep(2)
        self.fc.fd["dock_station"].click_file_button_on_notepad()
        time.sleep(2)
        self.fc.fd["dock_station"].click_new_tab_on_notepad()
        time.sleep(2)
        self.fc.fd["dock_station"].click_paste_button_on_notepad()
        assert self.fc.fd["dock_station"].get_version_on_notepad() == "*5CG427Z7HM - Notepad"
        self.fc.close_notepad()
        time.sleep(2)