import re
import ipaddress
from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow
from selenium.common.exceptions import NoSuchElementException

class AddPrinter(HPXFlow):
    flow_name = "add_printer"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    
    # device list case
    def maximize_app(self):
        self.driver.click("maximize_app")

    def refresh_device_page(self):
        """
        Refresh page and then device shows.
        """
        el = self.driver.wait_for_object("pane_refresh")
        el.click()
        return el.send_keys(Keys.CONTROL+"r")
    
    # ---------------- Add device panel ---------------- #
    def click_close_button(self):
        self.driver.click("close_button")

    def click_search_by_sn_button(self):
        self.driver.click("search_by_sn_button")
        self.driver.wait_for_object("enter_sn_edit")

    def click_choose_printer_button(self):
        self.driver.click("choose_a_printer_button", change_check={"wait_obj": "choose_a_printer_button", "invisible": True}, retry=2, delay=1)

    def click_back_button(self):
        self.driver.click("back_button")

    # ---------------- Device list screen ---------------- #
    def click_search_again_link(self):
        self.driver.click("search_again_link")

    def click_input_textbox(self):
        self.driver.click("input_textbox", retry=2)

    def click_my_printer_is_not_listed(self):
        self.driver.click("my_printer_isn't_listed_link")

    def select_network_printer(self):
        """
        click printer card on add device screen.
        Need change when the device page is ready.
        """
        self.driver.click("searched_network_printer")

    def click_add_printer_btn(self):
        """
        Add printer on printer card in device screen.
        """
        self.driver.click("add_printer_link")

    def is_valid_ip(self, ip):
        """
        check ipv4 address.
        """
        ipv4_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
        if not re.match(ipv4_pattern,ip):
            return False
        try:
            ipaddress.IPv4Address(ip)
            return True
        except:
            return False

    #input IP address/Hostname in add device screen.
    def search_printer(self, printer_obj, raise_e=True):
        self.driver.send_keys("input_textbox", printer_obj, press_enter=True, slow_type=True)
        self.driver.wait_for_object("results_scroll", timeout=20)
        search_res = self.driver.wait_for_object("dynamic_printer_info", format_specifier=[printer_obj], raise_e=False)
        if search_res is False:
            if raise_e:
                raise NoSuchElementException("Fail to found '{}' in printers".format(printer_obj))
            else:
                return False

    def select_printer(self, printer_obj):
        self.driver.click("dynamic_printer_info", format_specifier=[printer_obj])

    def click_top_exit_setup_btn(self, retry=3, raise_e=True):
        self.driver.click("top_exit_setup", timeout=5, retry=retry, raise_e=raise_e)

    def click_setup_incomplete_dialog_exit_setup_btn(self, raise_e=True):
        self.driver.click("setup_incomplete_dialog_exit_setup_btn", timeout=5, raise_e=raise_e)

    def click_printer_setup_is_incomplete_dialog_ok_btn(self, raise_e=True):
        self.driver.click("printer_setup_is_incomplete_dialog_ok_btn", timeout=5, raise_e=raise_e)
        
    def input_ip_address(self, ip, press_enter=True):
        self.driver.send_keys("input_textbox", ip, press_enter=press_enter, slow_type=True)
        if self.is_valid_ip(ip):
            if self.verify_searched_printers(raise_e=False):
                self.driver.wait_for_object("searched_printers",timeout=30) 
            else:
                self.driver.wait_for_object("no_results_message_text")
        else:
            self.driver.wait_for_object("no_results_message_text")

    def input_hostname(self, hostname, press_enter=True):
        self.driver.send_keys("input_textbox", hostname, press_enter=press_enter, slow_type=True)
        if self.verify_searched_printers(raise_e=False):
            self.driver.wait_for_object("searched_printers") 
        else:
            self.driver.wait_for_object("no_results_message_text")

    # Connectivity case

    # ----------------What type of printer are you trying to find?(3 options) ---------------- #
    def click_info_image_wifi_option(self):
        self.driver.click("info_image_wifi_option")

    def click_info_image_network_option(self):
        self.driver.click("info_image_network_option")

    def click_setup_mode_printer_button(self):
        self.driver.click("setup_mode_printer_button")

    def click_network_printer_button(self):
        self.driver.click("netwrok_printer_button")

    def click_usb_printer_button(self):
        self.driver.click("usb_printer_button")
            
    def click_dialog_ok_button(self):
        self.driver.click("dialog_ok_button")

    def click_back_link(self):
        """
        The back button on dialog.
        """
        self.driver.click("back_link")

    def click_dialog_close_button(self):
        self.driver.click("dialog_close_link")

    # ----------------Let's find your USB/network printer ---------------- #
    def click_show_me_how_link(self, index=0):
        """
         0: show_me_how_link, this link on let's find your network connected printer screen.
            The others on let's find your USB printer screen.
         1: show_me_how_1_link
         2: show_me_how_2_link
         3: show_me_how_3_link
        """
        btns = ["show_me_how_link", "show_me_how_1_link", "show_me_how_2_link", "show_me_how_3_link"]
        if self.driver.driver_type.lower() == "windows":
            self.driver.scroll_element(btns[index])
        self.driver.click(btns[index])

    def select_set_up_printer(self, printer_name):
        self.driver.click("dynamic_beaconing_printer_locator", format_specifier=[printer_name])

    def click_driver_unavailable_btn(self, retry=2):
        self.driver.click("driver_unavailable_btn", change_check={"wait_obj": "remove_and_add_printer_again_header"}, retry=retry)

    def click_back_btn(self):
        self.driver.click("back_btn_on_remove_add_screen")

    def click_printers_and_scanners_btn(self, retry=2):
        self.driver.click("printers_scanners_btn", retry=retry)

    def click_continue_btn(self, retry=3):
        """
        Click continue button about install driver.
        """
        self.driver.click("continue_btn", change_check={"wait_obj": "continue_btn","invisible": True}, retry=retry, delay=1)


    # ----------------No printers found screen---------------- #
    def click_add_using_ip_address_btn(self):
        self.driver.click("add_using_ip_address_btn")

    def click_search_again_btn(self):
        self.driver.click("search_again_btn")

    def click_continue_btn_on_add_printer_again(self, retry=3):
        """
        Click continue button about install driver.
        """
        self.driver.click("continue_btn_install_drive", retry=retry, delay=1)

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************

    # device list

    def verify_add_device_panel(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("missing_device_text", raise_e=raise_e, timeout=timeout) and \
               self.driver.wait_for_object("add_device_text" , raise_e=raise_e, timeout=timeout)
    
    def verify_enter_sn_panel(self, raise_e=True):
        return self.driver.wait_for_object("need_help_link", raise_e=raise_e) and \
               self.driver.wait_for_object("enter_sn_edit", raise_e=raise_e)

    def verify_notifications_panel(self, raise_e=True):
        return self.driver.wait_for_object("notifications_text", raise_e=raise_e) and \
               self.driver.wait_for_object("sign_in_create_account", raise_e=raise_e)
    
    def verify_profile_and_settings_panel(self, raise_e=True):
        return self.driver.wait_for_object("subscriptions_link",raise_e=raise_e) and \
               self.driver.wait_for_object("support_link", raise_e=raise_e)
    
    #This screen shows with searching printer process isn't finished.
    def verify_add_device_screen(self, raise_e=True):
        self.driver.wait_for_object("progress_bar",raise_e=raise_e)
        self.driver.wait_for_object("searching_printer_text",raise_e=raise_e)
    
    # ---------------- Add device screen ---------------- #
    def verify_search_printers_card(self, beconing_printer=True, network_printer=True):
        """
        Verify some printers shows in searched screen.
        """
        if beconing_printer:
            self.driver.wait_for_object("beaconing_printers")
        if network_printer:
            self.driver.wait_for_object("discovered_printers")
        if not beconing_printer and not network_printer:
            self.driver.wait_for_object("no_printers_found")

    def verify_search_again_link_is_enable(self, timeout=25):
        """
        Verify search agian link is enable after finishing seraching progress.
        """
        button = self.driver.wait_for_object("search_again_link", timeout=timeout)
        assert button.is_enabled()

    def verify_my_printer_isnt_listed_link_is_enable(self, timeout=25):
        button = self.driver.wait_for_object("my_printer_isn't_listed_link", timeout=timeout)
        assert button.is_enabled()

    def verify_searched_printers(self, raise_e=True):
        """
        The printer shows after inputing ip/hostname.
        """
        return self.driver.wait_for_object("searched_printers",timeout=60, raise_e=raise_e)
        
    def verify_no_results_messgae(self):
        """
        No results message shows after enter invalid ip or non-existent pinters IP/hostname.
        """
        self.driver.wait_for_object("no_results_message_text")

    def verify_progress_bar(self, timeout=30, invisible=True):
        """
        Verify the searching printer isn't finished.
        """
        self.driver.wait_for_object("progress_bar", timeout=timeout)
        self.driver.wait_for_object("progress_bar", timeout=timeout, invisible=invisible)

    def verify_spinner_image(self, timeout=30, invisible=True):
        """
        Verify the searching printer isn't finished.
        """
        self.driver.wait_for_object("spinner_image", timeout=timeout)
        self.driver.wait_for_object("spinner_image", timeout=timeout, invisible=invisible)
    
    def verify_discovered_printer(self):
        self.driver.wait_for_object("discovered_printers")


    # Connectivity

    #Below screens depend with testing printer enviroment.
    def verify_no_printers_screen(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("no_printers_found", timeout=timeout, raise_e=raise_e)

    def verify_results_scroll(self, raise_e=True, timeout=10):
        self.driver.wait_for_object("results_scroll", raise_e=raise_e, timeout=timeout)
    
    # ----------------What type of printer are you trying to find?(3 options) ---------------- #
    def verify_my_printer_is_not_listed_screen(self):
        """
        The screen shows after clicking my printer isn't link.
        """
        return self.driver.wait_for_object("wifi_printer_text") and \
               self.driver.wait_for_object("usb_printer_text") and \
               self.driver.wait_for_object("network_printer_text")

    def verify_check_wifi_setup_mode_dialog(self):
        """
        The screen shows after clicking info button on what type with wifi printer initial...pane.
        """
        return self.driver.wait_for_object("check_for_wifi_setup_mode_dialog") and \
               self.driver.wait_for_object("wifi_setup_dialog_text") and \
               self.driver.wait_for_object("dialog_ok_button")

    def  verify_check_network_connection_dialog(self):
        """
        The screen shows after clicking info button on what type with printer connected to network pane.
        """
        return self.driver.wait_for_object("network_connection_dialog") and \
               self.driver.wait_for_object("network_connection_dialog_text") and \
               self.driver.wait_for_object("dialog_ok_button")
               
    def verify_setup_mode_printer_button(self):
        """
        The button shows on what type with wifi printer initial set up or wifi reset pane.
        """
        if self.driver.driver_type.lower() == "windows":
            self.driver.scroll_element("setup_mode_printer_button")
        self.driver.wait_for_object("setup_mode_printer_button")

    def verify_network_printer_button(self):
        """
        The button shows on what type with printer connected to network pane.
        """
        if self.driver.driver_type.lower() == "windows":
            self.driver.scroll_element("netwrok_printer_button")
        self.driver.wait_for_object("netwrok_printer_button")

    def verify_usb_printer_button(self):
        """
        The button shows on what type with USB printer pane.
        """
        if self.driver.driver_type.lower() == "windows":
            self.driver.scroll_element("usb_printer_button")
        self.driver.wait_for_object("usb_printer_button")

    def verify_lets_find_your_new_printer_screen(self):
        """
        The screen shows after clicking setup mode printer button.
        """
        return self.driver.wait_for_object("find_your_new_printer_title") and \
               self.driver.wait_for_object("back_link") and \
               self.driver.wait_for_object("search_again_button")
    
    def verify_lets_find_your_network_connected_printer_screen(self):
        """
        The screen shows after clicking network printer button.
        """
        return self.driver.wait_for_object("let_us_find_your_network_connected_title") and \
               self.driver.wait_for_object("back_link") and \
               self.driver.wait_for_object("search_again_button")

    def verify_connect_printer_to_router_dialog(self):
        """
        The screen shows after clicking show me how link in network printer screen.
        """
        self.driver.wait_for_object("connect_printer_to_router_title")
        self.driver.wait_for_object("close_buttton")
        self.driver.wait_for_object("remove_any_plug_text")
        self.driver.wait_for_object("connect_the_ethernet_text")
        self.driver.wait_for_object("connect_the_other_text")
        self.driver.wait_for_object("wired_printer_image")
        self.driver.wait_for_object("when_ready_text")
        self.driver.wait_for_object("search_again_btn")
    
    def verify_show_me_how_link(self):
        """
        The link on let's find your network connected printer screen.
        """
        if self.driver.driver_type.lower() == "windows":
            self.driver.scroll_element("show_me_how_link")
        self.driver.wait_for_object("show_me_how_link")

    # ----------------Let's find your USB printer ---------------- #
    def verify_let_us_find_your_usb_printer(self):
        """
        The screen shows after clicking USB printer button.
        """
        self.driver.wait_for_object("let_us_find_your_usb_printer_title")
        self.driver.wait_for_object("show_me_how_1_link")
        self.driver.wait_for_object("show_me_how_2_link")
        self.driver.wait_for_object("show_me_how_3_link")
        self.driver.wait_for_object("search_again_btn")
    
    # ----------------show me how link 1 ---------------- #
    def verify_check_for_windows_update_dialog(self):
        self.driver.wait_for_object("check_for_windows_update_dialog")
        self.driver.wait_for_object("windows_update_image")
        self.driver.wait_for_object("dialog_close_link")
    
    # ----------------show me how link 2 ---------------- #
    def verify_driver_installation_dialog(self):
        self.driver.wait_for_object("check_the_driver_installation_title")
        self.driver.wait_for_object("driver_install_image")
        self.driver.wait_for_object("dialog_close_link")
        self.driver.wait_for_object("search_again_btn")
    
    # ----------------show me how link 3 ---------------- #
    def verify_connect_using_usb_dialog(self):
        self.driver.wait_for_object("connect_using_usb_title")
        self.driver.wait_for_object("connect_usb_image")
        self.driver.wait_for_object("dialog_close_link")
        self.driver.wait_for_object("search_again_btn")

    # ----------------printer found screen after clicking setup button ---------------- #
    def verify_printer_found_screen(self):
        """
        The screen shows after clicking setup button on add device screen with setup printer.
        """
        self.driver.wait_for_object("manage_printer_title")
        self.driver.wait_for_object("manage_printer_image")
        self.driver.wait_for_object("dialog_continue_button")

    # ---------------- Install driver to print ---------------- #
    def verify_install_driver_to_print_screen(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("driver_unavailable_btn", raise_e=raise_e, timeout=timeout) and\
        self.driver.wait_for_object("printers_scanners_btn", raise_e=raise_e, timeout=timeout) and\
        self.driver.wait_for_object("dialog_continue_button", raise_e=raise_e, timeout=timeout)
    
    def verify_remove_and_add_the_printer_again_screen(self):
        """
        The screen shows after clicking Driver unavailable button on "Install driver to print" screen.
        """
        self.driver.wait_for_object("remove_and_add_printer_again_header")
        self.driver.wait_for_object("circle1")
        self.driver.wait_for_object("circle2")
        self.driver.wait_for_object("imagelaunch")
        self.driver.wait_for_object("remove_printer_text")
        self.driver.wait_for_object("add_printer_again_text")
        self.driver.wait_for_object("return_here_text")
        if self.driver.driver_type.lower() == "windows":
            self.driver.swipe(direction="down", distance=4)
        self.driver.wait_for_object("visit_hp_support_text")
        self.driver.wait_for_object("back_btn_on_remove_add_screen")
        self.driver.wait_for_object("printers_and_scanners_btn_on_remove_screen")

        # ---------------- Install driver to print Auto ---------------- #
    def verify_auto_install_driver_to_print(self, timeout=30, raise_e=True):
        """
        Verify "Install driver to print-Auto Install" screen.
        """
        return self.driver.wait_for_object("process_image", raise_e=raise_e, timeout=timeout) and \
               self.driver.wait_for_object("get_driver_info_text", raise_e=raise_e, timeout=timeout) and \
               self.driver.wait_for_object("take_time_text", raise_e=raise_e, timeout=timeout)

    def verify_auto_install_driver_to_print_disappear(self, timeout=180):
        """
        Verify 'Install driver to print-Auto Install' screen disappears.
        """
        self.driver.wait_for_object("get_driver_info_text", timeout=timeout, invisible=True)

    def verify_auto_install_driver_done(self, timeout=30, raise_e=True):
        """
        Verify "Install driver to print-Auto Install" done dialog.
        """
        return self.driver.wait_for_object("auto_driver_installed", raise_e=raise_e, timeout=timeout) and \
               self.driver.wait_for_object("continue_btn", raise_e=raise_e, timeout=timeout)

    def verify_connecting_to_the_printer_screen(self, raise_e=True):
        """
        Verify the finding printer screen.
        """
        return self.driver.wait_for_object("finding_image", raise_e=raise_e) and \
               self.driver.wait_for_object("finding_printer_text", raise_e=raise_e) and \
               self.driver.wait_for_object("finding_time_text", raise_e=raise_e)

    def wait_for_printer_input_box_ready(self):
        """
        Wait until printers to load in add device screen.
        """
        self.driver.wait_for_object("printers_loaded", timeout=60)

    def verify_setup_incomplete_dialog(self, raise_e=True):
        return self.driver.wait_for_object("setup_incomplete_dialog_continue_setup_btn", raise_e=raise_e)

    def verify_printer_setup_is_incomplete_dialog(self, raise_e=True):
        return self.driver.wait_for_object("printer_setup_is_incomplete_dialog_install_to_print_btn", raise_e=raise_e)