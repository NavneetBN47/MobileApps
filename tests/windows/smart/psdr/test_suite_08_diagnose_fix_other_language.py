import pytest
import logging

from MobileApps.libs.ma_misc import conftest_misc as c_misc
import MobileApps.resources.const.windows.const as w_const
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_08_Diagnose_Fix_other_language(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.diagnose_fix = cls.fc.fd["diagnose_fix"]
        cls.welcome = cls.fc.fd["welcome_web"]
        cls.valueprop = cls.fc.fd["ows_value_prop"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]
     
        cls.stack = request.config.getoption("--stack")
        cls.locale = request.config.getoption("--locale")
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)


    def test_01_go_to_main_ui(self):
        """
        go to Main UI and select printer
        """
        logging.info("Unintall HP Smart...")
        self.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(1)
        if self.locale == "es":
            logging.info("The PC is being set to spanish language")
            self.driver.ssh.send_command("Set-WinSystemLocale es-ES")
            self.driver.ssh.send_command("Set-WinHomeLocation -GeoId 217")
            self.driver.ssh.send_command("Set-Culture es-ES")
            self.driver.ssh.send_command("Set-WinUserLanguageList es-ES -Force")
        elif self.locale == "pt":
            logging.info("The PC is being set to portuguese language")
            self.driver.ssh.send_command("Set-WinSystemLocale pt-BR")
            self.driver.ssh.send_command("Set-WinHomeLocation -GeoId 193")
            self.driver.ssh.send_command("Set-Culture pt-BR")
            self.driver.ssh.send_command("Set-WinUserLanguageList pt-BR -Force")
        elif self.locale == "zh":
            logging.info("The PC is being set to chinese language")
            self.driver.ssh.send_command("Set-WinSystemLocale zh-CN")
            self.driver.ssh.send_command("Set-WinHomeLocation -GeoId 45")
            self.driver.ssh.send_command("Set-Culture zh-CN")
            self.driver.ssh.send_command("Set-WinUserLanguageList zh-CN -Force")
        logging.info("Reinstall HP Smart...")
        self.driver.ssh.send_command(self.driver.session_data["installer_path"] + "\\Install.ps1 -Force", timeout=60)
        launch_activity = self.fc.get_activity_parameter()[0]
        self.fc.change_stack_server(stack=self.stack, restart=False)
        self.driver.launch_app(launch_activity)
        self.welcome.verify_welcome_screen()
        self.welcome.click_accept_all_btn()
        sleep(5)
        self.valueprop.select_native_value_prop_buttons(index=3)
        self.home.verify_home_screen()
        self.fc.select_a_printer(self.p)

    def test_02_check_all_button_on_here_are_your_results_screen(self):
        """
        Computer language must be set as Spanish
        Click "HP Support Forum" link on the Diagnose & Fix (If you're still having…) screen
        Verify correct website opens
        Verify Gotham log shows correct loglin
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556052
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556053
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556056
        """
        self.home.select_diagnose_and_fix_btn()
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        self.fc.trigger_printer_offline_status(self.p)
        self.home.select_diagnose_and_fix_start_btn()
        self.diagnose_fix.verify_here_are_your_results_text_2_screen()
        self.diagnose_fix.click_next_btn()
        self.diagnose_fix.verify_if_you_are_still_having_problems_screen()
        self.diagnose_fix.click_hp_support_forum_link()
        sleep(5)
        webpage = "hp_support_forum_link"
        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.diagnose_fix.click_hp_support_forum_link()
            self.web_driver.add_window(webpage)
        self.web_driver.switch_window(webpage)
        self.web_driver.close_window(webpage)
        event_msg_main = "Ui|DiagnoseAndFixViewModel:Initialize|TID:2|"
        event_msg_es = "Ui|PsDrLinksVm:UpdateLinksPerLanguage|TID:2| ret CurrentLanguage:es CurrentCulture.Name:es-ES SupportForum:http://www.hp.com/foro ShowVirtualAgentLink:True ShowSupportForumLink:True"
        event_msg_pt = "Ui|PsDrLinksVm:UpdateLinksPerLanguage|TID:2| ret CurrentLanguage:pt CurrentCulture.Name:pt-BR SupportForum:http://www.hp.com.br/forum ShowVirtualAgentLink:True ShowSupportForumLink:True"
        event_msg_zh = "Ui|PsDrLinksVm:UpdateLinksPerLanguage|TID:2| ret CurrentLanguage:zh CurrentCulture.Name:zh-CN SupportForum:http://www.hp.com.cn/hpcommunity ShowVirtualAgentLink:True"
        self.fc.check_gotham_log(event_msg_main)
        if self.locale == "es":
            self.fc.check_gotham_log(event_msg_es)
        elif self.locale == "pt":
            self.fc.check_gotham_log(event_msg_pt)
        elif self.locale == "zh":
            self.fc.check_gotham_log(event_msg_zh)
        
    def test_03_clean_env(self):
        self.driver.terminate_app()
        logging.info("Unintall HP Smart...")
        self.driver.ssh.remove_app(w_const.PROCESS_NAME.GOTHAM)
        sleep(1)
        self.driver.ssh.send_command("Set-WinSystemLocale en-US")
        self.driver.ssh.send_command("Set-WinHomeLocation -GeoId 244")
        self.driver.ssh.send_command("Set-Culture en-US")
        self.driver.ssh.send_command("Set-WinUserLanguageList en-US -Force")
        logging.info("Reinstall HP Smart...")
        self.driver.ssh.send_command(self.driver.session_data["installer_path"] + "\\Install.ps1 -Force", timeout=60)
