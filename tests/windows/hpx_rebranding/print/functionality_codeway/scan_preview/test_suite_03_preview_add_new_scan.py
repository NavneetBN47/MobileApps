import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_03_Preview_Add_New_Scan(object):
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
    def test_02_click_new_scan_button_with_one_page_c43738623_c43738624_c43738532_c43738533(self):
        """
        3.Perform a scan job
        4.Click on "New Scan" button from gallery preview screen without saving the image
        Verify "Start a new scan without saving" dialog shows

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738623
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738624
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738532 (Scan one page)
        https://hp-testrail.external.hp.com/index.php?/cases/view/43738533
        """
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_new_scan_btn()
        self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog()

    @pytest.mark.regression
    def test_03_click_no_button_in_dialog_c43738626(self):
        """
        3.Perform a scan job
        4.Click on the "New Scan" button from the gallery preview screen
        5.Click on the "No" button on Start a new Scan without saving? dialog box
        Verify user is taken back to preview screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738626
        """
        self.fc.fd["scan"].click_cancel_btn()
        assert self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_04_click_yes_button_in_dialog_c43738625(self):
        """
        3.Perform a scan job.
        4.Click on "New Scan" button in gallery preview screen
        5. Click "Yes" button on Start a new Scan without saving? dialog box
        Verify user is taken back to scan intro page

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738625
        """
        self.fc.fd["scan"].click_new_scan_btn()
        self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog()
        self.fc.fd["scan"].click_start_new_scan_btn()
        assert self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.regression
    def test_05_save_and_add_new_scan_in_preview_c43738627(self):
        """
        3.Perform a scan job and save the image
        4.Click on the "New Scan" button from the gallery preview screen
        Verify user is taken back to scan intro page

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738627
        """
        # Perform a scan job and save the image
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        flie_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        self.fc.fd["scan"].click_dialog_close_btn()
        self.driver.ssh.send_command("del " + flie_path)

        # Click on the "New Scan" button
        self.fc.fd["scan"].click_new_scan_btn()
        self.fc.fd["scan"].verify_scan_btn()

    @pytest.mark.regression
    def test_06_click_new_scan_button_with_multi_pages_c43738532(self):
        """
        Scan multiple pages.
        Click "New Scan" button when multiple scanned images are not saved.
        Verify exit without saving conformation dialog "Start a new scan without saving?" shows after clicking the "New Scan" button.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738532 (Scan multiple pages)
        """
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].verify_preview_with_single_image()
        self.fc.fd["scan"].click_new_scan_btn()
        self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog()

    @pytest.mark.regression
    def test_07_click_yes_button_to_back_to_scan_intro_page_c43738536(self):
        """
        Scan multiple pages and save them.
        Click "New Scan" button.
        Verify user is taken back to scan intro page after clicking the "New Scan" button.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738536
        """
        self.fc.fd["scan"].click_start_new_scan_btn()
        assert self.fc.fd["scan"].verify_start_a_new_scan_without_saving_dialog(raise_e=False) is False
        self.fc.fd["scan"].verify_scan_btn()
