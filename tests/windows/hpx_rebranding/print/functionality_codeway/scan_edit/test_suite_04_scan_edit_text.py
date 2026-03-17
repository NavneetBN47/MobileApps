import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_04_Scan_Edit_Text(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, temp_files_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_go_to_scan_edit_screen(self):
        """
        Click Scan or Printer Scan tile from Printer Device Page.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)        
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].select_import_text()
        self.fc.fd["scan"].verify_file_picker_dialog()
        self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
        self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)      
        self.fc.fd["scan"].verify_import_screen()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()

    @pytest.mark.regression
    def test_02_click_edit_text_button_c43738509(self):
        """
        Click on text button in the side panel.
        1.The text 'Type something' should be displayed inside a blue-colored text box on the image.
        2.The font family should be set to 'Open Sans Bold' by default.
        3.Line spacing should be set to 1 by default.
        4.Allignment, Fount size, 'Font color', and 'background color' default settings should be same as per the design.
        [Refer screen shot attached below]

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738509
        """
        self.fc.fd["scan"].click_text_item()
        self.fc.fd["scan"].verify_edit_text_setting_screen()
        self.fc.fd["scan"].verify_font_family_combo_value('Open Sans Bold')
        self.fc.fd["scan"].verify_line_spacing_edit_value('1.0')
        self.fc.fd["scan"].verify_font_size_edit_value('14')
        front_c = self.fc.fd["hpx_rebranding_common"].compare_image_diff("front_color_group", folder_n="scan", image_n="text_front_color.png")
        assert front_c < 0.02
        background_c = self.fc.fd["hpx_rebranding_common"].compare_image_diff("background_color_group", folder_n="scan", image_n="text_background_color.png")
        assert background_c < 0.02
        
    @pytest.mark.regression
    def test_03_add_text_in_text_box_c43738510(self):
        """
        Click on text button.
        Add some text in the text box
        Click on undo/redo icon.
        1.The text should be added correctly, and the scanned image should reflect the changes.
        2.Clicking the "Undo" icon should remove the text and restore the scanned image to its previous state.
        3.Clicking the "Redo" icon should reapply the text and change the scanned image accordingly.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738510  
        """
        self.fc.fd["hpx_rebranding_common"].save_image("canvas_image", image_n="text_org.png")
        self.fc.fd["scan"].add_some_text('good!')
        self.fc.fd["hpx_rebranding_common"].save_image("canvas_image", image_n="text_good.png")
        com_org = self.fc.fd["hpx_rebranding_common"].compare_image_diff("canvas_image", image_n="text_org.png")
        assert com_org > 0.02
        
        for _ in range(3):
            self.fc.fd["scan"].click_undo_btn()
            sleep(1)
        com_org = self.fc.fd["hpx_rebranding_common"].compare_image_diff("canvas_image", image_n="text_org.png")
        assert com_org < 0.02
       
        for _ in range(3):
            self.fc.fd["scan"].click_redo_btn()
            sleep(1)
        com_good = self.fc.fd["hpx_rebranding_common"].compare_image_diff("canvas_image", image_n="text_good.png")
        assert com_good > 0.02

    @pytest.mark.regression
    def test_04_min_max_edit_screen_c43738511(self):
        """
        Add some text in the text box.
        min/max Edit screen.
        'Added text' should be displayed on the image.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738511
        """
        self.fc.fd["devicesMFE"].click_top_maximize_btn()
        self.fc.fd["scan"].click_center_image()
        self.fc.fd["hpx_rebranding_common"].save_image("canvas_image", image_n="text_max.png")
        com_org = self.fc.fd["hpx_rebranding_common"].compare_image_diff("canvas_image", image_n="text_org.png")
        assert com_org > 0.12
        sleep(1)
        
        self.fc.fd["devicesMFE"].click_top_maximize_btn()
        self.fc.fd["scan"].click_center_image()
        com_max = self.fc.fd["hpx_rebranding_common"].compare_image_diff("canvas_image", image_n="text_max.png")
        assert com_max > 0.12
