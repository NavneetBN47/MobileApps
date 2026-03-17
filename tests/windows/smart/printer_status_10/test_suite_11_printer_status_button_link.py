import pytest
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc

pytest.app_info = "GOTHAM"
class Test_Suite_11_Printer_Status_Button_Link(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.pepto = cls.fc.fd["pepto"]
        cls.printer_settings = cls.fc.fd["printer_settings"]
        cls.printer_status = cls.fc.fd["printer_status"]
        cls.serial_number = cls.p.get_printer_information()["serial number"]

        cls.stack = request.config.getoption("--stack")
        cls.login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde", instant_ink=True)

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

    def test_01_go_home_and_add_a_printer(self):
        """ 
        https://hp-testrail.external.hp.com/index.php?/cases/view/14610459
        https://hp-testrail.external.hp.com/index.php?/cases/view/14607178
        https://hp-testrail.external.hp.com/index.php?/cases/view/14610667
       
        """
        self.fc.go_home(self.login_info["email"], self.login_info["password"])
        self.fc.select_a_printer(self.p)

    def test_02_trigger_ioref_button(self):
        """ 
        check button: Get More Help, Explore Options, Estimated Supply Levels
        """
        ioref_list = ['65557', '66378', '66379']
        self.fc.trigger_printer_status(self.serial_number, ioref_list)

    @pytest.mark.parametrize("ioref", ['65557', '66378', '66379'])
    def test_03_check_button(self, ioref):
        """ 
        click button to check
        """
        self.printer_status.click_ps_ioref_item(ioref)
        buttons_list = self.printer_status.check_right_body_btn()
        for check_btn in buttons_list:      
            self.__check_button(check_btn)

    def test_04_trigger_ioref_button(self):
        """ 
        Click "Get More Help" link for IOREF 65579/65585/66168.
        """
        ioref_list = ['65579', '65585', '66168']
        self.fc.trigger_printer_status(self.serial_number, ioref_list)

    @pytest.mark.parametrize("ioref", ['65579', '65585', '66168'])
    def test_05_check_button(self, ioref):
        """ 
        Correct link should launch.
        The line in the log

        https://hp-testrail.external.hp.com/index.php?/cases/view/32809999
        """
        self.printer_status.click_ps_ioref_item(ioref)    
        self.__check_button('Get More Help')

        check_event_list = ['Ui\|IORefUtils:GetSupportURL\|TID:[0-9]+\|(\s)Url (encoded):(\s)https://kaas.hpcloud.hp.com/PROD/v2/redirectapi?clientId=SmartAppW&contextId=*?&countryCode=US&languageCode=en&productSignature=[A-Z0-9]{6}']
        for each_event in check_event_list:
            self.pepto.check_pepto_data(each_event, check_data="p2")

    def test_06_trigger_ioref_link(self):
        """ 
        check link: 'www.hp.com/recycle', 'www.hp.com/go/anticounterfeit', 'More Information', 'View HP Privacy Statement Online', 'HP', 'HP Instant Ink', 'www.hpinstantink.com', 'View More Information online', 'www.hpinstantink.com/enroll', 'www.hpinstantink.com/bundle', 'hp.com/plus-support', 'www.support.hp.com', 'www.hpsmart.com', 'www.hp.com/contactHP', 'https://instantink.hpconnected.com/', 'www.hp.com/learn/ds', 'here', 'https://www8.hp.com/us/en/privacy/limited_warranty.html', 'hpsmart.com/activate', 'hp.com/support/printer-setup', 'www.hpsmart.com/wireless-printing'
        """
        ioref_list = ['65539', '65559', '65595', '65671', '65674', '65765', '65912', '65934', '65966', '66168', '66213', '66251', '66316', '66328', '66339', '66353', '66419', '66435']
        self.fc.trigger_printer_status(self.serial_number, ioref_list)

    @pytest.mark.parametrize("ioref", ['65539', '65559', '65595', '65671', '65674', '65765', '65912', '65934', '65966', '66168', '66213', '66251', '66316', '66328', '66339', '66353', '66419', '66435'])
    def test_07_check_link(self, ioref):
        """ 
        click link to check
        """
        self.printer_status.click_ps_ioref_item(ioref)
        links_list = self.printer_status.check_right_body_link()
        for check_link in links_list:     
            self.__check_link(check_link)

    #####################################################################
    #                       PRIVATE FUNCTIONS                        #
    #####################################################################
    def __check_link(self, check_link):     
        el = self.driver.find_object("right_body_text")        
        if check_link == 'More Information':           
            self.driver.click_by_coordinates(el, x_offset=0.05, y_offset=0.50)
            self.printer_status.verify_your_privacy_is_screen()
            self.printer_status.click_more_info_ok_btn()
            assert self.printer_status.verify_your_privacy_is_screen(raise_e=False) is False
        else:
            if check_link in ['View HP Privacy Statement Online', 'View More Information online']:
                self.driver.click_by_coordinates(el, x_offset=0.15, y_offset=0.98)
            elif check_link == 'https://instantink.hpconnected.com/':
                self.driver.click_by_coordinates(el, x_offset=0.5, y_offset=0.85)
            else:
                self.printer_status.click_ps_body_link(check_link)
            sleep(3)
            try:
                self.web_driver.add_window('check_link')
                sleep(2)
                self.web_driver.switch_window('check_link')
                sleep(3)
                current_url = self.web_driver.get_current_url()
                if  'HP Instant Ink' in check_link or 'instantink' in check_link:
                    assert "instantink.hpconnected.com" in current_url
                elif check_link == 'www.hp.com/recyle':
                    assert "hp.com" in current_url
                    assert "recycle_section" in current_url
                elif check_link == 'www.hp.com/recyle':
                    assert "recyle" in current_url
                elif check_link == 'www.hpsmart.com':
                    assert "www.hpsmart.com" in current_url
                else:
                    assert "hp.com" in current_url
            finally:
                self.web_driver.set_size('min')
            
    def __check_button(self, check_btn): 
        """
        Click "Explore Options" on the status message
        Click back arrow on the Supply Status screen.
        Verify Main UI shows after clicking the back arrow.
        https://hp-testrail.external.hp.com/index.php?/cases/view/14721519

        Click "Get more help" button
        Verify Chatbot launches in external web browser
        Verify the chatbot url in gotham log file is correct.
        https://hp-testrail.external.hp.com/index.php?/cases/view/16978335

        Check all the supplies related messages for "Estimated Supplies Levels" button
        Verify the "Estimated Supplies Levels" button is removed from all messages
        https://hp-testrail.external.hp.com/index.php?/cases/view/16861547

        Check all the supplies related messages for "Get Supplies" button
        Click on the "Explore Options" button
        Verify DSP screen should launch within the Gotham app
        Verify legacy supply status screen shows.
        https://hp-testrail.external.hp.com/index.php?/cases/view/16861549
        https://hp-testrail.external.hp.com/index.php?/cases/view/19447360
        """
        self.printer_status.click_ps_body_btn(check_btn)
        if check_btn == 'Get More Help':
            try:  
                self.web_driver.add_window("get_more_help")
                sleep(3)
                self.web_driver.switch_window("get_more_help")
                sleep(3)
                current_url = self.web_driver.get_current_url()
                assert "hp.com" in current_url
                assert "ProductSeriesNameOID" not in current_url
                assert "DevOS" not in current_url
                check_event_list = ['Ui\|IORefUtils:GetOnlineHelpURL\|TID:[0-9]+\|[\s]*Url \(encoded\): https:.*']
                for each_event in check_event_list:
                    self.pepto.check_pepto_data(each_event, check_data="p2")
            finally:
                self.web_driver.set_size('min')

        elif check_btn in ['Get Supplies', 'Estimated Supply Levels']:
            if self.printer_settings.verify_supply_status_page():
                sleep(5)
                self.printer_settings.select_printer_status_item()
                self.printer_status.verify_printer_ioref_status_screen()
            else:
                try:
                    self.web_driver.add_window("supply_status_page")
                    sleep(3)
                    self.web_driver.switch_window("supply_status_page")
                    sleep(3)
                    current_url = self.web_driver.get_current_url()
                    assert "hp.com" in current_url
                finally:
                    self.web_driver.set_size('min')
                
            if check_btn == 'Get Supplies':
                check_event_list = ['Ui\|ActionCenterViewModel:ElementClickHandler\|TID:[0-9]+\|[\s\S]*Element: id=idShopForSupplies', 'Ui|\Shell.xaml:NavigateTo\|TID:[0-9]+\|[\s]*Navigate SupplyDetail']
                for each_event in check_event_list:
                    self.pepto.check_pepto_data(each_event, check_data="p2")
