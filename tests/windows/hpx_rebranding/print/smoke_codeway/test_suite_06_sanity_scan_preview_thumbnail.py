import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_06_Sanity_Scan_Preview_Thumbnail(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, temp_files_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]
        cls.scanned_image = 2


    @pytest.mark.smoke
    def test_01_check_thumbnail_view_C43738581(self):
        """
        Verify: Scan multiple pages and check the Thumbnail view screen

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738581
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.__perform_multi_scan_jobs(page=self.scanned_image)
        self.fc.fd["scan"].click_thumbnail_view_icon() 
        self.fc.fd["scan"].verify_thumbnail_view_screen(num=self.scanned_image)

    @pytest.mark.smoke
    def test_02_check_rotate_functionality_C43738584(self):
        """
        Verify the functionality of the "Rotate" on the thumbnails view screen (Auto Orientation = ON)

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738584
        """
        # self.fc.fd["scan"].click_thumbnail_view_icon() 
        # self.fc.fd["scan"].verify_thumbnail_view_screen(num=self.scanned_image)
        self.fc.fd["scan"].select_thumbnail_item(num=self.scanned_image)
        self.fc.fd["scan"].verify_thumbnail_item(num=self.scanned_image, check=True)

        self.fc.fd["hpx_rebranding_common"].save_image("dynamic_item_btn", format_specifier=['Checkmark ' + str(self.scanned_image)], image_n="before_rotate.png")

        self.fc.fd["scan"].click_thumbnail_rotate_btn()
        sleep(3)
        
        com_org = self.fc.fd["hpx_rebranding_common"].compare_image_diff("dynamic_item_btn", format_specifier=['Checkmark ' + str(self.scanned_image)], image_n="before_rotate.png")
        assert com_org > 0.01

    @pytest.mark.smoke
    def test_03_check_delete_pop_up_C43738586(self):
        """
        Verify "Delete" from the thumbnails view screen, verify scan is deleted
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738586
        """
        self.fc.fd["scan"].click_thumbnail_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()

    @pytest.mark.smoke
    def test_04_delete_single_image_C43738594(self):
        """
        Select Delete button on the "Delete selected images" dialog, verify image is deleted 
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738594
        """
        self.fc.fd["scan"].click_dialog_delete_btn()
        assert self.fc.fd["scan"].verify_delete_selected_images_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_thumbnail_item(num=self.scanned_image-1)

    @pytest.mark.smoke
    def test_05_delete_multiple_images_C43738597(self):
        """
        Delete multiple scanned images, verify user is able to delete the scanned images without any issue 	 
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738597
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.__perform_multi_scan_jobs(page=3)
        self.fc.fd["scan"].click_thumbnail_view_icon() 
        self.fc.fd["scan"].verify_thumbnail_view_screen(num=3)
        # self.fc.fd["scan"].click_thumbnail_select_all_btn()
        self.fc.fd["scan"].select_thumbnail_item(num=1)
        sleep(1)
        self.fc.fd["scan"].select_thumbnail_item(num=2)
        self.fc.fd["scan"].click_thumbnail_delete_btn()
        self.fc.fd["scan"].verify_delete_selected_images_dialog()
        self.fc.fd["scan"].click_dialog_delete_btn()
        self.fc.fd["scan"].verify_thumbnail_view_screen(num=1)

    @pytest.mark.smoke
    def test_06_click_print_btn_on_thumbnail_view_C43738628(self):
        """
        Click Print button in Thumbnail view screen, verify print dialog shows 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738628
        """
        self.fc.restart_hpx()
        self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.__perform_multi_scan_jobs(page=self.scanned_image)
        self.fc.fd["scan"].click_thumbnail_view_icon() 
        self.fc.fd["scan"].verify_thumbnail_view_screen(num=self.scanned_image)
        self.fc.fd["scan"].select_thumbnail_item(num=self.scanned_image)
        self.fc.fd["scan"].verify_thumbnail_item(num=self.scanned_image, check=True)
        self.fc.fd["scan"].click_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_cancel_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_multi_image(num=self.scanned_image)
        

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
