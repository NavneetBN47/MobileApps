import pytest
from time import sleep
from MobileApps.libs.flows.web.ows.ows_printer import OWSEmuPrinter
from MobileApps.libs.flows.web.ows.ows_fc_factory import ows_fc_factory

pytest.app_info = "OWS"


class Test_OWS_Signup_No_Activation_Flow:
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup_signup):
        self = self.__class__
        self.driver, self.ows_emulator, self.config_option, self.hpid, self.account = ows_test_setup_signup
        liveui_version, oobe_status = self.ows_emulator.launch_flow_by_printer(self.config_option.emu_printer, self.config_option.emu_platform)
        self.driver.add_window("OWSEmuPrinter")
        self.ows_printer = OWSEmuPrinter(self.config_option.emu_printer, self.driver, liveui_version, oobe_status, \
                                    window_name="OWSEmuPrinter")
        self.ows_printer.verify_page_load()    
        self.ows_fc = ows_fc_factory(self.driver, self.ows_printer)
        sleep(3)
        self.ows_fc.flow["connected_printing_services"].verify_connected_printing_services()
        self.ows_fc.flow["connected_printing_services"].click_connected_printing_services()


    def test_01_ows_printer_skip_activate_account(self):
        self.ows_fc.flow["ucde_safety_net"].click_skip_account_activation()
        self.ows_fc.flow["ucde_safety_net"].click_skip_account_activation_again()
        self.ows_fc.flow["load_paper"].verify_carousel_screen_owl_dots()


    def test_02_ows_printer_load_paper(self):
        self.ows_fc.flow["load_paper"].navigate_load_paper()
        self.ows_fc.flow["load_ink"].verify_carousel_screen_owl_dots()


    def test_03_ows_printer_load_ink(self):
        self.ows_fc.flow["load_ink"].navigate_load_ink()
        self.ows_fc.flow["load_ink"].verify_arrow_btn_disable()