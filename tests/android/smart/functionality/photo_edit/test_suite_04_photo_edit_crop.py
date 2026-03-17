from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_04_Photo_Edit_Crop(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    def test_01_crop_photo(self):
        """
        Description:  C17023769, C17023770, C27151941, C27151945, C27151942, C27151943, C17029650
         1. Load to Edit screen through Scan
         2. Click on Crop button
         3. Do change through Crop type
         4. Click on Done button
         
        Expected Results:
         5. Verify Edit screen, and make sure photo is changed success based on document type
        """
        self.fc.load_edit_screen_through_my_photo()
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.CROP)
        self.edit.verify_screen_title(self.edit.CROP)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        #Verify crop flip function on EDIT screen
        self.edit.apply_crop_flip()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        new_after_flip_image = self.edit.edit_img_screenshot()
        assert (saf_misc.img_comp(current_image, new_after_flip_image) != 0), "Image doesn't flip successfully."
        # Verify crop rotate function on EDIT screen
        self.edit.select_edit_main_option(self.edit.CROP)
        self.edit.apply_crop_rotate()
        new_after_rotate_image = self.edit.edit_img_screenshot()
        assert (saf_misc.img_comp(current_image, new_after_rotate_image) != 0), "Image doesn't rotate successfully."
        # Verify crop by sizes function on EDIT screen
        self.edit.select_edit_main_option(self.edit.CROP)
        for crop_size in (self.edit.CUSTOM, self.edit.SQUARE, self.edit.LETTER, self.edit.A4, self.edit.SIZE_5_7,self.edit.SIZE_4_6, self.edit.SIZE_3_5_5):
            self.edit.select_edit_child_option(crop_size, direction="right", check_end=False, str_id=True)
            self.edit.apply_crop_scale_picker()
            new_after_crop_image = self.edit.edit_img_screenshot()
            assert (saf_misc.img_comp(current_image, new_after_crop_image) != 0), "Crop size {} didn't change successfully".format(crop_size)
            current_image = new_after_crop_image
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()