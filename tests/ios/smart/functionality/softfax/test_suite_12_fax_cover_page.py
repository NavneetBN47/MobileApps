import pytest
import time
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "SMART"

class Test_Suite_12_Fax_Cover_Page(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.fax_history = cls.fc.fd["softfax_fax_history"]
        cls.fax_settings = cls.fc.fd["fax_settings"]
        cls.preview = cls.fc.fd["preview"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.fake_recipient = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_05"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_02"]
        cls.node = request.node.name
        cls.fc.go_home(reset=True, stack=cls.stack, button_index=1, create_account=True)
    
    def test_01_verify_cover_page_for_user(self):
        """
        C24821257 - Verify “Empty Cover Pages” screen
        C24814556 - Verify "Create a Cover Page" button
        """
        self.fc.nav_to_compose_fax(new_user=True)
        cover_page_name = "test_01_cover_page"
        subject = self.test_01_verify_cover_page_for_user.__name__
        self._load_fax_settings_screen()
        self.__create_a_cover_page(cover_page_name, subject)
        self.fax_settings.verify_cover_page(cover_page_name)
    
    @pytest.mark.parametrize("options", ["cancel", "delete"])
    def test_02_verify_edit_cover_page(self, options):
        """
        C24814551 - Verify "Cancel Delete" from Edit Cover Page
        C24814548 - Verify "Edit Cover Pages" screen
        C24814552 - Verify "Delete" button option from "Are you sure?" pop up while deleting cover page
        C24814547 - Verify "Cover Pages" when user has already cover pages
        C24814554 - Verify "Cancel Delete" from "Edit" of Cover Page
        """
        self.fc.nav_to_compose_fax()
        cover_page_name = "test_02_cover_page_{}".format(options)
        subject = self.test_02_verify_edit_cover_page.__name__
        self._load_fax_settings_screen(options)
        self.__create_a_cover_page(cover_page_name, subject)
        self.fax_settings.select_single_cover_page(cover_page_name)
        self.fax_settings.verify_edit_cover_page_screen()
        self.fax_settings.click_cover_pages_delete_btn(is_edited=True)
        if options == "cancel":
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
            self.fax_settings.verify_edit_cover_page_screen()
        else:
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
            self.fax_settings.verify_cover_page_screen()
    
    def test_03_verify_edit_btn_cover_page(self):
        """
        C24814553 - Verify "Edit" from "Cover Pages" screen
        """
        self.fc.nav_to_compose_fax()
        cover_page_name = "test_03_cover_page"
        subject = self.test_03_verify_edit_btn_cover_page.__name__
        self._load_fax_settings_screen()
        self.__create_a_cover_page(cover_page_name, subject)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.COVER_PAGE_SELECT_BTN)
        self.fax_settings.verify_cover_page_edit_screen()
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.COVER_PAGE_CANCEL_BTN)
        self.fax_settings.verify_cover_page_screen()

    def test_04_verify_toggle_switch_behavior(self):
        """
        C31379777 Verify toggle switch enable behavior for "Need a cover page?"
        1.Tap on Mobile Fax tile and reach to the Composer Fax page
        2.Tap on "files and Cover page"
        3.Turn on toggle switch for "Need a cover page?"
        3.Verify below fields as soon as toggle switch turn on
        - Subject*
        - Message
        - Cover Page
        - 1 page text should show under "Cover Page"
        - Cover Page preview with magnifier glass icon
        - Trash icon
        """
        self.fc.nav_to_compose_fax()
        self.compose_fax.click_files_and_cover_page()
        self.compose_fax.toggle_need_a_cover_page_on_off()
        self.compose_fax.verify_subject()
        self.compose_fax.verify_trash_icon()
        self.compose_fax.verify_message()
        self.compose_fax.verify_cover_page_magnifier()

    def test_05_verify_toggle_switch_disable(self):
        """
        C31379781
        1.Tap on Mobile Fax tile and reach to the Composer Fax page
        2.Tap on "files and Cover page"
        3.Enter all required details in "To" and "From" section
        4.Turn on toggle switch for "Need a cover page?"
        5.Enter Subject and Message
        6.Turn off "Need a cover page?" toggle switch

        Expected results:
        6."Files and Cover Page" section get collapse and "Need a cover page?"
             toggle switch should turn off
        """
        self.fc.nav_to_compose_fax()
        self.compose_fax.enter_recipient_information(self.recipient_info['phone'], "Jane Doe")
        self.compose_fax.enter_sender_information(self.sender_info['name'], self.sender_info['phone'])
        self.compose_fax.click_files_and_cover_page()
        self.compose_fax.toggle_need_a_cover_page_on_off()
        self._verify_cover_page()
        # C31379778 Verify when user tap on "Send Fax" without entering Subject
        self.compose_fax.enter_subject("")
        self.compose_fax.verify_subject_invalid_message()
        self.compose_fax.enter_subject("Test Subject")
        self.compose_fax.toggle_need_a_cover_page_on_off(on=False)
        self._verify_cover_page(invisible=True)
        self.compose_fax.toggle_need_a_cover_page_on_off()
        # C31379779 Verify Delete(Trash) button
        self.compose_fax.click_trash_icon()
        self._verify_cover_page(invisible=True)
        # C31379780 Verify added Cover Page preview button
        self.compose_fax.toggle_need_a_cover_page_on_off()
        self.compose_fax.click_cover_page_magnifier()
        # C31379782 Verify "X" button from Cover page preview
        self.compose_fax.click_close_preview()
        self._verify_cover_page()

    def test_06_cover_page_templates(self):
        """
        C31379783 Verify "Save cover page template"
        1.Tap on Mobile Fax tile and reach to the Composer Fax page
        2.Tap on "files and Cover page"
        3.Enter all required details in "To" and "From" section
        4.Turn on toggle switch for "Need a cover page?"
        5.Enter Subject
        6.Enter Message
        7.Tap on "Save cover page template"

        Expected results:
        5."Save cover page template" should display
        6."Name your cover page template" bottom sheet open with "Name" field and "CANCEL" , "SAVE" button
        C31379784  Verify "CANCEL" from "Name your cover page template" bottom sheet
        C31379785 Verify "SAVE" from "Name your cover page template" bottom sheet
        C31379786 Verify "SAVE" from "Name your cover page template" bottom sheet when user does not enter name
        C31379787 Verify behavior when user tap on already created template name
        C31379788 Verify "None" behavior when user tap on template name
        C31379789 Verify "Edit" behavior when user tap on template name
        C31379790 Verify "Save" from Edit Cover Page
        C31379791 Verify "Save" from Edit Cover Page with all mandatory field Empty
        C31379792 Verify "Delete" from Edit Cover Page
        C31379793 Verify "Delete" button option from "Are you sure?" 
        pop up while deleting cover page
        """
        self.fc.nav_to_compose_fax()
        self.compose_fax.enter_recipient_information(self.recipient_info['phone'], "Jane Doe")
        self.compose_fax.enter_sender_information(self.sender_info['name'], self.sender_info['phone'])
        self.compose_fax.click_files_and_cover_page()
        self.compose_fax.toggle_need_a_cover_page_on_off()
        self.compose_fax.enter_subject("Test Subject2")
        self.compose_fax.click_save_cover_page_template()
        # C31379784  Verify "CANCEL" from "Name your cover page template" bottom sheet
        # C31379785 Verify "SAVE" from "Name your cover page template" bottom sheet
        self.compose_fax.verify_name_your_cover_page_template()
        # C31379786 Verify "SAVE" from "Name your cover page template" bottom sheet when user does not enter name
        self.compose_fax.enter_cover_page_name("")
        self.compose_fax.click_save_btn()
        self.compose_fax.verify_template_title_is_required()
        self.compose_fax.enter_cover_page_name("Template1")
        self.compose_fax.click_save_btn()
        # C31379787 Verify behavior when user tap on already created template name
        self.compose_fax.verify_template_list("Template1")
        assert self.compose_fax.get_cover_page_subject() == "Test Subject2"
        self.compose_fax.click_template_btn()
        # C31379789 Verify "Edit" behavior when user tap on template name
        self.compose_fax.click_edit_btn()
        self.compose_fax.verify_template_edit_view()
        self._create_invalid_entries()
        # edit and save template
        # C31379790 Verify "Save" from Edit Cover Page
        # C31379791 Verify "Save" from Edit Cover Page with all mandatory field Empty
        self.fax_settings.add_edit_cover_page(cover_page_name="Template1-e", cover_page_subject="Test Subject Edit", is_new=False)
        """
        This is a defect see: https://hp-jira.external.hp.com/browse/SOFTFAX-2728
        """
        #assert (self.compose_fax.get_cover_page_subject() =="Test Subject Edit")
        self.compose_fax.verify_cover_page_name("Template1-e")
        self.compose_fax.click_template_btn()
        # C31379788 Verify "None" behavior when user tap on template name
        self.compose_fax.click_none_option()
        assert self.compose_fax.get_cover_page_subject() == None
        self.compose_fax.click_template_btn()
        self.compose_fax.click_edit_btn()
        # C31379792 Verify "Delete" from Edit Cover Page
        self.fax_settings.verify_edit_cover_page_screen()
        #C31379793 Verify "Delete" button option from "Are you sure?" pop up while deleting cover page
        self.fax_settings.click_cover_pages_delete_btn(is_edited=True)
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
        self.compose_fax.verify_cover_page_name("",invisible=True)
        assert self.compose_fax.get_cover_page_subject() == None
        self.compose_fax.enter_subject("Test Subject4")
        self.compose_fax.click_save_cover_page_template()
        self.compose_fax.enter_cover_page_name("Template4")
        self.compose_fax.click_save_btn()
        # C31379794 Verify "Add Cover Page" from "Create a new cover page template"
        # C31379795 Verify "Add Cover Page" when user fill all required information and tap on "Save"
        self.compose_fax.click_template_btn()
        self.compose_fax.click_create_a_new_cover_page_template_option()
        self.fax_settings.add_edit_cover_page("Template3", "Test Subject 3", is_new=True)
        self.compose_fax.verify_cover_page_name("Template3")
        assert self.compose_fax.get_cover_page_subject() == "Test Subject 3"

    def _verify_cover_page(self, invisible=False):
        self.compose_fax.verify_subject(invisible=invisible)
        self.compose_fax.verify_message(invisible=invisible)
        self.compose_fax.verify_trash_icon(invisible=invisible)
        self.compose_fax.verify_cover_page_magnifier(invisible=invisible) 

    def _load_fax_settings_screen(self, options=None):
        if self.compose_fax.verify_compose_fax_screen(raise_e=False) == False:
            self.fc.nav_to_compose_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN)
        if options == "cancel":
            self.fax_settings.select_save_draft_button()
        self.fax_settings.verify_fax_settings_screen()

    def __create_a_cover_page(self, cover_page_name, subject):
        """
        - Click on Create Cover Page button
        - Add cover page name and subject
        - Click on Save button
        """
        self.fax_settings.click_fax_settings_option(self.fax_settings.COVER_PAGES_OPT)
        self.fax_settings.click_create_cover_page_btn()
        self.fax_settings.add_edit_cover_page(cover_page_name, subject)
        self.fax_settings.verify_cover_page_screen()
    def _create_invalid_entries(self):
        self.compose_fax.enter_name_one_character("X")
        self.compose_fax.clear_entry()
        self.compose_fax.verify_invalid_name_entry()
        self.compose_fax.enter_subject_one_character("X")
        self.compose_fax.clear_entry()
        self.compose_fax.verify_invalid_subject_entry()
