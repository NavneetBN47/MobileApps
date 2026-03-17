import pytest
import logging

from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_07_Diagnose_Fix_Hero_non_support_language(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.diagnose_fix = cls.fc.fd["diagnose_fix"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.valueprop = cls.fc.fd["ows_value_prop"]
     
        cls.stack = request.config.getoption("--stack")
       
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)


    def test_01_go_to_main_ui(self):
        """
        set other Language then go to Main UI and select printer
        """
        logging.info("Unintall HP Smart...")
        self.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(1)
        self.driver.ssh.send_command("Set-WinSystemLocale it-IT")
        self.driver.ssh.send_command("Set-WinHomeLocation -GeoId 118")
        self.driver.ssh.send_command("Set-Culture it-IT")
        self.driver.ssh.send_command("Set-WinUserLanguageList it-IT -Force")
        logging.info("Reinstall HP Smart...")
        self.driver.ssh.send_command(self.driver.session_data["installer_path"] + "\\Install.ps1 -Force", timeout=60)
        launch_activity = self.fc.get_activity_parameter()[0]
        self.driver.launch_app(launch_activity)
        self.welcome.verify_welcome_screen()
        self.welcome.click_accept_all_btn()
        sleep(5)
        self.valueprop.select_native_value_prop_buttons(index=3)
        self.home.verify_home_screen()
        self.fc.select_a_printer(self.p)

    def test_02_check_all_button_on_here_are_your_results_screen(self):
        """
        Computer language must be set other than [English, Spanish, German, Dutch, French, Japanese, Simplified Chinese, Portuguese (Portugal)]
        Generate Error from the attached screen
        Click the "Next" button on the "Diagnosis complete. Here are your results" screen
        Observe Diagnose & Fix (If you're still having…) screen
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556046(low)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556058
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/28511941

        """
        self.home.select_diagnose_and_fix_btn()
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        self.fc.trigger_printer_offline_status(self.p)
        self.home.select_diagnose_and_fix_start_btn()
        self.diagnose_fix.verify_here_are_your_results_text_2_screen()
        self.diagnose_fix.click_next_btn()
        self.diagnose_fix.verify_if_you_are_still_having_problems_screen()
        self.diagnose_fix.verify_hp_support_forum_link_diaplay()
        assert self.diagnose_fix.verify_chat_with_virtual_agent_link_diaplay(raise_e=False) is False

    def test_03_clean_env(self):
        if "DunePrinterInfo" in str(self.p.p_obj):
            self.p.pp_module._power_on()
        else:
            self.driver.connect_to_wifi(self.host, self.user, self.ssid, self.password)
        self.driver.ssh.send_command("Set-WinSystemLocale en-US")
        self.driver.ssh.send_command("Set-WinHomeLocation -GeoId 244")
        self.driver.ssh.send_command("Set-Culture en-US")
        self.driver.ssh.send_command("Set-WinUserLanguageList en-US -Force")
