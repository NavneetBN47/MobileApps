import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.mac.smart.utility import smart_utilities


pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_04_Ios_Smart_Scan_cancel_print_performance(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_info = cls.p.get_printer_information()
        cls.stack = request.config.getoption("--stack")
        cls.scan = cls.fc.fd["scan"]
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.home = cls.fc.fd["home"]
        cls.fc.go_home(stack=cls.stack)
        def clean_up_class():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)

    def test_01_validate_scan_cancel_msg(self):
        """
        C31299817 - Verify Cancel button functionality while scanning process is in progress
        C31299845 - Validate message while cancelling scan job
        C31299865 - Verify scan can be performed after cancelling scan job
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip test on MAC")
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button(verify_messages=False)
        self.scan.verify_scanning_screen()
        self.scan.select_cancel_scanning_job()
        self.scan.verify_scan_canceling_msg()
        self.scan.verify_scan_button()
        self.scan.select_scan_job_button()

    def test_02_perform_multiple_scans_and_print(self):
        """
        C31299834 - Validate message while cancelling scan job
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip test on MAC")
        page_count = 10
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(no_of_pages=page_count)
        assert self.common_preview.verify_preview_page_info()[1] == page_count
        # long timeout is to verify 10 pages print job completion
        self.fc.select_print_button_and_verify_print_job(self.p, timeout=500)

    def test_03_print_performance(self):
        """
        IOS & MAC:
        C31297709 - Validate Printing of 10 pages PDF
        C32065234 - Verify Print Preview Page layout
        """
        test_file = "ten_page_pdf"
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, test_file, no_of_pages=10)
        self.fc.select_a_file_and_go_to_print_preview(test_file)
        #long timeout is to verify 10 pages print job completion
        self.fc.select_print_button_and_verify_print_job(self.p, timeout=500)