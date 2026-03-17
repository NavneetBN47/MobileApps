import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info = "HPX"
class Test_Suite_16_Sanity_Dark_Mode(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, temp_files_cleanup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_go_to_preview_screen_with_multi_jobs(self):
        """
        Perform multiple scan jobs from the Document feeder or Scanner Glass
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        for i in range(3):
            self.fc.fd["scan"].verify_scan_btn()
            self.fc.fd["scan"].click_scan_btn()
            self.fc.fd["scan"].verify_scan_result_screen()
            if i!=2:
                self.fc.fd["scan"].click_add_pages_btn()
        self.fc.fd["scan"].verify_preview_with_multi_image(num=3)
        self.fc.fd["hpx_rebranding_common"].save_image("myhp_window", image_n="gall_org.png")
        self.fc.fd["scan"].click_thumbnail_view_icon()
        self.fc.fd["scan"].verify_thumbnail_view_screen(num=3)
        self.fc.fd["hpx_rebranding_common"].save_image("myhp_window", image_n="thum_org.png")
        
    @pytest.mark.smoke
    def test_02_check_gallery_view_dark_mode_C53721849(self):
        """
        Verify the Dark mode UI of the Scan Result MFE screen in Gallery view

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53721849
        """
        self.fc.enable_dark_mode()
        sleep(5)
        self.fc.fd["scan"].click_gallery_view_icon()
        gall = self.fc.fd["hpx_rebranding_common"].compare_image_diff("myhp_window", image_n="gall_org.png")
        assert gall > 0.6

    @pytest.mark.smoke
    def test_03_check_thumbnail_view_dark_mode_C53722131(self):
        """
        Verify the Dark mode UI of the Scan Result MFE screen in Thumbnail view

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53722131
        """
        self.fc.fd["scan"].click_thumbnail_view_icon()
        self.fc.fd["scan"].verify_thumbnail_view_screen(num=3)
        thum = self.fc.fd["hpx_rebranding_common"].compare_image_diff("myhp_window", image_n="thum_org.png")
        assert thum > 0.6

    @pytest.mark.smoke
    def test_04_disable_dark_mode_C53332010(self):
        """
        Verify UI Switches from Dark Mode to Light Mode

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53332010
        """
        self.fc.disable_dark_mode()
        thum = self.fc.fd["hpx_rebranding_common"].compare_image_diff("myhp_window", image_n="thum_org.png")
        assert thum < 0.01

