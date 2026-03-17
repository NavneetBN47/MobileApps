import pytest

pytest.app_info = "OWS"

class Test_03_ink_error(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup):
        self = self.__class__
        self.driver, self.emu_platform, self.ows_printer, self.fc, self.yeti_fc, self.status_and_login_info = ows_test_setup
        self.request = self.driver.session_data["request"]
         
    def test_01_ink_error(self, request):
        if self.request.config.getoption("--browser-type") in ["chrome", "edge"] and self.emu_platform in ["IOS", "Android"]:
            pytest.skip()
        self.fc.navigate_ows(self.ows_printer, stop_at="insertInk")
        #test_02_send_error_state:
        self.ows_printer.toggle_ledm_status("insert_ink_dropbox", option_value="string:failed")
        self.fc.flow["load_ink"].verify_spinner_modal()
        self.ows_printer.send_product_status(request.config.getoption("--emu-error"))
        #test_03_verify_error_modal
        self.fc.flow["load_ink"].verify_error_modal()
        #test_04_verify_error_modal_hide
        self.fc.flow["load_ink"].click_error_modal_learn_more_btn()
        self.fc.flow["load_ink"].verify_error_modal(invisible=True)
        self.fc.flow["load_ink"].verify_collapsed_error_body(invisible=False)
        #test_05_verify_error_modal_show
        self.fc.flow["load_ink"].click_collapsed_error_body()
        self.fc.flow["load_ink"].verify_error_modal(invisible=False)
        self.fc.flow["load_ink"].verify_collapsed_error_body(invisible=True)
        #test_06_recover_error_state
        self.ows_printer.send_product_status("noAlerts")
        self.ows_printer.insert_ink()
        self.fc.flow["load_ink"].ink_click_continue()
        #test_07_complete_flow
        self.fc.navigate_ows(self.ows_printer)