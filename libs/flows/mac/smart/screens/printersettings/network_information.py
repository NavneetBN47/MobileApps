# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on the network information page screen.

@author: Ivan
@create_date: Nov 06, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_setting_scroll import PrinterSettingScroll
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class NetworkInformation(PrinterSettingScroll, SmartScreens):
    folder_name = "printersettings"
    flow_name = "network_information"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(NetworkInformation, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait network information screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("wireless_title", timeout=timeout, raise_e=raise_e)

    def wait_for_offline_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Offline dialog load correctly
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[wait_for_offline_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("offline_dialog_title", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_non_ledm(self, timeout=30, raise_e=True):
        '''
        This is a method to wait network information could not be retrieved screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[wait_for_screen_load_non_ledm]-Wait for screen loading... ")

        return self.driver.wait_for_object("network_information_could_not_be_retrieved", timeout=timeout, raise_e=raise_e)

    def get_the_string_of_wireless_title(self):
        '''
        This is a method to get the string of Wireless Title
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_wireless_title]-Get the string of Wireless Title... ")

        return self.driver.get_value("wireless_title")

    def get_the_string_of_wireless_item(self):
        '''
        This is a method to get the string of Wireless Item
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_wireless_item]-Get the string of Wireless Item... ")

        return self.driver.get_value("wireless_item")

    def get_the_string_of_wireless_item_value(self):
        '''
        This is a method to get the string of Wireless Item value
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_wireless_item_value]-Get the string of Wireless Item value... ")

        return self.driver.get_value("wireless_item_value")

    def get_the_string_of_wireless_status_item(self):
        '''
        This is a method to get the string of Wireless Status Item
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_wirelss_status_item]-Get the string of Wireless Status Item... ")

        return self.driver.get_value("wireless_status_item")

    def get_the_string_of_wireless_status_item_value(self):
        '''
        This is a method to get the value of Wireless Status Item value
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_wireless_status_item_value]-Get the value of Wireless Status Item value... ")

        return self.driver.get_value("wireless_status_item_value")

    def get_the_string_of_bonjour_name_item(self):
        '''
        This is a method to get the string of Bonjour Name Item
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_bonjour_name_item]-Get the string of Bonjour Name Item... ")

        return self.driver.get_value("bonjour_name_item")

    def get_the_string_of_bonjour_name_item_value(self):
        '''
        This is a method to get the value of Bonjour Name Item value
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_bonjour_name_item_value]-Get the value of Bonjour Name Item value... ")

        return self.driver.get_value("bonjour_name_item_value")

    def get_the_string_of_ip_address_item(self):
        '''
        This is a method to get the string of IP Address Item
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_ip_address_item]-Get the string of IP Address Item... ")

        return self.driver.get_value("ip_address_item")

    def get_the_string_of_ip_address_item_value(self):
        '''
        This is a method to get the value of IP Address Item value
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_ip_address_item_value]-Get the value of IP Address Item value... ")

        return self.driver.get_value("ip_address_item_value")

    def get_the_string_of_network_name_ssid_item(self):
        '''
        This is a method to get the string of Network Name (SSID) Item
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_network_name_ssid_item]-Get the string of Network Name (SSID) Item... ")

        return self.driver.get_value("network_name_ssid_item")

    def get_the_string_of_network_name_ssid_item_value(self):
        '''
        This is a method to get the value of Network Name (SSID) Item value
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_network_name_ssid_item_value]-Get the value of Network Name (SSID) value... ")

        return self.driver.get_value("network_name_ssid_item_value")

    def get_the_string_of_mac_address_item(self):
        '''
        This is a method to get the string of Mac Address
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_mac_address_item]-Get the string of Mac Address... ")

        return self.driver.get_value("mac_address_item")

    def get_the_string_of_mac_address_item_value(self):
        '''
        This is a method to get the value of Mac Address value
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_mac_address_item_value]-Get the value of Mac Address value... ")

        return self.driver.get_value("mac_address_item_value")

    def get_the_string_of_host_name_item(self):
        '''
        This is a method to get the string of Host Name
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_host_name_item]-Get the string of Host Name... ")

        return self.driver.get_value("host_name_item")

    def get_the_string_of_host_name_item_value(self):
        '''
        This is a method to get the value of Host Name value
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_host_name_item_value]-Get the value of Host Name value... ")

        return self.driver.get_value("host_name_item_value")

    def get_the_string_of_ethernet_title(self):
        '''
        This is a method to get the string of Ethernet title
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_ethernet_title]-Get the string of Ethernet Item... ")

        return self.driver.get_value("ethernet_title")

    def get_the_string_of_ethernet_status_item(self):
        '''
        This is a method to get the string of Ethernet Status Item
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_ethernet_status_item]-Get the string of Ethernet Status Item... ")

        return self.driver.get_value("ethernet_status_item")

    def get_the_string_of_ethernet_status_item_value(self):
        '''
        This is a method to get the value of Ethernet Status Item value
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_ethernet_status_item_value]-Get the value of Ethernet Status Item value... ")

        return self.driver.get_value("ethernet_status_item_value")

    def get_the_string_of_bluetooth_low_energy_title(self):
        '''
        This is a method to get the string of Bluetooth Low Energy title
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_bluetooth_low_energy_title]-Get the string of Bluetooth Low Energy title... ")

        return self.driver.get_value("bluetooth_low_energy_title")

    def get_the_string_of_bluetooth_low_energy_status_item(self):
        '''
        This is a method to get the string of Bluetooth Low Energy status item
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_bluetooth_low_energy_status_item]-Get the string of Bluetooth Low Energy status item... ")

        return self.driver.get_value("bluetooth_low_energy_status_item")

    def get_the_string_of_bluetooth_low_energy_status_item_value(self):
        '''
        This is a method to get the string of Bluetooth Low Energy status item value
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_bluetooth_low_energy_status_item_value]-Get the string of Bluetooth Low Energy status item value... ")

        return self.driver.get_value("bluetooth_low_energy_status_item_value")

    def get_the_string_of_could_not_be_retrived(self):
        '''
        This is a method to get the string of network information could not be retrieved text
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[get_the_string_of_could_not_be_retrived]-Get the value of network information could not be retrieved text... ")

        return self.driver.get_value("network_information_could_not_be_retrieved")

    def click_ok_btn_on_offline_dialog(self):
        '''
        This is a method to click OK button on Offline dialog.
        :parameter:
        :return:
        '''
        logging.debug("[NetworkInformation]:[click_ok_btn_on_offline_dialog]-Click OK button... ")

        self.driver.click("offline_dialog_ok_btn", is_native_event=True)

# -------------------------------Verification Methods--------------------------
    def verify_network_information_page_items(self, Printer_Connection_Type, LEDM=True, Ethernet_Supported=True, Bluetooth_Supported=True):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter: Printer_Connection_Type = Wireless or Wired or USB
        :return:
        '''
        logging.debug("Verify network information items string ")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='network_information_screen')
        if LEDM:

            if Printer_Connection_Type == "Wireless":
                assert self.get_the_string_of_wireless_title() == test_strings['wireless_title']
                assert self.get_the_string_of_wireless_item() == test_strings['wireless_item']
                assert self.get_the_string_of_wireless_status_item() == test_strings['status_item']
                assert self.get_the_string_of_bonjour_name_item() == test_strings['bonjour_name_item']
                assert self.get_the_string_of_ip_address_item() == test_strings['ip_address_item']
                assert self.get_the_string_of_network_name_ssid_item() == test_strings['network_name_ssid_item']
                assert self.get_the_string_of_mac_address_item() == test_strings['mac_address_item']
                assert self.get_the_string_of_host_name_item() == test_strings['host_name_item']
                assert self.get_the_string_of_ethernet_title() == test_strings['ethernet_title']
                assert self.get_the_string_of_ethernet_status_item() == test_strings['status_item']
                # Verify Wireless Status is connected.
                assert self.get_the_string_of_wireless_status_item_value() == test_strings['connected']
                # If printer does not support ethernet network,  then ethernet status will show not supported on network information page.
                if Ethernet_Supported is True:
                    assert self.get_the_string_of_ethernet_status_item_value() == test_strings['not_connected']
                else:
                    assert self.get_the_string_of_ethernet_status_item_value() == test_strings['not_supported']
                # If printer support Bluetooth, the Bluetooth Low Energy section will show on network information page.
                if Bluetooth_Supported is True:
                    assert self.get_the_string_of_bluetooth_low_energy_title() == test_strings['bluetooth_low_energy_title']
                    assert self.get_the_string_of_bluetooth_low_energy_status_item() == test_strings['status_item']

            if Printer_Connection_Type == "Wired":
                if self.get_the_string_of_wireless_item_value() == test_strings['on_value']:
                    assert self.get_the_string_of_wireless_title() == test_strings['wireless_title']
                    assert self.get_the_string_of_wireless_item() == test_strings['wireless_item']
                    assert self.get_the_string_of_wireless_status_item() == test_strings['status_item']
                    assert self.get_the_string_of_bonjour_name_item() == test_strings['ethernet_title']
                    assert self.get_the_string_of_bonjour_name_item_value() == test_strings['status_item']
                    assert self.get_the_string_of_ip_address_item_value() == test_strings['bonjour_name_item']
                    assert self.get_the_string_of_network_name_ssid_item_value() == test_strings['ip_address_item']
                    assert self.get_the_string_of_mac_address_item_value() == test_strings['mac_address_item']
                    assert self.get_the_string_of_host_name_item_value() == test_strings['host_name_item']
                    # Verify Wired Status is connected.
                    assert self.get_the_string_of_ip_address_item() == test_strings['connected']
                    if Bluetooth_Supported is True:
                        assert self.get_the_string_of_ethernet_status_item() == test_strings['bluetooth_low_energy_title']
                        assert self.get_the_string_of_ethernet_status_item_value() == test_strings['status_item']
                else:
                    assert self.get_the_string_of_wireless_title() == test_strings['wireless_title']
                    assert self.get_the_string_of_wireless_item() == test_strings['wireless_item']
                    assert self.get_the_string_of_wireless_status_item() == test_strings['ethernet_title']
                    assert self.get_the_string_of_wireless_status_item_value() == test_strings['status_item']
                    assert self.get_the_string_of_bonjour_name_item_value() == test_strings['bonjour_name_item']
                    assert self.get_the_string_of_ip_address_item_value() == test_strings['ip_address_item']
                    assert self.get_the_string_of_network_name_ssid_item_value() == test_strings['mac_address_item']
                    assert self.get_the_string_of_mac_address_item_value() == test_strings['host_name_item']
                    # Verify Wired Status is connected.
                    assert self.get_the_string_of_bonjour_name_item() == test_strings['connected']
                    if Bluetooth_Supported is True:
                        assert self.get_the_string_of_host_name_item_value() == test_strings['bluetooth_low_energy_title']
                        assert self.get_the_string_of_ethernet_title() == test_strings['status_item']

            if Printer_Connection_Type == "USB":
                assert self.get_the_string_of_wireless_title() == test_strings['wireless_title']
                assert self.get_the_string_of_wireless_item() == test_strings['wireless_item']
                assert self.get_the_string_of_wireless_status_item() == test_strings['status_item']
                assert self.get_the_string_of_bonjour_name_item() == test_strings['ethernet_title']
                assert self.get_the_string_of_bonjour_name_item_value() == test_strings['status_item']
                if Bluetooth_Supported is True:
                    assert self.get_the_string_of_ip_address_item_value() == test_strings['bluetooth_low_energy_title']
                    assert self.get_the_string_of_network_name_ssid_item() == test_strings['status_item']
                    assert self.get_the_string_of_mac_address_item() == test_strings['usb_title']
                    assert self.get_the_string_of_mac_address_item_value() == test_strings['status_item']
                    # Verify USB Status is connected.
                    assert self.get_the_string_of_host_name_item() == test_strings['connected']
                else:
                    assert self.get_the_string_of_ip_address_item_value() == test_strings['usb_title']
                    assert self.get_the_string_of_network_name_ssid_item() == test_strings['status_item']
                    # Verify USB Status is connected.
                    assert self.get_the_string_of_network_name_ssid_item_value() == test_strings['connected']

        else:

            assert self.get_the_string_of_could_not_be_retrived() == test_strings['network_information_could_not_be_retrieved']
