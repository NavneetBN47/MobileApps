from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_05_Photo_Edit_Text(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    def test_01_text_by_fonts_type(self):
        """
        Description: C17023771, C27151982, C17023772, C27152338
         1. Load to Preview screen through My Photos
         2. Click on Edit button
         3. Click on Text button
         4. Click on Done button
         5. Click on Fonts button
         6. Click on each font type
         7. Click on Done button
         
        Expected Results:
         2. Verify Text screen with:
            - Title
            - Cancel button
            - Done button
         6. Verify Edit screen, and make sure photo is changed success based on font type
        """
        self.fc.load_edit_screen_through_my_photo()
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.verify_screen_title(self.edit.TEXT)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.TEXT_FONTS)
        self.edit.verify_screen_title(self.edit.FONTS_TITLE)
        for font_type in (self.edit.ARVO, self.edit.CONCERT, self.edit.COMMIRANT, self.edit.DANCING_SCRIPT, self.edit.MONTSERRAT, self.edit.OLD_STANDARD, self.edit.OSWALD, self.edit.PLAYFAIR_DISPLAY, self.edit.RAKKAS, self.edit.ROBOTO, self.edit.UBUNTU, self.edit.YATRA_ONE):
            self.edit.select_edit_child_option(font_type, direction="right", check_end=False, str_id=True)
            new_image = self.edit.edit_img_screenshot()
            assert (saf_misc.img_comp(current_image, new_image) != 0), "Fonts type {} doesn't select success".format(font_type)
            current_image = new_image
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTION_TITLE)
    
    @pytest.mark.parametrize("btn_name", ["add", "delete", "to_front"])
    def test_02_text_add_text(self, btn_name):
        """
        Description: C27761718, C27761719
         1. Load to Preview screen through My Photos
         2. Click on Edit button
         3. Click on Text button
         4. Type a text, and Click on Done button
         5. If btn_name = "add", then Click on Add Text button "+"
            If btn_name = "delete", then click on Delete button
         6. Click on Done button

        Expected Results:
         6. Make sure all new changes did success on Text Options screen
        """
        self.fc.load_edit_screen_through_my_photo()
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        current_image = self.edit.edit_img_screenshot()
        if btn_name == "add":
            self.edit.select_add_text()
            self.edit.add_txt_string("QAMA Functionality Testing")
            self.edit.select_edit_done()
        elif btn_name == "to_front":
            self.edit.select_to_front()
        else:
            self.edit.select_delete_text()
        new_image = self.edit.edit_img_screenshot()
        if btn_name == "to_front":
            assert(saf_misc.img_comp(current_image, new_image) == 0), "Text shouldn't be changed with to front function"
        else:
            assert(saf_misc.img_comp(current_image, new_image) != 0), "Text didn't add or delete successfully."

    def test_03_color_by_bgcolor(self):
        """
        Description: C17023773, C27152693, C17023774, C27152694
         1. Load to Preview screen through My Photos
         2. Click on Edit button
         3. Click on Text button
         4. Add text, and click on Done button
         5. then Click on BG Color
         6. Click on each BG color
         7.Click on Done button

        Expected Results:
         5. Verify Color Or BG screen with:
            - Title
            - Cancel button
            - Done button
         7. Verify the BG color can change success
        """
        self.fc.load_edit_screen_through_my_photo()
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.TEXT_BGCOLOR)
        self.edit.verify_screen_title(self.edit.TEXT_COLOR)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        for color_type in (self.edit.GRAY, self.edit.BLACK, self.edit.LIGHT_BLUE, self.edit.BLUE, self.edit.PURPLE, self.edit.ORCHID, self.edit.PINK, self.edit.RED, self.edit.ORANGE, self.edit.GOLD, self.edit.YELLOW, self.edit.OLIVE, self.edit.GREEN, self.edit.AQUAMARIN):
            self.edit.select_color(color_type)
            new_image = self.edit.edit_img_screenshot()
            assert (saf_misc.img_comp(current_image, new_image) != 0), "Text BG color {} doesn't select success".format(color_type)
            current_image = new_image
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTION_TITLE)

    def test_04_text_by_color(self):
        """
        Description:
         1. Load to Edit screen through My Photos
         2. Click on Text button
         3. Type a text
         4. Click on Done button
         5. Click on Color button
         6. Do change based on Color
         7. Click on Done button

        Expected Results:
         7. Verify Edit screen, and make sure photo is changed success based on font type
        """
        self.fc.load_edit_screen_through_my_photo()
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.COLOR_BTN)
        for color_type in (self.edit.GRAY, self.edit.BLACK, self.edit.LIGHT_BLUE, self.edit.BLUE, self.edit.PURPLE, self.edit.ORCHID, self.edit.PINK, self.edit.RED, self.edit.ORANGE, self.edit.GOLD, self.edit.YELLOW, self.edit.OLIVE, self.edit.GREEN, self.edit.AQUAMARIN):
            self.edit.select_color(color_type)
            new_image = self.edit.edit_img_screenshot()
            assert (saf_misc.img_comp(current_image, new_image) != 0), "Text color {} doesn't select success".format(color_type)
            current_image = new_image
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTION_TITLE)