import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

# Longer wait times in this test suite are to accommodate printing verification
class Test_Suite_05_Print_Status(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver, cls.web_driver)
        cls.common_preview = cls.fc.fd["common_preview"]
        cls.printers = cls.fc.fd["printers"]
        cls.home = cls.fc.fd["home"]
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        # Printer variables
        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(cls.p.get_printer_information()["ip address"])

    def test_01_verify_multi_printing_button(self):
        """
        verify multi print progress btn and cancel buttons - C31297252
        """
        if pytest.platform == "MAC":
            # Defect link: https://hp-jira.external.hp.com/browse/AIOI-21057
            pytest.skip("Skip this test on MAC platform because of defect while selecting multiple photos")
        self.go_to_print_preview(no_of_photos=2)
        self.common_preview.select_button(self.common_preview.PRINT_BTN)
        # Printing times varies on every printer and need long timeout to verify print job status
        self.common_preview.verify_printing_status_btn_changes(multi_print=True, timeout=120)

    def test_05_verify_print_reprint_and_done_buttons(self):
        """
        verify print, re-print and done button functionality on print preview screen-
                C17128720, C17128723, C27099491
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.fc.go_to_home_screen()
        self.go_to_print_preview(no_of_photos=1)
        self.common_preview.select_button(self.common_preview.PRINT_BTN)
        self.common_preview.verify_printing_status_btn_changes()
        self.common_preview.verify_an_element_and_click(self.common_preview.RE_PRINT_BTN)
        self.common_preview.verify_job_sent_and_reprint_buttons_on_print_preview()
        self.common_preview.verify_an_element_and_click(self.common_preview.DONE_BUTTON)
        assert self.home.verify_home_tile()

    def test_06_verify_print_button_with_no_printer_added(self):
        """
         Verify Print button disabled when no printer added , add printer and print - C17128725
        """
        if pytest.platform == "MAC":
            pytest.skip("Skip this test on MAC platform")
        self.fc.go_to_home_screen()
        self.fc.remove_default_paired_printer()
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.common_preview.go_to_print_preview_pan_view(pan_view=False)
        assert self.common_preview.verify_printer_name_displayed("Choose your Printer")
        print_btn = self.common_preview.verify_button(self.common_preview.PRINT_BTN)
        assert print_btn, "Cannot find {}".format(self.common_preview.PRINT_BTN)
        assert self.common_preview.is_button_enabled(self.common_preview.PRINT_BTN) is False
        self.common_preview.verify_an_element_and_click("choose_your_printer_option")
        self.printers.verify_printers_nav()
        self.printers.select_printer_from_printer_list(self.p.get_printer_information()["ip address"], timeout=180)
        assert self.common_preview.verify_printer_name_displayed(self.p.get_printer_information()['bonjour name'], delay=5)
        print_btn = self.common_preview.verify_button(self.common_preview.PRINT_BTN)
        assert print_btn, "Cannot find {}".format(self.common_preview.PRINT_BTN)
        assert self.common_preview.is_button_enabled(self.common_preview.PRINT_BTN)
        self.fc.select_print_button_and_verify_print_job(self.p)

    def go_to_print_preview(self, no_of_photos=1):
        if pytest.platform == "MAC":
            self.home.dismiss_tap_account_coachmark()
        self.home.close_smart_task_awareness_popup()
        self.fc.select_multiple_photos_to_preview(no_of_photos=no_of_photos)
        self.common_preview.go_to_print_preview_pan_view(pan_view=False)