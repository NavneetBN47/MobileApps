import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_02_Scan_Intro_Reset_Settings_Btn(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_check_reset_settings_btn_disabled_C43738417(self):
        """
        Navigate to Scanner Screen (settings not changed before), verify 'Reset Setting' is disabled

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738417
        """
        #Alpha code, cannot add printer so using a dummy printer by using a recent device list xml file
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name, timeout=60)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)

        self.fc.fd["scan"].verify_reset_settings_btn(enable=False)

    @pytest.mark.regression
    def test_02_verify_reset_settings_btn_enabled_C43738418(self):
        """
        Change scan settings, verify "Reset Settings" become active

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738418
        """
        if self.fc.fd["scan"].verify_source_dropdown_enabled():
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].SOURCE, self.fc.fd["scan"].ADF)
            sleep(1)
            self.fc.fd["scan"].verify_reset_settings_btn()
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PRESET, self.fc.fd["scan"].PHOTO)
            sleep(1)
            self.fc.fd["scan"].verify_reset_settings_btn()
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PAGESIZE, self.fc.fd["scan"].A4)
            sleep(1)
            self.fc.fd["scan"].verify_reset_settings_btn()
        else:
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PRESET, self.fc.fd["scan"].DOCUMENTS)
            sleep(1)
            self.fc.fd["scan"].verify_reset_settings_btn()
            self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].AREA, self.fc.fd["scan"].LETTER)
            sleep(1)
            self.fc.fd["scan"].verify_reset_settings_btn()
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].OUTPUT, self.fc.fd["scan"].GRAYSCALE)
        sleep(1)
        self.fc.fd["scan"].verify_reset_settings_btn()
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].DPI, self.fc.fd["scan"].DPI_150)
        sleep(1)
        self.fc.fd["scan"].verify_reset_settings_btn()

        self.fc.fd["scan"].click_reset_settings_btn()
        self.fc.fd["scan"].verify_reset_settings_btn(enable=False)
