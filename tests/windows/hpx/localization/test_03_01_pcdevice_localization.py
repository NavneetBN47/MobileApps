import logging
import re
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
import re
import time
from MobileApps.libs.ma_misc import conftest_misc
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert

pytest.app_info = "HPX"
language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')


@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["pc_device_screenshot"])
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

    def test_03_pcdevice_module_C33045054(self, language):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/pcdeviceLocalization.json", language, "pCDevice")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        time.sleep(3)
        ma_misc.create_localization_screenshot_folder("pc_device_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_device_screenshot/{}_pc_device.png".format(language))
        # Audio control
        time.sleep(3)
        actual_audio_control_text = self.fc.fd["devices"].get_audio_control_text_on_card()
        expected_audio_control_text = lang_settings["actions"]["audioControl"]["featureCard"]
        soft_assertion.assert_equal(actual_audio_control_text, expected_audio_control_text, f"Audio control card text is not matching. expected string text is {expected_audio_control_text}, but got {actual_audio_control_text}. ")
        # support
        time.sleep(3)
        actual_support_title_text = self.fc.fd["devices"].get_support_title_text()
        expected_support_title_text = lang_settings["actions"]["support"]["titleHpOne"]
        if actual_support_title_text=="24/7 Pro live support":
            expected_support_title_text = lang_settings["actions"]["support"]["titleHpOne"]
        elif actual_support_title_text=="Support":
            expected_support_title_text = lang_settings["actions"]["support"]["title"]
        soft_assertion.assert_equal(actual_support_title_text, expected_support_title_text, f"Support module title text is not matching. expected string text is {expected_support_title_text}, but got {actual_support_title_text}. ")
        # HPPK
        time.sleep(3)
        lang_settings_1 = self.fc.processing_localization_language("resources/test_data/hpx/programmablekeyLocalization.json", language, "progKey")
        expected_prog_key_text = lang_settings_1["featureCard"]
        actual_prog_key_text = self.fc.fd["devices"].get_prog_key_text()
        soft_assertion.assert_equal(actual_prog_key_text, expected_prog_key_text, f"Hppk module title text is not matching. expected string text is {expected_prog_key_text}, but got {actual_prog_key_text}. ")
        #click info icon
        time.sleep(3)
        self.fc.fd["devices"].click_infor_icon_on_device_page_header()
        #product number
        time.sleep(3)
        actual_product_number_text = self.fc.fd["devices"].get_display_product_number_on_pcdevice()
        expected_product_number_text = lang_settings["device"]["productNumber"]
        soft_assertion.assert_equal(actual_product_number_text, expected_product_number_text, f"Product number text is not matching. expected string text is {expected_product_number_text}, but got {actual_product_number_text}. ")
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_device_screenshot/{}_pc_device_product_number02.png".format(language))
        #serial number
        time.sleep(3)
        actual_serial_number_text = self.fc.fd["devices"].get_display_serial_number_on_pcdevice()
        expected_serial_number_text = lang_settings["device"]["serialNumber"]
        soft_assertion.assert_equal(actual_serial_number_text, expected_serial_number_text, f"Serial number text is not matching. expected string text is {expected_serial_number_text}, but got {actual_serial_number_text}. ")
        #warranty
        actual_warranty_text = self.fc.fd["devices"].get_verify_warranty_under_info_icon()
        expected_warranty_text = lang_settings["status"]["warranty"]["title"]
        soft_assertion.assert_equal(actual_warranty_text, expected_warranty_text, f"Warranty text is not matching. expected string text is {expected_warranty_text}, but got {actual_warranty_text}. ")
        #warranty unknown/Get details
        if bool(self.fc.fd["devices"].verify_unknown_text_value()) == True:
            actual_warranty_unknown_text = self.fc.fd["devices"].get_unknown_text()
            expected_warranty_unknown_text = lang_settings["status"]["warranty"]["unknown"]
            soft_assertion.assert_equal(actual_warranty_unknown_text, expected_warranty_unknown_text, f"Unknown text is not matching. expected string text is {expected_warranty_unknown_text}, but got {actual_warranty_unknown_text}. ")
        else:
            actual_get_details_text = self.fc.fd["devices"].get_get_detials_text()
            expected_get_details_text = lang_settings["status"]["warranty"]["getDetails"]
            soft_assertion.assert_equal(actual_get_details_text, expected_get_details_text, f"Get details text is not matching. expected string text is {expected_get_details_text}, but got {actual_get_details_text}. ")
        #battery tool tip
        time.sleep(3)
        self.fc.fd["devices"].click_battery_tool_tip()
        self.battery_tool_tip=self.fc.fd["devices"].get_battery_tooltips()
        actual_battery_tool_tip_text=self.battery_tool_tip.split(" ")[0]
        expected_battery_tool_tip_text=lang_settings["status"]["battery"]["title"]
        logging.info("actual_battery_tool_tip_text:{}".format(actual_battery_tool_tip_text))
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_device_screenshot/{}_pc_device_battery_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_battery_tool_tip_text, expected_battery_tool_tip_text, f"Battery tool tip text is not matching. expected string text is {expected_battery_tool_tip_text}, but got {actual_battery_tool_tip_text}. ")

        
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        soft_assertion.raise_assertion_errors()