from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_01_Novelli_Edit_Templates(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        if "novelli" not in cls.p.p_obj.projectName:
            pytest.skip("Novelli printer is unavailable for testing this time")

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.COMMON_PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]

        # Define the variable
        cls.bonjour_name = cls.p.get_printer_information()["bonjour name"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    @pytest.mark.parametrize("screen_type", ["front_btn", "back_btn"])
    def test_01_verify_edit_front_back_templates_screen(self, screen_type):
        """
        Description: C29777666, C29777675, C29718804, C29777772, C29718798, C29777773, C29718800, C29707845, C29810662, C29810664, C29810667
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon. If screen type == "back_btn", then choose Back button -> 3 dot icon -> Edit button
         6. CliCK on Edit button
         7. Click on Templates button
         8. Select any option from Templates button
         9. Click on Done button
         10. Click on Done button
    
        Expected Result:
         7. Verify Templates screen
         8. Templates can be selected success
         10. Verify Two-Sided Preview screen through:
            + Title
            + Front button
            + Back button
            + Print and Save button
        """
        template_options = [self.edit.VALENTINES_TEMPLATE, self.edit.BIRTHDAY_TEMPLATE, self.edit.CHILDREN_TEMPLATE, self.edit.WEDDING_TEMPLATE, self.edit.NEW_YEAR_TEMPLATE, self.edit.CHRISTMAS_TEMPLATE, self.edit.DIWALI_TEMPLATE, self.edit.HANUKKAH_TEMPLATE]
        self.fc.load_edit_screen_for_novelli(self.p, self.bonjour_name, self.edit.TEMPLATE, is_back_screen=screen_type == "back_btn")
        current_image = self.edit.edit_img_screenshot()
        for template in template_options:
            self.edit.select_templates_type(template)
            new_image = self.edit.edit_img_screenshot()
            assert(saf_misc.img_comp(current_image, new_image) != 0.0), "template doesn't choose success"
        for i in range(3):
            self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()

    def test_02_verify_edit_front_templates_replace_function(self):
        """
         Description: C29718799, C29870954
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon
         6. CliCK on Edit button
         7. Click on Templates button
         8. Select any option from Templates button
         9. Click on Done button
         10. Click on Replace button
         11. Select another option from Templates screen

         Expected Result:
         11. Templates can be changed success
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.bonjour_name, self.edit.TEMPLATE, is_back_screen=False)
        self.edit.select_templates_type(self.edit.VALENTINES_TEMPLATE)
        self.edit.select_edit_done()
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_done()
        self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()
        self.preview.select_page_options_btn(self, btn=self.preview.EDIT_BTN)
        self.edit.verify_edit_page_title()
        self.edit.select_edit_main_option(self.edit.TEMPLATE)
        self.edit.select_replace_btn()
        self.edit.select_templates_type(self.edit.BIRTHDAY_TEMPLATE)
        self.edit.select_edit_done()
        new_image = self.edit.edit_img_screenshot()
        assert(saf_misc.img_comp(current_image, new_image) != 0.0), "template doesn't replace success"

    def test_03_verify_edit_front_templates_exit_function(self):
        """
         Description: C29718803
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon
         6. CliCK on Edit button
         7. Click on Templates button
         8. Select any option from Templates button
         9. Click on X button

         Expected Result:
         9. Template doesn't change success
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.bonjour_name, self.edit.TEMPLATE, is_back_screen=False)
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_templates_type(self.edit.VALENTINES_TEMPLATE)
        self.edit.select_undo()
        new_image = self.edit.edit_img_screenshot()
        assert(saf_misc.img_comp(current_image, new_image) == 0.0), "template doesn't undo success"

    @pytest.mark.parametrize("markup_item", ["highlight", "white_out", "black_pen", "blue_pen", "red_pen"])
    def test_04_verify_edit_front_markup_function(self, markup_item):
        """
         Description: C29870953
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon
         6. CliCK on Edit button
         7. Click on Markup item
         8. Select any option from Markup screen
         9. Click on Done button
         10. Click on Replace  button
         11. Select any other markup option
         12. Click on Done button
    
         Expected Result:
         11. Replace function works
         12. Verify Two-Sided Preview screen through:
            + Title
            + Front button
            + Back button
            + Print and Save button
        """
        markup_items = {"highlight": self.edit.HIGHLIGHT_OPTION,
                      "white_out": self.edit.WHITE_OUT_OPTION,
                      "black_pen": self.edit.BLACK_PEN_OPTION,
                        "blue_pen": self.edit.BLUE_PEN_OPTION,
                        "red_pen": self.edit.RED_PEN_OPTION}
        self.fc.load_edit_screen_for_novelli(self.p, self.bonjour_name, self.edit.MARKUP, is_back_screen=False)
        self.edit.select_edit_child_option(markup_items[markup_item], direction="right", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider("right", 0.7)
        self.edit.select_edit_done()
        self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()