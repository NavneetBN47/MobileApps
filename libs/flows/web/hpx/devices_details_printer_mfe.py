from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.keys import Keys
from time import sleep

class DevicesDetailsPrinterMFE(HPXFlow):
    flow_name = "devices_details_printer_mfe"


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_printer_device_page(self, _printer, timeout=10, raise_e=True):
        if self.driver.wait_for_object("top_back_btn", timeout=timeout, raise_e=False) is False:
            if self.driver.driver_type.lower() == "windows":
                self.driver.swipe(direction="up", distance=6)
            if raise_e:
                self.driver.wait_for_object("top_back_btn", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("top_back_btn", timeout=timeout, raise_e=raise_e)
        el = self.driver.wait_for_object("device_details_page_device_name", timeout=timeout)
        # Commenting out the line as HPXG-5808
        # assert 'My Printer' in el.text
        el = self.driver.wait_for_object("device_details_page_nick_name")
        assert _printer in el.text
        if not self.driver.wait_for_object("device_details_page_supply_levels", raise_e=False):
            el = self.driver.wait_for_object("main_webview_pane")
            el.click()
            return el.send_keys(Keys.CONTROL+"r")
        self.driver.wait_for_object("device_details_page_supply_levels", raise_e=raise_e)

    def verify_dialog_ok_btn(self, raise_e=True):
        return self.driver.wait_for_object("dialog_ok_btn", raise_e=raise_e)

    def verify_all_tiles_printer_device_page(self, timeout=2, raise_e=True, check_flag=True):
        """
        Verify all tiles are present on the printer device page.
        
        Args:
            timeout (int): Timeout for waiting for objects
            raise_e (bool): Whether to raise exception on failure
            check_flag (bool): If True, checks all tiles including optional ones
        """
        self.win_scroll_element("print_dashboard_tile",distance=1)
        
        # Core tiles that are always checked
        core_tiles = [
            "get_supplies_tile",
            "scan_tile",
            "print_pdfs_tile", 
            "print_photos_tile",
            "printables_tile",
            "print_dashboard_tile"
        ]
        
        # Additional tiles checked when check_flag is True
        additional_tiles = [
            "mobile_fax_tile",
            "shortcuts_tile", 
            "cloud_scans_tile"
        ]
        
        # Determine which tiles to check
        tiles_to_check = core_tiles + (additional_tiles if check_flag else [])
        
        # Check all tiles and collect results
        for tile in tiles_to_check:
            self.driver.wait_for_object(tile, timeout=timeout, raise_e=raise_e)

    def verify_tile_invisable(self, tile):
        assert self.driver.wait_for_object(tile, raise_e=False) is False

    def verify_scan_tile(self, raise_e=True):
        self.win_scroll_element("scan_tile_sub_string")
        return self.driver.wait_for_object("scan_tile", raise_e=raise_e) and \
                self.driver.wait_for_object("scan_tile_header", raise_e=raise_e) and \
                self.driver.wait_for_object("scan_tile_sub_string", raise_e=raise_e) and \
                self.driver.wait_for_object("scan_tile_icon", raise_e=raise_e)

    def verify_print_pdfs_tile(self, raise_e=True):
        self.win_scroll_element("print_pdfs_tile_icon")
        return self.driver.wait_for_object("print_pdfs_tile", raise_e=raise_e) and \
                self.driver.wait_for_object("print_pdfs_tile_header", raise_e=raise_e) and \
                self.driver.wait_for_object("print_pdfs_tile_sub_string", raise_e=raise_e) and \
                self.driver.wait_for_object("print_pdfs_tile_icon", raise_e=raise_e)
     
    def verify_print_photos_tile(self, raise_e=True):
        self.win_scroll_element("print_photos_tile_icon")
        return self.driver.wait_for_object("print_photos_tile", raise_e=raise_e) and \
                self.driver.wait_for_object("print_photos_tile_header", raise_e=raise_e) and \
                self.driver.wait_for_object("print_photos_tile_sub_string", raise_e=raise_e) and \
                self.driver.wait_for_object("print_photos_tile_icon", raise_e=raise_e)

    def verify_printables_tile(self, raise_e=True):
        self.win_scroll_element("printables_tile_header")
        return self.driver.wait_for_object("printables_tile", raise_e=raise_e) and \
                self.driver.wait_for_object("printables_tile_header", raise_e=raise_e) and \
                self.driver.wait_for_object("printables_tile_sub_string", raise_e=raise_e) and \
                self.driver.wait_for_object("printables_tile_icon", raise_e=raise_e)

    def verify_mobile_fax_tile(self, raise_e=True):
        self.win_scroll_element("mobile_fax_tile")
        return self.driver.wait_for_object("mobile_fax_tile", raise_e=raise_e) and \
                self.driver.wait_for_object("mobile_fax_tile_header", raise_e=raise_e) and \
                self.driver.wait_for_object("mobile_fax_tile_sub_string", raise_e=raise_e) and \
                self.driver.wait_for_object("mobile_fax_tile_icon", raise_e=raise_e)

    def verify_shortcuts_tile(self, raise_e=True):
        self.win_scroll_element("shortcuts_tile")
        return self.driver.wait_for_object("shortcuts_tile", raise_e=raise_e)  and \
                self.driver.wait_for_object("shortcuts_tile_sub_string", raise_e=raise_e) and \
                self.driver.wait_for_object("shortcuts_tile_icon", raise_e=raise_e)

    def verify_hp_cloud_scans_tile(self, raise_e=True):
        self.win_scroll_element("hp_cloud_scans_tile")
        return self.driver.wait_for_object("hp_cloud_scans_tile", raise_e=raise_e) and \
                self.driver.wait_for_object("hp_cloud_scans_tile_header", raise_e=raise_e) and \
                self.driver.wait_for_object("hp_cloud_scans_tile_sub_string", raise_e=raise_e) and \
                self.driver.wait_for_object("hp_cloud_scans_tile_icon", raise_e=raise_e)

    def verify_print_dashboard_tile(self, raise_e=True):
        self.win_scroll_element("print_dashboard_tile_header")
        return self.driver.wait_for_object("print_dashboard_tile", raise_e=raise_e) and \
                self.driver.wait_for_object("print_dashboard_tile_header", raise_e=raise_e) and \
                self.driver.wait_for_object("print_dashboard_tile_sub_string", raise_e=raise_e) and \
                self.driver.wait_for_object("print_dashboard_tile_icon", raise_e=raise_e)
                
    def verify_switch_back_to_hp_smart_button(self, raise_e=True):
        self.win_scroll_element("switch_back_to_hp_smart_button")
        return self.driver.wait_for_object("switch_back_to_hp_smart_button", raise_e=raise_e) and \
               self.driver.wait_for_object("switch_back_to_hp_smart_header", raise_e=raise_e) and \
               self.driver.wait_for_object("smart_app_image", raise_e=raise_e)
    
    def verify_diagnositcs_part(self, raise_e=True):
        self.win_scroll_element("diagnostics_title")
        return self.driver.wait_for_object("diagnostics_title", timeout=2, raise_e=raise_e)

    def verify_diagnose_and_fix_item(self, raise_e=True):
        if raise_e:
            self.win_scroll_element("diagnose_and_fix_text")
        return self.driver.wait_for_object("diagnose_and_fix_text", timeout=2, raise_e=raise_e)

    def verify_diagnostics_view_all_item(self, raise_e=True):
        if raise_e:
            self.win_scroll_element("diagnostics_view_all_btn")
        return self.driver.wait_for_object("diagnostics_view_all_btn", timeout=2, raise_e=raise_e)

    def verify_print_quality_tools_item(self, raise_e=True):
        if raise_e:
            self.win_scroll_element("print_quality_tools_text")
        return self.driver.wait_for_object("print_quality_tools_text", timeout=2, raise_e=raise_e)

    def verify_printer_settings_part(self, raise_e=True):
        if raise_e:
            self.win_scroll_element("printer_settings_title")
        return self.driver.wait_for_object("printer_settings_title", timeout=2, raise_e=raise_e)

    def verify_advanced_settings_item(self, raise_e=True):
        return self.driver.wait_for_object("advanced_settings_text", timeout=2, raise_e=raise_e)

    def verify_privacy_item(self, raise_e=True):
        return self.driver.wait_for_object("privacy_text", timeout=2, raise_e=raise_e)

    def verify_settings_view_all_item(self, raise_e=True):
        if raise_e:
            self.win_scroll_element("settings_view_all_btn", timeout=100) 
        return self.driver.wait_for_object("settings_view_all_btn", timeout=2, raise_e=raise_e)
    
    def verify_product_information_mfe(self):
        self.win_scroll_element("more_info_and_reports_listitem") 
        self.driver.wait_for_object("product_information_section", timeout=2)

    def verify_product_number_info(self, product_number):
        self.win_scroll_element("more_info_and_reports_listitem") 
        assert self.driver.wait_for_object("product_number_listitem", timeout=2).text == 'Product number'
        assert self.driver.wait_for_object("copy_product_number_btn", timeout=2).text == product_number

    def verify_serial_number_info(self, serial_number):
        self.win_scroll_element("more_info_and_reports_listitem")
        assert self.driver.wait_for_object("serial_number_listitem", timeout=2).text == 'Serial number'
        assert self.driver.wait_for_object("copy_serial_number_btn", timeout=2).text == serial_number

    def verify_network_discovery_name_info(self, printer_name):
        self.win_scroll_element("more_info_and_reports_listitem") 
        assert self.driver.wait_for_object("network_discovery_name_listitem", timeout=2).text == 'Network discovery name'
        self.driver.wait_for_object("network_discovery_name_sub_text", timeout=2)
        network_name_text = self.driver.wait_for_object("network_discovery_name_info", timeout=2).text
        assert printer_name in network_name_text

    def verify_warranty_status_info(self):
        self.win_scroll_element("more_info_and_reports_listitem")
        sleep(5)
        assert self.driver.wait_for_object("warranty_status_listitem", timeout=2).text == 'Warranty status'
        # "warranty_status_value" cannot be located
        # self.driver.wait_for_object("warranty_status_value", timeout=2)
        self.driver.wait_for_object("warranty_status_arrow", timeout=2)

    def verify_more_info_and_reports_info(self):
        self.win_scroll_element("more_info_and_reports_listitem") 
        sleep(5)
        assert self.driver.wait_for_object("more_info_and_reports_listitem", timeout=2).text == 'More information and reports'
        self.driver.wait_for_object("more_info_and_reports_arrow", timeout=2)
    
    def verify_get_info_btn(self):
        return self.driver.wait_for_object("get_info_btn") 

    def verfiy_hpx_title(self):
        return self.driver.wait_for_object("_shared_hpx_title_text").text
    
    def verfiy_hpx_version_on_title(self):
        return self.driver.wait_for_object("_shared_app_version_text").text

    def verfiy_back_btn_text(self):
        assert self.driver.wait_for_object("top_back_btn").text == 'My Printer'
    
    def verify_remove_from_app_button(self):
        self.driver.send_keys("windows_app_pane", Keys.END)
        return self.driver.wait_for_object("remove_from_app_button")
    
    def verify_confirmation_dialog(self, raise_e=True):
        return self.driver.wait_for_object("cancel_button", raise_e=raise_e) and \
               self.driver.wait_for_object("remove_button", raise_e=raise_e)
    
    def verify_view_all_button(self, raise_e=True, timeout=60):
        if self.driver.wait_for_object("settings_view_all_btn", timeout=5, raise_e=False) is False and self.driver.driver_type.lower() == "windows":
            self.driver.scroll_element("settings_view_all_btn", direction="down", distance=4, time_out=timeout)
        self.driver.wait_for_object("settings_view_all_btn", timeout=5, raise_e=raise_e)
        

    def verify_sign_in_btn(self, raise_e=True):
        if self.driver.driver_type.lower() == "windows":
            self.driver.swipe(direction="up", distance=6)
        return self.driver.wait_for_object("sign_in_btn", raise_e=raise_e)

    def verify_privacy_option_is_hidden(self):
        self.win_scroll_element("printer_settings_title", timeout=20)
        return not self.driver.wait_for_object("privacy_arrow", raise_e=False)
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_top_back_btn(self, raise_e=True):
        if self.driver.driver_type.lower() == "windows":
            self.driver.swipe(direction="up", distance=10)
        return self.driver.click("top_back_btn", change_check={"wait_obj": "top_back_btn", "invisible": True}, retry=3, delay=1, raise_e=raise_e)
    
    def click_print_photos_tile(self):
        self.win_scroll_element("print_photos_tile_icon")
        if self.driver.click("print_photos_tile_icon", change_check={"wait_obj": "file_name_combo_box_edit", "flow_change": "print"}, retry=3, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("print_photos_tile_icon", timeout=2)
            el.send_keys(Keys.ENTER)

    def click_printables_tile(self):
        self.win_scroll_element("printables_tile_header")
        self.driver.click("printables_tile")

    def click_hp_cloud_scans_tile(self):
        self.win_scroll_element("hp_cloud_scans_tile")
        self.driver.click("hp_cloud_scans_tile")

    def click_copy_product_number_btn(self):
        return self.driver.click("copy_product_number_btn")
    
    def click_copy_serial_number_btn(self):
        return self.driver.click("copy_serial_number_btn")
    
    def click_get_info_btn(self):
        return self.driver.click("get_info_btn")
        
    def click_scan_tile(self):
        self.verify_scan_tile()
        return self.driver.click("scan_tile", change_check={"wait_obj": "scan_tile", "invisible": True}, retry=3, delay=1)
    
    def click_shortcuts_tile(self):
        self.verify_shortcuts_tile()
        self.driver.click("shortcuts_tile", change_check={"wait_obj": "shortcuts_tile", "invisible": True}, retry=3, delay=1)
    
    def click_mobile_fax_tile(self):
        self.verify_mobile_fax_tile()
        self.driver.click("mobile_fax_tile", change_check={"wait_obj": "mobile_fax_tile", "invisible": True}, retry=3, delay=1)
        
    def click_print_pdfs_tile(self):
        self.win_scroll_element("print_pdfs_tile_icon")
        if self.driver.click("print_pdfs_tile", change_check={"wait_obj": "file_name_combo_box_edit", "flow_change": "print"}, retry=3, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("print_pdfs_tile", timeout=2)
            el.send_keys(Keys.ENTER)
    
    def click_print_dashboard(self, direction="down"):
        self.win_scroll_element("print_dashboard_tile_header", direction=direction)
        self.driver.click("print_dashboard_tile")

    def click_supply_levels_link(self):
        self.driver.click("device_details_page_supply_levels")

    def click_door_open_sms_btn(self):
        self.driver.click("door_open_sms_btn")

    def click_dialog_ok_btn(self):
        return self.driver.click("dialog_ok_btn")

    def click_sign_in_btn(self):
        return self.driver.click("sign_in_btn")

    def click_remove_from_app_button(self):
        self.driver.click("remove_from_app_button", change_check={"wait_obj": "cancel_button"}, retry=3, delay=1)

    def click_cancel_button(self):
        self.driver.click("cancel_button", change_check={"wait_obj": "cancel_button", "invisible": True}, retry=3, delay=1)

    def click_remove_button(self):
        self.driver.click("remove_button")

    def click_view_all_button(self, retry=2):
        self.win_scroll_element("settings_view_all_btn")
        if self.driver.click("settings_view_all_btn", change_check={"wait_obj": "settings_view_all_btn", "invisible": True}, retry=retry, delay=1,  raise_e=False) is False:
            el = self.driver.wait_for_object("settings_view_all_btn", timeout=2)
            el.send_keys(Keys.ENTER)
        if self.driver.wait_for_object("find_printer_pin_dialog", timeout=5, raise_e=False):
            self.driver.click("sign_in_cancel_btn")

    def click_diagnostics_view_all_button(self, retry=2):
        self.win_scroll_element("diagnostics_view_all_btn")
        if self.driver.click("diagnostics_view_all_btn", change_check={"wait_obj": "diagnostics_view_all_btn", "invisible": True}, retry=retry, delay=1,  raise_e=False) is False:
            el = self.driver.wait_for_object("diagnostics_view_all_btn", timeout=2)
            el.send_keys(Keys.ENTER)

    def click_more_info_and_reports_listitem(self):
        self.driver.click("more_info_and_reports_listitem")

    def click_diagnose_and_fix_btn(self, retry=2):
        self.driver.click("diagnose_and_fix_text", change_check={"wait_obj": "diagnostics_title", "invisible": True}, retry=retry, delay=1)

    def click_print_quality_tools_btn(self, raise_e=True):
        self.driver.click("print_quality_tools_text", change_check={"wait_obj": "print_quality_tools_text", "invisible": True}, retry=2, delay=1)
    
    def close_feature_unavailable_popup(self, timeout=10):
        # HPXSUP-3801:[Support] [Rebrand] [Windows]"This feature is currently unavailable" shows on STG build because Methone Pro is disabled
        if self.driver.wait_for_object("feature_unavailable_text", raise_e=False, timeout=timeout):
            self.driver.click("dialog_ok_btn")

    def win_scroll_element(self, ele, direction="down", distance=4, timeout=120):
        if self.driver.wait_for_object(ele, timeout=2, raise_e=False) is False and self.driver.driver_type.lower() == "windows":
            self.driver.scroll_element(ele, direction=direction, distance=distance, time_out=timeout)
            self.driver.swipe(direction=direction, distance=distance)
            sleep(3)
