import pytest
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_03_Scan_Scanner(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.scan = cls.fc.fd["scan"]
  
        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=False)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        

    def test_01_click_cancel_while_scanning(self):
        """
        Click "Scan" tile on the main page.
        Click the "Scan" button./Click the "Preview" button. 
        Verify the scan setting right panel doesn't show during scanning.
        Click Cancel button while scanning.
        Verify "Scan Canceled" dialog pops up.
        Verify the scan job is canceled on printer.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064656
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14680826
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28581029
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072339
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572579
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235492 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235308 
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28581028
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235259
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14072232
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13235754
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13159661
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13792492
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.select_scan_tile()
        self.scan.verify_scan_intro_page()
        self.scan.click_get_started_btn()
        self.scan.verify_camera_tab_not_display()
        self.scan.click_scan_btn()
        # self.driver.ssh.send_command("netsh wlan disconnect")
        sleep(3)
        self.home.verify_navbar_back_btn_is_disabled()
        sleep(2)
        self.scan.click_cancel_btn()
        self.scan.verify_scan_canceled_dialog(60)
        self.scan.click_scan_canceled_x_btn()
        self.scan.click_preview_btn()
        self.scan.verify_scanner_preview_screen()
        self.home.select_navbar_back_btn()
        self.home.select_scan_tile()
        self.scan.verify_scanner_screen()
        self.scan.click_preview_btn()
        self.scan.click_cancel_btn()
        self.scan.verify_scan_canceled_dialog(60)
        self.scan.click_scan_canceled_x_btn()

    def test_02_scan_with_2_sided(self):
        """
        Make sure the "Source" value is “Document Feeder".
        Check the 2-Sided option and click "Scan"..
        Verify the 2-Sided is unchecked by default.
        Verify the scan job can be completed successfully.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13793680
        """
        so = self.scan.verify_source_dropdown()
        if so.get_attribute("IsEnabled").lower() == "true":
            self.scan.select_dropdown_listitem(self.scan.SOURCE, "Document Feeder")
            if self.scan.verify_2_sided_box_displays(raise_e=False):
                self.scan.verify_2_sided_box_is_off()
                self.scan.click_2_sided_box()
                self.scan.click_scan_btn()
                self.scan.verify_scan_result_screen()
                self.home.select_navbar_back_btn(return_home=False)
                self.scan.verify_exit_without_saving_dialog()
                self.scan.click_yes_btn()
                self.scan.verify_scanner_screen()
            else:
                logging.info("This priner does not 2-sided setting")
        else:
            logging.info("This priner does not support ADF")

    def test_03_scan_with_high_resolution(self):
        """
        Set the Resolution to 1200 dpi (high resolution)
        Select Edit from flyout menu
        Verify warning dialog shows in the Edit screen while the scanned image is loading to Edit screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29367745
        """
        self.scan.select_resolution_dropdown()
        if self.scan.verify_dropdown_listitem("1200 dpi", raise_e=False):
            self.scan.verify_dropdown_listitem("1200 dpi").click()
            self.scan.click_scan_btn()
            self.scan.verify_scan_result_screen(300)
            sleep(2)
            self.scan.click_menu_btn()
            self.scan.click_edit_btn()
            self.scan.verify_processing_scan_dialog()
        else:
            pytest.skip("The printer not support 1200 dpi, can not do this test")
