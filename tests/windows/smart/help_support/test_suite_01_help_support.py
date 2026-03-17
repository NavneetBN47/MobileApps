import pytest
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_01_Help_Support(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, utility_web_session, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.help_support = cls.fc.fd["help_support"]
        cls.diagnose_fix = cls.fc.fd["diagnose_fix"]

        cls.stack = request.config.getoption("--stack")

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    def test_01_verify_help_center_webview_without_printer(self):
        """
        Tile name change for "Help Center" to "Help & Support", verify correct name shows
        (No Printer added)Click "Help Center" Tile on the Main UI, Verify WebView opens within the HP Smart
        Click "Help Center" tile on the Main UI, verify correct URL shows in the Gotham log
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715621
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715638
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/16845773        
        """
        self.fc.go_home()

        el = self.home.verify_help_and_support_tile()
        assert el.text == "Help & Support"

        self.home.select_help_and_support_tile()
        self.help_support.verify_help_center_screen()
        self.help_support.verify_chat_with_virtual_assistant_btn()
        self.help_support.verify_chat_with_virtual_assistant_image()

        self.check_url_in_hp_smart_log(self.stack)

    def test_02_check_diagnose_and_fix_link_without_printer(self):
        """
        Start PSDr from Help & Support screen, verify results
        Verify PSDr screen shows if no printer was added to home page
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24841203    
        """
        self.help_support.swipe_and_click_item(self.help_support.PRINTING_ITEM)
        self.help_support.verify_help_center_printing_screen()
        self.help_support.swipe_and_click_item(self.help_support.DIAGNOSE_FIX_LINK)

        self.web_driver.add_window("diagnose_fix")
        if "diagnose_fix" not in self.web_driver.session_data["window_table"].keys():
            self.help_support.swipe_and_click_item(self.help_support.DIAGNOSE_FIX_LINK)
            self.web_driver.add_window("diagnose_fix")
        self.web_driver.switch_window("diagnose_fix")

        current_url = self.web_driver.get_current_url()
        assert "support.hp.com" in current_url
        self.web_driver.close_window("diagnose_fix")
        self.web_driver.set_size("min")

        self.help_support.verify_help_center_printing_screen()
        self.home.select_navbar_back_btn()

    def test_03_verify_help_center_webview_with_printer(self):
        """
        Click "Help & Support" Tile on the Main UI, Verify the help center web view opens within the app
        (Supported language) Check "Chat with Virtual Agent" link on list view, verify "Chat with Virtual Agent" link shows in the help center web view
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/15991975
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715626
        """
        self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)
        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        self.home.select_help_and_support_tile()
        self.help_support.verify_help_center_screen()

    @pytest.mark.parametrize("webpage", ["CHAT_WITH_VIRTUAL_ASSISTANT", "CONTACT_HP", "PRINTER_SUPPORT", "PRINT_ANYWHERE_ONLINE_SUPPORT", "SHORTCUTS_ONLINE_SUPPORT", "HP_MOBILE_PRINTING"])
    def test_04_verify_links_on_help_support_page(self, webpage):
        """
        Click "Chat with Virtual Assistant", "Contact HP", "Printer Support", "Print Anywhere Online Support", 
        "Smart Tasks Online Support", "HP Mobile Printing" on list view, verify correct website opens in the external web browser
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715628
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715635
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715630
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715631
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715632
            -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715633
            
        """
        webpage_links = {"CHAT_WITH_VIRTUAL_ASSISTANT": self.help_support.CHAT_WITH_VIRTUAL_ASSISTANT_LINK,
                 "CONTACT_HP": self.help_support.CONTACT_HP_LINK,
                 # HPC3-8530 - PRINTER SUPPORT LINK URL ISSUE FOR DUNE PRINTER
                 "PRINTER_SUPPORT": self.help_support.PRINTER_SUPPORT_LINK,
                 "PRINT_ANYWHERE_ONLINE_SUPPORT": self.help_support.PRINT_ANYWHERE_ONLINE_SUPPORT_LINK,
                 "SHORTCUTS_ONLINE_SUPPORT": self.help_support.SHORTCUTS_ONLINE_SUPPORT_LINK,
                 "HP_MOBILE_PRINTING": self.help_support.HP_MOBILE_PRINTING_LINK}

        webpage_urls = {"CHAT_WITH_VIRTUAL_ASSISTANT": self.help_support.CHAT_WITH_VIRTUAL_ASSISTANT_URL,
                "CONTACT_HP": self.help_support.CONTACT_HP_URL,
                "PRINTER_SUPPORT": self.help_support.PRINTER_SUPPORT_URL,
                "PRINT_ANYWHERE_ONLINE_SUPPORT": self.help_support.PRINT_ANYWHERE_ONLINE_SUPPORT_URL,
                "SHORTCUTS_ONLINE_SUPPORT": self.help_support.SHORTCUTS_ONLINE_SUPPORT_URL,
                "HP_MOBILE_PRINTING": self.help_support.HP_MOBILE_PRINTING_URL}

        if webpage in ["CHAT_WITH_VIRTUAL_ASSISTANT", "CONTACT_HP"]:
            self.help_support.click_item(webpage_links[webpage])
        else:
            self.help_support.swipe_and_click_item(webpage_links[webpage])
        self.web_driver.add_window(webpage)
        if webpage not in self.web_driver.session_data["window_table"].keys():
            if webpage in ["CHAT_WITH_VIRTUAL_ASSISTANT", "CONTACT_HP"]:
                self.help_support.click_item(webpage_links[webpage])
            else:
                self.help_support.swipe_and_click_item(webpage_links[webpage])
            self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)

        current_url = self.web_driver.get_current_url()

        for sub_url in webpage_urls[webpage]:
            assert sub_url in current_url
        
        self.web_driver.close_window(self.web_driver.current_window)
        self.web_driver.set_size("min")

    def test_05_check_download_here_link_with_printer(self):
        """
        Click "Fax" option under Printer Features, verify fax driver link is available in the contente
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/25625294   
        """
        self.help_support.click_item(self.help_support.FAX_ITEM)
        self.help_support.verify_hp_mobile_fax_screen()
        self.help_support.click_item(self.help_support.DOWNLOAD_HERE_LINK)

        self.web_driver.add_window("fax_driver")
        if "fax_driver" not in self.web_driver.session_data["window_table"].keys():
            self.help_support.click_item(self.help_support.DOWNLOAD_HERE_LINK)
            self.web_driver.add_window("fax_driver")
        self.web_driver.switch_window("fax_driver")

        current_url = self.web_driver.get_current_url()
        logging.info("Checking URL: {}".format(current_url))

        for sub_url in self.help_support.FAX_DRIVER_DOWNLOAD_URL:
            assert sub_url in current_url
        
        self.web_driver.close_window(self.web_driver.current_window)
        self.web_driver.set_size("min")

    def test_06_check_diagnose_fix_link_with_printer(self):
        """
        Start PSDr from Help & Support screen, verify results
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/24841203 
        """
        self.help_support.click_item(self.help_support.PRINTING_ITEM)
        self.help_support.click_item(self.help_support.DIAGNOSE_FIX_LINK)
        self.diagnose_fix.verify_diagnoseing_and_fixing_text_display()
        self.diagnose_fix.verify_diagnosis_complete_screen()
        self.home.select_navbar_back_btn(return_home=False)
        self.home.verify_help_and_support_page()

    def test_07_back_arrow(self):
        """
        Verify user navigates to the Main UI after clicking the back arrow.
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715624
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/22484603
        """
        self.home.select_navbar_back_btn()

    
    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def check_url_in_hp_smart_log(self, stack):
        if stack == "stage":
            check_string_1 = 'SupportViewModel:GenerateHelpCenterPayload|TID:2|	ret payload:{"chatbotLink":{"href":"https://virtualagent-dev.hpcloud.hp.com?botclient=hpsmart&botsubclient=win&LaunchPoint=HelpCenter'
            check_string_2 = 'SupportViewModel:GenerateHelpCenterPayload|TID:2|	Payload URL: https://www.hpsmartstage.com/us/en/in-app-help/desktop'
        elif stack == "pie":
            check_string_1 = 'SupportViewModel:GenerateHelpCenterPayload|TID:2|	ret payload:{"chatbotLink":{"href":"https://virtualagent-dev.hpcloud.hp.com?botclient=hpsmart&botsubclient=win&LaunchPoint=HelpCenter'
            check_string_2 = 'SupportViewModel:GenerateHelpCenterPayload|TID:2|	Payload URL: https://www.hpsmartpie.com/us/en/in-app-help/desktop'
        else:
            check_string_1 = 'SupportViewModel:GenerateHelpCenterPayload|TID:2|	ret payload:{"chatbotLink":{"href":"https://virtualagent.hpcloud.hp.com?botclient=hpsmart&botsubclient=win&LaunchPoint=HelpCenter'
            check_string_2 = 'SupportViewModel:GenerateHelpCenterPayload|TID:2|	Payload URL: https://www.hpsmart.com/us/en/in-app-help/desktop'
        
        self.fc.check_gotham_log(check_string_1)
        self.fc.check_gotham_log(check_string_2)