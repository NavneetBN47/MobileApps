import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_09_Sanity_Scan_Delete(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_click_cancel_btn_on_delete_dialog_C43738668(self):
        """
        Select Cancle button on the "Delete selected images" dialog, verify image is not deleted and user land back to preview screen

        Expected:
        Image should not delete and it should landback to scanned preview screen.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738668
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_single_image()
        self.fc.fd["scan"].click_image_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()
        self.fc.fd["scan"].click_cancel_btn()
        assert self.fc.fd["scan"].verify_delete_selected_images_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_preview_with_single_image()

    @pytest.mark.smoke
    def test_02_delete_single_scanned_image_from_gallery_view_C43738667(self):
        """
        Select Delete button on the "Delete selected images" dialog, verify image is deleted

        Expected:
        Image should be deleted and it should navigate to Scan intro page. [if user having only one image in preview screen]

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738667
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_single_image()
        self.fc.fd["scan"].click_image_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()
        self.fc.fd["scan"].click_dialog_delete_btn()
        assert self.fc.fd["scan"].verify_delete_selected_images_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.smoke
    def test_03_delete_multi_scanned_images_from_thumbnail_view_C43738670(self):
        """
        Select multi thumbnails in Thumbnail view screen to delete scans, verify scans are deleted

        Expected:
        1.'Delete Selected Image.' confirmation dialog box should be displayed.
        2. User should successfully delete the image and it should landback to scan intro page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738670
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)

        scanned_image = 3
        self.__perform_multi_scan_jobs(page=scanned_image)
        self.fc.fd["scan"].click_thumbnail_view_icon()
        self.fc.fd["scan"].verify_thumbnail_view_screen(num=3)
        self.fc.fd["scan"].click_thumbnail_select_all_btn()
        self.fc.fd["scan"].click_thumbnail_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()
        self.fc.fd["scan"].click_dialog_delete_btn()
        self.fc.fd["scan"].verify_scan_btn()


    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __perform_multi_scan_jobs(self, page=2):
        """
        Perform multi scan job. [Minimum 2]
        """
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_single_image() 
        for i in range(page-1):
            self.fc.fd["scan"].click_add_pages_btn()
            self.fc.fd["scan"].verify_scan_btn()
            self.fc.fd["scan"].click_scan_btn()
            self.fc.fd["scan"].verify_scan_result_screen()
            self.fc.fd["scan"].verify_preview_with_multi_image(num=i+2)
