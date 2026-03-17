import pytest
from MobileApps.libs.flows.web.ows.ows_emulator import OWSEmulator
pytest.app_info = "OWS"

class Test_07_SUH_error(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup):
        self = self.__class__
        self.driver, self.emu_platform, self.ows_printer, self.fc, self.yeti_fc, self.status_and_login_info = ows_test_setup
        self.request = self.driver.session_data["request"]
        self.ows_emulator = OWSEmulator(self.driver)
        self.emu_printer = self.request.config.getoption("--emu-printer")

    # https://hp-jira.external.hp.com/browse/OWS-66060. Please Refer to story for additional details.
    # suh will occur when -6 code is sent from emulator either using oobe get status, getinstantinkstatus or get productstatus
    # suh error modal depends on printer and liveUI step (Printers with sensor for that particular LiveUI step)
    
    def test_01_verify_suh_error(self, subtests):
        pytest.subtests = subtests
        if self.request.config.getoption("--browser-type") in ["chrome", "edge"] and self.emu_platform in ["IOS", "Android"] and  self.emu_printer in ["palermo", "verona", "taiji", "taccola"]:
            pytest.skip()
        if self.emu_printer in ["palermo", "verona"]:
            self.fc.navigate_ows(self.ows_printer, stop_at="languageConfig")
            self.fc.flow["country_language"].verify_web_page()
            self.fc.invoke_suh_via_oobe_status_code(self.ows_printer)
            self.fc.flow["country_language"].validate_country_language_screen()
            self.fc.navigate_ows(self.ows_printer, stop_at="insertInk")
            
            if self.emu_printer == "palermo":
                self.fc.invoke_suh_via_ink_completion_code(self.ows_printer, self.fc)
                self.fc.navigate_ows(self.ows_printer, stop_at="calibration")
                self.fc.invoke_suh_via_oobe_status_code(self.ows_printer, recover=False)
            
            if self.emu_printer == "verona":
                self.fc.invoke_suh_via_oobe_status_code(self.ows_printer)
                self.fc.navigate_ows(self.ows_printer, stop_at="semiCalibrationPrint")
                self.fc.invoke_suh_via_oobe_status_code(self.ows_printer)
                self.fc.navigate_ows(self.ows_printer, stop_at="semiCalibrationScan")
                self.fc.invoke_suh_via_oobe_status_code(self.ows_printer, recover=False)
    
        if self.emu_printer in ["taiji", "taccola"]:
            self.fc.navigate_ows(self.ows_printer, stop_at="insertInk")
            self.fc.invoke_suh_via_ink_completion_code(self.ows_printer, self.fc)
            self.fc.navigate_ows(self.ows_printer)
 
        if self.emu_printer in ["infinity", "vasari", "novelli", "horizon"]:
            self.fc.navigate_ows(self.ows_printer, stop_at ="loadMainTray")
            self.fc.invoke_suh_via_oobe_status_code(self.ows_printer)
            if self.emu_printer in ["infinity", "vasari", "novelli"]:
                self.fc.navigate_ows(self.ows_printer, stop_at="insertInk")
                self.fc.invoke_suh_via_product_completion_code(self.ows_printer, recover=False)