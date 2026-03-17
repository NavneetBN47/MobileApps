import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_05_Potg_Print_job_count(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        """
        Printer is remote
        Printer has Smart Driver capability
        Printer is not optimized
        Computer does not have smart driver installed
        User is HP+/UCDE
        """
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]
        cls.printers = cls.fc.fd["printers"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.scan = cls.fc.fd["scan"]
        cls.job_count = {}

        cls.stack = request.config.getoption("--stack")
        if 'pie' in cls.stack:
            pytest.skip("Skip this test as there is no remote printer with a pie account")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+", claimable=True)

    def test_01_sign_in_to_add_a_remote_printer(self):
        """
        Add the remote printer
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_remote_printer()
        self.fc.enable_print_anywhere_dialog()
        self.home.select_paw_x_btn()
        assert self.home.verify_print_anywhere_dialog(raise_e=False) is False  

    def test_02_switch_both_toggles_turn_on(self):
        """
        "Allow printing from Anywhere" toggle: ON
        "Require Private Pickup" toggle: ON      
        Send print job from "Print Documents"/"Print Photos"/"Scan Results"-Print icon.
        """
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_print_anywhere_option_display()
        self.printer_settings.select_print_anywhere()
        self.printer_settings.verify_print_anywhere_screen()
        self.printer_settings.switch_private_pickup_toggle(toggle='on')
        self.printer_settings.switch_printing_anywhere_toggle(toggle='on')
        self.home.select_navbar_back_btn()

    def test_03_sign_out_and_sign_in_again(self):
        """
        Sign out.
        Sign back with same HP+ account.
        Send print job from "Print Documents"/"Print Photos"/"Scan Results"-Print icon/"Scan Results"-Smart Task icon/"Smart Tasks" with print only ST.
        
        Verify print experience is remote.
        Verify print job is sent and not printed.
        Verify print job status is reflected in cloud que.

        https://hp-testrail.external.hp.com/index.php?/cases/view/27963763
        """
        self.fc.sign_out()
        assert self.home.verify_logged_in() is False
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        assert self.home.verify_logged_in() is not False

    def test_04_print_via_scan_results(self):
        """
        Send print job from "Scan Results"-Print icon.
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_scan_tile()
        self.scan.verify_new_scan_auto_enhancements_dialog()
        self.scan.click_get_started_btn()
        self.scan.verify_couldnt_connect_to_scanner_screen()

        self.scan.select_import_btn()
        self.scan.verify_import_dialog()
        self.scan.click_import_dialog_get_started_btn()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
        self.scan.verify_import_screen()
        self.scan.click_import_apply_btn()
        self.scan.verify_scan_result_screen()

        self.scan.click_print_btn()
        self.print.start_a_remote_print(type='doc')
        self.scan.verify_scan_result_screen()

    def test_05_print_via_print_photos(self):
        """
        Send print job from "Print Photos"-Print icon.
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_print_photos_tile()
        self.__print_via_cloud(w_const.TEST_DATA.FISH_PNG, type='photo')
        
    def test_06_check_job_count_when_sign_out(self):
        """
        Sign out the user account

        Verify job count is removed from printer card.

        https://hp-testrail.external.hp.com/index.php?/cases/view/28564515
        """
        self.home.verify_job_count_info()
        assert self.home.get_job_count_num() == 2  
        self.fc.sign_out()
        assert self.home.verify_logged_in() is False
        assert self.home.verify_job_count_info(raise_e=False) is False
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        assert self.home.verify_logged_in() is not False
        self.home.verify_job_count_info()
        assert self.home.get_job_count_num() == 2

    def test_07_print_via_print_documents(self):
        """
        Send print job from "Print Documents"-Print icon.
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_print_documents_tile()
        self.__print_via_cloud(w_const.TEST_DATA.ONE_PAGE_DOC, type='doc')

    def test_08_check_job_count_is_updated(self):
        """
        Send a few print jobs to printer
        Add 1 or more print jobs
        Leave and return home
        Check job count.
        
        Verify the job count shows on printer card.
        Verify the job count number matches the numbers of print job in cloud queue.
        Verify job count is updated correctly
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/28564510
        https://hp-testrail.external.hp.com/index.php?/cases/view/28564512
        """
        self.home.verify_job_count_info()
        assert self.home.get_job_count_num() == 3      

    def test_09_check_job_count_is_decreased(self):
        """
        Click on the job count on printer card
        Verify The portal webview opens to Private Pickup Files.

        https://hp-testrail.external.hp.com/index.php?/cases/view/28564511

        Check the job count on printer card
        Print 1 or more print jobs. or remove some print jobs
        Leave and return home
        Check job count.
        Verify job count is decreased correctly

        https://hp-testrail.external.hp.com/index.php?/cases/view/28564513
        https://hp-testrail.external.hp.com/index.php?/cases/view/28564515
        """
        self.__delete_pp_files(2)
        self.home.select_navbar_back_btn()
        self.home.verify_job_count_info()
        assert self.home.get_job_count_num() == 1

    def test_10_clear_private_pickup_files(self):
        """
        Clear all the Private Pickup Files
        "Ready to receive files for print" text shows
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        if self.home.verify_job_count_info(raise_e=False, timeout=45):
            self.__delete_pp_files(5)

    def test_11_restore_print_anywhere_toggle(self):
        """
        "Allow printing from Anywhere" toggle: On
        "Require Private Pickup" toggle: Off
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_printer_settings_tile()
        self.printer_settings.restore_print_anywhere_toggle()

        
    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __print_via_cloud(self, file_name, type):
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(file_name)
        self.print.verify_ipp_print_screen_no_preview_image(raise_e=False)
        self.print.start_a_remote_print(type=type)
        self.home.verify_home_screen()

    def __delete_pp_files(self, num):
            self.home.click_job_count_text()
            self.printer_settings.verify_private_pickup_screen()
            for _ in range(num):
                if not self.printer_settings.verify_no_files_print():
                    self.printer_settings.click_pp_del_button()
                    self.printer_settings.verify_are_you_sure_dialog()
                    self.printer_settings.click_dialog_del_button()
                    sleep(2)
                else:
                    break
