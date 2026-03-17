import pytest
from time import sleep
import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from selenium.common.exceptions import NoSuchElementException

pytest.app_info = "GOTHAM"
class Test_Suite_02_DSP_Log(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.web_driver = utility_web_session

        cls.printer_opt = {'printer_status':'ready'}

        cls.home = cls.fc.fd["home"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.dedicated_supplies_page = cls.fc.fd["dedicated_supplies_page"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.printer_status = cls.fc.fd["printer_status"]
        cls.serial_number = cls.p.get_printer_information()["serial number"]
        cls.model_name = cls.p.get_printer_information()["model name"].strip()

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack = cls.stack, a_type = "ucde")
        
        """
        This is a method to ensure the PC and printer are in the same wifi.
        """
        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)
        sleep(3)

    def test_01_go_home_and_add_a_printer(self):
        self.fc.go_home()
        self.fc.sign_in(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)
        
    def test_02_check_get_supplies_tile_online(self):
        """
        Click "Get Supplies" tile on main UI .

        Verify II related DSP content shows

        https://hp-testrail.external.hp.com/index.php?/cases/view/17117702
        https://hp-testrail.external.hp.com/index.php?/cases/view/17224348
        """
        check_event_list = []
        self.home.verify_instant_ink_tile_image()
        self.home.select_get_supplies_tile()
        if self.dedicated_supplies_page.verify_not_now_dialog():
            self.dedicated_supplies_page.select_not_now_btn()
        if self.dedicated_supplies_page.verify_hp_instant_ink_page():
            self.dedicated_supplies_page.select_back_btn()
            check_event_list.append('Launching in embedded webview')
 
        else:
            self.web_driver.add_window("get_supplies")
            sleep(3)
            self.web_driver.switch_window("get_supplies")
            sleep(3)
            current_url = self.web_driver.get_current_url()
            if 'hpinstantink' not in current_url and 'hp.com' not in current_url:
                raise NoSuchElementException('Failed launch instant ink url')
            self.web_driver.close_window("get_supplies")
            check_event_list.append('Launching External Browser')

        self.home.verify_home_screen(timeout=10)
        self.driver.terminate_app()
        check_event_list.extend(['OnrampContentPostRequestAsync:', 'MessageRedirectUrl:'])

        for each_event in check_event_list:
                self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_03_check_ink_level_icon(self):
        """
        Click Ink level icon on the Main UI

        verify correct jump id shows in the Gotham log as below
        Win: in_r11549_ii2_winhpsmart_supplystatus_042919

        https://hp-testrail.external.hp.com/index.php?/cases/view/17169852
        https://hp-testrail.external.hp.com/index.php?/cases/view/17117703
        https://hp-testrail.external.hp.com/index.php?/cases/view/17859950
        https://hp-testrail.external.hp.com/index.php?/cases/view/31174651
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.verify_instant_ink_tile_image()
        if self.home.verify_carousel_estimated_supply_image(raise_e=False):
            self.home.click_carousel_estimated_supply_levels()
            if self.printer_settings.verify_supply_status_page():
                sleep(1)
                self.home.select_navbar_back_btn()           
            else:
                self.web_driver.add_window("estimated_supply")
                sleep(3)
                self.web_driver.switch_window("estimated_supply")
                sleep(3)
                current_url = self.web_driver.get_current_url()
                if 'hpinstantink' not in current_url and 'hp.com' not in current_url:
                    raise NoSuchElementException('Failed launch instant ink url')
                self.web_driver.close_window("estimated_supply")
            self.home.verify_home_screen(timeout=10)
            self.driver.terminate_app()
            check_event_list = ['in_r11549_ii2_winhpsmart_supplystatus-car_042919']
            for each_event in check_event_list:
                    self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_04_click_explore_option_btn(self):
        """
        change the test flag to Generate any supplies related messages
        Click "Explore Options" button on the message.

        Verify Gotham log shows correct Jump ID as below
        Win: in_r11549_ii2_winhpsmart_printerstatus_042919

        https://hp-testrail.external.hp.com/index.php?/cases/view/17135129
        https://hp-testrail.external.hp.com/index.php?/cases/view/17117706
        https://hp-testrail.external.hp.com/index.php?/cases/view/17117711
        https://hp-testrail.external.hp.com/index.php?/cases/view/29408947
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        ioref_list = ['65537']
        self.fc.trigger_printer_status(self.serial_number, ioref_list)
        if self.printer_status.click_ps_body_btn('Get Supplies'):
            if self.printer_settings.verify_supply_status_page():
                sleep(1)
                self.home.select_navbar_back_btn()           
            else:
                self.web_driver.add_window("get supplies")
                sleep(3)
                self.web_driver.switch_window("get supplies")
                sleep(3)
                current_url = self.web_driver.get_current_url()
                if 'hpinstantink' not in current_url and 'hp.com' not in current_url:
                    raise NoSuchElementException('Failed launch instant ink url')
                self.web_driver.close_window("get supplies")
            self.home.verify_home_screen(timeout=10)
            self.driver.terminate_app()
            check_event_list = ['in_r11549_ii2_winhpsmart_printerstatus_042919']
            for each_event in check_event_list:
                    self.pepto.check_pepto_data(each_event, check_data="p2")
    
    def test_05_click_supply_status_tab(self):
        """
        Click on Supply Status tab under printer settings

        Verify correct parameters are seen in log file.

        https://hp-testrail.external.hp.com/index.php?/cases/view/17052569
        https://hp-testrail.external.hp.com/index.php?/cases/view/17117704
        https://hp-testrail.external.hp.com/index.php?/cases/view/17859951
        https://hp-testrail.external.hp.com/index.php?/cases/view/31174650
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_settings_page()
        self.printer_settings.select_printer_status_item()
        self.printer_settings.select_supply_status_option()
        if self.printer_settings.verify_supply_status_page():
            sleep(1)
            self.home.select_navbar_back_btn()           
        else:
            self.web_driver.add_window("supply_status")
            sleep(3)
            self.web_driver.switch_window("supply_status")
            current_url = self.web_driver.get_current_url()
            if 'hpinstantink' not in current_url and 'hp.com' not in current_url:
                raise NoSuchElementException('Failed launch instant ink url')
            self.web_driver.close_window("supply_status")
        self.home.verify_home_screen(timeout=10)
        self.driver.terminate_app()
        check_must_list = ['x-api-key:[\s]*[A-Za-z0-9-]+', 'Language_code:[\s]*en', 'Country_code:[\s]*US', 'Printer_sku:[\s]*[A-Za-z0-9]+', 'Printer_make_and_model:[\s]*[A-Za-z0-9 ]+', 'Client:[\s]*smartWinV[0-9]', 'Sn:[\s]*{}'.format(self.serial_number), 'Jump_id:[\s]*[A-Za-z0-9_]+', 'Reference_id:[\s]*[A-Za-z0-9-]+', 'Redirect_url:[\s]*hpsmartwin://callback']
        for each_event in check_must_list:
                self.pepto.check_pepto_data(each_event, check_data="p2")

        check_available_dir = {'Webauth_token:':'Webauth_token:[\s]*[A-Za-z0-9]{5,}', 'post_card:':'post_card:[\s]*[A-Za-z0-9]{5,}', 'Cached_supplies_array:':'Cached_supplies_array:.*', 'Supplies_data_timestamp:':'Supplies_data_timestamp:[\s]*[A-Z0-9 :/+]{10,}', 'Total_impressions:':'Total_impressions:[\s]*[A-Za-z0-9]+', 'Service_id:':'Service_id:[\s]*[0-9]{4,5}', 'Connection_type:':'Connection_type:[\s]*Local_network_printer', 'Consumableconfigdyn:':'Consumableconfigdyn:[\s]*null|Consumableconfigdyn:[\s]*present', 'Productconfigdyn:':'Productconfigdyn:[\s]*null|Productconfigdyn:[\s]*present', 'Productusagedyn:':'Productusagedyn:[\s]*null|Productusagedyn:[\s]*present', 'Productstatusdyn:':'Productstatusdyn:[\s]*null|Productstatusdyn:[\s]*present', 'eprintconfigdyn:':'eprintconfigdyn:[\s]*null|eprintconfigdyn:[\s]*present'}
        for each_event in list(check_available_dir.keys()):
            if self.pepto.check_pepto_data(each_event, check_data="p2", raise_e=False) is not False:
                self.pepto.check_pepto_data(check_available_dir[each_event], check_data="p2")

    def test_06_turn_off_printer_wireless(self):
        """
        An offline printer.
        Computer is network connected.
        """
        self.fc.restart_hp_smart()
        self.home.verify_home_screen()
        self.fc.trigger_printer_offline_status(self.p)
        self.home.verify_carousel_printer_offline_status()

    def test_07_check_get_supplies_tile_offline(self):
        """
        Click "Get Supplies"/"Get Ink" tile after the printer is offline

        Verify P2 page shows

        https://hp-testrail.external.hp.com/index.php?/cases/view/16978305
        """
        check_event_list = []
        self.home.verify_instant_ink_tile_image()
        self.home.select_get_supplies_tile()
        if self.dedicated_supplies_page.verify_not_now_dialog():
            self.dedicated_supplies_page.select_not_now_btn()
        if self.dedicated_supplies_page.verify_hp_instant_ink_page():
            self.dedicated_supplies_page.select_back_btn() 
            check_event_list.append('Launching in embedded webview')
        else:
            self.web_driver.add_window("get_supplies")
            sleep(3)
            self.web_driver.switch_window("get_supplies")
            sleep(3)
            current_url = self.web_driver.get_current_url()
            if 'hpinstantink' not in current_url and 'hp.com' not in current_url:
                logging.info("Get Supplies url: {}".format(current_url))
                raise NoSuchElementException('Failed launch instant ink url')
            self.web_driver.close_window("get_supplies")
            check_event_list.append('Launching External Browser')

        self.home.verify_home_screen(timeout=10)
        self.driver.terminate_app()
        check_event_list.extend(['OnrampContentPostRequestAsync:', 'MessageRedirectUrl:'])
        for each_event in check_event_list:
                self.pepto.check_pepto_data(each_event, check_data="p2")
    
    def test_08_check_must_parameters(self):
        """
        Add a printer to the main UI which is not enrolled into II
        Click on Get Ink / Get Supplies tile
        open Gotham log

        https://hp-testrail.external.hp.com/index.php?/cases/view/16946966
        """
        check_event_list = ['x-api-key:(\s+)[a-z0-9-]{36}', 'Language_code:(\s+)en', 'Country_code:(\s+)US', 'Printer_sku:(\s+)[A-Z0-9]{6}', 'Printer_make_and_model:(\s+){}'.format(self.model_name), 'Client:(\s+)smartWinV[0-9]{1}', 'Sn:(\s+){}'.format(self.serial_number), 'Jump_id:(\s+)[a-z0-9_]{36}', 'Reference_id:(\s+)[a-z0-9-]{36}', 'Redirect_url:(\s+)hpsmartwin://callback']
        for each_event in check_event_list:
                self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_09_check_parameters_not_present(self):
        """
        Click Get supplies/Get Ink tile on the Main UI
        Close the app once DSP page is loaded
        Check the Gotham log.

        Verify the following log lines are not present in the Gotham log.
        Got Eprintconfigdyn: True
        Eprintconfigdyn: present

        https://hp-testrail.external.hp.com/index.php?/cases/view/27090159
        """
        check_event_list = ['Got Eprintconfigdyn:(\s)True', 'Eprintconfigdyn:(\s)present']
        for each_event in check_event_list:
                assert self.pepto.check_pepto_data(each_event, check_data="p2", raise_e=False) is False