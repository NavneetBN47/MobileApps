import logging
from datetime import datetime

import pytest

from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA


pytest.app_info = "SMART"


class Test_Suite_08_Preview_PDF_Password(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]

        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=False, pro=True)

        def clean_up_class():
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)


    @pytest.mark.parametrize("screen", ["share", "save"])
    def test_01_pdf_password(self, screen):
        """
        Description: C31299650, C31299651, C31299652, C31299658, C31299659, C31299660, C31299661, C31299653, C31299665, C31299654, C31299662
         1. Sign in with hp+ pro account
         2. Load preview screen through scanner
         3. Select Share/Save depending on screen param
         4. Select Basic PDF File Type
         5. Toggle "Add password protection" switch
         6. Enter a password < 6 characters long and select action button
         7. Enter a password < 6 characters long with spaces and select action button
         8. Enter a password > 32 characters long and select action button
         9. Enter a password > 32 characters long with spaces and select action button
         10. Enter a password between 6 and 32 characters long with spaces and select action button
         11. Enter a valid password (between 6 and 32 characters without spaces) and select action button
         12. Save/Share file
        Expected Results:
         3. Verify PDF Password protection switch is invisible
         4. Verify PDF Password protection switch is visible and disabled
         5. Verify Password edit text appears
         6. Verify short password text
         7. Verify short password with spaces text
         8. Verify long password text
         9. Verify long password with spaces text
         10. Verify password with spaces text
         12. Verify saved file exists
        """
        file_name = "{}_{}_{}".format(self.test_01_pdf_password.__name__, screen, datetime.now().strftime("%-m-%d-%Y_%H-%M-%S"))
        file_path = "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, file_name + ".pdf")
        valid_pwd = "abc123456789"
        invalid_pwds = {
            self.preview.SHORT_PWD_HINT: "abc12",
            self.preview.SHORT_PWD_SPACES_HINT: "ab 12",
            self.preview.LONG_PWD_HINT: "abcdefghijklmnopqrstuvwxyz123456789",
            self.preview.LONG_PWD_SPACES_HINT: "abcde fghijklmnopqrstuv wxyz123456789",
            self.preview.PWD_SPACES_HINT: "abcdefg 1234"
        }
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_scan_single_page(self.p, from_tile=False, mode="document")
        self.scan.select_adjust_next_btn()
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN if screen == "save" else self.preview.SHARE_BTN)
        self.preview.rename_file(file_name)
        self.preview.select_file_type(self.preview.BASIC_PDF)
        self.preview.verify_pdf_password(enabled=False)
        self.preview.toggle_pdf_password()
        for pwd_type, pwd in invalid_pwds.items():
            self.preview.enter_pdf_password(pwd)
            self.preview.select_action_btn(change_check=None)
            self.preview.verify_hint(message=pwd_type)
            logging.info("Verified proper message for {} password".format(pwd_type))
        self.preview.enter_pdf_password(valid_pwd)
        self.preview.select_action_btn()
        if screen == "save":
            self.local_files.save_file_to_downloads_folder(file_name)
            assert self.fc.verify_existed_file(file_path), "File {} was not created".format(file_path)
        else:
            self.fc.flow_preview_share_via_gmail("qa.mobiauto@gmail.com", "{}_{}".format(file_name, self.driver.driver_info["desired"]["udid"]))