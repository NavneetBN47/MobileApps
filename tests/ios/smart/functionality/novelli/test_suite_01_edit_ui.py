import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_01_Edit_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()

        if "novelli" not in cls.p.p_obj.projectName:
            pytest.skip("Novelli printer is unavailable for testing this time")

        # Define the flows
        cls.home = cls.fc.fd["home"]
        cls.preview = cls.fc.fd["preview"]
        cls.photos = cls.fc.fd["photos"]
        cls.edit = cls.fc.fd["edit"]

        # Define variables
        cls.stack = request.config.getoption("--stack")
        cls.printer_info = cls.p.get_printer_information()
        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=False, instant_ink=True)
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.fc.go_home(stack=cls.stack)

    @pytest.mark.parametrize("item_name", ["adjust", "crop", "filter"])
    def test_01_verify_edit_front_adjust_function(self, item_name):
        """
        C29136374, C29141318, C29142866, C29142869, C29142870, C29142871, C29810662, C29810664, C29810667,  C29145919,  C29145921
         Description:
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
        self.fc.load_edit_screen_for_novelli(self.p, items_name[item_name], is_back_screen=False)
        if item_name == "crop":
            self.edit.select_edit_child_option(self.edit.CROP_SIZE_4_6, direction="right", check_end=False, str_id=True)
            self.edit.apply_crop_scale_picker()
        else:
            if item_name == "adjust":
                self.edit.select_edit_child_option(self.edit.ADJUST_OPTIONS[1], direction="right", check_end=False)
            else:
                self.edit.select_edit_main_option(self.edit.FILTER_DOCUMENT)
                self.edit.select_edit_child_option(self.edit.FILTER_DOCUMENT_OPTIONS[2], check_end=False)
            self.edit.verify_and_swipe_adjust_slider(direction="right")
        self.edit.select_edit_done()
        self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()

    @pytest.mark.parametrize("btn_type", ["front_btn", "back_btn"])
    def test_02_verify_edit_text_function(self, btn_type):
        """
        C29870954, C29152737, C29152740
         Description:
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
        self.fc.load_edit_screen_for_novelli(self.p, self.edit.TEXT, is_back_screen=btn_type == "back_btn")
        self.edit.add_txt_string("QAMATesting")
        for _ in range(3):
            self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()

    def test_03_verify_edit_discards_popup_function(self):
        """
        C29142875, C29152749
         Description:
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on 3 dot icon
         6. CliCK on Edit button, and do some edit
         7. Click on Done button
         8. Click on Cancel button
         9. Click on No Button
         10. Click on Cancel button
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
        self.fc.load_edit_screen_for_novelli(self.p, self.edit.ADJUST, is_back_screen=False)
        self.edit.select_edit_child_option(self.edit.ADJUST_OPTIONS[0], direction="right", check_end=False)
        self.edit.verify_and_swipe_adjust_slider()
        self.edit.select_edit_done()
        self.edit.select_edit_cancel()
        self.edit.verify_discard_edits_screen()
        self.edit.select_discard_changes_btn(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS[3])
        self.edit.verify_edit_page_title()
        self.edit.select_edit_cancel()
        self.edit.select_discard_changes_btn(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS[2])
        self.preview.verify_two_sided_preview_screen()

    def test_04_verify_edit_back_text_cancel_function(self):
        """
        C29142880, C29152739, C29152748
         Description:
         1. Load to Home screen with HP+ account login
         2. Click on View & Print button
         3. Click on My Photos, and select any photo from album
         4. Select 4x6 Two-Sided option from Print Size screen
         5. Click on Back button
         6. Click on 3 dot icon
         7. CliCK on Edit button
         8. Click on Text item
         9. Click on Cancel button
         10. Click on Cancel button
         11. Click on Yes button

         Expected Result:
         11. Verify Two-Sided Preview screen through:
            + Title
            + Front button
            + Back button
            + Print and Save button
        """
        self.fc.load_edit_screen_for_novelli(self.p, self.edit.TEXT, is_back_screen=True)
        self.edit.add_txt_string("QAMATesting")
        for _ in range(2):
            self.edit.select_edit_cancel()
        self.preview.verify_two_sided_preview_screen()

    @pytest.mark.parametrize("item", ["front", "color"])
    def test_05_verify_edit_back_text_function(self, item):
        """
        C29152744, C29152745, C29152746, C29152750
         Description:
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
        items = {"front": self.edit.TEXT_FONTS,
                      "color": self.edit.TEXT_COLOR}
        self.fc.load_edit_screen_for_novelli(self.p, self.edit.TEXT, is_back_screen=True)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        self.edit.select_edit_main_option(items[item])
        if item == "front":
            self.edit.select_edit_child_option(self.edit.TEXT_FONT_OPTIONS[2], direction="right", check_end=False, str_id=False)
        else:
            self.edit.select_edit_child_option(self.edit.TEXT_COLOR_OPTIONS[4], direction="right", check_end=False, str_id=False)
        for _ in range(3):
            self.edit.select_edit_done()
        self.preview.verify_two_sided_preview_screen()