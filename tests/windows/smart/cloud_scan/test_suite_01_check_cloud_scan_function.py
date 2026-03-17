import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import SPL.driver.driver_factory as p_driver_factory
import logging


pytest.app_info = "GOTHAM"
class Test_Suite_01_Check_Cloud_Scan_function(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        # Initializing Printer1
        cls.p = load_printers_session
        cls.ip = cls.p.get_printer_information()["ip address"]
        if 'dune' in str(cls.p):
            cls.ip = cls.p.p_con.ethernet_ip_address

        # Initializing Printer2
        cls.sys_config = ma_misc.load_system_config_file()
        cls.db_info = cls.sys_config.get("database_info", None)
        cls.p2 = p_driver_factory.get_printer(cls.sys_config["printer_power_config"], db_info=cls.db_info)
        cls.p2.set_mech_mode(mech=False)
        cls.printer_info2 = cls.p2.get_printer_information()
        logging.info("Another Printer Information:\n {}".format(cls.printer_info2))

        cls.ip2 = cls.p2.get_printer_information()["ip address"]
        if 'dune' in str(cls.p2):
            cls.ip2 = cls.p2.p_con.ethernet_ip_address

        cls.home = cls.fc.fd["home"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.cloud_scan = cls.fc.fd["cloud_scan"]

        cls.stack = request.config.getoption("--stack")
        if cls.stack != 'stage':
            pytest.skip("Only stage stack owns cloud scan account")
        cls.login_info = ma_misc.get_hpid_account_info(stack = cls.stack, a_type = "hp+", cloud_scan = True)
        
        """
        This is a method to ensure the PC and printer are in the same wifi.
        """
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_check_tile_no_printer_login_or_not(self):
        """
        Check tiles when no printer is in the carousel.
        
        Account is not signed in:
        Verify "My HP Cloud Scans" tile is not seen on the home page when no printer is in the carousel.

        Sign in a cloud scan enabled account:
        Verify "My HP Cloud Scans" tile is seen when no printer is in the carousel.

        https://hp-testrail.external.hp.com/index.php?/cases/view/44453800
        """
        self.fc.go_home()
        assert self.home.verify_cloud_scans_tile(raise_e=False) is False
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_welcome_back_dialog()
        self.home.select_an_organization_list_item('last()')
        self.home.select_welcome_back_continue_btn()
        self.home.verify_home_screen(timeout=60)
        self.home.verify_cloud_scans_tile()        

    def test_02_check_tile_with_two_printers_login_or_not(self):
        """
        Add some (>=2) non cloud scan-enabled printers, and then check tiles.
        
        Account is not signed in:
        Verify "My HP Cloud Scans" tile is not seen for all printers when non cloud scan-enabled printers are added in the carousel.

        Sign in a cloud scan enabled account:
        Verify "My HP Cloud Scans" tile is seen for all printers after cloud scan NOT supported printers are added in the carousel.
        
        https://hp-testrail.external.hp.com/index.php?/cases/view/38965554 (2 non cloud scan-enabled printers)
        https://hp-testrail.external.hp.com/index.php?/cases/view/38965555 (2 non cloud scan-enabled printers)
        """
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()
        self.fc.select_a_printer(self.p2, add_new=True)
        assert self.home.verify_pagination_text().get_attribute("Name") == "2 of 2 printers."
        self.home.verify_cloud_scans_tile()
        self.fc.sign_out()
        assert self.home.verify_logged_in() is False
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        assert self.home.verify_cloud_scans_tile(raise_e=False) is False
        
    def test_03_check_cloud_scans_tile(self):
        """
        Click "My HP cloud Scans" Tile area on the Main Page

        Verify "MY HP cloud Scans" shows in the tile section
        Verify "My HP cloud Scans" webview open

        https://hp-testrail.external.hp.com/index.php?/cases/view/38965556
        """
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.home.verify_welcome_back_dialog()
        self.home.select_an_organization_list_item('last()')
        self.home.select_welcome_back_continue_btn()
        self.home.verify_home_screen(timeout=60)
        self.home.select_cloud_scans_tile()
        self.cloud_scan.verify_my_hp_cloud_scans_screen()

    def test_04_click_back_arrow(self):
        """
        Click Back arrow on the webapp

        Verify user is navigated back to home page
        Verify log line can be found in the gotham log
        Verify simpleUi event is published to Kibana board

        https://hp-testrail.external.hp.com/index.php?/cases/view/38965558
        https://hp-testrail.external.hp.com/index.php?/cases/view/38965569
        """
        self.cloud_scan.click_back_arrow()
        self.home.verify_cloud_scans_tile()

        check_event_list = ['Ui\|DataCollection:SendSimpleUiEventAction\|TID:[0-9]+\|(\s)SendUiEvent action:ControlButtonClicked, screen:HpCloudScan, activity:Scan-v01, Path:.*?, mode:, control:Back, detail:, actionAuxParameters:']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_05_click_refresh_icon(self):
        """
        Click Refresh icon on the webapp

        Verify content is refreshed in the webapp

        https://hp-testrail.external.hp.com/index.php?/cases/view/38965559
        """
        self.home.select_cloud_scans_tile()
        self.cloud_scan.verify_my_hp_cloud_scans_screen()
        self.cloud_scan.click_refresh_icon()
        self.cloud_scan.verify_my_hp_cloud_scans_screen()

    def test_06_click_hamburger_icon(self):
        """
        Click hamburger icon on the webapp

        Verify all the linked Cloud scan available printer shows on the list

        https://hp-testrail.external.hp.com/index.php?/cases/view/38965560
        """
        list_exit = self.cloud_scan.verify_cloud_scan_printers_list(raise_e=False)
        if list_exit:
            self.cloud_scan.click_hamburger_icon()
            assert self.cloud_scan.verify_cloud_scan_printers_list(raise_e=False) is False
        self.cloud_scan.click_hamburger_icon()
        self.cloud_scan.verify_cloud_scan_printers_list()

    def test_07_check_toggle_on_off(self):
        """
        Turn the toggle on/Off on the priners dialog

        Verify user is able to turn off the toggle without any issue

        https://hp-testrail.external.hp.com/index.php?/cases/view/38965561
        """
        for i in range(1,4):       
            toggle_status = self.cloud_scan.get_sync_toggle_status(num=i)
            if int(toggle_status) == 1:
                assert self.cloud_scan.get_printer_sync_text(index=1, num=i) == 'Update sync schedule'
                self.cloud_scan.switch_printer_sync_toggle(num=i)
                assert self.cloud_scan.get_printer_sync_text(index=0, num=i) == 'Sync is turned off'
                assert int(self.cloud_scan.get_sync_toggle_status(num=i)) == 0
                sleep(2)
                self.cloud_scan.switch_printer_sync_toggle(num=i)
                self.cloud_scan.verify_set_up_your_sync_schedule_dialog()
                self.cloud_scan.select_sync_schedule(schedule=1)
                self.cloud_scan.click_save_button()
                self.cloud_scan.verify_sync_successful_dialog()
                self.cloud_scan.click_dialog_close_button()
                assert self.cloud_scan.get_printer_sync_text(index=1, num=i) == 'Update sync schedule'
                assert int(self.cloud_scan.get_sync_toggle_status(num=i)) == 1
            elif toggle_status is False:
                sleep(2)
                self.cloud_scan.switch_printer_sync_toggle(num=2)
                self.cloud_scan.verify_set_up_your_sync_schedule_dialog()
                self.cloud_scan.select_sync_schedule(schedule=1)
                self.cloud_scan.click_save_button()
                self.cloud_scan.verify_sync_successful_dialog()
                self.cloud_scan.click_dialog_close_button()
                assert self.cloud_scan.get_printer_sync_text(index=1, num=2) == 'Update sync schedule'
                assert int(self.cloud_scan.get_sync_toggle_status(num=2)) == 1
        
        self.cloud_scan.verify_my_hp_cloud_scans_screen()

    def test_08_click_x_button(self):
        """
        Click "X" icon on the dialog

        Verify dialog is closed
        Verify user is still on the webapp

        https://hp-testrail.external.hp.com/index.php?/cases/view/38965563
        """
        self.cloud_scan.click_x_button()
        assert self.cloud_scan.verify_cloud_scan_printers_list(raise_e=False) is False
        self.cloud_scan.verify_my_hp_cloud_scans_screen()
