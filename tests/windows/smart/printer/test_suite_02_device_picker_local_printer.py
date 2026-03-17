import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from selenium.common.exceptions import NoSuchElementException


pytest.app_info = "GOTHAM"
class Test_Suite_02_Device_Picker_Local_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, check_bluetooth_network):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]

        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)

    def test_01_check_printer_not_in_dp_with_already_carousel(self):
        """
        user goes to the DP -> no printer found screen shows as the printer is already in the carousel
        user is selecting search by IP and putting the same IP as the printer is in the carousel

        Verify 2-N OOBE flow is not seen.
        Verify printer is added to main UI.
        user should not see the printer again after searching by IP
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/13802143
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13311464
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29487722
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/13258785
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/30658071(Obsolete)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/12382194
          
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)
        self.home.select_left_add_printer_btn()
        self.printers.verify_device_picker_screen() 
        #Ban Obsolete GOTH-22358
        # self.printers.search_printer(self.p.p_obj.ipAddress, value=False)
        # self.printers.verify_warning_message_display(w_const.TEST_TEXT.WARNING_MSG_VALUE, self.p.p_obj.ipAddress)
  
    def test_02_my_printer_isnt_listed_link(self):
        """
        Click on "My Printer Isn't Listed" link.
        Wi-Fi adapter is NOT enabled
        BT is NOT enabled

        Verify Reset beacon flows start 
        Verify "Turn on Bluetooth or Wi-Fi" screen is NOT shown
        Verify "Turn on Bluetooth or Wi-Fi" screen shows.(step 2 3)
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/12577951
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29870950
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29901329
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29901331
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29901328
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29870957
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/29870958
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/17511480
        """
        self.printers.select_my_printer_isnt_listed_link()
        self.printers.verify_turn_on_ble_or_wifi_screen_not_display()
        if self.printers.verify_exit_setup_btn(raise_e=False):
            self.printers.select_exit_setup()
            self.printers.select_exit_setup_btn_on_dialog()
            self.home.verify_home_screen()
            self.home.select_left_add_printer_btn()
            self.printers.verify_device_picker_screen()
        elif self.home.verify_navbar_back_btn(raise_e=False):
                self.home.select_navbar_back_btn(return_home=False)
                self.printers.verify_device_picker_screen()
        else:
            self.driver.restart_app()
            self.home.verify_home_screen()
            self.home.select_left_add_printer_btn()
        try:
            self.fc.trigger_printer_offline_status(self.p)
            self.printers.select_my_printer_isnt_listed_link()
            self.printers.verify_turn_on_ble_or_wifi_screen()
            self.printers.click_continue_btn()
            self.printers.verify_turn_on_ble_or_wifi_dialog()
            self.printers.click_try_again_btn()
            self.printers.verify_turn_on_ble_or_wifi_dialog()
            self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)
            self.printers.click_try_again_btn()
            self.printers.verify_device_picker_screen()
        except NoSuchElementException:
            raise NoSuchElementException("go to 'Turn on Bluetooth or Wi-Fi' screen without network flow is failed")
        finally:
            if "DunePrinterInfo" in str(self.p.p_obj):
                self.p.pp_module._power_on()
            else:
                self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)
