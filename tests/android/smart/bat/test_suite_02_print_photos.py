from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
import pytest

pytest.app_info = "SMART"

class Test_Suite_02_Print_Photos(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    def test_01_print_photos_share_gmail(self):
        """
        Description: C31297320, C33560122
            1/ Load Home screen
            2/ Connect to target printer
            3/ At Home screen, click on Print Photos tile (if this tile is invisible, enable it on Personalize screen). Dimiss App Permission popup if it displays.
            4/  At Photos screen, click on My Photos. Then, select a photo at 'Select a Photo' screen.
            5/ Click on Share button
            6/ Go through Share flow to send an email via Gmail

        Expected Result:
            4/ Verify Landing Page
            6/ Verify that the email is sent to Gmail account.

        """
        self.fc.reset_app()
        self.__select_photo_from_home(is_printer=False)
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.fc.flow_preview_share_via_gmail(self.email_address,
                                                  "{}".format(self.test_01_print_photos_share_gmail.__name__),
                                             from_email=self.email_address)

    def test_02_print_photos_print_trapdoor_ui(self):
        """
        Description: C29728521
            1/ Following test 01. If current screen is not Landing Page from test 01,
            then implement agains from step 1 to step 4 of test 01.
            2/ Click Print button
            3/ If App Permission display, dismiss it.
            4/ Make a printing job via HPPS trapdoor ui

        Expected Result:
            4/ Verify printing job on:
                - Printer
                - HPPS app via trapdoor ui

        """
        self.__select_photo_from_home(is_printer=True)
        self.fc.flow_preview_make_printing_job(self.p)

    # -----------------         PRIVATE FUNCTIONS       ---------------------------------
    def __select_photo_from_home(self, is_printer=False):
        """
        From Home screen:
            - Click on Print Photos tile
            - Select a target photo
        End of flow: Landing Page
        """
        self.fc.flow_load_home_screen()
        if is_printer:
            self.fc.flow_home_select_network_printer(self.p)
            self.home.dismiss_print_anywhere_popup()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if not is_printer:
            self.files_photos.verify_limited_access_popup()
            self.files_photos.select_continue_btn()
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.local_photos.select_recent_photo_by_index()
        if self.preview.verify_title(self.preview.PRINT_SIZE_TITLE, raise_e=False):
            self.preview.select_print_size(self.preview.PRINT_SIZE_4x6)