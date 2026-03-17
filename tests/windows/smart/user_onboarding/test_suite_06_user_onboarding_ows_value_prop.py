import pytest
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "GOTHAM"
class Test_Suite_06_User_Onboarding_OWS_Value_Prop(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        cls.welcome = cls.fc.fd["welcome_web"]
        cls.ows_value_prop = cls.fc.fd["ows_value_prop"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]

        cls.stack = request.config.getoption("--stack")

    def test_01_relaunch_on_ows_value_prop_screen(self):
        """
        Click "Yes"/ "No" button on the Pepto screen, verify OWS value prop screen shows
        Close the app while you are on OWS value prop and relaunch the app, verify app launched to the Main UI
        Observe OWS value prop screen, verify shell title bar is removed

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176710
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27263287 (GOTH-22072)
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176717
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176787
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176711
        """
        self.welcome.verify_welcome_screen()
        self.welcome.click_accept_all_btn()

        self.ows_value_prop.verify_windows_ows_value_prop_screen()
        self.ows_value_prop.verify_printer_setup_exit_setup_removed()
        self.fc.restart_hp_smart()
        self.ows_value_prop.verify_windows_ows_value_prop_screen()

    def test_02_close_on_sign_in_dialog(self):
        """
        Click "X" button on the HPID Sign in/Create account dialog, verify user navigates to the Home page
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997914
        """
        self.__restore_app()

        self.ows_value_prop.select_native_value_prop_buttons(index=1)
        self.fc.verify_hp_id_sign_in_up_page()
        self.fc.close_hp_id_sign_in_up_page()

    def test_03_click_skip_for_now_btn(self):
        """
        Click "Skip for now" link on the yeti value prop screen, verify user navigates to main UI
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27176720
        """
        self.__restore_app()

        self.ows_value_prop.select_native_value_prop_buttons(index=3)

        self.home.verify_home_screen()

    def test_04_click_setup_a_new_printer_btn(self):
        """
        Click "Set Up printer"button on the yeti value prop screen, verify Device Picker launched
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27796423
        """
        self.__restore_app()

        self.ows_value_prop.select_primary_btn()

        self.printers.verify_device_picker_screen()


    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __restore_app(self):
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)

        self.welcome.click_accept_all_btn()
        self.ows_value_prop.verify_windows_ows_value_prop_screen()
