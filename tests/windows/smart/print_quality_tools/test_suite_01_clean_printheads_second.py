import pytest
from time import sleep
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_01_Clean_Printheads_Second(object):
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

    def test_02_check_clean_feature_is_available(self):
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
            self.check_feature['clean'] = self.printer_settings.verify_clean_printheads_part(raise_e=False)
        else:
            self.check_feature['clean'] = False

    def test_03_click_cleaning_second_cancel_btn(self):
        """
        Select Print Quality Tools
        Click on Clean Printheads
        Click on Second Level Clean button
        Click Cancel button

        Verify Clean Printheads job should immediately end and dialogue should close.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15965720
        """
        if self.check_feature['clean']:
            self.printer_settings.click_clean_printheads_btn()
            self.printer_settings.verify_cleaning_dialog_1()
            self.printer_settings.verify_cleaning_dialog_2()
            self.printer_settings.verify_second_cleaning_dialog()
            sleep(20)
            self.printer_settings.click_cleaning_second_btn()
            if not self.printer_settings.verify_cleaning_dialog_1(raise_e=False):
                sleep(20)
                self.printer_settings.click_retry_btn()
                self.printer_settings.verify_cleaning_dialog_1()
            self.printer_settings.click_dialog_cancel_btn()

    def test_04_restart_app_and_go_to_printer_settings_screen(self):
        if self.check_feature['clean']:
            self.fc.restart_hp_smart()
            self.home.verify_printer_settings_tile()
            self.home.select_printer_settings_tile()
            self.printer_settings.verify_printer_settings_page()
            sleep(2)
            self.printer_settings.select_print_quality_tools()
            self.printer_settings.verify_print_quality_tools_page()

    def test_05_click_second_dialog_done_btn(self):
        """
        Click on Printer Settings
        Select Print Quality Tools
        Click on Clean Printheads
        Click Close/Done button when finished

        Should clean printheads. Dialogue should close after clicking Close/Done button afterwards. 
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965689
        https://hp-testrail.external.hp.com/index.php?/cases/view/15971722
        https://hp-testrail.external.hp.com/index.php?/cases/view/15971724
        https://hp-testrail.external.hp.com/index.php?/cases/view/15965689
        """
        if self.check_feature['clean']:
            self.printer_settings.click_clean_printheads_btn()
            if not self.printer_settings.verify_cleaning_dialog_1(raise_e=False):
                sleep(20)
                self.printer_settings.click_retry_btn()
            self.printer_settings.verify_cleaning_dialog_1()
            self.printer_settings.verify_cleaning_dialog_2()
            self.printer_settings.verify_second_cleaning_dialog()
            self.printer_settings.click_cleaning_done_btn()

        