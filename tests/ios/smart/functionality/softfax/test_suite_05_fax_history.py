import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "SMART"

class Test_Suite_05_Fax_History(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.fax_history = cls.fc.fd["softfax_fax_history"]
        cls.fax_settings = cls.fc.fd["fax_settings"]
        cls.preview = cls.fc.fd["preview"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.fake_recipient = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_11"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_03"]
    
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.home.select_app_settings()
        self.app_settings.select_mobile_fax()
        self.fc.create_account_from_tile()
        self.fc.verify_fax_welcome_screens_and_nav_compose_fax()

    def test_01_verify_fax_history_ui_when_no_faxes_sent(self):
        """
        Descriptions: C31379885
            1.Launch the app and navigate to "Compose Fax" screen
            2.Tap on 3 dot menu and tap on "Fax History" option
            3.Verify for the sent fax history details
        Expected Results:
            3."You have no sent fax history" screen should be displayed when no faxes were sent 
        """
        self.compose_fax.click_menu_option_btn(self.fax_settings.MENU_FAX_HISTORY_BTN, "save_as_draft_popup_exit_bn")
        self.fax_history.verify_sent_fax_history_list(is_empty=True)

    def test_02_verify_sent_fax_history_ui(self):
        """
        Descriptions: C31379886, C31379895
            1.launch app
            2.tap on fax tile and navigate to fax history screen
            3.tap on SENT tab
            4.tap on Select button
        Expected Results:
            2.User should be navigated to "Fax History" page 
            3.verify that all the list of faxes sent should be displayed with the info:
                - Recipient Name
                - Recipient Number
                - time Sent
                - Number of pages sent
                - successful/unsuccessful/processing status   
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.recipient_info["phone"])
        self.fax_history.verify_sent_fax_history_list(is_empty=False)
    
    def test_03_verify_print_confirmation_successful_sent_fax(self):
        """
        Descriptions: C31379890, C16033028, C24773511
            1.launch app
            2.tap on fax tile and navigate to fax history screen
            3.tap on SENT tab
            4.tap on any processing fax from the list
        Expected Results:
            4.verify that "Sent Fax Details" screen displayed matches with the actual fax sent
                - preview of the pages sent
                - Processing Documents section : - To: (Recipient Name & Recipient Number) - Pages: (Number of pages)
                - Fax Sent Success section -: - Started: Started date and time - Finished: Finished date and time
                - Edit and Resend button
                - Cancel button
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.recipient_info["phone"])
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.verify_send_fax_status(is_successful=True, check_sending=False)
        self.send_fax_details.verify_phone_number(phone_number="+1 " + self.recipient_info["phone"])
        self.send_fax_details.verify_time_information(is_successful=True)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.PRINT_CONFIRMATION_BTN, self.send_fax_details.HOME_BTN])
    
    def test_04_verify_unsuccessful_fax_sent_history(self):
        """
        Descriptions: C31379887, C31379891, C31379889
            1.launch app
            2.tap on fax tile and navigate to fax history screen
            3.tap on SENT tab
            4.tap on any sent fax from the list which is not successful
            5.tap on the cancel button
            6.tap on any sent fax from the list which is not successful
            7.tap on the 'retry fax' button
            8.tap on 'Cancel fax' button
        Expected Results:
            4.verify that "Sent Fax Details" screen displayed matches with the actual fax sent
                - Delivery Failed section -: - To: Recipient number - Started: Started date and time - Finished: Finished date and time
                - preview of the pages sent
                - Retry Fax button
                - Edit and Resend button
            5.verify that the fax processing is cancelled and removed from the fax history list
            7.verify that Sent Fax Details screen should be displayed with the retry of the fax sending and options:
                -Cancel Fax
                -Home
            8.verify that the fax retry is stopped
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.fake_recipient["phone"], is_successful=False) 
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.fake_recipient["phone"], status=self.fax_history.FAILED_STATUS)
        self.send_fax_details.verify_send_fax_status(is_successful=False, check_sending=False)
        self.send_fax_details.verify_phone_number(phone_number="+1 " + self.fake_recipient["phone"])
        self.send_fax_details.verify_time_information(is_successful=False)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.RETRY_FAX_BTN, self.send_fax_details.EDIT_RESEND_BTN])
        self.send_fax_details.click_bottom_button(self.send_fax_details.RETRY_FAX_BTN)    
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.CANCEL_FAX_BTN, self.send_fax_details.HOME_BTN])
    
    def test_06_verify_fax_edit_and_resend_failed_fax(self):
        """
        Descriptions: C31379893
            1.launch app
            2.tap on fax tile and navigate to fax history screen
            3.tap on SENT tab
            4.tap on any sent fax from the list which was not successful
            5.tap on "Edit and Resend" option
            6.Edit the files already added and send the fax
        Expected Results:
            Verify that the fax is sent successfully
        """
        self.fc.nav_to_compose_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.fake_recipient["phone"], status=self.fax_history.FAILED_STATUS)
        self.send_fax_details.verify_send_fax_status(is_successful=False, check_sending=False)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.RETRY_FAX_BTN, self.send_fax_details.EDIT_RESEND_BTN])
        self.send_fax_details.click_bottom_button(self.send_fax_details.RETRY_FAX_BTN)

    def test_07_verify_fax_history_draft_when_faxes_are_saved(self):
        """
        Descriptions: C31379894
            1.Launch the app and navigate to "Compose Fax" screen
            2.Tap on 3 dot menu and tap on "Fax History" option
            3.tap on DRAFT tab and verify for the saved fax details
        Expected Results:
            verify that all the list of faxes saved should be displayed with the info:
                -[Draft]
                -Recipient Name
                -Recipient Number
                -time/day Sent
                -Number of pages added
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.recipient_info["phone"], option="draft")
        self.fax_history.select_tab(self.fax_history.DRAFT_RECORD_CELL)
        self.fax_history.select_history_record(self.fax_history.DRAFT_RECORD_CELL, phone_number=self.recipient_info["phone"])
        
    def test_08_verify_print_confirmation_sent_fax_details(self):
        """
        C24773511 - Verify "Print confirmation" button from Sent Fax Details
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.recipient_info["phone"])
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.click_bottom_button(self.send_fax_details.PRINT_CONFIRMATION_BTN)
        self.preview.verify_preview_screen()
    
    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_09_verify_compose_new_fax_button_sent_tab_fax_history(self, tab):
        """
        Descriptions: C31379897
            1.Tap on Mobile Fax tile and Compose Fax screen
            2.Tap on Three vertical dots from top right corner of the screen
            3.Tap on Fax history option
            4.Tap on "Sent" tab
            5.Tap on "Compose New Fax" button
        Expected Results:
            5.User navigate to "Compose Fax" page 
        """
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN, "save_as_draft_popup_exit_bn")
        self.fax_history.verify_fax_history_screen()
        if tab == "sent":
            self.fax_history.select_tab(self.fax_history.SENT_TAB)
        else:
            self.fax_history.select_tab(self.fax_history.DRAFT_RECORD_CELL)
        self.fax_history.click_compose_new_fax()
        self.compose_fax.verify_compose_fax_screen()
    
    def test_11_verify_delete_fax_history(self):
        """
        Descriptions: C31379903
            1.Tap on Mobile Fax tile and Compose Fax screen
            2.Tap on Three vertical dots from top right corner of the screen
            3.Tap on Fax history option
            4.Tap on "Sent" tab
            5.Tap on any successful sent Fax
            6.Tap on three vertical dots from top right corner of the Sent Fax Details screen
            7.Select "Delete this Fax" option
            8.Tap on Delete
        Expected Results:
            8.User should be re-directed to "Fax History" page under "Sent" tab and make sure deleted fax should not be available in Fax sent tab
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.recipient_info["phone"])
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_DELETE_BTN)
        self.send_fax_details.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()
    
    def test_12_verify_home_btn_fax_screen(self):
        """
        Descriptions: C31379899
            1.Tap on Mobile Fax tile and Compose Fax screen
            2.Tap on Three vertical dots from top right corner of the screen
            3.Tap on Fax history option
            4.Tap on "Sent" tab
            5.Tap on any successful sent Fax
            6.Tap on Home button
        Expected Results:
            6. User should be re-directed to Home Screen
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.recipient_info["phone"])
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.click_bottom_button(self.send_fax_details.HOME_BTN)
        self.home.verify_home_tile()

    def test_13_verify_delete_fax_option(self):
        """
        Descriptions: C31379900
            1.Tap on Mobile Fax tile and Compose Fax screen
            2.Tap on Three vertical dots from top right corner of the screen
            3.Tap on Fax history option
            4.Tap on "Sent" tab
            5.Tap on any successful sent Fax
            6.Tap on three vertical dots from top right corner of the Sent Fax Details screen
            7.Select "Delete this Fax" option
            8.Tap on Cancel button
        Expected Results:
            7.Are you sure? pop up should open
                Message= This fax history item and attachment will be deleted. This action can't be undone.
                Buttons- "CANCEL" , "DELETE"
            8.Pop up should dismiss and user should be at Sent Fax Details page
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.recipient_info["phone"])
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_DELETE_BTN)
        self.send_fax_details.dismiss_delete_confirmation_popup(is_yes=False)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.verify_phone_number(phone_number="+1 " + self.recipient_info["phone"])
    
    def test_14_verify_save_fax_log(self):
        """
        Descriptions: C31379901
            1.Tap on Mobile Fax tile and Compose Fax screen
            2.Tap on Three vertical dots from top right corner of the screen
            3.Tap on Fax history option
            4.Tap on "Sent" tab
            5.Tap on any successful sent Fax
            6.Tap on three vertical dots from top right corner of the Sent Fax Details screen
            7.Select "Save Fax Log" option
        Expected Results:
            1.Fax History Logs should open in PDF viewer 
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.recipient_info["phone"])
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_SAVE_LOG_BTN)
        self.send_fax_details.verify_menu_save_fax_log(invisible=True)
    
    def test_15_verify_home_option_from_menu(self):
        """
        Descriptions: C31379902
            1.Tap on Mobile Fax tile and Compose Fax screen
            2.Tap on Three vertical dots from top right corner of the screen
            3.Tap on Fax history option
            4.Tap on "Sent" tab
            5.Tap on any successful sent Fax
            6.Tap on three vertical dots from top right corner of the Sent Fax Details screen
            7.Select "Home"
        Expected Results:
            7.User should re-directed to Home Screen
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.recipient_info["phone"])
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.home.verify_home_tile()
    
    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_16_verify_edit_fax_history(self, tab):
        """
        Descriptions: C31379905, C31379904, C31379918, C31379906, C31379924
            1.Tap on Mobile Fax tile and Compose Fax screen
            2.Tap on Three vertical dots from top right corner of the screen
            3.Tap on Fax history option
            4.Tap on "Select" from top right corner of the page for Sent Tab
            5.Tap on any sent Fax
            6.tap on delete option
            7.choose delete option from the pop up window
            8.navigate to draft faxes tab
            9.tap on Selct button
            10.choose any one saved fax from the list and tap on delete option
            11.choose delete option from the pop up window 
        Expected Results:
            4.Radio button to select should display in front of All sent/draft faxes will
                "Cancel" from top right corner of the screen
                "Delete" and "Export Fax Log" option should be disable at the bottom of the screen
            5.Verify "Delete" and "Export Fax Log" options should be enable at the bottom of the screen
            7.Verify that the fax is deleted successfully from the list of sent faxes
            11.verify that the fax is deleted successfully from the list of saved faxes
        """
        self.send_fax_and_go_to_fax_history_screen(phone_no=self.recipient_info["phone"], option=tab)
        if tab == "draft":
            self.fax_history.select_tab(self.fax_history.DRAFT_RECORD_CELL)
        self.fax_history.load_edit_screen()
        self.fax_history.verify_edit_screen()
        if tab == "sent":
            self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"])
        else:
            self.fax_history.select_tab(self.fax_history.DRAFT_RECORD_CELL)
            self.fax_history.select_history_record(self.fax_history.DRAFT_RECORD_CELL, phone_number=self.recipient_info["phone"])
        self.fax_history.click_edit_delete()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()
        if tab == "sent":
            self.fax_history.verify_sent_fax_history_list(is_empty=True)
        else:
            self.fax_history.verify_draft_fax_history_list(is_empty=True)

    def send_fax_and_go_to_fax_history_screen(self, phone_no=None, option="sent", is_successful=True, no_faxes=1):
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
                self.send_fax_details.verify_send_fax_status(timeout=360, is_successful=is_successful, check_sending=False)
            else:
                sleep(10)
                self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_SAVE_DRAFT_BTN, "save_as_draft_popup_save_draft_btn")
            self.send_fax_details.click_back()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN, "save_as_draft_popup_exit_bn")
        self.fax_history.verify_fax_history_screen()
