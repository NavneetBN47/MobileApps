import pytest
import MobileApps.resources.const.windows.const as w_const
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_04_Preview_Image_Icon(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_go_to_scanner_screen(self):
        """
        Click Scan or Printer Scan tile from Printer Device Page.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.regression
    def test_02_verify_image_icon_with_one_page_c43738520_c43738522(self):
        """
        3.Perform a scan job.
        Verify the Rotate icon shows when only 1 page listed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738520

        Verify the Edit icon shows when only 1 page scanned.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738522
        """
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
    def test_03_click_rotate_icon_c43738521(self):
        """
        3.Perform a scan job.
        4.Click on rotate button on the gallery screen
        Verify the scanned file is rotated after clicking the Rotate icon.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738521
        """
        self.fc.fd["hpx_rebranding_common"].save_image("body_area", folder_n="scan", image_n="preview_org.png", pre=True)
        org = self.fc.fd["hpx_rebranding_common"].compare_image_diff("body_area", folder_n="scan", image_n="preview_org.png", pre=True)
        assert org < 0.02
        self.fc.fd["scan"].click_image_rotate_btn()
        self.fc.fd["hpx_rebranding_common"].save_image("body_area", folder_n="scan", image_n="preview_rotate.png", pre=True)
        right = self.fc.fd["hpx_rebranding_common"].compare_image_diff("body_area", folder_n="scan", image_n="preview_rotate.png", pre=True)
        assert right < 0.02

    @pytest.mark.regression
    def test_04_verify_image_replace_icon_c43738580(self):
        """
        Initiate Scan and step by step to Scan Preview screen.
        Click Replace icon.
        Verify a screen with "Cancel" button, "Scan" button and description strings displays after cliking Replace icon.
        Verify scan job for replace is completed successfully.
        Verify only selected item gets replaced by the new scanned page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738580
        """
        self.fc.fd["scan"].click_image_replace_btn()
        self.fc.fd["scan"].verify_replace_screen()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        rep = self.fc.fd["hpx_rebranding_common"].compare_image_diff("body_area", folder_n="scan", image_n="preview_org.png", pre=True)
        assert rep > 0.15
            
    @pytest.mark.regression
    def test_05_click_edit_icon_with_one_page_c43738523(self):
        """
        Click the Edit icon for each image.
        Verify the Edit screen shows when only 1 page scanned.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738523
        """
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        self.fc.fd["scan"].click_edit_cancel_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_06_verify_image_icon_with_multi_pages_c43738520_c43738522(self):
        """
        Verify the Rotate icon shows for each image when multiple pages are scanned.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738520

        Verify the Edit icon shows for each image when multiple pages scanned.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738522
        """
        for _ in range(2):
            self.fc.fd["scan"].click_add_pages_btn()
            self.fc.fd["scan"].verify_scan_btn()
            self.fc.fd["scan"].click_scan_btn()
            self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_multi_image(num=3)
        for i in range(3):
            self.fc.fd["scan"].select_gallery_item(num=i+1)
            self.fc.fd["scan"].verify_image_preview()

    @pytest.mark.regression
    def test_07_click_edit_icon_with_multi_pages_c43738523(self):
        """
        Verify the Edit screen shows for each image when multiple pages scanned.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738523
        """
        for i in range(3):
            self.fc.fd["scan"].select_gallery_item(num=i+1)
            self.fc.fd["scan"].click_image_edit_btn()
            self.fc.fd["scan"].verify_edit_screen()
            self.fc.fd["scan"].click_edit_cancel_btn()
            self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_08_verify_left_and_right_arrow_with_multi_pages_c43738526(self):
        """
        3.Scan multiple documents.
        4.Click on the right and left arrow key in the scanned preview screen
        Verify left and right arrows on both sides of the image on Gallery screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738526
        """
        for i in range(3):
            self.fc.fd["scan"].select_gallery_item(num=i+1)
            if i == 0:
                self.fc.fd["scan"].verify_right_arrow_btn_display()
                assert self.fc.fd["scan"].verify_left_arrow_btn_display(raise_e=False) is False
            elif i == 1:
                self.fc.fd["scan"].verify_left_arrow_btn_display()
                self.fc.fd["scan"].verify_right_arrow_btn_display()
            else:
                self.fc.fd["scan"].verify_left_arrow_btn_display()
                assert self.fc.fd["scan"].verify_right_arrow_btn_display(raise_e=False) is False
