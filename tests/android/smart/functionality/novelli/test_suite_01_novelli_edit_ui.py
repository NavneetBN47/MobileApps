from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_Novelli_Edit_UI(object):
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

        #Define the variable
        cls.bonjour_name = cls.p.get_printer_information()["bonjour name"]
        cls.fc.set_hpid_account("hp+", claimable=False, ii_status=True, smart_advance=True)

    @pytest.mark.parametrize("item_name", ["adjust", "crop", "filter"])
    def test_01_verify_edit_front_adjust_function(self, item_name):
        """
         Description: C29136374, C29141318, C29142869, C29142870, C29142871, C29142878
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon
         6. CliCK on Edit button
         7. If item_name == "adjust", Click on Adjust item
            If item_name == "crop", Click on Crop item
            If item_name == "filters", Click on Filters item
         8. If item_name == "adjust", Select any option from Adjust screen
            If item_name == "crop", Select any option from Crop screen
            If item_name == "filters",Select any option from Filters screen
         9. Click on Done button
         10. Click on Done button

         Expected Result:
         6. Verify Front Edit screen:
         10. Verify Two-Sided Preview screen through:
            + Title
            + Front button
            + Back button
            + Print and Save button
        """
        items_name = {"adjust": self.edit.ADJUST,
                        "crop": self.edit.CROP,
                        "filter": self.edit.FILTERS}
        self.fc.load_edit_screen_for_novelli(self.p, self.bonjour_name, items_name[item_name], is_back_screen=False)
        if item_name == "crop":
            self.edit.select_edit_child_option(self.edit.SIZE_4_6, direction="right", check_end=False, str_id=True)
            self.edit.apply_crop_scale_picker()
        else:
            if item_name == "adjust":
                self.edit.select_edit_child_option(self.edit.SATURATION, direction="right", check_end=False, str_id=True)
            else:
                self.edit.select_edit_main_option(self.edit.FILTER_DOCUMENT)
                self.edit.select_edit_child_option(self.edit.BW2, direction="left", check_end=False, str_id=True)
            self.edit.verify_and_swipe_adjust_slider()
        self.edit.select_edit_done()
        self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()

    @pytest.mark.parametrize("btn_type", ["front_btn", "back_btn"])
    def test_02_verify_edit_text_function(self, btn_type):
        """
         Description: C29142874, C29152737, C29152740
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon depends on either from Front screen or Back screen
         6. CliCK on Edit button
         7. Click on Text item
         8. Input any text
         9. Click on Done button
         10. Click on Done button

         Expected Result:
         10. Verify Two-Sided Preview screen through:
            + Title
            + Front button
            + Back button
            + Print and Save button
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.bonjour_name, self.edit.TEXT, is_back_screen=btn_type == "back_btn")
        self.edit.add_txt_string("QAMATesting")
        for _ in range(3):
            self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()

    def test_03_verify_edit_discards_popup_function(self):
        """
         Description: C29142875, C29152749
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon
         6. CliCK on Edit button, and do some edit
         7. Click on Done button
         8. Click on Back button
         9. Click on No Button
         10. Click on Back button
         11. Click on Yes button

         Expected Result:
         8. Verify Discard Edits popup through:
            + Title
            + Body message
            + Yes and No button
         9. Verify Edit screen
         10. Verify Discard Edits popup
         11. Verify Two-Sided Preview screen
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.bonjour_name, self.edit.ADJUST, is_back_screen=False)
        self.edit.select_edit_child_option(self.edit.BRIGHTNESS, direction="right", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider()
        self.edit.select_edit_done()
        self.driver.press_key_back()
        self.edit.verify_discard_edits_screen()
        self.edit.select_discard_changes_btn(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS[3])
        self.edit.verify_edit_page_title()
        self.driver.press_key_back()
        self.edit.select_discard_changes_btn(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS[2])
        self.preview.verify_two_sided_preview_screen()

    def test_04_verify_edit_back_text_cancel_function(self):
        """
         Description: C29142880, C29152739, C29152748
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on Back button
         6. Click on 3 dot icon
         7. CliCK on Edit button
         8. Click on Text item
         9. Click on Back button
         10. Click on Back button
         11. Click on Yes button

         Expected Result:
         11. Verify Two-Sided Preview screen through:
            + Title
            + Front button
            + Back button
            + Print and Save button
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.bonjour_name, self.edit.TEXT, is_back_screen=True)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        self.edit.select_edit_done()
        self.driver.press_key_back()
        self.edit.select_discard_changes_btn(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS[2])
        self.preview.verify_two_sided_preview_screen()

    @pytest.mark.parametrize("item_name", ["front_function", "color_function"])
    def test_05_verify_edit_back_text_function(self, item_name):
        """
         Description: C29152744, C29152745, C29152746, C29152750
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on Back button
         6. Click on 3 dot icon
         7. CliCK on Edit button
         8. Click on Text item
         9. Click on Done button
         10. If item_name == "front_function": Click on Fonts item
             If item_name == "color_function": Click on Color item
         11. Select each item one by one
         12. Click on Done button

         Expected Result:
         12. verify each font can be selected success
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.bonjour_name, self.edit.TEXT, is_back_screen=True)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        if item_name == "front_function":
            self.edit.select_edit_main_option(self.edit.TEXT_FONTS)
            self.edit.select_edit_child_option(self.edit.ARVO, direction="right", check_end=False, str_id=True)
        else:
            self.edit.select_edit_main_option(self.edit.COLOR_BTN)
            self.edit.select_color(self.edit.BLACK)
        for _ in range(3):
            self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()