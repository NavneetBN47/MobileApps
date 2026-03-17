import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

class LogStringFoundException(Exception):
    pass

pytest.app_info = "GOTHAM"
class Test_Suite_06_Home_Tiles_Gen1_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        try:
            printer_gen_type = cls.p.get_printer_gen()
        except Exception as e:
            pytest.skip("Skip this test: " + str(e))
        if "gen1" not in printer_gen_type:
            pytest.skip("Non Gen1 printer is not suitable for this testing")

        cls.home = cls.fc.fd["home"]
        cls.printer = cls.fc.fd["printers"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_check_gotham_log_gen1_printer(self):
        """
        Add a network non-Gen 2 printer to main UI, verify log does not contain "foreign-access" 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17843699  
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064328(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24218227(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/24218229(low)
        """
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        if self.printer.verify_pin_dialog(raise_e=False) is not False:
            if self.printer.input_pin(self.p.get_pin()) is True:
                self.printer.select_pin_dialog_submit_btn()

        self.home.verify_main_page_tiles()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.verify_print_anywhere_option_is_hidden()
        
        check_string = "foreign-access"
        with self.driver.ssh.remote_open(w_const.TEST_DATA.HP_SMART_LOG_PATH) as f:
            data = f.read().decode("utf-8")
        if check_string not in data:
            return True
        raise LogStringFoundException("HP Smart should not call {} API".format(check_string))
