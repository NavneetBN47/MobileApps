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
from MobileApps.libs.flows.web.ows.firmware_update_page import FirmwareUpdateChoice
from MobileApps.libs.flows.web.ows import ows_utility

pytest.app_info = "OWS"

class Test_hp_one_horizon(object):
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
        self.connected_printing_services = ConnectedPrintingServices(self.driver)
        self.firmware_update_choice = FirmwareUpdateChoice(self.driver)
        if self.biz_model == "Flex":
            self.model_sku = "6GX01A"
        else:
            self.model_sku = "6GW99A"
        try:
            ows_status, self.access_token, self.id_token, self.sim_printer_info, self.username, self.password = self.fc.emulator_start_yeti(self.stack, self.profile, self.biz_model, self.model_sku)
            self.driver.wait_for_new_window(timeout=15)
            self.driver.add_window("OWSEmuPrinter")
            self.ows_printer = OWSEmuPrinter(self.fc.get_printer_name_from_profile(self.profile), self.driver, 2, ows_status, window_name="OWSEmuPrinter")  
            self.ows_fc = BaseFlowContainer(self.driver, self.ows_printer)
        except:
            session_attachment = pytest.session_result_folder + "session_attachment"
            os.makedirs(session_attachment)
            c_misc.save_screenshot_and_publish(self.driver, session_attachment + "/ows_yeti_setup_failure.png")
            c_misc.save_source_and_publish(self.driver,  session_attachment+ "/", file_name = "ows_yeti_setup_failure.txt")
            traceback.print_exc()
            raise

        """
        This is HP one Horizon POC
        Decline Ink
        if HP+ then No FW update Screen E2E only.
        if Flex then check FW update choice Screen.
        """

    def test_01_horizon_accept_hp_plus_no_FW_update_screen_flow(self):
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
        self.ows_fc.navigate_ows(self.ows_printer)
        if self.biz_model == "Flex":
            self.firmware_update_choice.verify_firmware_update_choice_page()
            self.firmware_update_choice.click_auto_update_button()
            self.firmware_update_choice.click_apply_button()
        else:
            assert self.firmware_update_choice.verify_firmware_update_choice_page(raise_e=False) is False
        ows_utility.remove_printer(self.sim_printer_info['serial_number'])
        time.sleep(140) # Adding time delay to avoid 500 server error. wpp api will block calls if too many api calls done frequently.