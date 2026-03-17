from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_Photo_Edit(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]

        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    @pytest.mark.parametrize("img_source", ["scanner", "camera"])
    def test_01_photo_edit_ui(self, img_source):
        """
        Description: C31299863, C31299883, C31299857, C31297720, C17023765
         1. Load to Preview screen through Camera Scan or Scanner
         2. Click on Edit button
         
        Expected Results:
         2. Verify Edit screen with:
            - Title
            - Cancel button
            - Done button
            - Adjust / Filters / Crop / Text displays
        """
        if img_source == "camera":
            self.fc.reset_app()
            self.fc.load_edit_screen_through_camera_scan()
        else:
            self.fc.flow_home_load_scan_screen(self.p, from_tile=False)
            self.scan.start_capture()
            self.scan.verify_successful_scan_job()
            self.scan.select_adjust_next_btn()
            self.preview.verify_preview_screen()
            self.preview.select_page_options_btn(btn=self.preview.EDIT_BTN)
            self.home.check_run_time_permission()
        self.edit.verify_edit_ui_elements(self.edit.EDIT_OPTIONS)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        
    @pytest.mark.parametrize("btn_name", ["cancel", "done"])
    def test_02_edit_cancel(self, btn_name):
        """
        Description:
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. If btn_name == "cancel": Click on Cancel button
            If btn_name == "done": Click on Done button
         
        Expected Results:
         3. Verify Preview screen
        """
        self.fc.load_edit_screen_through_my_photo()
        if btn_name == "cancel":
            self.edit.select_edit_cancel()
        else:
            self.edit.select_edit_done()
        self.preview.verify_preview_screen()
        
    @pytest.mark.parametrize("btn_name", ["yes", "no"])
    def test_03_discard_edits(self, btn_name):
        """
        Description: C17029645, C17029647, C17029646
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. Click on Adjust, and do some change on Brightness
         4. Click on Done button
         5. Click on Cancel button
         6. If btn_name == yes, then click on Yes button
            If btn_name == no, then click on No button

        Expected Results:
         5. Verify Discard Edits? popup with:
            - Title
            - Yes and No button
         6. If btn_name == yes, then verify Preview screen
            If btn_name == no, then verify Edit screen
        """
        self.fc.load_edit_screen_through_my_photo()
        self.edit.select_edit_main_option(self.edit.ADJUST)
        self.edit.select_edit_child_option(self.edit.BRIGHTNESS, direction="right", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        self.edit.select_edit_cancel()
        self.edit.verify_discard_edits_screen()
        if btn_name == "yes":
            self.edit.select_discard_changes_btn(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS[2])
            self.preview.verify_preview_screen()
        else:
            self.edit.select_discard_changes_btn(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS[3])
            self.edit.verify_edit_page_title()
