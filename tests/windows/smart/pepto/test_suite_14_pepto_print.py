import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const

pytest.app_info = "GOTHAM"
class Test_Suite_14_Pepto_Print(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.print = cls.fc.fd["print"]

        cls.build_version = (cls.driver.session_data["app_info"])[pytest.app_info].split('-')[1]
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_add_printer_and_enable_pepto(self):
        """
        Enable the Pepto log.
        Launch the app to Main UI
        """  
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        sleep(3)

        self.pepto.enable_pepto_log(self.build_version)
        assert self.pepto.verify_pepto_log_file_created() == True  

    def test_02_print_photos_flow(self):
        """
        Send a local print job to local Printer.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961264
        """
        self.home.select_print_photos_tile()
        self.print.verify_file_picker_dialog()
        self.print.input_file_name(w_const.TEST_DATA.AUTUMN_JPG)
        self.print.verify_simple_print_dialog()
        self.print.select_printer(self.hostname)
        self.print.select_print_dialog_print_btn()
        self.home.verify_home_screen()
        
        sleep(1)
        self.driver.terminate_app()

    def test_03_check_pepto_data(self):
        """
        Send a local print job to local Printer.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15961264
        """ 
        check_event_list = ['"app_event_actor":"self","app_event_action":"initiated","app_event_object":"task","app_event_object_label":"task_print_basic"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
    
    
