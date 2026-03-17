import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
import logging
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_07_push_awc_setup(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printers = cls.fc.fd["printers"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.printer_ip_address = cls.p.p_obj.ipAddress
        cls.bonjour_name = cls.p.get_printer_information()['bonjour name']
        cls.printer_name = cls.bonjour_name[cls.bonjour_name.find("HP ") + 3:cls.bonjour_name.find("series") - 1]
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        cls.pin_num = cls.p.get_pin()
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_printer_oobe_reset(self):
        """
        Precondition: Do an OOBE reset for printer
        Start and finish an OOBE_AWC setup flow.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12607633
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/12797882
        """
        logging.info("OOBE Reset for printer...")
        oobe_reset_printer = self.p.oobe_reset_printer()
        if not oobe_reset_printer:
            raise Exception("Printer OOBE reset failed")
        logging.info("Skip oobe flow...")
        self.p.exit_oobe()

    def test_02_go_to_connect_printer_to_wifi_screen(self):
        """
        Go through flow to  “Connect to Wi-Fi” screen
        """
        self.fc.go_home()
        self.home.verify_carousel_add_printer_title()
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen()
        self.printers.check_beaconing_printer_show(self.printer_name)
        printer = self.printers.search_printer(self.printer_name, beaconing_printer=True)
        printer.click()
        self.moobe.verify_we_found_your_printer_screen()
        self.moobe.select_continue()
        self.moobe.verify_access_wifi_password_dialog(self.ssid)
        self.moobe.select_continue()
        self.moobe.verify_connect_to_wifi_progress_screen()

    def test_03_check_need_more_time_dialog_after_5min(self):
        """
        Wait for the progress circle to go to the 2nd thermometer
        Wait for more than 5 minutes on the "Touch the checkmark..." modal
        Check UI layout, form and fit against the "Need more time?" modal
        Press "Cancel" or "x" on printer front panel when the "Touch the checkmark..." modal shows.
        Verify "Are you sure you want to cancel?" modal shows.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17464947(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17408587
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17464948
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17450907(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17450920(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17450927(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17465491
                  no fb
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17464892(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17464898
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25437451(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25437452(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/25437453
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29970871(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29970872
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29970875(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29970876(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29970877
        """
        if self.moobe.verify_touch_checkmark_dialog(raise_e=False):
            #Wait for 5 minutes when "Touch the checkmark on your printer display" modal 
            sleep(320)
            self.moobe.verify_need_more_time_dialog()
            self.moobe.click_dialog_try_again_btn()
            self.moobe.verify_touch_checkmark_dialog()
            self.p.click_front_panel_btn("fb_cancel")
            self.moobe.verify_are_you_sure_you_want_to_cancel_dialog()
            self.moobe.click_dialog_try_again_btn()
            self.moobe.verify_touch_checkmark_dialog()
            self.p.click_front_panel_btn("fb_cancel")
            self.moobe.verify_are_you_sure_you_want_to_cancel_dialog()
            self.moobe.click_exit_setup_btn()
            self.home.verify_home_screen(time=120)
            self.home.verify_carousel_add_printer_btn()
        if self.moobe.verify_press_info_btn_dialog(raise_e=False):
            #Wait for 5 minutes on "Press and release the flashing "Wi-Fi" button on your printer...." modal
            sleep(320)
            self.moobe.verify_need_more_time_dialog()
            self.moobe.click_dialog_try_again_btn()
            self.moobe.verify_touch_checkmark_dialog()
            self.p.press_cancel_btn()
            self.moobe.verify_are_you_sure_you_want_to_cancel_dialog()
            self.moobe.click_dialog_try_again_btn()
            self.moobe.verify_touch_checkmark_dialog()
            self.p.press_cancel_btn()
        self.moobe.verify_are_you_sure_you_want_to_cancel_dialog()
        self.moobe.click_exit_setup_btn()
        self.home.verify_home_screen(time=120)
        self.home.verify_carousel_add_printer_btn()
        