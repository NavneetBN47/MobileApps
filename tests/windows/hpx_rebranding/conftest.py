import pytest
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx_rebranding.utility.vcosmos_utilities import VcosmosUtilities
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.ma_misc import conftest_misc
import time
import shutil
import logging
import MobileApps.resources.const.windows.const as w_const

class PlatformNotMarkedException(Exception):
    pass

def pytest_addoption(parser):
    test_option = parser.getgroup('Windows HPX Test Parameters')
    test_option.addoption("--app-type", action="store", default="integration", help="The type of app you would like to run")
    test_option.addoption("--app-env", action="store", default="stg", help="The env of app you would like to run")
    test_option.addoption("--ota-test", action="store", default=None, help="HPX Rebrand OTA tesing")
    test_option.addoption("--screenshot-workspace", action="store", default=None, help="Copy screenshot zip file to jenkins workspace")
    test_option.addoption("--languages", action="store", default="en-US", help="Specify a comma-separated list of language codes for testing")


def pytest_runtest_setup(item):
    if 'print' in str(item.fspath):
        return
    else: 
        platform_path = "C:\\Users\\exec\\platform.txt"
        stack = item.config.getoption("--stack")
        mobile_device = item.config.getoption("--mobile-device")
        ssh = SSH(mobile_device, "exec")
        if not (platform := ssh.send_command(f"cat {platform_path}", raise_e=False)):
            raise PlatformNotMarkedException(f"The machine: {mobile_device} is not marked with a platfrom at {platform_path}")
        
        stack_mark = [mark.args[0] for mark in item.iter_markers(name="require_stack")]
        exclude_platform_mark = [mark.args[0] for mark in item.iter_markers(name="exclude_platform")]
        require_platform_mark = [mark.args[0] for mark in item.iter_markers(name="require_platform")]

        platform = platform["stdout"].rstrip()

        if stack_mark and stack not in stack_mark[0]:
            pytest.skip(f"Test does not run on stack: {stack}")
        
        if exclude_platform_mark and platform in exclude_platform_mark[0]:
            pytest.skip(f"Test does not run on platform: {exclude_platform_mark} current platform: {platform}")

        if require_platform_mark and platform not in require_platform_mark[0]:
            pytest.skip(f"Test only run on platfrom: {require_platform_mark} current platform: {platform}")


@pytest.fixture(scope="session")
def publish_hpx_rebrand_localization_screenshot(request, screenshot_folder_name):
    yield "Compress screenshot files."
    workspace = request.config.getoption("--screenshot-workspace")
    time.sleep(2)
    attachment_path = conftest_misc.get_attachment_folder()
    conftest_misc.save_localization_screenshot_and_publish(attachment_path + screenshot_folder_name + "/", attachment_path + screenshot_folder_name + ".zip")

    if workspace is not None:
        try:
            shutil.copy(attachment_path + screenshot_folder_name + ".zip", workspace + "/" + screenshot_folder_name + ".zip")
        except Exception as e:
            logging.info(f"Error occurred while creating copy file: {e}")   

@pytest.fixture(scope="session")
def language(request):
    language_codes = request.config.getoption("--languages")
    return language_codes

@pytest.fixture(scope="class")
def class_setup_fixture(request, windows_test_setup):
    # Change the parameter order - request must come first
    request.cls.driver = windows_test_setup
    request.cls.platform = request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
    request.cls.fc = FlowContainer(request.cls.driver)
    request.cls.fc.launch_app()

@pytest.fixture(scope="class")
def class_setup_fixture_for_desktop(request, windows_test_setup):
    # Change the parameter order - request must come first
    request.cls.driver = windows_test_setup
    request.cls.platform = request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
    request.cls.fc = FlowContainer(request.cls.driver)
    request.cls.fc.launch_myHP()

@pytest.fixture(scope="class", autouse=True)
def class_setup_fixture_app_cleanup(request, windows_test_setup):
    """
    Kill processes for PSADriverApp, HPPrinterHealthMonitor and HPAudioControl_19H1 if they are running
    """
    request.cls.driver = windows_test_setup
    process_output = request.cls.driver.ssh.send_command("Get-Process")["stdout"]
    process_names = ["PSADriverApp", "HPPrinterHealthMonitor", "HPAudioControl_19H1"]
    for pname in process_names:
        if pname in process_output:
            request.cls.driver.ssh.send_command(f'Stop-Process -Name "{pname}"', raise_e = False, timeout=10)

