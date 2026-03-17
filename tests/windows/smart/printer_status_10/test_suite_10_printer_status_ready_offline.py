import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from SAF.misc import saf_misc
import MobileApps.resources.const.windows.const as w_const
from selenium.common.exceptions import NoSuchElementException

pytest.app_info = "GOTHAM"
class Test_Suite_10_Printer_Status_Ready_Offline(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printer_status = cls.fc.fd["printer_status"]
        cls.diagnose_fix = cls.fc.fd["diagnose_fix"]
        cls.serial_number = cls.p.get_printer_information()["serial number"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=True)

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
    
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        def tab_clean_up():
            self.web_driver.close_window(self.web_driver.current_window)
        request.addfinalizer(tab_clean_up)

    def test_01_go_home_and_add_a_printer(self):
        """
        add a printer
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)

    def test_02_check_printer_ready_status(self):
        """ 
        Verify "Ready" status shows with a green check mark on Main UI
        Verify "Ready" status shows on the printer information screen 
        Go to Printer Settings -> Printer Status Screen and check.

        https://hp-testrail.external.hp.com/index.php?/cases/view/13972833
        https://hp-testrail.external.hp.com/index.php?/cases/view/14595359
        https://hp-testrail.external.hp.com/index.php?/cases/view/14595830
        """
        if self.home.verify_carousel_printer_status('Ready', raise_e=False):
            cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element('carousel_printer_status_icon'))
            cur_img = saf_misc.img_crop(cur_img, 0.0, 0.0, 0.0, 0.0)
            toggle_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.STATUS_IMAGE + 'main_ui_ready.png'))
            assert saf_misc.img_comp(cur_img, toggle_img) < 0.4
            self.home.select_printer_settings_tile()
            self.printer_settings.verify_printer_info_status('Ready')
            self.printer_settings.select_printer_status_item()
            self.printer_status.verify_printer_ready_screen()

    def test_03_check_printer_offline_status(self):
        """       
        Turn off printer and wait for the Printer offline icon displayed on Main UI.
        Click back arrow on the title bar on Printer Status screen.

        Verify correct status icon shows on the main UI
        Verify correct status string shows on the main UI
        Verify correct ink level icons shows (If applicable)
        Go to Printer Settings -> Printer Status Screen and check.
        Verify Main UI shows after clicking back arrow (Win).

        https://hp-testrail.external.hp.com/index.php?/cases/view/14595861
        https://hp-testrail.external.hp.com/index.php?/cases/view/13972833
        https://hp-testrail.external.hp.com/index.php?/cases/view/14603896
        https://hp-testrail.external.hp.com/index.php?/cases/view/14598081
        """
        self.fc.trigger_printer_offline_status(self.p)
        self.fc.restart_hp_smart()
        if self.home.verify_carousel_printer_status('Printer offline', raise_e=False):
            cur_img = saf_misc.load_image_from_base64(self.driver.screenshot_element('carousel_printer_status_icon'))
            cur_img = saf_misc.img_crop(cur_img, 0.0, 0.0, 0.0, 0.0)
            toggle_img = saf_misc.load_image_from_file(ma_misc.get_abs_path(w_const.TEST_DATA.STATUS_IMAGE + 'main_ui_offline.png'))
            assert saf_misc.img_comp(cur_img, toggle_img) < 0.4  
            self.home.select_printer_settings_tile()
            printer_infor_status = self.printer_settings.get_printer_infor_status()
            if printer_infor_status not in ['Printer offline', 'Printer status unknown']:
                raise NoSuchElementException("printer status is not as expected")
            self.printer_settings.select_printer_status_item()
            self.printer_status.verify_printer_offline_screen()
            sleep(2)
            self.home.select_navbar_back_btn()

    def test_04_restore_printer_ready_status(self):
        """
        Fix the error condition

        https://hp-testrail.external.hp.com/index.php?/cases/view/13972833
        https://hp-testrail.external.hp.com/index.php?/cases/view/14610671
        """
        self.fc.restore_printer_online_status(self.p)
        if self.home.verify_home_screen(raise_e=False) is False:
            self.home.select_navbar_back_btn()
        if self.home.verify_carousel_printer_status('Ready', raise_e=False):
            self.home.select_printer_settings_tile()
            self.printer_settings.select_printer_information()
            self.printer_settings.verify_printer_info_status('Ready')
            self.printer_settings.select_printer_status_item()
            self.printer_status.verify_printer_ready_screen()

    def test_05_click_X_to_dismiss_info_con(self):
        """
        Dismiss the 1 message from Printer Status (acknowlodging/fix).

        Verify the message is removed and the other message(s) remains.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14610907
        """
        self.fc.trigger_printer_status(self.serial_number, ['65610', '65550', '65546'])
        for ioref in ['65610', '65550', '65546']:
            self.printer_status.verify_status_sorted_in_order(ioref)
        self.printer_status.click_info_x_btn('65550')
        for ioref in ['65610', '65550', '65546']:
            if ioref == '65550':
               assert self.printer_status.verify_status_sorted_in_order(ioref, raise_e=False) == False 
            else:
                self.printer_status.verify_status_sorted_in_order(ioref)

    def test_06_generate_an_error_con(self):
        """       
        Generate an error condition for this printer.
        Go to Printer Settings -> Printer Status Screen.

        Verify correct message shows in Printer Status.
        Verify the correct cartridge icon is seen if it's supply related.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14607173
        https://hp-testrail.external.hp.com/index.php?/cases/view/14607175
        https://hp-testrail.external.hp.com/index.php?/cases/view/14723461
        """
        self.fc.trigger_printer_status(self.serial_number, ['65610'])
        self.printer_status.check_ps_content_all('65610')

    def test_07_generate_a_warning_con(self):
        """       
        Generate a warning condition for this printer.
        Go to Printer Settings -> Printer Status Screen.

        Verify correct message shows in Printer Status.
        Verify the correct cartridge icon is seen if it's supply related.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14607179
        https://hp-testrail.external.hp.com/index.php?/cases/view/14610349
        """
        self.fc.trigger_printer_status(self.serial_number, ['65550'])
        self.printer_status.check_ps_content_all('65550')

    def test_08_generate_a_info_con(self):
        """       
        Generate a info condition for this printer.
        Go to Printer Settings -> Printer Status Screen.

        Verify correct message shows in Printer Status.
        Verify the correct cartridge icon is seen if it's supply related.

        https://hp-testrail.external.hp.com/index.php?/cases/view/14610460
        https://hp-testrail.external.hp.com/index.php?/cases/view/14610462
        """
        self.fc.trigger_printer_status(self.serial_number, ['65546'])
        self.printer_status.check_ps_content_all('65546')
        
    def test_09_click_back_arrow_with_different_size(self):
        """       
        Click Back arrow when app is at different sizes.

        Verify correct screen show. 

        https://hp-testrail.external.hp.com/index.php?/cases/view/14720972
        """
        self.home.select_navbar_back_btn()
        self.home.select_printer_settings_tile()
        self.printer_settings.select_printer_status_item()
        self.printer_status.check_ps_content_all('65546')
