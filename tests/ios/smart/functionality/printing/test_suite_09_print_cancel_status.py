import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"

class Test_Suite_09_Print_Cancel_Status(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(cls.p.get_printer_information()["ip address"])

    def test_02_verify_print_cancel_pop_up_ui(self):
        """
        verify print progress and cancel buttons - C17128721
        """
        self.go_to_print_preview(no_of_photos=3)
        self.common_preview.select_button(self.common_preview.PRINT_BTN)
        self.common_preview.verify_an_element_and_click(self.common_preview.CANCEL_BUTTON)
        self.common_preview.verify_array_of_elements(self.common_preview.CANCEL_JOB_ELEMENTS)
        # Long timeout is to complete sending print job
        self.common_preview.verify_job_sent_and_reprint_buttons_on_print_preview(timeout=180)

    def test_03_verify_print_cancel_yes_button_functionality(self):
        """
        Select Yes on Cancel and verify printjob is cancelled and user back on preview screen - C25355762
        """
        self.go_to_print_preview(no_of_photos=10)
        self.common_preview.select_button(self.common_preview.PRINT_BTN)
        sleep(2)
        self.common_preview.verify_an_element_and_click(self.common_preview.CANCEL_BUTTON)
        assert self.common_preview.verify_an_element_and_click(self.common_preview.YES_BTN)
        self.common_preview.verify_printing_status_btn_changes()
        assert self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)

    def test_04_verify_print_cancel_no_button_functionality(self):
        """
        Select No on cancel button and verify print job is not interrupted - C25355763
        """
        self.go_to_print_preview(no_of_photos=3)
        self.common_preview.select_button(self.common_preview.PRINT_BTN)
        self.common_preview.verify_an_element_and_click(self.common_preview.CANCEL_BUTTON)
        assert self.common_preview.verify_an_element_and_click(self.common_preview.NO_BTN)
        # long timeout is to verify 10 pages print job completion
        self.common_preview.verify_printing_status_btn_changes(multi_print=True, timeout=250)
        assert self.common_preview.verify_title(self.common_preview.PRINT_PREVIEW_TITLE)

    def go_to_print_preview(self, no_of_photos=1):
        self.fc.select_multiple_photos_to_preview(no_of_photos=no_of_photos)
        self.common_preview.go_to_print_preview_pan_view(pan_view=False)