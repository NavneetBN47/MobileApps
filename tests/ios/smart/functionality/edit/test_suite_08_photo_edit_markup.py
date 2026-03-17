import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
pytest.app_info = "SMART"

class Test_Suite_08_Photo_Edit_Markup(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.edit = cls.fc.fd["edit"]
        cls.stack = request.config.getoption("--stack")
        # Navigating to home screen
        cls.fc.go_home(stack=cls.stack)

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
        self.fc.go_to_edit_screen_with_camera_scan_image()
        orig_img = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.MARKUP)
        self.edit.verify_screen_title(self.edit.MARKUP)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.verify_markup_screen()
        for color in self.edit.BRUSH_COLORS:
            brush_numb = self.edit.BRUSH_COLOR_FMT[color]
            self.edit.select_brush(brush_numb)
        coordinates = [(20,200), (20,350), (20,400), (150,200), (150,350), (150,400)]
        percent_brush_width = [0.2, 0.4, 0.6, 0.8, 0.9, 1.0]
        for n, coordinate in enumerate(coordinates):
            x = coordinate[0]
            y = coordinate[1]
            self.edit.select_brush(n % 5 + 1)
            actual_percent = self.edit.adjust_slider("adjust_brush_width", percent_brush_width[n])
            assert 0.95 * percent_brush_width[n] < actual_percent < 1.05 * percent_brush_width[n], "fails for brush width {} actual_percent {:.2f}".format(per_brush_width[n], actual_percent)
            self.edit.draw_line(x_start=x, y_start=y, x_end=x + 80, y_end=y)
        self.edit.select_edit_done()
        marked_img = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(orig_img, marked_img)