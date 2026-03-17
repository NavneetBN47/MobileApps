import pytest
from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_02_Help_Support_Non_Support_Language(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.help_support = cls.fc.fd["help_support"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')


    def test_01_help_support_screen_support_language(self):
        """
        (+) Click "Accept Cookies" on accept cookie banner, verify accept cookies doesn't show every time whenever you launch the help center 
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14779128
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715623       
        """
        self.fc.go_home()

        self.fc.select_a_printer(self.p)
        self.home.verify_carousel_printer_image()

        self.home.select_help_and_support_tile()
        self.help_support.verify_help_center_screen()
        if self.help_support.verify_accept_cookie_banner(raise_e=False) is True:
            self.help_support.select_accept_cookies()
        self.help_support.verify_chat_with_virtual_assistant_btn()
        self.help_support.verify_chat_with_virtual_assistant_image()
        self.help_support.verify_chat_with_virtual_assistant_content()

        self.home.select_navbar_back_btn()

        self.home.select_help_and_support_tile()
        self.help_support.verify_help_center_screen()
        assert self.help_support.verify_accept_cookie_banner(raise_e=False) is False
        self.home.select_navbar_back_btn()

    def test_02_help_support_screen_non_support_language(self):
        """
        (Non supported language) Check "Chat with Virtual Agent option on the list view, verify Virtual Agent option is hidden 
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14715629        
        """
        self.driver.ssh.send_command("Set-WinSystemLocale pl-PL")
        self.driver.ssh.send_command("Set-WinHomeLocation -GeoId 191")
        self.driver.ssh.send_command("Set-Culture pl-PL")

        sleep(2)

        self.home.select_help_and_support_tile()
        self.help_support.verify_help_center_screen()
        assert self.help_support.verify_chat_with_virtual_assistant_btn(timeout=3, raise_e=False) is False
        assert self.help_support.verify_chat_with_virtual_assistant_image(timeout=3, raise_e=False) is False
        assert self.help_support.verify_chat_with_virtual_assistant_content(timeout=3, raise_e=False) is False
        
        self.home.select_navbar_back_btn()

    def test_03_set_back_to_enu_language(self):
        """
        Set back to English language
        """
        self.driver.ssh.send_command("Set-WinSystemLocale en-US")
        self.driver.ssh.send_command("Set-WinHomeLocation -GeoId 244")
        self.driver.ssh.send_command("Set-Culture en-US")
