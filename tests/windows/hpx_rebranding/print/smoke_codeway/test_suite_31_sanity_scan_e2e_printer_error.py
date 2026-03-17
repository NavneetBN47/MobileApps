import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
@pytest.mark.skip(reason="Skipping test suite temporarily due to ONESIM printer limitation.")
class Test_Suite_31_Sanity_Scan_E2E_Printer_Error(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name = cls.p.get_printer_information()['model name']
        cls.hostname = cls.p.get_printer_information()['serial number']


    @pytest.mark.smoke
    def test_01_add_a_printer(self):
        """
        Click on the printer card.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)

    @pytest.mark.smoke
    def test_02_trigger_printer_error_and_fixed(self):
        """
        Click on the printer card.
        """
        # Trigger a printer error during the scan job
        self.fc.trigger_printer_offline_status(self.p)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_printer_not_available_screen()

    @pytest.mark.smoke
    def test_03_fix_printer_error_and_fixed(self):
        """
        Click on the printer card.
        """
        # Fix the printer error 
        self.fc.restore_printer_online_status(self.p)
        self.fc.fd["scan"].click_back_arrow()

    @pytest.mark.smoke
    def test_04_scanning_with_printer_offline_error_c43738397(self):
        """
        [Unhappy path] Initial Scan with a printer error, fix and then continue to save/share/print.

        https://hp-testrail.external.hp.com/index.php?/cases/view/43738397
        """
        # Click on the scan tile.
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn()

        # Perform a scan job.
        # Verify that the preview screen is displayed with the image.
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen()

        # Click on the edit button in the preview screen.
        # Click on the 'Markup' button.
        # Make some changes in the settings.
        # Verify that changes are reflected in the image.
        self.fc.fd["scan"].click_image_edit_btn()
        self.fc.fd["scan"].verify_edit_screen()
        self.fc.fd["scan"].click_markup_item()
        self.fc.fd["scan"].verify_edit_makup_setting_screen()
        self.fc.fd["scan"].click_red_pen_btn()
        self.fc.fd["scan"].click_center_image()
        self.fc.fd["scan"].click_edit_done_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        # Save, share, or print the edited image.
        # Verify that the image is saved, shared, or printed successfully.
        # save
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

        # print
        self.fc.fd["scan"].click_print_btn()
        self.fc.fd["print"].verify_simple_print_dialog()
        self.fc.fd["print"].select_printer(self.hostname)
        self.fc.fd["print"].select_simple_print_dialog_print_btn()
        self.fc.fd["scan"].verify_scan_result_screen()

        # share
        self.fc.fd["scan"].click_share_btn()
        self.fc.fd["scan"].verify_share_dialog()
        self.fc.fd["scan"].click_dialog_share_btn()
        self.fc.fd["scan"].verify_share_picker_popup()
        self.fc.fd["scan"].dismiss_share_picker_popup()
        self.fc.fd["scan"].verify_share_picker_popup(invisible=True)