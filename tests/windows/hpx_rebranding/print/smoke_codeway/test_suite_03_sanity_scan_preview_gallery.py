import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_03_Sanity_Scan_Preview_Gallery(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_check_scan_preview_gallery_screen_C43738518(self):
        """
        Perform a single scan via any available entry, verify the Gallery view screen with single scan

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738518
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_single_image()

    @pytest.mark.smoke
    def test_02_click_new_scan_and_no_btn_C43738535(self):
        """
        Click "No" button on Start a new Scan without saving? dialog, verify user is taken back to preview screen

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738535
        """
        self.fc.fd["scan"].click_new_scan_btn()
        self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog()
        self.fc.fd["scan"].click_cancel_btn()
        assert self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.smoke
    def test_03_click_new_scan_and_yes_btn_C43738534(self):
        """
        Click "Yes" button on Start a new Scan without saving? dialog, verify user is taken back to scan intro page

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738534
        """
        self.fc.fd["scan"].click_new_scan_btn()
        self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog()
        self.fc.fd["scan"].click_start_new_scan_btn()
        assert self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.smoke
    def test_04_click_delete_icon_on_scan_preview_gallery_C43738524(self):
        """
        Click Delete icon on Preview Gallery screen, verify user can only delete one item at a time

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738524
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        scanned_image = 3
        self.__perform_multi_scan_jobs(page=scanned_image)

        for i in range(scanned_image):
            self.fc.fd["scan"].click_image_delete_btn()
            self.fc.fd["scan"].verify_delete_selected_images_dialog()
            self.fc.fd["scan"].click_dialog_delete_btn()
            assert self.fc.fd["scan"].verify_delete_selected_images_dialog(raise_e=False) is False
            if i<1: 
                self.fc.fd["scan"].verify_preview_with_multi_image(num=scanned_image-1-i)
            elif i==1:
                self.fc.fd["scan"].verify_preview_with_single_image()
            else:
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