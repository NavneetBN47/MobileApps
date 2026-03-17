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

@pytest.fixture(scope="session", params=["programmable_key_screenshot"])
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

    def test_09_hppk_module_C33053785(self, language):
        soft_assertion = SoftAssert()
        lang_settings = self.fc.processing_localization_language("resources/test_data/hpx/programmablekeyLocalization.json", language, "progKey")
        self.fc.myhp_login_startup_for_localization_scripts(language)
        assert bool(self.fc.fd["devices"].verify_HPPK_card_visible()) is True, "HPPK card not available."
        logging.info("HPPK module available")
        self.fc.fd["devices"].click_prog_key_card()
        #programmable key
        expected_prog_key_text=lang_settings["functionLibrary"]["programmableKey"]
        actual_prog_key_text=self.fc.fd["hppk"].get_prog_key_nav_text()
        ma_misc.create_localization_screenshot_folder("programmable_key_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_homepage.png".format(language))
        soft_assertion.assert_equal(actual_prog_key_text, expected_prog_key_text, f"Programmable key text is not matching, expected string text is {expected_prog_key_text}, but got {actual_prog_key_text}. ")
        #Create personalized shortcuts with the press of a button
        expected_personalized_text=lang_settings["personalizedShorcuts"]
        actual_personalized_text=self.fc.fd["hppk"].verify_programmable_key_heading()
        soft_assertion.assert_equal(actual_personalized_text, expected_personalized_text, f"Create personalized short cut text is not matching, expected string text is {expected_personalized_text}, but got {actual_personalized_text}. ")
        #Automation
        expected_automation_text=lang_settings["automationText"]
        actual_automation_text=self.fc.fd["hppk"].get_automation_text()
        soft_assertion.assert_equal(actual_automation_text, expected_automation_text, f"Automation text is not matching, expected string text is {expected_automation_text}, but got {actual_automation_text}. ")
        #Key sequence
        expected_key_sequence_text=lang_settings["keysequenceText"]
        actual_key_sequence_text=self.fc.fd["hppk"].get_key_sequence_text()
        soft_assertion.assert_equal(actual_key_sequence_text, expected_key_sequence_text, f"Key sequence text is not matching, expected string text is {expected_key_sequence_text}, but got {actual_key_sequence_text}. ")
        #Text input
        expected_text_input_text=lang_settings["textInputText"]
        actual_text_input_text=self.fc.fd["hppk"].get_text_input_text()
        soft_assertion.assert_equal(actual_text_input_text, expected_text_input_text, f"Text input text is not matching, expected string text is {expected_text_input_text}, but got {actual_text_input_text}. ")
        #click on Automation option
        self.fc.fd["hppk"].click_automation_radio_btn()
        #Assign apps, websites, files or folders to open for your shortcut
        expected_assign_apps_text=lang_settings["automateShortcutDescription"]
        actual_assign_apps_text=self.fc.fd["hppk"].get_assign_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_Automation.png".format(language))
        soft_assertion.assert_equal(actual_assign_apps_text, expected_assign_apps_text, f"Assign apps text is not matching, expected string text is {expected_assign_apps_text}, but got {actual_assign_apps_text}. ")
        #click Add action drop down
        self.fc.fd["hppk"].click_add_action()
        #Add action....
        expected_add_action_text=lang_settings["addAction"]
        actual_add_action_text=self.fc.fd["hppk"].get_add_action_text_in_list()
        logging.info("actual_add_action_text after click automation: {}".format(actual_add_action_text))
        
        if language == "sv-SE":
            actual_add_action_text = actual_add_action_text.replace(" ..."," ...")
        logging.info("actual_action_text: {}".format(actual_add_action_text))
        logging.info("expected_action_text: {}".format(expected_add_action_text))
        soft_assertion.assert_equal(actual_add_action_text, expected_add_action_text, f"Add action text is not matching, expected string text is {expected_add_action_text}, but got {actual_add_action_text}. ")
        
        #Application
        expected_application_text=lang_settings["automatePagePickerItems"]["application"]
        actual_application_text=self.fc.fd["hppk"].get_application_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_add_action.png".format(language))
        soft_assertion.assert_equal(actual_application_text, expected_application_text, f"Application text is not matching, expected string text is {expected_application_text}, but got {actual_application_text}. ")
        self.fc.fd["hppk"].click_application()
        time.sleep(10)
        #Application window elements
        expected_app_text=lang_settings["LaunchApplication"]["applications"]
        actual_app_text=self.fc.fd["hppk"].get_app_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_application_window.png".format(language))
        soft_assertion.assert_equal(actual_app_text, expected_app_text, f"Applications window text is not matching, expected string text is {expected_app_text}, but got {actual_app_text}. ")
        #search application
        expected_search_text=lang_settings["LaunchApplication"]["searchApplication"]
        actual_search_text=self.fc.fd["hppk"].get_search_text()
        soft_assertion.assert_equal(actual_search_text, expected_search_text, f"Search application text is not matching, expected string text is {expected_search_text}, but got {actual_search_text}. ")
        #cancel
        expected_cancel_text=lang_settings["LaunchWebsite"]["cancel"]
        actual_cancel_text=self.fc.fd["hppk"].get_cancel_text()
        soft_assertion.assert_equal(actual_cancel_text, expected_cancel_text, f"Cancel text is not matching, expected string text is {expected_cancel_text}, but got {actual_cancel_text}. ")
        #add
        expected_add_text=lang_settings["LaunchWebsite"]["add"]
        #select app from all list then click add btn
        self.fc.fd["hppk"].click_msaccess_app_applist()
        actual_add_text=self.fc.fd["hppk"].get_add_app_text()
        soft_assertion.assert_equal(actual_add_text, expected_add_text, f"Add text is not matching, expected string text is {expected_add_text}, but got {actual_add_text}. ")
        self.fc.fd["hppk"].click_cancel_app_button()
        self.fc.fd["hppk"].click_add_action()
        #website window elements
        #website
        expected_website_text=lang_settings["automatePagePickerItems"]["website"]
        actual_website_text=self.fc.fd["hppk"].get_website_text()
        soft_assertion.assert_equal(actual_website_text, expected_website_text, f"Website text is not matching, expected string text is {expected_website_text}, but got {actual_website_text}. ")
        self.fc.fd["hppk"].click_website()
        time.sleep(1)
        #website tile text
        expected_website_header_text=lang_settings["LaunchWebsite"]["header"]
        actual_website_header_text=self.fc.fd["hppk"].get_website_header()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_website_window.png".format(language))
        soft_assertion.assert_equal(actual_website_header_text, expected_website_header_text, f"Website title text is not matching, expected string text is {expected_website_header_text}, but got {actual_website_header_text}. ")
        #website description
        expected_website_description_text=lang_settings["LaunchWebsite"]["description"]
        actual_website_description_text=self.fc.fd["hppk"].get_website_description_text()
        soft_assertion.assert_equal(actual_website_description_text, expected_website_description_text, f"Website description text is not matching, expected string text is {expected_website_description_text}, but got {actual_website_description_text}. ")
        #website text box
        expected_website_textbox_text=lang_settings["LaunchWebsite"]["header"]
        actual_website_textbox_text=self.fc.fd["hppk"].get_textbox_text()
        soft_assertion.assert_equal(actual_website_textbox_text, expected_website_textbox_text, f"Website textbox text is not matching, expected string text is {expected_website_textbox_text}, but got {actual_website_textbox_text}. ")
        #enter invalid entry in website text box
        self.fc.fd["hppk"].input_url("efgt")
        expected_error_msg=lang_settings["LaunchWebsite"]["errorText"]
        actual_error_msg=self.fc.fd["hppk"].get_website_invalid_url_warning_text()
        soft_assertion.assert_equal(actual_error_msg, expected_error_msg, f"Error msg text is not matching, expected string text is {expected_error_msg}, but got {actual_error_msg}. ")
        #cancel
        expected_website_cancel_text=lang_settings["LaunchWebsite"]["cancel"]
        actual_website_cancel_text=self.fc.fd["hppk"].get_website_cancel_text()
        soft_assertion.assert_equal(actual_website_cancel_text, expected_website_cancel_text, f"Cancel text is not matching, expected string text is {expected_website_cancel_text}, but got {actual_website_cancel_text}. ")
        #add
        expected_website_add_text=lang_settings["LaunchWebsite"]["add"]
        self.fc.fd["hppk"].input_url("www.google.com")
        actual_website_add_text=self.fc.fd["hppk"].get_website_add_text()
        soft_assertion.assert_equal(actual_website_add_text, expected_website_add_text, f"Add text is not matching, expected string text is {expected_website_add_text}, but got {actual_website_add_text}. ")
        self.fc.fd["hppk"].click_website_cancel()
        self.fc.fd["hppk"].click_add_action()
        #File
        expected_file_text=lang_settings["automatePagePickerItems"]["file"]
        actual_file_text=self.fc.fd["hppk"].get_file_text()
        soft_assertion.assert_equal(actual_file_text, expected_file_text, f"File text is not matching, expected string text is {expected_file_text}, but got {actual_file_text}. ")
        #Folder
        expected_folder_text=lang_settings["automatePagePickerItems"]["folder"]
        actual_folder_text=self.fc.fd["hppk"].get_folder_text()
        soft_assertion.assert_equal(actual_folder_text, expected_folder_text, f"Folder text is not matching, expected string text is {expected_folder_text}, but got {actual_folder_text}. ")
        #click add action drop down
        self.fc.fd["hppk"].click_add_action()
        #--------------------------key sequence--------------------------------
        #click on key sequence option
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        #Add action....
        expected_add_action_text=lang_settings["addAction"]
        actual_add_action_text=self.fc.fd["hppk"].get_add_action_text_in_key_sequence()
        logging.info("actual_add_action_text after click key sequence: {}".format(actual_add_action_text))
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_add_action.png".format(language))
        if language == "sv-SE":
            actual_add_action_text = actual_add_action_text.replace(" ..."," ...")
        logging.info("actual_action_text: {}".format(actual_add_action_text))
        logging.info("expected_action_text: {}".format(expected_add_action_text))
        soft_assertion.assert_equal(actual_add_action_text, expected_add_action_text, f"add action text is not matching, expected string text is {expected_add_action_text}, but got {actual_add_action_text}. ")
        
        if bool(self.fc.fd["hppk"].verify_key_sequence_close_button()) is True:
            #click 'x' btn on key sequence
            self.fc.fd["hppk"].click_key_sequence_close_button()
        #enter some text in key sequence text box
        self.fc.fd["hppk"].enter_keys_in_key_sequence_textbox("d")
        #Save
        expected_save_text_key_sequence=lang_settings["Save"]
        actual_save_text_key_sequence=self.fc.fd["hppk"].get_save_text_key_sequence()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_save.png".format(language))
        soft_assertion.assert_equal(actual_save_text_key_sequence, expected_save_text_key_sequence, f"Save text is not matching, expected string text is {expected_save_text_key_sequence}, but got {actual_save_text_key_sequence}. ")
        #click save btn on key sequence
        self.fc.fd["hppk"].click_key_sequence_save_button()
        time.sleep(5)
        if bool(self.fc.fd["hppk"].verify_saved_text_key_sequence()) is True:
            #verify Saved! text
            expected_saved_text=lang_settings["saved"]
            actual_saved_text=self.fc.fd["hppk"].get_saved_text_key_sequence()
            self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_saved.png".format(language))
            soft_assertion.assert_equal(actual_saved_text, expected_saved_text, f"Saved text is not matching, expected string text is {expected_saved_text}, but got {actual_saved_text}. ")
        #click on text input option
        self.fc.fd["hppk"].click_text_input_radio_btn()
        #click on key sequence option
        self.fc.fd["hppk"].click_key_sequence_radio_btn()
        #enter some text in key sequence text box
        self.fc.fd["hppk"].enter_keys_in_key_sequence_textbox("d")
        #click save btn on key sequence
        self.fc.fd["hppk"].click_key_sequence_save_button()
        #verify every text in that popup
        assert bool(self.fc.fd["hppk"].verify_change_shortcut_modal_title()) is True, "Change shortcut modal title not available."
        #Change shortcut
        expected_change_shortcut_text=lang_settings["changeShortcut"]
        actual_change_shortcut_text=self.fc.fd["hppk"].get_change_shortcut_modal_title()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_change_shortcut.png".format(language))
        soft_assertion.assert_equal(actual_change_shortcut_text, expected_change_shortcut_text, f"Change shortcut text is not matching, expected string text is {expected_change_shortcut_text}, but got {actual_change_shortcut_text}. ")
        #subtitle(You are about to change the assigned shortcut for this key. Doing so will erase any previous shortcuts you assigned. Do you wish to continue?)
        expected_subtitle_text=lang_settings["changeShortcutPrompt"]
        actual_subtitle_text=self.fc.fd["hppk"].get_change_shortcut_modal_subtitle()
        soft_assertion.assert_equal(actual_subtitle_text, expected_subtitle_text, f"Subtitle text is not matching, expected string text is {expected_subtitle_text}, but got {actual_subtitle_text}. ")
        #Continue
        expected_continue_text=lang_settings["continue"]
        actual_continue_text=self.fc.fd["hppk"].get_continue_btn_modal()
        soft_assertion.assert_equal(actual_continue_text, expected_continue_text, f"Continue text is not matching, expected string text is {expected_continue_text}, but got {actual_continue_text}. ")
        #Cancel
        expected_cancel_text=lang_settings["LaunchWebsite"]["cancel"]
        actual_cancel_text=self.fc.fd["hppk"].get_cancel_btn_modal()
        soft_assertion.assert_equal(actual_cancel_text, expected_cancel_text, f"Cancel text is not matching, expected string text is {expected_cancel_text}, but got {actual_cancel_text}. ")
        #click cancel btn on modal
        self.fc.fd["hppk"].click_cancel_btn_modal()
    #------------------------------------------text input--------------------------------
        #click on text input option
        self.fc.fd["hppk"].click_text_input_radio_btn()
        #Add text...
        expected_add_text_text_input=lang_settings["enterTextPlaceholder"]
        actual_add_text_text_input=self.fc.fd["hppk"].get_add_text_in_text_input()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_add_text.png".format(language))
        soft_assertion.assert_equal(actual_add_text_text_input, expected_add_text_text_input, f"Add text text is not matching, expected string text is {expected_add_text_text_input}, but got {actual_add_text_text_input}. ")
        #characters lefts
        expected_char_left_text=lang_settings["enterTextInputInfo"]
        char_left_text=self.fc.fd["hppk"].get_char_left_text()
        logging.info("char = " +self.fc.fd["hppk"].filter_char_left_text(char_left_text))
        actual_char_left_text=self.fc.fd["hppk"].filter_char_left_text(char_left_text)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_char_left.png".format(language))
        soft_assertion.assert_equal(actual_char_left_text, expected_char_left_text, f"Characters left text is not matching, expected string text is {expected_char_left_text}, but got {actual_char_left_text}. ")
        
        #enter characters in text box
        self.fc.fd["hppk"].enter_char_in_text_input("enter some text")
        #Save
        expected_save_text_input=lang_settings["Save"]
        actual_save_text=self.fc.fd["hppk"].get_save_in_text_input()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_save.png".format(language))
        soft_assertion.assert_equal(actual_save_text, expected_save_text_input, f"Save text is not matching, expected string text is {expected_save_text_input}, but got {actual_save_text}. ")
        
        #click save on text input
        self.fc.fd["hppk"].click_text_input_save_button()
        
        #verify change shortcut popup
        assert bool(self.fc.fd["hppk"].verify_change_shortcut_modal_title()) is True, "Change shortcut modal title not available."
        #Change shortcut
        expected_change_shortcut_text=lang_settings["changeShortcut"]
        actual_change_shortcut_text=self.fc.fd["hppk"].get_change_shortcut_modal_title()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_change_shortcut.png".format(language))
        soft_assertion.assert_equal(actual_change_shortcut_text, expected_change_shortcut_text, f"Change shortcut text is not matching, expected string text is {expected_change_shortcut_text}, but got {actual_change_shortcut_text}. ")
        #subtitle(You are about to change the assigned shortcut for this key. Doing so will erase any previous shortcuts you assigned. Do you wish to continue?)
        expected_subtitle_text=lang_settings["changeShortcutPrompt"]
        actual_subtitle_text=self.fc.fd["hppk"].get_change_shortcut_modal_subtitle()
        soft_assertion.assert_equal(actual_subtitle_text, expected_subtitle_text, f"Subtitle text is not matching, expected string text is {expected_subtitle_text}, but got {actual_subtitle_text}. ")
        #Continue
        expected_continue_text=lang_settings["continue"]
        actual_continue_text=self.fc.fd["hppk"].get_continue_btn_modal()
        soft_assertion.assert_equal(actual_continue_text, expected_continue_text, f"Continue text is not matching, expected string text is {expected_continue_text}, but got {actual_continue_text}. ")
        #Cancel
        expected_cancel_text=lang_settings["LaunchWebsite"]["cancel"]
        actual_cancel_text=self.fc.fd["hppk"].get_cancel_btn_modal()
        soft_assertion.assert_equal(actual_cancel_text, expected_cancel_text, f"Cancel text is not matching, expected string text is {expected_cancel_text}, but got {actual_cancel_text}. ")
        #click cancel btn on modal
        self.fc.fd["hppk"].click_cancel_btn_modal()
        #click on doted image 
        self.fc.fd["hppk"].click_myhp_image()
        #my programmable keys
        expected_my_prog_key_text=lang_settings["myHPProgrammableKeyText"]
        actual_my_prog_key_text=self.fc.fd["hppk"].get_my_programmable_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_my_programmable_keys.png".format(language))
        soft_assertion.assert_equal(actual_my_prog_key_text, expected_my_prog_key_text, f"My programmable key text is not matching, expected string text is {expected_my_prog_key_text}, but got {actual_my_prog_key_text}. ")
        
        #click 2nd image on home page of HPPK module
        self.fc.fd["hppk"].click_supportkey_icon()
        #myHP Support
        expected_myhp_support_text=lang_settings["myHPSupportText"]
        actual_myhp_support_text=self.fc.fd["hppk"].get_my_support_key_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_my_hp_support.png".format(language))
        soft_assertion.assert_equal(actual_myhp_support_text, expected_myhp_support_text, f"MyHP Support text is not matching, expected string text is {expected_myhp_support_text}, but got {actual_myhp_support_text}. ")
        
        #click 3rd image on home page of HPPK module
        self.fc.fd["hppk"].click_pcpk_prog_key_image()
        #myHP PC Device
        expected_myhp_pc_device_text=lang_settings["myHPPCDeviceText"]
        actual_myhp_pc_device_text=self.fc.fd["hppk"].get_my_hp_pc_device_text()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "programmable_key_screenshot/{}_programmable_key_myhp_pc_device.png".format(language))
        soft_assertion.assert_equal(actual_myhp_pc_device_text, expected_myhp_pc_device_text, f"MyHP PC Device text is not matching, expected string text is {expected_myhp_pc_device_text}, but got {actual_myhp_pc_device_text}. ")
        
        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        soft_assertion.raise_assertion_errors()
