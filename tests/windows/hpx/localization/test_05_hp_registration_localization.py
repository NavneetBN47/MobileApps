import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
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

@pytest.fixture(scope="session", params=["hp_registraion_screenshot"])
def screenshot_folder_name(request):
    return request.param


class Test_Suite_Localization(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.attachment_path = conftest_misc.get_attachment_folder()

    # HP Registration Page
    def test_01_HP_Registration_module_C33369573(self, language, publish_hpx_localization_screenshot, screenshot_folder_name):
        lang_settings = ma_misc.load_json_file("resources/test_data/hpx/hpregistration.json")[language]["translation"]["registration"]
        self.fc.uninstall_app()
        self.fc.install_app(self.driver.session_data["installer_path"])
        time.sleep(30)
        self.fc.update_properties(language)
        self.fc.launch_app()
        time.sleep(5)
        self.fc.launch_app()

        if self.fc.fd["hp_privacy_setting"].verify_manage_options_show():
            self.fc.fd["hp_privacy_setting"].click_decline_all_button()
        
        if self.fc.fd["hp_registration"].verify_hpone_page_show():
            self.fc.maximize_window()            
            self.fc.fd["hp_registration"].click_hpone_page_skip_btn()

        # Registration
        actual_registration_header_text = self.fc.fd["hp_registration"].verify_header_text()
        expected_registation_header_text = lang_settings["subHeader"]["title"]
        ma_misc.create_localization_screenshot_folder("hp_registraion_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "hp_registraion_screenshot/{}_hp_registraion.png".format(language))
        assert actual_registration_header_text == expected_registation_header_text, "Registration header text is not matched"

        # Register your PC for faster warranty support
        actual_subtitle_text = self.fc.fd["hp_registration"].check_localization_sub_title()
        expected_subtitle_text = lang_settings["header"]["title"]
        assert actual_subtitle_text == expected_subtitle_text, "Subtitle text is not matched"

        # First Name
        actual_firstname_text = self.fc.fd["hp_registration"].check_localization_firstname_text()
        expected_firstname_text = lang_settings["firstNameLabel"]["title"]
        assert actual_firstname_text == expected_firstname_text, "First name text is not matched"

        # Last Name
        actual_lastname_text = self.fc.fd["hp_registration"].check_localization_lastname_text()
        expected_lastname_text = lang_settings["lastNameLabel"]["title"]
        assert actual_lastname_text == expected_lastname_text, "Last name text is not matched"

        # Email Address
        actual_email_text = self.fc.fd["hp_registration"].check_localization_email_text()
        expected_email_text = lang_settings["emailLabel"]["title"]
        assert actual_email_text == expected_email_text, "Email text is not matched"

        # Country
        actual_country_text = self.fc.fd["hp_registration"].check_localization_country()
        expected_country_text = lang_settings["dropdownmenu"]["title"]
        assert actual_country_text == expected_country_text, "Country text is not matched"
        
        # By registering you consent to the following...
        actual_privacy_link = self.fc.fd["hp_registration"].verify_localization_privacy_statement()
        expected_privacy_link = lang_settings["footer"]["text"]
        assert actual_privacy_link == expected_privacy_link, "Privacy link text is not matched"

        # Register
        actual_register_button_text = self.fc.fd["hp_registration"].verify_localization_register_button()
        expected_register_button_text = lang_settings["register"]["title"]
        assert actual_register_button_text == expected_register_button_text, "Register button text is not matched"

        # Skip this step
        actual_skip_button_text = self.fc.fd["hp_registration"].verify_localization_skip_button()
        expected_skip_button_text = lang_settings["skipStep"]
        assert actual_skip_button_text == expected_skip_button_text, "Skip this step text is not matched"

        # A valid first name is required.
        self.fc.fd["hp_registration"].enter_invalid_first_name()
        actual_invalid_first_name = self.fc.fd["hp_registration"].check_localization_invalid_first_name()
        expected_invalid_first_name = lang_settings["validFirstNameError"]["text"]

        # A valid last name is required.
        self.fc.fd["hp_registration"].enter_invalid_last_name()
        actual_invalid_first_name = self.fc.fd["hp_registration"].check_localization_invalid_last_name()
        expected_invalid_first_name = lang_settings["validLastNameError"]["text"]

        # A valid email is required.
        self.fc.fd["hp_registration"].enter_invalid_email()
        actual_invalid_first_name = self.fc.fd["hp_registration"].check_localization_invalid_email()
        expected_invalid_first_name = lang_settings["validEmailError"]["text"]
