import time
import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import json
from MobileApps.libs.flows.web.ows.ows_printer import OWSEmuPrinter
from MobileApps.libs.flows.web.ows.sub_flow.connected_printing_services import ConnectedPrintingServices

pytest.app_info = "OWS"

class Test_OWS_Hero_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_emulator_init):
        self = self.__class__
        self.driver, self.emulator, self.config_option, self.hpid, self.account = ows_emulator_init # (driver, ows_emulator, config_option, hpid, account)
        self.emu_printer = self.config_option.emu_printer
        self.emu_platform = self.config_option.emu_platform
        self.stack = self.config_option.stack
        self.connected_printing_services = ConnectedPrintingServices(self.driver)

        # https://hp-jira.external.hp.com/browse/OWS-67625 https://hp-jira.external.hp.com/browse/OWS-68111 https://github.azc.ext.hp.com/ows/ows-oss-python3/pull/442 
    
    def test_01_validate_PDCN_screen_with_ODcontextsession(self):
        self.live_ui_version, self.oobe_status = self.emulator.launch_flow_by_printer(self.emu_printer, self.emu_platform)
        self.driver.add_window("OWSEmuPrinter")
        self.ows_printer = OWSEmuPrinter(self.emu_printer, self.driver, self.live_ui_version, self.oobe_status, window_name="OWSEmuPrinter")
        self.ows_printer.verify_page_load()
        time.sleep(3)
        self.connected_printing_services.verify_connected_printing_services()
        self.driver.close_window("OWSEmuPrinter")
        self.emulator.open_emulator(stack=self.stack)
        data = saf_misc.load_json(ma_misc.get_abs_path("/resources/test_data/ows/od_session_context.json"))
        session_context = json.dumps(data)
        self.emulator.select_quick_option_by_printer(self.emu_printer)
        self.emulator.select_app_or_post_oobe_list_item()
        self.emulator.enter_od_session_context(session_context)
        self.emulator.select_actions_button()
        time.sleep(3)
        assert self.connected_printing_services.verify_connected_printing_services(raise_e=False) is False, "Printer Consents Screen Present"