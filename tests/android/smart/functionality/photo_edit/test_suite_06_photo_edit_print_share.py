from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"

class Test_Suite_06_Photo_Edit_Print_Share(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    def test_01_add_edit_print_photos(self):
        """
        Description: C27152696, C17029648
            1. Launch the Smart app
            2. Scan or Select single and proceed to the landing screen
            3. Perform some edits on the images (crop, text, color change etc)
            4. Tap on Done to save the edit changes.
            5. Submit a print job
         
        Expected Results:
            Verify that the print job is successful with all the edit changes and the print matches the preview
        """
        self.fc.load_edit_screen_through_my_photo(self.p)
        original_img = self.preview.verify_preview_img()
        # perform edits
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.add_txt_string("QAMATest")
        self.edit.select_edit_done()
        self.edit.select_edit_main_option(self.edit.COLOR_BTN)
        self.edit.select_color(self.edit.GRAY)
        self.edit.select_edit_done() # Finished color Selection
        self.edit.select_edit_done() # Finished color button selection
        self.edit.select_edit_done() # Finished edits
        # verify image changed
        assert saf_misc.img_comp(original_img, self.preview.verify_preview_img()) > 0.01, "Preview image should not match original image"
        self.fc.flow_preview_make_printing_job(self.p)

    def test_02_photos_share_gmail(self):
        """
        C28299202
        Description:
            1. Navigate to Home Screen
            2. Tap on the "Camera Scan" Tile Or select a photo from MY Photo screen
            3. From Adjust Boundaries Screen, Tap on Next
            4. From the Preview screen, tap anywhere on the photo to edit.
            5. Perform the below actions on the clicked photo:
                a.) Edit a photo
                b.) Apply a filter
                c.) Add some adjustments (brightness, contrast, etc) e.) Add text
            6. After performing the above actions, tap on "Done"
            7. Go back to Files and Photos Screen
            8. Select the same Photo/ File
            9. From the preview Screen, tap on the Photo/file
            10. Observe
            11. Share the Photo/ File using Gmail, PSP, Save to Drive, Messages, Blue Tooth
            12. Observe
        NOTE: Perform the same steps (Step 3 - Step 12) for Printer Scan
        """
        self.fc.load_edit_screen_through_my_photo()
        # Filter image
        self.edit.select_edit_main_option(self.edit.FILTERS)
        self.edit.select_edit_main_option(self.edit.FILTER_PHOTO)
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_child_option(self.edit.SUMMER, direction="right", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider(direction="right", per_offset=0.25)
        new_image = self.edit.edit_img_screenshot()
        assert (saf_misc.img_comp(current_image, new_image) != 0), "Filters photo type didn't change successfully"
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        # Adjust image
        self.edit.select_edit_main_option(self.edit.ADJUST)
        self.edit.verify_screen_title(self.edit.ADJUST)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        original_img = self.preview.verify_preview_img()
        self.edit.select_edit_child_option(self.edit.BRIGHTNESS, direction="right", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider(direction="left", per_offset=0.25)
        new_img = self.preview.verify_preview_img()
        # verify image changed
        assert saf_misc.img_comp(original_img, new_img) != 0.0, "Adjust type doesn't select success"
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        self.edit.select_edit_done() # done editing
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.fc.flow_preview_share_via_gmail(self.email_address,
                                                  "{}".format(self.test_02_photos_share_gmail.__name__),
                                             from_email=self.email_address)