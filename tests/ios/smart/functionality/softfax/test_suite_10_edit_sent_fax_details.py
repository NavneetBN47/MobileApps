import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "SMART"

class Test_Suite_10_Edit_Sent_Fax_Details(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

        # Initializing Printer
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.welcome = cls.fc.fd["welcome"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.scan = cls.fc.fd["scan"]
        cls.fax_history = cls.fc.fd["softfax_fax_history"]
        cls.fax_settings = cls.fc.fd["fax_settings"]
        cls.preview = cls.fc.fd["preview"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.fake_recipient = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_09"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_03"]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.welcome.allow_notifications_popup(raise_e=False)
        self.home.select_app_settings()
        self.app_settings.select_mobile_fax()
        self.fc.create_account_from_tile()
        self.fc.verify_fax_welcome_screens_and_nav_compose_fax()

    def test_01_successfully_sent_fax_detail(self):
        '''
        Descriptions: C31379947
            1. Launch the app and navigate to fax history screen
            2. Navigate to sent faxes tab
            3. Tap on any successfully sent fax
        Expected Result:
            Sent Fax Details screen should be displayed with the below info:
                - Sent Fax Details title name
                - Three dot menu
                - Green Tick icon
                - "Fax Delivered!" message
                - "To:" should display the recipient number
                - "Started:" should display the time started to send the fax
                - "Finished:" should display the time finished to sent the fax
                - "Files:" Displays the file name and number of pages sent
                - Print Confirmation button
                - Home button
        '''
        file_name, number_pages = self.create_sent_fax_job(recipient_phone=self.recipient_info["phone"])
        if not len(file_name) and not len(number_pages):
            pytest.skip("No scan feature available on Printer: {}".format(self.p.get_printer_information()))
        self.go_to_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.verify_send_fax_status(is_successful=True, check_sending=False)
        self.send_fax_details.verify_phone_number(phone_number="+1 " + self.recipient_info["phone"])
        self.send_fax_details.verify_time_information(is_successful=True)
        self.send_fax_details.verify_file_information(file_name=file_name, number_page=number_pages)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.PRINT_CONFIRMATION_BTN, self.send_fax_details.HOME_BTN])

    def test_02_sent_fax_details_home(self):
        '''
        Descriptions: C31379951
            1.launch the app and navigate to fax history screen
            2.navigate to sent faxes tab
            3.tap on any sent fax
            4.from "Sent Fax Details" screen tap on three dot menu and tap on "Home" option
        Expected Result:
            verify that the smart app home screen is displayed
        '''
        _, _ = self.create_sent_fax_job(recipient_phone=self.recipient_info["phone"])
        self.go_to_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_HOME_BTN)
        self.home.verify_home()

    def test_03_save_fax_log(self):
        '''
        Descriptions: C31379949
            1.launch the app and navigate to fax history screen
            2.navigate to sent faxes tab
            3.tap on any sent fax
            4.From "Sent Fax Details" screen tap on three dot menu and tap on "Save Fax Log" option
        Expected Result:
            verify that the smart app fax history log should be opened in the PDF viewer screen 
        '''
        _, _ = self.create_sent_fax_job(recipient_phone=self.recipient_info["phone"])
        self.go_to_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_SAVE_LOG_BTN)
        self.preview.verify_preview_screen()

    def test_04_cancel_and_delete_fax(self):
        '''
        Descriptions: C31379948, C31379950
            1.launch the app and navigate to fax history screen
            2.navigate to sent faxes tab
            3.tap on any sent fax
            4.From "Sent Fax Details" screen tap on three dot menu and tap on "Delete this Fax" option
            5.choose delete option from the pop up window
            6.From "Sent Fax Details" screen tap on three dot menu and tap on "Delete this Fax" option 
            7.choose Cancel option from the pop up window 
        Expected Result:
            5.verify that the fax is deleted successfully from the list of sent faxes
            7.verify that the fax is not deleted from the list of sent faxes
        '''
        _, _ = self.create_sent_fax_job(recipient_phone=self.recipient_info["phone"])
        self.go_to_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_DELETE_BTN)
        self.send_fax_details.dismiss_delete_confirmation_popup(is_yes=False)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_DELETE_BTN)
        self.send_fax_details.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()

    def go_to_fax_history(self):
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN, "save_as_draft_popup_exit_bn")
        self.fax_history.verify_fax_history_screen()

    def create_sent_fax_job(self, recipient_phone):
        self.compose_fax.enter_recipient_information(recipient_phone)
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.SCANNER_BTN)
        self.scan.select_scanner_if_first_time_popup_visible()
        if self.scan.verify_coachmark_on_scan_page(self.scan.ADJUST_SCAN_COACH_MARK, raise_e=False):
            self.driver.click_by_coordinates(area="mm")
        assert not self.scan.verify_scan_not_available(), "Scan Not Available message for printer: {}".format(self.p.get_printer_information())
        self.scan.select_scan_job()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.select_add_page()
        self.scan.select_scan_job()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        assert self.preview.get_no_pages_from_preview_label() == 2
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        sleep(5)
        self.compose_fax.verify_compose_fax_screen()
        file_name, number_pages = self.compose_fax.get_added_file_information()
        self.compose_fax.click_send_fax_native_btn()
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.verify_send_fax_status(timeout=600)
        self.send_fax_details.click_back()
        return file_name, number_pages
