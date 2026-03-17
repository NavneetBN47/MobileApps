import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_05_Preview_Gallery(object):
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
    def test_02_scan_one_page_c43738530(self):
        """
        Make sure only 1 page scanned.
        Verify the thumbnail icon is hidden in Preview screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738530
        """
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_single_image()

    @pytest.mark.regression
    def test_03_click_back_button_without_save_c43738565(self):
        """
        Initiate Scan and step by step to Scan Preview screen.
        Do NOT save scanned file and then click Back arrow on the Gallery view.
        Verify "Exit without saving?" dialog shows

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738565 (one page)
        """
        self.fc.fd["scan"].click_back_arrow()
        self.fc.fd["scan"].verify_exit_without_saving_dialog()
        self.fc.fd["scan"].click_no_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_04_scan_multi_pages_c43738528_c43738531(self):
        """
        Initiate Scan and step by step to Scan Preview screen.
        Scan multiple pages.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738528

        Click '+ Add'.
        Verify user is taken to Scan screen and able to add more scans.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738531
        """
        for _ in range(2):
            self.fc.fd["scan"].click_add_pages_btn()
            self.fc.fd["scan"].verify_scan_btn()
            self.fc.fd["scan"].click_scan_btn()
            self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_multi_image(num=3)
        
    @pytest.mark.regression
    def test_05_switch_between_thumbnail_and_gallery_icon_c43738583_c43738527(self):
        """
        4.Click on the thumbnail view in the scanned preview page
        5.Click on the nested square icon
        After clicking on the nested square icon
        The user is returned to full view screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738583

        
        Click the thumbnail icon to launch the Thumbnail view screen.
        Click the Gallery icon to go back to Gallery screen.
        Click the 2 icons for mutiple times.
        Verify user can switch between the 2 screens without any issue.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738527
        """
        for _ in range(3):
            self.fc.fd["scan"].click_thumbnail_view_icon() 
            self.fc.fd["scan"].verify_thumbnail_view_screen(num=3)
            self.fc.fd["scan"].click_gallery_view_icon()
            self.fc.fd["scan"].verify_preview_with_multi_image(num=3)

    @pytest.mark.regression
    def test_06_click_back_button_without_save_c43738565(self):
        """
        Scan multiple pages.
        Do NOT save scanned file and then click Back arrow.
        Verify "Exit without saving?" dialog shows

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738565  (multiple pages)
        """
        self.fc.fd["scan"].click_back_arrow()
        self.fc.fd["scan"].verify_exit_without_saving_dialog()
        self.fc.fd["scan"].click_no_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_07_click_back_button_with_save_c43738566(self):
        """
        Scan mutiple pages and save scan files.
        Click Back arrow on the Gallery view ad observe.
        Verify user is taken to scan intro page.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738566
        """
        # HPXG-1360:[Function] The Exit without saving dialog still pops up after clicking back button even though scan job has been saved.
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        file_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        self.fc.fd["scan"].click_dialog_close_btn()
        # self.driver.ssh.send_command("del " + file_path)
        self.driver.ssh.send_command("Remove-Item -Path {} -Force -Recurse".format(file_path), timeout=20)

        self.fc.fd["scan"].click_back_arrow()
        assert self.fc.fd["scan"].verify_exit_without_saving_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_scan_btn()