@pytest.fixture(scope="class")
def class_setup_fixture_funtional_ota(request, windows_test_setup):
        request.cls.driver = windows_test_setup
        request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        request.cls.fc = FlowContainer(request.cls.driver)          
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            request.cls.fc.launch_myHP()
            time.sleep(10)
            request.cls.fc.ota_app_after_update()
        else:
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
        time.sleep(5)
        yield
        try:    
            request.cls.fc.copy_rebrand_logs_with_timestamp()
            time.sleep(2)
            if request.config.getoption("--ota-test") is not None:
                request.cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
            print(f"[teardown warning] failed: {e}")

@pytest.fixture(scope="class")
def class_setup_fixture_robotics_usb_and_charger(request, windows_test_setup):
        request.cls.driver = windows_test_setup
        request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        request.cls.vcosmos=VcosmosUtilities(request.cls.driver.ssh)
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.process_util = ProcessUtilities(request.cls.driver.ssh) 
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
            time.sleep(5)
            request.cls.fc.ota_app_after_update()
        else:
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
        time.sleep(5)
        yield
        try:
            request.cls.fc.copy_rebrand_logs_with_timestamp()
            time.sleep(2)
            request.cls.vcosmos.add_charger_and_usb()
            request.cls.vcosmos.clean_up_logs()
            request.cls.fc.copy_log_with_timestamp()
            if request.config.getoption("--ota-test") is not None:
                request.cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
            print(f"[teardown warning] failed: {e}")

@pytest.fixture(scope="class")
def class_setup_fixture_oobe(request, windows_test_setup):
    request.cls.driver = windows_test_setup
    request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
    request.cls.process_util = ProcessUtilities(request.cls.driver.ssh)
    request.cls.fc = FlowContainer(request.cls.driver)  
    request.cls.fc.change_system_region_to_united_states()
    request.cls.fc.install_video_apps_from_ms_store_for_disney("Disney+","disney_plus_app_ms_store")
    time.sleep(20)
    request.cls.fc.kill_msstore_process()
    time.sleep(10)
    request.cls.fc.change_system_region_to_china()
    time.sleep(15)
    request.cls.fc.install_video_apps_from_ms_store("腾讯视频","tencent_video_app_ms_store")
    time.sleep(15)
    request.cls.fc.install_video_apps_from_ms_store("爱奇艺","iqiyi_video_app_ms_store")
    time.sleep(15)
    request.cls.fc.kill_msstore_process()
    time.sleep(5)
    request.cls.fc.change_system_region_to_united_states()
    if request.config.getoption("--ota-test") is not None:
        time.sleep(10)
        request.cls.fc.launch_myHP()
        time.sleep(5)
        request.cls.fc.ota_app_after_update()
    else:
        request.cls.fc.add_capture_logs_file()
        time.sleep(5)
        request.cls.fc.launch_myHP()
    time.sleep(5)
    yield
    try:
        request.cls.fc.copy_rebrand_logs_with_timestamp()
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.exit_hp_app_and_msstore()
            request.cls.vcosmos.clean_up_logs()
    except Exception as e:
        print(f"[teardown warning] failed: {e}")
    request.cls.fc.kill_tencent_video_process()
    request.cls.fc.kill_iqiyi_video_process()
    request.cls.fc.kill_disney_video_process()
    request.cls.fc.kill_msstore_process()
    

@pytest.fixture(scope="class")
def class_setup_fixture_oobe_robotics(request, windows_test_setup):
    request.cls.driver = windows_test_setup
    request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
    request.cls.process_util = ProcessUtilities(request.cls.driver.ssh)
    request.cls.fc = FlowContainer(request.cls.driver)  
    request.cls.vcosmos=VcosmosUtilities(request.cls.driver.ssh)
    request.cls.fc.change_system_region_to_united_states()
    request.cls.fc.close_myHP()
    request.cls.fc.install_video_apps_from_ms_store_for_disney("Disney+","disney_plus_app_ms_store")
    time.sleep(20)
    request.cls.fc.kill_msstore_process()
    time.sleep(10)
    request.cls.fc.change_system_region_to_china()
    time.sleep(15)
    request.cls.fc.install_video_apps_from_ms_store("腾讯视频","tencent_video_app_ms_store")
    time.sleep(15)
    request.cls.fc.install_video_apps_from_ms_store("爱奇艺","iqiyi_video_app_ms_store")
    time.sleep(15)
    request.cls.fc.kill_msstore_process()
    time.sleep(5)
    request.cls.fc.change_system_region_to_united_states()
    if request.config.getoption("--ota-test") is not None:
        time.sleep(10)
        request.cls.fc.add_capture_logs_file()
        time.sleep(5)
        request.cls.fc.launch_myHP()
        time.sleep(5)
        request.cls.fc.ota_app_after_update()
    else:
        request.cls.fc.add_capture_logs_file()
        time.sleep(5)
        request.cls.fc.launch_myHP()
    time.sleep(5)
    yield
    try:
        request.cls.fc.copy_rebrand_logs_with_timestamp()
        time.sleep(2)
        request.cls.vcosmos.clean_up_logs()
        request.cls.fc.copy_log_with_timestamp()
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.exit_hp_app_and_msstore()
    except Exception as e:
        print(f"[teardown warning] failed: {e}")

