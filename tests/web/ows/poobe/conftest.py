import pytest
import requests
from MobileApps.libs.flows.web.poobe.poobe import PortalOOBE
from MobileApps.libs.flows.web.poobe.ecp import ECP
from MobileApps.libs.flows.web.poobe.flow_container import FlowContainer
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.flows.web.hp_id.hp_id import HPID


@pytest.fixture(scope="class")
def poobe_test_setup(web_session_setup, request):
    driver = web_session_setup
    driver.set_size("max")
    printer_profile = request.config.getoption("--printer-profile")
    biz_model = request.config.getoption("--printer-biz-model")
    endpoint, sku = None, None
    if "_" not in printer_profile or "real" in printer_profile:
        if "Flex" in biz_model:
            endpoint = "connect"
        elif "E2E" in biz_model:
            endpoint = "activate"
        if printer_profile in ["marconi", "kebin"]:
            endpoint = "onboard"
        if "beam" in printer_profile:
            endpoint = "go"
        if printer_profile in ["cherry", "lotus"]:
            endpoint = "startscan"
    elif "ecp" in printer_profile:
        endpoint = "pn"
    elif "pdl" in printer_profile:
        endpoint = "connect"
    fc = FlowContainer(driver, endpoint, printer_profile)
    p_oobe = fc.fd["poobe"]
    ecp = fc.fd["ecp"]
    hpid = fc.fd["hpid"]
    try:
        if "ecp" in printer_profile:
            driver.navigate(ecp.url)
        else:
            driver.navigate(p_oobe.poobe_url)
        hpid.handle_privacy_popup(timeout=5)
    except:
        attachment_root_path = c_misc.get_attachment_folder()
        c_misc.save_source_and_publish(driver, attachment_root_path, file_name="page_source.txt")
        c_misc.save_screenshot_and_publish(driver,"{}/screenshot_{}.png".format(attachment_root_path, request.node.name))
        if request.config.getoption("--har"):
            c_misc.save_har_and_publish(driver, attachment_root_path, file_name="poobe_har")
        raise AssertionError("Test Setup failed")
    
    return (driver, p_oobe, fc, printer_profile, biz_model, hpid)