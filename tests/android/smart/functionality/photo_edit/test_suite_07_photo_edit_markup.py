from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_07_Photo_Edit_Markup(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=False, smart_advance=False)

    def test_01_verify_markup_screen_and_ui(self):
        """
        C29684723, C29684724, C29684730
        Description:
            1. Launch the Smart app
            2. Scan or select a photo to print and proceed to the preview screen
            3. Tap on edit icon
            4. Tap on Markup option
            5. Observe
        Expected Results:
            Verify that user is on Markup screen and the UI as given below with all the options avaialble
    C29684724

        1.Launch the Smart app
        2.Scan a document or select a photo to print and proceed to the preview screen
        3. Tap on edit icon
        4.Tap on Markup option (Color option and Size option)
        Expected result:
        -Verify Below options are available on the screen:
            1. Highlight
            2. White Out
            3. Black Pen
            4. Blue Pen
            5. Red Pen
        - Verify Size option on the screen
        """
        COLORS = [
            self.edit.HIGHLIGHT_OPTION,
            self.edit.WHITE_OUT_OPTION,
            self.edit.BLACK_PEN_OPTION,
            self.edit.BLUE_PEN_OPTION,
            self.edit.RED_PEN_OPTION
        ]
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.MARKUP)
        self.edit.verify_screen_title(self.edit.MARKUP)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.select_edit_child_option(self.edit.BRUSH_COLOR_BTN, direction="right", check_end=False, str_id=True)
        self.edit.verify_brush_color_screen()
        self.fc.select_back()
        self.edit.select_edit_child_option(self.edit.BRUSH_SIZE_BTN, direction="right", check_end=False, str_id=True)
        self.edit.verify_edit_ui_elements(self.edit.MARKUP_OPTIONS_BUTTONS)

