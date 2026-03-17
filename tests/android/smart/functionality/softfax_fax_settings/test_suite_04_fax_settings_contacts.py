from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
import datetime

pytest.app_info = "SMART"


class Test_Suite_04_Fax_Settings_Contacts(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_settings = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_SETTINGS]
        cls.contacts = cls.fc.flow[FLOW_NAMES.SOFTFAX_CONTACTS]

        # Define variables
        cls.recipient_phone = cls.fc.get_softfax_recipient_info()["phone"]
        cls.recipient_code = cls.fc.get_softfax_recipient_info()["code"]
        cls.udid = cls.driver.driver_info["desired"]["udid"]

    def test_01_delete_contacts(self):
        """
        Description: C31379855, C31379856, C31379857, C31379858
            1. Load to Compose Fax with an new account
            2. Click on 3 dot menu/ Fax Settings
            3. Click Contacts
            4. Click on Add a Contact screen
            5. Add Fax Number and Name
            6. Click on Save button
            7. Click on Edit button
            8. Select a contact
            9. Click on Delete button
            10. Click on Cancel button
            11. Click on Delete button
            12. Click on Delete button

        Expected Result:
            3. Verify Contacts empty screen with:
               - Title
               - Add a contact button
               - Empty contact message "You don't have any contacts"
            9. Verify Are you sure? popup:
               - Message popup
               - Cancel button
               - Delete button
            10. Verify Contacts edit screen
            12. Verify Contacts screen
        """
        contact_name = "{}_{:%d_%H_%M_%S}".format("cancel_delete", (datetime.datetime.now()))
        self.__load_contacts_screen()
        self.fax_settings.verify_empty_contact_screen()
        self.__add_new_contact(self.recipient_phone, contact_name)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.CONTACT_SELECT_BTN)
        self.contacts.select_saved_contact(self.recipient_phone, contact_name)
        self.fax_settings.click_contact_delete_btn()
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
        self.fax_settings.verify_contact_edit_screen()
        self.fax_settings.click_contact_delete_btn()
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
        self.fax_settings.verify_contact_screen()
        self.contacts.verify_contact(phone_number=self.recipient_phone, contact_name=contact_name, invisible=True)

    def test_02_delete_edit_contacts(self):
        """
        Description: C31379861, C31379863, C31379864
            1. Load to Contacts screen with contacts list
            2. Select any contact
            3. Click on Delete button
            4. Click on Cancel button
            5. Click on Delete button
            6. Click on Delete button

        Expected Result:
            2. Verify Edit Contact screen
            3. Verify Are you sure? popup:
               - Message popup
               - Cancel button
               - Delete button
            4. Verify Edit Contacts screen
            6. Verify Contacts screen
        """
        contact_name = "{}_{:%d_%H_%M_%S}".format("cancel_delete", (datetime.datetime.now()))
        self.__load_contacts_screen()
        self.__add_new_contact(self.recipient_phone, contact_name)
        self.contacts.select_saved_contact(self.recipient_phone, contact_name)
        self.fax_settings.verify_edit_contact_screen()
        self.fax_settings.click_contact_delete_btn()
        self.fax_settings.dismiss_edit_delete_confirmation(is_deleted=False)
        self.fax_settings.verify_edit_contact_screen()
        self.fax_settings.click_contact_delete_btn()
        self.fax_settings.dismiss_edit_delete_confirmation(is_deleted=True)
        self.fax_settings.verify_contact_screen()
        self.contacts.verify_contact(self.recipient_phone, contact_name, invisible=True)

    def test_03_contacts_edit_cancel(self):
        """
        Description: C31379859, C31379860
            1. Load to Compose Fax with HPID account login
            2. Click on 3 dot menu/ Fax Settings
            3. Click on Contacts
            4. Click on Edit button
            5. Click on Cancel button

        Expected Result:
            3. Verify Contacts screen with:
               - Title
               - Contact Lists
            4. Verify Contacts Edit screen with:
               - Title
               - Cancel button
            5. Verify Contacts screen with:
               - Title
               - Contact Lists
        """
        contact_name = "{}_{:%d_%H_%M_%S}".format("test_05", (datetime.datetime.now()))
        self.__load_contacts_screen()
        self.__add_new_contact(self.recipient_phone, contact_name)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.CONTACT_SELECT_BTN)
        self.fax_settings.verify_contact_edit_screen()
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.CONTACT_CANCEL_BTN)
        self.fax_settings.verify_contact_screen()

    def test_04_edit_contacts_save(self):
        """
        Description: C31379862
            1. Load to Contacts screen with a new HPID account
            2. click any contact from the contacts list
            3. Update Fax number
            4. Click on Save button

        Expected Result:
            4. Verify Contacts save success
        """
        contact_name = "{}_{:%d_%H_%M_%S}".format("test_06", (datetime.datetime.now()))
        self.__load_contacts_screen()
        self.__add_new_contact(self.recipient_phone, contact_name)
        self.contacts.select_saved_contact(self.recipient_phone, contact_name)
        self.contacts.add_edit_contact("(858) 689-5898", "{}_updated".format(contact_name), False)
        self.contacts.verify_contact("{} {}".format(self.recipient_code, "(858) 689-5898"), "{}_updated".format(contact_name), False)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __load_contacts_screen(self, create_acc=True):
        """
        - Load Compose Fax screen with HPID account login or created a new HPID account
        - Click on Fax Settings on from More Option menu
        - Click on Contacts on Fax Settings screen
        """
        # Make sure tests not affected by previous test suite
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=create_acc, check_onboarding=False)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN)
        self.fax_settings.verify_fax_settings_screen()
        self.fax_settings.click_fax_settings_option(self.fax_settings.CONTACTS_OPT)
        self.fax_settings.verify_contact_screen()
    
    def __add_new_contact(self, receipt_phone, contact_name):
        """
        At Contacts screen, add a new contact
        :return contact phone and name
        """
        self.fax_settings.click_add_a_contact_btn()
        self.contacts.add_edit_contact(receipt_phone, contact_name, is_new=True)
        self.fax_settings.verify_contact_screen()
        self.contacts.verify_contact(phone_number="{} {}".format(self.recipient_code, receipt_phone), contact_name=contact_name)
        return "{} {}".format(self.recipient_code, receipt_phone), contact_name