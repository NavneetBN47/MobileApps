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
            cls.fc.close_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_pc_device_new_ui_C38473579(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(10)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        assert bool(self.fc.fd["navigation_panel"].verify_pc_device_show()) is True, "PC Device is not visible on left panel."
        pc_device_name = self.fc.fd["navigation_panel"].get_pc_device_name()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(10)
        local_machine_name = self.fc.fd["devices"].get_device_name_text()
        assert pc_device_name == local_machine_name, "PC Device text Mismatch"

    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_02_pc_device_new_ui_interface_C38473527(self):
        time.sleep(2)
        self.fc.restart_myHP()    
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(7)
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header."
        assert bool(self.fc.fd["devices"].verify_modal_name_show_on_device_page_header()) is True, "The modal name is not visible on header."
        assert bool(self.fc.fd["devices"].verify_battery_icon_show_on_device_page_header()) is True, "The battery icon is not visible on header."
        assert bool(self.fc.fd["devices"].verify_infor_icon_show_on_device_page_header()) is True, "The infor icon is not visible on header."
        self.fc.fd["devices"].click_infor_icon_on_device_page_header()
        time.sleep(10)
        assert bool(self.fc.fd["devices"].verify_product_number_name_show_on_device_page_header()) is True, "The production number text is not visible on header."
        assert bool(self.fc.fd["devices"].verify_product_number_show_on_device_page_header()) is True, "The production number is not visible on header."
        assert bool(self.fc.fd["devices"].verify_product_number_copy_icon_show_on_device_page_header()) is True, "The production number copy icon is not visible on header."
        assert bool(self.fc.fd["devices"].verify_serial_number_name_show_on_device_page_header()) is True, "The serial number text is not visible on header."
        assert bool(self.fc.fd["devices"].verify_serial_number_show_on_device_page_header()) is True, "The serial number is not visible on header."
        assert bool(self.fc.fd["devices"].verify_serial_number_copy_icon__show_on_device_page_header()) is True, "The serial number copy icon is not visible on header."
        assert bool(self.fc.fd["devices"].verify_pc_device_image_show_on_device_page()) is True, "The pc device image is not visible on header."
        self.fc.fd["devices"].click_infor_icon_on_device_page_header()
        time.sleep(2)
        if self.fc.fd["devices"].verify_audio_control_card_show_on_device_page() is False:
            print("This machine does not have audio control card")
            
        else:
            if self.fc.fd["devices"].verify_video_control_card_show_on_device_page() is False:
                print("This machine does not have video control card")
                
            else:
                if self.fc.fd["devices"].verify_display_control_card_show_on_device_page() is False:
                    print("This machine does not have display control card")
                    
                else:
                    if self.fc.fd["devices"].verify_programmable_key_card_show_on_device_page() is False:
                        print("This machine does not have programmable key card")
                        
                    else:
                        if self.fc.fd["devices"].verify_5G_card_show_on_device_page() is False:
                            print("This machine does not have 5G card")
                            
                        else:
                            if self.fc.fd["devices"].verify_support_card_show_on_device_page() is False:
                                print("This machine does not have support card")


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_03_check_battry_on_device_page_header_C38473746(self):
        time.sleep(2)
        self.fc.restart_myHP()    
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_battery_icon_show_on_device_page_header()) is True, "The battery icon is not visible on header."
        assert self.fc.fd["devices"].get_battery_tooltips()[:7] == "Battery", "Battery tooltips text Mismatch"


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.require_sanity_check(["sanity"])
    def test_04_check_infor_on_device_page_header_C38473582(self):
        time.sleep(2)
        self.fc.restart_myHP()    
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert bool(self.fc.fd["devices"].verify_infor_icon_show_on_device_page_header()) is True, "The infor icon is not visible on header."
        self.fc.fd["devices"].click_infor_icon_on_device_page_header()
        time.sleep(10)
        assert bool(self.fc.fd["devices"].verify_product_number_name_show_on_device_page_header()) is True, "The production number text is not visible on header."
        assert bool(self.fc.fd["devices"].verify_product_number_show_on_device_page_header()) is True, "The production number is not visible on header."
        assert bool(self.fc.fd["devices"].verify_product_number_copy_icon_show_on_device_page_header()) is True, "The production number copy icon is not visible on header."
        assert bool(self.fc.fd["devices"].verify_serial_number_name_show_on_device_page_header()) is True, "The serial number text is not visible on header."
        assert bool(self.fc.fd["devices"].verify_serial_number_show_on_device_page_header()) is True, "The serial number is not visible on header."
        assert bool(self.fc.fd["devices"].verify_serial_number_copy_icon__show_on_device_page_header()) is True, "The serial number copy icon is not visible on header."


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_05_hpx_ui_C38412703(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        assert bool(self.fc.fd["navigation_panel"].verify_home_navagation()) is True, "The home module is not visible on navigation panel."
        assert bool(self.fc.fd["navigation_panel"].verify_pcdevice_module_show()) is True, "The pc device module is not visible on navigation panel."
        assert bool(self.fc.fd["navigation_panel"].verify_support_module_show()) is True, "The support module is not visible on navigation."
        assert bool(self.fc.fd["navigation_panel"].verify_setting_module_show()) is True, "The setting module is not visible on navigation panel." 


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_06_hppk_under_action_title_C38474997(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header." 
        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_pc_programmable_key_module()
        assert bool(self.fc.fd["devices"].verify_pc_device_top_title_on_hppk_module()) is True, "The hppk module is not visible on pc device header." 
        assert self.fc.fd["hppk"].get_prog_key_nav_text() == "Programmable key", "The Programmable Key text Mismatch." 
        time.sleep(2)
        self.fc.fd["devices"].click_pc_device_title_from_programmable_key_title()
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header." 


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_07_support_under_action_title_C38475153(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header." 
        time.sleep(2)
        self.fc.fd["devices"].click_support_module_on_pc_device()
        time.sleep(3)
        self.fc.kill_chrome_process()
        time.sleep(3)
        assert bool(self.fc.fd["sanity_check"].verify_support_module_show()) is True, "The support module is not visible on pc device." 
        time.sleep(2)
        self.fc.fd["devices"].click_back()
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header." 


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_08_check_device_name_equal_pc_device_name_C38474082(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        pc_device_name = self.fc.fd["navigation_panel"].get_pc_device_name()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header." 
        time.sleep(10)
        local_machine_name = self.fc.fd["devices"].get_device_name_text()
        assert pc_device_name == local_machine_name, "The PC device name does not match the local name." 


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_09_check_serial_numder_under_inor_icon_C38474251(self):
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        assert bool(self.fc.fd["navigation_panel"].verify_pc_device_show()) is True, "PC Device is not visible on left panel."
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_infor_icon_show_on_device_page_header()) is True, "The infor icon is not visible on header."
        self.fc.fd["devices"].click_infor_icon_on_device_page_header()
        time.sleep(5)
        assert bool(self.fc.fd["devices"].verify_serial_number_name_show_on_device_page_header()) is True, "The serial number text is not visible on header."
        assert bool(self.fc.fd["devices"].verify_serial_number_show_on_device_page_header()) is True, "The serial number is not visible on header."
        assert bool(self.fc.fd["devices"].verify_serial_number_copy_icon__show_on_device_page_header()) is True, "The serial number copy icon is not visible on header."
        self.fc.fd["devices"].click_serial_number_under_infor_icon()
        copied = self.fc.fd["devices"].get_serial_number_copied_under_infor_icon()
        assert copied == "Copied", "The Copied text Mismatch." 


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_10_verify_tooltip_copy_button_C38474464(self):
        self.fc.restart_myHP()    
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        self.fc.fd["devices"].verify_infor_icon_show_on_device_page_header()
        self.fc.fd["devices"].click_infor_icon_on_device_page_header()
        time.sleep(5)
        assert bool(self.fc.fd["devices"].verify_serial_number_name_show_on_device_page_header()) is True, "The serial number text is not visible on header."
        assert bool(self.fc.fd["devices"].verify_serial_number_show_on_device_page_header()) is True, "The serial number is not visible on header."
        assert bool(self.fc.fd["devices"].verify_serial_number_copy_icon__show_on_device_page_header()) is True, "The serial number copy icon is not visible on header."
        assert bool(self.fc.fd["devices"].verify_presenceof_serialnumber_tooltip()) is True, "The presenceof serial number tooltip is not visible on header."
        assert bool(self.fc.fd["devices"].verify_product_number_name_show_on_device_page_header()) is True, "The production number text is not visible on header."
        assert bool(self.fc.fd["devices"].verify_product_number_show_on_device_page_header()) is True, "The production number is not visible on header."
        assert bool(self.fc.fd["devices"].verify_product_number_copy_icon_show_on_device_page_header()) is True, "The production number copy icon is not visible on header."
        self.fc.fd["devices"].click_productnumber_value_tooltip()
        expected_productnumber_tooltip_text = "Copied"
        actual_productnumber_tooltip_text = self.fc.fd["devices"].get_productnumber_value_tooltip_text()
        assert actual_productnumber_tooltip_text == expected_productnumber_tooltip_text
        assert bool(self.fc.fd["devices"].verify_presenceof_productnumber_tooltip()) is True, "The presenceof production number tooltip is not visible on header."
        self.fc.fd["devices"].click_serialnumber_value_tooltip()
        expected_serialnumber_tooltip_text = "Copied"
        actual_serialnumber_tooltip_text = self.fc.fd["devices"].get_serialnumber_value_tooltip_text()
        assert actual_serialnumber_tooltip_text == expected_serialnumber_tooltip_text, "The presenceof serial number tooltip text is not visible on header."
        assert bool(self.fc.fd["devices"].verify_presenceof_serialnumber_tooltip()) is True, "The presenceof serial number tooltip is not visible on header."


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_12_verify_tooltip_for_device_name_C38474610(self):
        time.sleep(3)
        self.fc.restart_myHP()
        time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        assert bool(self.fc.fd["navigation_panel"].verify_pc_device_show()) is True, "The pc device module is not visible."
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        self.fc.fd["devices"].verify_presenceOf_custom_deviceName()
        time.sleep(10)
        devicename_text = self.fc.fd["devices"].get_device_name_text()
        time
        self.fc.fd["devices"].click_devicename_for_text()
        time.sleep(5)
        devicename_text_tooltip = self.fc.fd["devices"].get_custom_devicename_text()
        assert devicename_text_tooltip == devicename_text,"Device tootip text Mismatch"


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_13_verify_tooltip_for_product_number_C38474122(self):
        time.sleep(2)
        self.fc.restart_myHP()
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        assert bool(self.fc.fd["navigation_panel"].verify_pc_device_show()) is True, "PC Device is not visible on left panel."
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(7)
        assert bool(self.fc.fd["devices"].verify_infor_icon_show_on_device_page_header()) is True, "The infor icon is not visible on header."
        self.fc.fd["devices"].click_infor_icon_on_device_page_header()
        time.sleep(10)
        assert bool(self.fc.fd["devices"].verify_product_number_name_show_on_device_page_header()) is True, "The production number text is not visible on header."
        assert bool(self.fc.fd["devices"].verify_product_number_show_on_device_page_header()) is True, "The production number is not visible on header."
        assert bool(self.fc.fd["devices"].verify_product_number_copy_icon_show_on_device_page_header()) is True, "The production number copy icon is not visible on header."
        self.fc.fd["devices"].click_productnumber_value_tooltip()
        expected_productnumber_tooltip_text = "Copied"
        actual_productnumber_tooltip_text = self.fc.fd["devices"].get_productnumber_value_tooltip_text()
        assert actual_productnumber_tooltip_text == expected_productnumber_tooltip_text, "Production number tootip text Mismatch"
        assert bool(self.fc.fd["devices"].verify_presenceof_productnumber_tooltip()) is True, "The presenceof production number tooltip is not visible on header."


    @pytest.mark.commercial
    @pytest.mark.function
    @pytest.mark.ota
    def test_14_back_to_pc_device_page_from_system_control_page_C38475204(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header."
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True,"system control card is not displayed"
        self.fc.fd["devices"].click_system_control_card()
        assert bool(self.fc.fd["system_control"].verify_smart_sense()) is True,"Smart Sense header is not displayed"
        assert bool(self.fc.fd["system_control"].verify_performance_commercial()) is True,"Performance Control title is not displayed"
        self.fc.fd["devices"].click_devicename_for_back_PC_device_page()
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header."
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True,"system control card is not displayed"

    @pytest.mark.function
    @pytest.mark.ota
    def test_04_back_to_check_battery_card_under_pc_device_page_C38475205(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_presenceOf_custom_deviceName()) is True, "The device name is not visible on header."
        self.fc.fd["devices"].verify_battery_manager_card()
        self.fc.fd["devices"].click_for_battery_manager_card()
        assert self.fc.fd["battery"].get_info_title_text() == "Battery Information"
        self.fc.fd["battery"].click_devicename_on_header()
        assert bool(self.fc.fd["devices"].verify_presenceOf_custom_deviceName()) is True, "The device name is not visible on header."
