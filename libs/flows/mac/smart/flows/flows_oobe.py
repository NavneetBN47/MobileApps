# encoding: utf-8
'''
Description: It defines common flows in the OOBE section.

@author: Sophia
@create_date: May 6, 2019
'''

import logging
from time import sleep

import MobileApps.resources.const.mac.const as smart_const
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.system.screens.system_preferences import SystemPreferences
from MobileApps.libs.flows.mac.smart.screens.oobe.ows import OWS
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.hpid.sign_up_dialog import SignUpDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.let_find_your_printer import FindYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_a_printer_to_set_up import ChooseAPrinterToSetUp
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_connected_to_wifi import PrinterConnectedtoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.print_from_other_devices import PrintFromOtherDevices
from MobileApps.libs.flows.mac.smart.screens.oobe.send_another_link_dialog import SendAnotherLinkDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_printer_to_wifi import ConnectPrintertoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_a_printer_to_set_up import ChooseAPrinterToSetUp
from MobileApps.libs.flows.mac.smart.screens.oobe.connecting_printer_to_wifi import ConnectingPrintertoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.install_driver_to_print import InstallDriverToPrint
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_lets_print import PrinterSetupLetsPrint
#from MobileApps.libs.flows.mac.smart.screens.oobe.what_type_of_printer_are_you_trying_to_find import WhatTypeOfPrinterAreYouTryingToFind
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_using_usb import ConnectUsingUSB
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_a_connection_method_dialog import ChooseCnnectionMethodDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.switch_to_using_wifi import SwitchToUsingWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_printer_with_ethernet import ConnectPrinterWithEthernet
from MobileApps.libs.flows.mac.smart.screens.oobe.we_could_not_find_your_printer_dialog import WeCouldNotFindYourPrinterDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_connected import PrinterConnected
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_to_wifi import ConnectToWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.wireless_setup_using_usb import WirelessSetupUsingUSB
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_your_computer_to_the_wifi_network import ConnectYourComputerToTheWiFiNetwork
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_your_computer_to_the_network import ConnectYourComputerToTheNetwork
from MobileApps.libs.flows.mac.smart.screens.common.connected_printing_services import ConnectedPrintingServices
from MobileApps.libs.flows.mac.smart.screens.hpid.sign_in_dialog import SigninDialog
from MobileApps.libs.flows.mac.smart.screens.hpid.getting_the_most_out_of_your_account import GettingTheMostOutOfYourAccount
from MobileApps.libs.flows.mac.smart.screens.oobe.ows_yeti import OWS_Yeti
#from MobileApps.libs.flows.mac.smart.screens.oobe.put_the_printer_into_wifi_setup_mode import PutThePrinterIntoWifiSetupMode
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_your_printer import ChooseYourPrinter



