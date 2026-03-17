import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_09_User_Onboarding_Tiles_Print_Photos(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.hostname = cls.p.get_printer_information()["host name"][:-1]
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.ows_ucde_value_prop = cls.fc.fd["ows_value_prop"]
        cls.print = cls.fc.fd["print"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

        cls.fc.go_home()
        cls.fc.select_a_printer(cls.p)
        cls.home.verify_carousel_printer_image()


    @pytest.mark.parametrize("buttons", ["create_account", "sign_in"])
    def test_01_close_sign_in_up_dialog(self, buttons):
        """
        Click "X" button on the HPID Sign in/Create account dialog, verify user navigates to the Home page
        First time launch the app with any other region than china and click on the Print Photos and Print Documents tile, verify tile is locked

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997911
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/29777810
        """
        self.home.select_print_photos_tile()
        if self.home.verify_install_to_print_dialog(raise_e=False):
            self.home.select_install_printer_btn()
            self.home.verify_installing_printer_dialog()
            self.home.verify_success_printer_installed_dialog(timeout=120)
            self.home.select_success_printer_installed_ok_btn()
            self.home.verify_home_screen()
            self.home.select_print_photos_tile()
            
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()

        if buttons == "create_account":
            self.ows_ucde_value_prop.select_native_value_prop_buttons(index=0)
            self.fc.verify_hp_id_sign_in_up_page(is_sign_up=True)
        else:
            self.ows_ucde_value_prop.select_native_value_prop_buttons(index=1)
            self.fc.verify_hp_id_sign_in_up_page()

        self.fc.close_hp_id_sign_in_up_page()

    @pytest.mark.parametrize("buttons", ["sign_in", "close", "create_account"])
    def test_02_user_onboarding_flow_via_print_photos_tile(self, buttons):
        """
        Click "Print Photos" tile without signed in, verify OWS UCDE value prop shows for Print Photos
        (+)Create Account via any locked tile, verify flow continues and the user is onboarded
        Sign in via any Tile, verify flow continues and user is onboarded
        Click "Close" button on the OWS value prop, verify user navigates to Home Page
        Print photo locally (not signed in), verify output and that Simple photo Print dialog is received 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731300
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731497
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27731496
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997910
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14064335
        """
        self.home.select_print_photos_tile()
        self.ows_ucde_value_prop.verify_ows_ucde_value_prop_screen()

        if buttons == "create_account":
            self.ows_ucde_value_prop.select_native_value_prop_buttons(index=0)
            self.fc.handle_web_login(create_account=True)
            self.print.verify_file_picker_dialog(timeout=60)
            self.print.select_file_picker_dialog_cancel_btn()
            self.home.verify_home_screen()
        elif buttons == "sign_in":
            self.ows_ucde_value_prop.select_native_value_prop_buttons(index=1)
            self.fc.handle_web_login(username=self.login_info["email"], password=self.login_info["password"])
            self.print.verify_file_picker_dialog(timeout=60)
            self.print.input_file_name(w_const.TEST_DATA.WOMAN_BMP)
            self.print.verify_simple_print_dialog()
            self.print.select_printer(self.hostname)
            self.print.select_print_dialog_print_btn()
            self.home.verify_home_screen()
        elif buttons == "close":
            self.ows_ucde_value_prop.select_native_value_prop_buttons(index=2)
            self.home.verify_home_screen()

        if buttons in ["create_account", "sign_in"]:
            assert self.home.verify_logged_in() is True
            self.fc.sign_out()
            assert self.home.verify_logged_in() is False
            self.fc.web_password_credential_delete()
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
