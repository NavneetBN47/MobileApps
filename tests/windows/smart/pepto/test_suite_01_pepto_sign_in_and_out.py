import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_01_Pepto_Sign_In_And_Out(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.pepto = cls.fc.fd["pepto"]
        cls.home = cls.fc.fd["home"]
        cls.shortcuts = cls.fc.fd["shortcuts"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.hpid = cls.fc.fd["hpid"]

        cls.build_version = (cls.driver.session_data["app_info"])[pytest.app_info].split('-')[1]

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
        self.fc.select_a_printer(self.p)
        sleep(3)

        self.pepto.enable_pepto_log(self.build_version)
        assert self.pepto.verify_pepto_log_file_created() == True

    def test_02_person_icon_sign_in_and_out(self): 
        """
        Sign in via person icon 
        Sign out of HPID account

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554621
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27674426
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554622
        """  
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.sign_out()

    def test_03_shortcus_tile_sign_in_and_out(self): 
        """
        Sign in via Shortcuts tile

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554635
        """  
        sleep(3)
        self.home.select_shortcuts_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()
        self.ows_ucde_value_prop.select_native_value_prop_buttons(1)
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login(self.login_info["email"], self.login_info["password"])
        self.shortcuts.verify_shortcuts_screen()
        self.home.select_navbar_back_btn()

        self.fc.sign_out()

    def test_04_check_pepto_data(self):
        """
        Verify HTTP RESULT=Created (201) shows in "Pdsmq.Data.txt" file.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15541202
        """ 
        check_event_list = ['HTTP RESULT=Created \(201\)'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_05_check_pepto_data(self):
        """
        Sign in via person icon

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554621
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27674426
        """ 
        check_event_list = ['"login_action":"Login","login_method":"Manual","app_flow":"HpcSignIn","result":"success"', 
                            '"hpid_sub"', '"fq_tenant_id"', '"moniker":"x-cscr_gotham_report_hpclogin_summary/1.0"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_06_check_pepto_data(self):
        """
        Sign out via person icon

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554622
        """ 
        check_event_list = ['"schema":"app_eventinfo/2.0.1","app_event_actor":"user","app_event_action":"clicked","app_event_object":"tile","app_event_object_label":"/GroupFunctions#HpcSignOut"', '"schema":"app_eventinfo/2.0.1","app_event_actor":"app","app_event_action":"displayed","app_event_object":"screen","app_event_object_label":"/HpcSignOut.flow/HpcSignOutPage"', '"launch_from":"UserOnboardingLogout","cumulative_state":"User,StartSession,GetSetupCommands,Finished,EndSession,OwsUserCmplt,","onboarding_type":"signout","sort_id":"","dev_productnumber":"unknown"', '"login_action":"Logout"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_07_check_pepto_data(self):
        """
        Sign in via Shortcuts tile

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554635
        """ 
        check_event_list = ['"app_event_details":{"login_action":"Login","login_method":"Manual","app_flow":"SmartTasks","result":"success","app_deployed_uuid":"System.Threading.Tasks.Task`1\[System.String\]"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)

    def test_08_check_pepto_data(self):
        """
        Verify correct value program level shows in the pepto log value could be "Base", "HPplus", "UCDE"

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/28862808
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29880324
        """ 
        check_event_list = ['"user_programlevel"', '"productivity-bundle-entitlement"'] 

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event)
