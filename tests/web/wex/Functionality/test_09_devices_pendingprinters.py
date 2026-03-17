import pytest
from MobileApps.libs.ma_misc import ma_misc
from time import sleep
pytest.app_info = "WEX"

class Test_04_Workforce_Devices_PendingPrinters(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, wex_setup, request):
        self = self.__class__
        self.driver, self.fc = wex_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.pending_printers = self.fc.fd["devices_pendingprinters"]
        self.account = ma_misc.get_wex_account_info(self.stack)
        self.hpid_username = self.account["customer_email"]
        self.hpid_password = self.account["customer_password"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_printers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       
        if self.home.verify_side_menu_expand_button_is_displayed() is False:
            self.home.click_side_menu_expand_button()
        if self.home.verify_sidemenu_devices_button_is_expanded() is False:
            self.home.click_sidemenu_devices_dropdown_button()
        self.home.click_sidemenu_devices_printers_dropdown_option()
        self.pending_printers.verify_devices_pending_printers_button()
        self.pending_printers.click_devices_pending_printers_button()
        return self.pending_printers.verify_devices_pending_printers_table_loaded()

    def test_01_verify_pending_printers_add_printers_popup_ui(self):
        #
        self.pending_printers.click_pending_printers_add_printers_button()
        self.pending_printers.verify_add_printers_popup_title()
        self.pending_printers.verify_add_printers_popup_description()
        self.pending_printers.verify_add_printers_popup_close_button()
        self.pending_printers.verify_add_printers_popup_cancel_button()
        self.pending_printers.verify_add_printers_popup_enter_manually_button()

        self.pending_printers.verify_add_printers_popup_enter_manually_button_name()
        self.pending_printers.verify_add_printers_popup_enter_manually_button_description()
        self.pending_printers.verify_add_printers_popup_enter_manually_button_icon()

        self.pending_printers.click_add_printers_popup_close_button()
        self.pending_printers.verify_devices_pending_printers_table_loaded()

    def test_02_verify_pending_printers_add_printers_enter_manually_popup_ui(self):
        #
        #Verify Add Printers - Enter Manually popup UI elements
        self.pending_printers.click_pending_printers_add_printers_button()
        self.pending_printers.click_add_printers_popup_enter_manually_button()
        self.pending_printers.verify_add_printers_enter_manually_popup_title()
        self.pending_printers.verify_add_printers_enter_manually_popup_description()
        self.pending_printers.verify_add_printers_enter_manually_popup_back_button()
        self.pending_printers.verify_add_printers_enter_manually_popup_close_button()
        self.pending_printers.verify_add_printers_enter_manually_popup_cancel_button()
        self.pending_printers.verify_add_printers_enter_manually_popup_submit_button()

        # Verify Add Printers - Enter Manually popup - Printer 1 field UI elements
        self.pending_printers.verify_add_printers_printer1_field()
        self.pending_printers.verify_add_printers_printer1_field_title()
        self.pending_printers.verify_add_printers_printer1_field_delete_button("disabled")
        self.pending_printers.verify_add_printers_printer1_field_serial_number_label()
        self.pending_printers.verify_add_printers_printer1_field_product_number_label()
        self.pending_printers.verify_add_printers_printer1_field_serial_number_textbox()
        self.pending_printers.verify_add_printers_printer1_field_product_number_textbox()
        self.pending_printers.verify_add_printers_printer1_field_serial_number_label_icon()
        self.pending_printers.verify_add_printers_printer1_field_product_number_label_icon()
        self.pending_printers.verify_add_printers_enter_manually_popup_add_another_printer_button()

        # Verify Add Printers - Enter Manually popup - Printer 1 field tooltip message
        self.pending_printers.verify_add_printers_printer1_field_serial_number_label_tooltip_message()
        self.pending_printers.verify_add_printers_printer1_field_product_number_label_tooltip_message()

        # Verify Add Printers - Enter Manually popup - Back button functionality
        self.pending_printers.click_add_printers_enter_manually_popup_back_button()
        self.pending_printers.verify_add_printers_popup_title()

        # Verify Add Printers - Enter Manually popup - Close button functionality
        self.pending_printers.click_add_printers_popup_enter_manually_button()
        self.pending_printers.click_add_printers_enter_manually_popup_close_button()
        self.pending_printers.verify_devices_pending_printers_table_loaded()

    def test_03_verify_add_printers_enter_manually_popup_cancel_button_functionality(self):
        #
        self.pending_printers.click_pending_printers_add_printers_button()
        self.pending_printers.click_add_printers_popup_enter_manually_button()
        self.pending_printers.enter_add_printers_printer1_field_serial_number("1234567890")
        self.pending_printers.enter_add_printers_printer1_field_product_number("123456")

        self.pending_printers.click_add_printers_enter_manually_popup_cancel_button()
        
        # Verify the Discard changes popup
        self.pending_printers.verify_discard_changes_popup()
        self.pending_printers.verify_discard_changes_popup_title()
        self.pending_printers.verify_discard_changes_popup_message()
        self.pending_printers.verify_discard_changes_popup_go_back_button()
        self.pending_printers.verify_discard_changes_popup_discard_button()
        self.pending_printers.click_discard_changes_popup_go_back_button()

        # Verify the changes are not discarded
        self.pending_printers.verify_add_printers_enter_manually_popup_title()
        assert self.pending_printers.get_add_printers_printer1_field_serial_number() == "1234567890", \
            "The serial number field is not retaining the entered value after clicking 'Go Back' button."
        assert self.pending_printers.get_add_printers_printer1_field_product_number() == "123456", \
            "The product number field is not retaining the entered value after clicking 'Go Back' button."

    def test_04_verify_add_printers_enter_manually_popup_tooltip_messages(self):
        #
        self.pending_printers.click_pending_printers_add_printers_button()
        self.pending_printers.click_add_printers_popup_enter_manually_button()
        self.pending_printers.click_add_printers_enter_manually_popup_submit_button()
        
        # Verify tooltip messages for serial number and product number fields
        self.pending_printers.verify_add_printers_printer1_field_serial_number_field_warning_message()
        self.pending_printers.verify_add_printers_printer1_field_product_number_field_warning_message()

        # Enter special characters in the serial number and product number fields
        self.pending_printers.enter_add_printers_printer1_field_serial_number("!@#$%^&*()")
        self.pending_printers.enter_add_printers_printer1_field_product_number("!@#$%^&*()")

        # Verify tooltip messages for invalid characters
        self.pending_printers.verify_add_printers_printer1_field_serial_number_field_warning_message()
        self.pending_printers.verify_add_printers_printer1_field_product_number_field_warning_message()

    def test_05_verify_add_printer_with_blacklisted_product_number(self):
        #
        self.pending_printers.click_pending_printers_add_printers_button()
        self.pending_printers.click_add_printers_popup_enter_manually_button()

        # Enter a valid serial number and a blacklisted product number
        self.pending_printers.enter_add_printers_printer1_field_serial_number("1234567890")
        self.pending_printers.enter_add_printers_printer1_field_product_number("4U561B")

        # Click the submit button
        self.pending_printers.click_add_printers_enter_manually_popup_submit_button()

        # Verify the error message for blacklisted product number
        self.pending_printers.verify_add_printers_printer1_field_product_number_blacklisted_warning_message()

        # Close the popup
        self.pending_printers.click_add_printers_enter_manually_popup_close_button()
        self.pending_printers.verify_devices_pending_printers_table_loaded()

    def test_06_verify_add_printer_functionality_already_claimed_to_same_account(self):
        #
        # Enter a serial number and product number of a printer already claimed to the same account
        existing_serial_number = (self.pending_printers.get_all_pending_printers_serial_number()[0]).upper()
        existing_product_number = (self.pending_printers.get_all_pending_printers_product_number()[0]).upper()

        self.pending_printers.click_pending_printers_add_printers_button()
        self.pending_printers.click_add_printers_popup_enter_manually_button()

        # Enter a valid serial number and a blacklisted product number
        self.pending_printers.enter_add_printers_printer1_field_serial_number(existing_serial_number)
        self.pending_printers.enter_add_printers_printer1_field_product_number(existing_product_number)

        # Click the submit button
        self.pending_printers.click_add_printers_enter_manually_popup_submit_button()

        # Verify the error message for a printer already claimed to the same account
        self.pending_printers.verify_add_printers_printer1_field_already_claimed_warning_message()

        # Close the popup
        self.pending_printers.click_add_printers_enter_manually_popup_close_button()
        self.pending_printers.verify_devices_pending_printers_table_loaded()
        
    def test_07_verify_add_printer_functionality_multiple_printers_fields_ui(self):
        #
        self.pending_printers.click_pending_printers_add_printers_button()
        self.pending_printers.click_add_printers_popup_enter_manually_button()
        self.pending_printers.click_add_printers_enter_manually_popup_add_another_printer_button()

        # Verify Add Printers - Enter Manually popup - Printer 2 field UI elements
        self.pending_printers.verify_add_printers_printer2_field()
        self.pending_printers.verify_add_printers_printer2_field_title()
        self.pending_printers.verify_add_printers_printer2_field_delete_button("enabled")
        self.pending_printers.verify_add_printers_printer2_field_serial_number_label()
        self.pending_printers.verify_add_printers_printer2_field_product_number_label()
        self.pending_printers.verify_add_printers_printer2_field_serial_number_textbox()
        self.pending_printers.verify_add_printers_printer2_field_product_number_textbox()
        self.pending_printers.verify_add_printers_enter_manually_popup_add_another_printer_button()

        self.pending_printers.click_add_printers_printer2_field_delete_button()
        self.pending_printers.verify_add_printers_printer2_field(displayed=False)