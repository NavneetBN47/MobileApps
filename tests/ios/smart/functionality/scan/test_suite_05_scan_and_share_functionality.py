import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import TEST_DATA

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_05_Scan_And_Share_Funct(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.files = cls.fc.fd["files"]
        cls.share = cls.fc.fd["share"]
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_info = cls.p.get_printer_information()
        cls.stack = request.config.getoption("--stack")
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"]["username"]
        cls.fc.go_home(stack=cls.stack, create_account=True)
        def delete_all_hp_smart_files():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(delete_all_hp_smart_files)

    def test_02_verify_save_share_scan_photo_option(self):
        """
        Scan image, validate default type photo is jpg, change file name in share/save screen, save and
        verify image saved accordingly in jpg format- C31297329
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip test on MAC")
        self.fc.navigate_to_share_save_screen(self.p, option="Photo")
        assert self.common_preview.verify_file_type_selected("jpg")
        self.fc.save_file_to_hp_smart_files_and_go_home("default_photo_type", self.common_preview.SHARE_SAVE_TITLE)
        self.fc.go_hp_smart_files_screen_from_home()
        self.files.verify_file_name_exists("default_photo_type.jpg")

    def test_03_verify_save_share_scan_doc_option(self):
        """
        C31297715 - Verify pop up when saving PDF file
        C31297716 - Scan image, validate default type document is pdf, change file name in share/save screen, save and
        verify image saved accordingly in pdf format
        """
        self.fc.navigate_to_share_save_screen(self.p, option="Document")
        assert self.common_preview.verify_file_type_selected("Basic PDF")
        btn = self.common_preview.SHARE_SAVE_TITLE if pytest.platform == "IOS" else self.common_preview.SHARE_BTN
        self.fc.save_file_to_hp_smart_files_and_go_home("default_doc_type", btn, file_type="PDF")
        self.fc.go_hp_smart_files_screen_from_home()
        self.files.verify_file_name_exists("default_doc_type.pdf")

    def test_06_validate_scan_and_share_email(self):
        """
        IOS & MAC:
        Scan image as type=pdf and verify share to email - C31297708
        """
        self.fc.navigate_to_share_save_screen(self.p)
        if pytest.platform == "IOS":
            self.common_preview.select_button(self.common_preview.SHARE_SAVE_BTN)
            self.share.select_gmail()
        else:
            self.common_preview.verify_an_element_and_click(self.common_preview.CONTINUE_BUTTON)
            self.share.select_mail()
        self.fc.send_and_verify_email(from_email_id=self.email_address, to_email_id=self.email_address,
                                      subject="scan_type_pdf_share")