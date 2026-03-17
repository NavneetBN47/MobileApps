# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Let's find your network connected printer screen

@author: Ivan
@create_date: Dec 01, 2021
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class LetsFindYourNetworkConnectedPrinter(SmartScreens):
    folder_name = "oobe"
    flow_name = "lets_find_your_network_connected_printer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(LetsFindYourNetworkConnectedPrinter, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("lets_find_your_network_connected_printer_screen_printer_image", timeout=timeout, raise_e=raise_e)

    def wait_for_connect_printer_to_router_or_wired_access_point_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Connect printer to router or wired access point dialog load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[wait_for_connect_printer_to_router_or_wired_access_point_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_printer_to_router_or_wired_access_point_dialog_image", timeout=timeout, raise_e=raise_e)

    def click_lets_find_your_network_connected_printer_screen_back_btn(self):
        '''
        This is a method to click Back button on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[click_lets_find_your_network_connected_printer_screen_back_btn]-Click Back button... ")

        self.driver.click("lets_find_your_network_connected_printer_screen_back_btn", is_native_event=True)

    def click_lets_find_your_network_connected_printer_screen_search_again_btn(self):
        '''
        This is a method to click Search Again button on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[click_lets_find_your_network_connected_printer_screen_search_again_btn]-Click Search Again button... ")

        self.driver.click("lets_find_your_network_connected_printer_screen_search_again_btn", is_native_event=True)

    def click_show_me_how_text(self):
        '''
        This is a method to click Show me how text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[click_show_me_how_text]-Click Show me how text... ")

        self.driver.click("show_me_how_text", is_native_event=True)

    def click_connect_printer_to_router_or_wired_access_point_dialog_search_again_btn(self):
        '''
        This is a method to click Search Again button on Connect printer to router or wired access point dialog.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[click_connect_printer_to_router_or_wired_access_point_dialog_search_again_btn]-Click Search Again button...")

        self.driver.click("connect_printer_to_router_or_wired_access_point_dialog_search_again_btn", is_native_event=True)

    def click_connect_printer_to_router_or_wired_access_point_dialog_close_btn(self):
        '''
        This is a method to click Close button on Connect printer to router or wired access point dialog.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[click_connect_printer_to_router_or_wired_access_point_dialog_close_btn]-Click Close button...")

        self.driver.click("connect_printer_to_router_or_wired_access_point_dialog_close_btn", is_native_event=True)

    def get_value_of_lets_find_your_network_connected_printer_screen_title(self):
        '''
        This is a method to get the value of Let's find your network connected printer screen title.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_lets_find_your_network_connected_printer_screen_title]-Get the value of screen title...  ")

        return self.driver.get_value("lets_find_your_network_connected_printer_screen_title")

    def get_value_of_to_help_to_find_your_printer_text(self):
        '''
        This is a method to get the value of To help to find your printer text on Let's find your network connected printer screen
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_to_help_to_find_your_printer_text]-Get the value of To help to find your printer text...  ")

        return self.driver.get_value("to_help_to_find_your_printer_text")

    def get_value_of_make_sure_the_printer_is_plugged_text(self):
        '''
        This is a method to get the value of Make sure the printer is plugged text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_make_sure_the_printer_is_plugged_text]-Get the value of Make sure the printer is plugged text...  ")

        return self.driver.get_value("make_sure_the_printer_is_plugged_text")

    def get_value_of_temporarily_disconnect_your_computer_text(self):
        '''
        This is a method to get the value of Temporarily disconnect your computer text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_temporarily_disconnect_your_computer_text]-Get the value of Temporarily disconnect your computer text...  ")

        return self.driver.get_value("temporarily_disconnect_your_computer_text")

    def get_value_of_if_the_printer_is_already_text(self):
        '''
        This is a method to get the value of If the printer is already text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_if_the_printer_is_already_text]-Get the value of If the printer is already text...  ")

        return self.driver.get_value("if_the_printer_is_already_text")

    def get_value_of_if_using_ethernet_text(self):
        '''
        This is a method to get the value of If using ethernet text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_if_using_ethernet_text]-Get the value of If using ethernet text...  ")

        return self.driver.get_value("if_using_ethernet_text")

    def get_value_of_show_me_how_text(self):
        '''
        This is a method to get the value of Show me how text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_show_me_how_text]-Get the value of Show me how text...  ")

        return self.driver.get_value("show_me_how_text")

    def get_value_of_select_text(self):
        '''
        This is a method to get the value of Select text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_select_text]-Get the value of Select text...  ")

        return self.driver.get_value("select_text")

    def get_value_of_search_again_text(self):
        '''
        This is a method to get the value of Search again text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_search_again_text]-Get the value of Search again text...  ")

        return self.driver.get_value("search_again_text")

    def get_value_of_when_ready_if_your_printer_text(self):
        '''
        This is a method to get the value of When ready if your printer text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_when_ready_if_your_printer_text]-Get the value of When ready if your printer text...  ")

        return self.driver.get_value("when_ready_if_your_printer_text")

    def get_value_of_lets_find_your_network_connected_printer_screen_back_btn(self):
        '''
        This is a method to get the value of Back button on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_lets_find_your_network_connected_printer_screen_back_btn]-Get the value of Back button...  ")

        return self.driver.get_title("lets_find_your_network_connected_printer_screen_back_btn")

    def get_value_of_lets_find_your_network_connected_printer_screen_search_again_btn(self):
        '''
        This is a method to get the value of Search Again button on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_lets_find_your_network_connected_printer_screen_search_again_btn]-Get the value of When ready if your printer text...  ")

        return self.driver.get_title("lets_find_your_network_connected_printer_screen_search_again_btn")

    def get_value_of_connect_printer_to_router_or_wired_access_point_dialog_title(self):
        '''
        This is a method to get the value of Connect printer to router or wired access point dialog title after clicking Show me how text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_connect_printer_to_router_or_wired_access_point_dialog_title]-Get the value of Connect printer to router or wired access point dialog title...")

        return self.driver.get_value("connect_printer_to_router_or_wired_access_point_dialog_title")

    def get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_1(self):
        '''
        This is a method to get the value of Connect printer to router or wired access point dialog content - 1 after clicking Show me how text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_1]-Get the value of Connect printer to router or wired access point dialog content - 1...")

        return self.driver.get_value("connect_printer_to_router_or_wired_access_point_dialog_content_1")

    def get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_2(self):
        '''
        This is a method to get the value of Connect printer to router or wired access point dialog content - 2 after clicking Show me how text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_2]-Get the value of Connect printer to router or wired access point dialog content - 2...")

        return self.driver.get_value("connect_printer_to_router_or_wired_access_point_dialog_content_2")

    def get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_3(self):
        '''
        This is a method to get the value of Connect printer to router or wired access point dialog content - 3 after clicking Show me how text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_3]-Get the value of Connect printer to router or wired access point dialog content - 3...")

        return self.driver.get_value("connect_printer_to_router_or_wired_access_point_dialog_content_3")

    def get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_4(self):
        '''
        This is a method to get the value of Connect printer to router or wired access point dialog content - 4 after clicking Show me how text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_4]-Get the value of Connect printer to router or wired access point dialog content - 4...")

        return self.driver.get_value("connect_printer_to_router_or_wired_access_point_dialog_content_4")

    def get_value_of_connect_printer_to_router_or_wired_access_point_dialog_search_again_btn(self):
        '''
        This is a method to get the value of Search again button on Connect printer to router or wired access point dialog after clicking Show me how text on Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[LetsFindYourNetworkConnectedPrinter]:[get_value_of_connect_printer_to_router_or_wired_access_point_dialog_search_again_btn]-Get the value of Search again button on Connect printer to router or wired access point dialog...")

        return self.driver.get_title("connect_printer_to_router_or_wired_access_point_dialog_search_again_btn")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_lets_find_your_network_connected_printer_screen(self):
        '''
        This is a verification method to check UI strings of Let's find your network connected printer screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of Let's find your network connected printer screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='lets_find_your_network_connected_printer_screen')
        assert self.get_value_of_lets_find_your_network_connected_printer_screen_title() == test_strings['lets_find_your_network_connected_printer_screen_title']
        assert self.get_value_of_to_help_to_find_your_printer_text() == test_strings['to_help_to_find_your_printer_text']
        assert self.get_value_of_make_sure_the_printer_is_plugged_text() == test_strings['make_sure_the_printer_is_plugged_text']
        assert self.get_value_of_temporarily_disconnect_your_computer_text() == test_strings['temporarily_disconnect_your_computer_text']
        assert self.get_value_of_if_the_printer_is_already_text() == test_strings['if_the_printer_is_already_text']
        assert self.get_value_of_if_using_ethernet_text() == test_strings['if_using_ethernet_text']
        assert self.get_value_of_show_me_how_text() == test_strings['show_me_how_text']
        assert self.get_value_of_select_text() == test_strings['select_text']
        assert self.get_value_of_search_again_text() == test_strings['search_again_text']
        assert self.get_value_of_when_ready_if_your_printer_text() == test_strings['when_ready_if_your_printer_text']
        assert self.get_value_of_lets_find_your_network_connected_printer_screen_back_btn() == test_strings['lets_find_your_network_connected_printer_screen_back_btn']
        assert self.get_value_of_lets_find_your_network_connected_printer_screen_search_again_btn() == test_strings['lets_find_your_network_connected_printer_screen_search_again_btn']
 
    def verify_connect_printer_to_router_or_wired_access_point_dialog(self):
        '''
        This is a verification method to check UI strings of Connect printer to router or wired access point dialog.
        :parameter:
        :return:
        '''
        self.wait_for_connect_printer_to_router_or_wired_access_point_dialog_load()
        logging.debug("Start to verify UI string of Connect printer to router or wired access point dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_to_router_or_wired_access_point_dialog')
        assert self.get_value_of_connect_printer_to_router_or_wired_access_point_dialog_title() == test_strings['connect_printer_to_router_or_wired_access_point_dialog_title']
        assert self.get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_1() == test_strings['connect_printer_to_router_or_wired_access_point_dialog_content_1']
        assert self.get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_2() == test_strings['connect_printer_to_router_or_wired_access_point_dialog_content_2']
        assert self.get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_3() == test_strings['connect_printer_to_router_or_wired_access_point_dialog_content_3']
        assert self.get_value_of_connect_printer_to_router_or_wired_access_point_dialog_content_4() == test_strings['connect_printer_to_router_or_wired_access_point_dialog_content_4']
        assert self.get_value_of_connect_printer_to_router_or_wired_access_point_dialog_search_again_btn() == test_strings['connect_printer_to_router_or_wired_access_point_dialog_search_again_btn']