import logging
import re
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
from MobileApps.libs.ma_misc import conftest_misc
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert

pytest.app_info = "HPX"

language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')

@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["dock_station_screenshot"])
def screenshot_folder_name(request):
    return request.param

class Test_Suite_Localization(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, publish_hpx_localization_screenshot, screenshot_folder_name):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.close_app()
        cls.fc.launch_app()
        cls.attachment_path = conftest_misc.get_attachment_folder()

    @pytest.mark.require_platform(["goldy"])
    def test_15_dock_station_localization_C43538957(self, language):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/dockstationLocalization.json", language, "pCDock")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        assert bool(self.fc.fd["dock_station"].verify_dock_station_module_show()) is True, "Dock station module is not displayed"
        logging.info("Dock Station module available")
        self.fc.fd["dock_station"].navigate_to_dock_station_page()
        #click on USB icon
        self.fc.fd["dock_station"].click_dock_station_connection_button()
        expected_connected_usb_text = lang_settings["connection"]
        connected_usb_text = self.fc.fd["dock_station"].get_dock_station_connection_tooltips()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "dock_station_screenshot/{}_dock_station_homepage02.png".format(language))
        soft_assertion.assert_contains(connected_usb_text, expected_connected_usb_text, f"Connected text is not matching, expected string text is {expected_connected_usb_text}, but got {connected_usb_text}. ")
        #click on info icon
        self.fc.fd["dock_station"].click_dock_station_infor_button()
        #Serial Number
        expected_serial_number = lang_settings["serialNumber"]
        actual_serial_number = self.fc.fd["dock_station"].get_dock_station_serial_number()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "dock_station_screenshot/{}_dock_station_homepage03.png".format(language))
        soft_assertion.assert_equal(actual_serial_number, expected_serial_number, f"Serial Number text is not matching, expected string text is {expected_serial_number}, but got {actual_serial_number}. ")
        #Firmware version
        expected_firmware_version = lang_settings["firmwareVersion"]
        actual_firmware_version = self.fc.fd["dock_station"].get_dock_station_firmware_version()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "dock_station_screenshot/{}_dock_station_homepage04.png".format(language))
        soft_assertion.assert_equal(actual_firmware_version, expected_firmware_version, f"Firmware Version text is not matching, expected string text is {expected_firmware_version}, but got {actual_firmware_version}. ")

        self.fc.fd["dock_station"].click_dock_station_infor_button()
        #Dock Support
        expected_dock_support_text = lang_settings["supportButton"]
        actual_dock_support_text = self.fc.fd["dock_station"].get_dock_station_support_button_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "dock_station_screenshot/{}_dock_station_homepage05.png".format(language))
        soft_assertion.assert_equal(actual_dock_support_text, expected_dock_support_text, f"Dock Support text is not matching, expected string text is {expected_dock_support_text}, but got {actual_dock_support_text}. ")
        
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        soft_assertion.raise_assertion_errors()
