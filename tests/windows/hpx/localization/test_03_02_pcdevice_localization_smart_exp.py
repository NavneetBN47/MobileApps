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

@pytest.fixture(scope="session", params=["pc_device_smart_exp_screenshot"])
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

    def test_03_pcdevice_module_smart_exp_C35437880(self, language):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/smartexperienceLocalization.json", language, "smartExperiences")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        time.sleep(3)
        ma_misc.create_localization_screenshot_folder("pc_device_smart_exp_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_device_smart_exp_screenshot/{}_pc_device_smart_exp.png".format(language))
        time.sleep(3)
        #presence_detection
        expected_presence_detection_text = lang_settings["presenceDetection"]["title"].strip()
        actual_presence_detection_text = self.fc.fd["devices"].verify_presence_detection_text().strip()
        soft_assertion.assert_equal(actual_presence_detection_text, expected_presence_detection_text, f"Presence_detection text is not matching. expected string text is {expected_presence_detection_text}, but got {actual_presence_detection_text}. ")
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        soft_assertion.raise_assertion_errors()
