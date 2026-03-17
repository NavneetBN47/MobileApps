import logging
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

@pytest.fixture(scope="session", params=["system_control_commercial_screenshot"])
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
        
    def test_10_system_control_module_C35103448(self, language):# 4 modes on commercial machines
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/systemcontrolLocalization.json", language, "thermalControl")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True, "System control module is not available"
        logging.info("System control module available")
        self.fc.fd["devices"].click_system_control_card()
        #system control header
        expected_system_control_header_text=lang_settings["moduleTitle"]
        actual_system_control_header_text=self.fc.fd["system_control"].get_system_control_header_text()
        ma_misc.create_localization_screenshot_folder("system_control_commercial_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "system_control_commercial_screenshot/{}_system_control_homepage.png".format(language))
        soft_assertion.assert_equal(expected_system_control_header_text, actual_system_control_header_text, "System control header text is not matching for {}".format(language))
        #Performance Control
        expected_thermal_setting_text=lang_settings["performanceControl"]
        actual_thermal_setting_text=self.fc.fd["system_control"].get_thermal_setting_text()
        soft_assertion.assert_equal(expected_thermal_setting_text, actual_thermal_setting_text, "Performance control text is not matching for {}".format(language))
        
        ##performance control tool tip
        self.fc.fd["system_control"].click_system_control_title_tooltip_commercial()
        performance1_text=lang_settings["performanceControl"]
        performance2_text=lang_settings["thermalSettingTooltip"]
        expected_performance_control_tool_tip_text = performance1_text+performance2_text
        actual_performance_control_tool_tip_text = self.fc.fd["system_control"].get_system_control_title_tooltip_commercial()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "system_control_consumer_screenshot/{}_system_control_thermal_setting_tooltips.png".format(language))
        soft_assertion.assert_equal(expected_performance_control_tool_tip_text, actual_performance_control_tool_tip_text, "Performance control tool tip text is not matching for {}".format(language))
        
        #Performance Control description
        expected_thermal_setting_sub_text=lang_settings["performanceControlDescription"]
        actual_thermal_setting_sub_text=self.fc.fd["system_control"].get_thermal_setting_sub_text()
        soft_assertion.assert_equal(expected_thermal_setting_sub_text, actual_thermal_setting_sub_text, "Performance control description text is not matching for {}".format(language))
        #smart sense display in english for al languages
        #smart sense tool tip
        self.fc.fd["system_control"].click_smart_sense_tool_tip()
        expected_smart_sense_tool_tip=lang_settings["smartSenseTooltip"]
        actual_smart_sense_tool_tip=self.fc.fd["system_control"].get_smart_sense_tool_tip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "system_control_commercial_screenshot/{}_system_control_smart_sense_tooltips.png".format(language))
        soft_assertion.assert_equal(expected_smart_sense_tool_tip, actual_smart_sense_tool_tip, "Smart sense tool tip text is not matching for {}".format(language))
        #performance
        expected_performance_text=lang_settings["performance"]
        actual_performance_text=self.fc.fd["system_control"].get_performance_commercial()
        soft_assertion.assert_equal(expected_performance_text, actual_performance_text, "Performance text is not matching for {}".format(language))
        #performance tool tip
        self.fc.fd["system_control"].click_performance_commercial_tooltip()
        expected_performance_tool_tip_text=lang_settings["performanceTooltip"]
        actual_performance_tool_tip_text=self.fc.fd["system_control"].get_performance_commercial_tooltip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "system_control_commercial_screenshot/{}_system_control_performance_tooltips.png".format(language))
        soft_assertion.assert_equal(expected_performance_tool_tip_text, actual_performance_tool_tip_text, "Performance tool tip text is not matching for {}".format(language))
        
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