class OOBEFlows(object):

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        self.driver = driver

    def __designjet_flow(self, ows_screen):
        # TODO: need manual test cases
        '''
        This is a flow for DesignJet in OWS.
        :parameter:
        :return:
        '''
        pass

    def __laserjet_flow(self, ows_screen):
        '''
        This is a flow for LaserJet in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for LaserJet printer... ")

        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def __ciss_inkjet_flow(self, ows_screen):
        '''
        This is a flow for CISS printer in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for CISS printer or Non-II printer... ")

        self.__go_through_enjoy_hp_acct(ows_screen)
        self.__go_through_register_printer(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __taiji_gen1_inkjet_flow(self, ows_screen):
        '''
        This is a flow for TaiJi in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for TaiJi printer... ")

        # TODO: OWS need fully reset OOBE printer to finish
        self.__go_through_hardware_setup(ows_screen)
        self.__instant_ink_flow(ows_screen)
        self.__go_through_register_printer(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __lhasaboom_gen1_inkjet_flow(self, ows_screen):
        '''
        This is a flow for Lhasa Boom in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for Lhasa Boom printer... ")

        ows_screen.wait_for_cartridges_install_load(60)
        ows_screen.wait_for_skip_btn_shows(120)
        ows_screen.click_skip_btn_cartridges_install()

        self.__go_through_hardware_setup(ows_screen)
        self.__instant_ink_flow(ows_screen)
        self.__go_through_register_printer(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __others_gen1_inkjet_flow(self, ows_screen):
        '''
        This is a flow for other Gen 1 InkJet printers in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for Gen 1 printer... ")

        self.__instant_ink_flow(ows_screen)
        self.__go_through_register_printer(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __verona_gen2_inkjet_flow(self, ows_screen, usename, password):
        '''
        This is a flow for Verona in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for Verona family printer... ")

        # TODO: OWS need fully reset OOBE printer to finish
        self.__go_through_enjoy_hp_acct(ows_screen, usename, password)
        self.__instant_ink_flow(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __palermo_gen2_inkjet_flow(self, ows_screen, usename, password):
        '''
        This is a flow for Palermo in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for Palermo family printer... ")

        # TODO: OWS need fully reset OOBE printer to finish
        self.__go_through_enjoy_hp_acct(ows_screen, usename, password)
        self.__instant_ink_flow(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __tango_gen2_inkjet_flow(self, ows_screen):
        '''
        This is a flow for Tango in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for HP Tango printer... ")

        self.__go_through_enjoy_hp_acct(ows_screen)
        # TODO: OWS need fully reset OOBE printer to finish
        self.__instant_ink_flow(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __go_through_enjoy_hp_acct(self, ows_screen, usename, password):
        '''
        This is a flow from enjoy hp account then to hp id sign in dialog.
        :parameter:
        :return:
        '''
        connected_printing_services = ConnectedPrintingServices(self.driver)
        if connected_printing_services.wait_for_screen_load(timeout=120, raise_e=False):
            sleep(5)
            connected_printing_services.click_connected_printing_sevices_continue_btn()
        ows_screen.wait_for_enjoy_hp_account_load()
        sleep(2)
        ows_screen.click_sign_in_btn_enjoy_hp_account()
        self.go_through_sign_in_flow(usename, password)

    def __go_through_hardware_setup(self, ows_screen):
        '''
        This is a flow from hardware setup finish/alignment finish/cartridges installed or
        paper loaded, then to instant ink screen.
        :parameter:
        :return:
        '''
        if ows_screen.wait_for_cartridges_install_load(60, raise_e=False):
            ows_screen.click_continue_btn_cartridges_install()

    def __go_through_register_printer(self, ows_screen):
        '''
        This is a flow from register your printer with HP to next screen.
        :parameter:
        :return:
        '''
        ows_screen.wait_for_register_printer_load(60)
        ows_screen.click_skip_btn_register_printer()

    def __instant_ink_flow(self, ows_screen):
        '''
        This is a flow from instant ink advertisement screen to reminder screen.
        :parameter:
        :return:
        '''
        sleep(20)
#         ows_screen.wait_for_starting_printer_alignment_content_load()
        ows_screen.wait_for_hp_instant_ink_advertisement_load(300)
        ows_screen.click_continue_btn_hp_instant_ink_advertisement()
        if ows_screen.wait_for_hp_instant_ink_plan_load(60, raise_e=False):
            ows_screen.choose_no_instank_ink_radio_btn()
            ows_screen.click_continue_btn_hp_instant_ink_plan()
            ows_screen.wait_for_reminder_load(60)
            ows_screen.click_reminder_me_btn_reminder()
            if ows_screen.wait_for_account_created_screen_load(timeout=60, raise_e=False):
                ows_screen.click_continue_setup_btn()
        else:
            ows_screen.wait_for_confirm_your_details_to_receive_ink_screen_load()
            ows_screen.click_skip_ink_savings_btn()
            ows_screen.wait_for_are_you_sure_you_want_to_skip_dialog_load()
            ows_screen.click_are_your_sure_you_want_to_skip_dialog_yes_skip_offer_btn()

    def __help_make_better_product_flow(self, ows_screen):
        '''
        This is a method to set up information on the help HP make better product screen
        :parameter:
        :return:
        '''
        ows_screen.wait_for_help_hp_make_better_load()
        if ows_screen.wait_for_radio_btn_shows(timeout=5, raise_e=False):
            ows_screen.choose_in_home_radio_btn()
            ows_screen.click_in_home_drop_down_list()
            ows_screen.choose_in_home_drop_down_list_item()
        ows_screen.set_postal_code(smart_const.PRINTER_INFO.POSTAL_CODE)
        ows_screen.click_continue_btn_help_better()

    __ows_switcher = {
        0: __designjet_flow,
        1: __laserjet_flow,
        2: __ciss_inkjet_flow,
        3: __taiji_gen1_inkjet_flow,
        4: __lhasaboom_gen1_inkjet_flow,
        5: __others_gen1_inkjet_flow,
        6: __verona_gen2_inkjet_flow,
        7: __palermo_gen2_inkjet_flow,
        8: __tango_gen2_inkjet_flow
    }

    def go_through_ows_flow(self, printer_ows_type, username, password):
        '''
        This is a method to go through OWS flow during the OOBE setup.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow... ")

        ows_screen = OWS(self.driver)
        return self.__ows_switcher.get(printer_ows_type, lambda: 'Invalid printer OWS type...')(self, ows_screen, username, password)

    def go_through_to_instant_ink_flow(self):
        '''
        This is a method to go through OOBE flow to Instant Ink plan screen from Enjoy Your printer screen with Palermo GEN2 printer.
        :parameter:
        :return:
        '''
        logging.debug("Go through Enjoy HP Account Screen")
        ows_screen = OWS(self.driver)
        ows_screen.wait_for_enjoy_hp_account_load(360)
        sleep(2)
        ows_screen.click_continue_btn_enjoy_hp_account()
        sign_up_dialog = SignUpDialog(self.driver)
        if sign_up_dialog.wait_for_screen_load(raise_e=False):
            sign_up_dialog.click_close_btn()

        logging.debug("Go through Hardware Setup screen")
        if ows_screen.wait_for_cartridges_install_load(60, raise_e=False):
            ows_screen.click_continue_btn_cartridges_install()

        logging.debug("Go through Instant Ink Plan page")
        ows_screen.wait_for_hp_instant_ink_advertisement_load(120)
        ows_screen.click_continue_btn_hp_instant_ink_advertisement()
        ows_screen.wait_for_hp_instant_ink_plan_load(60)
        ows_screen.choose_first_instank_ink_plan_radio_btn()
        ows_screen.click_continue_btn_hp_instant_ink_plan()

    def go_through_to_reminder_me_flow(self):
        '''
        This is a method to go through OOBE flow to Reminder me screen from Enjoy Your printer screen with Palermo GEN2 printer.
        :parameter:
        :return:
        '''
        logging.debug("Go through Enjoy HP Account Screen")
        ows_screen = OWS(self.driver)
        ows_screen.wait_for_enjoy_hp_account_load(360)
        sleep(2)
        ows_screen.click_skip_btn_enjoy_hp_account()
        ows_screen.wait_for_dont_miss_out_on_your_automatic_printer_warranty_load()
        ows_screen.click_skip_btn_dont_miss_out()

        logging.debug("Go through Hardware Setup screen")
        if ows_screen.wait_for_cartridges_install_load(60, raise_e=False):
            ows_screen.click_continue_btn_cartridges_install()

        logging.debug("Go through to Reminder me screen")
        ows_screen.wait_for_hp_instant_ink_advertisement_load(120)
        ows_screen.click_continue_btn_hp_instant_ink_advertisement()
        ows_screen.wait_for_hp_instant_ink_plan_load(60)
        ows_screen.choose_no_instank_ink_radio_btn()
        ows_screen.click_continue_btn_hp_instant_ink_plan()
        ows_screen.wait_for_reminder_load(60)
        ows_screen.click_reminder_me_btn_reminder()

    def go_through_sign_in_flow(self, username, password):
        '''
        This is a flow to sign in on HPID popup dialog.
        :parameter:
        :return:
        '''
        sign_in_dialog = SigninDialog(self.driver)
        sign_in_dialog.wait_for_screen_load(60)
        sign_in_dialog.input_username_inputbox(username)
#         sign_in_dialog.click_sign_in_dialog_next_btn()
        sleep(5)
        sign_in_dialog.wait_for_sign_in_dialog_password_inputbox_load(60)
        sign_in_dialog.input_password_inputbox(password)
#         sign_in_dialog.click_sign_in_dialog_sign_in_btn()

        sign_in_dialog.verify_dialog_disappear()
        sleep(1)

        getting_the_most_out_of_your_account_page = GettingTheMostOutOfYourAccount(self.driver)
        if getting_the_most_out_of_your_account_page.wait_for_screen_load(raise_e=False):
            getting_the_most_out_of_your_account_page.click_getting_the_most_out_of_your_account_title()
            getting_the_most_out_of_your_account_page.click_getting_the_most_out_of_your_account_continue_btn()

    def go_through_to_select_a_printer_screen(self):
        '''
        This is a setup printer flow with no beaconing printer.
        :parameter:
        :return:
        '''
        logging.debug("Go through OOBE flow to Select a printer screen from Let's find your printer screen for without beaconing printer")
        let_find_your_printer = FindYourPrinter(self.driver)
        let_find_your_printer.verify_lets_find_your_printer_screen()
        let_find_your_printer.click_continue_btn()

        choose_a_printer_to_set_up_screen = ChooseAPrinterToSetUp(self.driver)
        choose_a_printer_to_set_up_screen.verify_select_a_printer_screen()

    def no_beaconing_printer_setup_flow(self, printer_name):
        '''
        This is a setup printer flow with no beaconing printer.
        :parameter:
        :return:
        '''
        logging.debug("Go through OOBE flow to Printer connected screen from Let's find your printer screen for without beaconing printer")
        self.go_through_to_select_a_printer_screen()

        choose_a_printer_to_set_up_screen = ChooseAPrinterToSetUp(self.driver)
        choose_a_printer_to_set_up_screen.click_to_selected_printer(printer_name)

        we_found_your_printer = WeFoundYourPrinter(self.driver)
        we_found_your_printer.verify_we_found_your_printer_without_title_screen()
        we_found_your_printer.click_continue_btn()

        printer_connected = PrinterConnected(self.driver)
        printer_connected.verify_printer_connected_screen()
        printer_connected.click_continue_btn()

    def navigate_flow_to_connect_printer_to_wifi_screen(self):
        '''
        This is a flow for navigate to Connect Printer to WiFi screen from We found your printer screen.
        :parameter:
        :return:
        '''
        we_found_your_printer = WeFoundYourPrinter(self.driver)
        if we_found_your_printer.wait_for_screen_load(raise_e=False):
            we_found_your_printer.verify_we_found_your_printer_screen()
        else:
            we_found_your_printer.verify_we_found_your_printer_without_title_screen()
        we_found_your_printer.click_continue_btn()

    def navigate_to_unable_to_access_wifi_password_dialog(self):
        '''
        This is a flow for go to Unable to Access Wi-Fi Password dialog with select Deny button on Security Agent dialog.
        :parameter:
        :return:
        '''
        connect_printer_to_wifi = ConnectPrintertoWiFi(self.driver)
        connect_printer_to_wifi.verify_access_wifi_password_dialog()
        connect_printer_to_wifi.click_continue_btn_on_access_wifi_password()
        security_agent_dialog = SystemPreferences(self.driver)
        security_agent_dialog.wait_for_security_agent_dialog_load()
        security_agent_dialog.click_security_agent_deny_btn()
        connect_printer_to_wifi.verify_unable_to_access_wifi_password_dialog()

    def continue_btn_flow_to_connecting_printer_to_wifi(self, system_username, system_password):
        '''
        This is a flow for go to Connecting Printer to WiFi screen with select Continue button on Access Wi-Fi Password dialog.
        :parameter: system_username - the required system user name for Security Agent dialog.
                    system_password - the required system password for Security Agent dialog.
        :return:
        '''
        connect_printer_to_wifi = ConnectPrintertoWiFi(self.driver)
        connect_printer_to_wifi.verify_access_wifi_password_dialog()
        connect_printer_to_wifi.click_continue_btn_on_access_wifi_password()
        security_agent_dialog = SystemPreferences(self.driver)
        security_agent_dialog.wait_for_security_agent_dialog_load()
        security_agent_dialog.input_username(system_username)
        security_agent_dialog.input_password(system_password)
        security_agent_dialog.click_security_agent_allow_btn()
        if security_agent_dialog.wait_for_security_agent_dialog_load(timeout=5, raise_e=False):
            security_agent_dialog.input_password(system_password)
            security_agent_dialog.click_security_agent_allow_btn()

    def no_thanks_flow_to_connecting_printer_to_wifi(self, printer_name, wifi_name, wifi_password):
        '''
        This is a flow for go to Connecting Printer to WiFi screen with select No Thanks button on Access Wi-Fi Password dialog.
        :parameter: printer_name - Your tested printer name.
                    wifi_name - Your current connected Wi-Fi name.
                    wifi_password - Your current connected Wi-Fi password.
        :return:
        '''
        connect_printer_to_wifi = ConnectPrintertoWiFi(self.driver)
        connect_printer_to_wifi.verify_access_wifi_password_dialog()
        connect_printer_to_wifi.click_no_thanks_btn_on_access_wifi_password()
        connect_printer_to_wifi.verify_connect_printer_to_wifi_screen(printer_name, wifi_name)
        connect_printer_to_wifi.input_enter_wifi_password_box(wifi_password)
        connect_printer_to_wifi.click_connect_btn()

    def access_link_flow_to_connecting_printer_to_wifi(self, printer_name, wifi_name, system_username, system_password):
        '''
        This is a flow for go to Connecting Printer to WiFi screen with select "Access my Wi-Fi password automatically" link on "Connect printer to Wi-Fi" screen.
        :parameter: printer_name - Your tested printer name.
                    wifi_name - Your current connected Wi-Fi name.
                    system_username - the required system user name for Security Agent dialog.
                    system_password - the required system password for Security Agent dialog.
        :return:
        '''
        connect_printer_to_wifi = ConnectPrintertoWiFi(self.driver)
        connect_printer_to_wifi.verify_access_wifi_password_dialog()
        connect_printer_to_wifi.click_no_thanks_btn_on_access_wifi_password()
        connect_printer_to_wifi.verify_access_wifi_password_dialog_dismiss()
        connect_printer_to_wifi.verify_connect_printer_to_wifi_screen(printer_name, wifi_name)
        connect_printer_to_wifi.click_access_my_wifi_password_automatically_link()

        security_agent_dialog = SystemPreferences(self.driver)
        security_agent_dialog.wait_for_security_agent_dialog_load()
        security_agent_dialog.input_username(system_username)
        security_agent_dialog.input_password(system_password)
        security_agent_dialog.click_security_agent_allow_btn()
        if security_agent_dialog.wait_for_security_agent_dialog_load(timeout=5, raise_e=False):
            security_agent_dialog.input_password(system_password)
            security_agent_dialog.click_security_agent_allow_btn()

    def go_through_connected_to_wifi_flow(self, printer_name, wifi_name, wifi_password):
        '''
        This is a flow from "connect printer to WIFI" screen to "printer connected to WIFI" screen.
        :parameter: wifi_password - the required WIFI password on connect printer to WIFI screen.
        :return:
        '''
        logging.debug("Go through printer connected to WIFI flow... ")

        self.no_thanks_flow_to_connecting_printer_to_wifi(printer_name, wifi_name, wifi_password)

        connecting_printer_to_wifi = ConnectingPrintertoWiFi(self.driver)
        connecting_printer_to_wifi.verify_connecting_printer_to_wifi_screen()

        printer_connected_to_wifi = PrinterConnectedtoWiFi(self.driver)
        printer_connected_to_wifi.verify_printer_connected_to_wifi_screen()
        printer_connected_to_wifi.click_continue_btn()

    def go_to_we_can_help_connect_your_printer_screen(self):
        '''
        This is method to go to We can help connect your printer screen from select "No, Continue with Ethernet" opt on Switch to Using WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to We can help connect your printer screen")
        switch_to_using_wifi = SwitchToUsingWiFi(self.driver)
        switch_to_using_wifi.verify_switch_to_using_wifi_screen()
        switch_to_using_wifi.click_no_continue_with_ethernet_opt()
        switch_to_using_wifi.verify_continue_btn_is_enabled()
        switch_to_using_wifi.click_continue_btn()

        what_type_of_printer_are_you_trying_to_find_screen = WhatTypeOfPrinterAreYouTryingToFind(self.driver)
        what_type_of_printer_are_you_trying_to_find_screen.verify_what_type_of_printer_are_you_trying_to_find_screen()

    def go_through_connect_your_computer_to_the_wifi_network_screen(self):
        '''
        This is method to Enable continue button by clicking Open network settings button on Connect your computer to the Wi-Fi network screen.
        :parameter:
        :return:
        '''
        connect_your_computer_to_the_wifi_network = ConnectYourComputerToTheWiFiNetwork(self.driver)
        connect_your_computer_to_the_wifi_network.verify_connect_your_computer_to_the_wifi_network_screen()
        connect_your_computer_to_the_wifi_network.click_open_network_settings_btn()

        network_page = SystemPreferences(self.driver)
        sleep(4)
        network_page.click_close_network_page_btn()
        connect_your_computer_to_the_wifi_network.wait_for_screen_load()
        connect_your_computer_to_the_wifi_network.verify_continue_btn_is_enabled()

    def go_to_connect_your_computer_to_the_wifi_network_flow_for_ethernet_network(self):
        '''
        This is method to go to Connect your computer to the Wi-Fi network screen from select "Yes, Switch to WiFi" opt on Switch to Using WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to We can help connect your printer screen")
        switch_to_using_wifi = SwitchToUsingWiFi(self.driver)
        switch_to_using_wifi.verify_switch_to_using_wifi_screen()
        switch_to_using_wifi.click_yes_switch_to_wifi_opt()
        switch_to_using_wifi.verify_continue_btn_is_enabled()
        switch_to_using_wifi.click_continue_btn()

        self.go_through_connect_your_computer_to_the_wifi_network_screen()

    def go_to_connect_your_computer_to_the_wifi_network_flow_for_no_network(self):
        '''
        This is method to go to Connect your printer to your WiFi network screen from select "Yes, connect to network" opt on Connect your printer to your network screen during OOBE USB flow
        :parameter:
        :return:
        '''
        connect_your_computer_to_the_network = ConnectYourComputerToTheNetwork(self.driver)
        connect_your_computer_to_the_network.verify_connect_your_computer_to_the_network_screen()
        connect_your_computer_to_the_network.select_yes_connect_to_network_opt()
        connect_your_computer_to_the_network.click_continue_btn()

        self.go_through_connect_your_computer_to_the_wifi_network_screen()

    def go_to_what_type_of_printer_are_you_trying_to_find_screen_flow(self):
        '''
        This is method to go to What type of printer are you trying to find screen after clicking My printer isn't listed button on Device Picker screen.
        Precondition: If your test network has Wi-Fi Direct on Yeti printer, Addtional screens will shows before What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        choose_your_printer = ChooseYourPrinter(self.driver)
        put_the_printer_into_wifi_setup_mode_screen = PutThePrinterIntoWifiSetupMode(self.driver)
        what_type_of_printer_are_you_trying_to_find_screen = WhatTypeOfPrinterAreYouTryingToFind(self.driver)
        if choose_your_printer.wait_for_screen_load(timeout=120, raise_e=False):
            choose_your_printer.click_printer_not_listed_btn()
            put_the_printer_into_wifi_setup_mode_screen.wait_for_screen_load(120)
            put_the_printer_into_wifi_setup_mode_screen.click_exit_setup_btn()
        elif put_the_printer_into_wifi_setup_mode_screen.wait_for_put_the_printer_into_wifi_setup_mode_screen_load(raise_e=False):
            put_the_printer_into_wifi_setup_mode_screen.click_change_printer_btn()
            put_the_printer_into_wifi_setup_mode_screen.wait_for_screen_load(120)
            put_the_printer_into_wifi_setup_mode_screen.click_exit_setup_btn()
        elif put_the_printer_into_wifi_setup_mode_screen.wait_for_screen_load(raise_e=False):
            put_the_printer_into_wifi_setup_mode_screen.click_exit_setup_btn()
        else:
            what_type_of_printer_are_you_trying_to_find_screen.wait_for_screen_load()

    def go_to_connecting_printer_to_wifi_wireless_setup(self):
        '''
        This is method to go to Connecting printer to WiFi... screen from select WiFi opt on We can help connect your printer screen
        :parameter:
        :return:
        '''
        logging.debug("Go to connecting printer to wifi.. screen... ")
        what_type_of_printer_are_you_trying_to_find_screen = WhatTypeOfPrinterAreYouTryingToFind(self.driver)
        what_type_of_printer_are_you_trying_to_find_screen.verify_what_type_of_printer_are_you_trying_to_find_screen()
        what_type_of_printer_are_you_trying_to_find_screen.select_wireless_radio()
        what_type_of_printer_are_you_trying_to_find_screen.click_continue_btn()

        connect_to_wifi_screen = ConnectToWiFi(self.driver)
        connect_to_wifi_screen.verify_connect_to_wifi_screen()

    def go_to_wireless_setup_using_usb(self):
        '''
        This is method to go to Wireless setup using USB screen from connecting printer to wifi..screen
        :parameter:
        :return:
        '''
        logging.debug("go to Wireless setup using USB  screen... ")

        connect_to_wifi_screen = ConnectToWiFi(self.driver)
        connect_to_wifi_screen.click_no_opt()
        connect_to_wifi_screen.click_continue_btn()

        wireless_setup_using_usb = WirelessSetupUsingUSB(self.driver)
        wireless_setup_using_usb.verify_wireless_setup_using_usb_screen()

    def go_to_connect_printer_with_ethernet_screen(self):
        '''
        This is method to go to Connect printer with Ethernet screen from select Ethernet opt on We can help connect your printer screen during OOBE Ethernet flow
        :parameter:
        :return:
        '''
        logging.debug("Go to Connect printer with Ethernet screen... ")
        what_type_of_printer_are_you_trying_to_find_screen = WhatTypeOfPrinterAreYouTryingToFind(self.driver)
        what_type_of_printer_are_you_trying_to_find_screen.verify_what_type_of_printer_are_you_trying_to_find_screen()
        what_type_of_printer_are_you_trying_to_find_screen.select_ethernet_radio()
        what_type_of_printer_are_you_trying_to_find_screen.click_continue_btn()

        connect_printer_with_ethernet = ConnectPrinterWithEthernet(self.driver)
        connect_printer_with_ethernet.verify_connect_printer_with_ethernet_screen()

    def go_to_printer_connected_screen_in_ethernet_flow(self):
        '''
        This is a flow from Connect your printer to your network screen to Printer connected screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to printer connected screen... ")
        connect_printer_with_ethernet = ConnectPrinterWithEthernet(self.driver)
        connect_printer_with_ethernet.click_connect_printer_btn()

        we_could_not_find_your_printer_dialog = WeCouldNotFindYourPrinterDialog(self.driver)
        if we_could_not_find_your_printer_dialog.wait_for_screen_load(timeout=300, raise_e=False):
            we_could_not_find_your_printer_dialog.click_try_again_btn()
        we_found_your_printer = WeFoundYourPrinter(self.driver)
        we_found_your_printer.verify_we_found_your_printer_screen()
        we_found_your_printer.click_continue_btn()
        printer_connected = PrinterConnected(self.driver)
        printer_connected.verify_printer_connected_screen()

    def go_to_connect_using_usb_screen(self):
        '''
        This is method to go to Connect Using USB screen from select USB opt on We can help connect your printer screen during OOBE Ethernet flow
        :parameter:
        :return:
        '''
        logging.debug("Go to Connect your printer to your network screen... ")
        what_type_of_printer_are_you_trying_to_find_screen = WhatTypeOfPrinterAreYouTryingToFind(self.driver)
        what_type_of_printer_are_you_trying_to_find_screen.verify_what_type_of_printer_are_you_trying_to_find_screen()
        what_type_of_printer_are_you_trying_to_find_screen.select_usb_radio()
        what_type_of_printer_are_you_trying_to_find_screen.click_continue_btn()

        connect_using_usb = ConnectUsingUSB(self.driver)
        connect_using_usb.verify_connect_using_usb_screen()

    def go_to_printer_connected_screen_usb_flow(self):
        '''
        This is method to go to Printer Connected screen (USB) from select USB opt on We can help connect your printer screen during Set up a new printer flow.
        :parameter:
        :return:
        '''
        self.go_to_connect_using_usb_screen()
        connect_using_usb = ConnectUsingUSB(self.driver)
        connect_using_usb.click_connect_printer_btn()
        we_found_your_printer = WeFoundYourPrinter(self.driver)
        we_found_your_printer.wait_for_screen_load()
        we_found_your_printer.click_continue_btn()
        printer_connected = PrinterConnected(self.driver)
        printer_connected.verify_printer_connected_screen_usb()
        printer_connected.click_continue_btn()

    def check_wifi_printer_initial_set_up_or_wifi_reset_dialog_flow(self):
        '''
        This is a method to check Wi-Fi printer initial set up or Wi-Fi reset dialog after clicking info button under Setup Mode Printer section on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("Check 'Wi-Fi printer initial set up or Wi-Fi reset dialog' flow")
        what_type_of_printer_are_you_trying_to_find_screen = WhatTypeOfPrinterAreYouTryingToFind(self.driver)
        what_type_of_printer_are_you_trying_to_find_screen.wait_for_screen_load()
        what_type_of_printer_are_you_trying_to_find_screen.click_setup_mode_printer_info_btn()
        what_type_of_printer_are_you_trying_to_find_screen.verify_wifi_printer_initial_set_up_or_wifi_reset_dialog()
        what_type_of_printer_are_you_trying_to_find_screen.click_info_dialog_ok_btn()
        what_type_of_printer_are_you_trying_to_find_screen.wait_for_screen_load()

    def check_check_for_network_connection_dialog_flow(self):
        '''
        This is a method to check Check for network connection dialog after clicking info button under Network Printer section on What type of printer are you trying to find screen.
        :parameter:
        :return:
        '''
        logging.debug("Check 'Check for network connection dialog' flow")
        what_type_of_printer_are_you_trying_to_find_screen = WhatTypeOfPrinterAreYouTryingToFind(self.driver)
        what_type_of_printer_are_you_trying_to_find_screen.wait_for_screen_load()
        what_type_of_printer_are_you_trying_to_find_screen.click_network_printer_info_btn()
        what_type_of_printer_are_you_trying_to_find_screen.verify_check_for_network_connection_dialog()
        what_type_of_printer_are_you_trying_to_find_screen.click_info_dialog_ok_btn()
        what_type_of_printer_are_you_trying_to_find_screen.wait_for_screen_load()

    def click_change_printer_flow_on_we_found_your_printer(self):
        '''
        This is method for click change printer link flow on We Found Your Printer screen during AWC flow.
        :parameter:
        :return:
        '''
        we_found_your_printer = WeFoundYourPrinter(self.driver)
        we_found_your_printer.wait_for_screen_load(600)
        we_found_your_printer.click_change_printer_btn()

        choose_a_printer_to_set_up_screen = ChooseAPrinterToSetUp(self.driver)
        choose_a_printer_to_set_up_screen.wait_for_screen_load()

#     def go_through_flow_to_main_ui_after_ows(self):
#         '''
#         This is a flow from 'printer from other devices' screen to main UI.
#         Click Send Link button to go through Print from other devices screen
#         Click Print button to go through Printer setup lets print screen
#         :parameter:
#         :return:
#         '''
#         logging.debug("Click Send Link button to go through Print from other devices screen")
#         print_from_other_devices = PrintFromOtherDevices(self.driver)
#         print_from_other_devices.verify_print_from_other_devices_screen()
#         print_from_other_devices.click_send_link_btn()
#         print_from_other_devices.select_email_menu_item()
#         sleep(2)
#         print_from_other_devices.click_quit_btn()
# 
#         send_another_link_dialog = SendAnotherLinkDialog(self.driver)
#         send_another_link_dialog.verify_send_another_link_dialog()
#         send_another_link_dialog.click_done_btn()
# 
#         install_driver_to_print = InstallDriverToPrint(self.driver)
#         install_driver_to_print.verify_success_print_installed_dialog()
#         install_driver_to_print.click_ok_btn()
# 
#         logging.debug("Click Print button to go through Printer setup lets print screen")
#         printer_setup_lets_print = PrinterSetupLetsPrint(self.driver)
#         printer_setup_lets_print.verify_printer_setup_lets_print_screen()
#         printer_setup_lets_print.click_print_btn()
#         printer_setup_lets_print.wait_for_print_dialog_load()
#         printer_setup_lets_print.click_print_btn_on_print_dialog()
# 
#         main_screen = MainUI(self.driver)
#         main_screen.wait_for_screen_load(60)

    def go_through_oobe_flow_after_printer_connected(self, printer_type):
        '''
        This is a flow from OWS screen to main UI.
        Click Skip sending this link button to go through Print from other devices screen
        Click No now button to go through Printer setup lets print screen
        :parameter:
        :return:
        '''
        self.go_through_ows_flow(printer_type)
        self.go_through_flow_to_main_ui_after_ows()

    def go_through_flow_to_main_ui_after_ows(self):
        logging.debug("Click Skip sending this link button to go through Print from other devices screen")
        print_from_other_devices = PrintFromOtherDevices(self.driver)
        print_from_other_devices.verify_print_from_other_devices_screen()
        print_from_other_devices.click_skip_sending_this_link_btn()

        install_driver_to_print = InstallDriverToPrint(self.driver)
        if install_driver_to_print.wait_for_install_success_screen_load(120, raise_e=False):
            install_driver_to_print.verify_success_print_installed_dialog()
            install_driver_to_print.click_ok_btn()
        else:
            install_driver_to_print.click_printers_scanners_btn()
            printer_screen = SystemPreferences(self.driver)
            printer_screen.click_close_printers_scanners_btn()
            install_driver_to_print.click_continue_btn()

        logging.debug("Click No now button to go through Printer setup lets print screen")
        printer_setup_lets_print = PrinterSetupLetsPrint(self.driver)
        if printer_setup_lets_print.wait_for_screen_load(timeout=120, raise_e=False):
            printer_setup_lets_print.verify_printer_setup_lets_print_screen()
            printer_setup_lets_print.click_skip_printing_file_btn()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(60)

    def sign_in_hp_account_from_sign_up_dialog(self, username, password):
        sign_up_dialog = SignUpDialog(self.driver)
        sign_up_dialog.wait_for_screen_load(120)
        sign_up_dialog.click_already_have_an_hp_account_sign_in_btn()

        self.go_through_sign_in_flow(username, password)

    def go_to_enjoy_account_or_get_more_value_screen_in_awc_flow(self, wifi_password):
        '''
        This is method to go to enjoy_account screen or get_more_value_from_your_printing_experience  during OOBE AWC flow
        :parameter:
        :return:
        '''
        we_found_your_printer = WeFoundYourPrinter(self.driver)
        we_found_your_printer.wait_for_screen_without_title_load()
        we_found_your_printer.click_continue_btn()
        connect_printer_to_wifi = ConnectPrintertoWiFi(self.driver)
        connect_printer_to_wifi.click_no_thanks_btn_on_access_wifi_password()
        sleep(3)
        connect_printer_to_wifi.input_enter_wifi_password_box(wifi_password)
        connect_printer_to_wifi.click_connect_btn()
        printer_connected_to_wifi = PrinterConnectedtoWiFi(self.driver)
        printer_connected_to_wifi.wait_for_screen_load(600)
        printer_connected_to_wifi.click_continue_btn()
        connected_printing_services = ConnectedPrintingServices(self.driver)
        if connected_printing_services.wait_for_screen_load(180, raise_e=False):
            connected_printing_services.click_connected_printing_sevices_continue_btn()

    def go_through_flex_flow_before_not_sign_in(self, username, password):
        ows_yeti = OWS_Yeti(self.driver)
        ows_yeti.wait_for_get_more_value_from_your_printing_experience_load(180)
        ows_yeti.click_get_more_value_from_your_printing_experience_do_not_activate_hp_plus_btn()
        ows_yeti.wait_for_are_you_sure_dialog_load()
        ows_yeti.click_are_you_sure_dialog_decline_hp_plus_btn()
        ows_yeti.wait_for_create_hp_account_or_sign_in_to_register_your_printer_load()
        sleep(8)
        ows_yeti.click_sign_in_btn()
        self.go_through_sign_in_flow(username, password)
        sleep(120)
#         ows_yeti.wait_for_welcome_of_flex_screen_load()
#         sleep(5)
#         ows_yeti.click_welcome_screen_of_flex_continue_btn()

    def go_through_e2e_flow_before_not_sign_in(self, username, password):
        ows_yeti = OWS_Yeti(self.driver)
        ows_yeti.wait_for_get_more_value_from_your_printing_experience_load(180)
        ows_yeti.click_get_more_value_from_your_printing_experience_continue_btn()
        ows_yeti.wait_for_your_printer_to_dialog_load()
        ows_yeti.click_activate_HP_btn()
        self.sign_in_hp_account_from_sign_up_dialog(username, password)
        sleep(120)
        ows_yeti.wait_for_free_ink_plan_screen_load()
        sleep(2)
        ows_yeti.click_free_ink_plan_skip_free_ink_btn()
        ows_yeti.wait_for_are_you_sure_to_skip_dialog_load()
        ows_yeti.click_yes_skip_offer_btn()

    def go_through_e2e_flow_with_already_sign_in(self):
        ows_yeti = OWS_Yeti(self.driver)
        ows_yeti.wait_for_get_more_value_from_your_printing_experience_load(180)
        ows_yeti.click_get_more_value_from_your_printing_experience_continue_btn()
        ows_yeti.wait_for_your_printer_to_dialog_load()
        ows_yeti.click_activate_HP_btn()
        sleep(120)
        ows_yeti.wait_for_free_ink_plan_screen_load()
        sleep(2)
        ows_yeti.click_free_ink_plan_skip_free_ink_btn()
        ows_yeti.wait_for_are_you_sure_to_skip_dialog_load()
        ows_yeti.click_yes_skip_offer_btn()
