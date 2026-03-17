import logging
import pytest
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Printers(SmartFlow):
    flow_name = "printers"

    ####################################################################################################################
    #                                Printers - Add Printer button screen                                              #
    ####################################################################################################################
    
    def set_up_printer(self, option="wifi"):
        """
        From the "How do you want to connect this printer" page
        Select connection type, "wifi" or "ethernet" then continue button
        """
        self.driver.click("connection_option_wifi") if option=="wifi" else self.driver.click("connection_option_ethernet")
        self.driver.click("continue_btn")
    
    def verify_set_up_printer_screen(self):
        """
        Verify "How do you want to connect this printer" page
        Select connection type, "wifi" or "ethernet" then continue button
        """
        self.driver.wait_for_object("connection_option_wifi", timeout=60)
        self.driver.wait_for_object("connection_option_ethernet")

    def verify_printers_list_screen_ui(self):
        self.verify_printers_nav()
        self.verify_add_printers_btn()
        self.verify_back_arrow_btn()
        self.verify_printers_list()

    def verify_printers_list(self):
        self.driver.wait_for_object("printers_tv")

    def verify_add_printers_btn(self, raise_e=True):
        return self.driver.wait_for_object("add_printer_btn", raise_e=raise_e)

    def verify_printers_nav(self, timeout=10, raise_e=True):
        """
        Verify Printers screen navigation bar title
        """
        return self.driver.wait_for_object("printers_title", timeout=timeout, raise_e=raise_e)

    def verify_add_printer_screen(self):
        """
        Verify Add Printer Screen
        """
        self.driver.wait_for_object("add_printer_using_ip_btn")

    def verify_search_bar(self):
        """
        search bar on the printer list screen
        """
        return self.driver.wait_for_object("search_box")

    def verify_clear_text_button(self):
        """
        verify the small x button on search bar
        """
        return self.driver.wait_for_object("_shared_clear_text_btn")

    def verify_connect_the_printer_screen(self):
        """
        Verify the Connect the Printer screen
        """
        self.driver.wait_for_object("connect_the_printer_txt")

    def get_search_bar_text(self):
        """
        Return the text value found in the search bar of the printer list screen
        """
        return self.driver.wait_for_object("search_box").text

    def select_search_bar(self):
        self.verify_search_bar().click()

    def select_clear_text_button(self):
        self.verify_clear_text_button().click()

    def find_printer_using_search_bar(self, printer_str):
        """
        :param printer_str: name of the printer or ip address
        """
        self.driver.send_keys("search_box", printer_str)

    def verify_printer_in_list(self, printer_str, timeout=10, raise_e=True):
        """
        :param printer_str: ip or bonjour name of the printer
        """
        return self.driver.wait_for_object("dynamic_printer_cell", format_specifier=[printer_str], timeout=timeout, raise_e=raise_e)

    def select_printer_in_list(self, printer_str):
        self.driver.click("dynamic_printer_cell", format_specifier=[printer_str])

    def select_printer_not_listed_btn(self):
        """
        Click the "Printer not listed" button
        """
        return self.driver.click("add_printer_btn")
    
    def verify_printer_not_listed_btn(self, timeout=5, raise_e=True):
        """
        Verify the "Printer not listed" button
        """
        return self.driver.wait_for_object("add_printer_btn", timeout=timeout, raise_e=raise_e)

    def count_number_of_printers(self):
        """
         gives the number of printers available in printer list
            dynamically changes but count approx before we click next button,
                keep this dynamic GA as special case, we will get mismatch in count but will be a subset
        :return: number of items on printer list
        """
        ## GA Purpose
        printers = self.driver.find_object("printers_cell", multiple=True)
        dynamic_ga_key_value = str(len(printers))
        logging.info("the availabel printers are {}".format(dynamic_ga_key_value))
        self.driver.wait_for_object("printers_cell")
        return len(printers)

    def search_for_printer(self, query):
        self.driver.swipe(direction="up", per_offset=0.6)
        self.driver.send_keys("search_box", query)

    def select_moobe_printer_from_list(self, printer_name, attempt=20):
        for i in range(attempt):
            try:
                self.driver.wait_for_object("moobe_printer", format_specifier=[printer_name]).click()
                break
            except TimeoutException:
                if i == attempt-1:
                    raise TimeoutException("Could not find moobe printer")
                else:
                    logging.info("Could not find moobe printer, try#: {}".format(i+1))

    def search_for_printer_directly_using_ip(self, name):
        """
        Enters ip address into the text field and clicks done to search for a printer
        :param ip:String, ip address
        :return:
        """
        self.driver.click("enter_ip_address")
        if pytest.platform == "IOS":
            self.driver.send_keys("enter_ip_address", name, press_enter=True)
        else:
            self.driver.send_keys("enter_ip_address", name, append_newline=True)
        sleep(2)

    def select_is_this_your_printer(self, yes=True):
        if yes:
            self.driver.click("is_this_your_printer_yes_btn", timeout=30)
            sleep(3)
        else:
            self.driver.click("_shared_no")

    def get_printers(self):
        """
        Return a list of all the web elements of the printers listed
        """
        return self.driver.find_object("printers_cell", multiple=True)

    def select_printer_by_index(self, index=0):
        self.driver.click("printers_cell", index=index)

    def search_for_printer_using_serial_num(self, serialnum):
        """
        Enters serial number into the text field and clicks done to search for a printer
        param serial number
        """
        self.driver.click("enter_serial_number_text_box")
        self.driver.send_keys("enter_serial_number_text_box", serialnum, press_enter=True)
        sleep(5)

    def verify_listed_printer_using_serial_num(self):
        """
        verify printer list by serial number.
        """
        return self.driver.wait_for_object("add_a_device_by_serial")

    def click_on_add_device_using_serial_num(self):
        """
        click on add device by serial number.
        """
        self.driver.click("add_a_device_by_serial")

    def verify_help_link_for_search_by_serial_number_screen(self):
        """
        Verify help link on search by serial number.
        """
        self.driver.wait_for_object("enter_serial_number_text_box")
        self.driver.wait_for_object("help_link_for_serial_number")

    def click_and_verify_help_link_for_search_by_serial_number_screen(self):
        """
        click help link on search by serial number.
        """
        self.driver.click("help_link_for_serial_number")
        self.driver.wait_for_object("hp_support_page_link")

    def click_on_back_arrow_on_add_device_button(self):
        """
        Clicks on add device button.
        """
        self.driver.click("add_a_device_button")

    def verify_add_device_page(self):
        """
        Verify add device page.
        """
        self.driver.wait_for_object("set_up_new_printer")
        self.driver.wait_for_object("add_printer_btn")
        self.driver.wait_for_object("search_by_serial")

    ####################################################################################################################
    #                   Printers - setup new printer OR connect to previously used printer                             #
    ####################################################################################################################
    def verify_printers_setup_screen_ui(self):
        self.driver.wait_for_object("set_up_new_printer_btn")
        self.driver.wait_for_object("add_printer_using_ip_btn")
        self.driver.wait_for_object("supported_printer_btn")
        self.driver.wait_for_object("connect_to_previously_used_printer_btn")
        self.verify_printers_nav()
        self.verify_back_arrow_btn()

    def select_set_up_a_new_printer(self):
        self.driver.wait_for_object("set_up_new_printer_btn").click()

    def select_add_printer_using_ip(self):
        """
        Selects the add printer using ip address button
        """
        if pytest.platform == "MAC":
            self.driver.click("add_printer_using_ip_btn")
        else:
            if not self.driver.click("add_printer_using_ip_btn", raise_e=False):
                self.driver.swipe(direction='down')
                self.driver.click("add_printer_using_ip_btn")

    def select_supported_printers_btn(self):
        """
        Clicks on the Supported printers button
        """
        self.driver.click("supported_printer_btn")

    def select_connect_to_previously_used_printer(self):
        """
        Clicks on the Connect to a previously used printer button on the empty printer list screen
        """
        self.driver.click("connect_to_previously_used_printer_btn")

    def select_add_printer(self):
        """
        select the add printer button on printers page [big list of printers,
        """
        self.driver.swipe(direction='down')
        self.driver.click("add_printer_btn")

    def select_printer_from_printer_list(self, printer_ip, timeout=120):
        """
        Select a printer according to its printer's ip address.
        Steps:
            - Scroll down printer list to target printer. IF not see, scroll up one time
            - Click on target printer
        End of flow: Printer Info screen of target printer
        :param printer_ip: printer's ip address
        """
        self.driver.wait_for_object("printers_tv", timeout=10)
        target_printer = self.driver.scroll("printer_ip", format_specifier=[printer_ip],
                                            full_object=False, timeout=timeout, check_end=False)
        # if it is not found for scrolling down, scroll up for finding one more 
        if not target_printer:
            target_printer = self.driver.scroll("printer_ip", direction="up", format_specifier=[printer_ip],
                                                full_object=False, timeout=timeout, check_end=False)
        target_printer.click()

    def verify_bluetooth_on_by_invisible_popup(self):
        """

        :return:
        """
        self.driver.wait_for_object("connect_bluetooth_popup_title", invisible=True)

    def verify_connect_bluetooth_popup(self):
        """
        Verify current popup is "Connect using Bluetooth popup"
            - title
            - Close button
        """
        self.driver.wait_for_object("connect_bluetooth_popup_title")

    def is_connect_using_bluetooth_popup(self):
        """
        Checks if the current screen contains the bluetooth popup and dismisses it
        :return:
        """
        if self.verify_bluetooth_on_by_invisible_popup():
            logging.warning("Device-blue tooth is ON --Current Screen did NOT contain the Bluetooth Popup")
        else:
            try:
                self.verify_connect_bluetooth_popup()
                self.driver.click("connect_bluetooth_popup_close_btn")
            except TimeoutException:
                logging.warning("Current Screen did NOT contain the Bluetooth Popup")

    def select_get_connection_help(self):
        """
        Clicks on Get Connection help button on the wifi off screen
        :return:
        """
        self.driver.click("get_connection_help_btn")

    def select_learn_more(self):
        """
        Selects the learn more button on the wifi off screen
        :return:
        """
        self.driver.click("learn_more_btn")

    def verify_printer_list_wifi_off(self):
        """
        Verifies that the wifi off screen is displayed
        :return:
        """
        sleep(10)
        self.driver.wait_for_object("get_connection_help_btn")
        self.driver.wait_for_object("learn_more_btn")

    def verify_printer_list_empty(self):
        """
        Verify tha the printer list is displaying the empty printer list screen
        :return:
        """
        self.driver.wait_for_object("set_up_a_new_printer_btn")
        self.driver.wait_for_object("connect_to_previously_used_printer_btn")

    def select_setup_a_new_printer(self):
        """
        Clicks on the Set up a new printer button on the empty printer list
        :return:
        """
        self.driver.click("set_up_a_new_printer_btn")

    def select_add_printer_using_ip_via_empty_printer_list(self):
        """
        SElects the add printer using ip address button
        :return:
        """
        self.driver.click("add_printer_using_ip_btn")

    def add_printer_ip(self, printer_ip):
        # self.verify_printers_nav()
        if not self.verify_add_printers_btn(raise_e=False):
            self.driver.click("connect_using_ip_address")
        else:
            self.select_add_printer_btn()
            self.verify_add_printer_screen()
            self.select_add_printer_using_ip()
        self.verify_connect_the_printer_screen()
        sleep(3)
        self.search_for_printer_directly_using_ip(printer_ip)
        sleep(3)
        if self.driver.wait_for_object("printer_limited_support_pop_title_txt", raise_e=False):
            self.driver.click("_shared_str_ok")
        self.select_is_this_your_printer()

    def select_a_diff_printer(self, printer_name):
        printer_list = self.driver.find_object("printer_cell_visible", multiple=True)
        for printer in printer_list:
            displayed_printer_name = printer.text
            if displayed_printer_name != printer_name:
                self.driver.click("dynamic_printer_cell", format_specifier=[displayed_printer_name])
                logging.info("Printer selected- {}".format(displayed_printer_name))
                break

    def verify_automatically_put_device_on_network(self):
        self.driver.wait_for_object("connect_automatically_logo", displayed=False)

    def verify_found_printer_for_setup(self, bonjour_name):
        self.driver.wait_for_object("_shared_dynamic_text", format_specifier=[
                self.get_text_from_str_id("found_printer_for_setup").replace("%@", bonjour_name)])

    ####################################################################################################################
    #                                                   Printer Connection                                             #
    ####################################################################################################################
    def verify_printer_connection_screen_ui(self):
        self.driver.wait_for_object("printer_connection_navbar_title")
        self.driver.wait_for_object("how_do_i_do_this_link")
        self.driver.wait_for_object("follow_instructions_txt")
        self.driver.wait_for_object("check_printer_txt")
        self.driver.wait_for_object("check_printer_details_txt")
        self.driver.wait_for_object("check_network_conn_txt")
        self.driver.wait_for_object("check_network_details_txt_os14")
        self.driver.wait_for_object("restart_router_txt")
        self.driver.wait_for_object("restart_router_details_txt")
        self.driver.wait_for_object("try_again_btn")
        self.driver.wait_for_object("get_more_help_link")
        self.driver.wait_for_object("contact_HP_on_facebook_messenger_link")

    def verify_connect_the_printer_screen_ui(self):
        self.verify_connect_the_printer_screen()
        self.verify_back_arrow_btn()
        self.driver.wait_for_object("enter_ip_address")

    def select_open_permissions_button(self):
        self.driver.click("open_permissions_btn")

    def verify_enable_local_network_permission_blocker_screen(self):
        self.driver.wait_for_object("enable_local_network_blocker_screen")

    def verify_choose_type_of_printer_screen(self):
        self.driver.wait_for_object("choose_type_of_printer_screen")

    def verify_printer_options_screen(self, timeout=5, raise_e=True):
        """
        Verify the printer options screen
            - Set up a new printer image
            - Get Started button
            - Add a printer that's already set up image
            - Add printer button
        Returns: (bool) True if successfull, False otherwise
        """
        ret_val = True
        ret_val = ret_val and self.driver.wait_for_object("option_get_started_img", timeout=timeout, raise_e=raise_e)
        ret_val = ret_val and self.driver.wait_for_object("option_add_printer_img", timeout=timeout, raise_e=raise_e)
        ret_val = ret_val and self.driver.wait_for_object("get_started_btn", timeout=timeout, raise_e=raise_e)
        ret_val = ret_val and self.driver.wait_for_object("add_printer_btn", timeout=timeout, raise_e=raise_e)
        return ret_val

    def select_get_started_button(self):
        self.driver.click("get_started_btn")

    def verify_choose_printer_screen_ui(self):
        self.verify_back_arrow_btn()
        self.verify_choose_type_of_printer_screen()
        self.driver.wait_for_object("get_started_btn")
        self.verify_add_printers_btn()

    def select_add_printer_btn(self):
        if pytest.platform == "IOS":
            self.driver.swipe(direction="down", per_offset=0.6)
        self.driver.click("add_printer_btn")
    
    def verify_add_new_printer_screen(self):
        return self.driver.wait_for_object("add_printer_setup_title")
    
    def click_set_up_new_printer_option(self):
        self.driver.click("set_up_new_printer")

    def click_search_by_serial_number_option(self):
        self.driver.click("search_by_serial")

    def verify_connect_this_printer_option(self):
        self.driver.wait_for_object("connect_this_printer")

    def verify_search_by_serial_number_screen(self):
        self.driver.wait_for_object("search_by_serial_number_btn")