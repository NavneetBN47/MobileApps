import pytest
from time import sleep
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import SPL.driver.driver_factory as p_driver_factory

pytest.app_info = "GOTHAM"
class Test_Suite_02_Printer_Info_Multi_Printers(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session

        # # Initializing Printer1
        cls.p = load_printers_session
        cls.ip = cls.p.get_printer_information()["ip address"]
        if 'dune' in str(cls.p):
            cls.ip = cls.p.p_con.ethernet_ip_address
        cls.host_name = cls.p.get_printer_information()["host name"]
        cls.model_name = cls.p.get_printer_information()["model name"].strip()
        if 'HP' not in cls.model_name:
            cls.model_name = 'HP ' + cls.model_name
        cls.serial_number = cls.p.get_printer_information()["serial number"].strip()
        cls.firmware_version = cls.p.get_printer_information()["firmware version"].strip()
        cls.service_id = cls.p.get_printer_information()["service id"].strip()

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
        cls.host_name2 = cls.p2.get_printer_information()["host name"]
        cls.model_name2 = cls.p2.get_printer_information()["model name"].strip()
        if 'HP' not in cls.model_name2:
            cls.model_name2 = 'HP ' + cls.model_name2
        cls.serial_number2 = cls.p2.get_printer_information()["serial number"].strip()
        cls.firmware_version2 = cls.p2.get_printer_information()["firmware version"].strip()
        cls.service_id2 = cls.p2.get_printer_information()["service id"].strip()

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.printer_status = {}

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)

        cls.printer_settings_opt = {"printer_status" : cls.printer_settings.PRINTER_STATUS, 
                              "supply_status" : cls.printer_settings.SUPPLY_STATUS, 
                              "printer_infor" :cls.printer_settings.PRINTER_INFO,
                              "network_infor" : cls.printer_settings.NETWORK_INFO, 
                              "printer_reports" : cls.printer_settings.PRINTER_REPORTS, 
                              "print_quality" :cls.printer_settings.PRINT_QUALITY}

    @pytest.fixture()
    def restore_printer_info(self, request):
        def restore():
            self.fc.restart_hp_smart()
            self.home.verify_home_screen()
            self.fc.restore_printer_info_country_language(self.p.get_pin())
        request.addfinalizer(restore)

    def test_01_add_two_printers(self):
        """
        Switch between different printers.
        Click Printer Settings tile to go to the Printer Information screen.

        Verify all information under printer information is accurate.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078915
        """
        self.fc.go_home(username=self.login_info["email"], password=self.login_info["password"])
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()
        self.fc.select_a_printer(self.p2, add_new=True)
        assert self.home.verify_pagination_text().get_attribute("Name") == "2 of 2 printers."
        
    def test_02_verify_second_printer_infomation(self):
        """
        Verify second printer information is accurate.
        """
        if self.home.verify_carousel_printer_status_text(index=1, raise_e=False):
            self.printer_status['status2'] = self.home.get_carousel_printer_status_text(index=1) 
        else:
            self.printer_status['status2'] = "Finish Setup" 
        self.home.select_printer_settings_tile()
        self.fc.enter_printer_pin_number(self.p.get_pin())
        self.printer_settings.verify_printer_info_must_part(self.host_name2, self.model_name2, status=self.printer_status['status2'], ip=self.ip2)
        self.printer_settings.verify_printer_info_optional_part(self.host_name2, self.serial_number2, self.firmware_version2, self.service_id2)
        self.printer_settings.verify_preference_part()

    def test_03_switch_to_first_printer(self):
        """
        Switch between different printers.
        """
        self.home.select_navbar_back_btn()
        self.home.click_previous_device_btn()
        self.home.verify_setup_or_add_printer_card()
        sleep(8)
        assert self.home.verify_pagination_text().get_attribute("Name") == "1 of 2 printers."

    def test_04_verify_first_printer_infomation(self):
        """
        Verify first printer information is accurate.
        #5: Wireless connected + LEDM printer
        #6: Wireless connected + non-LEDM printer

        https://hp-testrail.external.hp.com/index.php?/cases/view/15080782 (#5 #6) 
        https://hp-testrail.external.hp.com/index.php?/cases/view/15142109 (#5 #6)
        https://hp-testrail.external.hp.com/index.php?/cases/view/15142184 (#5 #6)
        https://hp-testrail.external.hp.com/index.php?/cases/view/15142204 (#5 #6)
        """
        if self.home.verify_carousel_printer_status_text(raise_e=False):
            self.printer_status['status1'] = self.home.get_carousel_printer_status_text()
        else:
            self.printer_status['status1'] = "Finish Setup"
        self.home.select_printer_settings_tile()
        self.fc.enter_printer_pin_number(self.p.get_pin())
        self.printer_settings.verify_printer_info_must_part(self.host_name, self.model_name, status=self.printer_status['status1'], ip=self.ip)
        self.printer_settings.verify_printer_info_optional_part(self.host_name, self.serial_number, self.firmware_version, self.service_id)
        self.printer_settings.verify_preference_part()

    @pytest.mark.parametrize("each_opt", ["printer_status", "supply_status", "printer_infor", "network_infor", "printer_reports", "print_quality"])
    def test_05_check_quick_reference_btn(self, each_opt):
        """
        Click on Print Settings tile and land on Printer Information page
        Click on other areas (Printer Reports, Printer Status, Supply Status, etc.)

        Verify 'Quick Reference' link and icon still shows in the title bar

        https://hp-testrail.external.hp.com/index.php?/cases/view/24840980
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666379
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666397
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666400
        """
        self.printer_settings.select_printer_settings_opt(self.printer_settings_opt[each_opt])
        sleep(5)
        self.printer_settings.verify_quick_reference_btn()

    def test_06_check_quick_reference_btn(self):
        """
        Check 'Quick Reference' in Printer Information page.
        Check for "Quick Reference' icon in the title bar of Printer Information page.

        Verify Quick Reference link shows to the right side of title bar of Printer Information page.
        Verify Quick Reference icon shows to the left side of Quick Reference link. [Note: This doesn't apply to Mac]
        Verify the following lines shows in hp smart logs file
        The generic/normal webpage launches and shows well.
        Verify string are translated correctly and matching string table.

        https://hp-testrail.external.hp.com/index.php?/cases/view/24840978
        https://hp-testrail.external.hp.com/index.php?/cases/view/25413203
        https://hp-testrail.external.hp.com/index.php?/cases/view/25413199
        https://hp-testrail.external.hp.com/index.php?/cases/view/24840983
        https://hp-testrail.external.hp.com/index.php?/cases/view/24840981
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666380
        https://hp-testrail.external.hp.com/index.php?/cases/view/24840979
        https://hp-testrail.external.hp.com/index.php?/cases/view/24840982
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666375
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666376
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666377
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666378
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666398
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666399
        """
        assert self.printer_settings.get_quick_reference_text() == 'Quick Reference'
        self.printer_settings.click_quick_reference_btn()
        self.web_driver.add_window("quick_reference")
        sleep(3)
        self.web_driver.switch_window("quick_reference")
        sleep(3)
        current_url = self.web_driver.get_current_url()
        assert 'support.hp.com' in current_url or 'hpsmart.com' in current_url
        self.web_driver.set_size('min')
        sleep(2)
        self.home.select_navbar_back_btn()
        check_event_list = ['Ui\|ShellVm:LaunchQuickReference\|TID:[0-9]+\|(\s)+Launching URL:.*','Ui\|ShellVm:LaunchQuickReference\|TID:[0-9]+\|(\s)+LaunchQuickReference']

        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_07_check_quick_reference_btn_not_show(self, restore_printer_info):
        """
        Check for 'Quick Reference' link across the app other than Print settings pages/areas.

        Verify 'Quick Reference' link does not show in other screens across the app

        https://hp-testrail.external.hp.com/index.php?/cases/view/25666382
        https://hp-testrail.external.hp.com/index.php?/cases/view/24840982
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666403
        """
        main_tiles_list = ["scan_tile", "shortcuts_tile", "printables_tile", "print_documents_tile", "mobile_fax_tile", "help_and_support_tile"]
        
        for main_tile in main_tiles_list:
            self.home.select_each_tile(main_tile)
            sleep(5)
            assert self.printer_settings.verify_quick_reference_btn(raise_e=False) is False
            if main_tile == "printables_tile":
                self.web_driver.add_window("printables_tile")
                sleep(3)
                self.web_driver.switch_window("printables_tile")
                sleep(3)
                self.web_driver.set_size('min')
            else:
                self.home.select_navbar_back_btn()
