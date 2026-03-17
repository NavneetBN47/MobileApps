import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_02_Menu(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_history = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]
        cls.send_fax_details = cls.fc.flow[FLOW_NAMES.SEND_FAX_DETAILS]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

        # Define variables
        cls.recipient_phone = cls.fc.get_softfax_recipient_info()["phone"]
        cls.recipient_code = cls.fc.get_softfax_recipient_info()["code"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    def test_01_cancel_deleting_fax(self):
        """
        Description: C31379900, C31379903, C31379948, C31379950
            1/ Load to Compose Fax with creating new account
            2/ Start a sending job
            3/ Load Fax History and select processing job
            4/ Click 3 dots menu button -> click on Delete this fax button
            5/ Click Cancel button on Are you sure? popup
            6/ Click 3 dots menu button -> click on Delete this fax button
            7/ Click Delete button on Are you sure? popup
        Expected Result:
            5/ Sent Fax Details:
                - title
                - Phone number
                - file name and page number
            7/ Fax History
        """
        self.__make_send_fax_job(recipient_phone=self.recipient_phone, check_onboarding=False)
        self.__load_fax_details_screen(self.recipient_phone)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_DELETE_BTN)
        self.send_fax_details.dismiss_delete_confirmation_popup(is_yes=False)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.verify_phone_number(phone_number="{} {}".format(self.recipient_code, self.recipient_phone))
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_DELETE_BTN)
        self.send_fax_details.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()

    def test_02_save_fax_log(self):
        """
        Description:C31379901, C31379949
            1/ Load to Compose Fax with creating new account
            2/ Start a sending job
            3/ Load Fax History and select processing job
            4/ Click 3 dots menu button
            5/ Click on Save Fax log
        Expected Result:
            5/ Save fax log is invisible
        """
        self.__make_send_fax_job(recipient_phone=self.recipient_phone, check_onboarding=False)
        self.__load_fax_details_screen(self.recipient_phone)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_SAVE_LOG_BTN)
        self.send_fax_details.verify_menu_save_fax_log(invisible=True)

    def test_03_edit_forward(self):
        """
        Description: C31379893
            1/ Load to Compose Fax with creating new account
            2/ Start a sending job
            3/ Load Fax History and select processing job
            4/ Click 3 dots menu button
            5/ Click on Edit and Forward button
        Expected Result:
            5/ Compose Fax
        """
        self.__make_send_fax_job(recipient_phone=self.recipient_phone, check_onboarding=False)
        self.__load_fax_details_screen(self.recipient_phone)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_EDIT_FORWARD_BTN)
        self.compose_fax.verify_compose_fax_screen()

    def test_04_print_confirmation_home(self):
        """
        Description: C31379888, C31379899, C31379902, C31379951
            1. Load to Compose Fax with creating new account
            2. Start a sending job
            3. Load Fax History and select a job
            4. Click on Home button

        Expected Result:
            4. Verify Home screen
        """
        self.__make_send_fax_job(recipient_phone=self.recipient_phone, check_onboarding=False)
        self.__load_fax_details_screen(self.recipient_phone)
        self.send_fax_details.click_bottom_button(self.send_fax_details.HOME_BTN)
        self.home.verify_home_nav()

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __load_fax_details_screen(self, phone):
        """
        From Compose Fax, load Fax Details screen via Fax History
                - Load Compose Fax screen
                - CLick on Fax History on menu
                - Select target record
        """
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone,
                                               status=self.fax_history.PROCESSING_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()

    def __make_send_fax_job(self, recipient_phone, check_onboarding=True):
        """
        Make a successful sending fax:
            - Load Compose Fax screen
            - Enter valid information of receiver and sender
            - Add a file (from camera scan)
            - Click on Send Fax
            - Verify status of job if is_successful or is_fail. Otherwise, skip this step
            - Click on Back button -> Compose screen
        :return recipient phone number
        """
        #Make sure compose fax screen is empty, not affect by previous test
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=True,
                                                  check_onboarding=check_onboarding)
        self.fc.make_send_fax_job(recipient_phone, self.sender_info["name"], self.sender_info["phone"])
        self.send_fax_details.click_back()