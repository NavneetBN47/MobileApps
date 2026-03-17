import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA, HOME_TILES
from MobileApps.resources.const.web.const import WEBVIEW_URL

pytest.app_info = "SMART"


class Test_Suite_01_Ios_Compose_Fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.personalize = cls.fc.fd["personalize"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.fax_history = cls.fc.fd["softfax_fax_history"]
        cls.fax_welcome = cls.fc.fd["softfax_welcome"]
        cls.preview = cls.fc.fd["preview"]
        cls.recipient_info = cls.fc.recipient_info_for_os()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.name = 'savedraft' + cls.fc.get_random_str()
        cls.fc.go_home(stack=cls.stack, create_account=True)
        cls.fc.nav_to_compose_fax(new_user=True)

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.nav_to_compose_fax()

    def test_01_compose_new_fax_from_fax_history_sent(self):
        """
        Compose new fax from fax history sent screen and compose fax 3 dot menu options - C16028354, C31379700, C31379702
        """
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.click_compose_new_fax()
        assert self.compose_fax.verify_compose_fax_screen(raise_e=False) is not False
        assert self.compose_fax.verify_3_dots_menu_options() is True
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_CLEAR_FIELDS_BTN)

    def test_02_go_home_from_compose_fax(self):
        """
        Verify navigation to "Home" from bottom options of the three vertical dots on compose fax screen
        - C24628889, C31379873, C31379703
        """
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_HOME_BTN)
        self.fc.fd["home"].verify_home_tile()

    def test_03_verify_clear_all_fields(self):
        """
        Enter Recipient, sender information and add a file, select clear all fields and verify
        all fields cleared - C31379871, C31379704
        """
        self.enter_fax_details_and_select_menu_options("save_as_draft_popup_exit_bn", self.compose_fax.MENU_CLEAR_FIELDS_BTN, add_file=True)
        phone, name, code = self.compose_fax.get_recipient_information()
        assert (phone == "" and name == ""), "Recipient phone number is not empty"
        sender_phone, sender_name = self.compose_fax.get_sender_information()
        assert (sender_phone == "" and sender_name == ""), "Sender phone number is not empty"
        assert self.compose_fax.verify_file_added() is False

    def test_04_verify_save_as_draft_and_delete_confirmation(self):
        """
        Enter Recipient, sender information, select clear all fields,
        select "Save as Draft" on popup and verify the Draft history - C31379705
        """
        self.enter_fax_details_and_select_menu_options("save_as_draft_popup_save_draft_btn", self.compose_fax.MENU_HOME_BTN)
        self.fc.fd["home"].verify_home()
        self.home.select_tile_by_name(HOME_TILES.TILE_MOBILE_FAX)
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=10)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_tab(self.fax_history.DRAFT_TAB)
        self.fax_history.verify_draft_fax_history_list(phone_number=self.recipient_info["phone"])
        self.fax_history.open_record_menu_for_ios(self.recipient_info["phone"])
        self.fax_history.click_record_delete_btn()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()

    def test_05_verify_cancel_save_as_draft_from_pop_up(self):
        """
        Enter Recipient, sender information, select clear all fields,
        select "Cancel" on popup and verify for the fields to remain the same - C31379707
        """
        self.enter_fax_details_and_select_menu_options("save_as_draft_popup_cancel_btn", self.compose_fax.MENU_HOME_BTN)
        self.compose_fax.verify_compose_fax_screen()
        phone, name, code = self.compose_fax.get_recipient_information()
        assert (phone == self.recipient_info["phone"]), "Recipient phone number is not preserved"
        sender_phone, sender_name = self.compose_fax.get_sender_information()
        assert (sender_phone == self.sender_info["phone"] and sender_name == self.sender_info["name"]), "Sender phone number is not preserved"
        assert self.compose_fax.verify_file_added() is False

    def test_06_verify_exit_save_as_draft_from_pop_up(self):
        """
        Enter Recipient, sender information, select clear all fields,
        select "Exit" on popup and verify for an empty Draft history - C31379874, C31379706
        """
        phone = "343-345-3234"
        self.enter_fax_details_and_select_menu_options("save_as_draft_popup_exit_bn", self.compose_fax.MENU_HOME_BTN, recipient_phone=phone)
        self.fc.fd["home"].verify_home()
        self.home.select_tile_by_name(HOME_TILES.TILE_MOBILE_FAX)
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=10)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_tab(self.fax_history.DRAFT_TAB)
        assert self.fax_history.verify_draft_fax_history_list(is_empty=True, raise_e=False)

    def enter_fax_details_and_select_menu_options(self, option, button_to_click, recipient_phone="", add_file=False):
        self.compose_fax.verify_compose_fax_screen()
        if not recipient_phone:
            recipient_phone = self.recipient_info["phone"]
        self.compose_fax.enter_recipient_information(recipient_phone)
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_recipient_dropdown()
        if add_file:
            self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
            self.fc.select_photo_from_photo_picker(select_all_files = False)
            self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
            self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
            sleep(5)
            self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_menu_option_btn(btn_name=button_to_click, popup_action=option)