@pytest.fixture(scope="class")
def class_setup_fixture_robotics_led_or_button(request, windows_test_setup):
        request.cls.driver = windows_test_setup
        request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        request.cls.vcosmos=VcosmosUtilities(request.cls.driver.ssh)
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.process_util = ProcessUtilities(request.cls.driver.ssh) 
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
            time.sleep(5)
            request.cls.fc.ota_app_after_update()
        else:
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
        time.sleep(5)
        yield
        try:
            request.cls.fc.copy_rebrand_logs_with_timestamp()
            time.sleep(2)
            request.cls.vcosmos.clean_up_logs()
            request.cls.fc.copy_log_with_timestamp()
            if request.config.getoption("--ota-test") is not None:
                request.cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
            print(f"[teardown warning] failed: {e}")

@pytest.fixture(scope="class")
def class_setup_fixture_robotics_usb_and_3_5mm(request, windows_test_setup):
        request.cls.driver = windows_test_setup
        request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        request.cls.vcosmos=VcosmosUtilities(request.cls.driver.ssh)
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.process_util = ProcessUtilities(request.cls.driver.ssh)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
            time.sleep(5)
            request.cls.fc.ota_app_after_update()
        else:
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
        time.sleep(5)
        yield
        try:
            request.cls.fc.copy_rebrand_logs_with_timestamp()
            time.sleep(2)
            request.cls.vcosmos.add_charger_and_usb()
            request.cls.vcosmos.remove_3_5_headphone()
            request.cls.vcosmos.clean_up_logs()
            request.cls.fc.copy_log_with_timestamp()
            if request.config.getoption("--ota-test") is not None:
                request.cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
            print(f"[teardown warning] failed: {e}")

@pytest.fixture(scope="class")
def class_setup_fixture_robotics_3_5mm(request, windows_test_setup):
        request.cls.driver = windows_test_setup
        request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        request.cls.vcosmos=VcosmosUtilities(request.cls.driver.ssh)
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.process_util = ProcessUtilities(request.cls.driver.ssh)         
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
            time.sleep(5)
            request.cls.fc.ota_app_after_update()
        else:
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
        time.sleep(5)
        yield
        try:
            request.cls.fc.copy_rebrand_logs_with_timestamp()
            time.sleep(2)
            request.cls.vcosmos.remove_3_5_headphone()
            request.cls.vcosmos.clean_up_logs()
            request.cls.fc.copy_log_with_timestamp()
            if request.config.getoption("--ota-test") is not None:
                request.cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
            print(f"[teardown warning] failed: {e}")

@pytest.fixture(scope="class")
def class_setup_fixture_ota_regression(request):
    request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
    request.cls.fc.change_system_region_to_united_states()       # setting system region to US as default
    request.cls.fc.terminate_conflicting_hp_processes()
    request.cls.fc.fd["accessibility"].dismiss_open_windows_overlays()
    request.cls.fc.web_password_credential_delete()
    local_build = request.config.getoption("--local-build")
    if request.config.getoption("--ota-test") is not None:
        request.cls.fc.install_bundle(local_build)
        request.cls.fc.launch_myHP(terminate_hp_background_apps=True)
        request.cls.fc.fd["css"].maximize_hp()
        request.cls.fc.ota_app_after_update()
    else:
        request.cls.fc.launch_myHP(terminate_hp_background_apps=True)
        request.cls.fc.fd["css"].maximize_hp()
    request.cls.fc.close_myHP()


@pytest.fixture(scope="class")
def class_setup_fixture_capture_logs(request, windows_test_setup):
        request.cls.driver = windows_test_setup
        request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.process_util = ProcessUtilities(request.cls.driver.ssh)          
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
            time.sleep(5)
            request.cls.fc.ota_app_after_update()
        else:
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
        time.sleep(5)
        yield
        try:
            request.cls.fc.copy_rebrand_logs_with_timestamp()
            if request.config.getoption("--ota-test") is not None:
                request.cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
            print(f"[teardown warning] failed: {e}")


