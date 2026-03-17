import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "SMART"

class Test_Suite_13_sender_profiles(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.preview = cls.fc.fd["preview"]
        cls.contacts = cls.fc.fd["softfax_contacts"]
        cls.fax_settings = cls.fc.fd["fax_settings"]
        cls.recipient_info = cls.fc.recipient_info_for_os()
        cls.phone, cls.name = cls.recipient_info["phone"], 'test' + cls.fc.get_random_str()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.fc.go_home(stack=cls.stack, button_index=2)
        cls.email, cls.password = cls.fc.create_account_from_homepage()
        cls.fc.nav_to_compose_fax(new_user=True)
        cls.fc.nav_to_fax_settings_screen(fax_settings_option=cls.fax_settings.SEND_PROFILES_OPT, stack=cls.stack)
        cls.profile_name = 'test' + cls.fc.get_random_str()
        cls.profile_name2 = 'test2' + cls.fc.get_random_str()

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        if not self.fax_settings.verify_sender_profile_screen_title():
            self.fc.nav_to_fax_settings_screen(fax_settings_option=self.fax_settings.SEND_PROFILES_OPT, stack=self.stack)

    def test_01_empty_sender_profile_screen(self):
        """
        Navigate to Sender Profiles screen and verify empty contacts screen - C25367428
        """
        self.fax_settings.verify_sender_profiles_screen(is_empty=True)

    def test_02_create_and_verify_sender_profile_screen(self):
        """
        Verify Create Sender Profiles screen and Sender Profile screen with contacts - C25367429, C25367430, C27099543
        """
        self.fax_settings.verify_sender_profiles_screen(is_empty=True)
        self.add_sender_profile(self.profile_name)
        self.fax_settings.verify_sender_profiles_screen()
        assert self.fax_settings.verify_sender_profile_list(self.profile_name) is not False
        self.fax_settings.verify_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_SELECT_BTN)

    def test_03_verify_save_with_no_info(self):
        """
        Verify Add Sender Profile Save button with no info - C25367431
        """
        self.fax_settings.verify_sender_profiles_screen()
        self.fax_settings.click_create_a_new_sender_profile_btn()
        self.fax_settings.verify_new_sender_profile_screen()
        assert self.fax_settings.verify_profile_save_btn_enabled() is False
        self.fax_settings.click_save_btn()
        self.fax_settings.verify_new_sender_profile_screen()

    def test_04_verify_sender_profile_edit_screen(self):
        """
        Verify Edit Sender Profile screen elements - C25367432
        Verify Cancel on Edit Sender Profile screen with no contact selected - C25367433
        """
        self.add_sender_profile(self.profile_name)
        self.add_sender_profile(self.profile_name2)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_SELECT_BTN)
        self.fax_settings.verify_sender_profiles_edit_screen()
        self.fax_settings.verify_edit_sender_profile_radio_btn()
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_CANCEL_BTN)
        self.fax_settings.verify_sender_profile_screen_title()
        assert self.fax_settings.verify_sender_profile_list(self.profile_name, raise_e=False) is not False
        assert self.fax_settings.verify_sender_profile_list(self.profile_name2, raise_e=False) is not False

    def test_05_verify_cancel_on_sender_profiles(self):
        """
        Verify Cancel on Edit Sender Profile screen closes edit screen and
        nav back to Sender Profile screen with contacts intact - C25367434
        """
        self.add_sender_profile(self.profile_name)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_SELECT_BTN)
        self.fax_settings.verify_sender_profiles_edit_screen()
        self.fax_settings.select_single_sender_profiles(self.profile_name)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_CANCEL_BTN)
        self.fax_settings.verify_sender_profile_screen_title()
        assert self.fax_settings.verify_sender_profile_list(self.profile_name, raise_e=False) is not False

    @pytest.mark.parametrize('delete_action', ['cancel','delete'])
    def test_06_verify_delete_on_sender_profiles(self, delete_action):
        """
        Verify Delete Popup, Delete and Cancel btn functionality on Edit Sender Profile screen - C25367436
        """
        self.add_sender_profile(self.profile_name)
        self.add_sender_profile(self.profile_name2)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_SELECT_BTN)
        self.fax_settings.verify_sender_profiles_edit_screen()
        self.fax_settings.select_single_sender_profiles(self.profile_name2)
        self.fax_settings.click_sender_profiles_delete_btn(is_edited=False)
        if delete_action == 'cancel':
            self.verify_cancel_on_delete_popup(is_edited=False)
            self.fax_settings.verify_sender_profiles_edit_screen() 
            assert self.fax_settings.verify_sender_profile_list(self.profile_name2, raise_e=False) is not False
        else:
            self.verify_delete_on_delete_popup(is_edited=False)
            self.fax_settings.click_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_SELECT_BTN)
            self.fax_settings.verify_sender_profiles_edit_screen()
            assert self.fax_settings.verify_sender_profile_list(self.profile_name2, raise_e=False) is False
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_CANCEL_BTN)

    @pytest.mark.parametrize('delete_action', ['cancel', 'delete'])
    def test_07_verify_cancel_delete_on_edit_sender_profile(self, delete_action):
        """
        Verify Delete Popup, Delete and Cancel btn functionality on Sender Profile Edit screen - C25367435, C25367434, C27099542
        """
        self.add_sender_profile(self.profile_name2)
        self.fax_settings.select_single_sender_profiles(self.profile_name2)
        self.fax_settings.verify_edit_sender_profile_screen()
        if delete_action == 'cancel':
            self.verify_cancel_on_delete_popup()
            self.fax_settings.verify_edit_sender_profile_screen()
            self.fax_settings.click_back()
            self.fax_settings.verify_sender_profile_screen_title()
            assert self.fax_settings.verify_sender_profile_list(self.profile_name2, raise_e=False) is not False
        else:
            self.verify_delete_on_delete_popup()
            assert self.fax_settings.verify_sender_profile_list(self.profile_name2, raise_e=False) is False

    def add_sender_profile(self, profile_name):
        if self.fax_settings.verify_sender_profile_list(profile_name, raise_e=False) is False:
            self.fax_settings.verify_sender_profiles_screen()
            self.fax_settings.click_create_a_new_sender_profile_btn()
            self.fax_settings.add_edit_sender_profile_page(profile_name, self.sender_info["name"],
                                                           self.sender_info["phone"], is_new=True)
            self.fax_settings.verify_sender_profile_list(profile_name)

    def verify_cancel_on_delete_popup(self, is_edited=True):
        self.fax_settings.click_sender_profiles_delete_btn(is_edited=is_edited)
        self.fax_settings.verify_cover_page_delete_popup()
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)

    def verify_delete_on_delete_popup(self, is_edited=True):
        self.fax_settings.click_sender_profiles_delete_btn(is_edited=is_edited)
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
        self.fax_settings.verify_sender_profile_screen_title()