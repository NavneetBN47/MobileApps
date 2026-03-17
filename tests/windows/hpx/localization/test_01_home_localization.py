import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
from MobileApps.libs.ma_misc import conftest_misc

pytest.app_info = "HPX"
language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
with open(language_list_path, "r+") as f:
    languages = f.read().split(',')

@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["home_screenshot"])
def screenshot_folder_name(request):
    return request.param


class Test_Suite_Localization(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.close_app()
        cls.fc.launch_app()
        cls.attachment_path = conftest_misc.get_attachment_folder()

    def test_01_home_module_C33045047(self, language, publish_hpx_localization_screenshot, screenshot_folder_name):
        self.fc.update_properties(language)
        self.fc.close_app()
        self.fc.launch_app()
        time.sleep(6)
        if(self.fc.fd["hp_registration"].verify_registration_page_is_display()) is True:
            self.driver.swipe(direction="down", distance=3)
            if self.fc.fd["hp_registration"].verify_skip_button_show():
                self.fc.fd["hp_registration"].click_skip_button()
            else:
                logging.info("skip button not available")
        else:
            logging.info("registration page not displayed")
        lang_settings = ma_misc.load_json_file("resources/test_data/hpx/homepageLocalization.json")[language]["translation"]["welcome"]
        time.sleep(5)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        expected_home_text = lang_settings["title"]
        actual_home_text = self.fc.fd["navigation_panel"].verify_home_menu_navigation()
        assert actual_home_text == expected_home_text, "Home text is not matched"
        # control your PC
        actual_control_your_pc_text = self.fc.fd["home"].verify_control_your_pc()
        logging.info("ac="+str(actual_control_your_pc_text))
        expected_control_your_pc_text = lang_settings["actions"]["section"]
        logging.info("ex="+str(expected_control_your_pc_text))
        ma_misc.create_localization_screenshot_folder("home_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "home_screenshot/{}_home.png".format(language))
        assert actual_control_your_pc_text == expected_control_your_pc_text, "Control your PC text is not matched"
        # view all controls
        actual_view_all_controls_text = self.fc.fd["home"].get_view_all_controls_text()
        expected_view_all_controls_text = lang_settings["actions"]["controls"]
        assert actual_view_all_controls_text == expected_view_all_controls_text, "View all controls text is not matched"
        # video control card
        if bool(self.fc.fd["home"].verify_video_control_card_visible()) is True:
            # video control
            actual_video_control_text = self.fc.fd["home"].get_video_control_text()
            expected_video_control_text = lang_settings["actions"]["videoControl"]["title"]
            assert actual_video_control_text == expected_video_control_text, "Video control text is not matched"
        # optimize conference and stresming
            actual_optimize_conference_streaming_text = self.fc.fd["home"].get_optimize_conference_streaming_text()
            expected_optimize_conference_streaming_text = lang_settings["actions"]["videoControl"]["description4"]
            assert actual_optimize_conference_streaming_text == expected_optimize_conference_streaming_text, "Optimize conference and streaming text is not matched"
        else:
            logging.info("video control card not available")
        # HPPK card
        if bool(self.fc.fd["home"].verify_Programmable_Key_card_visible()) is True:
            # programmable key
            actual_prog_key_text = self.fc.fd["home"].get_prog_key_text()
            expected_prog_key_text = lang_settings["actions"]["programmableKey"]["title"]
            assert actual_prog_key_text == expected_prog_key_text, "Programmable key text is not matched"
        # create short cut text
            actual_create_short_cut_text = self.fc.fd["home"].get_create_short_cut_text()
            expected_create_short_cut_text = lang_settings["actions"]["programmableKey"]["description6"]
            assert actual_create_short_cut_text == expected_create_short_cut_text, "Create short cut text is not matched"
        # Display Card
        if bool(self.fc.fd["home"].verify_display_control_card_visible()) is True:
            # Display Control
            actual_display_control_title_text = self.fc.fd["home"].get_display_control_title_text()
            expected_display_control_title_text = lang_settings["actions"]["displayControl"]["title"]
            assert actual_display_control_title_text == expected_display_control_title_text, "Display control title text is not matched"
        # manage display settings
            actual_manage_display_setting_text = self.fc.fd["home"].get_manage_display_setting_text()
            expected_manage_display_setting_text = lang_settings["actions"]["displayControl"]["description6"]
            assert actual_manage_display_setting_text == expected_manage_display_setting_text, "Manage display setting text is not matched"
        else:
            logging.info("display control card not available")
            # Audio card
        if bool(self.fc.fd["home"].verify_AudioControl_card_visible()) is True:
            # Audio control
            expected_audio_control_text = lang_settings["actions"]["audioControl"]["title"]
            actual_audio_control_text = self.fc.fd["home"].get_audio_control_text()
            assert actual_audio_control_text == expected_audio_control_text, "Audio control text is not matched"
        # configure to optimize audio
            expected_configure_text = lang_settings["actions"]["audioControl"]["description4"]
            actual_configure_text = self.fc.fd["home"].get_configure_to_optimize_audio_text()
            assert actual_configure_text == expected_configure_text, "Configure to optimize audio text is not matched"
        else:
            logging.info("audio card not available")
            # Support control
        if bool(self.fc.fd["home"].verify_support_card_visible()) is True:
            expected_support_text = lang_settings["actions"]["support"]["title"]
            actual_support_text = self.fc.fd["home"].verify_support_card_title()
            assert actual_support_text == expected_support_text, "Support text is not matched"
            expected_sub_text = lang_settings["actions"]["support"]["description4"]
            actual_sub_text = self.fc.fd["home"].verify_support_detail_page_title()
            assert actual_sub_text == expected_sub_text, "Support sub text is not matched"
        else:
            logging.info("Support Control card not available")
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.fd["devices"].restore_app()
