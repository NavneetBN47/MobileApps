from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import re


pytest.app_info = "HPX"
class Test_Suite_PCDevice(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_app()
        time.sleep(2)

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_stack(["production"])
    def test_01_verify_all_module_at_hamburger_menu_C32313078(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        home_Menu_text = self.fc.fd["navigation_panel"].verify_home_menu_navigation()
        assert "Home" == home_Menu_text,"Home menu is not visible"
        devices_Menu_text = self.fc.fd["navigation_panel"].verify_devices_menu_navigation()
        assert "Devices" == devices_Menu_text,"Devices menu is not visible"
        support_Menu_text = self.fc.fd["navigation_panel"].verify_support_menu_navigation()
        assert "Support" == support_Menu_text,"Support menu is not visible"
        settings_Menu_text = self.fc.fd["navigation_panel"].verify_settings_menu_navigation()
        assert "Settings" == settings_Menu_text,"Settings menu is not visible"
        pen_control_submenu_text = self.fc.fd["devices"].verify_pen_control()
        assert "Pen" == pen_control_submenu_text,"Pen Control submenu is not visible"


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_platform(["grogu"])
    def test_03_click_on_the_audio_control_card_under_the_action_title_C32313081(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        assert audio_control_text == "Audio control","Audio Control is not visible at PC Device - {}".format(audio_control_text)
        self.fc.fd["devices"].click_audio_control()
        self.fc.fd["devices"].click_pc_device_title_from_audio_title()
        audio_control_text = self.fc.fd["devices"].verify_audio_control()
        assert audio_control_text == "Audio control","Audio Control is not visible at PC Device - {}".format(audio_control_text)

    @pytest.mark.require_stack(["production"])
    def test_04_click_on_video_control_card_under_the_action_title_C32588620(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        video_control_text = self.fc.fd["devices"].verify_video_control()
        assert video_control_text == "Video control","Video Control is not visible at PC Device - {}".format(video_control_text)
        self.fc.fd["devices"].click_video_control()
        self.fc.fd["devices"].close_hp_video_app()

    @pytest.mark.require_platform(["on hold"])
    def test_05_click_on_the_RGB_Keyboard_card_under_the_action_title_C32313082(self):
        self.fc.restart_app()
        self.fc.maximize_window()    
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        rgb_keyword_text = self.fc.fd["devices"].verify_rgb_keyword()
        assert rgb_keyword_text == "RGB Keyboard Action Item","RGB keyboard is not visible at PC Device - {}".format(rgb_keyword_text)
        self.fc.fd["devices"].click_rgb_keyword()
        self.fc.fd["devices"].click_pc_device_title_from_rgb_keyboard_title()
        rgb_keyword_text = self.fc.fd["devices"].verify_rgb_keyword()
        assert rgb_keyword_text == "RGB Keyboard Action Item","RGB keyboard is not visible at PC Device - {}".format(rgb_keyword_text)


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_stack(["production"])
    @pytest.mark.require_platform(["grogu","london"])
    def test_06_click_on_the_programmable_Key_card_under_the_action_title_C32313083(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)
        self.fc.fd["devices"].click_programmable_key()
        self.fc.fd["devices"].click_pc_device_title_from_programmable_key_title()
        programmable_key_text = self.fc.fd["devices"].verify_programmable_key()
        assert programmable_key_text == "Programmable Key Action Item","Programmable Key is not visible at PC Device - {}".format(programmable_key_text)

    @pytest.mark.require_stack(["production"])
    def test_07_click_on_the_support_card_under_the_action_title_C32313086(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        support_text = self.fc.fd["devices"].verify_support_action_card()
        assert support_text == "Support","Support is not visible at PC Device - {}".format(support_text)
        self.fc.fd["devices"].click_support_btn()
        self.fc.fd["devices"].click_back()
        support_text = self.fc.fd["devices"].verify_support_action_card()
        assert support_text == "Support","Support is not visible at PC Device - {}".format(support_text)

    @pytest.mark.require_platform(["grogu","london","willie"])
    @pytest.mark.require_stack(["production"])
    def test_08_click_on_display_control_card_under_the_action_title_C32871667(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)
        self.fc.fd["devices"].click_display_control()
        self.fc.fd["devices"].click_pc_device_title_from_display_title()
        display_control_text = self.fc.fd["devices"].verify_display_control()
        assert display_control_text == "Display Control Action Item","Display Control is not visible at PC Device - {}".format(display_control_text)

    @pytest.mark.require_stack(["production"])
    def test_09_title_bar_operations_C32313097(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].maximize_app()
        self.fc.fd["devices"].minimize_app()
        self.fc.launch_app()
        self.fc.fd["devices"].close_app()

    @pytest.mark.require_stack(["production"])
    def test_10_presence_of_element_on_pcdevicepage_C32313079(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        assert bool(self.fc.fd["devices"].verify_presenceOf_custom_deviceName()) is True
        assert bool(self.fc.fd["devices"].verify_presenceOf_actionItems()) is True


    @pytest.mark.require_stack(["production"])
    def test_11_presence_of_image_on_pcdevicepage_C32629335(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        assert bool(self.fc.fd["devices"].verify_presenceOf_image_devicepage()) is False


    @pytest.mark.require_stack(["production"])
    def test_12_presence_of_header_icon_on_pcdevicepage_C33693995(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        assert bool(self.fc.fd["devices"].verify_presenceOf_info_icon_devicepage()) is True
        assert bool(self.fc.fd["devices"].verify_presenceOf_batteryIcon()) is True


    @pytest.mark.require_stack(["production"])
    def test_13_verify_devicename_leftnav_name_on_pcdevicepage_C33827785(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        pc_Device_Menu_text = self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        deviceName_text=self.fc.fd["devices"].get_custom_devicename_text()
        assert pc_Device_Menu_text == deviceName_text


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_stack(["production"])
    def test_14_tooltip_of_productnumber_on_pcdevicepage_C34220155(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_info_icon_devicepage()
        self.fc.fd["devices"].click_on_productnumber()
        self.fc.fd["devices"].click_productnumber_value_tooltip()
        expected_productnumber_tooltip_text = "Copied"
        actual_productnumber_tooltip_text = self.fc.fd["devices"].get_productnumber_value_tooltip_text()
        assert actual_productnumber_tooltip_text == expected_productnumber_tooltip_text
        assert bool(self.fc.fd["devices"].verify_presenceof_productnumber_tooltip()) is True


    @pytest.mark.require_stack(["production"])
    def test_15_tooltip_of_serialnumber_on_pcdevicepage_C34220245(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_info_icon_devicepage()
        self.fc.fd["devices"].click_serialnumber_value_tooltip()
        expected_serialnumber_tooltip_text = "Copied"
        actual_serialnumber_tooltip_text = self.fc.fd["devices"].get_serialnumber_value_tooltip_text()
        assert actual_serialnumber_tooltip_text == expected_serialnumber_tooltip_text
        assert bool(self.fc.fd["devices"].verify_presenceof_serialnumber_tooltip()) is True


    @pytest.mark.require_stack(["production"])
    def test_16_tooltip_of_copybutton_on_pcdevicepage_C34220156(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_info_icon_devicepage()
        self.fc.fd["devices"].click_copyserialnumber_btn()
        self.fc.fd["devices"].click_copyserialnumber_btn_tooltip()
        expected_copyserialnumber_tooltip_text = "Copied"
        actual_copyserialnumber_tooltip_text = self.fc.fd["devices"].get_copyserialnumber_btn_tooltip_text()
        assert actual_copyserialnumber_tooltip_text == expected_copyserialnumber_tooltip_text
        assert bool(self.fc.fd["devices"].verify_presenceof_copyserialnumberbtn_tooltip()) is True
        self.fc.fd["devices"].click_copyproductnumber_btn()
        self.fc.fd["devices"].click_copyproductnumber_btn_tooltip()
        expected_copyproductnumber_tooltip_text = "Copied"
        actual_copyproductnumber_tooltip_text = self.fc.fd["devices"].get_copyproductnumber_btn_tooltip_text()
        assert actual_copyproductnumber_tooltip_text == expected_copyproductnumber_tooltip_text
        assert bool(self.fc.fd["devices"].verify_presenceof_copyproductnumberbtn_tooltip()) is True


    @pytest.mark.require_stack(["production"])
    def test_17_presence_of_items_info_icon_on_pcdevicepage_C33694128(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].verify_click_on_info_icon_devicepage()
        assert bool(self.fc.fd["devices"].verify_presenceOf_productnumber()) is True
        assert bool(self.fc.fd["devices"].verify_presenceOf_serialnumber()) is True
        assert bool(self.fc.fd["devices"].verify_presenceOf_copybtn_productnumber()) is True
        assert bool(self.fc.fd["devices"].verify_presenceOf_copybtn_serialnumber()) is True


    @pytest.mark.require_stack(["production"])
    def test_18_verify_batteryicon_on_pcdevicepage_C33694182(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].click_battery_tool_tip()
        time.sleep(3)
        actual_battery_tooltip_text = self.fc.fd["devices"].get_battery_tool_tip()
        output = re.search("([\w]{1,10})", actual_battery_tooltip_text).group(1)
        assert output != None


    @pytest.mark.require_stack(["production"])
    def test_19_verify_click_copy_productnumber_on_pcdevicepage_C35505922(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].verify_click_on_info_icon_devicepage()
        self.fc.fd["devices"].verify_click_on_productnumber_copyicon()
        expected_copyproductnumber_text = "CopyProductNumber"
        actual_copyproductnumber_text = self.fc.fd["devices"].get_copyproduct_number_text()
        assert actual_copyproductnumber_text == expected_copyproductnumber_text


    @pytest.mark.require_stack(["production"])
    def test_20_verify_click_copy_serialnumber_on_pcdevicepage_C35505921(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["devices"].verify_click_on_info_icon_devicepage()
        self.fc.fd["devices"].verify_click_on_serialnumber_copyicon()
        expected_copyserialnumber_text = "CopySerialNumber"
        actual_copyserialnumber_text = self.fc.fd["devices"].get_copyserial_number_text()
        assert actual_copyserialnumber_text == expected_copyserialnumber_text

