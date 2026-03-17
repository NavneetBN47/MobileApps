from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.keys import Keys

import time

class DockStation(HPXFlow):
    flow_name = "dock_station"

    def navigate_to_dock_station_page(self):
        self.driver.click("dock_station_module")

    def verify_dock_station_module_show(self):
        return self.driver.wait_for_object("dock_station_module", raise_e=False, timeout=10)
    
    def verify_dock_station_title_show(self):
        return self.driver.wait_for_object("dock_station_title", raise_e=False, timeout=10)
    
    def verify_dock_station_title_edit_button_show(self):
        return self.driver.wait_for_object("dock_station_title_edit_button", raise_e=False, timeout=10)

    def verify_dock_station_module_name_show(self):
        return self.driver.wait_for_object("dock_station_module_name", raise_e=False, timeout=10)

    def verify_dock_station_support_button_show(self):
        return self.driver.wait_for_object("dock_station_support_button", raise_e=False, timeout=10)
    
    def click_dock_station_support_button(self):
        self.driver.click("dock_station_support_button")

    def verify_dock_station_scroll_view_show(self):
        return self.driver.wait_for_object("dock_station_scroll_view_page", raise_e=False, timeout=10)
    
    def verify_dock_station_image_show(self):
        return self.driver.wait_for_object("dock_station_image", raise_e=False, timeout=10)

    def verify_dock_station_connection_button_show(self):
        return self.driver.wait_for_object("dock_station_connection_button", raise_e=False, timeout=10)
    
    def get_dock_station_connection_tooltips(self):
        return self.driver.get_attribute("dock_station_connection_button", "Name")

    def verify_dock_station_infor_button_show(self):
        return self.driver.wait_for_object("dock_station_infor_button", raise_e=False, timeout=10)
    
    def get_dock_station_name(self):
        return self.driver.get_attribute("dock_station_title", "Name")
    
    def get_dock_station_name_on_edit_status(self):
        return self.driver.get_attribute("dock_station_content", "Name")
    
    def set_new_dock_station_name(self, new_name):
        rename = self.driver.wait_for_object("dock_station_content", raise_e=False, timeout=10)
        for i in range(0, 12):
            rename.send_keys(Keys.BACK_SPACE)
        self.driver.send_keys("dock_station_content", new_name)
        rename.send_keys(Keys.ENTER)

    def set_special_dock_station_name(self, new_name):
        rename = self.driver.wait_for_object("dock_station_content", raise_e=False, timeout=10)
        for i in range(0, 12):
            rename.send_keys(Keys.BACK_SPACE)
        self.driver.send_keys("dock_station_content", new_name)

    def get_dock_station_name_on_navigation_panel(self):
        return self.driver.get_attribute("dock_station_module", "Name")
    
    def click_edit_button(self):
        self.driver.click("dock_station_title_edit_button")

    def click_clear_button(self):
        self.driver.click("dock_station_clear_button")

    def keep_default_dock_station_name(self, new_name):
        self.driver.send_keys("dock_station_title", new_name)
        rename = self.driver.wait_for_object("dock_station_title", raise_e=False, timeout=10)
        rename.send_keys(Keys.ENTER)
        time.sleep(2)
    
    def click_dock_station_connection_button(self):
        self.driver.click("dock_station_connection_button")
    
    def click_dock_station_infor_button(self):
        self.driver.click("dock_station_infor_button")
    
    def get_dock_station_serial_number(self):
        return self.driver.get_attribute("dock_station_serial_number", "Name")
    
    def get_dock_station_firmware_version(self):
        return self.driver.get_attribute("dock_station_firmware_version", "Name")
    
    def get_dock_station_support_button_text(self):
        return self.driver.get_attribute("dock_station_support_button", "Name")

    def get_dock_station_rename_error_message(self):
        return self.driver.get_attribute("dock_station_rename_error_message", "Name")

    def check_keyboard_focus_elements(self):
        elements = ["dock_station_content","dock_station_module_name1", "dock_station_connection_button1", "dock_station_infor_button", "dock_station_support_button"]
        for element in elements:
            new_element = self.driver.wait_for_object(element)
            new_element.send_keys(Keys.TAB)
            elements1 = ["dock_station_module_name1", "dock_station_connection_button1", "dock_station_infor_button", "dock_station_support_button", "bell_icon"]
            for element1 in elements1:
                self.driver.wait_for_object(element1)
                focus_status = self.driver.get_attribute(element1, "IsKeyboardFocusable")
                assert focus_status == "true",f"Element {element1} is not keyboard focusable"
    
    def verify_serial_number_dock_station(self):
        return self.driver.wait_for_object("serial_number_dock_station", raise_e=False, timeout=10)
    
    def verify_copy_icon_dock_station(self):
        return self.driver.wait_for_object("copy_icon_dock_station", raise_e=False, timeout=10)
    
    def verify_firmware_version_dock_station(self):
        return self.driver.wait_for_object("firmware_version_dock_station", raise_e=False, timeout=10)
    
    def click_copy_icon_dock_station(self):
        self.driver.click("copy_icon_dock_station")    

    def get_dock_station_rename_error_message(self):
        return self.driver.get_attribute("dock_station_rename_error_message", "Name")
    
    def get_firmware_version_dock_station(self):
        return self.driver.get_attribute("firmware_version_dock_station", "Name")

    def click_copy_icon_dock_station(self):
        self.driver.click("copy_icon_dock_station")

    def click_file_button_on_notepad(self):
        self.driver.click("file_button_on_notepad")

    def click_new_tab_on_notepad(self):
        self.driver.click("new_tab_on_notepad")

    def get_version_on_notepad(self):
        return self.driver.get_attribute("version_on_notepad", "Name")
    
    def click_paste_button_on_notepad(self):
        paste_place = self.driver.wait_for_object("version_paste_on_notepad")
        paste_place.send_keys(Keys.CONTROL, 'v')