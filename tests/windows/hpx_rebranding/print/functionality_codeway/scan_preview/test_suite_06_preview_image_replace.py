import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_06_Preview_Image_Replace(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, temp_files_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_go_to_preview_with_one_image_screen(self):
        """
        Initiate Scan and step by step to Scan Preview screen.
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
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].click_import_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_single_image()

    @pytest.mark.regression
    def test_02_click_replace_icon_with_one_image_screen(self):
        """
        Click Replace icon on Gallery screen, verify Replace flow functionality

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738525 (one page)
        """
        self.fc.fd["hpx_rebranding_common"].save_image("body_area", image_n="body_area.png", pre=True)
        self.fc.fd["scan"].click_image_replace_btn()
        # self.fc.fd["scan"].verify_replace_screen()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen(timeout=180)
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_single_image()

        com_org = self.fc.fd["hpx_rebranding_common"].compare_image_diff("body_area", image_n="body_area.png", pre=True)
        assert com_org > 0.15

    @pytest.mark.regression
    def test_03_go_to_preview_with_multi_images_screen(self):
        """
        Initiate Scan and step by step to Scan Preview screen.
        """
        for _ in range(2):
            self.fc.fd["scan"].click_add_pages_btn()
            self.fc.fd["scan"].verify_scan_btn()
            self.fc.fd["scan"].select_import_text()
            self.fc.fd["scan"].verify_file_picker_dialog()
            self.fc.check_files_exist(w_const.TEST_DATA.WOMAN_BMP, w_const.TEST_DATA.WOMAN_BMP_PATH)
            self.fc.fd["scan"].input_file_name(w_const.TEST_DATA.WOMAN_BMP)
            self.fc.fd["scan"].verify_import_screen()
            self.fc.fd["scan"].click_import_full_option()
            self.fc.fd["scan"].click_import_done_btn()
            self.fc.fd["scan"].verify_scan_result_screen()
   
        self.fc.fd["scan"].verify_preview_with_multi_image(num=3)

    @pytest.mark.regression
    def test_04_click_replace_icon_with_multi_images_c43738656_c43738525(self):
        """
        Click Replace from preview screen (multi-item scan), verify the functionality

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738656

        Click Replace icon on Gallery screen, verify Replace flow functionality

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738525 (multiple pages)
        """
        self.fc.fd["hpx_rebranding_common"].save_image("dynamic_item_btn", format_specifier=['1'], image_n="item_1.png")
        self.fc.fd["hpx_rebranding_common"].save_image("dynamic_item_btn", format_specifier=['2'], image_n="item_2.png")
        self.fc.fd["hpx_rebranding_common"].save_image("dynamic_item_btn", format_specifier=['3'], image_n="item_3.png")

        self.fc.fd["scan"].click_image_replace_btn()
        # self.fc.fd["scan"].verify_replace_screen()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen(timeout=180)
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_multi_image(num=3)

    @pytest.mark.regression
    def test_05_verify_image_get_replaced_c43738664(self):
        """
        Click Replace from the preview screen, verify the image gets replaced with an image from the correct Source

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738664
        """
        com_1 = self.fc.fd["hpx_rebranding_common"].compare_image_diff("dynamic_item_btn", format_specifier=['1'], image_n="item_1.png")
        assert com_1 == 0
        com_2 = self.fc.fd["hpx_rebranding_common"].compare_image_diff("dynamic_item_btn", format_specifier=['2'], image_n="item_2.png")
        assert com_2 == 0
        com_3 = self.fc.fd["hpx_rebranding_common"].compare_image_diff("dynamic_item_btn", format_specifier=['3'], image_n="item_3.png")
        assert com_3 > 0.3
