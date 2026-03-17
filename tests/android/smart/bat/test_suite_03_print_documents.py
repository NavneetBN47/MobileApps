from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
import pytest

pytest.app_info = "SMART"

class Test_Suite_03_Print_Documents(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.pdf_fn = TEST_DATA.ONE_PAGE_PDF
        cls.bonjour_name = cls.p.get_printer_information()["bonjour name"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device([cls.pdf_fn])

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    def test_01_print_documents_pdf_share_gmail(self):
        """
        Descriptions: C31297708, C33560115
            1/ Load Home screen
            2/ Connect to target printer
            3/ At Home screen, click on Print Documents tile. If this tile is not enable, then enable it at Personalize screen
            4/ Click on PDF's button on Files screen. Dismiss coach-mark if it displays
            5/ select  "test_file.pdf" by checking the checkbox
            6/ click on Share button
            7/ Go through Share flow to send an email via Gmail

        Expected Result:
            5/ Verify Landing Page
            7/ Verify that the email is sent to Gmail account.

        """
        self.fc.flow_home_load_file_screen(self.p, self.bonjour_name, self.pdf_fn, from_tile=True)
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.fc.flow_preview_share_via_gmail(self.email_address,
                                    "{}".format(self.test_01_print_documents_pdf_share_gmail.__name__),
                                             from_email=self.email_address)

    def test_02_print_documents_pdf_print_trapdoor_ui(self):
        """
        Descriptions:
            1/ Press key back of mobile device. Then, if current scrren is not Files , implement again  step 1 to step 3 of test 01
            2/ Click on Scanned Files button on Files screen. Dismiss coach-mark if it displays
            3/ select  "test_file.jpg" by checking the checkbox
            4/ click Print button
            5/ If App Permission display, dismiss it.
            6/ Make a printing job via HPPS trapddor ui

        Expected Result:
            6/ Verify printing job on:
                - Printer
                - HPPS app via trapdoor ui
        """
        self.fc.reset_app()
        self.fc.flow_home_load_file_screen(self.p, self.bonjour_name, self.pdf_fn, from_tile=True)
        self.fc.flow_preview_make_printing_job(self.p)