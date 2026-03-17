import pytest

from MobileApps.libs.ma_misc import conftest_misc as c_misc
from selenium.common.exceptions import NoSuchElementException
import MobileApps.resources.const.windows.const as w_const
from time import sleep

pytest.app_info = "GOTHAM"
class Test_Suite_06_Diagnose_Fix_Hero_Flow_3(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session, utility_web_session, restore_devices_status):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup
        cls.p = load_printers_session
        cls.web_driver = utility_web_session

        cls.home = cls.fc.fd["home"]
        cls.diagnose_fix = cls.fc.fd["diagnose_fix"]
        cls.scan = cls.fc.fd["scan"]
     
        cls.stack = request.config.getoption("--stack")
       
        cls.ssid, cls.password = c_misc.get_wifi_info(request)
        cls.host = request.config.getoption("--mobile-device")
        cls.user = "exec"
        cls.driver.connect_to_wifi(cls.host, cls.user, cls.ssid, cls.password)


    def test_01_go_to_main_ui(self):
        """
        go to Main UI and select printer
        """
        self.fc.go_home()
        self.fc.select_a_printer(self.p)

    def test_02_check_all_button_on_here_are_your_results_screen(self):
        """
        Click "Diagnose & Fix" icon on the navigation pane on Main UI (Win)/ Menu bar->Printers (Mac) -> 
        verify "Diagnose & Fix" screen shows
        Click "Start" button on the "Diagnose & Fix" button
        Diagnosing & fixing screen for a brief moment and eventually "Diagnosis complete. 
        Here are your results." will show
        Click "Next" on "Diagnosis complete. 
        Click "Chat with Virtual Agent" link
        Click "Test Print" button
        Click the "Done" button
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14419934
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33339369
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14592260
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554641
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14512812
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14554639
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33339370
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556039
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556048
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556036(high)
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556037(low)
        """
        # self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        # self.driver.ssh.send_command("netsh wlan disconnect")
        self.home.select_diagnose_and_fix_btn()
        self.driver.ssh.send_command('Remove-Printer -Name "*HP*"')
        self.fc.trigger_printer_offline_status(self.p)
        self.home.select_diagnose_and_fix_start_btn()
        self.diagnose_fix.verify_here_are_your_results_text_2_screen()
        self.diagnose_fix.click_try_again_btn()
        self.diagnose_fix.verify_diagnoseing_and_fixing_text_display()
        self.diagnose_fix.verify_here_are_your_results_text_2_screen()
        self.diagnose_fix.click_next_btn()
        self.diagnose_fix.verify_if_you_are_still_having_problems_screen()

    def test_03_click_hp_support_link(self):
        """
        Click "HP Support Forum" link on the Diagnose & Fix (If you're still having…) screen

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556051
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/15989721
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/15989722
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/15989720
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/33339397
        """
        self.diagnose_fix.click_hp_support_forum_link()
        sleep(5)
        webpage = "hp_support_forum_link"
        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.diagnose_fix.click_hp_support_forum_link()
            self.web_driver.add_window(webpage)
        sleep(3)
        self.web_driver.switch_window(webpage)
        sleep(3)
        current_url = self.web_driver.get_current_url()
        for sub_url in self.diagnose_fix.hp_support_forum_link:
            assert sub_url in current_url
        self.web_driver.close_window(webpage)

    def test_04_click_virtual_agent_link(self): 
        self.diagnose_fix.click_chat_with_virtual_agent_link()
        webpage = "agent_link"
        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.diagnose_fix.click_chat_with_virtual_agent_link()
            self.web_driver.add_window(webpage)
        sleep(3)
        self.web_driver.switch_window(webpage)
        sleep(3)
        current_url = self.web_driver.get_current_url()
        if self.stack == "production":
            for sub_url in self.diagnose_fix.prod_link:
                assert sub_url in current_url
        else:
            for sub_url in self.diagnose_fix.stage_link:
                assert sub_url in current_url
        self.web_driver.close_window(webpage)

    def test_05_click_troubleshppting_link(self):
        """
        check  "Online Troubleshooting" link on the Diagnose & Fix 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556049
        """
        self.diagnose_fix.click_online_troubleshooting_link()
        webpage = "troubleshooting_link"
        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.diagnose_fix.click_online_troubleshooting_link()
            self.web_driver.add_window(webpage)
        sleep(3)
        self.web_driver.switch_window(webpage)
        sleep(3)
        current_url = self.web_driver.get_current_url()
        for sub_url in self.diagnose_fix.online_troubleshooting_link:
            assert sub_url in current_url
        self.web_driver.close_window(webpage)

    def test_06_click_software_link(self):
        """
        Click "Software and Driver Download" link on the Check Diagnose & Fix screen

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/14556050
        """
        self.diagnose_fix.click_software_and_driver_downloads_link()
        webpage = "software_link"
        if webpage not in self.web_driver.session_data["window_table"].keys():
            self.diagnose_fix.click_software_and_driver_downloads_link()
            self.web_driver.add_window(webpage)
        sleep(3)
        self.web_driver.switch_window(webpage)
        sleep(3)
        current_url = self.web_driver.get_current_url()
        for sub_url in self.diagnose_fix.online_troubleshooting_link:
            assert sub_url in current_url
        self.web_driver.close_window(webpage)
        self.diagnose_fix.verify_diagnosis_complete_screen()
        sleep(5)
        self.diagnose_fix.click_test_print_btn()
        self.scan.verify_print_dialog()
        self.scan.click_print_dialog_cancel_btn()
        self.diagnose_fix.verify_if_you_are_still_having_problems_screen()
        self.diagnose_fix.click_done_btn()
        self.home.verify_home_screen()
        event_msg_1 = "Ui|DiagnoseAndFixViewModel:Initialize|TID:2|"
        event_msg_2 = "Ui|DiagnoseAndFixViewModel:Initialize|TID:2|"
        event_msg_3 = "Ui|PsDrLinksVm:UpdateLinksPerLanguage|TID:2|	ret CurrentLanguage:en CurrentCulture.Name:en-US SupportForum:http://www.hp.com/supportcommunity ShowVirtualAgentLink:True ShowSupportForumLink:True"
        f = self.driver.ssh.remote_open(w_const.TEST_DATA.HP_SMART_LOG_PATH)
        data = f.read().decode("utf-8")
        f.close()
        if str(event_msg_1) and str(event_msg_2) and str(event_msg_3) in data:
            return True
        raise NoSuchElementException(
            "Fail to found {} or {} or {}".format(event_msg_1, event_msg_2, event_msg_3))

    def test_07_connect_wifi(self):
        self.fc.restore_printer_online_status(self.p)
        