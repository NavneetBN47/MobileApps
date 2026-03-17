import pytest
import random
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "WEX"
from MobileApps.libs.flows.web.wex.wex_api_utility import *
from MobileApps.resources.const.web import const as w_const
from time import sleep

class Test_09_Pending_Printers_Cloud_Device_Onboarding(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.pending_printers = self.fc.fd["devices_pendingprinters"]
        self.printers = self.fc.fd["fleet_management_devices"]
        self.dashboard = self.fc.fd["fleet_management_dashboard"]
        self.account = ma_misc.get_wex_account_info(self.stack)
        self.hpid_username = self.account["customer_email"]
        self.hpid_password = self.account["customer_password"]
        self.tenantID = self.account["tenantID"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_button()
        self.home.click_sidemenu_analytics_button()
        self.home.click_analytics_fleet_management_button()
        self.dashboard.verify_printer_inventory_card()
        return self.dashboard.verify_printer_inventory_card_printers_count()

    @pytest.fixture(scope="class")
    def onboarded_simulator_serial_num(request):
        # Select a random profile
        profile = random.choice(["camden", "busch"])
        # Creating Simulator through API
        create_simulator_uri = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers"
        response = create_simulator("stage", profile, create_simulator_uri)
        serial_number = response.json()["entity_id"]
        product_number = response.json()["model_number"]
        return serial_number , product_number
        
    def test_01_verify_add_printers_e2e_functionality_in_pending_printers_through_one_simulator_devices(self, onboarded_simulator_serial_num):
        serial_number, product_number = onboarded_simulator_serial_num

        # Get the Printer Inventory Widget Printer Count from Dashboard
        printer_inventory_count = int(self.dashboard.get_printer_inventory_card_printers_count())

        # Registering the Printer and collecting the device Cloud- ID
        enabling_web_services_uri = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers/"+serial_number+"/register"
        response = registering_simulator(self.stack, enabling_web_services_uri)
        device_cloud_id = response.json()["cloud_id"]

        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.pending_printers.verify_devices_pending_printers_button()
        self.pending_printers.click_devices_pending_printers_button()

        self.pending_printers.verify_pending_printers_status_overview_card()
        connected_printer_count = self.pending_printers.get_pending_printers_connected_card_printers_count()

        # Adding the Printer in Pending Printers tab
        self.pending_printers.click_pending_printers_add_printers_button()
        self.pending_printers.click_add_printers_popup_enter_manually_button()
        self.pending_printers.enter_add_printers_printer1_field_serial_number(serial_number)
        self.pending_printers.enter_add_printers_printer1_field_product_number(product_number)
        self.pending_printers.click_add_printers_enter_manually_popup_submit_button()
        
        # Click refresh button and verify the device is added in Pending Printers table
        sleep(5)  # Wait for the device to be processed
        self.pending_printers.click_pending_printers_refresh_button()
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        self.pending_printers.search_pending_printers(serial_number)
        self.pending_printers.verify_pending_printers_connectivity_column_status(serial_number)

        assert self.pending_printers.get_pending_printers_connected_card_printers_count() == connected_printer_count + 1, \
            f"Expected printer count to increase by 1. Before: {connected_printer_count}, After: {self.pending_printers.get_pending_printers_connected_card_printers_count()}"
        
        # Verify the onboarded device is displayed in Printers - Devices tab
        self.printers.click_devices_printers_button()
        self.printers.verify_devices_printers_table_loaded()
        self.printers.search_printers(serial_number)
        self.printers.verify_devices_printers_table_loaded()
        self.printers.verify_search_results_with_serial_number(serial_number)
        self.printers.click_first_entry_link()
        assert device_cloud_id == self.printers.get_device_cloud_id()

        # Verify the updated Printer count in 'Printer Inventory' widget
        self.home.click_sidemenu_analytics_button()
        self.home.click_analytics_fleet_management_button()
        self.dashboard.verify_printer_inventory_card()
        self.dashboard.verify_printer_inventory_card_printers_count()
        current_printer_count = int(self.dashboard.get_printer_inventory_card_printers_count())

        assert printer_inventory_count + 1 == current_printer_count, \
            f"Expected printer count to increase by 1. Original: {printer_inventory_count}, Current: {current_printer_count}"

    def test_02_verify_delete_functionality_in_pending_printers(self, onboarded_simulator_serial_num):
        serial_number, _ = onboarded_simulator_serial_num

        printer_inventory_count = int(self.dashboard.get_printer_inventory_card_printers_count())

        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.pending_printers.verify_devices_pending_printers_button()
        self.pending_printers.click_devices_pending_printers_button()
        self.pending_printers.verify_devices_pending_printers_table_loaded()

        # Delete the Printer from Pending Printers tab
        self.pending_printers.search_pending_printers(serial_number)
        self.pending_printers.click_pending_printers_checkbox()
        self.pending_printers.click_pending_printers_delete_button()
        self.pending_printers.click_delete_confirmation_popup_delete_button()
        # self.pending_printers.check_toast_successful_message()

        # Verify the Printer is deleted from Pending Printers table

        self.pending_printers.click_pending_printers_refresh_button()
        self.pending_printers.search_pending_printers(serial_number)
        self.pending_printers.verify_pending_printers_removed()

        # Verify the deleted Printer count got updated in 'Printer Inventory' widget
        self.home.click_sidemenu_analytics_button()
        self.home.click_analytics_fleet_management_button()
        self.dashboard.verify_printer_inventory_card()
        self.dashboard.verify_printer_inventory_card_printers_count()
        current_printer_count = int(self.dashboard.get_printer_inventory_card_printers_count())
        
        assert printer_inventory_count - 1 == current_printer_count, \
            f"Expected printer count is decreased by 1. Original: {printer_inventory_count}, Current: {current_printer_count}"
