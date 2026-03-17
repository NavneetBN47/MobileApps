import os
import time
import pytest
import traceback

import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.flows.web.ows.yeti_flow_container import YetiFlowContainer
from MobileApps.libs.flows.web.ows.ows_printer import OWSEmuPrinter
from MobileApps.libs.flows.web.ows.flow_container_base import BaseFlowContainer
from MobileApps.libs.flows.web.ows.ows_fc_factory import ows_fc_factory
from MobileApps.libs.flows.web.ows.sub_flow.connected_printing_services import ConnectedPrintingServices

pytest.app_info = "OWS"

class Test_OWS_Yeti(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, web_session_setup, request):
        self = self.__class__
        self.driver = web_session_setup
        self.driver.set_size("max")
        self.fc = YetiFlowContainer(self.driver)
        self.profile =  request.config.getoption("--printer-profile")
        self.biz_model = request.config.getoption("--printer-biz-model")
        self.stack = request.config.getoption("--stack")
        self.emu_platform = request.config.getoption("--emu-platform")
        self.emu_printer = request.config.getoption("--emu-printer")
        self.driver.set_global_cms_sys_arg(["--printer-profile", "--printer-biz-model", "--emu-platform"])
        self.connected_printing_services = ConnectedPrintingServices(self.driver)
        try:
            ows_status, self.access_token, self.id_token, self.sim_printer_info, self.username, self.password = self.fc.emulator_start_yeti(self.stack, self.profile, self.biz_model)
            self.driver.wait_for_new_window(timeout=15)
            self.driver.add_window("OWSEmuPrinter")
            self.ows_printer = OWSEmuPrinter(self.fc.get_printer_name_from_profile(self.profile), self.driver, 2, ows_status, window_name="OWSEmuPrinter")  
            self.ows_fc = BaseFlowContainer(self.driver, self.ows_printer)
            self.fd = ows_fc_factory(self.driver, self.ows_printer)
        except:
            session_attachment = pytest.session_result_folder + "session_attachment"
            os.makedirs(session_attachment)
            c_misc.save_screenshot_and_publish(self.driver, session_attachment + "/ows_yeti_setup_failure.png")
            c_misc.save_source_and_publish(self.driver,  session_attachment+ "/", file_name = "ows_yeti_setup_failure.txt")
            traceback.print_exc()
            raise

        """
        This is a Post-oobe Flow. Post-oobe flow is when the onboarded printer is taken through the onboarding flow to enroll in Ink or accept HP+ etc. 
        This particular Test case is to check that when the printer is onboarded again or going through the flow again does not see the Printer consents page again if the user has already accepted or already managed (Decline for some countrie)
        Reference Story HPC3-8155  OWS-67930
        """

    def test_01_yeti_flow(self):
        self.connected_printing_services.verify_connected_printing_services()
        self.connected_printing_services.click_connected_printing_services()
        self.fc.navigate_yeti(self.profile, self.biz_model)
        self.ows_printer.login(self.access_token, self.id_token)
        time.sleep(3)
        redirect_url_1 = self.ows_printer.get_console_data("PUT - ForceSignInHp")["params"]["continuationUrl"]+ "&completionCode=0"
        self.driver.switch_window()
        self.driver.navigate(redirect_url_1)
        time.sleep(10)
        self.fc.flow["value_proposition"].verify_value_proposition_page(timeout=40)
        self.fc.flow["value_proposition"].skip_value_proposition_page()
        self.fd.navigate_ows(self.ows_printer)
        self.driver.close_window("OWSEmuPrinter")
        self.fc.flow["ows_emulator"].open_emulator(self.stack)
        self.fc.flow["ows_emulator"].dismiss_banner()
        self.fc.flow["ows_emulator"].select_quick_option_by_printer(self.emu_printer)
        self.fc.flow["ows_emulator"].select_app_or_post_oobe_list_item()
        access_token_1 = self.fc.flow["ows_emulator"].get_web_auth_access_token()
        self.fc.flow["ows_emulator"].clear_web_auth_access_token()
        id_token_1 = self.fc.flow["ows_emulator"].get_id_token()
        self.fc.flow["ows_emulator"].clear_id_token()
        self.fc.flow["ows_emulator"].toggle_app_authenticate_user(on=False)
        self.fc.flow["ows_emulator"].select_device_menu_list_item()
        self.fc.flow["ows_emulator"].enter_claim_postcard(self.sim_printer_info["claim_postcard"])
        self.fc.flow["ows_emulator"].enter_uuid(self.sim_printer_info["uuid"])
        self.fc.flow["ows_emulator"].enter_cdm_printer_fingerprint(self.sim_printer_info["fingerprint"])
        self.fc.flow["ows_emulator"].enter_serial_number(self.sim_printer_info["serial_number"])
        self.fc.flow["ows_emulator"].enter_sku(self.sim_printer_info["model_number"])
        self.fc.flow["ows_emulator"].select_language_config_dropdown_and_choose("completed")
        self.fc.flow["ows_emulator"].select_country_config_dropdown_and_choose("completed")
        self.fc.flow["ows_emulator"].select_app_or_post_oobe_list_item()
        self.fc.flow["ows_emulator"].select_app_type_dropdown_and_choose(option=self.emu_platform)
        self.fc.flow["ows_emulator"].select_printer_claim_dropdown_and_choose(option="true")
        self.fc.flow["ows_emulator"].toggle_oobe()
        self.fc.flow["ows_emulator"].toggle_ink_subscription()
        self.fc.flow["ows_emulator"].select_actions_button()
        assert self.connected_printing_services.verify_connected_printing_services(raise_e=False) is False, "Printer Consents Screen is present"
        self.fc.flow["ucde_offer"].verify_ucde_hp_plus_benefits_page()