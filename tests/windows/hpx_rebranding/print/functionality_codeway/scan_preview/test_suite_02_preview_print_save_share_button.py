import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_02_Preview_Print_Save_Share_Button(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.hostname = cls.p.get_printer_information()['serial number']


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
    def test_02_verify_print_button_in_preview_c43738589_c43738542(self):
        """
        Check "Print" button on the Preview screen verify print shows.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738589

        Check the Preview screen.
        Verify print button show.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738542
        """
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_all_the_button_on_preview()
        
    @pytest.mark.regression
    def test_03_scan_and_print_in_preview_c43738588(self):
        """
        3.Perform a scan job
        4.Click on the "Print" button in scanned preview screen
        After clicking on printing button, print driver window is opened.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738588

        """
        self.fc.fd["scan"].click_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_printer(self.hostname)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_04_scan_multi_page_and_print_in_preview_c43738541(self):
        """
        Scan multiple pages and then click the Print button.
        Verify print dialog shows with scanned images.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738541
        """
        for _ in range(2):
            self.fc.fd["scan"].click_add_pages_btn()
            self.fc.fd["scan"].verify_scan_btn()
            self.fc.fd["scan"].click_scan_btn()
            self.fc.fd["scan"].verify_scan_result_screen()
        self.fc.fd["scan"].click_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_printer(self.hostname)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_05_verify_detect_edges_screen_c43738447(self):
        """
        Initiate Scan and step by step to Detect Edge screen.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738447
        """
        self.fc.fd["scan"].click_add_pages_btn()
        self.fc.fd["scan"].verify_scan_btn()
        self.fc.fd["scan"].click_detect_edges_checkbox()
        assert self.fc.fd["scan"].verify_detect_edges_checkbox_status() == "1"
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen(timeout=180)     
        self.fc.fd["scan"].verify_import_screen()

    @pytest.mark.regression
    def test_06_save_the_scan_file_c43738454_c43738637_c43738550(self):
        """
        Initiate Scan and step by step to Detect Edge screen.
        Click "Done" on the Detect Edges screen.
        Save the scan file.
        Scan job with detect edges should completed successfully.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738454

        3.Perform a scan job
        4.Select full in detect edges screen
        5.Click on Save button in preview screen
        Verify Save flyout shows
        Click on save button and verify image is saved

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738637

        Click "Save" button.
        Verify Save flyout shows.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738550
        """
        self.fc.fd["scan"].click_import_full_option()
        self.fc.fd["scan"].click_import_done_btn()
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
        try:
            self.driver.ssh.send_command(f'Remove-Item -Path "{flie_path}" -Force -ErrorAction SilentlyContinue', timeout=30)
        except Exception:
            sleep(2)
            self.driver.ssh.send_command(f'Remove-Item -Path "{flie_path}" -Force -ErrorAction SilentlyContinue', timeout=30, raise_e=False)

    @pytest.mark.regression
    def test_07_import_and_print_in_preview_c43738629(self):
        """
        3.Scan/Import an image from the scan intro page
        4.Check for print button on the preview screen
        Verify print button is shown

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738629
        """
        self.fc.fd["scan"].click_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

    @pytest.mark.regression
    def test_08_share_the_scan_file_c43738638_c43738551(self):
        """
        3.Perform a scan job
        4.Click on the "Share" button from the gallery preview screen
        Verify Share flyout shows, click on share button and verify share functionality

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738638

        Click "Share" button.
        Verify Share flyout shows.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738551
        """
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()
        self.fc.fd["scan"].click_dialog_share_btn()
        self.fc.fd["scan"].verify_share_picker_popup()
        self.fc.fd["scan"].dismiss_share_picker_popup()
        self.fc.fd["scan"].verify_share_picker_popup(invisible=True)