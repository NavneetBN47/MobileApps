import logging
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow

class Accessibility(HPXRebrandingFlow):
    flow_name = "accessibility"

########################### Verification Methods ################################
    def dismiss_open_windows_overlays(self):
        """Dismiss any open Windows overlays (Start menu, search box)"""
        toggle_state_windows_btn = self.driver.get_attribute("start_menu_window_btn", "Toggle.ToggleState")
        if toggle_state_windows_btn == "1":
            logging.info("Start menu is open, closing it")
            self.driver.click("start_menu_window")

        toggle_state_search_btn = self.driver.get_attribute("search_bar_on_windows", "Toggle.ToggleState")
        if toggle_state_search_btn == "1":
            logging.info("Search box is open, closing it")
            self.driver.click("start_menu_window")
            self.driver.click("start_menu_window")
        logging.info("Desktop state prepared - overlays closed")

    def click_start_menu_button(self):
        self.driver.wait_for_object("start_menu_window_btn")
        self.driver.click("start_menu_window_btn")

    def click_apps_button(self):
        self.driver.wait_for_object("apps_button")
        self.driver.click("apps_button")

    def click_installed_apps_button(self):
        self.driver.wait_for_object("installed_apps_button")
        self.driver.click("installed_apps_button")

    def click_search_for_installed_apps(self):
        self.driver.wait_for_object("search_bar_for_apps")
        self.driver.click("search_bar_for_apps")
        self.driver.send_keys("search_bar_for_apps", "HP")

    def verify_hp_app_icon_in_windows_settings(self):
        self.driver.scroll_element("HP_apps_icon")
        return self.driver.wait_for_object("HP_apps_icon")

    def click_hp_app_icon_in_windows_settings(self):
        self.driver.wait_for_object("HP_apps_icon")
        self.driver.click("HP_apps_icon")

    def verify_myhp_app_icon_on_taskbar(self):
        self.driver.wait_for_object("myhp_app_icon_on_taskbar")

    def click_library_button_on_msstore(self):
        self.driver.click("library_button_on_msstore", timeout=30)

    def click_myhp_app_icon_on_taskbar(self):
        self.driver.click("myhp_app_icon_on_taskbar")

    def hover_to_maximize_button(self):
        self.driver.hover("maximize_button")
        self.driver.wait_for_object("maximize_button")

    def verify_myhp_pinned_to_start_menu(self):
        self.click_start_menu_button()
        self.driver.wait_for_object("myhp_app_icon_on_start_menu")
        self.click_start_menu_button()

    def click_unpin_hp_from_start_menu(self):
        if self.driver.wait_for_object("unpin_hp_from_start_menu"):
            self.driver.click("unpin_hp_from_start_menu")

    def verify_scroll_bar(self):
        self.driver.wait_for_object("scroll_bar")

    def click_scroll_bar(self):
        self.driver.click("scroll_bar", timeout=10)

    def refresh_btn_is_disabled(self):
        if self.driver.wait_for_object("refresh_button", raise_e=False):
            return True
        else:
            return False
