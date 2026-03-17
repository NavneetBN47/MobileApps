import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from MobileApps.resources.const.ios.const import *

pytest.app_info = "GOTHAM"
class Test_Suite_13_Pepto_Mobile_fix(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.mobile_fax = cls.fc.fd["softfax_home"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.build_version = (cls.driver.session_data["app_info"])[pytest.app_info].split('-')[1]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

    def test_01_go_home_and_enable_pepto(self):
        """
        Enable the Pepto log.
        Launch the app to Main UI
        """  
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        sleep(3)

        self.pepto.enable_pepto_log(self.build_version)
        assert self.pepto.verify_pepto_log_file_created() == True
        
    def test_02_click_mobile_fax_tile(self):
        """
        Click on the "Mobile Fax"

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17165413  
        """
        self.home.select_mobile_fax_tile()
        self.mobile_fax.verify_mobile_fax_home_screen()

        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()

    def test_03_mobile_fix_in_bell_icon(self):
        """
        Click "Mobile Fax" option under the bell icon

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/19410630 
        """
        self.home.select_activity_btn()
        self.home.click_mobile_fax_listview()
        self.mobile_fax.verify_mobile_fax_home_screen()

        self.home.select_navbar_back_btn()
        self.home.verify_home_screen()

        sleep(1)
        self.driver.terminate_app()

    def test_04_check_pepto_data(self):
        """
        verify the pepto log shows #SoftFax tile click event.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/17165413  
        """ 
        check_event_list = ['"schema":"app_eventinfo/2.0.1","app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#SoftFax"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_05_check_pepto_data(self):
        """
        Click "Mobile Fax" option under the bell icon

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/19410630 
        """ 
        check_event_list = ['"schema":"app_eventinfo/2.0.1","app_event_actor":"user","app_event_action":"clicked","app_event_object":"button","app_event_object_label":"/MainPage-Menu#SoftFax"']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_06_shortcuts_cleanup(self):
        self.fc.del_shortcuts(w_const.TEST_TEXT.TEST_TEXT_01)
   