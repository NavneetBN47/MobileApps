import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_08_Printing_From_Diff_File_Sources(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.scan = cls.fc.fd["scan"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(cls.p.get_printer_information()["ip address"])

    def test_01_verify_printing_from_print_documents_tile(self):
        """
        IOS & MAC:
        verify_printing_from_print_documents- C31297387
        """
        file_name= "test_pdf_file"
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, file_name)
        self.fc.select_a_file_and_go_to_print_preview(file_name)
        self.fc.select_print_button_and_verify_print_job(self.p)
        self.common_preview.select_done()  # after print job we are clicking done button to go back to home screen, so that we can delete the file
        self.fc.go_hp_smart_files_and_delete_all_files()

    def test_03_verify_printing_from_camera_scan_tile(self):
        """
        verify_printing_from_print_photos- C31297389
        """
        if pytest.platform == "MAC":
            pytest.skip("This test is not supported on MAC")
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.multiple_manual_camera_capture(1)
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_04_verify_printing_from_print_scan_tile(self):
        """
        IOS & MAC:
        verify_printing_from_print_photos- C31297390
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        if pytest.platform == "IOS":
            self.common_preview.nav_detect_edges_screen()
        else:
            self.scan.verify_top_navbar_button_and_click("scan_print_btn", raise_e=False)
            self.scan.enter_full_screen_mode()
        self.fc.select_print_button_and_verify_print_job(self.p)