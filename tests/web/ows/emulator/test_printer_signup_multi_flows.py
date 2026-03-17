import pytest
from time import sleep
from MobileApps.libs.flows.web.ows.ows_printer import OWSEmuPrinter
from MobileApps.libs.flows.web.ows.ows_fc_factory import ows_fc_factory
from MobileApps.tests.web.ows.conftest import ows_test_setup_no_signin
from MobileApps.tests.web.ows.conftest import ows_test_setup_signup
pytest.app_info = "OWS"


class Test_OWS_Signup_Multi_Flows:
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup_signup):
        self = self.__class__
        self.driver, self.ows_emulator, self.config_option, self.hpid, self.account = ows_test_setup_signup
        self.url = self.driver.get_current_url()
        liveui_version, oobe_status = self.ows_emulator.launch_flow_by_printer(self.config_option.emu_printer, self.config_option.emu_platform)
        self.driver.add_window("OWSEmuPrinter")
        self.ows_printer = OWSEmuPrinter(self.config_option.emu_printer, self.driver, liveui_version, oobe_status, \
                                    window_name="OWSEmuPrinter")
        self.ows_printer.verify_page_load()    
        self.ows_fc = ows_fc_factory(self.driver, self.ows_printer)
        self.ows_fc.flow["connected_printing_services"].verify_connected_printing_services()
        self.ows_fc.flow["connected_printing_services"].click_connected_printing_services()

    def test_01_ows_printer_choose_sign_in_option(self, clean_up):  
        self.ows_fc.flow["ucde_safety_net"].click_sign_in()
        self.ows_fc.flow["ucde_safety_net"].verify_loading_hp_account()
        clean_up(self.url)

    def test_02_ows_printer_choose_sign_up_option(self, ows_test_setup_no_signin, clean_up):
        self.driver, self.ows_emulator, self.config_option, self.ows_fc, self.ows_printer = ows_test_setup_no_signin
        self.ows_fc.flow["ucde_safety_net"].click_create_account()
        self.ows_fc.flow["ucde_safety_net"].verify_loading_hp_account()
        clean_up(self.url)
        
    def test_03_ows_printer_choose_read_more_option(self, ows_test_setup_no_signin):
        self.driver, self.ows_emulator, self.config_option, self.ows_fc, self.ows_printer = ows_test_setup_no_signin
        self.ows_fc.flow["ucde_safety_net"].click_read_more()
        self.ows_fc.flow["ucde_safety_net"].verify_read_more_screen()
        self.ows_fc.flow["ucde_safety_net"].click_read_more_ok_btn()
        self.ows_fc.flow["ucde_safety_net"].verify_back_to_main_page()