import pytest

pytest.app_info = "OWS"

class Test_04_calibration_error(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup):
        self = self.__class__
        self.driver, self.emu_platform, self.ows_printer, self.fc, self.yeti_fc, self.status_and_login_info = ows_test_setup
        self.request = self.driver.session_data["request"]

    def test_01_calibration_error(self):
        if self.request.config.getoption("--browser-type") in ["chrome", "edge"] and self.emu_platform in ["IOS", "Android"]:
            pytest.skip()
        self.fc.navigate_ows(self.ows_printer, stop_at="insertInk")

        #test_02_send_error_state_ink
        self.ows_printer.toggle_ledm_status("insert_ink_dropbox", option_value="string:failed")
        self.fc.flow["load_ink"].verify_spinner_modal()
        self.ows_printer.send_product_status("cartridgeFailure")
        #test_03_verify_error_modal
        self.fc.flow["load_ink"].verify_error_modal()
        #test_04_recover_error_state
        self.ows_printer.send_product_status("noAlerts")
        self.ows_printer.insert_ink()
        self.fc.flow["load_ink"].ink_click_continue()
        #test_05_navigate_to_calibrate
        self.fc.navigate_ows(self.ows_printer, stop_at="calibration")
        #test_06_send_error_state_calibration
        self.ows_printer.toggle_ledm_status("calibration_dropbox", option_value="string:failed")
        self.ows_printer.click_get_oobe_status_btn()
        self.fc.flow["calibration"].verify_spinner_modal()
        self.ows_printer.send_product_status(self.request.config.getoption("--emu-error"))
        #test_07_verify_error_page
        self.fc.flow["calibration"].verify_failure_screen()
        #test_08_recover_error_state
        self.ows_printer.send_product_status("noAlerts")
        self.ows_printer.calibrate_printer()
        #test_08_complete_ows
        self.fc.navigate_ows(self.ows_printer)