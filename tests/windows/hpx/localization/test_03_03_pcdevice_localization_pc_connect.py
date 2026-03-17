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

#languages=['zh-Hant-HK','en-GB''zh-Hans', 'zh-Hant', 'es-MX','id-ID'] language not covered in pcdevice--Please refer ticket HPXWC-11174,HPXWC-11139

@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["pc_device_pc_connect_screenshot"])
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

    def test_03_pcdevice_module_pc_connect_C35439257(self, language):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/pcdeviceLocalization.json", language, "pCDevice")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        time.sleep(3)
        ma_misc.create_localization_screenshot_folder("pc_device_pc_connect_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_device_pc_connect_screenshot/{}_pc_device_pc_connect.png".format(language))
        # 5G
        expected_5g_text = lang_settings["actions"]["connectivity"]["title3"]
        actual_5g_text = self.fc.fd["devices"].get_5g_text()
        soft_assertion.assert_equal(actual_5g_text, expected_5g_text, f"5g title text is not matching. expected string text is {expected_5g_text}, but got {actual_5g_text}. ")
        expected_5g_des_text = lang_settings["actions"]["connectivity"]["description"]
        actual_5g_des_text = self.fc.fd["devices"].get_5g_des_text()
        soft_assertion.assert_equal(actual_5g_des_text, expected_5g_des_text, f"5g des text is not matching. expected string text is {expected_5g_des_text}, but got {actual_5g_des_text}. ")
        #battery tool tip
        time.sleep(3)
        self.fc.fd["devices"].click_battery_tool_tip()
        self.battery_tool_tip=self.fc.fd["devices"].get_battery_tool_tip()
        actual_battery_tool_tip_text=self.battery_tool_tip.split(" ")[0]
        expected_battery_tool_tip_text=lang_settings["status"]["battery"]["title"]
        logging.info("actual_battery_tool_tip_text:{}".format(actual_battery_tool_tip_text))
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_device_screenshot/{}_pc_device_battery_tooltips.png".format(language))
        soft_assertion.assert_equal(actual_battery_tool_tip_text, expected_battery_tool_tip_text, f"Battery tool tip text is not matching. expected string text is {expected_battery_tool_tip_text}, but got {actual_battery_tool_tip_text}. ")

        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        soft_assertion.raise_assertion_errors()