from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_02_Photo_Edit_Adjust(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    def test_01_adjust_ui(self):
        """
        Description: C17023767, C27151708
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. Click on Adjust button, and select adjust type based on adjust_type value
         4. Do change through scroll bar
         5. Click on Done button

        Expected Results:
         2. Verify Adjust screen with:
            - Title
            - Cancel button
            - Done button
         5. Verify Edit screen, and make sure photo is changed success based on adjust type
        """
        self.fc.load_edit_screen_through_my_photo()
        self.edit.select_edit_main_option(self.edit.ADJUST)
        self.edit.verify_screen_title(self.edit.ADJUST)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        original_img = self.preview.verify_preview_img()
        for adjust_opt in (self.edit.BRIGHTNESS, self.edit.SATURATION, self.edit.CONTRAST, self.edit.CLARITY, self.edit.EXPOSURE,
        self.edit.SHADOWS, self.edit.HIGHLIGHTS, self.edit.WHITES, self.edit.BLACKS, self.edit.TEMPERATURE):
            self.edit.select_edit_child_option(adjust_opt, direction="right", check_end=False, str_id=True)
            self.edit.verify_and_swipe_adjust_slider(direction="left", per_offset=0.25)
            new_img = self.preview.verify_preview_img()
            # verify image changed
            assert saf_misc.img_comp(original_img, new_img) != 0.0, "Adjust type {} doesn't select success".format(adjust_opt)
            original_img=new_img
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()

    @pytest.mark.parametrize("btn_name", ["cancel", "undo"])
    def test_02_adjust_cancel(self, btn_name):
        """
        Description: C27151707, C27152697, C17029644
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. Click on Adjust button
         4. Click on Brightness,do some change
         5. Click on Cancel button

        Expected Results:
         2. Verify Edit screen with photo no any change
        """
        self.fc.load_edit_screen_through_my_photo()
        self.edit.select_edit_main_option(self.edit.ADJUST)
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_child_option(self.edit.BRIGHTNESS, direction="right", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider()
        if btn_name == "cancel":
            self.edit.select_edit_cancel()
            self.edit.verify_edit_page_title()
        else:
            self.edit.select_undo()
            new_image = self.edit.edit_img_screenshot()
            assert(saf_misc.img_comp(current_image, new_image) < 0.06), "Photo should be same with previous one after clicking undo button"