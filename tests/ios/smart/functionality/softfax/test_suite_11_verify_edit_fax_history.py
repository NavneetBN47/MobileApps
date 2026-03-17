import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "SMART"

class Test_Suite_11_Verify_Edit_Fax_History(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.fax_history = cls.fc.fd["softfax_fax_history"]
        cls.fax_settings = cls.fc.fd["fax_settings"]
        cls.preview = cls.fc.fd["preview"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.fake_recipient = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_05"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_02"]
    
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.home.select_app_settings()
        self.app_settings.select_mobile_fax()
        self.fc.create_account_from_tile()
        self.fc.verify_fax_welcome_screens_and_nav_compose_fax()

    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_01_verify_edit_sent_faxes_ui(self, tab):
        """
        Descriptions: C31379916, C31379917
            1.launch the app and navigate to fax history screen
            2.navigate to sent faxes tab
            3.tap on Select button
            4.navigate to draft faxes tab
            5.tap on edit button
        Expected Result:
            3.verify that all the faxes under sent tab should be displayed in the edit mode to choose any fax to edit with the options-:
                -Delete
                -Export Fax Log
                -Cancel button
            5.verify that all the faxes under draft tab should be displayed in the edit mode to choose any fax to edit with the options-:
                -Delete
                -Export Fax Log
                -Cancel button
        """
        
        if tab == "sent":
            self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], no_faxes=1)
        else:
            self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], option="draft", no_faxes=1)
        self.fax_history.load_fax_edit_screen_from_fax_history(draft_tab=(tab == "draft"))
        self.fax_history.verify_edit_screen()

    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_02_verify_edit_and_do_not_delete_sent_faxes(self, tab):
        """
        Descriptions: C31379919,C31379925
            1.launch the app and navigate to fax history screen
            2.navigate to sent faxes tab
            3.tap on edit button
            4.choose any sent fax from the list and tap on delete option
            5.choose Cancel option from the pop up window
            6.navigate to draft faxes tab
            7.tap on Select button
            8.choose any saved fax from the list and tap on delete option
            9.choose Cancel option from the pop up window 
        Expected Result:
            5.verify that the fax is not deleted and the fax is displayed under the list of sent faxes
            9.verify that the fax is not deleted and the fax is displayed under the list of draft faxes
        """
        fax_option, draft_option, history_option = (None, False, self.fax_history.SENT_RECORD_CELL) if tab == "sent" else ("draft", True, self.fax_history.DRAFT_RECORD_CELL)
        self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], no_faxes=1, option=fax_option)
        self.fax_history.load_fax_edit_screen_from_fax_history(draft_tab=draft_option)
        self.fax_history.select_multiple_history_records(history_option, phone_number=self.recipient_info["phone"], number_records=1)
        self.fax_history.click_edit_delete()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=False)
        self.fax_history.click_edit_cancel()
        if tab == "sent":
            self.fax_history.verify_sent_fax_history_list(is_empty=False, phone_number=self.recipient_info["phone"])
        else:
            self.fax_history.verify_draft_fax_history_list(is_empty=False, phone_number=self.recipient_info["phone"])
        
    def test_03_verify_edit_and_export_multiple_faxes_from_sent_faxes(self):
        """
        Descriptions: C31379920
        1.launch the app and navigate to fax history screen
        2.navigate to sent faxes tab
        3.tap on Select button
        4.choose multiple faxes from the list and tap on "Export Fax Log" option
        Expected Result:
        4.verify that the smart app fax history log should be opened in the PDF viewer screen for all the faxes choosen 
        """
        self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], no_faxes=2)
        self.fax_history.load_edit_screen()
        self.fax_history.verify_edit_screen()
        self.fax_history.select_multiple_history_records(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], number_records=2)
        self.fax_history.click_edit_export_fax_log()
        self.preview.verify_preview_screen()

    @pytest.mark.parametrize("sent_fax_number", ["single", "multiple"])
    def test_04_verify_edit_and_delete_multiple_faxes_from_sent_faxes(self, sent_fax_number):
        """
        Descriptions: C31379921, C31379926
        1.launch the app and navigate to fax history screen
        2.navigate to sent faxes tab
        3.tap on Select button
        4.choose multiple faxes from the list and tap on "Delete" option
        5.choose delete option from the pop up window
        6.navigate to Draft faxes tab
        7.tap on Select button
        8.choose multiple saved faxes from the list and tap on delete option
        9.choose delete option from the pop up window 
        Expected Result:
        5.verify that all the faxes choosen should be deleted from the list of sent faxes
        9.verify that all the selected faxes are deleted successfully from the list of saved faxes
        """
        page_count = 1 if sent_fax_number == "single" else 2
        self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], no_faxes=page_count)
        self.fax_history.load_fax_edit_screen_from_fax_history()
        self.fax_history.select_multiple_history_records(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], number_records=page_count)
        self.fax_history.click_edit_delete()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()
        assert not self.driver.wait_for_object("history_record_phone_number", format_specifier=["phone"], raise_e=False, timeout=5)
    
    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_05_verify_swipe_delete(self, tab):
        """
        Descriptions: C31379922, C31379927
        1.launch the app and navigate to fax history screen
        2.navigate to sent faxes tab
        3.swipe left on any sent fax
        4.choose delete option
        5.choose delete option from the pop up window
        6.navigate to Draft faxes tab
        7.swipe left on any of the saved fax
        8.choose delete option
        9.choose delete option from the pop up window
        Expected Result:
        5.verify that the fax is deleted successfully from the list of sent faxes
        9.verify that the fax is deleted successfully from the list of saved faxes
        """
        if tab == "sent":
            self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], no_faxes=1)
            self.fax_history.open_record_menu_for_ios(self.recipient_info["phone"])
        else:
            self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], option="draft", no_faxes=1)
            self.fax_history.select_tab(self.fax_history.DRAFT_TAB)
        self.fax_history.open_record_menu_for_ios(self.recipient_info["phone"])
        self.fax_history.click_record_delete_btn()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()
        assert not self.driver.wait_for_object("history_record_phone_number", format_specifier=["phone"], raise_e=False, timeout=5)

    def send_fax_and_go_to_fax_history_screen(self, phone_no=None, option="sent", no_faxes=1):
        """
        option: sent = send fax; draft = create draft
        """
        for _ in range (no_faxes):
            self.compose_fax.enter_recipient_information(phone_no)
            self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
            self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
            self.fc.select_photo_from_photo_picker(select_all_files=False)
            self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
            self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
            self.compose_fax.verify_compose_fax_screen()
            if option == "sent":
                self.compose_fax.click_send_fax_native_btn()
                self.send_fax_details.verify_send_fax_status(timeout=360, is_successful=True, check_sending=False)
            else:
                sleep(10)
                self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_SAVE_DRAFT_BTN)
                self.compose_fax.handle_save_as_draft_popup("save_as_draft_popup_save_draft_btn")
            self.send_fax_details.click_back()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.compose_fax.handle_save_as_draft_popup("save_as_draft_popup_exit_bn")
        self.fax_history.verify_fax_history_screen()
