import pytest
from selenium.webdriver.support.ui import WebDriverWait
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA, HOME_TILES

pytest.app_info = "SMART"

class Test_Suite_14_Ios_Compose_Fax_From_Settings(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.fax_history = cls.fc.fd["softfax_fax_history"]        
        cls.fax_settings = cls.fc.fd["fax_settings"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.preview = cls.fc.fd["preview"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_03"]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=1)
        self.fc.add_mobile_fax_tile()
        self.home.select_tile_by_name(HOME_TILES.TILE_MOBILE_FAX)
        self.fax_history.handle_fax_feature_update_popup(raise_e=False)

    def test_01_load_compose_fax_by_using_fax_settings(self):
        """
        C31379816
        Mobile Fax Account
        You are currently signed in as
        Current Plan:
        Sending
        Cover pages
        Sender Profile
        Contacts
        About Mobile Fax
        Terms of Service
        Business Associate Agreement
        Version:
        C31379817

        1.Tap on Mobile Fax tile and navigate to "Compose Fax" page
        2.Tap on Three vertical dots from top right corner of the screen and tap on "Fax Settings" option
        3.Tap on Three vertical dots from top right corner of the "Mobile Fax Settings"
        4.Tap on "Compose New Fax"
        Verify
        User should re-directed to the Compose Fax screen
        """
        self.fax_history.click_compose_new_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN, "save_as_draft_popup_exit_bn")
        self.fax_settings.verify_fax_settings_screen() #C31379816
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_COMPOSE_NEW_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()

    def test_02_load_fax_history(self):
        """
        C31379818
        1.Tap on Mobile Fax tile and navigate to "Compose Fax" page
        2.Tap on Three vertical dots from top right corner of the screen and tap on "Fax Settings" option
        3.Tap on Three vertical dots from top right corner of the "Mobile Fax Settings"
        4.Tap on Fax History
        Verify
        User should Navigate to "Fax History" page
        """
        self.fax_history.click_compose_new_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN, "save_as_draft_popup_exit_bn")
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()

    def test_03_navigate_to_home(self):
        """
        C31379819
        1.Tap on Mobile Fax tile and navigate to "Compose Fax" page
        2.Tap on Three vertical dots from top right corner of the screen and tap on "Fax Settings" option
        3.Tap on Three vertical dots from top right corner of the "Mobile Fax Settings"
        4.Tap on Home
        Verify
        User should navigate to Home Screen without any error
        """
        self.fax_history.click_compose_new_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN, "save_as_draft_popup_exit_bn")
        self.fax_settings.verify_fax_settings_screen()
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_HOME_BTN)
        self.home.verify_home()

    def test_04_export_log(self):
        """
        C31379820
        1. Freshly Install HP Smart with the latest build
        2. Launch Smart app
        3. Accept all the consents.
        4. Navigate to Home screen with user onboarding login
        5. Click on MOBILE Fax tile, and lead to Compose Fax screen
        6. Send a successful fax, check the confirmation and come back to the Compose Fax screen
        7. Click on More Option button -
        8. Tap on Three vertical dots on the top right corner.
        9. Select Fax History
        10. Tap on three vertical dots, and choose option "Select"
        11. Select any record from the sent tab under Fax history
        12. Tap on "Export Fax Log"
        13. Observe
        """
        self.fax_history.click_compose_new_fax()
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.fc.select_photo_from_photo_picker(select_all_files=False)
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_send_fax_native_btn()
        self.send_fax_details.verify_send_fax_status(timeout=360, is_successful=True, check_sending=False)
        self.send_fax_details.click_back()

        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN, "save_as_draft_popup_exit_bn")
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_FAX_HISTORY_BTN)
        self.fax_history.load_edit_screen()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"])
        self.fax_history.click_edit_export_fax_log()
        self.preview.verify_preview_screen_title()

    def test_05_load_terms_of_service(self):
        """
        C31379853
        1.Tap on Mobile Fax tile and navigate to "Compose Fax" page
        2.Tap on Three vertical dots from top right corner of the screen and tap on "Fax Settings" option
        3.Tap on "Terms of Service" option
        Verify Terms of service PDF should open for IOS device.
        """
        if '15' in self.driver.driver_info['platformVersion']:
            pytest.skip("Unusual behavior detected on page source")
        self.fax_history.click_compose_new_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN, "save_as_draft_popup_exit_bn")
        self.fax_settings.click_terms_of_services_btn()
        assert WebDriverWait(self.driver.wdvr, 20).until(lambda x: x.query_app_state("com.apple.mobilesafari") == 4)

    def test_06_load_business_associate_agreement(self):
        """
        C31379854
        1.Tap on Mobile Fax tile and navigate to "Compose Fax" page
        2.Tap on Three vertical dots from top right corner of the screen and tap on "Fax Settings" option
        3.Tap on "Business Associate Agreement"
        Verify  "Business Associate Agreement"  PDF should open for IOS device.
        """
        if '15' in self.driver.driver_info['platformVersion']:
            pytest.skip("Unusual behavior detected on page source")
        self.fax_history.click_compose_new_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN, "save_as_draft_popup_exit_bn")
        self.fax_settings.click_business_associate_agreement_btn()
        assert WebDriverWait(self.driver.wdvr, 20).until(lambda x: x.query_app_state("com.apple.mobilesafari") == 4)
