from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import time
import logging

class Printers(SmartFlow):
    flow_name = "printers"

    MY_PRINTER_IS_NOT_LISTED = "my_printer_is_not_listed_txt"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_add(self):
        """
        Click on Add icon button on Printers screen
        End of flow: Add Printer screen.
                     Popup display for clicking this button first time.
        """
        try:
            self.driver.click("add_printer_btn")
        except NoSuchElementException:
            self.driver.click("alternative_add_printer_btn")

    def select_looking_for_wifi_direct_printers(self, is_permission=True):
        """
        Click on Allow button of Looking for Wi-Fi printers? button
        ENd of flow: Printer screen
                        Note: App Permission display if it is clicked at first time
        """
        self.driver.click("looking_for_wifi_direct_printers_btn")
        if is_permission:
            self.select_location_usage_ok_button()

    def select_search_icon(self):
        """
        Click on Search icon button in Printers page (WiFi-Direct/network printer)
        End of flow: Search screen
        """
        self.driver.click("search_btn", change_check={"wait_obj": "printer_title", "invisible": True})

    def search_printer(self, key_word):
        """
        Enter key_word to text field
        Press enter on virtual key
        :param key_word:
        End of flow: found printer list or empty list
        """
        self.driver.send_keys("search_tf", key_word)
    
    def search_printer_by_ip(self, ip_add):
        """
        Enter IP address in the text field
        Selects the printer from the list
        :param ip_add: IP address of the printer
        """
        self.driver.wait_for_object("search_for_printer_txt_box")
        self.driver.click("search_for_printer_txt_box")
        self.driver.send_keys("search_for_printer_txt_box", ip_add)
        for _ in range(5):
            if self.driver.wait_for_object("select_printer", format_specifier=[ip_add], timeout=10, raise_e=False):
                self.driver.click("select_printer", format_specifier=[ip_add])
                return
            else:
                self.driver.swipe()
        else:
            raise NoSuchElementException("Cannot find printer with IP address: {}".format(ip_add)) 

    def select_printer(self, printer_info, wifi_direct=False, is_searched=False, keyword=None, timeout=120):
        """
        Select target printer via its printer's ip address/Wifi-Direct name
        :param printer_info: IP address or Wifi-Direct name of printer
        :param wifi_direct: is Wi-Direct printer screen or not
        :param timeout: timeout for printer list loading and printer is on the list
        """
        logging.info("Select Printer - Printer Info: {} - via Search: {}".format(printer_info, is_searched))
        if wifi_direct:
            self.driver.wait_for_object("wifi_direct_printer_title", timeout=10)
            plist_obj = "wifi_direct_lv"
        else:
            self.driver.wait_for_object("printer_title", timeout=10)
            plist_obj = "printers_lv"
        self.driver.wait_for_object(plist_obj, timeout=timeout)
        logging.info("Waiting for 10 seconds for loading completely...")
        time.sleep(10)
        if is_searched:
            self.select_search_icon()
            self.search_printer(keyword)
            
        self.driver.scroll("printer_status_txt", scroll_object=plist_obj, format_specifier=[printer_info],
                               full_object=False, timeout=timeout, check_end=False)
        try:
            self.driver.click("printer_status_txt", format_specifier=[printer_info], change_check={"wait_obj": plist_obj, "invisible": True})
        except StaleElementReferenceException:
            self.driver.click("printer_status_txt", format_specifier=[printer_info], change_check={"wait_obj": plist_obj, "invisible": True})

    def select_search_printers_popup_continue(self, is_permission=False, raise_e=True):
        """
        Click on Continue button of Search for printers? popup
        ENd of flow: Printer screen
                        Note: App Permission display if it is clicked at first time
        """
        if self.driver.wait_for_object("search_printers_popup_continue_btn", timeout=10, raise_e=raise_e):
            self.driver.click("search_printers_popup_continue_btn")
            if is_permission:
                self.check_run_time_permission(accept=True)

    def dismiss_search_for_printers_popup(self):
        """
        Dismiss the popup, 'Search for printers?'
            - Click on Allow button
            - Allow on App Permission popup
        End of flow: Add Printers screen
        """
        try:
            self.driver.wait_for_object("search_printers_popup_title")
            self.select_search_printers_popup_continue()
            self.check_run_time_permission()
        except (TimeoutException, NoSuchElementException):
            logging.info("Search for Printers? popup is not displayed")

    def count_printers(self, wifi_direct=False):
        """
        Count number of found IP/Wifi-Direct printers
        :param wifi_direct: is Wi-Direct printer screen or not
        :return number of printers
        """
        if wifi_direct:
            self.driver.wait_for_object("wifi_direct_lv", timeout=10)
        else:
            self.driver.wait_for_object("printers_lv", timeout=10)
        printer_list = []
        end = False
        timeout = time.time() + 60
        while not end and time.time() < timeout:
            status_els = self.driver.find_object("printer_status_txt", multiple=True)
            for el in status_els:
                if el.text not in printer_list:
                    printer_list.append(el.text)
            time.sleep(5)
            end = self.driver.swipe(check_end=True)[1]
        return len(printer_list)

    # -----------------      Add Printer screen      -------------------------
    def select_my_printer_is_not_listed(self):
        """
        On Android 7/8/9: Click on My print is not listed button
        On Android 10/11: Click on Printer Not Listed? button
        End of flow: Setup new printer screen
        """ 
        if int(self.driver.platform_version) > 9:
            self.driver.click("printer_not_listed_btn")
        else:
            self.driver.click("my_printer_is_not_listed_button")
    
    def select_get_more_help_button(self):
        """
        On Android 10/11 Only: Click on Get More Help button
        End of flow: Setup new printer screen
        """ 
        self.driver.click("get_more_help_button")

    def select_printer_setup_printer_model(self, model):
        """
        Select a printer model in list on Print Setup Instruction screen
        :param model: specific printer model. Random selection if model is empty value
        """
        self.driver.click("select_printer_spinner")
        self.driver.scroll("select_printer_item", scroll_object="select_printer_lists", format_specifier=[model],
                           check_end=False, full_object=False, timeout=90)
        self.driver.click("select_printer_item", format_specifier=[model],change_check={"wait_obj": "select_printer_lists", "invisible": True})

    def select_setup_instruction_link(self, is_network=True):
        """
        Click on instruction link (Setup Mode / Network)
        :param is_network: setup network link (True). False: Setup Mode
        """
        if is_network:
            self.driver.click("network_setup_inst_link")
        else:
            self.driver.click("setup_mode_inst_link")

    def select_setup_instruction_popup_ok(self, is_network=True):
        """
        Click on OK button instruction popup
        :param is_network: setup network link (True). False: Setup Mode
        """
        if is_network:
            self.driver.click("network_setup_inst_popup_ok_btn")
        else:
            self.driver.click("setup_mode_inst_popup_ok_btn")

    def toggle_setup_instruction_checkbox(self, is_network=True, enable=True):
        """
        Check/uncheck an checkbox
        :param is_network: setup network link (True). False: Setup Mode
        """
        if is_network:
            self.driver.check_box("printer_network_setup_cb", uncheck=not enable)
        else:
            self.driver.check_box("printer_setup_mode_cb", uncheck=not enable)

    def select_printer_setup_try_again(self):
        """
        Click on Try Again button
        """
        self.driver.click("try_again_button")

    def select_print_setup_cancel(self):
        """
        Click on Cancel button
        """
        self.driver.click("cancel_button")

    def select_search_again_button(self):
        """Click on search again"""
        self.driver.click("search_again_btn")

    def select_exit_setup_button(self, check_kibana=False):
        """Click on exit setup"""
        if check_kibana:
            self.driver.click("printer_connected_exit_setup_btn")
        else:
            self.driver.click("exit_setup_btn")

    def select_oobe_printer(self, moobe_name):
        """
        Select OOBE printer on Add Printer screen
        :param moobe_name: moobe name or BLE mac address
        End of flow: Connected to Wifi of Moobe process
        """
        logging.info("OOBE Name: {}".format(moobe_name))
        for _ in range(3):
            self.driver.swipe(direction="up")         # Refresh the list
            if not self.driver.wait_for_object("printer_status_txt", format_specifier=[moobe_name], raise_e=False, 
                                               timeout=30):
                continue
            return self.driver.click("printer_status_txt", format_specifier=[moobe_name], 
                                     change_check={"wait_obj": "add_printer_title", "invisible": True}, raise_e=False)
        raise NoSuchElementException("Fail on selecting oobe printer {} after 3 tries".format(moobe_name))
    
    def select_oobe_awc_printer(self, moobe_name, ssid):
        """
        This flow is used for Select OOBE printer - AWC path on Android 10 and up
            - CLick on Printer not listted button
            - Click on Find printer
            - Click on target printer by moobe name
        """
        self.driver.click("printer_not_listed_btn", timeout=10)
        self.driver.click("find_printer_btn")
        # Based on developer's email.
        # It is system popup for scanning printer, user can quit whenever they want by clicking on cancel.
        # Therefore, no spec for it.
        # Also, 1 mitnute for timeout is valid for wirless discovery based on developer's expectation.
        # Tested with all pritners, 20 seconds is enough. 10 seconds is not enough.
        self.driver.click("printer_oobe_name", format_specifier=[moobe_name], timeout=20)
        self.driver.click("setup_printer_continue_btn")
        self.driver.click("select_network_ssid", format_specifier=[ssid], timeout=10)

    def select_remote_printer(self, printer_bonjour_name, is_searched=False, keyword=None):
        """
        Select target printer via its printer's bonjour name
        :param printer_info: bonjour name of printer
        :param is_searched
        """
        self.driver.wait_for_object("printers_lv")
        logging.info("Waiting for 3 seconds for loading completely...")
        time.sleep(3)
        if is_searched:
            self.select_search_icon()
            self.search_printer(keyword)
        self.driver.click("add_printer_ssid", format_specifier=[printer_bonjour_name], change_check={"wait_obj": "printers_lv", "invisible": True})

    # -----------------      WiFi Direct Printer screen      -------------------------

    def select_connect_to_the_printer(self):
        """
        Click on Connect to the printer on 'Wi-Fi Direct Printer' screen
        End of flow: Connect t "printer name"
        """
        # if pytest.config.getoption("--ga"):
        self.driver.click("wifi_direct_connect_to_printer_button", change_check={"wait_obj": "wifi_direct_connect_to_printer_button", "invisible": True})

    def select_disconnect_to_the_printer(self):
        """
        Select Network printers for printer types
            - Click on Connect to the printer button
        End of flow: Connect to password screen
        """
        self.driver.click("wifi_direct_disconnect_from_printer_button")

    def connect_to_wifi_direct_printer(self, pwd):
        """
        At popup "Connect to <WiFi- Direct name>":
            - Enter password into text field
            - CLick on Connect button
        :param pwd:
        End of flow: Wi-Fi direct Printer screen with loading icon
        """
        self.driver.send_keys("pwd_edit_tf", pwd)
        self.driver.click("pwd_connect_button")

    # -----------------      Printer Option Screens      -------------------------
    def load_printer_setup_screen(self, connection="wifi"):
        """
        Loads the add printer screen(android <= 9) or printer setup screen(android > 9)
        1. Selects get started
        2. Selects connection type, "wifi" or "ethernet"
        3. Selects continue
        4. Turn on Location Services
        5. Handle Location consent
            - selects continue
            - select allow on and location permission popup
            - selects "while using the app" button
        :param connection: The type of connection the desired printer uses, "wifi" or "ethernet"
        """
        if connection not in ("wifi", "ethernet"):
            raise ValueError('connection: "{}" is invalid'.format(connection))
        if self.verify_printer_options_screen(raise_e=False):
            self.select_printer_option_get_started()
        if connection == "wifi":
            self.driver.click("connection_type_wifi_rb")
        else:
            self.driver.click("connection_type_ethernet_rb")
        self.driver.click("setup_printer_continue_btn")
        self.driver.click("setup_printer_continue_btn")
        if int(self.driver.platform_version) > 11:
            self.check_run_time_permission()
        self.select_location_usage_ok_button(raise_e=False)

    def select_printer_option_add_printer(self):
        """Selects the add printer button on the add printer option screen"""
        self.driver.click("option_add_btn")

    def select_printer_option_get_started(self):
        """Selects the get started button on the add printer option screen"""
        self.driver.click("option_get_started_btn")

    def select_ethernet_connection(self, timeout=10):
        """Selects the Ethernet Cable option on the printer connection type screen"""
        self.driver.click("connection_type_ethernet_rb", timeout=timeout)
        self.driver.click("setup_printer_continue_btn")

    def select_wifi_connection(self, timeout=10):
        """Selects the Wifi option on the printer connection type screen"""
        self.driver.click("connection_type_wifi_rb", timeout=timeout)
        self.driver.click("setup_printer_continue_btn")

    def select_setup_continue(self, is_permission=False):
        self.driver.click("setup_printer_continue_btn")
        if is_permission:
            self.check_run_time_permission()

    def select_location_usage_ok_button(self, is_permission=True, raise_e=True):
        """Selects Continue button on the using location data popup"""
        self.driver.click("location_notice_continue_btn", raise_e=raise_e)
        if is_permission:
            self.check_run_time_permission()

    def select_wifi_screen_learn_more(self):
        """
        Selects the learn more link on the prepare wifi screen
        NOTE: The learn more link is embedded at the end of the last element so must try clicking along 
            bottom of element.
        """
        for x in range(10):
            self.driver.click_element_by_offset("prepare_wifi_printer_learn_more_txt", x * 0.1, 0.9)
            if self.driver.wait_for_object("wifi_learn_more_popup_title_txt", timeout=1, raise_e=False):
                return True
        raise NoSuchElementException("wifi_learn_more_popup_title_txt did not appear")

    def select_wifi_learn_more_ok_button(self):
        """Selects the Ok button on the learn more popup at the wifi connectivity screen"""
        self.driver.click("wifi_learn_more_popup_ok_btn")

    def select_turn_on_bluetooth_continue_btn(self):
        """Selects the CONTINUE button on the turn on bluetooth popup"""
        self.driver.click("turn_on_bluetooth_btn", format_specifier=[self.driver.return_str_id_value("turn_on_bluetooth_btn").upper()])

    def select_permissions_popup_button(self, btn):
        """
        Selects a button on the Smart allow permissions popup
        :param btn: The button to select on the popup. "exit" or "permissions"
        """
        self.driver.click("provide_permissions_popup_{}_btn".format(btn))

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_search_printers_screen(self, is_empty=False, is_wifi_direct=False):
        """
        Verify current screen is searching screen
        :param is_empty: True -> empty list. False: has list
        :param is_wifi_direct: True -> for Wifi Direct. False: for Printer list
        """
        self.driver.wait_for_object("search_tf")
        if is_wifi_direct:
            self.driver.wait_for_object("wifi_direct_connection_status", invisible=is_empty, timeout=10)
        else:
            self.driver.wait_for_object("add_printer_connection_status", invisible=is_empty, timeout=10)

    #-----------------------        PRINTER SCREEN      ---------------------------

    def verify_printers_screen(self, raise_e=True):
        """
        Verify that current screen is Printers screen:
            - Printers title
            - Search icon button
        """
        return bool(self.driver.wait_for_object("printer_title", raise_e=raise_e)) and bool(self.driver.wait_for_object("search_btn", raise_e=raise_e))

    def verify_search_printers_popup(self, raise_e=True):
        """
        Verify current popup is "Search for printers?" popup via:
            - title
            - Continue button
        """
        return self.driver.wait_for_object("search_printers_popup_title", raise_e=raise_e) is not False and \
            self.driver.wait_for_object("search_printers_popup_continue_btn", raise_e=raise_e)

    def verify_printer_options_screen(self, raise_e=True):
        """
        Verify the printer options screen
         - Set up a new printer image
         - Get Started button
         - Add a printer that's already set up image
         - Add printer button
        """
        return self.driver.wait_for_object("option_get_started_img", raise_e=raise_e) is not False and \
            self.driver.wait_for_object("option_add_printer_img", raise_e=raise_e) is not False and \
            self.driver.wait_for_object("option_get_started_btn", raise_e=raise_e) is not False and \
            self.driver.wait_for_object("option_add_btn", raise_e=raise_e) is not False

    def verify_printer_connection_type_screen(self):
        """
        Verify the printer connection type screen
         - wifi radio button
         - ethernet radio button
         - "How do you want to connect this printer?" text
         - continue button
        """
        self.driver.wait_for_object("connection_type_title")
        self.driver.wait_for_object("connection_type_wifi_rb")
        self.driver.wait_for_object("connection_type_ethernet_rb")
        self.driver.wait_for_object("setup_printer_continue_btn")

    def verify_connect_ethernet_screen(self):
        """
        Verify the prepare printer to connect using ethernet screen
         - header text
         - continue button
        """
        self.driver.wait_for_object("prepare_ethernet_header_txt")
        self.driver.wait_for_object("setup_printer_continue_btn")
    
    def verify_connect_wifi_screen(self):
        """
        Verify the get printer ready to connect over Wi-Fi screen
         - header text
         - continue button
        """
        self.driver.wait_for_object("prepare_wifi_header_txt")
        self.driver.wait_for_object("setup_printer_continue_btn")

    def verify_prepare_wifi_learn_more_popup(self, invisible=False):
        """
        Verify the "How are location and Bluetooth used?" popup from the connect wifi screen's learn more link
         - title text
         - body text
         - ok button
        """
        self.driver.wait_for_object("wifi_learn_more_popup_title_txt", invisible=invisible)
        self.driver.wait_for_object("wifi_learn_more_popup_body_txt", invisible=invisible)
        self.driver.wait_for_object("wifi_learn_more_popup_ok_btn", invisible=invisible)

    def verify_turn_on_bluetooth_popup(self):
        """
        Verify the "Turn on Bluetooth" popup
         - title text
         - body text
         - continue button
        """
        self.driver.wait_for_object("turn_on_bluetooth_title_txt")
        self.driver.wait_for_object("turn_on_bluetooth_txt")
        self.driver.wait_for_object("turn_on_bluetooth_btn", format_specifier=[self.driver.return_str_id_value("turn_on_bluetooth_btn").upper()])

    def verify_turn_on_location_popup(self):
        """
        Verify the "Turn on location..." popup
         - title text
         - open settings button
        """
        self.driver.wait_for_object("turn_on_location_title_txt")
        self.driver.wait_for_object("turn_on_location_settings_btn", format_specifier=[self.driver.return_str_id_value("turn_on_location_settings_btn").upper()])

    def verify_location_usage_popup(self):
        """
        Verify the "Using location data" popup
         - title text
         - body text
         - ok button
        """
        self.driver.wait_for_object("location_notice_title_txt")
        self.driver.wait_for_object("location_notice_txt")
        self.driver.wait_for_object("location_notice_continue_btn")

    def verify_provide_permissions_popup(self, permission=None):
        """
        Verify the provide permissions popup
         - title text
         - permissions button
         - exit button
        :param permission: The permission the popup should represent. Possible values: "nearby_device", "precise_location", "all_permissions"
        """
        title_fs = []
        if permission is not None:
            if permission == "all_permissions" and int(self.driver.platform_version) < 12:
                permission = "all_permissions_old"
            title_fs = [self.driver.return_str_id_value("provide_permissions_popup_{}_title_str".format(permission))]
        self.driver.wait_for_object("provide_permissions_popup_title_txt", format_specifier=title_fs)
        self.driver.wait_for_object("provide_permissions_popup_permissions_btn")
        self.driver.wait_for_object("provide_permissions_popup_exit_btn")

    def verify_hide_printer(self):
        """
        Verifies "Hide Printer" on printer screen. Expected to be near bottom of screen.
        """
        self.driver.scroll("hide_printer_btn", timeout=30)

    #-----------------------        WIFI DIRECT PRINTER SCREEN      ---------------------------
    def verify_wifi_direct_printers_screen(self):
        """
        Verify that current screen is Wifi Direct Printers screen:
            - Wifi Direct printers display
        """
        self.driver.wait_for_object("search_btn")
        self.driver.wait_for_object("wifi_direct_printer_title")

    def verify_connect_printers_wifi_direct_screen(self, is_disconnect=False):
        """
        Verify that current screen is Network Printers screen:
            - Wi-Fi Direct Printer description
            - Connect to the printer button
            - Disconnect button is is_disconnect = True
        :param is_disconnect: True: visible disconnect btn. False: invisible disconnect
        """
        self.driver.wait_for_object("wifi_direct_desc")
        self.driver.wait_for_object("wifi_direct_connect_to_printer_button")
        self.driver.wait_for_object("wifi_direct_disconnect_from_printer_button", invisible= not is_disconnect)

    def verify_visible_wifi_direct_wrong_pwd_txt(self):
        """
        Verify that 'Something might be wrong with your password.' is visible
        """
        self.driver.wait_for_object("wifi_direct_wrong_pwd_txt", timeout=60)

    def verify_setup_authentication_screen(self):
        """
        Verify that current screen is Wireless Password popup:
            - Enter pwd field
            - Cancel button
            - Connect button
        """
        self.driver.wait_for_object("pwd_edit_tf")
        self.driver.wait_for_object("pwd_cancel_button")
        self.driver.wait_for_object("pwd_connect_button")

    #-----------------------        PRINTER SETUP SCREEN      ---------------------------
    def verify_printer_setup_screen(self, connection="wifi", timeout=10):
        """
        Verify printer setup screen
         android > 9
          - setup printer title
          - printer not listed? button
         android <= 9
          - add printer title
          - my printer is not listed button
        :param connection: The connection type that was selected, "wifi" or "ethernet"
        """
        if int(self.driver.platform_version) > 9:
            if connection == "wifi":
                if (self.driver.wait_for_object("turn_on_bluetooth_title_txt",raise_e=False)):
                    self.driver.click("continue_turn_on_bluetooth")
                    self.driver.click("allow_bluetooth")
                if self.driver.wait_for_object("provide_permissions_popup_all_permissions_title_str", raise_e=False):
                    self.driver.click("provide_permissions_popup_exit_btn")
                self.driver.wait_for_object("printer_setup_title")
            else:
                self.driver.wait_for_object("add_printer_title")
            self.driver.wait_for_object("printer_not_listed_btn", timeout=timeout)
        else:
            self.driver.wait_for_object("add_printer_title")
            self.driver.wait_for_object("my_printer_is_not_listed_button", timeout=timeout)
    
    #-----------------------        ADD PRINTERS SCREEN      ---------------------------

    def verify_add_printers_screen(self):
        """
        Verify Add Printer screen with no printer on the list via: 
            - If platform is Android 9 or lower, then verify Add Printer title.
            - 'There are no printers in Setup Mode' text
        Note: This screen only for Android 7/8/9. Android 10 or higher, please refer verify_printer_setup_screen() for details
        """
        self.driver.wait_for_object("add_printer_title")
        self.driver.wait_for_object("my_printer_is_not_listed_button")

    def verify_add_printers_list(self, is_empty=False):
        """
        Verify Add Printers has printers on list or empty list
        :param is_empty: True -> empty list. False: has printer on list
        """
        if int(self.driver.platform_version) > 9:
            self.verify_printer_setup_screen()
        else:
            self.verify_add_printers_screen()
        if is_empty:
            self.driver.wait_for_object("add_printer_no_printers_txt")
        else:
            self.driver.wait_for_object("add_printer_lv")

    def verify_setup_printers_instruction_screen(self):
        """
        Verify that current screen is Setup Printer Instruction screen
            - Try again button
            - Cancel button
        """
        self.driver.wait_for_object("select_printer_spinner")
        self.driver.wait_for_object("try_again_button")
        self.driver.wait_for_object("cancel_button")

    def verify_my_printer_not_listed_help_msg(self):
        """
        Verify my printer not listed help text on Setup printers screen after clicking -My printer is not listed-
        """
        self.driver.wait_for_object("printer_not_listed_help_text")

    def verify_my_printer_setup_instruction(self):
        """
        Verify that current screen is printer setup screen with instruction:
            + checkbox for "Make sure printer is in Setup Mode" display
            + checkbox for "Make sure you know your network name and password" display
            + How do I do this? link display (2 links)
        """
        self.driver.wait_for_object("printer_setup_mode_cb")
        self.driver.wait_for_object("setup_mode_inst_link")
        self.driver.wait_for_object("printer_network_setup_cb")
        self.driver.wait_for_object("network_setup_inst_link")

    def verify_setup_instruction_link_popup(self, is_network=False):
        """
        Verify a popup after click the setup instruction link
        :param is_network: True: from network link. False: from setup mode link
        """
        if is_network:
            self.driver.wait_for_object("network_setup_inst_popup_title")
        else:
            self.driver.wait_for_object("setup_mode_inst_popup_title")

    def verify_try_again_button(self, is_enabled=False):
        """
        check if the button "Try Again" is enabled or not
        :param is_enabled:
        """
        self.driver.wait_for_object("try_again_button")
        try_btn = self.driver.find_object("try_again_button")
        current_status = True if try_btn.get_attribute("enabled").lower() == "true" else False
        if is_enabled != current_status:
            raise AssertionError("Try Button is not matched with expected status {}".format(is_enabled))

    def verify_printer_setup_with_printer_not_listed_msg(self,raise_e=True, timeout=10):
        """
        Verify "Printer Not Listed?" message on Printer Setup screen
        """
        self.driver.wait_for_object("find_printer_text", raise_e=raise_e, timeout=timeout)

    def verify_add_printer_help_find_your_printer_instruction_screen(self):
        """
        Verify Add Printer instruction screen via:
            - Add Printer title
            - Check these items to help find your printer message
            - Search Again button
            - Exit Setup button
        """
        self.driver.wait_for_object("add_printer_title")
        self.driver.wait_for_object("help_find_your_printer_msg")
        self.driver.wait_for_object("search_again_btn")
        self.driver.wait_for_object("exit_setup_btn")
