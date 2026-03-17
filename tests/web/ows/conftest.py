import pytest
import time
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.ma_misc.conftest_misc as c_misc

from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.ows.ows_emulator import OWSEmulator
from MobileApps.libs.flows.web.ows.ows_printer import OWSEmuPrinter
from MobileApps.libs.flows.web.ows.yeti_flow_container import YetiFlowContainer
from MobileApps.libs.flows.web.ows.ows_fc_factory import ows_fc_factory
from MobileApps.libs.flows.web.ows.sub_flow.connected_printing_services import ConnectedPrintingServices

def pytest_addoption(parser):
    web_argument_group = parser.getgroup('OWS Test Parameters')
    web_argument_group.addoption("--emu-version", action="store", default="v8", help="Choose which version of emulator to run. Eg. v8,v9")
    web_argument_group.addoption("--emu-printer", action="store", default="palermo", help="Choose which emulated printer to run against")
    web_argument_group.addoption("--emu-platform", action="store", default=None, help="Choose which platfrom to emulate")
    web_argument_group.addoption("--emu-error", action="store", default=None, help="Choose an error state (currently this is used for both calibration and ink step)")

    yeti_argument_group = parser.getgroup("OWS YETI Test Parameters")
    yeti_argument_group.addoption("--printer-biz-model", action="store", default="E2E", help="Choose which emulated printer to run against")
    yeti_argument_group.addoption("--model-sku", action="store", default=None, help="Choose which emulated printer to run against")

    poobe_argument_group = parser.getgroup('poobe Test Parameters')
    poobe_argument_group.addoption("--printer-operation", action="store", default="company", help="choose printer is personal or managed by organization")

@pytest.fixture(scope="class")
def ows_test_setup(web_session_setup, request):
    driver = web_session_setup
    driver.set_size("max")
    stack = driver.session_data['stack']
    printer_profile = request.config.option.printer_profile
    biz_model = request.config.option.printer_biz_model
    model_sku = request.config.option.model_sku
    emu_platform = request.config.option.emu_platform
    emu_printer = request.config.option.emu_printer
    emu_version = request.config.option.emu_version
    status_and_login_info = None
    try:
        yeti_fc = YetiFlowContainer(driver)
        if printer_profile:
            status_and_login_info = yeti_fc.emulator_start_yeti(stack, printer_profile, biz_model, model_sku=model_sku)
            driver.wait_for_new_window(timeout=15)
            driver.add_window("OWSEmuPrinter")
        else:
            ows_emulator = OWSEmulator(driver, version = emu_version)
            ows_emulator.open_emulator(stack)
            ows_emulator.verify_emulator_load()
            hpid = HPID(driver)
            account = ma_misc.get_hpid_account_info(stack, a_type="basic", claimable=False)
            ows_emulator.select_dev_menu_list_item()
            ows_emulator.click_hpid_login_button()
            hpid.login(account["email"], account["password"])
            hpid.handle_privacy_popup()
            ows_emulator.verify_emulator_load()
            ows_emulator.dismiss_banner()
            liveui_version, ows_status = ows_emulator.launch_flow_by_printer(emu_printer, emu_platform)
            driver.add_window("OWSEmuPrinter")
            ows_printer = OWSEmuPrinter(emu_printer, driver, liveui_version, ows_status, window_name="OWSEmuPrinter")
            ows_printer.verify_page_load()
            fc = ows_fc_factory(driver, ows_printer)
        time.sleep(3)
        connected_printing_services = ConnectedPrintingServices(driver)
        connected_printing_services.verify_connected_printing_services()
        connected_printing_services.click_connected_printing_services()
        
    except:
        attachment_root_path = c_misc.get_attachment_folder()
        for window, _ in driver.session_data["window_table"].items():
            driver.switch_window(window)
            c_misc.save_source_and_publish(driver, attachment_root_path, file_name="page_source_{}.txt".format(window))
            c_misc.save_screenshot_and_publish(driver, "{}/screenshot_{}_{}.png".format(attachment_root_path, request.node.name, window))
            c_misc.save_session_id(driver, attachment_root_path, f_name="Session_id_{}.txt".format(window))
        if request.config.getoption("--har"):
            c_misc.save_har_and_publish(driver, attachment_root_path, file_name="ows_bat_har")
        raise

    return (driver, emu_platform, ows_printer, fc, yeti_fc, status_and_login_info)