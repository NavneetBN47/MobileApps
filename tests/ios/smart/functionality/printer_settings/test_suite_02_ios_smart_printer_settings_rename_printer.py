import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings

pytest.app_info = "SMART"

class Test_Suite_02_Ios_Smart_Printer_Settings_Rename_Printer(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup, request, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.printer_settings = cls.fc.fd["printer_settings"]
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_informations = cls.p.get_printer_information()
        cls.printer_actual_bonjour_name = cls.printer_informations["bonjour name"]
        cls.printer_actual_direct_name = cls.p.get_wifi_direct_information()["name"]
        cls.printer_sn = cls.printer_informations['serial number']
        cls.stack = request.config.getoption("--stack")
        cls.pin_code = cls.p.get_pin_udw()
        # Go Home
        cls.fc.go_home(stack=cls.stack)


    def test_01_verify_rename_my_printer_functionality(self):
        """
        Navigate to rename my printer screen, edit printer name and verify printer name updated on
        home screen - C16798177
        """
        rename_printer = "Test Printer"
        self.rename_printer_name(PrinterSettings.NETWORK_INFO_BONJOUR_NAME, rename_printer)
        self.printer_settings.select_navigate_back()
        self.printer_settings.select_navigate_back()
        self.fc.fd["home"].verify_home_tile(raise_e=True)
        edited_printer_name = self.fc.fd["home"].get_printer_name_from_device_carousel()
        # clean up- Reset printer name back to Bonjour name
        self.rename_printer_name(PrinterSettings.NETWORK_INFO_BONJOUR_NAME, self.printer_actual_bonjour_name)
        assert edited_printer_name == rename_printer

    def test_02_verify_bonjour_name_edit_screen(self):
        """
        Navigate to Bonjour name edit screen, verify ui elements and edit name - C16825221
        """
        new_bonjour_name = "Test Printer"
        self.rename_printer_name(PrinterSettings.NETWORK_INFO_BONJOUR_NAME, new_bonjour_name)
        edited_bonjour_name = self.printer_settings.verify_title_and_get_value("Bonjour Name")
        # clean up
        self.rename_printer_name(PrinterSettings.NETWORK_INFO_BONJOUR_NAME, self.printer_actual_bonjour_name)
        self.printer_settings.select_navigate_back()
        assert edited_bonjour_name == new_bonjour_name

    def test_03_verify_direct_connection_name_edit_screen(self):
        """
        Navigate to Direct Connection Name Edit screen, verify ui elements and edit name - C16825270
        """
        new_direct_name = "Direct-Test-Printer"
        self.rename_printer_name(PrinterSettings.NETWORK_INFO_DIRECT_CONNECTION_NAME, new_direct_name)
        edited_direct_name = self.printer_settings.verify_title_and_get_value("Direct Name")
        default_name_text = self.get_printer_name_first_part_wifi_direct_update(edited_direct_name, self.printer_actual_direct_name)
        self.printer_settings.select_navigate_back()
        self.rename_printer_name(PrinterSettings.NETWORK_INFO_DIRECT_CONNECTION_NAME, self.printer_actual_direct_name.replace(default_name_text, ""))
        self.printer_settings.select_navigate_back()
        assert new_direct_name in edited_direct_name

    def test_04_verify_bonjour_and_direct_name_edit_screen_ui_elements(self):
        """
        Verify Bonjour and Direct Name edit screen UI elements
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.printer_settings.select_ui_option(PrinterSettings.PS_NETWORK_INFORMATION)
        self.printer_settings.select_ui_option(PrinterSettings.NETWORK_INFO_BONJOUR_NAME)
        self.printer_settings.verify_ui_elements(PrinterSettings.PS_RENAME_PRINTER_UI_ELEMENTS)
        assert self.driver.get_attribute(PrinterSettings.SAVE_BUTTON, attribute="enabled").lower() == "false"
        self.printer_settings.select_cancel()
        self.printer_settings.go_to_wi_fi_direct()
        self.printer_settings.select_ui_option(PrinterSettings.NETWORK_INFO_DIRECT_CONNECTION_NAME)
        self.printer_settings.verify_rename_printer_screen()
        assert self.driver.get_attribute(PrinterSettings.SAVE_BUTTON, attribute="enabled").lower() == "false"
        # clean up
        self.printer_settings.select_cancel()
        self.printer_settings.select_navigate_back()

    def rename_printer_name(self, element, printer_name):
        if self.printer_sn.lower().startswith('th'):
            pytest.skip("The printer is not suitable for this test case. Test case skipped!")
        if not self.printer_settings.verify_printer_settings_screen():
            self.fc.go_to_printer_settings_screen(self.p)
        self.printer_settings.select_ui_option(PrinterSettings.PS_NETWORK_INFORMATION)
        if element=="direct_connection_name":
            self.printer_settings.go_to_wi_fi_direct()
            if self.driver.wait_for_object(PrinterSettings.WIFI_DIRECT_FIND_PRINTER_PIN, raise_e=False, timeout=5):
                self.printer_settings.select_and_submit_pin_code(self.pin_code)
        self.printer_settings.select_ui_option(element)
        self.printer_settings.verify_rename_printer_screen()
        self.printer_settings.edit_printer_name_and_save(printer_name)
        if self.driver.wait_for_object(PrinterSettings.WIFI_DIRECT_FIND_PRINTER_PIN, raise_e=False, timeout=5):
            self.printer_settings.select_and_submit_pin_code(self.pin_code)
            
    def get_printer_name_first_part_wifi_direct_update(self, modified_name, original_name):
        """
        Method used to get the first part of the printer name which is always present
        when the printer name is updated from wi-fi direct 
        """
        min_length = min(len(modified_name), len(original_name))

        # Iterate over the characters in both strings until a mismatch is found
        common_slice = ""
        for i in range(min_length):
            if modified_name[i] == original_name[i]:
                common_slice += modified_name[i]
            else:
                break

        return common_slice