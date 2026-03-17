import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from selenium.common.exceptions import NoSuchElementException

pytest.app_info = "GOTHAM"
class Test_Suite_01_Printer_Info_Network_Ledm(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.moobe = cls.fc.fd["moobe"]
        cls.printer_settings = cls.fc.fd["printer_settings"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")

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
        cls.printer_status = {}
        
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)
        sleep(3)

        cls.country_list = ["Angola", "Afghanistan", "Albania", "Argentina", "Australia", "Austria", "Belarus", "Belgium", "Brazil", "Bulgaria", 'Brunei', "Canada", "Chile", "China", "Colombia", "Costa Rica", "Croatia", "Czech Republic", "Denmark", "Ecuador", "Egypt", "Estonia", "Finland", "France", "Germany", "Greece", "Guatamala", "Hong Kong SAR", "Hungary", "Iceland", "India", "Indonesia", "Ireland", "Israel", "Italy", "Japan", "Jordan", "Kazakhstan", "Korea", "Kuwait", "Latvia", "Lebanon", "Lithuania", "Malaysia", "Mexico", "Morocco", "Mozambique", "Netherlands", "New Zealand", "Norway", "Pakistan", "Panama", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Saudi Arabia", "Singapore", "Slovakia", "Slovenia", "South Africa", "Spain", "Sweden", "Switzerland", "Taiwan Region", "Thailand", "Tunisia", "Turkey", "UAE", "Ukraine", "United Kingdom", "United States", "Uruguay", "Venezuela", "United Kingdom of Great Britain and Northern Ireland", "Vietnam", "Yemen", "Select country/region"]

        cls.language_list = ["English", "Spanish, Castilian", "French", "Portuguese", "German", "Chinese (Simplified)", "Korean", "Chinese (Traditional)", "Japanese", "Italian", "Dutch", "Danish", "Swedish", "Norwegian", "Finnish", "Arabic", "Russian", "Turkish", "Polish", "Greek, Modern", "Czech", "Hungarian", "Slovak", "Romanian", "Slovene", "Bulgarian", "Croatian", "Select language"]
    
    @pytest.fixture()
    def restore_printer_info(self, request):
        def restore():
            self.fc.restart_hp_smart()
            self.fc.restore_printer_info_country_language(self.p.get_pin())
        request.addfinalizer(restore)

    def test_01_add_a_printer(self):
        """
        Don't install printer driver (Remove the driver if it installed auto).
        Go to main ui and add a printer.
        """
        self.fc.disable_printer_driver_auto_install()
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

    def test_02_check_print_info_installation_status_test(self):
        """
        Click Printer Settings tile to go to the Printer Information screen.
        Check the value of "Installation Status" on Printer Information.
        Install the printer driver.
        Refresh the printer information screen and check the value of "Installation Status".

        Verify "Not Installed" displayed behind the Installation Status when printer driver does not install.
        Verify "Installed" displayed behind the Installation Status when printer driver install.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078902
        """
        self.home.select_printer_settings_tile()
        self.fc.enter_printer_pin_number(self.p.get_pin())    
        assert self.printer_settings.verify_installation_status_text() == "Not installed"
        self.home.select_navbar_back_btn()
        self.home.select_print_documents_tile()
        self.home.verify_install_to_print_dialog()
        self.home.select_install_printer_btn()
        self.home.verify_installing_printer_dialog()        
        if self.home.verify_success_printer_installed_dialog(timeout=300, raise_e=False):
            self.home.select_success_printer_installed_ok_btn()
            assert self.home.verify_success_printer_installed_dialog(raise_e=False) is False
            self.home.select_printer_settings_tile()
            assert self.printer_settings.verify_installation_status_text() == "Installed"
        else:
            raise NoSuchElementException('Failed to install printer driver')
  
    def test_03_go_to_printer_info_screen(self):
        """
        Click Printer Settings tile to go to the Printer Information screen.
        Check the printer information details info.
        Compare the printer information displaysed on app with printer.

        Verify the printer information details info displayed well on the right panel.
        Verify the value of Connection Type is "Network" and Connection Status is "Active" when printer is online. (if printer offline, the Connection Status is "Inactive")
        Verify Model name/IP Address/Host Name/MAC Address/Printer Email Address/Product Number/Serial Number/Service ID/Firmware Version/TP Number on App are consistent with Printer.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078898
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078899
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078932
        https://hp-testrail.external.hp.com/index.php?/cases/view/15142116
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666401
        https://hp-testrail.external.hp.com/index.php?/cases/view/25666402
        """
        self.home.select_navbar_back_btn()
        if self.home.verify_carousel_printer_status_text(raise_e=False):
            self.printer_status['status'] = self.home.get_carousel_printer_status_text()
        else:
            self.printer_status['status'] = "Finish Setup"
        self.home.select_printer_settings_tile()
        self.printer_settings.verify_printer_info_must_part(self.host_name, self.model_name, status=self.printer_status['status'], ip=self.ip)
        self.printer_settings.verify_printer_info_optional_part(self.host_name, self.serial_number, self.firmware_version, self.service_id)

    def test_04_click_refresh_btn_to_check_offline_status(self):
        """
        Turn off the test printer, make sure the printer offline displayed on Main UI.
        Generate a different status for this printer
        Click "Refresh" icon behind the Status.

        Verify the Status value updates to the correct status.
        Verify the printer details still shows and printer status says printer offline
        Verify the preferences (if applicable) and register printer does not show.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078901
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078916
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078934
        https://hp-testrail.external.hp.com/index.php?/cases/view/15142118
        """
        self.fc.trigger_printer_offline_status(self.p)
        for _ in range(3):
            if self.printer_settings.verify_status_text('Printer offline', raise_e=False):
                break
            else:
                self.printer_settings.click_status_circle_btn()
                sleep(2)
        self.printer_settings.verify_printer_info_must_part(self.host_name, self.model_name, status='Printer offline', con_status='Inactive')

    def test_05_check_the_preferences_section(self):
        """
        Check the preferences section of Printer Information screen.
        Observe the Preference section on the printer information page for Country and Language section

        For Win, Verify the Country and Language settings displays;
        Verify the information displayed under preferences matches with the printer preference settings on printer front panel.
        Verify the Auto-off settings is not show since it is removed (GOTH-3792).

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078903
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078918
        """
        self.fc.restore_printer_online_status(self.p)
        self.home.select_navbar_back_btn()
        assert self.home.verify_carousel_printer_offline_status(raise_e=False) is False
        self.home.select_printer_settings_tile()
        
    def test_06_check_country_region_dropdown(self):
        """
        Click "Country" dropdown
        Scroll the scroll bar to the top and then to the bottom for the country dropdown list.
        Select a country different from current country and check.

        Verify the dropdown list opens with available countries displayed.
        Verify all displays countries can also be found on printer front panel supported countries in preferences.
        Verify "Set Country" dialog pops up.
        Verify China shows in it if the printer support this option.
        Verify Taiwan Region shows in it if the printer support this option.
        Verify HongKong SAR shows in it if the printer support this option.
        Verify Macau SAR shows in it if the printer support this option.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078904
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078905
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078908
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078936
        https://hp-testrail.external.hp.com/index.php?/cases/view/44771530
        """
        if self.printer_settings.verify_preference_part() is not False:
            check_cr = []
            cou_list = ["China", "Hong Kong SAR", "Morocco", "Taiwan Region"]
            self.printer_settings.click_preferences_title()
            self.printer_settings.click_country_dropdown()
            el = self.driver.wait_for_object("country_region_box")
            el.send_keys(Keys.HOME)
            select_item = None

            # Handle popup and click buttons on printer
            self.moobe.click_button_on_fp_from_printer(self.p)
            for i in range(len(self.country_list)):
                if i < 2:
                    self.printer_settings.click_country_region_index(i+1)
                    if self.printer_settings.verify_set_country_or_language_dialog(raise_e=False):
                        self.printer_settings.click_set_save_btn()
                    if self.printer_settings.verify_sign_in_to_dialog(raise_e=False):
                        self.printer_settings.edit_sign_in_password(self.p.get_pin())
                        self.printer_settings.click_sign_in_submit_btn()
                else:
                    el = self.printer_settings.verify_country_select_item(select_item)
                    el.send_keys(Keys.DOWN, Keys.ENTER)
                    if self.printer_settings.verify_set_country_or_language_dialog(raise_e=False):
                        self.printer_settings.click_set_save_btn()
                select_item = self.printer_settings.get_country_region_text()
                check_cr.append(select_item)
                assert select_item in self.country_list
                if select_item=="Select country/region":
                    break
                else:
                    self.printer_settings.click_country_dropdown()
            assert set(cou_list) < set(check_cr)

    def test_07_check_set_country_dialog_btn(self):
        """
        Select a country different from current country and check.
        Click "Cancel" button on the "Set Country/Region" dialog.
        Click "Save" button on the "Set Country/Region" dialog.

        Verify "Set Country" dialog pops up.
        Verify the dialog is closed, and the country setting is not changed, still is the previous one after click "Cancel" button.
        Verify the country setting is changed to you selected one on Gotham app and on printer at the both time after click "Save" button.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078908
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078909
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078938
        """
        if self.printer_settings.verify_preference_part() is not False:
            self.printer_settings.click_preferences_title()
            self.printer_settings.click_country_dropdown()
            el = self.printer_settings.verify_country_select_item("Select country/region")
            el.send_keys(Keys.UP, Keys.ENTER)
            assert self.printer_settings.verify_country_select_item("Select country/region", raise_e=False) is False
            select_item = self.printer_settings.get_country_region_text()
            self.printer_settings.click_country_dropdown()
            el = self.printer_settings.verify_country_select_item(select_item)
            el.send_keys(Keys.UP, Keys.ENTER)
            self.printer_settings.verify_set_country_or_language_dialog()
            self.printer_settings.click_set_cancel_btn()
            self.printer_settings.verify_country_select_item(select_item)
            self.printer_settings.click_country_dropdown()
            el.send_keys(Keys.UP, Keys.ENTER)
            self.printer_settings.verify_set_country_or_language_dialog()
            self.printer_settings.click_set_save_btn()
            assert self.printer_settings.verify_country_select_item(select_item, raise_e=False) is False
    
    def test_08_check_language_dropdown(self):
        """
        Click "Language" dropdown
        Scroll the scroll bar to the top and then to the bottom for the language dropdown list.

        Verify the dropdown list opens with available countries displayed.
        Verify all displays languages can also be found on printer front panel supported languages in preferences.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078906
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078907
        """
        if self.printer_settings.verify_preference_part() is not False:
            check_lan = []
            lan_list = ["Chinese (Simplified)", "Chinese (Traditional)"]
            self.printer_settings.click_preferences_title()
            self.printer_settings.click_language_dropdown()
            el = self.driver.wait_for_object("language_box")
            el.send_keys(Keys.HOME)
            select_item = None
            for i in range(len(self.language_list)):
                if i==0:
                    self.printer_settings.click_language_index(1)
                else:
                    el = self.printer_settings.verify_language_select_item(select_item)
                    el.send_keys(Keys.DOWN, Keys.ENTER)             
                if self.printer_settings.verify_set_country_or_language_dialog(raise_e=False):
                    self.printer_settings.click_set_save_btn()
                select_item = self.printer_settings.get_language_text()
                check_lan.append(select_item)
                assert select_item in self.language_list
                if select_item=="Select language":
                    break
                else:
                    self.printer_settings.click_language_dropdown()
            assert set(lan_list) < set(check_lan)

    def test_09_check_set_language_dialog_btn(self, restore_printer_info):
        """
        Select a language different from the current language and check.
        Click "Cancel" button on the "Set Language" dialog.
        Click "Save" button on the "Set Language" dialog.

        Verify the dialog is closed, and the language setting is not changed, still is the previous one after click "Cancel" button.
        Verify the language setting is changed to you selected one on Gotham app and on printer at the both time after click "Save" button.

        https://hp-testrail.external.hp.com/index.php?/cases/view/15078910
        https://hp-testrail.external.hp.com/index.php?/cases/view/15078911
        """
        if self.printer_settings.verify_preference_part() is not False:
            self.printer_settings.click_preferences_title()
            self.printer_settings.click_language_dropdown()
            el = self.printer_settings.verify_language_select_item("Select language")
            el.send_keys(Keys.UP, Keys.ENTER)
            assert self.printer_settings.verify_language_select_item("Select language", raise_e=False) is False
            select_item = self.printer_settings.get_language_text()
            self.printer_settings.click_language_dropdown()
            el = self.printer_settings.verify_language_select_item(select_item)
            el.send_keys(Keys.UP, Keys.ENTER)
            self.printer_settings.verify_set_country_or_language_dialog()
            self.printer_settings.click_set_cancel_btn()
            self.printer_settings.verify_language_select_item(select_item)
            self.printer_settings.click_language_dropdown()
            el.send_keys(Keys.UP, Keys.ENTER)
            self.printer_settings.verify_set_country_or_language_dialog()
            self.printer_settings.click_set_save_btn()
            assert self.printer_settings.verify_language_select_item(select_item, raise_e=False) is False
