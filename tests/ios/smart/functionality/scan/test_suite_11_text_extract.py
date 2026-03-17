import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_11_Text_Extract(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.p = load_printers_session
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.scan = cls.fc.flow["scan"]
        cls.camera = cls.fc.flow["camera"]
        cls.text_extract = cls.fc.flow["text_extract"]
        cls.common_preview = cls.fc.flow["common_preview"]
        cls.photos = cls.fc.flow["photos"]
        ma_misc.get_hpid_account_info(stack=request.config.getoption("--stack"), a_type="hp+", instant_ink=True, driver=cls.driver)
        cls.fc.go_home(stack=request.config.getoption("--stack"))

    @pytest.mark.parametrize("source", ["camera", "scanner"])
    def test_01_text_extract_from_scan(self, source):
        """
        Description: C31299598, C31299599, C31299601 & C31299619
         1. Load Scan or Camera Scan
         2. Select Text Extract mode
         3. Capture Image
         4. Select Continue button
        Expected Results:
         3. Verify Text Extract continue screen
         4. Verify Text Extract screen
        """
        self.fc.load_text_extract(printer=self.p if source == "scanner" else None)
    
    @pytest.mark.parametrize("img_count", [1, 3])
    def test_02_text_extract_from_preview(self, img_count):
        """
        Description: C31299622, C31299621 & C31299620
         1. Load Camera Scan
         2. Select Document mode
         3. Capture 1 or 3 images
         4. Select Text Extract on Top Toolbar
         5. Select Continue button
        Expected Results:
         5. Verify Extracted Text screen
        """
        self.fc.load_text_extract(from_preview=True, pages=img_count)
    
    def test_03_text_extract_language(self):
        """
        Description: C31299600
         1. Load Camera Scan
         2. Select Text Extract mode
         3. Capture an image
         4. Select Language option
        Expected Results:
         4. Verify Language screen
        """
        self.fc.load_text_extract(to_text_edit=False)
        self.common_preview.select_language_btn()
        self.common_preview.verify_selected_language()
    
    def test_04_share_file_types(self):
        """
        Description: C31299614
         1. Load Camera Scan
         2. Select Text Extract mode
         3. Capture an image
         4. Select Continue
         5. Select Done
         6. Select Share/Save
         7. Select File Types
        Expected Results:
         7. Verify JPG, Basic PDF,Searchable PDF, DOCX and TXT file types
        """
        self.fc.load_text_extract()
        self.text_extract.select_done()
        self.common_preview.dismiss_feedback_popup()
        self.common_preview.select_bottom_nav_btn(self.common_preview.SHARE_SAVE_TITLE)
        self.common_preview.select_file_type()
        self.common_preview.verify_file_types([self.common_preview.IMAGE_JPG, self.common_preview.BASIC_PDF, self.common_preview.SEARCHABLE_PDF, self.common_preview.WORD_DOCUMENT, self.common_preview.PLAIN_TXT])

    def test_05_copy_all(self):
        """
        Description: C31299610
         1. Load Camera Scan
         2. Select Text Extract mode
         3. Capture an image
         4. Select Continue
         5. Select Copy All button
        Expected Results:
         5. Verify "Text copied to clipboard" popup
        """
        clipboard_txt = "placeholder text, this should be replaced"
        self.driver.wdvr.set_clipboard_text(clipboard_txt)
        self.fc.load_text_extract()
        self.text_extract.select_copy_all()
        self.text_extract.verify_text_copied_popup()
        assert self.driver.wdvr.get_clipboard_text() != clipboard_txt, "Clipboard text should have changed"