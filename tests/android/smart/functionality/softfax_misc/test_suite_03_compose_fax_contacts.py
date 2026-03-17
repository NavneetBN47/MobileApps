import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_03_Compose_Fax_Contacts(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.contacts = cls.fc.flow[FLOW_NAMES.SOFTFAX_CONTACTS]
        cls.send_fax_details = cls.fc.flow[FLOW_NAMES.SEND_FAX_DETAILS]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]

        # Define variables
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.recipient_phone = cls.fc.get_softfax_recipient_info()["phone"]
        cls.recipient_code = cls.fc.get_softfax_recipient_info()["code"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.smart_context = cls.fc.smart_context  

    def test_01_empty_contacts_list(self):
        """
        Description: C31379715, C31379711, C31379719
            1/ Load Contacts screen with creating new hpid
            2/ Click on each tab and verify
            3/ Click on Add button
            4/ Add new contact successfully
            5/ Click on Saved tab
            6/ Click on i icon of contact
            7/ Click on Delete button
            8/ Click on Cancel button

            9/ Click on Delete button
            10/ Click on Delete button
            11/ Click on Saved tab
            12/ Verify contact on Saved tab
        Expected Result:
            2/ Ech tab have empty list
            5/ Verify new contact on Saved list on Contacts screen.
            6/ Verify Edit Contact screen
                - Edit Contact title
                - Delete button
            7/ Verify Are you sure? popup
            8/ Verify Edit Contact screen
            11/ Verify Contact screen
            12/ Empty list on Contacts screen/Saved tab
        """
        # create a HPID account without any contacts
        self.__load_contacts_screen(check_onboarding=False)
        self.contacts.click_tab_btn(self.contacts.RECENT_TAB_BTN)
        self.contacts.verify_empty_contact_list(is_saved=False)
        self.contacts.click_tab_btn(self.contacts.SAVED_TAB_BTN)
        self.contacts.verify_empty_contact_list(is_saved=True)
        # Do cancel action on Contact delete popup screen
        self.__add_new_contact(self.recipient_phone, "test_01_{}".format(self.udid), self.recipient_code)
        self.__load_edit_contact_screen("{} {}".format(self.recipient_code, self.recipient_phone), "test_01_{}".format(self.udid))
        self.contacts.click_edit_contact_delete()
        self.contacts.verify_edit_delete_confirmation_popup()
        self.contacts.dismiss_edit_delete_confirmation_popup(is_deleted=False)
        self.contacts.verify_edit_contact_screen()
        # delete the contacts success
        self.contacts.click_edit_contact_delete()
        self.contacts.dismiss_edit_delete_confirmation_popup(is_deleted=True)
        self.contacts.verify_contacts_screen()
        self.contacts.click_tab_btn(self.contacts.SAVED_TAB_BTN)
        self.contacts.verify_contact(self.recipient_phone, "test_01_{}".format(self.udid), is_saved=True, invisible=True)

    def test_02_edit_saved_contact(self):
        """
        Description: C31379718, C31379720
            1/ Load Contacts screen with log in hpid
            2/ Add new contact
            3/ Click on i icon of contact
            4/ Changing name
        Expected Result:
            2/ New contact on Saved list on Contacts screen
            4/ Updated contact replace for old one
        """
        self.__load_contacts_screen()
        self.__add_new_contact(self.recipient_phone, "test_02_{}".format(self.udid), self.recipient_code)
        self.__load_edit_contact_screen("{} {}".format(self.recipient_code, self.recipient_phone), "test_02_{}".format(self.udid))
        self.contacts.add_edit_contact("(254) 572-5943", "{}_updated".format(self.udid), is_new=False)
        self.contacts.verify_contact(phone_number="(254) 572-5943", contact_name="{}_updated".format(self.udid), is_saved=True, invisible=False)
        self.contacts.verify_contact(self.recipient_phone, "test_02_{}".format(self.udid), is_saved=True, invisible=True)

    def test_03_send_fax_by_saved_contact(self):
        """
        Description: C31379713
            1/ Load Contacts screen with log in hpid
            2/ Add new contact
            3/ Select this contact for sending fax
            4/ enter valid sender information and adding a file
            5/ Click on Send Fax
        Expected Result:
            3/ Compose Fax screen display
            5/ Verify Send Fax Details screen
        """
        self.__load_contacts_screen()
        phone, contact_name = self.__add_new_contact(self.recipient_phone, "test_03_{}".format(self.udid), self.recipient_code)
        self.contacts.select_saved_contact(phone, contact_name)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_add_files_option_btn(self.compose_fax.CAMERA_BTN)
        self.fc.flow_camera_scan_capture_photo(chk_bottom_navbar=False)
        self.preview.verify_title(self.preview.PREVIEW_TITLE)
        self.preview.select_fax_next()
        # There are some test cases failed by No Such context issue, so add timeout for wait_for_context for fixing this issue
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.verify_uploaded_file(timeout=60)
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_send_fax()
        self.send_fax_details.verify_send_fax_detail_screen()

    def test_04_add_new_contact_with_invalid_formart(self):
        """
        Description:C31379716
            1. Load Contacts screen with log in hpid
            2. Click on Add button
            3. Input invalid fax number & name
        Expected Result:
            3. Verify new contact on Saved list on Contacts screen.
        """
        self.__load_contacts_screen()
        self.contacts.click_add()
        self.contacts.verify_phone_invalidation_message(1234567890123, self.test_04_add_new_contact_with_invalid_formart.__name__, is_new=True)

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __load_contacts_screen(self, check_onboarding=False):
        """
        Load to Contacts screens:
            - Load Compose Fax screen
            - Click on person icon in To area
            - Verify Contacts screen as current screen
        """
        # Make sure compose fax screen is empty, not affect by previous test
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=True,
                                                  check_onboarding=check_onboarding)
        self.compose_fax.click_contacts_icon()
        self.contacts.verify_contacts_screen()

    def __add_new_contact(self, phone, contact_name, code):
        """
        At Contacts screen, add a new contact
        :return contact phone and name
        """
        self.contacts.click_add()
        self.contacts.add_edit_contact(phone, contact_name, is_new=True)
        self.contacts.verify_contacts_screen()
        self.contacts.click_tab_btn(self.contacts.SAVED_TAB_BTN)
        self.contacts.verify_contact(phone_number="{} {}".format(code, phone), contact_name=contact_name, is_saved=True)
        return "{} {}".format(code, phone),contact_name

    def __load_edit_contact_screen(self, phone_number, contact_name):
        """
        At Contacts/ Saved tab, load Edit Contact screen
        :param phone_number:
        :param contact_name:
        """
        self.contacts.click_tab_btn(self.contacts.SAVED_TAB_BTN)
        self.contacts.click_saved_contact_info(phone_number=phone_number, contact_name=contact_name)
        self.contacts.verify_edit_contact_screen()