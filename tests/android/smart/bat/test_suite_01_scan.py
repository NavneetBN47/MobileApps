from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
import pytest

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}

class Test_Suite_01_Scan(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        # Define flows
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.bonjour_name = cls.p.get_printer_information()["bonjour name"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    def test_01_scan_multiple_pages_share_gmail(self):
        """
        Description: C31299782, C33556891, C33556893, C33556899
            1/ Load Home screen
            2/ Connect to target printer and make a scan job for single page with default scan settings
             (If scan tile is not on Home screen, then enable it in Personalize screen)
            3/ At Preview, add 1 more page via Add icon button
            4/ At Preview, click on Share btn on bottom navigation
            5/ Rename file name, toggle pdf on, click on bottom button
            6/ Go through Share flow to send an email via Gmail
        Expected Result:
            3/ Verify Preview:
                 - Navigation bar: Back, Edit, and 3dots icon buttons, and  Preview title
                 - There are at least 3 icons at bottom navigation bar
                 - Total page is "2"
            4/ Share Option screen display
            6/ Verify that the email is sent to Gmail account.
        """
        file_name = self.test_01_scan_multiple_pages_share_gmail.__name__
        self.fc.flow_home_scan_single_page(self.p, from_tile=True)
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_top_toolbar_btn(self.preview.ADD_BTN)
        self.scan.verify_scan_screen(source=self.scan.SOURCE_PRINTER_SCAN_OPT)
        self.scan.start_capture()
        self.scan.verify_successful_scan_job()
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        assert self.preview.verify_preview_page_info()[1] == 2, "Page count should be two"
        self.preview.verify_bottom_nav(btns=[self.preview.SHARE_BTN, self.preview.SAVE_BTN, self.preview.PRINT_PREVIEW_BTN])
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.preview.verify_title(self.preview.SHARE_TITLE)
        self.preview.verify_action_screen()
        self.preview.select_file_type(self.preview.BASIC_PDF)
        self.preview.rename_file(file_name)
        self.preview.select_action_btn()
        self.fc.flow_preview_share_via_gmail(self.email_address, "{}".format(file_name), from_email=self.email_address)

    def test_02_scan_print_trapdoor_ui(self):
        """
        Description: C31297390
            1/ If current screen is not Preview from test 02, implement 2 first steps of test 02
            2/ At Preview, click on Print button on bottom navigation bar
            3/ If App Permission display, dismiss it.
            4/ Make a printing job via HPPS trapddor ui

        Expected Result:
            4/ Verify printing job on:
                - Printer
                - HPPS app via trapdoor ui
        """
        #reset app to make sure the app can detect printer status correctly--CR AIOA-15118
        self.fc.reset_app()
        self.fc.flow_home_scan_single_page(self.p, from_tile=True)
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.fc.flow_preview_make_printing_job(self.p)

    def test_03_scan_pdf_save(self):
        """
        Description:
            1/ Continue test 03 by pressing Back key of mobile device.  If current screen is not Preview from test 02, implement 2 first steps of test 02
            2/ At Preview, click on Save button on bottom navigation bar
            3/ Rename file name, toggle pdf on, click on bottom button
            4/ Wait for toast message invisible

        Expected Result:
            2/ Save Option screen display
            4/ Verify Preview
        """
        # reset app to make sure the app can detect printer status correctly--CR AIOA-15118
        self.fc.reset_app()
        file_name = self.test_03_scan_pdf_save.__name__
        self.fc.flow_home_scan_single_page(self.p, from_tile=True)
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.select_file_type(self.preview.BASIC_PDF)
        self.preview.rename_file(file_name)
        self.preview.select_action_btn()
        self.local_files.save_file_to_downloads_folder(file_name)
        self.preview.dismiss_file_saved_popup()
        self.preview.verify_preview_screen()
        self.fc.verify_existed_file("{}/{}.pdf".format(TEST_DATA.MOBILE_DOWNLOAD, file_name))

    def test_04_scan_jpg_save(self):
        """
        Description: C31297329
            Save as test 04, but on Save Option screen, toggle pdf off

        Expected Result:
            2/ Save Option screen display
            4/ Verify Preview:
        """
        # reset app to make sure the app can detect printer status correctly--CR AIOA-15118
        self.fc.reset_app()
        file_name = self.test_04_scan_jpg_save.__name__
        self.fc.flow_home_scan_single_page(self.p, from_tile=True)
        self.scan.select_adjust_next_btn()
        self.preview.verify_preview_screen()
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.select_file_type(self.preview.IMAGE_JPG)
        self.preview.rename_file(file_name)
        self.preview.select_action_btn()
        self.preview.dismiss_file_saved_popup()
        self.preview.verify_preview_screen()
        self.fc.verify_existed_file("{}/{}.jpg".format(TEST_DATA.MOBILE_PICTURES, file_name))