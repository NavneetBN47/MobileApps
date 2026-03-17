from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from time import strftime

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}


class Test_Suite_06_Scan_OCR(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define flows
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.system_flow = cls.fc.flow[FLOW_NAMES.SYSTEM_FLOW]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    @pytest.mark.parametrize('state',
    [('SEARCHABLE_PDF','SCAN','NOT_SMART_FILE','NOT_SAVE_ORIG'),
    ('WORD_DOCUMENT','SCAN','NOT_SMART_FILE','_NOT_SAVE_ORIG'),
    ('PLAIN_TXT','SCAN','NOT_SMART_FILE','NOT_SAVE_ORIG'),    
    ('SEARCHABLE_PDF','SCAN','SMART_FILE','NOT_SAVE_ORIG'),
    ('WORD_DOCUMENT','SCAN','SMART_FILE','_NOT_SAVE_ORIG'),
    ('PLAIN_TXT','SCAN','SMART_FILE','NOT_SAVE_ORIG')])
    def test_01_scan_to_editable_file(self,state):
        """
        Description: C31299469, C31299593, C31299591, C31299590, C31299516, C31299594, C31299530, C31299595, C31299470, C31299485, C31299588
        1. Launch the app
        2. Sign in to your account
        3. Navigate to app home screen
        4. Tap on scan tile > select Document option
        5. Take a scan
        6. Tap on 'Next' in Detect Edges page
        7. On the Preview Page, tap on the Share/Save button
        8. Tap on File type in Share Option page
        9. (skip) Get to "Save Document As" page
        10. Tap on any option under Convert to Text section (ex. Searchable PDF)
        11. Get to 'Convert to Text' page
        12. (skip) Make sure "Save Original to HP Smart Files" is enabled by default
        13. Tap on "Destination" button > select destination > tap on "<" button
        14. Tap on "Create File" button
        15. Tap on "Home" button on pop up
        16. Get to home page
        17. Tap on "View&Print" button
        18. Click on PDFs in the files & Photos
        19. Observe
        For Android:
        Note:
        Step 8: Tap on File type in Share Option page
        Step 9 is not there: Save Document as page is not there for android
        Step 12 is not there: Selection destination type functionality has been removed from Android
        Step 18: Click on PDFs in the files & Photos
        Verify file can be found in HP Smart Files folder
        """
        filenamebase = "OCR_Test_"+strftime("%M_%S")
        filename = ""
        docs = dict()
        docs['SEARCHABLE_PDF']=(self.preview.SEARCHABLE_PDF,filenamebase+".pdf",filename+".pdf")
        docs['WORD_DOCUMENT']=(self.preview.WORD_DOCUMENT,filenamebase+".docx",filename+".docx")
        docs['PLAIN_TXT']=(self.preview.PLAIN_TXT,filenamebase+".txt",filename+".txt")
        self.fc.reset_app()
        self.fc.flow_home_scan_single_page(self.p, from_tile=True, mode="document", verify_signin=False)
        self.scan.select_adjust_next_btn()
        self.preview.verify_bottom_nav([self.preview.SAVE_BTN, self.preview.SHARE_BTN])
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.verify_title(self.preview.SAVE_TITLE)
        self.preview.select_file_type(file_type=docs[state[0]][0]) # Select file type
        self.driver.wait_for_object("selected_language_txt",invisible=True)
        self.preview.toggle_save_to_hp_smart(enable=False)
        assert (self.driver.wait_for_object("pdf_password_switch", raise_e=False) == False)
        if state[2] != 'SMART_FILE':
            self.preview.rename_file(filenamebase)
        self.preview.select_action_btn()
        self.preview.dismiss_file_saved_popup()
        self.local_files.select_save_btn()
        self.preview.select_exit_popup_btn("home")
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_local_files_photos_btns()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        if state[2] == "SMART_FILE":
            self.fc.verify_existed_file(docs[state[0]][2])
        else:
            self.fc.verify_existed_file(docs[state[0]][1])