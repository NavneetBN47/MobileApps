import pytest
from time import sleep
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.one_simulator.printer_simulation import delete_simulator_printer


pytest.app_info = "HPX"
class Test_Suite_09_Scan_Intro_Sticky(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]


        # Initializing Printer2
        cls.p2 = cls.fc.initialize_printer(printer_config="HP Envy 6100e series")
        cls.printer_name2 = cls.p2.get_printer_information()["model name"]
        cls.serial_number2 = cls.p2.get_printer_information()["serial number"]
        cls.ip2 = cls.p2.get_printer_information()["ip address"]


        yield
        delete_simulator_printer(cls.ip2, cls.serial_number2)
        
    @pytest.mark.regression
    def test_01_verify_scan_settings_sticky_c43738433(self):
        """
        Change scan settings, perform a scan, select a different printer, go to Scan screen, verify scan settings are sticky
        Note: Use the Expected Result of https://hp-testrail.external.hp.com/index.php?/cases/view/43738422 as a reference

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738433
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.add_a_printer(self.p2)

        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        default_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
        logging.info("Printer #1: {0} Default Scan Settings: {1}".format(self.printer_name, default_scan_settings))

        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)

            sleep(1)
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PAGESIZE, self.fc.fd["scan"].A4)
            sleep(1)
            adf_printer = True
        else:
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].AREA, self.fc.fd["scan"].A4)
            sleep(1)
            adf_printer = False

        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PRESET, self.fc.fd["scan"].DOCUMENTS)
        sleep(1)
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].OUTPUT, self.fc.fd["scan"].GRAYSCALE)
        sleep(1)
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_150)
        
        change_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
        logging.info("Printer #1: {0} Updated Scan Settings: {1}".format(self.printer_name, change_scan_settings))
        
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=60)
        self.fc.fd["scan"].click_back_arrow()
        self.fc.fd["scan"].verify_exit_without_saving_dialog()
        self.fc.fd["scan"].click_yes_btn()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_back_arrow()       
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()

        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name2, timeout=30)
        sleep(3)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name2)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name2, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        another_printer_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
        logging.info("Printer #2: {0} Default Scan Settings: {1}".format(self.printer_name2, another_printer_scan_settings))
        
        if adf_printer:
            assert self.fc.fd["scan"].get_scan_presets_value() == self.fc.fd["scan"].PHOTO
            assert self.fc.fd["scan"].get_scan_area_value() == self.fc.fd["scan"].ENTIRE_SCAN_AREA
        else:
            assert self.fc.fd["scan"].get_scan_presets_value() == self.fc.fd["scan"].DOCUMENTS
            assert self.fc.fd["scan"].get_scan_area_value() == self.fc.fd["scan"].A4
        
        assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].GLASS
        assert self.fc.fd["scan"].get_scan_output_value() == self.fc.fd["scan"].GRAYSCALE
        assert self.fc.fd["scan"].get_scan_resolution_value() == self.fc.fd["scan"].DPI_150
