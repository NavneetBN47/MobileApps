from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_03_Photo_Edit_Filters(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    def test_01_filters_by_document_type(self):
        """
        Description: C17023768, C27151711, C27151712
         1. Load to Preview screen through My Photos
         2. Click on Edit button
         3. Click on Filters button
         4. Click on Document
         5. Do change through Document type
         6. Click on Done button

        Expected Results:
         3. Verify Filter screen with:
            - Title
            - Cancel button
            - Done button
         6. Verify Edit screen, and make sure photo is changed success based on document type
        """
        self.fc.load_edit_screen_through_my_photo()
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.select_edit_main_option(self.edit.FILTERS)
        self.edit.verify_screen_title(self.edit.FILTERS)
        self.edit.select_edit_main_option(self.edit.FILTER_DOCUMENT)
        for document_type in (self.edit.BW, self.edit.BW2, self.edit.GREYSCALE, self.edit.ALABASTER):
            original_img = self.preview.verify_preview_img()
            self.edit.select_edit_child_option(document_type, direction="left", check_end=False, str_id=True)
            self.edit.verify_and_swipe_adjust_slider(per_offset=0.15)
            new_image = self.edit.edit_img_screenshot()
            assert (saf_misc.img_comp(original_img, new_image) != 0), "Filters document type {} didn't change successfully".format(document_type)
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()

    def test_02_filters_photo_by_photo(self):
        """
        Description: C27151939, C27151940
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. Click on Filters button
         4. Click on Photo,do some change
         5. Click on Done button

        Expected Results:
         5. Verify Edit screen, and make sure photo is changed success based on photo type
        """
        self.fc.load_edit_screen_through_my_photo()
        self.edit.select_edit_main_option(self.edit.FILTERS)
        self.edit.select_edit_main_option(self.edit.FILTER_PHOTO)
        current_image = self.edit.edit_img_screenshot()
        for photo_type in (self.edit.SUMMER, self.edit.AURORA, self.edit.ULTRAVIOLET, self.edit.INK_STAINS, self.edit.ALABASTER, self.edit.DUSK, self.edit.NOIR, self.edit.DAYDREAM, self.edit.EMBERS, self.edit.MOONLIGHT, self.edit.SNOWSHINE, self.edit.ATMOSPHERIC, self.edit.HONEYBEE, self.edit.FIRESIDE, self.edit.GLACIAL, self.edit.SAUNA, self.edit.SEAFARER, self.edit.CAMEMO, self.edit.TIMEWORN, self.edit.SUNLIGHT):
            self.edit.select_edit_child_option(photo_type, direction="right", check_end=False, str_id=True)
            self.edit.verify_and_swipe_adjust_slider(direction="right", per_offset=0.25)
            new_image = self.edit.edit_img_screenshot()
            assert (saf_misc.img_comp(current_image, new_image) != 0), "Filters photo type {} didn't change successfully".format(photo_type)
            current_image = new_image
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()