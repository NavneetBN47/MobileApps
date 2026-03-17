import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_01_Preview_Thumbnail(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, temp_files_cleanup):
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
    def test_02_scan_photo_turn_on_auto_ori_c43738537(self):
        """
        Scan photo, turn Auto-Orientation On, verify rotation animations shows while scanned image shows in Preview screen
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738537
        """
        self.fc.fd["scan"].select_dropdown_listitem(self.fc.fd["scan"].PRESET, self.fc.fd["scan"].PHOTO)
        assert self.fc.fd["scan"].get_scan_presets_value() == self.fc.fd["scan"].PHOTO

        self.fc.fd["scan"].select_auto_enhancement_icon()
        self.fc.fd["scan"].verify_auto_enhancement_panel()
        assert self.fc.fd["scan"].verify_auto_orientation_state() == '0'
        self.fc.fd["scan"].click_auto_orientation_toggle()
        assert self.fc.fd["scan"].verify_auto_orientation_state() == '1'
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_03_hover_gallery_thumbnail_icon(self):
        """
        Hover the "Gallery View" icon in scan preview screen, confirm tooltip message appears

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738582 (can not recognise the hover text)

        Hover over the thumbnail view icon in Preview screen.
        When the cursor hovers over the thumbnail icon, "Thumbnail View" tooltip message appears.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738529 (can not recognise the hover text)
        """
        for _ in range(3):
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
        self.fc.fd["scan"].verify_preview_with_multi_image()
        # self.fc.fd["scan"].hover_gallery_view_icon()
        # self.fc.fd["scan"].verify_dynamic_text_item('Gallery View')
        # self.fc.fd["scan"].hover_thumbnail_view_icon()
        # self.fc.fd["scan"].verify_dynamic_text_item('Thumbnail View')

    @pytest.mark.regression
    def test_04_verify_rotate_button_in_thumbnail_c43738585(self):
        """
        3.Set Auto Orientation= off
        4.Perform a scan job
        5.Click on thumbnail view icon and select any one image
        6.Click on the "Rotate" button from the thumbnail preview screen
        Verify the rotate button functionality in thumbnail view screen, the selected image should Roate
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738585
        """
        self.fc.fd["scan"].click_add_pages_btn()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].select_auto_enhancement_icon()
        assert self.fc.fd["scan"].verify_auto_orientation_state() == '1'
        self.fc.fd["scan"].click_auto_orientation_toggle()
        assert self.fc.fd["scan"].verify_auto_orientation_state() == '0'
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_thumbnail_icon()
        self.fc.fd["scan"].click_thumbnail_view_icon() 
        self.fc.fd["scan"].verify_thumbnail_view_screen(num=5)
        self.fc.fd["hpx_rebranding_common"].save_image("dynamic_item_btn", format_specifier=['3'], image_n="thumbnail_default.png")
        self.fc.fd["scan"].select_thumbnail_item(num=3)
        self.fc.fd["scan"].click_thumbnail_rotate_btn()
        self.fc.fd["scan"].click_thumbnail_deselect_all_btn()
        compare = self.fc.fd["hpx_rebranding_common"].compare_image_diff("dynamic_item_btn", format_specifier=['3'], image_n="thumbnail_default.png")
        assert compare > 0.15

    @pytest.mark.regression
    def test_05_verify_edit_button_no_item_c43738607(self):
        """
        Check Edit option when only no file is selected, verify edit option is NOT available

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738607
        """
        assert self.fc.fd["scan"].get_thumbnail_edit_state() == 'false'

    @pytest.mark.regression
    def test_06_verify_edit_button_one_item_c43738606(self):
        """
        Check Edit option when only one file is selected, verify edit option is available

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738606
        """
        self.fc.fd["scan"].select_thumbnail_item(num=1)
        assert self.fc.fd["scan"].get_thumbnail_edit_state() == 'true'

    @pytest.mark.regression
    def test_07_verify_edit_button_multi_item_c43738605(self):
        """
        Check Edit option when multiple items are selected on thumbnail view, verify Edit option is disable

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738605
        """
        self.fc.fd["scan"].select_thumbnail_item(num=2)
        assert self.fc.fd["scan"].get_thumbnail_edit_state() == 'false'

    @pytest.mark.regression
    def test_08_verify_delete_single_scan_in_thumbnail_c43738595(self):
        """
        5.Select a single document in the thumbnails preview screen.
        6.Click on the delete icon.
        verify delete conformation dialog shows.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738595
        """
        self.fc.fd["scan"].click_thumbnail_deselect_all_btn()
        self.fc.fd["scan"].select_thumbnail_item(num=1)
        self.fc.fd["scan"].click_thumbnail_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()
        self.fc.fd["scan"].click_dialog_delete_btn()
        assert self.fc.fd["scan"].verify_delete_selected_images_dialog(raise_e=False) is False

    @pytest.mark.regression
    def test_09_click_select_all_btn_in_thumbnail_c43738617(self):
        """
        The "Deselect all" button will appear if one or more images are selected.
        The "Select all" button will appear if no images are selected.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738617
        """
        for i in range(4):
            self.fc.fd["scan"].verify_thumbnail_item(num=i+1, check=False)
        self.fc.fd["scan"].verify_thumbnail_select_all_btn_attr()

        for i in range(4):
            self.fc.fd["scan"].select_thumbnail_item(num=i+1)
            self.fc.fd["scan"].verify_thumbnail_item(num=i+1, check=True)
            self.fc.fd["scan"].verify_thumbnail_deselect_all_btn_attr()
            sleep(1)            

    @pytest.mark.regression
    def test_10_click_deselect_all_btn_in_thumbnail_c43738618(self):
        """
        5.Click on "Select all" button, and verify all the items are selected
        6.Click on "Deselect All" button
        Verify all the scanned items are deselected
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738618
        """
        self.fc.fd["scan"].click_thumbnail_deselect_all_btn()
        for i in range(4):
            self.fc.fd["scan"].verify_thumbnail_item(num=i+1, check=False)

        self.fc.fd["scan"].click_thumbnail_select_all_btn()
        for i in range(4):
            self.fc.fd["scan"].verify_thumbnail_item(num=i+1, check=True)

        self.fc.fd["scan"].click_thumbnail_deselect_all_btn()
        for i in range(4):
            self.fc.fd["scan"].verify_thumbnail_item(num=i+1, check=False)

    @pytest.mark.regression
    def test_11_select_some_pages_in_thumbnail_c43738604(self):
        """
        5.Select some of the desired pages from the thumbnail view
        Verify user can select desired page

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738604
        """
        for i in range(2):
            self.fc.fd["scan"].select_thumbnail_item(num=i+1)
        for i in range(4):
            if i < 2:
                check = True
            else:
                check = False
            self.fc.fd["scan"].verify_thumbnail_item(num=i+1, check=check)

    @pytest.mark.regression
    def test_12_verify_delete_multi_scans_in_thumbnail_c43738587_c43738596(self):
        """
        5.Select few scanned documents from thumbnails view page.
        6.Click on the delete icon.
        Verify the scans are deleted.
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738587

        5.Select multiple thumbnails and click on delete button
        verify delete conformation dialog shows

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738596
        """
        self.fc.fd["scan"].click_thumbnail_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()
        self.fc.fd["scan"].click_dialog_delete_btn()
        assert self.fc.fd["scan"].verify_delete_selected_images_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_thumbnail_view_screen(num=2)

