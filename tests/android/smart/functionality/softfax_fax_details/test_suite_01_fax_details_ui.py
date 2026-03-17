import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_01_Fax_Details_UI(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_history = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]
        cls.send_fax_details = cls.fc.flow[FLOW_NAMES.SEND_FAX_DETAILS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        # Define variables
        cls.recipient_phone = cls.fc.get_softfax_recipient_info()["phone"]
        cls.recipient_code = cls.fc.get_softfax_recipient_info()["code"]

        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.smart_context = cls.fc.smart_context  
        cls.pkg_name = cls.fc.pkg_name

    def test_01_fax_detail(self):
        """
        Description: C31379947, C31379887, C31379890, C31379891
            1/ Load to Compose Fax with creating new account
            2/ Successfully send fax
            3/ Load Fax History and select this record in Sent tab
        Expected Result:
            3/ Sent Fax Details:
                - title
                - Phone number
                - file name and page number
        """
        file_name, number_page, phone = self.__make_send_fax_job(recipient_phone=self.recipient_phone)
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone, status=self.fax_history.PROCESSING_STATUS)
        self.send_fax_details.verify_phone_number(phone_number="{} {}".format(self.recipient_code, self.recipient_phone))
        self.send_fax_details.verify_time_information(is_successful=False, check_end=False)
        self.send_fax_details.verify_file_information(file_name=file_name, number_page=number_page)

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __make_send_fax_job(self, recipient_phone):
        """
        Make a successful sending fax:
            - Load Compose Fax screen
            - Enter valid information of receiver and sender
            - Add a file (from my photos)
            - Click on Send Fax
            - Verify status of job if is_successful or is_fail. Otherwise, skip this step
            - Click on Back button -> Compose screen
        :return file name, number_pages, and recipient phone number
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=True, check_onboarding=False)
        self.compose_fax.click_add_files_option_btn(self.compose_fax.CAMERA_BTN)
        self.fc.flow_camera_scan_capture_photo(chk_bottom_navbar=False)
        self.preview.verify_title(self.preview.PREVIEW_TITLE)
        self.preview.select_fax_next()
        # There are some test cases failed by No Such context issue, so add timeout for wait_for_context for fixing this issue
        self.driver.wait_for_context(self.smart_context, timeout=20)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.verify_uploaded_file(timeout=30)
        file_name, number_pages = self.compose_fax.get_added_file_information()
        self.compose_fax.enter_recipient_information(recipient_phone)
        phone, _, code = self.compose_fax.get_recipient_information()
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_send_fax()
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_back()
        return file_name, number_pages, "{} {}".format(code, phone)