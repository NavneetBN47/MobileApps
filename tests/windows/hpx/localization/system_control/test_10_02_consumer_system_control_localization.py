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

@pytest.fixture(scope="session", params=["system_control_consumer_screenshot"])
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
        
    def test_10_system_control_module_C37720624(self, language):# 6 modes in consumer machine
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/systemcontrolLocalization.json", language, "thermalControl")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        assert bool(self.fc.fd["devices"].verify_system_control_card()) is True, "System control module is not available"
        logging.info("System control module available")
        self.fc.fd["devices"].click_system_control_card()
        #system control header
        expected_system_control_header_text=lang_settings["title"]
        actual_system_control_header_text=self.fc.fd["system_control"].get_system_control_header_text()
        ma_misc.create_localization_screenshot_folder("system_control_consumer_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "system_control_consumer_screenshot/{}_system_control_homepage.png".format(language))
        soft_assertion.assert_equal(expected_system_control_header_text, actual_system_control_header_text, "System control header text is not matching for {}".format(language))
        #Performance Control
        expected_performance_control_text=lang_settings["performanceControl"]
        actual_performance_control_text=self.fc.fd["system_control"].get_system_control_title()
        soft_assertion.assert_equal(expected_performance_control_text, actual_performance_control_text, "Performance control text is not matching for {}".format(language))    
        
        #performance control tool tip------------xpath for this element not working
        self.fc.fd["system_control"].click_system_control_title_tooltip()
        performance1_text=lang_settings["performanceControl"]
        performance2_text=lang_settings["thermalSettingTooltip"]
        expected_performance_control_tool_tip_text = performance1_text+performance2_text
        actual_performance_control_tool_tip_text = self.fc.fd["system_control"].get_system_control_title_tooltip()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "system_control_consumer_screenshot/{}_system_control_thermal_setting_tooltips.png".format(language))
        soft_assertion.assert_equal(expected_performance_control_tool_tip_text, actual_performance_control_tool_tip_text, "Performance control tool tip text is not matching for {}".format(language))
               
        #performance control description
        expected_performance_control_sub_text = lang_settings["performanceControlDescription"]
        actual_performance_control_sub_text = self.fc.fd["system_control"].get_system_control_subtitle()
        soft_assertion.assert_equal(expected_performance_control_sub_text, actual_performance_control_sub_text, "Performance control sub text is not matching for {}".format(language))
        #smart sense display in english for al languages
        #smart sense tool tip
        self.fc.fd["system_control"].click_smart_sense_tool_tip_consumer()
        smart_sense1_text="Smart Sense"
        smart_sense2_text=lang_settings["smartSenseTooltip"]
        expected_smart_sense_tool_tip=smart_sense1_text+smart_sense2_text
        actual_smart_sense_tool_tip=self.fc.fd["system_control"].get_smart_sense_tooltip_consumer()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "system_control_consumer_screenshot/{}_system_control_smart_sence_tooltips.png".format(language))
        soft_assertion.assert_equal(expected_smart_sense_tool_tip, actual_smart_sense_tool_tip, "Smart sense tool tip text is not matching for {}".format(language))
        #balanced
        expected_balanced_text=lang_settings["balanced"]
        actual_balanced_text=self.fc.fd["system_control"].get_balanced()
        soft_assertion.assert_equal(expected_balanced_text, actual_balanced_text, "Balanced text is not matching for {}".format(language))
        #balance tool tip
        self.fc.fd["system_control"].click_balanced_tooltip_consumer()
        balanced1_text=lang_settings["balanced"]
        balanced2_text=lang_settings["balancedTooltip"]
        expected_balanced_tool_tip_text=balanced1_text+balanced2_text
        actual_balanced_tool_tip_text=self.fc.fd["system_control"].get_balanced_tooltip_consumer()
        soft_assertion.assert_equal(expected_balanced_tool_tip_text, actual_balanced_tool_tip_text, "Balanced tool tip text is not matching for {}".format(language)) 
        #cool
        expected_cool_text=lang_settings["cool"]
        actual_cool_text=self.fc.fd["system_control"].get_cool()
        soft_assertion.assert_equal(expected_cool_text, actual_cool_text, "Cool text is not matching for {}".format(language))
        #cool tool tip
        self.fc.fd["system_control"].click_cool_tooltip_consumer()
        cool1_text=lang_settings["cool"]
        cool2_text=lang_settings["coolTooltip"]
        expected_cool_tool_tip_text=cool1_text+cool2_text
        actual_cool_tool_tip_text=self.fc.fd["system_control"].get_cool_tooltip_consumer()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "system_control_consumer_screenshot/{}_system_control_cool_tooltips.png".format(language))
        soft_assertion.assert_equal(expected_cool_tool_tip_text, actual_cool_tool_tip_text, "Cool tool tip text is not matching for {}".format(language))
        #quiet
        expected_quiet_text=lang_settings["quiet"]
        actual_quiet_text=self.fc.fd["system_control"].get_quiet()
        soft_assertion.assert_equal(expected_quiet_text, actual_quiet_text, "Quiet text is not matching for {}".format(language))
        #quiet tool tip
        self.fc.fd["system_control"].click_quiet_tooltip_consumer()
        text1_text=lang_settings["quiet"]
        text2_text=lang_settings["quietTooltip"]
        expected_quiet_tool_tip_text=text1_text+text2_text
        actual_quiet_Tool_tip_text=self.fc.fd["system_control"].get_quiet_tooltip_consumer()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "system_control_consumer_screenshot/{}_system_control_quiet_tooltips.png".format(language))
        soft_assertion.assert_equal(expected_quiet_tool_tip_text, actual_quiet_Tool_tip_text, "Quiet tool tip text is not matching for {}".format(language))
        #performance
        expected_performance_text=lang_settings["performance"]
        actual_performance_text=self.fc.fd["system_control"].get_performance()
        soft_assertion.assert_equal(expected_performance_text, actual_performance_text, "Performance text is not matching for {}".format(language))
        #performance tool tip
        self.fc.fd["system_control"].click_performance_tooltip_consumer()
        expected_performance_tool_tip_text=lang_settings["performanceTooltip"]
        actual_performance_tool_tip_text=self.fc.fd["system_control"].get_performance_tooltip_consumer()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "system_control_consumer_screenshot/{}_system_control_performance_tooltips.png".format(language))
        soft_assertion.assert_equal(expected_performance_tool_tip_text, actual_performance_tool_tip_text, "Performance tool tip text is not matching for {}".format(language))
        #power saver---currently not displaying this mode
        expected_power_saver_text=lang_settings["powerSaver"]
        actual_power_saver_text=self.fc.fd["system_control"].get_power_saver()
        soft_assertion.assert_equal(expected_power_saver_text, actual_power_saver_text, "Power saver text is not matching for {}".format(language))
        #power saver tool tip
        self.fc.fd["system_control"].click_power_saver_tooltip_consumer()
        power1_text=lang_settings["powerSaver"]
        power2_text=lang_settings["powerSaverTooltip"]
        expected_power_saver_tooltip_text=power1_text+power2_text
        actual_power_saver_tooltip_text=self.fc.fd["system_control"].get_power_saver_tooltip_consumer()
        soft_assertion.assert_equal(expected_power_saver_tooltip_text, actual_power_saver_tooltip_text, "Power saver tool tip text is not matching for {}".format(language))
        
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
