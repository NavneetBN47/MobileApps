import pytest
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_04_Align_Complete_Semi(object):
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
        
    def test_03_click_print_alignment_page_btn(self):
        """
        Click on Align Printheads
        Click "Print Alignment page" button

        Page should print and user should proceeds to Align 2 of 2

        https://hp-testrail.external.hp.com/index.php?/cases/view/15965730
        """
        if self.check_feature['align']:
            self.printer_settings.click_align_printheads_btn()
            self.printer_settings.verify_print_alignment_dialog()
            self.printer_settings.click_print_alignment_page_btn()
            self.printer_settings.verify_scan_alignment_dialog()

    def test_04_click_printing_cancel_btn(self):
        """
        Click on Align Printheads
        Click Cancel button

        Clean Printheads job should immediately end and dialogue should close and user returns to PQT screen.
        The alignment is canceled without any error and any dialog popping up.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965732
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965724
        """
        if self.check_feature['align']:
            self.printer_settings.click_alignment_back_btn()
            self.printer_settings.click_print_alignment_page_btn()
            self.printer_settings.click_dialog_cancel_btn()
            self.printer_settings.verify_print_quality_tools_page()
        
    def test_05_click_scan_exit_btn(self):
        """
        Click on Align Printheads
        Click Next button
        Click the Exit button on Align 2 of 2 page

        Dialogue should be dismissed and user returns to PQT screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/15965733
        """
        if self.check_feature['align']:
            self.check_feature['align'] = False
            self.printer_settings.click_align_printheads_btn()
            if self.printer_settings.verify_print_alignment_dialog(raise_e=False):
                self.printer_settings.click_print_next_btn()
                self.printer_settings.verify_scanning_dialog()
                if self.printer_settings.verify_alignment_complete_dialog(raise_e=False):
                    self.printer_settings.click_complete_close_btn()
                    self.printer_settings.verify_print_quality_tools_page()
                elif self.printer_settings.verify_scan_alignment_dialog(raise_e=False):
                    self.printer_settings.click_scan_exit_btn()
                    self.printer_settings.verify_print_quality_tools_page()
                    self.fc.restart_hp_smart()
                    self.home.verify_printer_settings_tile()
                    self.home.select_printer_settings_tile()
                    self.printer_settings.verify_printer_settings_page()
                    sleep(2)
                    self.printer_settings.select_print_quality_tools()
                    self.printer_settings.verify_print_quality_tools_page()
                    self.check_feature['align'] = True
                    sleep(2)             

    def test_06_alignment_complete_flow(self):
        """
        Click on Align Printheads
        Click Next button
        Click Scan Alignment page on Align 2 of 2

        Align Complete dialogue displays

        https://hp-testrail.external.hp.com/index.php?/cases/view/15965735
        https://hp-testrail.external.hp.com/index.php?/cases/view/15971746
        https://hp-testrail.external.hp.com/index.php?/cases/view/15971742
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965721
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965723
        """
        if self.check_feature['align']:
            self.printer_settings.click_align_printheads_btn()
            self.printer_settings.verify_print_alignment_dialog()
            self.printer_settings.click_print_next_btn()
            if self.printer_settings.verify_scan_alignment_dialog(raise_e=False):
                self.printer_settings.click_scan_alignment_page_btn()
                self.printer_settings.verify_scanning_dialog()
                self.printer_settings.verify_alignment_complete_dialog()
                self.printer_settings.click_complete_close_btn()
                self.printer_settings.verify_print_quality_tools_page()
                
