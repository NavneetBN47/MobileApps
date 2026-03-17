from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from MobileApps.resources.const.android.const import *
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import datetime

pytest.app_info = "SMART"

class Test_Suite_01_Files_And_Cover_Page(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.fax_settings = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_SETTINGS]

        # Define variables
        cls.recipient_info = cls.fc.get_softfax_recipient_info()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    def test_01_disable_cover_page(self):
        """
        Description: C31379781, C31379777, C31379778, C31379779
            1. Load to Compose Fax with an account as the one in precondition
            2. Click on Files and Cover Page
            3. Enable Need a cover page?
            4. Fill Subject
            5. Disable a cover page
            6. Turn on need a cover page?
            7. Fill Message
            8. Click on Any button on the screen
            9. Click on Trash icon

        Expected Result:
            2. Verify Files and Cover Page screen
            5. Verify Files and Cover page screen with:
               - Cover Page / 1 page message is invisible
               - Message and Subject message is invisible
               - Need a cover page? should be turned off
            8. Verify invalid message with:
               - Fax Subject is required
            9. Need a cover page? should be turned off
        """
        self.__load_file_cover_page_screen()
        self.compose_fax.toggle_need_a_cover_page_on_off(on=False)
        self.compose_fax.verify_cover_page(invisible=True, displayed=False)
        self.compose_fax.verify_one_cover_page(invisible=True, displayed=False)
        self.compose_fax.verify_subject(invisible=True)
        self.compose_fax.toggle_need_a_cover_page_on_off(on=True)
        self.compose_fax.enter_subject(name="")
        self.compose_fax.click_send_fax(raise_e=False)
        self.compose_fax.verify_subject_invalid_message()
        self.compose_fax.click_trash_icon()
        self.compose_fax.verify_cover_page(invisible=True, displayed=False)
        self.compose_fax.verify_one_cover_page(invisible=True, displayed=False)
        self.compose_fax.verify_subject(invisible=True)

    def test_02_cancel_save_cover_page_template(self):
        """
        Description: C31379783, C31379784, C31379785
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Fill Subject information
            6. Click on Save cover page template button
            7. Click on CANCEL button
            8. Click on Save cover page template button
            9. Enter cover page template name
            10. Click on SAVE button
        Expected Result:
            7. Verify compose fax screen without Template: shows
            10. Verify Template: shows on Compose Fax screen
        """
        template_name = "{}_{:%d_%H_%M_%S}".format("cancel_Save", (datetime.datetime.now()))
        name = "{}_{:%M_%S}".format("QAMA", (datetime.datetime.now()))
        self.__load_file_cover_page_screen(create_acc=True)
        self.compose_fax.enter_subject(name=name)
        self.compose_fax.click_save_cover_page_template()
        self.compose_fax.verify_name_your_cover_page_template()
        self.compose_fax.click_cancel_btn()
        self.compose_fax.verify_cover_page(invisible=False, displayed=False)
        self.compose_fax.verify_one_cover_page(invisible=False)
        self.compose_fax.click_save_cover_page_template()
        self.compose_fax.enter_cover_page_name(template_name)
        self.compose_fax.click_save_btn()
        self.compose_fax.verify_cover_template()
    
    def test_03_save_cover_page_template_without_name(self):
        """
        Description: C31379786
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Click Save cover page template
            6. Click on Save button without filling Name
        Expected Result:
            6. Verify the message "A cover page template title is required"
        """
        self.__load_file_cover_page_screen(create_acc=True)
        self.compose_fax.enter_subject(name="QAMA")
        self.compose_fax.click_save_cover_page_template()
        self.compose_fax.verify_name_your_cover_page_template()
        self.compose_fax.click_save_btn()
        self.compose_fax.verify_no_cover_page_template_title_message()

    def test_04_template_edit(self):
        """
        Description: C31379789, C31379790
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Click Save cover page template with a name
            6. Click on Template on Compose fax screen
            7. Click on Edit button
            8. Do some change on Edit Cover Page screen
            9. Click on Save button
        Expected Result:
            7. Verify Edit Cover Page screen
            9. Verify compose fax screen with new updated template information
        """
        template_name = "{}_{:%d_%H_%M_%S}".format("test_04", (datetime.datetime.now()))
        name = "{}_{:%M_%S}".format("QAMA", (datetime.datetime.now()))
        new_cover_page_name = "new_{}".format(self.udid)
        subject_name = self.test_04_template_edit.__name__
        self.__load_file_cover_page_screen(create_acc=True)
        self.__load_template(name=name, template_name=template_name)
        self.compose_fax.click_template_btn()
        self.compose_fax.click_edit_btn()
        self.fax_settings.add_edit_cover_page(new_cover_page_name, subject_name, is_new=False)
        self.compose_fax.verify_template_list(new_cover_page_name)

    def test_05_template_delete(self):
        """
        Description: C31379792, C31379793
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Click Save cover page template with a name
            6. Click on Template on Compose fax screen
            7. Click on Edit button
            8. Click on Delete button
            9. Click on CANCEL button
            10. Click on Delete button
            11. Click on DELETE button
        Expected Result:
            8. Verify Are you sure? popup
            9. Verify Edit Cover Page screen
            11. Verify Compose fax screen without template
        """
        template_name = "{}_{:%d_%H_%M_%S}".format("cancel_delete", (datetime.datetime.now()))
        self.__load_file_cover_page_screen(create_acc=True)
        self.__load_template(name="QAMA", template_name=template_name)
        self.compose_fax.click_template_btn()
        self.compose_fax.click_edit_btn()
        self.fax_settings.click_cover_pages_delete_btn(is_edited=True)
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
        self.fax_settings.verify_edit_cover_page_screen()
        self.fax_settings.click_cover_pages_delete_btn(is_edited=True)
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
        self.compose_fax.verify_cover_template(invisible=True, raise_e=True)

    def test_06_template(self):
        """
        Description: C31379787, C31379788, C31379795, C31379794
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Click Save cover page template with a name
            6. Click on Template on Compose fax screen
            7. Click on None button
            8. Click on Template on Compose fax screen
            9. Click on Create a new cover page template, and create a new cover page
        Expected Result:
            6. Verify Template screen with:
               - None
               - Edit
               - Create a new cover page template
            7. Verify compose fax screen with template == None
            9. Verify Add Cover Page screen, and cover page can be saved success after that
        """
        template_name = "{}_{:%d_%H_%M_%S}".format("test_06", (datetime.datetime.now()))
        name = "{}_{:%M_%S}".format("QAMA", (datetime.datetime.now()))
        self.__load_file_cover_page_screen(create_acc=True)
        self.__load_template(name=name, template_name=template_name)
        self.compose_fax.click_template_btn()
        self.compose_fax.verify_cover_template_option_screen()
        self.compose_fax.click_none_option()
        self.compose_fax.verify_cover_template()
        self.compose_fax.verify_template_list("None")
        self.compose_fax.click_template_btn()
        self.compose_fax.click_create_a_new_cover_page_template_option()
        self.fax_settings.add_edit_cover_page("test_06", "test_06")
        self.compose_fax.verify_template_list("test_06")

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __load_file_cover_page_screen(self, create_acc=True):
        """
        Load to Files and Cover Page screens:
            - Load Compose Fax screen
            - Click on Files and Cover Page
            - Verify Files and Cover Page screen
        """
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=create_acc,check_onboarding=False)
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.verify_no_updated_file()
        self.compose_fax.toggle_need_a_cover_page_on_off(on=True)
        self.compose_fax.verify_cover_page(invisible=False, displayed=False)
        self.compose_fax.verify_one_cover_page(invisible=False)
        self.compose_fax.verify_subject(invisible=False)
    
    def __load_template(self, name, template_name):
        """
        Load template:
            - enter subject
            - Click on save cover page template
            - Click on cover page name, and click on Save button after that
        """
        self.compose_fax.enter_subject(name=name)
        self.compose_fax.click_save_cover_page_template()
        self.compose_fax.enter_cover_page_name(cover_page_name=template_name)
        self.compose_fax.click_save_btn()