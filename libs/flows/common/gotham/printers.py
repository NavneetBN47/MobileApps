import time
from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
from selenium.common.exceptions import NoSuchElementException
import logging

class Printers(GothamFlow):
    flow_name = "printers"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_my_printer_isnt_listed_link(self):
        self.driver.click("my_printer_isnt_listed_link", timeout=20)

    def select_search_again_link(self):
        """
        Click the Search again link. The printer list will refresh.
        """
        search_again_link = self.driver.wait_for_object("search_again_link", raise_e=False, timeout=20)

        if search_again_link is not False:
            search_again_link.click()
        else:
            raise Exception("No search again link")

    def search_printer(self, keyword, beaconing_printer=False, value=True, raise_e=True):
        """
        Input the searching keyword in the search box,
        and then click on somewhere else(TopBar title here) to start searching.

        Return the specific printer element.
        """
        logging.info(f"Searching printer via: {keyword}")
        self.driver.click("search_box_text_box")
        if self.driver.send_keys("search_box_text_box", keyword, slow_type=True, check_key_sent=True, press_enter=True) is True:
            if value:
                if any(char.isalpha() for char in keyword):
                    if not beaconing_printer: 
                        return self.driver.wait_for_object("dynamic_printer_name_locator", format_specifier=[keyword], raise_e=raise_e)
                    else:
                        return self.driver.wait_for_object("dynamic_beaconing_printer_locator", format_specifier=[keyword], raise_e=raise_e)
                else:
                    return self.driver.wait_for_object("dynamic_printer_locator", format_specifier=[keyword], raise_e=raise_e)

    def select_remote_printer(self):
        self.driver.swipe("remote_printer_grid_view", distance=30)
        self.driver.click("dynamic_printer_locator", format_specifier=['Remote'])

    def select_network_printer(self, printer_name):
        self.driver.click("searched_network_printer", format_specifier=[printer_name])

    def select_set_up_printer(self, printer_name):
        self.driver.click("dynamic_beaconing_printer_locator", format_specifier=[printer_name])

    def click_continue_btn(self, check_kibana=False):
        if check_kibana:
            self.driver.click("turn_on_continue_btn")
        else:
            self.driver.click("continue_btn")

    def click_try_again_btn(self):
        self.driver.click("try_again_btn")

    def click_no_bluetooth_or_wifi_btn(self):
        self.driver.click("no_bluetooth_or_wifi_btn")

    def select_first_printer_item(self):
        self.driver.click("first_printer_item")

    def select_refresh_list_link(self):
        self.driver.click("refresh_list_link")

    # ---------------- pin dialog ---------------- #
    def input_pin(self, pin_number):
        return self.driver.send_keys("pin_block", pin_number)

    def select_pin_dialog_submit_btn(self):
        self.driver.click("pin_submit_btn")

    def select_pin_cancel_btn(self):
        self.driver.click("pin_cancel_btn")
    # ---------------- pin dialog ---------------- #

    # ---------------- printer setup ---------------- #
    def select_printer_setup_accept_all_btn(self):
        self.driver.click("printer_setup_accept_all_btn")
    # ---------------- printer setup ---------------- #

    def select_exit_setup(self):
        self.driver.click("exit_setup_btn")
    
    def select_pop_up_exit_setup(self):
        self.driver.click("popup_exit_setup_btn", timeout=20)

    def select_popup_back_btn(self):
        self.driver.click("popup_back_btn")

    def select_exit_setup_btn_on_dialog(self):
        self.driver.click("exit_setup_btn_on_dialog", timeout=20)

    def clear_search_box(self):
        # Only for test
        search_box = self.verify_search_box()
        self.driver.click_by_coordinates(search_box, 250, 16)
    
    def click_install_success_dialog_continue_btn(self):
        self.driver.click("install_success_dialog_continue_btn", timeout=10)

    def click_ok_btn(self):
        self.driver.click("ok_btn")

    # ---------------- no printers found ---------------- #
    def select_add_using_ip_addr_btn(self):
        self.verify_add_using_ip_addr_btn()        
        self.driver.click("use_ip_addr_btn")

    def select_search_again_btn(self):
        self.verify_search_again_btn()
        self.driver.click("search_again_btn")

    # ---------------- Setup incomplete dialog ---------------- #
    def click_exit_setup_btn(self):
        self.driver.click("exit_setup_btn")

    def click_continue_setup_btn(self):
        self.driver.click("continue_setup_btn")

    # ----------------what type of printer are you trying to find?---------------- #
    def select_setup_mode_printer_btn(self):
        self.driver.click("setup_mode_printer_btn")

    def select_wifi_mode_i_icon(self):
        el = self.driver.find_object("what_type_pane")
        self.driver.click_by_coordinates(el, x_offset=0.284, y_offset=0.084)


    def select_usb_printer_btn(self):
        self.driver.click("usb_printer_btn")

    def select_network_printer_btn(self):
        self.driver.click("network_printer_btn")

    def select_network_i_icon(self):    
        el = self.driver.find_object("what_type_pane")
        self.driver.click_by_coordinates(el, x_offset=0.945, y_offset=0.084)
   
    # ---------------- Choose a priner to set up ---------------- #
    def click_printer_not_listed_link(self):
        self.driver.click("printer_not_listed_btn")

    def click_refresh_link(self):
        self.driver.click("refresh_btn")

    # ---------------- Let's find your new printer ---------------- #
    def click_hp_support_website_link(self):
        self.driver.click("hp_support_website_link")

    # ---------------- Let's find your USB printer ---------------- #
    def click_show_me_how_link(self, index=0):
        """
        - 0: show_me_how_link
        - 1: show_me_how_1_link
        - 2: show_me_how_2_link
        - 3: show_me_how_3_link
        """
        btns = ["show_me_how_link", "show_me_how_1_link", "show_me_how_2_link", "show_me_how_3_link"]
        self.driver.click(btns[index])

    def click_x_button_to_close_dialog(self):
        self.driver.click("dialog_x_btn")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_device_picker_screen(self):
        """
        Verify the current screen is device picker screen
        """
        if self.verify_search_box(raise_e=False, timeout=60) is False:
            self.verify_no_printers_found_screen()
        else:
            self.verify_discovered_printers_grid_view()
    
    def check_beaconing_printer_show(self, printer_name, timeout=30):
        return self.driver.wait_for_object("dynamic_beaconing_printer_locator", format_specifier=[printer_name], timeout=timeout)

    def check_network_printer_show(self, ip_address, timeout=60):
        printer_show = False
        time_out = time.time() + timeout
        while time.time() < time_out:
            if self.driver.wait_for_object("network_printer", format_specifier=[ip_address], raise_e=False, timeout=2):
                printer_show =True
                break
            self.driver.swipe()
            time.sleep(3)
        if printer_show:
            return True
        else:
            raise Exception(f"The specified ip address {ip_address} printer does not show on Device Picker screen")

    def verify_smb_device_picker_screen(self, has_printer=True):
        """
        Verify the current screen is device picker screen for SMB account
        """
        self.driver.wait_for_object("my_printer_isnt_listed_text", invisible=True)
        self.driver.wait_for_object("refresh_list_link", timeout=60)
        assert self.driver.get_attribute("search_box_text_box", attribute="Name") == "Search by printer model"
        if has_printer:
            self.driver.wait_for_object("smb_title_text", timeout=15)
            self.driver.wait_for_object("smb_search_text")
            self.driver.wait_for_object("dynamic_printer_locator", format_specifier=["Remote"])
        else:
            self.driver.wait_for_object("no_available_title_text", timeout=15)
            self.driver.wait_for_object("smb_no_available_search_text")

    def verify_smb_searching_screen(self):
        """
        Verify the current screen is searching printer for SMB on device picker screen 
        """
        self.driver.wait_for_object("smb_searching_title", timeout=2)
        self.driver.wait_for_object("smb_searching_text")

    def verify_search_box(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("search_box_text_box", timeout=timeout, raise_e=raise_e)

    def verify_search_again_link(self):
        return self.driver.wait_for_object("search_again_link")

    def verify_discovered_printers_grid_view(self):
        self.driver.wait_for_object("discovered_printers_grid_view")

    def verify_warning_message_display(self, name, ip):
        if self.driver.wait_for_object("warning_message_text", format_specifier=[name], raise_e=False):
            return True
        else:
            assert ip != self.driver.get_attribute("first_printer_locator", attribute="Name")
        
    def verify_turn_on_ble_or_wifi_screen(self, raise_e=True, timeout=15):
        return self.driver.wait_for_object("turn_on_ble_or_wifi_title", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("turn_on_ble_or_wifi_image", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("to_find_a_new_printer_text", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("bluetooth_text", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("open_bluetooth_settings_text", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("wifi_text", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("open_network_settings_text", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("note_your_computer_text", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("continue_btn", timeout=timeout, raise_e=raise_e)

    def verify_turn_on_ble_or_wifi_dialog(self, raise_e=True):
        return self.driver.wait_for_object("turn_on_ble_or_wifi_text", raise_e=raise_e) and \
        self.driver.wait_for_object("if_your_computer_is_text", raise_e=raise_e) and \
        self.driver.wait_for_object("if_your_computer_does_text", raise_e=raise_e) and \
        self.driver.wait_for_object("no_bluetooth_or_wifi_btn", raise_e=raise_e) and \
        self.driver.wait_for_object("try_again_btn", raise_e=raise_e)

    def verify_turn_on_ble_or_wifi_screen_not_display(self):
        if self.driver.wait_for_object("turn_on_ble_or_wifi_title", raise_e=False, timeout=15):
            raise NoSuchElementException("the screen display")
        return True

    def verify_select_a_different_printer_dialog(self, raise_e=True):
        return self.driver.wait_for_object("select_different_printer_title", raise_e=raise_e)

    def verify_time_to_connect_screen(self, raise_e=True):
        return self.driver.wait_for_object("time_to_connect_screen_text", raise_e=raise_e)

    # ---------------- what type of printer are you trying to find ---------------- #
    def verify_what_type_of_printer_screen(self, timeout=25, wifi_connect=True):
        if wifi_connect:
            self.driver.wait_for_object("wifi_printer_initial_image")
            self.driver.wait_for_object("wifi_printer_initial_text")
            self.driver.wait_for_object("set_up_and_connect_text")
            self.driver.wait_for_object("this_option_is_also_text")
            self.driver.wait_for_object("setup_mode_printer_btn")

        self.verify_exit_setup_btn()
        self.driver.wait_for_object("what_type_of_printer_title", timeout=timeout)
        self.driver.wait_for_object("usb_printer_image")
        self.driver.wait_for_object("usb_printer_text")
        self.driver.wait_for_object("select_this_option_text")
        self.driver.wait_for_object("connect_the_cable_text")
        self.driver.wait_for_object("usb_printer_btn")

        self.driver.wait_for_object("network_printer_image")
        self.driver.wait_for_object("printer_to_text")
        self.driver.wait_for_object("find_a_printer_text")
        self.driver.wait_for_object("the_printer_might_text")
        self.driver.wait_for_object("network_printer_btn")

    def verify_check_for_network_connection_dialog(self, raise_e=True):
        return self.driver.wait_for_object("check_for_network_title", raise_e=raise_e) and \
        self.driver.wait_for_object("network_the_indicator_for_text", raise_e=raise_e) and \
        self.driver.wait_for_object("ok_btn", raise_e=raise_e)

    def verify_check_for_wifi_setup_mode_dialog(self, raise_e=True):
        return self.driver.wait_for_object("check_for_wifi_setup_mode_title", raise_e=raise_e) and \
        self.driver.wait_for_object("wifi_the_indicator_for_text", raise_e=raise_e) and \
        self.driver.wait_for_object("ok_btn", raise_e=raise_e)
        
    def verify_printer_status_is_offline(self):
        assert self.driver.get_attribute("first_printer_locator", attribute="Name") == 'Offline'

    # ---------------- pin dialog ---------------- #
    def verify_pin_dialog(self, raise_e=True):
        """
        Verify the current screen is Find the printer PIN screen
        """
        return self.driver.wait_for_object("pin_block", raise_e=raise_e)

    def verify_pin_dialog_submit_btn(self):
        return self.driver.wait_for_object("pin_submit_btn")

    def verify_pin_dialog_submit_btn_not_enabled(self):
        assert self.driver.get_attribute("pin_submit_btn", attribute="IsEnabled").lower() == 'false'

    def verify_incorrect_pin_dialog_show(self):
        self.driver.wait_for_object("incorrectpinerror_text")

    def verify_network_error_pin_dialog_show(self):
        self.driver.wait_for_object("networkerror_text", timeout=30)

    def verify_sign_in_dialog_show(self, raise_e=True):
        return self.driver.wait_for_object("signin_text", raise_e=raise_e)

    def verify_incorrect_pin_enter_dialog_show(self):
        self.driver.wait_for_object("incorrectpin_dialog_title")

    def verify_incorrect_pw_dialog_show(self):
        self.driver.wait_for_object("incorrectpassworderror_text")

    def verify_pw_locked_dialog_show(self , raise_e=True):
        self.driver.wait_for_object("locked_meessage_text", raise_e=raise_e)

    # ---------------- printer setup ---------------- #
    def verify_printer_setup_webpage(self, raise_e=True):
        #better name?
        return self.driver.wait_for_object("printer_setup_accept_all_btn", raise_e=raise_e)
        
    def verify_exit_setup_btn(self, raise_e=True, timeout=25):
        return self.driver.wait_for_object("exit_setup_btn", raise_e=raise_e, timeout=timeout)

    def verify_printer_setup_is_incomplete_dialog(self, raise_e=True, timeout=25):
        return self.driver.wait_for_object("printer_setup_is_incomplete_text", raise_e=raise_e, timeout=timeout)
    
    def verify_install_success_dialog(self, raise_e=True, timeout=25):
        return self.driver.wait_for_object("install_success_text", raise_e=raise_e, timeout=timeout)
    # ---------------- printer setup ---------------- #
    def verify_touch_checkmark_dialog(self, timeout=10, raise_e=True):
        '''
        Touch the checkmark on your printer display dialog
        '''
        return self.driver.wait_for_object("touch_checkmark_text", timeout=timeout, raise_e=raise_e)
    
    # ---------------- no printers found ---------------- #
    def verify_no_printers_found_screen(self):
        """
        Verify the current screen is no printers found screen
        """
        self.driver.wait_for_object("no_printers_found_text", timeout=15)
        self.driver.wait_for_object("no_printers_found_pane", timeout=15)

    def verify_add_using_ip_addr_btn(self):
        self.driver.wait_for_object("use_ip_addr_btn")

    def verify_search_again_btn(self):
        self.driver.wait_for_object("search_again_btn")

# ---------------- Setup incomplete dialog ---------------- #
    def verify_setup_incomplete_dialog(self, raise_e=True):
        '''
        Verify the current screen is Setup incomplete Dialog.
        '''
        return self.driver.wait_for_object("setup_incomplete_title", raise_e=raise_e) and \
        self.driver.wait_for_object("exit_setup_btn", raise_e=raise_e) and \
        self.driver.wait_for_object("continue_setup_btn", raise_e=raise_e)

    def verify_setup_incomplete_dialog_2(self, raise_e=True):
        '''
        Verify the current screen is Setup incomplete Dialog.
        '''
        self.driver.wait_for_object("setup_incomplete_title", raise_e=raise_e)
        self.driver.wait_for_object("exit_setup_btn", raise_e=raise_e)
        self.driver.wait_for_object("popup_back_btn", raise_e=raise_e)

    def verify_printer_setup_is_incomplete_dialog_1(self, raise_e=True):
        return self.driver.wait_for_object("printer_setup_is_incomplete_text", raise_e=raise_e) and \
        self.driver.wait_for_object("popup_back_btn", raise_e=raise_e) and \
        self.driver.wait_for_object("exit_setup_btn_on_dialog", raise_e=raise_e)

    def verify_printer_setup_is_incomplete_dialog_2(self, raise_e=True):
        return self.driver.wait_for_object("printer_setup_is_incomplete_text", raise_e=raise_e) and \
        self.driver.wait_for_object("popup_back_btn", raise_e=raise_e) and \
        self.driver.wait_for_object("ok_btn", raise_e=raise_e) and \
        self.driver.wait_for_object("install_to_print_btn", raise_e=raise_e)

# ---------------- Choose a printer to set up ---------------- #
    def verify_choose_a_printer_to_set_up_screen(self):
        '''
        Verify the current screen is Choose a printer to set up.
        '''
        self.driver.wait_for_object("choose_printer_set_up_title")
        self.driver.wait_for_object("exit_setup_btn")
        self.driver.wait_for_object("refresh_btn")
        self.driver.wait_for_object("printer_not_listed_btn")

    # ---------------- Let's find your new printer ---------------- #
    def verify_let_us_find_your_new_printer_screen(self):
        self.driver.wait_for_object("wifi_printer_initial_image")
        self.driver.wait_for_object("let_us_find_your_new_printer_title")
        self.driver.wait_for_object("make_sure_the_printer_text")
        self.driver.wait_for_object("make_sure_your_printer_text")
        self.driver.wait_for_object("temporarlly_disconnect_your_text")
        self.driver.wait_for_object("select_search_again_text")
        self.driver.wait_for_object("if_you_continue_to_text")
        self.driver.wait_for_object("hp_support_website_link")
        self.driver.wait_for_object("search_again_btn")

    # ---------------- Let's find your USB printer ---------------- #
    def verify_let_us_find_your_usb_printer_screen(self):
        self.driver.wait_for_object("wifi_printer_initial_image")
        self.driver.wait_for_object("let_us_find_your_usb_printer_title")
        self.driver.wait_for_object("to_help_find_text")
        self.driver.wait_for_object("your_windows_operating_text")
        self.driver.wait_for_object("the_printer_driver_text")
        self.driver.wait_for_object("the_printer_is_plugged_text")
        self.driver.wait_for_object("the_usb_cable_is_text")
        self.driver.wait_for_object("try_unplugging_and_reconnecting_text")
        self.driver.wait_for_object("select_search_again_text")
        self.driver.wait_for_object("show_me_how_1_link")
        self.driver.wait_for_object("show_me_how_2_link")
        self.driver.wait_for_object("show_me_how_3_link")
        self.driver.wait_for_object("search_again_btn")

    def verify_check_for_windows_update_screen(self):
        self.driver.wait_for_object("check_for_windows_update_title")
        self.driver.wait_for_object("dialog_x_btn")
        self.driver.wait_for_object("in_windows_text")
        self.driver.wait_for_object("complete_all_windows_text")
        self.driver.wait_for_object("restart_printer_setup_text")
        self.driver.wait_for_object("check_for_windows_update_image")

    def verify_check_the_status_of_screen(self):
        self.driver.wait_for_object("check_the_status_of_title")
        self.driver.wait_for_object("dialog_x_btn")
        self.driver.wait_for_object("open_control_pane_text")
        self.driver.wait_for_object("select_devices_and_printers_text")
        self.driver.wait_for_object("if_installation_failes_text")
        self.driver.wait_for_object("when_the_driver_text")
        self.driver.wait_for_object("network_printer_image")
        self.driver.wait_for_object("search_again_btn")

    def verify_connect_using_usb_screen(self):
        self.driver.wait_for_object("connect_using_usb_title")
        self.driver.wait_for_object("dialog_x_btn")
        self.driver.wait_for_object("connect_the_square_text")
        self.driver.wait_for_object("then_connect_text")
        self.driver.wait_for_object("when_ready_text")
        self.driver.wait_for_object("usb_printer_image")
        self.driver.wait_for_object("search_again_btn")

    # ----------------Let's find your network connected printer---------------- #
    def verify_let_us_find_your_network_screen(self):
        self.driver.wait_for_object("let_us_find_your_network_title")
        self.driver.wait_for_object("wifi_printer_initial_image")
        self.driver.wait_for_object("to_help_find_text")
        self.driver.wait_for_object("make_sure_the_printer_is_text")
        self.driver.wait_for_object("temporarlly_disconnect_your_text")
        self.driver.wait_for_object("if_the_printer_is_text")
        self.driver.wait_for_object("if_using_ethernet_text")
        self.driver.wait_for_object("select_search_again_text")
        self.driver.wait_for_object("show_me_how_link")
        self.driver.wait_for_object("search_again_btn")

    def verify_connect_printer_to_router_screen(self):
        self.driver.wait_for_object("connect_printer_to_router_title")
        self.driver.wait_for_object("dialog_x_btn")
        self.driver.wait_for_object("remove_any_plug_text")
        self.driver.wait_for_object("connect_the_ethernet_text")
        self.driver.wait_for_object("connect_the_other_text")
        self.driver.wait_for_object("usb_printer_image")
        self.driver.wait_for_object("when_ready_text")
        self.driver.wait_for_object("search_again_btn")

    def verify_remote_printer_not_show(self):
        assert self.driver.wait_for_object("dynamic_printer_locator", raise_e=False, format_specifier=['Remote']) is False
