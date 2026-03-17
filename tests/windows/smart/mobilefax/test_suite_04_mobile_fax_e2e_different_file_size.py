import pytest
import logging
from SAF.misc import saf_misc

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "GOTHAM"
class Test_Suite_04_Mobile_Fax_E2E_Different_File_Size(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.mobile_fax = cls.fc.fd["softfax_home"]
        cls.print = cls.fc.fd["print"]
        cls.softfax_landing = cls.fc.fd["softfax_landing"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_06"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        result = cls.driver.ssh.send_command("Test-Path " + w_const.TEST_DATA.TEST_50PAGES_PDF)
        pdf_50pages_path = ma_misc.get_abs_path(w_const.TEST_DATA.TEST_50PAGES_PDF_PATH)
        if "True" not in result["stdout"]: 
            logging.debug("The PDF file was not found! Is being transferred...")
            cls.driver.ssh.send_file(pdf_50pages_path, w_const.TEST_DATA.TEST_50PAGES_PDF)
        else:
            logging.debug("PDF file already exists!")
        cls.fc.go_home()
        cls.fc.sign_in(cls.login_info["email"], cls.login_info["password"])
        cls.fc.select_a_printer(cls.p)

    # @pytest.mark.parametrize('file', [w_const.TEST_DATA.WORM_JPEG, w_const.TEST_DATA.TEST_50PAGES_PDF, w_const.TEST_DATA.CORRUPTED_PDF])
    @pytest.mark.parametrize('file', ["worm_jpeg", "test_50_pages_pdf", "corrupted_pdf"])
    def test_01_send_mobile_fax_with_invalid_information(self, file):
        """
        Click "Mobile Fax" tile on the Main UI
        Select different size of the file from the supported file type
        Max file size is 20MB
        Max page numbers are 50
        Select the file with a format error

        Verify mobile fax sent without any error.
        Verify the correct Error message shows. (Result for step #5)
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17320140
                     https://hp-testrail.external.hp.com/index.php?/cases/view/17361088
                     https://hp-testrail.external.hp.com/index.php?/cases/view/17261137
        """
        file_types ={"worm_jpeg":w_const.TEST_DATA.WORM_JPEG,
        "test_50_pages_pdf":w_const.TEST_DATA.TEST_50PAGES_PDF,
        "corrupted_pdf":w_const.TEST_DATA.CORRUPTED_PDF}
        self.home.select_mobile_fax_tile()
        self.softfax_landing.skip_landing_screen()
        self.mobile_fax.verify_mobile_fax_home_screen()
        self.mobile_fax.select_compose_fax_menu()
        self.mobile_fax.enter_recipient_information(self.recipient_info["phone"])
        self.mobile_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.mobile_fax.click_add_files_option_btn(self.mobile_fax.FILES_PHOTOS_BTN)
        self.print.input_file_name(file_types[file])
        if file == "corrupted_pdf":
            self.mobile_fax.verify_correct_error_screen()
            self.mobile_fax.click_close_btn()
        else:
            self.mobile_fax.verify_add_files_successfully()
            self.mobile_fax.click_send_fax()
            self.mobile_fax.verify_job_is_sending()
            self.mobile_fax.verify_job_sent_successfully()
        self.home.select_navbar_back_btn()
