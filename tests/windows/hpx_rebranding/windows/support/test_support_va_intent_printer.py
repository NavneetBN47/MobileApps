from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_VA_Intent_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)

        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.task_util = TaskUtilities(cls.driver.ssh)
        cls.registry = RegistryUtilities(cls.driver.ssh)

        cls.stack = request.config.getoption("--stack")
        cls.__first_start_HPX(cls)

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_environment()
        self.fc.ensure_web_password_credentials_cleared()
        if self.stack in ["itg"]:
            self.fc.set_proxy_on_remote_windows("web-proxy.corp.hp.com:8080")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59598251")
    def test_01_hpx_rebranding_C59598251(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59598251
        """ 
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        self.__click_start_virtual_assist_btn()
        assert self.fc.fd["devices_support_pc_mfe"].get_va_page_title() == "What can we help you with?"
        assert self.fc.fd["devices_support_pc_mfe"].verify_printer_setup_btn() is True
        assert self.fc.fd["devices_support_pc_mfe"].verify_printer_offline_btn() is True
        assert self.fc.fd["devices_support_pc_mfe"].verify_printer_connectivity_issue_btn() is True
        assert self.fc.fd["devices_support_pc_mfe"].verify_printer_scanning_btn() is True
        assert self.fc.fd["devices_support_pc_mfe"].verify_printer_quality_btn() is True
        self.fc.fd["devices_support_pc_mfe"].click_va_show_more_printer_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_ink_cartridge_btn() is True
        assert self.fc.fd["devices_support_pc_mfe"].verify_print_job_stuck_in_queue_btn() is True
        assert self.fc.fd["devices_support_pc_mfe"].verify_paper_jam_issue_btn() is True
        assert self.fc.fd["devices_support_pc_mfe"].verify_others_printer_btn() is True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59892623")
    def test_02_hpx_rebranding_C59892623(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59892623
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_printer_setup_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I can help with setting up your printer. Which printer setup topic would you like help with?") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I\'m setting up my printer for the first time") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I want to use my printer with additional computers or mobile devices") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("My Wi-Fi settings changed on a printer I have been using, and I need to reconnect it") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I want to set up scanning on a printer I have been using") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I want to set up faxing on a printer I have been using") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I don't need help with setting up the printer. I'd like to rephrase my question.") == True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59897842")
    def test_03_hpx_rebranding_C59897842(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59897842
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_printer_offline_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("If your printer is showing as Offline or Unavailable, I can help! Basic steps can take 5 to 10 minutes.") == True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59898927")
    def test_04_hpx_rebranding_C59898927(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59898927
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_printer_connectivity_issue_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Restart devices") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Restart your computer or mobile device, printer, and router to clear any error states.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Disconnect your computer or mobile device from the network name (SSID), and then reconnect it to the same network name your printer is connected to.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("If the printer is available and has a ready status, the issue is resolved. You do not need to continue troubleshooting.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Press the Power button to turn off the printer. If the printer does not turn off, disconnect the power cord from the printer and from the power source.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Turn off the computer or mobile device that the printer was set up with.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Restart the router.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Reconnect the power cord to the printer and to a wall outlet.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("NOTE : HP recommends plugging the printer directly into a wall outlet.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Turn on the computer or mobile device.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Check the connection to make sure the same network is used by the printer and the device.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Computer or mobile device: Open the list of available networks and make sure it is connected to the correct network.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Printer: Check the Wireless light on the control panel. If it is solid blue the printer is connected.") == True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59899000")
    def test_05_hpx_rebranding_C59899000(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59899000
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_printer_scanning_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I can help you with scanning. Which topic would you like help with?") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("How to Scan") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Scanner not found or connected") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message("\"Scanner Failure\" error message") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Determine if my printer has scan capability") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Scans don\'t look good") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I don\'t need help with scanning. I'd like to rephrase my question") == True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59899003")
    def test_06_hpx_rebranding_C59899003(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59899003
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_printer_quality_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I can help with print quality issues, including:") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Printing blank pages:") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Printer adds extra blank pages in the end") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Printer only prints blank pages") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Printouts are damp") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Printouts are damp or smudge when handled, and ink is not drying.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Other print quality issues:") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Color or black ink missing on printouts") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Streaking or fading on pages") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Blurred, fuzzy or smeared text") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Any other issue with printouts") == True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59899556")
    def test_07_hpx_rebranding_C59899556(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59899556
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_show_more_printer_btn()
        self.fc.fd["devices_support_pc_mfe"].click_ink_cartridge_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Please select the type of error you see") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Cartridges incompatible or incorrect") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Cartridges depleted") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Cartridges missing or not detected") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Cartridge not communicating with printer") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Use SETUP cartridges message") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("All other ink cartridge error") == True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59899560")
    def test_08_hpx_rebranding_C59899560(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59899560
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_show_more_printer_btn()
        self.fc.fd["devices_support_pc_mfe"].click_print_job_stuck_in_queue_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I can help with print jobs stuck in print queue.") == True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59899566")
    def test_09_hpx_rebranding_C59899566(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59899566
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_show_more_printer_btn()
        self.fc.fd["devices_support_pc_mfe"].click_paper_jam_issue_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Paper jams, real or false, can be frustrating. Let’s find a solution for this issue.") == True

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C59899696")
    def test_10_hpx_rebranding_C59899696(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59899696
        """
        self.fc.select_device()
        self.__sign_in_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index(2)
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_va_show_more_printer_btn()
        self.fc.fd["devices_support_pc_mfe"].click_others_printer_btn()
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Type a question below or choose a popular topic.") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("How can I assist you?") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Use AI Search") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("PC") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Printer") == True
        self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Great deals from HP") == True
        
    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __start_HPX(self, maxmized=False):
        self.fc.restart_app()
        if maxmized:
            self.fc.maximize_window()
        if self.fc.fd["hpx_fuf"].verify_accept_cookies_button_show():
            self.fc.fd["hpx_fuf"].click_accept_cookies_button()
        if self.fc.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fc.fd["hpx_fuf"].click_accept_all_button()
        if self.fc.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fc.fd["hpx_fuf"].click_continue_as_guest_button()
        if self.fc.fd["hpx_fuf"].verify_what_is_this_dialog_show():
            self.fc.fd["hpx_fuf"].click_what_is_new_skip_button()

    def __select_device(self, maxmized=False, index=0):
        self.__start_HPX(maxmized=maxmized)
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index(index)

    def __click_start_virtual_assist_btn(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()  

    def __sign_in_HPX(self, sign_in_from_profile=False):
        self.fc.sign_in("dtodxte2eseponboarded100@yopmail.com", "P@ssw0rd", self.web_driver, sign_in_from_profile=sign_in_from_profile)             