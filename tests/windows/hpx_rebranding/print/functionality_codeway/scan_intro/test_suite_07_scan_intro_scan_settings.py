import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_07_Scan_Intro_Scan_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.parametrize("quit_app", ["during_scan_flow", "after_scan_flow"])
    @pytest.mark.regression
    def test_01_check_scan_settings_restart_app_C43738422(self, quit_app):
        """
        Change scan settings, perform a scan, quit the app, "Verify Default and Sticky Values for Scan Settings"

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738422
        """
        if quit_app == "during_scan_flow":
            self.fc.launch_hpx_to_home_page()
            self.fc.add_a_printer(self.p)
            self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
            self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
            self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].click_reset_settings_btn()
        self.fc.fd["scan"].verify_reset_settings_btn(enable=False)

        default_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
     
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
            assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF
        sleep(1)
        if quit_app == "during_scan_flow":
            
            if self.fc.fd["scan"].verify_source_dropdown_enabled():
                self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PRESET, self.fc.fd["scan"].PHOTO)
                sleep(1)
                self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PAGESIZE, self.fc.fd["scan"].A4)
            else:
                self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PRESET, self.fc.fd["scan"].DOCUMENTS)
                sleep(1)
                self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].AREA, self.fc.fd["scan"].LETTER)
            sleep(1)
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_150)
            sleep(1)
        else:
            if self.fc.fd["scan"].verify_source_dropdown_enabled():
                self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PAGESIZE, self.fc.fd["scan"].LEGAL)
            else:
                self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].AREA, self.fc.fd["scan"].LETTER)
            sleep(1)
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_75)
            sleep(1)
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].OUTPUT, self.fc.fd["scan"].GRAYSCALE)
        sleep(1)
        
        updated_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
        restored_scan_settings = [default_scan_settings[0], default_scan_settings[1], default_scan_settings[2], 
                                    updated_scan_settings[3], updated_scan_settings[4]]

        self.fc.fd["scan"].click_scan_btn()
        if quit_app == "after_scan_flow":
            self.fc.fd["scan"].verify_scanning_screen()
            self.fc.fd["scan"].verify_scan_result_screen(timeout=120)

        self.fc.restart_hpx()

        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            assert self.fc.fd["scan"].get_all_scan_settings() == restored_scan_settings
        else:
            assert self.fc.fd["scan"].get_all_scan_settings() == updated_scan_settings

    @pytest.mark.regression
    def test_02_check_scan_settings_leave_and_return_C43738434(self):
        """
        Change scan settings, perform a scan, leave and return to Scan screen, "Verify Default and Sticky Values for Scan Settings"

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738434
        """
        self.fc.restart_hpx()

        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].click_reset_settings_btn()
        self.fc.fd["scan"].verify_reset_settings_btn(enable=False)

        default_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
            assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF
        sleep(1)
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_150)
        sleep(1)
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].OUTPUT, self.fc.fd["scan"].GRAYSCALE)
        sleep(1)
        
        updated_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
        restored_scan_settings = [default_scan_settings[0], default_scan_settings[1], default_scan_settings[2], 
                                    updated_scan_settings[3], updated_scan_settings[4]]

        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)
        self.fc.fd["scan"].click_back_arrow()
        self.fc.fd["scan"].verify_exit_without_saving_dialog()
        self.fc.fd["scan"].click_yes_btn()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].click_back_arrow()
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_top_back_btn()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            assert self.fc.fd["scan"].get_all_scan_settings() == restored_scan_settings
        else:
            assert self.fc.fd["scan"].get_all_scan_settings() == updated_scan_settings

    @pytest.mark.regression
    def test_03_check_scan_settings_add_more_scan_C43738435(self):
        """
        Change scan settings, perform a scan, add more scan jobs, "Verify Default and Sticky Values for Scan Settings"

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738435
        """
        self.fc.restart_hpx()

        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        sleep(2)
        self.fc.fd["scan"].click_reset_settings_btn()
        self.fc.fd["scan"].verify_reset_settings_btn(enable=False)

        default_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
            assert self.fc.fd["scan"].get_scan_source_value() == self.fc.fd["scan"].ADF
        sleep(1)
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_150)
        sleep(1)
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].OUTPUT, self.fc.fd["scan"].GRAYSCALE)
        sleep(1)
        
        updated_scan_settings = self.fc.fd["scan"].get_all_scan_settings()
        restored_scan_settings = [default_scan_settings[0], default_scan_settings[1], default_scan_settings[2], 
                                    updated_scan_settings[3], updated_scan_settings[4]]

        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=120)
        self.fc.fd["scan"].click_add_pages_btn()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            assert self.fc.fd["scan"].get_all_scan_settings() == restored_scan_settings
        else:
            assert self.fc.fd["scan"].get_all_scan_settings() == updated_scan_settings







