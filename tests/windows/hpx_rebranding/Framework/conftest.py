import pytest
import logging

@pytest.fixture(scope="function")
def function_setup_clear_sign_out(request):
    """
    This function is called before each test case to sign out
    """
    if request.cls.fc.is_app_open():
        request.cls.fc.close_myHP()
    request.cls.fc.web_password_credential_delete()
    request.cls.fc.fd["profile"].minimize_chrome()
    for attempt in range(3):
        request.cls.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        if not request.cls.fc.is_app_open():
            logging.warning(f"HP app not launched, attempt {attempt+1} failed.")
            continue
        logging.info("HP app launched successfully...")
        request.cls.fc.fd["css"].maximize_hp()
        if request.cls.fc.fd["devices_details_pc_mfe"].verify_pc_device_name_show_up(raise_e=False):
            logging.info("PC device name is showing up.")
            break
        else:
            logging.info("No PC device name, verify device card show up.")
            if request.cls.fc.fd["devicesMFE"].verify_device_card_show_up(raise_e=False):
                logging.info("Device card is showing up.")
                break
            else:
                logging.warning("App launched but homepage didn't load/stuck in blue screen , retrying...")
        request.cls.fc.close_myHP()
    else:
        raise RuntimeError("Failed to launch HP app after multiple attempts.")

@pytest.fixture(scope="function")
def function_setup_myhp_launch(request):
    """
    This function is launch and close application before and after each test case.
    """
    if request.cls.fc.is_app_open():
        request.cls.fc.close_myHP()
    request.cls.fc.kill_chrome_process()
    for attempt in range(3):
        request.cls.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        if not request.cls.fc.is_app_open():
            logging.warning(f"HP app not launched, attempt {attempt+1} failed.")
            continue
        logging.info("HP app launched successfully...")
        request.cls.fc.fd["css"].maximize_hp()
        if request.cls.fc.fd["devices_details_pc_mfe"].verify_pc_device_name_show_up(raise_e=False):
            logging.info("PC device name is showing up.")
            break
        else:
            logging.info("No PC device name, verify device card show up.")
            if request.cls.fc.fd["devicesMFE"].verify_device_card_show_up(raise_e=False):
                logging.info("Device card is showing up.")
                break
            else:
                logging.warning("App launched but homepage didn't load/stuck in blue screen/blank screen , retrying...")
        request.cls.fc.close_myHP()
    else:
        raise RuntimeError("Failed to launch HP app after multiple attempts.")

@pytest.fixture(scope="function")
def function_setup_to_reset_and_launch_myhp(request):
    """
    This function is called before each test case to reset and launch HP app.
    """
    if request.cls.fc.is_app_open():
        request.cls.fc.close_myHP()
    if "skip_kill_chrome" not in request.node.keywords:
        request.cls.fc.kill_chrome_process()
    for attempt in range(3):
        request.cls.fc.reset_myHP_app_through_command(launch_app=True)
        if not request.cls.fc.is_app_open():
            logging.warning(f"HP app not launched, attempt {attempt+1} failed.")
            continue
        logging.info("HP app launched successfully...")
        request.cls.fc.fd["css"].maximize_hp()
        if request.cls.fc.fd["app_consents"].verify_accept_all_button_show_up():
            break
        else:
            logging.warning("App launched but consents page didn't load/stuck in blue screen , retrying...")
            request.cls.fc.close_myHP()
    else:
        raise RuntimeError("Failed to launch HP app after multiple attempts.")

def pytest_collection_modifyitems(config, items):
    stack = config.getoption("--stack")
    
    skip_markers = {
        "rebrand_production": "skip_in_prod",
        "rebrand_stage": "skip_in_stg",
        "rebrand_pie": "skip_in_pie"
    }
    
    if stack in skip_markers:
        marker_to_skip = skip_markers[stack]
        deselected = []
        selected = []
        
        for item in items:
            if marker_to_skip in item.keywords:
                deselected.append(item)
            else:
                selected.append(item)
        
        items[:] = selected
        config.hook.pytest_deselected(items=deselected)