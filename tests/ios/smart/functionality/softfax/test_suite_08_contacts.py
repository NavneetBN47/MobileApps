import pytest
from selenium.common.exceptions import TimeoutException
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_08_Contacts(object):

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
        cls.fc.go_home(stack=cls.stack, button_index=2)
        cls.email, cls.password = cls.fc.create_account_from_homepage()
        cls.fc.nav_to_compose_fax(new_user=True)

    def test_01_verify_empty_contacts_screen(self):
        """
        Navigate to saved contacts screen and verify contacts screen with no contacts - C24829085
        """
        self.fc.nav_to_contacts_screen()
        assert self.contacts.verify_empty_contact_list(is_saved=False, raise_e=False) is not False
        assert self.contacts.verify_add_btn() is not False
        self.contacts.click_tab_btn_native(self.contacts.SAVED_TAB_BTN)
        assert self.contacts.verify_empty_contact_list(raise_e=False) is not False
        assert self.contacts.verify_add_btn() is not False

    def test_02_verify_contacts_screen_with_no_contacts(self):
        """
        Navigate to contacts screen from fax settings and verify ui with no contacts - C25410922
        """
        self.fc.nav_to_fax_settings_screen(fax_settings_option=self.fax_settings.CONTACTS_OPT, stack=self.stack)
        self.fax_settings.verify_contact_screen()
        assert self.fax_settings.verify_empty_contact_screen(raise_e=False) is not False

    def test_03_add_and_verify_contact_screen(self):
        """
        Verify add contacts screen ui elements, add contact and verify contact screen ui with contacts added
            C25410923, C25410924, C25410925
        """
        code, phone, name = self.add_contact(self.phone, self.name)
        self.fax_settings.verify_contact_screen(select=True)
        assert self.contacts.verify_contact(phone_number=phone, contact_name=name) is True

    def test_04_verify_cancel_when_no_contact_selected(self):
        """
        Verify contact edit cancel when no contact selected - C25410927
        """
        code, phone, name = self.add_contact(self.phone, self.name)
        self.fax_settings.verify_contact_screen(select=True)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.CONTACT_SELECT_BTN)
        self.fax_settings.verify_contact_edit_screen()
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.CONTACT_CANCEL_BTN)
        self.fax_settings.verify_contact_screen()
        assert self.contacts.verify_contact(phone_number=phone, contact_name=name) is True

    def test_05_verify_edit_cancel_when_contact_selected(self):
        """
        Verify edit screen select, Cancel and Delete button and click cancel when contact selected
        C25410926, C25410929
        """
        code, phone, name = self.add_contact(self.phone, self.name)
        self.fax_settings.verify_contact_screen(select=True)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.CONTACT_SELECT_BTN)
        self.contacts.select_saved_contact(phone, name)
        self.fax_settings.verify_contact_edit_screen(delete_btn=True)
        self.fax_settings.click_contact_delete_btn()
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
        assert self.contacts.verify_contact(phone_number=phone, contact_name=name) is True
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.CONTACT_CANCEL_BTN)

    def test_06_verify_edit_saved_contact(self):
        """
        Select an already added contact and verify edit contact screen displays - C25410931
        """
        code, phone, name = self.add_contact(self.phone, self.name)
        self.fax_settings.verify_contact_screen(select=True)
        self.contacts.select_saved_contact(phone, name)
        self.contacts.verify_edit_contact_screen()

    def test_07_verify_delete_from_contact_edit_screen(self):
        """
        Verify Delete pop_up, cancel and delete options from contact edit screen -
        C25410933, C27212794, C27212795
        """
        code, phone, name = self.add_contact(self.phone, self.name)
        assert self.contacts.verify_contact(phone_number=phone, contact_name=name) is True
        code1, phone1, name1 = self.add_contact(self.phone, "second_contact")
        self.fax_settings.verify_contact_screen(select=True)
        self.contacts.select_saved_contact(phone1, name1)
        self.contacts.verify_edit_contact_screen()
        self.contacts.click_edit_contact_delete()
        self.contacts.verify_edit_delete_confirmation_popup()
        self.contacts.dismiss_edit_delete_confirmation_popup(is_deleted=False)
        self.contacts.verify_edit_contact_screen()
        self.contacts.click_edit_contact_delete()
        self.contacts.dismiss_edit_delete_confirmation_popup()
        assert self.contacts.verify_and_select_saved_contact(phone_number=phone1, contact_name=name1) is False

    def test_08_verify_delete_single_contact(self):
        """
        Verify Delete when user have only one saved contact - C25410934
        """
        code, phone, name = self.add_contact(self.phone, self.name)
        self.fax_settings.verify_contact_screen(select=True)
        self.contacts.select_saved_contact(phone, name)
        self.contacts.verify_edit_contact_screen()
        self.contacts.click_edit_contact_delete()
        self.contacts.dismiss_edit_delete_confirmation_popup()
        assert self.fax_settings.verify_empty_contact_screen(raise_e=False) is not False

    def add_contact(self, phone, name):
        if self.contacts.verify_contact_screen_title() is False:
            self.fc.nav_to_fax_settings_screen(fax_settings_option=self.fax_settings.CONTACTS_OPT, stack=self.stack)
            self.contacts.verify_contact_screen_title(raise_e=True)
        try:
            self.contacts.verify_contact(phone_number=phone, contact_name=name)
        except TimeoutException:
            self.fax_settings.click_add_a_contact_btn()
            return self.contacts.add_edit_contact(phone, name, is_new=True)
        return "1", phone, name