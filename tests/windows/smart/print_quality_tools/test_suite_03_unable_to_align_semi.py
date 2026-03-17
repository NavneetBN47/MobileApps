import pytest
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_03_Unable_To_Align_Semi(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.check_feature = {}

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_go_home_and_add_a_printer(self):
        self.fc.go_home()
        self.fc.select_a_printer(self.p)

    def test_02_check_align_feature_is_available(self):
        """ 
        Verify "This feature is not available for the selected printer. On some printers, you might be able to access Advanced Settings under Settings System Service to perform print quality actions." is not show 
        """
        self.home.verify_printer_settings_tile()
        self.home.select_printer_settings_tile()
        self.fc.enter_printer_pin_number(self.p.get_pin())
        self.printer_settings.verify_printer_settings_page()
        sleep(2)
        self.printer_settings.select_print_quality_tools()
        self.printer_settings.verify_print_quality_tools_page()
        if not self.printer_settings.verify_this_feature_is_not_screen():
            self.check_feature['align'] = self.printer_settings.verify_align_printheads_part(raise_e=False)
        else:
            self.check_feature['align'] = False
        
    def test_03_click_print_back_btn(self):
        """
        Click on Align Printheads
        Click the back arrow

        Dialogue should be dismissed and user returns to PQT screen
        The Alignment Dialogue 1 of 2 should appear.
        Next button / Back arrow / Print Alignment Page button

        https://hp-testrail.external.hp.com/index.php?/cases/view/15965726
        https://hp-testrail.external.hp.com/index.php?/cases/view/15971738      
        https://hp-testrail.external.hp.com/index.php?/cases/view/15971736
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965727
        """
        if self.check_feature['align']:
            self.printer_settings.click_align_printheads_btn()
            self.printer_settings.verify_print_alignment_dialog()
            self.printer_settings.click_alignment_back_btn()
            self.printer_settings.verify_print_quality_tools_page()

    def test_04_click_print_next_btn(self):
        """
        Click on Align Printheads
        Click the Next button
        Click the Back arrow

        User should proceed to Align Dialogue 2 of 2
        Exit button / Back arrow / Scan Alignment Page button
        User should return to Align Dialogue 1 of 2

        https://hp-testrail.external.hp.com/index.php?/cases/view/15965728
        https://hp-testrail.external.hp.com/index.php?/cases/view/15971740
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965729
        """
        if self.check_feature['align']:
            self.printer_settings.click_align_printheads_btn()
            self.printer_settings.verify_print_alignment_dialog()
            self.printer_settings.click_print_next_btn()
            self.printer_settings.verify_scan_alignment_dialog()
            self.printer_settings.click_alignment_back_btn()
            self.printer_settings.verify_print_alignment_dialog()

    def test_05_unable_to_align_flow(self):
        """
        Click on Align Printheads
        Print Alignment Page button
        Click Scan Alignment page

        Unable to Align dialogue displays with Back button (Scan page is NOT loaded into scan bed)
        Clicking Back button should allow user to go back and then complete alignment process

        https://hp-testrail.external.hp.com/index.php?/cases/view/15965734
        https://hp-testrail.external.hp.com/index.php?/cases/view/15971744
        """
        if self.check_feature['align']:
            self.printer_settings.click_print_alignment_page_btn()
            if self.printer_settings.alignment_is_not_finished_dialog():
                self.printer_settings.click_dialog_cancel_btn()
            else:
                self.printer_settings.verify_scan_alignment_dialog()
                self.printer_settings.click_scan_alignment_page_btn()
                self.printer_settings.verify_scanning_dialog()
                if self.printer_settings.verify_unable_to_align_dialog(raise_e=False):
                    self.printer_settings.click_unable_align_back_btn()
                    assert self.printer_settings.verify_unable_to_align_dialog(raise_e=False) is False
                elif self.printer_settings.verify_alignment_complete_dialog(raise_e=False):
                    self.printer_settings.click_complete_close_btn()
                    assert self.printer_settings.verify_alignment_complete_dialog(raise_e=False) is False
