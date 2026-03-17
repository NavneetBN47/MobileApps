import pytest
import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
import SPL.driver.driver_factory as p_driver_factory
from selenium.common.exceptions import NoSuchElementException


pytest.app_info = "GOTHAM"
class Test_Suite_01_Nav_Pane_Smart_Dashboard(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        # Initializing Printer2
        cls.sys_config = ma_misc.load_system_config_file()
        cls.db_info = cls.sys_config.get("database_info", None)
        cls.p2 = p_driver_factory.get_printer(cls.sys_config["printer_power_config"], db_info=cls.db_info)
        cls.p2.set_mech_mode(mech=False)
        cls.printer_info2 = cls.p2.get_printer_information()
        logging.info("Printer Information:\n {}".format(cls.printer_info2))

        cls.home = cls.fc.fd["home"]
        cls.smart_dashboard = cls.fc.fd["smart_dashboard"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"

    def test_01_check_smart_dashboard_without_printer(self):
        """
        *Click on person icon (new user signed in), select "Manage HP Account" from login flyout, verify Smart Dashboard opens in a web view
        Check gotham logs file, verify correct Smart Dashboard urls shows on the logs file

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30300353
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997738
        """    
        self.fc.go_home(create_account=True)
        assert self.home.verify_carousel_printer_image(timeout=10, raise_e=False) is False

        self.home.select_manage_hp_account_btn()
        self.smart_dashboard.verify_my_account_page()
        self.home.select_navbar_back_btn()
        self.home.verify_setup_or_add_printer_card()
        self.check_url_in_hp_smart_log(self.stack)

    def test_02_check_smart_dashboard_with_one_printer(self):
        """
        *Click on person icon (new user signed in), select "Manage HP Account" from login flyout, verify Smart Dashboard opens in a web view
        Check gotham logs file, verify correct Smart Dashboard urls shows on the logs file
        Click back arrow from Smart Dashboard, verify user navigate to app main UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30300353
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/30300356
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27997734
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/17212358
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28572417
        """
        self.fc.web_password_credential_delete()
        self.fc.reset_hp_smart()
        self.fc.change_stack_server(self.stack)

        self.fc.go_home(self.login_info["email"], self.login_info["password"])
        self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)
        self.fc.select_a_printer(self.p, from_carousel=True)
        self.home.verify_carousel_printer_image()

        self.home.verify_navigation_pane_split_view(login=True, printer=True)
        self.home.select_manage_hp_account_btn()
        self.smart_dashboard.verify_my_account_page()
        self.home.select_navbar_back_btn()
        self.home.verify_carousel_printer_image()
        self.check_url_in_hp_smart_log(self.stack)
        assert self.home.verify_previous_device_btn_enabled_status() == "true"
        assert self.home.verify_next_device_btn_enabled_status() == "false"
        
    def test_03_check_smart_dashboard_with_multiple_printers(self):
        """
        *Click on person icon (new user signed in), select "Manage HP Account" from login flyout, verify Smart Dashboard opens in a web view
        Click back arrow from Smart Dashboard, verify user navigate to app main UI

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/30300353
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/30300354
        """
        self.fc.select_a_printer(self.p2)
        assert self.home.verify_pagination_text().get_attribute("Name") == "2 of 2 printers."

        self.home.select_manage_hp_account_btn()
        self.smart_dashboard.verify_my_account_page()
        self.home.select_navbar_back_btn()

        printer2_model_name = self.home.get_carousel_printer_model_name(index=1)
        shortened_model_name = ma_misc.truncate_printer_model_name(self.printer_info2["model name"], case_sensitive=False)
        shorteded_model_name = list(shortened_model_name.split(' '))
        for sub_name in shorteded_model_name:
            assert sub_name in printer2_model_name.lower()


    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def check_url_in_hp_smart_log(self, stack):
        if stack == "stage":
            check_string = "https://www.hpsmartstage.com/ucde"
        elif stack == "pie":
            check_string = "https://www.hpsmartpie.com/ucde"
        else:
            check_string = "https://www.hpsmart.com/ucde"
        
        self.fc.check_gotham_log(check_string)