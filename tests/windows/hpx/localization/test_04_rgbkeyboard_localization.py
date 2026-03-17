import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
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

@pytest.fixture(scope="session", params=["rgb_keyboard_screenshot"])
def screenshot_folder_name(request):
    return request.param


class Test_Suite_Localization(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, publish_hpx_localization_screenshot, screenshot_folder_name):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.close_app()
        cls.fc.launch_app()
        cls.attachment_path = conftest_misc.get_attachment_folder()

    def test_04_rgbkeyboard_module_C33053786(self, language):
        soft_assertion = SoftAssert()
        lang_settings = ma_misc.load_json_file("resources/test_data/hpx/rgbkeyboardLocalization.json")[language]["translation"]
        self.fc.myhp_login_startup_for_localization_scripts(language)
        assert bool(self.fc.fd["devices"].verify_RGB_card_visible()) is True, "RGB module not available."
        logging.info("RGB module is available")
        self.fc.fd["devices"].click_rgb_keyword()
        # RGB Keyboard header text
        assert bool(self.fc.fd["rgb_keyboard"].verify_rgb_header()) is True
        expected_rgb_keyboard_text = self.fc.fd["rgb_keyboard"].get_rgb_keyboard_text()
        actual_rgb_keyboard_text = lang_settings["rgbKeyboard"]["title"]
        soft_assertion.assert_equal(actual_rgb_keyboard_text, expected_rgb_keyboard_text, f"RGB Keyboard header text is not matching, expected string text is {expected_rgb_keyboard_text}, but got {actual_rgb_keyboard_text}. ")
        # enable RGB lighting
        expected_rgb_lighting_text = lang_settings["displayLabel"]["rgbToggle"]
        actual_rgb_lighting_text = self.fc.fd["rgb_keyboard"].get_enable_rgb_lighting_text()
        ma_misc.create_localization_screenshot_folder("rgb_keyboard_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "rgb_keyboard_screenshot/{}_rgb_keyboard_homepage.png".format(language))
        soft_assertion.assert_equal(actual_rgb_lighting_text, expected_rgb_lighting_text, f"Enable RGB lighting text is not matching, expected string text is {expected_rgb_lighting_text}, but got {actual_rgb_lighting_text}. ")
        # static
        expected_static_text = lang_settings["effects"]["Static"]
        actual_static_text = self.fc.fd["rgb_keyboard"].get_static_text()
        soft_assertion.assert_equal(actual_static_text, expected_static_text, f"Static text is not matching, expected string text is {expected_static_text}, but got {actual_static_text}. ")
        # wave
        expected_wave_text = lang_settings["effects"]["Wave"]
        actual_wave_text = self.fc.fd["rgb_keyboard"].get_wave_text()
        soft_assertion.assert_equal(actual_wave_text, expected_wave_text, f"Wave text is not matching, expected string text is {expected_wave_text}, but got {actual_wave_text}. ")
        # #ripple
        expected_ripple_text = lang_settings["effects"]["Ripple"]
        actual_ripple_text = self.fc.fd["rgb_keyboard"].get_ripple_text()
        soft_assertion.assert_equal(actual_ripple_text, expected_ripple_text, f"Ripple text is not matching, expected string text is {expected_ripple_text}, but got {actual_ripple_text}. ")
        # breathing
        actual_breathing_text = self.fc.fd["rgb_keyboard"].get_breathing_text()
        expected_breathing_text = lang_settings["effects"]["Breathing"]
        soft_assertion.assert_equal(actual_breathing_text, expected_breathing_text, f"Ripple text is not matching, expected string text is {expected_breathing_text}, but got {actual_breathing_text}. ")
        # raindrops
        actual_raindrops_text = self.fc.fd["rgb_keyboard"].get_raindrops_text()
        expected_raindrops_text = lang_settings["effects"]["Raindrops"]
        soft_assertion.assert_equal(actual_raindrops_text, expected_raindrops_text, f"Raindrops text is not matching, expected string text is {expected_raindrops_text}, but got {actual_raindrops_text}. ")
        # colorcycle
        actual_colorcycle_text = self.fc.fd["rgb_keyboard"].get_colorcycle_text()
        expcted_colorcycle_text = lang_settings["effects"]["ColorCycle"]
        soft_assertion.assert_equal(actual_colorcycle_text, expcted_colorcycle_text, f"Colorcycle text is not matching, expected string text is {expcted_colorcycle_text}, but got {actual_colorcycle_text}. ")
        # restore Defaults button
        self.driver.swipe(direction="down", distance=1)
        actual_restore_button_text = self.fc.fd["rgb_keyboard"].get_restore_button_text()
        expected_restore_button_text = lang_settings["displayLabel"]["restoreDefaults"]
        soft_assertion.assert_equal(actual_restore_button_text, expected_restore_button_text, f"Restore Defaults text is not matching, expected string text is {expected_restore_button_text}, but got {actual_restore_button_text}. ")
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.fd["devices"].restore_app()
        soft_assertion.raise_assertion_errors()
