import logging
import time
from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction



class Devices(HPXFlow):
    flow_name = "devices"

    def click_pc_devices(self):
        self.driver.click("pc_devices_module", timeout=20)

    def click_pen_control(self):
        self.driver.click("pen_control_module")

    def click_keyboard(self):
        self.driver.click("keyboard_module")

    def click_mouse(self):
        self.driver.click("mouse_module")

    def verify_actions_header(self):
        return self.driver.wait_for_object("actions_header")

    def verify_pen_control(self):
        return self.driver.get_attribute("pen_control_module", "Name")

    def verify_audio_control(self):
        return self.driver.get_attribute("Audio_Control_Display", "Name")

    def click_audio_control(self):
        return self.driver.click("Audio_Control_Display")

    def verify_video_control(self):
        return self.driver.get_attribute("Video_Control_Display", "Name")

    def click_video_control(self):
        return self.driver.click("Video_Control_Display")

    def close_hp_video_app(self):
        if "HPPresenceVideo" in self.driver.ssh.send_command("tasklist.exe")["stdout"]:
            self.driver.ssh.send_command(
                'powershell taskkill /f /im HPPresenceVideo.exe')
        if "HPEnhancedCamera" in self.driver.ssh.send_command("tasklist.exe")["stdout"]:
            self.driver.ssh.send_command(
                'powershell taskkill /f /im HPEnhancedCamera.exe')

    def verify_rgb_keyword(self):
        return self.driver.get_attribute("RGB_keyboard", "Name")

    def click_rgb_keyword(self):
        self.driver.click("RGB_keyboard")

    def verify_programmable_key(self):
        return self.driver.get_attribute("prog_key_card", "Name")

    def click_programmable_key(self):
        self.driver.click("Programmable_Key")

    def click_support_action_card(self):
        self.driver.click("Support")

    def verify_support_action_card(self):
        return self.driver.get_attribute("Support", "Name")

    def click_back(self):
        self.driver.click("Back_Arrow")

    def click_display_control(self):
        self.driver.click("Display_control", raise_e=False, timeout=15)

    def verify_display_control(self):
        return self.driver.get_attribute("Display_control", "Name", raise_e=False, timeout=30)

    def click_pc_devices_back_button(self):
        self.driver.click("pc_devices_back_button")

    def maximize_app(self):
        self.driver.click("Maximize_myHP")

    def restore_app(self):
        self.driver.click("Restore_myHP")

    def minimize_app(self):
        if(self.driver.wait_for_object("Minimize", raise_e=False, timeout=10) is True):
            self.driver.click("Minimize")

    def close_app(self):
        self.driver.click("Close_myHP" , timeout = 10)

    def get_pcdevice_text(self):
        return self.driver.wait_for_object("pc_devices_module").get_attribute("Name")
    
    def verify_pc_device_module_show_on_global_navigation(self):
        return self.driver.wait_for_object("pc_devices_module", raise_e=False, timeout=10)
    
    def verify_pc_device_module_show_on_global_navigation_panel(self):
        return self.driver.wait_for_object("devices_module", raise_e=False, timeout=10)

    def get_rgb_title_text(self):
        return self.driver.wait_for_object("RGB_keyboard_title").get_attribute("Name")

    def get_select_keyboard_text(self):
        return self.driver.wait_for_object("select_keyboard_text").get_attribute("Name")

    def get_support_title_text(self):
        return self.driver.wait_for_object("support_card").get_attribute("Name")

    def get_option_text(self):
        return self.driver.wait_for_object("option_text").get_attribute("Name")

    def get_product_number_text(self):
        return self.driver.wait_for_object("Product_number").get_attribute("Name")

    def get_serial_number_text(self):
        return self.driver.wait_for_object("Serial_number").get_attribute("Name")

    def get_warranty_text(self):
        return self.driver.wait_for_object("Warranty").get_attribute("Name")

    def get_unknown_text(self):
        return self.driver.wait_for_object("Unknown").get_attribute("Name")

    def click_pc_device_title(self):
        self.driver.click("pc_device_title")

    def click_support_btn(self):
        self.driver.click("support_btn")

    def click_audio_card_on_pcdevice(self):
        return self.driver.click("audio_card_on_pcdevice",timeout=20)

    def get_audio_control_text_on_card(self):
        return self.driver.wait_for_object("audio_control_text_on_card").get_attribute("Name")

    def get_audio_descrip_text_on_card(self):
        return self.driver.wait_for_object("audio_descrip_text_on_card").get_attribute("Name")

    def click_pc_device_title_from_audio_title(self):
        self.driver.click("pc_devices_back_button_from_audio_title_bar")


    def click_display_control_card_pcdevice(self):
        self.driver.wait_for_object("display_control_card", raise_e=False, timeout=30)
        self.driver.click("display_control_card")

    def verify_product_number(self):
        return self.driver.wait_for_object("Product_number", raise_e=False, timeout=2)

    def verify_serial_number(self):
        return self.driver.wait_for_object("Serial_number", raise_e=False, timeout=2)

    def verify_warranty(self):
        return self.driver.wait_for_object("Warranty", raise_e=False, timeout=2)

    def verify_audio_card_visible(self):
        return self.driver.wait_for_object("audio_card_on_pcdevice", raise_e=False, timeout=2)

    def verify_RGB_card_visible(self):
        return self.driver.wait_for_object("RGB_keyboard", raise_e=False, timeout=2)

    def verify_support_card_visible(self):
        return self.driver.wait_for_object("support_card", raise_e=False, timeout=2)

    def verify_display_card_visible(self):
        return self.driver.wait_for_object("display_card", raise_e=False, timeout=2)

    def get_display_control_text(self):
        return self.driver.wait_for_object("display_control_card").get_attribute("Name")

    def get_display_control_des_text(self):
        return self.driver.wait_for_object("display_control_des_txt").get_attribute("Name")

    def verify_HPPK_card_visible(self):
        return self.driver.wait_for_object("prog_key_card", raise_e=False, timeout=2)

    def get_prog_key_text(self):
        return self.driver.wait_for_object("prog_key_card").get_attribute("Name")

    def get_prog_key_des_text(self):
        return self.driver.wait_for_object("prog_key_des_text").get_attribute("Name")

    def verify_5G_card_visible(self):
        return self.driver.wait_for_object("5g_card", raise_e=False, timeout=2)
    
    def click_5g_card(self):
        self.driver.click("5g_card")

    def get_5g_text(self):
        return self.driver.wait_for_object("5g_text").get_attribute("Name")

    def get_5g_des_text(self):
        return self.driver.wait_for_object("5g_des_text").get_attribute("Name")

    def verify_video_control_card_visible(self):
        return self.driver.wait_for_object("video_control_card", raise_e=False, timeout=2)
    
    def click_video_control_card(self):
        self.driver.click("video_control_card")

    def get_video_control_text(self):
        return self.driver.wait_for_object("video_control_text").get_attribute("Name")

    def get_video_control_des_text(self):
        return self.driver.wait_for_object("video_control_des_text").get_attribute("Name")
    
    def verify_get_details(self):
        return self.driver.wait_for_object("get_details", raise_e=False, timeout=2)

    def get_get_detials_text(self):
        return self.driver.wait_for_object("get_details_text").get_attribute("Name")
    
    def verify_audio_card_pcdevice(self):
        return self.driver.wait_for_object("audio_card_on_pcdevice", raise_e=False, timeout=20)

    def verify_presenceOf_custom_deviceName(self):
        return self.driver.wait_for_object("devicename_tooltips_on_pcdevice", raise_e=False, timeout=10)

    def verify_presenceOf_image_devicepage(self):
        return self.driver.wait_for_object("displayOf_image_on_pcdevice", raise_e=False, timeout=10)

    def verify_presence_info_icon_devicepage(self):
        return self.driver.wait_for_object("display_info_icon_on_pcdevice", raise_e=False, timeout=10)

    def verify_presenceOf_system_deviceName(self):
        return self.driver.wait_for_object("system_devicename_on_pcdevice", raise_e=False, timeout=10)

    def verify_presence_productnumber(self):
        return self.driver.wait_for_object("display_product_number_on_pcdevice", raise_e=False, timeout=10)

    def verify_presence_serialnumber(self):
        return self.driver.wait_for_object("display_serial_number_on_pcdevice", raise_e=False, timeout=10)

    def verify_presenceOf_batteryIcon(self):
        return self.driver.wait_for_object("displayOf_battery_icon_on_pcdevice", raise_e=False, timeout=10)

    def verify_presenceOf_actionItems(self):
        return self.driver.wait_for_object("displayOf_action_items_on_pcdevice", raise_e=False, timeout=10)
    
    def verify_privacy_alert(self):
        return self.driver.wait_for_object("privacy_alert_card", raise_e=False, timeout=5) is not False

    def get_privacy_alert_text(self):
        return self.driver.wait_for_object("privacy_alert_card").get_attribute("Name")

    def get_privacy_alert_des_text(self):
        return self.driver.wait_for_object("privacy_alert_description_text").get_attribute("Name")

    def verify_auto_screen_dimming(self):
        return self.driver.wait_for_object("auto_screen_dimming_card", raise_e=False, timeout=5)

    def get_auto_screen_dimming_text(self):
        return self.driver.wait_for_object("auto_screen_dimming_card").get_attribute("Name")

    def get_auto_screen_dimming_des_text(self):
        return self.driver.wait_for_object("auto_screen_dimming_description_text").get_attribute("Name")

    def click_get_details(self):
        self.driver.click("get_details")

    def get_allow_personalized_support_get_details_text(self):
        return self.driver.wait_for_object("allow_personalized_support_get_details").get_attribute("Name")

    def get_detail_text_on_personalized_support_text(self):
        return self.driver.wait_for_object("detail_text_on_personalized_support").get_attribute("Name")

    def get_view_data_collected_link_text(self):
        return self.driver.wait_for_object("view_data_collected_link").get_attribute("Name")

    def get_yes_text(self):
        return self.driver.wait_for_object("yes_btn_personalized_support").get_attribute("Name")

    def click_pc_device_title_from_video_title(self):
        self.driver.click("pc_devices_back_button_from_video_title_bar")

    def click_pc_device_title_from_programmable_key_title(self):
        self.driver.click("pc_devices_back_button_from_programmable_key_title_bar")

    def click_pc_device_title_from_display_title(self):
        self.driver.click("pc_devices_back_button_from_display_title_bar")

    def click_pc_device_title_from_rgb_keyboard_title(self):
        self.driver.click("pc_devices_back_button_from_rgb_keyboard_title_bar")

    def get_no_text(self):
        return self.driver.wait_for_object("no_btn_personalized_support").get_attribute("Name")

    def click_view_data_collected_link(self):
        self.driver.click("view_data_collected_link")

    def get_about_title_text(self):
        return self.driver.wait_for_object("warranty_status_title_text_in_view_data").get_attribute("Name")

    def get_para1_in_view_data_window_text(self):
        return self.driver.wait_for_object("para1_in_view_data_window").get_attribute("Name")

    def get_para2_in_view_data_window_text(self):
        return self.driver.wait_for_object("para2_in_view_data_window").get_attribute("Name")

    def get_para3_in_view_data_window_text(self):
        return self.driver.wait_for_object("para3_in_view_data_window").get_attribute("Name")

    def get_para4_in_view_data_window_text(self):
        return self.driver.wait_for_object("para4_in_view_data_window").get_attribute("Name")

    def get_why_should_text(self):
        return self.driver.wait_for_object("why_should_text").get_attribute("Name")

    def get_authorized_para_text(self):
        return self.driver.wait_for_object("authorized_para_text").get_attribute("Name")

    def selection_this_option_text(self):
        return self.driver.wait_for_object("selection_this_option_text").get_attribute("Name")

    def selection_involve_text(self):
        return self.driver.wait_for_object("selection_involve_text").get_attribute("Name")

    def yes_text_under_involve_text(self):
        return self.driver.wait_for_object("yes_text_under_involve").get_attribute("Name")

    def get_change_text(self):
        return self.driver.wait_for_object("change_text").get_attribute("Name")

    def get_preference_text(self):
        return self.driver.wait_for_object("preference_text").get_attribute("Name")

    def click_close_warranty(self):
        self.driver.click("close_btn_warranty")

    def click_no(self):
        self.driver.click("no_btn_personalized_support")

    def get_custom_devicename_text(self):
        return self.driver.wait_for_object("devicename_tooltips_on_pcdevice").get_attribute("Name")

    def get_device_name_text(self):
        return self.driver.wait_for_object("devicename_on_pcdevice", timeout=40).get_attribute("Name")
    
    def verify_device_name_show_on_device_page_header(self):
        return self.driver.wait_for_object("devicename_on_pcdevice", raise_e=False, timeout = 15) is not False
        
    def verify_cellular(self):
        return self.driver.wait_for_object("cellular", raise_e=False, timeout=5)
    
    def get_cellular_text(self):
        return self.driver.wait_for_object("cellular").get_attribute("Name")
    
    def click_cellular_icon(self):
        self.driver.click("cellular", timeout = 10)
    
    def get_display_product_number_on_pcdevice(self):
        return self.driver.wait_for_object("infor_ProductNumber_name_show_on_device").get_attribute("Name")
    
    def get_display_serial_number_on_pcdevice(self):
        return self.driver.wait_for_object("infor_SerialNumber_name_show_on_device").get_attribute("Name")
    
    def verify_warranty_under_info_icon(self):
        return self.driver.wait_for_object("warranty_under_info_icon", raise_e=False, timeout=5)
    
    def get_verify_warranty_under_info_icon(self):
        return self.driver.wait_for_object("warranty_under_info_icon").get_attribute("Name")
    
    def click_prog_key_card(self):
        self.driver.click("prog_key_card", timeout = 10)
    
    def verify_disconnected_text(self):
        return self.driver.wait_for_object("disconnected_text", raise_e=False, timeout=5)
    
    def get_disconnected_text(self):
        return self.driver.wait_for_object("disconnected_text").get_attribute("Name")
    
    def verify_unknown_text_value(self):
        return self.driver.wait_for_object("unknown_text", raise_e=False, timeout=5) is not False
    
    def get_unknown_text(self):
        return self.driver.wait_for_object("unknown_text").get_attribute("Name")
    
    def verify_info_icon(self):
        return self.driver.wait_for_object("info_icon", raise_e=False, timeout=5)
    
    def verify_system_control_card(self):
        return self.driver.wait_for_object("system_control_card", raise_e=False, timeout=5)
    
    def get_system_control_text(self):
        return self.driver.wait_for_object("system_control_card").get_attribute("Name")
    
    def get_support_control_sub_text(self):
        return self.driver.wait_for_object("system_control_subtext").get_attribute("Name")
     
    def search_text(self,ele):
        max_time=20
        for time in range(0,max_time) :
            if(self.driver.wait_for_object(ele,invisible=False,raise_e=False)):
                break
            else:
                self.driver.swipe()
                continue
    
    def verify_window_maximize(self):
        self.driver.wait_for_object("Maximize_myHP", raise_e=False, timeout=20)
        return self.driver.get_attribute("Maximize_myHP","Name")

    def click_system_control_card(self):
        self.driver.click("system_control_card")

    def click_on_productnumber(self):
        self.driver.click("displayOf_product_number_on_pcdevice")

    def click_info_icon_devicepage(self):
        self.driver.click("displayOf_info_icon_on_pcdevice")

    def click_productnumber_value(self):
        self.driver.click("productnumber_value")

    def click_serialnumber_value_tooltip(self):
        self.driver.click("serialnumber_value_tooltip")

    def get_serialnumber_value_tooltip_text(self):
        return self.driver.wait_for_object("serialnumber_value_tooltip").get_attribute("Name")

    def verify_presenceof_serialnumber_tooltip(self):
        return self.driver.wait_for_object("serialnumber_value_tooltip", raise_e=False, timeout=10)

    def get_productnumber_value_tooltip_text(self):
        return self.driver.wait_for_object("productnumber_value_tooltip").get_attribute("Name")

    def click_productnumber_value_tooltip(self):
        self.driver.click("productnumber_value_tooltip", timeout = 10)

    def verify_presenceof_productnumber_tooltip(self):
        return self.driver.wait_for_object("productnumber_value_tooltip", raise_e=False, timeout=10)

    def click_copyserialnumber_btn_tooltip(self):
        self.driver.click("copyserialnumber_btn_tooltip")

    def click_copyserialnumber_btn(self):
        self.driver.click("copyserialnumber_btn")

    def get_copyserialnumber_btn_tooltip_text(self):
        return self.driver.wait_for_object("copyserialnumber_btn_tooltip").get_attribute("Name")

    def verify_presenceof_copyserialnumberbtn_tooltip(self):
        return self.driver.wait_for_object("copyserialnumber_btn_tooltip", raise_e=False, timeout=10)

    def click_copyproductnumber_btn_tooltip(self):
        self.driver.click("copyproductnumber_btn_tooltip")

    def click_copyproductnumber_btn(self):
        self.driver.click("copyproductnumber_btn")

    def get_copyproductnumber_btn_tooltip_text(self):
        return self.driver.wait_for_object("copyproductnumber_btn_tooltip").get_attribute("Name")

    def verify_presenceof_copyproductnumberbtn_tooltip(self):
        return self.driver.wait_for_object("copyproductnumber_btn_tooltip", raise_e=False, timeout=10)

    def click_privacy_alert(self):
        self.driver.click("privacy_alert_card")
    
    def click_battery_tool_tip(self):
        self.driver.click("battery_icon_on_device_page_header")
    
    def get_battery_tool_tip(self):
        return self.driver.get_attribute("battery_tool_tip","Name")
    
    def click_device_rename_on_pcdevice(self):
        return self.driver.wait_for_object("device_rename_icon_on_pcdevice", raise_e=False, timeout=10)
        
    def verify_presenceOf_info_icon_devicepage(self):
        return self.driver.wait_for_object("displayOf_info_icon_on_pcdevice", raise_e=False, timeout=10)

    def verify_presenceOf_productnumber(self):
        return self.driver.wait_for_object("displayOf_product_number_on_pcdevice", raise_e=False, timeout=10)
    
    def verify_presenceOf_serialnumber(self):
        return self.driver.wait_for_object("displayOf_serial_number_on_pcdevice", raise_e=False, timeout=10)
   
    def verify_presenceOf_warrantyInfo(self):
        return self.driver.wait_for_object("displayOf_warranty_info_on_pcdevice", raise_e=False, timeout=10)
    
    def verify_presenceOf_copybtn_serialnumber(self):
        return self.driver.wait_for_object("displayOf_copybtn_serialnumber_on_pcdevice", raise_e=False, timeout=10)
    
    def verify_presenceOf_copybtn_productnumber(self):
        return self.driver.wait_for_object("displayOf_copybtn_productnumber_on_pcdevice", raise_e=False, timeout=10)
    
    def verify_click_on_info_icon_devicepage(self):
        self.driver.click("displayOf_info_icon_on_pcdevice", timeout=20)

    def verify_click_on_product_number(self):
        self.driver.click("copy_productnumber")

    def verify_click_on_serial_number(self):
        self.driver.click("serial_productnumber")

    def verify_click_on_productnumber_copyicon(self):
        self.driver.click("displayOf_copybtn_productnumber_on_pcdevice")

    def verify_click_on_serialnumber_copyicon(self):
        self.driver.click("displayOf_copybtn_serialnumber_on_pcdevice", timeout=20)

    def get_copyproduct_number_text(self):
       return self.driver.get_attribute("displayOf_copybtn_productnumber_on_pcdevice","Name")

    def get_copyserial_number_text(self):
       return self.driver.get_attribute("displayOf_copybtn_serialnumber_on_pcdevice","Name")

    def click_auto_screen_dimming(self):
        self.driver.click("auto_screen_dimming")

    def verify_system_control_title(self):
        return self.driver.wait_for_object("system_control_text", raise_e=False, timeout=5)

    def verify_system_control_subtitle(self):
        return self.driver.wait_for_object("system_control_subtext", raise_e=False, timeout=5)

    def verify_touchpad_PCDevice_header(self):
        return self.driver.wait_for_object("touchpad_device_page_header", raise_e=False, timeout=20)
    
    def verify_touchpad_PCDevice_header_text(self):
        return self.driver.wait_for_object("touchpad_device_page_header_text", raise_e=False, timeout=20)
    
    def get_touchpad_PCDevice_header_text(self):
        return self.driver.wait_for_object("touchpad_device_page_header_text").get_attribute("Name")    
    
    def click_touchpad_header(self):
        self.driver.click("touchpad_device_page_header")
        
    def verify_modal_name_show_on_device_page_header(self):
        return self.driver.wait_for_object("modal_name_on_device_page_header", raise_e=False, timeout=20)
    
    def get_modal_name_show_on_device_page_header(self):
        return self.driver.wait_for_object("modal_name_on_device_page_header").get_attribute("Name")
    
    def verify_battery_icon_show_on_device_page_header(self):
        return self.driver.wait_for_object("battery_icon_on_device_page_header", raise_e=False, timeout=20)
    
    def get_battery_tooltips(self):
        return self.driver.wait_for_object("battery_tooltips_on_device_page_header").get_attribute("Name")
    
    def verify_infor_icon_show_on_device_page_header(self):
        return self.driver.wait_for_object("infor_icon_show_on_device_page_header", raise_e=False, timeout=40) is not False

    def click_infor_icon_on_device_page_header(self):
        self.driver.click("infor_icon_show_on_device_page_header", timeout=40)
        
    def verify_product_number_name_show_on_device_page_header(self):
        return self.driver.wait_for_object("infor_ProductNumber_name_show_on_device", raise_e=False, timeout=20)
    
    def verify_product_number_show_on_device_page_header(self):
        return self.driver.wait_for_object("infor_ProductNumber_show_on_device", raise_e=False, timeout=20)
    
    def verify_product_number_copy_icon_show_on_device_page_header(self):
        return self.driver.wait_for_object("infor_ProductNumber_copy_icon_show_on_device", raise_e=False, timeout=20)
    
    def verify_serial_number_name_show_on_device_page_header(self):
        return self.driver.wait_for_object("infor_SerialNumber_name_show_on_device", raise_e=False, timeout=20)
    
    def verify_serial_number_show_on_device_page_header(self):
        return self.driver.wait_for_object("infor_SerialNumber_show_on_device", raise_e=False, timeout=20)
    
    def verify_serial_number_copy_icon__show_on_device_page_header(self):
        return self.driver.wait_for_object("infor_SerialNumber_copy_icon_show_on_device", raise_e=False, timeout=20)
    
    def verify_pc_device_image_show_on_device_page(self):
        return self.driver.wait_for_object("pc_device_image_on_device_page", raise_e=False, timeout=20)
    
    def verify_audio_control_card_show_on_device_page(self):
        return self.driver.wait_for_object("audio_Control_card_on_device_page", raise_e=False, timeout=20)
    
    def verify_video_control_card_show_on_device_page(self):
        return self.driver.wait_for_object("video_Control_card_on_device_page", raise_e=False, timeout=20)
    
    def verify_display_control_card_show_on_device_page(self):
        return self.driver.wait_for_object("Display_control", raise_e=False, timeout=30)
    
    def verify_programmable_key_card_show_on_device_page(self):
        return self.driver.wait_for_object("prog_key_card", raise_e=False, timeout=20)
    
    def verify_5G_card_show_on_device_page(self):
        return self.driver.wait_for_object("5g_card", raise_e=False, timeout=20)
    
    def verify_support_card_show_on_device_page(self):
        return self.driver.wait_for_object("support_card", raise_e=False, timeout=20)
    
    def click_view_all_controls_link(self):
        self.driver.wait_for_object("view_all_controls_link", raise_e=False, timeout=20)
        self.driver.click("view_all_controls_link")
    
    def verify_view_all_controls_link_show(self):
        return self.driver.wait_for_object("view_all_controls_link", raise_e=False, timeout=20)
    
    
    def verify_pc_device_top_title_on_audio_module(self):
        return self.driver.wait_for_object("pc_devices_back_button_from_audio_title_bar", raise_e=False, timeout=20)
    
    def verify_pc_device_top_title_on_hppk_module(self):
        return self.driver.wait_for_object("pc_devices_back_button_from_programmable_key_title_bar", raise_e=False, timeout=20)
    

    def verify_touchpad_PCDevice_header_description(self):
        return self.driver.wait_for_object("touchpad_device_page_header_description", raise_e=False, timeout=20)
    
    def get_touchpad_PCDevice_header_description(self):
        return self.driver.wait_for_object("touchpad_device_page_header_description").get_attribute("Name")    
    
    def click_support_module_on_pc_device(self):
        self.driver.wait_for_object("support_btn",raise_e=False, timeout=20) 
        self.driver.click("support_btn", raise_e=False, timeout=10)
    
    def verify_pc_device_top_title_on_display_control_module(self):
        return self.driver.wait_for_object("pc_devices_back_button_from_display_title_bar", raise_e=False, timeout=20)
    
    def verify_pc_device_top_title_on_smartexp_module(self):
        return self.driver.wait_for_object("pc_devices_back_button_from_smartexp_title_bar", raise_e=False, timeout=20)
    
    def click_pc_device_title_from_smartexp_title(self):
        self.driver.click("pc_devices_back_button_from_smartexp_title_bar")
        
    def click_product_numder_under_infor_icon(self):
        self.driver.click("product_number_under_infor_icon")

    def click_serial_number_under_infor_icon(self):
        self.driver.click("serial_number_under_infor_icon")

    def get_serial_number_under_infor_icon(self):
        return self.driver.wait_for_object("serial_number_under_infor_icon").get_attribute("Name")
        
    def get_product_numder_under_infor_icon(self):
        return self.driver.wait_for_object("product_number_under_infor_icon").get_attribute("Name")
    
    def get_serial_number_copied_under_infor_icon(self):
        return self.driver.wait_for_object("infor_SerialNumber_copy_icon_show_on_device").get_attribute("Name")

    def click_devicename_for_back_PC_device_page(self):
        self.driver.click("devicename_for_back_PC_device_page")
    
    def get_privacy_alert_card_on_pcdevice(self):
        return self.driver.get_attribute("privacy_alert_card_on_pcdevice","Name")
    
    def get_auto_screen_dimming_card_on_pcdevice(self):
        return self.driver.get_attribute("auto_screen_dimming_card_on_pcdevice","Name")

    def verify_battery_manager_card(self):
        return self.driver.wait_for_object("battery_manager_action_item", raise_e=False, timeout=20)

    def click_devicename_for_text(self):
        self.driver.click("devicename_tooltips_on_pcdevice")

    def get_product_number_copied_under_infor_icon(self):
        return self.driver.wait_for_object("infor_ProductNumber_show_on_device").get_attribute("Name")
    
    def click_wi_fi_card(self):
        self.driver.click("wi-fi_card")

    def click_MyScan_card(self):
        self.driver.click("MyScan_card")
    
    def verify_Unknown_text(self):
        return self.driver.wait_for_object("Unknown", raise_e=False, timeout=5) is not False
    
    def click_for_battery_manager_card(self):
        self.driver.click("battery_manager_action_item")

    def verify_gesture_show_on_device_page(self):
        return self.driver.wait_for_object("gesture_card", raise_e=False, timeout=5) is not False
    
    def verify_wifi_sharing_show_on_device_page(self):
        return self.driver.wait_for_object("wifi_card_on_pc_device_page", raise_e=False, timeout=5) is not False
    
    def verify_screen_distance_card_on_pcdevice_page(self):
        return self.driver.wait_for_object("screen_distance_card", raise_e=False, timeout=5) is not False
    
    def click_screen_distance_card(self):
        self.driver.click("screen_distance_card")

    def verify_pc_device_is_selected_from_navbar(self):
        return self.driver.get_attribute("pc_devices_module", "SelectionItem.IsSelected", timeout = 20)

    def verify_presence_detection_card_on_pcdevice_page(self):
        return self.driver.wait_for_object("presence_detection_card", raise_e=False, timeout=10) is not False
    
    def click_presence_detection_card(self):
        self.driver.click("presence_detection_card", timeout = 10)

    def verify_presence_detection_text(self):
        return self.driver.get_attribute("presence_detection_text", "Name", timeout = 10)

    def verify_support_module_on_pc_device(self):
        return self.driver.wait_for_object("support_btn",raise_e=False, timeout=20)

    def verify_energy_consumption_card(self):
        return self.driver.wait_for_object("energy_consumption_card",raise_e=False, timeout=20)
