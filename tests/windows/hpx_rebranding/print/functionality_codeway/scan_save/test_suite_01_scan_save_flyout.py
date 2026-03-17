import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep
import logging


pytest.app_info = "HPX"
class Test_Suite_01_Scan_Save_Flyout(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)        
        cls.printer_name = cls.p.get_printer_information()["model name"]

        
    @pytest.mark.regression
    def test_01_check_scan_save_flyout_C43738443_C43738463_C43738462(self):
        """
        Verify "Scanning..." screen UI
        Click "Save" button in Preview screen, verify Save flyout shows
        Save Flyout UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738443
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738463
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738462
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_scan_tile()
        self.fc.fd["scan"].verify_scan_btn(timeout=30)
        self.fc.fd["scan"].click_scan_btn()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scan_result_screen(timeout=60)
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()

    @pytest.mark.regression
    def test_02_click_save_flyout_cancel_btn_C43738469(self):
        """
        Click "Cancle" button in Save flyout, verify Save flyout is dissmissed

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738469
        """
        self.fc.fd["scan"].click_dialog_cancel_btn()
        self.fc.fd["scan"].verify_save_dialog(invisible=True)

    @pytest.mark.regression
    def test_03_click_save_flyout_save_btn_C43738468(self):
        """
        Click "Save" button in Save flyout, verify file is successfully saved

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/43738468
        """
        self.fc.fd["scan"].click_save_btn()
        self.fc.fd["scan"].verify_save_dialog()
        file_name = self.fc.fd["scan"].get_current_file_name()
        self.fc.fd["scan"].click_dialog_save_btn()
        sleep(1)
        self.fc.fd["scan"].click_save_as_dialog_save_btn()
        self.fc.fd["scan"].verify_file_saved_dialog()
        file_path = self.fc.fd["scan"].verify_the_saved_file_name_is_correct(file_name)
        logging.info(f"Saved Path: {file_path}")
        self.fc.fd["scan"].click_dialog_close_btn()
        self.driver.ssh.send_command("del " + file_path)