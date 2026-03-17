from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

class SystemPreferences(GothamFlow):
    flow_name = "system_preferences"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    # ----------------Windows Settings(Printers & Scanners)---------------- #
    def click_ps_big_plus_btn(self):
        self.driver.click("add_a_printer_or_scanner_btn")

    def click_ps_printer_list_item(self, num=1, timeout=60):
        self.driver.click("dynamic_add_printer_item", format_specifier=[num], timeout=timeout)

    def click_ps_printer_list_item_by_name(self, value_name, time_out=300):
        time_out = time.time() + time_out
        while time.time() < time_out:
            if self.driver.wait_for_object("add_printer_item_by_name", format_specifier=[value_name], raise_e=False, timeout=2):
                break
            self.driver.swipe(distance=3)
            sleep(1)
        self.driver.click("add_printer_item_by_name", format_specifier=[value_name])
        if not self.driver.wait_for_object("add_device_btn", raise_e=False, timeout=2):
            self.driver.swipe()

    def click_ps_add_device_btn(self):
        self.driver.click("add_device_btn")

    def click_ps_popup_add_btn(self):
        self.driver.click("popup_add_btn")

    def click_ps_open_printer_app_btn(self):
        self.driver.click("open_printer_app_btn", raise_e=False) 

    def click_ps_get_app_btn(self):
        self.driver.click("get_app_btn", raise_e=False) 

    def get_printer_info_text(self, num=1):
        return self.driver.get_attribute("dynamic_add_printer_item", format_specifier=[num], attribute="Name")

    def click_close_btn(self):
        self.driver.click("close_btn")

    # ----------------Microsoft Store(HP Smart)---------------- #   
    def click_ms_get_btn(self):
        self.driver.click("ms_get_btn", timeout=25)

    def click_ms_retry_btn(self):
        self.driver.click("ms_retry_btn", timeout=10)

    def click_ms_open_btn(self, raise_e=False):
        return self.driver.click("ms_open_btn", timeout=30, raise_e=raise_e)
    
    def verify_ms_progress_ring(self):
        self.driver.wait_for_object("ms_install_progress_ring", timeout=180, invisible=True)

    def click_ms_apps_item(self):
        self.driver.click("ms_apps_item")

    def edit_ms_search_box(self, search_app):
        self.driver.click("ms_search_box")
        sleep(2)
        self.driver.send_keys("ms_search_box", search_app, press_enter=True)
        self.driver.click("ms_hp_card")

    # ----------------Microsoft account dialog---------------- #     
    def edit_ms_username(self, username):
        self.driver.click("ms_username_edit")
        sleep(2)
        self.driver.send_keys("ms_username_edit", username)

    def click_ms_next_btn(self):
        self.driver.click("ms_next_btn")

    def edit_ms_password(self, password):
        self.driver.click("ms_password_edit")
        sleep(2)
        self.driver.send_keys("ms_password_edit", password)

    def click_ms_sign_in_btn(self):
        self.driver.click("ms_sign_in_btn")

    def click_ms_account_item(self):
        self.driver.click("ms_account_item")

    def click_ms_continue_btn(self):
        self.driver.click("ms_continue_btn")
    
    def click_ms_account_btn(self):
        self.driver.click("ms_account_btn")

    def click_ms_sign_out_btn(self):
        el = self.driver.wait_for_object("ms_sign_out_group")
        el.send_keys(Keys.ENTER)

    def click_ms_home_sign_in_btn(self):
        el = self.driver.wait_for_object("ms_sign_in_menu")
        el.send_keys(Keys.ENTER)

    # ----------------123.hp.com---------------- # 
    def enter_printer_name(self, printer_name):
        self.driver.click("web_enter_printer_name_edit")
        sleep(2)
        self.driver.send_keys("web_enter_printer_name_edit", printer_name)

    def select_a_printer(self):
        self.driver.click("web_printer_name")
    
    def click_web_next_btn(self):
        self.driver.click("web_next_btn")

    def click_web_install_hp_smart_btn(self):
        self.driver.click("web_install_hp_smart_btn")

    def click_web_open_ms_btn(self):
        el = self.driver.wait_for_object("web_open_ms_btn")
        el.send_keys(Keys.ENTER)

     # ----------------Windows Start--------------- #
    def extend_win_start_list(self):
        el = self.driver.wait_for_object("win_start_btn")
        el.send_keys(Keys.ENTER)

    def unextend_win_start_list(self):
        el = self.driver.wait_for_object("win_start_btn")
        el.send_keys(Keys.ESCAPE)

    def click_win_app_head_letter(self):
        self.driver.click("win_head_app_letter")

    def click_win_h_app_letter(self):
        self.driver.click("win_h_app_group")

    def right_click_win_hp_app_item(self):
        el = self.driver.wait_for_object("win_hp_smart_item")
        el.send_keys(Keys.SHIFT, Keys.F10)

    def click_win_app_uninstall_btn(self):
        self.driver.click("win_uninstall_btn")

    def click_win_app_uninstall_info_btn(self):
        self.driver.click("win_uninstall_info_btn")

    def click_win_hp_app_item(self):
        self.driver.click("win_hp_smart_item")

    def check_hp_app_exist(self, check_path):
        fh = self.driver.ssh.check_file(check_path)
        return fh

    def click_hp_smart_taskbar(self):
        self.driver.click("hp_smart_taskbar")

    # ----------------Toast Message---------------- # 
    def click_toast_message_launch_btn(self):
        self.driver.click("toast_launch_app_btn")
           
    # ********************************************************************************
    #                            VERIFICATION FLOWS                                  *
    # ********************************************************************************
    def verify_printer_scannerers_title(self):
        self.driver.wait_for_object("printer_scannerers_text")

    def verify_ps_big_plus_btn(self):
        self.driver.wait_for_object("add_a_printer_or_scanner_btn")

    def verify_ps_progress_bar(self):
        self.driver.wait_for_object("printer_add_progress_bar", timeout=60, invisible=True)

    def verify_ps_add_device_btn(self):
        self.driver.wait_for_object("add_device_btn")

    def verify_ps_open_printer_app_btn(self, raise_e=True):
        self.driver.swipe("add_a_printer_or_scanner_btn", direction="up")
        return self.driver.wait_for_object("open_printer_app_btn", timeout=120, raise_e=raise_e)

    def verify_ps_printer_ready_text(self, raise_e=True):
        self.driver.swipe("add_a_printer_or_scanner_btn", direction="up")
        return self.driver.wait_for_object("add_printer_item_by_name", format_specifier=["Ready"], timeout=120, raise_e=raise_e)

    def verify_ps_get_app_btn(self, raise_e=False):
        return self.driver.wait_for_object("get_app_btn", timeout=60, raise_e=raise_e)

    def verify_ps_popup_add_btn(self, raise_e=False):
        return self.driver.wait_for_object("popup_add_btn", timeout=60, raise_e=raise_e)

    def verify_ms_sign_in_dialog(self, raise_e=False):
        """
        Verify microsoft dialog
        """
        return self.driver.wait_for_object("ms_sign_in_dialog",timeout=20, raise_e=raise_e)
   
    def verify_ms_username_dialog(self, raise_e=False, invisible=False):
        """
        Verify microsoft dialog
        """
        return self.driver.wait_for_object("ms_username_edit", timeout=25, raise_e=raise_e, invisible=invisible)
        
    def verify_ms_password_dialog(self):
        """
        Verify microsoft dialog
        """
        return self.driver.wait_for_object("ms_password_edit",timeout=20)
    
    def verify_ms_continue_dialog(self, raise_e=False, invisible=False):
        """
        Verify microsoft dialog
        """
        return self.driver.wait_for_object("ms_continue_btn", timeout=25, raise_e=raise_e, invisible=invisible)

    def verify_ms_last_dialog(self, raise_e=False, invisible=False):
        """
        Verify microsoft dialog
        """
        return self.driver.wait_for_object("ms_next_btn", timeout=20, raise_e=raise_e, invisible=invisible)

    def verify_ms_display(self):
        """
        Verify Microsoft Store display
        """
        self.driver.wait_for_object("ms_home_control")

    def verify_ms_is_login(self, raise_e=False):
        """
        Verify Microsoft Store display
        """
        return self.driver.wait_for_object("ms_sign_out_group",timeout=25, raise_e=raise_e)

    def verify_ms_is_logout(self):
        """
        Verify Microsoft Store display
        """
        self.driver.wait_for_object("ms_sign_in_menu")

    def verify_ms_retry_btn(self, raise_e=False):
        return self.driver.wait_for_object("ms_retry_btn", timeout=10, raise_e=raise_e)

    def verify_network_status_page(self):
        self.driver.wait_for_object("network_status_text")

    # ----------------123.hp.com---------------- # 

    def verify_123_hp_webpage(self, timeout=20):
        """
        Verify 123.hp.com webpage
        """
        self.driver.send_keys("web_edit_bar", "www.123.hp.com", press_enter=True)
        self.driver.wait_for_object("web_next_btn", timeout=timeout)

    def verify_printer_name_list(self, raise_e=False):
        """
        Verify 123.hp.com webpage
        """
        return self.driver.wait_for_object("web_printer_name_list", raise_e=raise_e)

    def verify_install_hp_smart_webpage(self, raise_e=False):
        """
        Verify 123.hp.com webpage
        """
        return self.driver.wait_for_object("web_install_hp_smart_btn", raise_e=raise_e)

    def verify_open_ms_dialog(self, raise_e=False):
        """
        Verify 123.hp.com webpage
        """
        return self.driver.wait_for_object("web_open_ms_btn", raise_e=raise_e, timeout=20)

    # ----------------Windows Start--------------- #
    def verify_win_start_display(self, raise_e=False):
        """
        Verify Win Start launched
        """
        return self.driver.wait_for_object("win_app_list", raise_e=raise_e)

    def verify_win_h_letter_display(self, raise_e=False):
        """
        Verify Win Start h letter
        """
        return self.driver.wait_for_object("win_h_app_letter", raise_e=raise_e)

    def verify_win_hp_right_opt_display(self):
        """
        Verify Win Start -> letters -> H ->right click
        """
        self.driver.wait_for_object("win_uninstall_btn")

    def verify_win_app_uninstall_info_dialog(self, raise_e=False, timeout=25):
        """
        Verify Win Start -> letters -> H -> right click -> uninstall-> uninstall
        """
        return self.driver.wait_for_object("win_uninstall_info_btn", raise_e=raise_e, timeout=timeout)

    def verify_hp_smart_pin_to_start(self):
        """
        Verify HP Smart pin to start
        """
        self.driver.wait_for_object("pinned_hp_smart_listitem")
    
    # ----------------Toast Message---------------- # 
    def verify_win_toast_message(self, raise_e=False, timeout=25):
        """
        Install printer on Win Settings
        """
        return self.driver.wait_for_object("toast_launch_app_btn", raise_e=raise_e, timeout=timeout)
    
    # ----------------Win Settings---------------- # 
    def verify_win_printers_and_scanners_screen(self):
        """
        Printers & Scanners
        """
        self.driver.wait_for_object("win_settints_printers_and_scanners")
    