@pytest.fixture(scope="class")
def class_setup_fixture_funtional_audio(request, windows_test_setup):
        request.cls.driver = windows_test_setup
        request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        request.cls.fc = FlowContainer(request.cls.driver)          
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            request.cls.fc.launch_myHP()
            time.sleep(5)
            request.cls.fc.ota_app_after_update()
        else:
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
        time.sleep(5)
        yield
        try:    
            request.cls.fc.copy_rebrand_logs_with_timestamp()
            if request.config.getoption("--ota-test") is not None:
                request.cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
            print(f"[teardown warning] failed: {e}")
        request.cls.fc.restart_myHP()
        time.sleep(5)
        request.cls.fc.fd["devicesMFE"].click_device_card()
        time.sleep(4)
        assert request.cls.fc.fd["devices_details_pc_mfe"].verify_audio_card_show_up(), "Audio card is not displayed"
        request.cls.fc.fd["devices_details_pc_mfe"].click_audio_card()
        time.sleep(2)
        assert request.cls.fc.fd["audio"].verify_external_speaker_settings_show_up(), "External speaker settings is not displayed"
        request.cls.fc.fd["audio"].click_external_speaker_settings()
        time.sleep(2)
        assert request.cls.fc.fd["audio"].verify_external_speaker_settings_text_show_up(), "External speaker settings text is not displayed"
        if request.cls.fc.fd["audio"].get_multistreaming_toggle_off_state() == "0":
            request.cls.fc.fd["audio"].click_multistreaming_toggle_off_state()
            time.sleep(2)
            assert request.cls.fc.fd["audio"].get_multistreaming_toggle_on_state() == "1", "Multistreaming toggle is not turned on"


@pytest.fixture(scope="class")
def class_setup_fixture_functional_standalone_app(request, windows_test_setup):
        request.cls.driver = windows_test_setup
        request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        request.cls.fc = FlowContainer(request.cls.driver)          
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            request.cls.fc.launch_myHP()
            time.sleep(10)
            request.cls.fc.ota_app_after_update()
        else:
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
            time.sleep(5)
        yield
        try:    
            if request.config.getoption("--ota-test") is not None:
                request.cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
                print(f"[teardown warning] failed: {e}")
        request.cls.fc.uninstall_audio_standalone_app_for_commercial_machine()


@pytest.fixture(scope="class")
def class_setup_fixture_functional_MEP_notification(request, windows_test_setup):
        request.cls.driver = windows_test_setup
        request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        request.cls.fc = FlowContainer(request.cls.driver)          
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            request.cls.fc.launch_myHP()
            time.sleep(10)
            request.cls.fc.ota_app_after_update()
        else:
            request.cls.fc.launch_myHP()
            time.sleep(5)
        yield
        try:
            request.cls.fc.copy_rebrand_logs_with_timestamp()
            if request.config.getoption("--ota-test") is not None:
                request.cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
                print(f"[teardown warning] failed: {e}")
        request.cls.fc.open_system_settings_notifications()
        time.sleep(3)
        if "Maximize Settings" == request.cls.fc.fd["audio"].verify_system_settings_window_maximize():
            request.cls.fc.fd["audio"].click_on_system_settings_maximize_button()
        else:
            request.cls.fc.open_system_settings_notifications()
            time.sleep(3)
            request.cls.fc.fd["audio"].click_on_system_settings_maximize_button()
        if request.cls.fc.fd["audio"].verify_hp_notification_toggle_on_windows_settings_page_show_up():
            if request.cls.fc.fd["audio"].is_hp_notification_toggle_enabled() == "0":
                request.cls.fc.fd["audio"].click_hp_notification_toggle_on_windows_settings_page()
                time.sleep(3)
            assert request.cls.fc.fd["audio"].is_hp_notification_toggle_enabled() == "1", "HP notification toggle is not turned on"
        request.cls.fc.close_windows_settings_panel()

    
@pytest.fixture(scope="class")
def class_setup_fixture_functional_audio_level(request, windows_test_setup):
        request.cls.driver = windows_test_setup
        request.cls.platform=request.cls.driver.ssh.send_command('cat {}'.format(w_const.TEST_DATA.PLATFORM_FILE))['stdout'].strip()
        request.cls.fc = FlowContainer(request.cls.driver)          
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            request.cls.fc.launch_myHP()
            time.sleep(10)
            request.cls.fc.ota_app_after_update()
        else:
            request.cls.fc.add_capture_logs_file()
            time.sleep(5)
            request.cls.fc.launch_myHP()
        time.sleep(5)
        yield
        try:    
            request.cls.fc.copy_rebrand_logs_with_timestamp()
            time.sleep(2)
            if request.config.getoption("--ota-test") is not None:
                request.cls.fc.exit_hp_app_and_msstore()
        except Exception as e:
            print(f"[teardown warning] failed: {e}")
        request.cls.fc.close_windows_settings_panel()