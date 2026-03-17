import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_05_Home_CEC(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.cec = cls.fc.fd["cec"]
        cls.hpid = cls.fc.fd["hpid"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.stack = request.config.getoption("--stack")
        if cls.stack == "stage":
            login_info = ma_misc.get_smb_account_info("stage_journey_testing")
        else:
            login_info = ma_misc.get_smb_account_info(cls.stack)
        cls.username, cls.password = login_info["email"], login_info["password"]

    def test_01_add_xml_file(self):
        """
        Add <CustomFeatures>UseTenancyLogin</CustomFeatures> to LoggingData.xml
        """
        self.driver.terminate_app()
        self.home.add_usetanancylogin_msg()
    
    def test_02_sigin_in_from_cec(self):
        """
        Install the latest app
        Launch the app to the main page
        make sure user is not signed in
        perform sign in action form CEC tile
        Verify org picker shows
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30717288
        """
        self.fc.go_home()
        self.home.verify_cec_banner()
        if self.cec.verify_see_all_btn(raise_e=False):
            self.cec.click_see_all()
            self.cec.verify_do_more_with_hp_smart_screen(timeout=30)
        self.cec.verify_unlock_cloud_features_tile()
        self.cec.click_unlock_cloud_features_tile()
        self.cec.verify_create_account_or_sign_in_screen()
        self.cec.click_sign_in_btn()
        self.fc.handle_web_login(username=self.username, password=self.password)
        self.home.verify_welcome_back_dialog()
        