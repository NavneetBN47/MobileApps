import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_06_Scan_Edit_Delete(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]


    @pytest.mark.regression
    def test_01_go_to_scan_preview_screen(self):
        """
        1.Click on the printer card.
        2.Click on the scan tile.
        3.Perform a scan job.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_single_image() 

    @pytest.mark.regression
    def test_02_click_delete_button_with_one_job_c43738665_c43738666_c43738639_c43738640(self):
        """
        Click on delete button in preview screen.
        "Delete Selected images?" confirmation dialog box should be displayed.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738665
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738666

        3.Perform a scan job
        4.Click on the "Delete" button from the gallery preview screen
        Verify Delete confirmation dialog shows after the user clicks on the Delete icon

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738639
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738640
        """
        self.fc.fd["scan"].click_image_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()

    @pytest.mark.regression
    def test_03_delete_with_one_job_c43738598(self):
        """
        3.Perform a scan job
        4.Click on the delete icon in the scanned preview page
        5.Click on the delete button in the dialog box
        verify user is able to delete the scan file without any issue

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738598
        """
        self.fc.fd["scan"].click_dialog_delete_btn()
        assert self.fc.fd["scan"].verify_delete_selected_images_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.regression
    def test_04_perform_multi_scan_job_c43738621(self):
        """
        3.Scan multiple items from single scan
        4.Verify the Gallery preview screen
        Verify Preview Screen Gallery view-UI as show below

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738621
        """
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        for _ in range(2):
            self.fc.fd["scan"].click_add_pages_btn()
            self.fc.fd["scan"].verify_scan_btn()
            self.fc.fd["scan"].click_scan_btn()
            self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_multi_image(num=3)
        self.fc.fd["scan"].click_gallery_view_icon()

    @pytest.mark.regression
    def test_05_verify_cancel_delete_with_multi_job_c43738592_c43738642(self):
        """
        3.Scan multiple documents in scan tile
        4.Click on delete button is scanned preview screen
        5.Click on Cancel button in the dialog box.
        verify image is not deleted and user land back to preview screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738592

        3.Perform a multiple scan job
        4.Click on the "Delete" button from the gallery preview screen
        5.Click on the Cancel button
        Verify the image is not deleted and userland back to the preview screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738642
        """
        self.fc.fd["scan"].click_image_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()
        self.fc.fd["scan"].click_dialog_cancel_btn()
        assert self.fc.fd["scan"].verify_delete_selected_images_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_06_verify_delete_with_multi_job_c43738671_c43738593_c43738620_c43738641(self):
        """
        Select image and click on delete button.
        "Delete selected images?" confirmation dialog box should be displayed.
        The image should be deleted successfully.
        The 'Gallery' icon and 'Thumbnail' icon should disappear.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738671

        3.Scan multiple document
        4.Click on the delete button in scanned preview screen
        Verify "Delete the selected images?" dialog box.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738593

        3.Scan multiple items from single scan
        4.Click on Delete button from the gallery preview screen
        Verify user can only delete one item at a time from the gallery preview screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738620

        3.Perform a multiple scan job
        4.Click on the "Delete" button from the gallery preview screen
        5.Click on the Delete button
        Verify the image is deleted

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738641
        """
        for i in range(3):
            self.fc.fd["scan"].click_image_delete_btn()
            self.fc.fd["scan"].verify_delete_selected_images_dialog()
            self.fc.fd["scan"].click_dialog_delete_btn()
            assert self.fc.fd["scan"].verify_delete_selected_images_dialog(raise_e=False) is False
            if i==0: 
                self.fc.fd["scan"].verify_preview_with_multi_image(num=2)
            elif i==1:
                self.fc.fd["scan"].verify_preview_with_single_image()
            elif i==2:
                self.fc.fd["scan"].verify_scan_btn()
