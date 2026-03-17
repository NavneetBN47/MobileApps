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
class Test_Suite_VA_Intent(object):
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

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59591943")
    def test_01_hpx_rebranding_C59591943(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59591943
        """ 
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_computerisslow_btn() is True, "Computer is slow button is not displayed"
        assert self.fc.fd["devices_support_pc_mfe"].verify_displayortouchissue_btn() is True, "Display or touch issue button is not enabled"
        assert self.fc.fd["devices_support_pc_mfe"].verify_keyboardmousesettings_btn() is True, "Keyboard or mouse settings button is not enabled"
        assert self.fc.fd["devices_support_pc_mfe"].verify_restorecomputersettings_btn() is True, "Restore computer settings button is not enabled"
        assert self.fc.fd["devices_support_pc_mfe"].verify_nosound_btn() is True, "No sound button is not enabled"
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_connectivityissue_btn() is True, "Connectivity issue button is not enabled"
        assert self.fc.fd["devices_support_pc_mfe"].verify_computerlocksorfreezes_btn() is True, "Computer locks or freezes button is not enabled"
        assert self.fc.fd["devices_support_pc_mfe"].verify_windowssupport_btn() is True, "Windows support button is not enabled"
        assert self.fc.fd["devices_support_pc_mfe"].verify_computerwillnotstart_btn() is True, "Computer will not start button is not enabled"
        assert self.fc.fd["devices_support_pc_mfe"].verify_cannotlogincomputer_btn() is True, "Cannot login computer button is not enabled"
        assert self.fc.fd["devices_support_pc_mfe"].verify_storgageissue_btn() is True, "Storage issue button is not enabled"
        assert self.fc.fd["devices_support_pc_mfe"].verify_cannotconnectprinter_btn() is True, "Cannot connect printer button is not enabled"
        assert self.fc.fd["devices_support_pc_mfe"].verify_otherpc_btn() is True, "Cannot connect to other PC button is not enabled"
        self.fc.fd["devices_support_pc_mfe"].click_vashowlesspc_btn()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() is True, "Start Virtual Assist button is not displayed"

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59592891")
    def test_02_hpx_rebranding_C59592891(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59592891
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerisslow_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Run Windows Update") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Update your Windows 11 or Windows 10 computer using Windows Update.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("HP PCs - Updating drivers using Windows Update (Windows 11, 10)") == True
        # assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Click here to view a how to video.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("In Windows, search for and open Check for updates. If there are any available updates, they begin automatically.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("NOTE: To download and install optional updates, use the following instructions for your operating system:") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("In Windows 11, select Advanced options, select Optional updates, select the updates that you want to install, and then click Download & install.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("In Windows 10, select View all optional updates, select the updates that you want to install, and then click Download and install.") == True  
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("After the updates install, restart your computer when prompted.") == True  

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59593877")
    def test_03_hpx_rebranding_C59593877(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59593877
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_displayortouchissue_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I can help with the PC\'s display or touchscreen and monitors including:") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Touchscreens:") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("sensitivity, inaccurate or non-responsive to touch") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Image quality:") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("blurry, fuzzy or stretched image, lines in screen, dots in image, flickering or blank screen.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Damage:") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("cracked or scratched screens") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Connecting to multiple:") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("connecting or configuring another monitor") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Settings:") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("desktop backgrounds or icons, screen savers, brightness, text size and resolution") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59594092")
    def test_04_hpx_rebranding_C59594092(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59594092
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_keyboardmousesettings_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("What can I help with?") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Built-In Keyboard") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Built-In Touchpad") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Wireless Keyboard") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Wired Keyboard") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Purchase a Keyboard") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59594479")
    def test_05_hpx_rebranding_C59594479(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59594479
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_restorecomputersettings_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Windows Recovery") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I can help get your PC back up and running as fast as possible, select the issue below that applies to your situation.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Note: A full reinstallation may not be necessary to resolve the issue, read through the options listed below.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("System Restore will restore your PC back to a previous time. Resetting your PC will attempt to repair your PC by reinstalling Windows.") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59594696")
    def test_06_hpx_rebranding_C59594696(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59594696
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_nosound_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Restart the computer") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("If no sound comes from the speakers or headphones connected to your computer, an application controlling the device might be preventing other applications from using the speakers or headphones.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Restart your computer, and then test the audio to see if the problem is fixed.") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59595228")
    def test_07_hpx_rebranding_C59595228(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59595228
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()
        self.fc.fd["devices_support_pc_mfe"].click_connectivityissue_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Which method of troubleshooting would you prefer?") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Watch a video") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Read step by step instructions") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Help with printer Wi-Fi issues") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Rephrase my question") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59595237")
    def test_08_hpx_rebranding_C59595237(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59595237
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerlocksorfreezes_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Please choose the issue you need help with.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Error messages displayed on a blue screen") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("After waking from sleep mode") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Other computer lock ups or freezing issues​") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I\'d like to rephrase my question") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59595401")
    def test_09_hpx_rebranding_C59595401(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59595401
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()
        self.fc.fd["devices_support_pc_mfe"].click_windowssupport_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I can help you with Operating System issues.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Please select below what you need help with:") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Help with HP System Recovery") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Can\'t boot into Windows") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I can\'t sign into Windows") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Windows Support") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("OS Update") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59595402")
    def test_10_hpx_rebranding_C59595402(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59595402
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()
        self.fc.fd["devices_support_pc_mfe"].click_computerwillnotstart_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("If your device is not turning on, or is not starting correctly, I can help.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I'm going to ask some questions to confirm that I am understanding the issue correctly.") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59595403")
    def test_11_hpx_rebranding_C59595403(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59595403
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()
        self.fc.fd["devices_support_pc_mfe"].click_cannotlogincomputer_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Which method are you using to log in to Windows?") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Typing in a password") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Typing in a Pin ID (number)") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Windows Hello (facial recognition)") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Fingerprint sign on") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59595403")
    def test_12_hpx_rebranding_C52215051(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/52215051
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()   
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()
        self.fc.swipe_window(direction="down", distance=6)
        self.fc.fd["devices_support_pc_mfe"].click_storgageissue_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Which option best describes what you need help with?") == True
        # assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Low Disk Space") == True
        # assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Hard Disk Failure") == True
        # assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("USB Storage devices") == True
        # assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Purchase USB Storage devices") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("I have a 24 digit failure id") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Low disk spaces issues and errors") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("SMART hard disk error") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Boot device not found") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Hard disk error during start up") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Purchase storage devices") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59595410")
    def test_13_hpx_rebranding_C59595410(self): 
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59595410
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()
        self.fc.fd["devices_support_pc_mfe"].click_cannotconnectprinter_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Restart devices") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Restart your computer or mobile device, printer, and router to clear any error states.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Disconnect your computer or mobile device from the network name (SSID), and then reconnect it to the same network name your printer is connected to.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("If the printer is available and has a ready status, the issue is resolved. You do not need to continue troubleshooting.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Press the Power button to turn off the printer. If the printer does not turn off, disconnect the power cord from the printer and from the power source.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Turn off the computer or mobile device that the printer was set up with.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Restart the router.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Reconnect the power cord to the printer and to a wall outlet.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("NOTE : HP recommends plugging the printer directly into a wall outlet.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Turn on the computer or mobile device.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Check the connection to make sure the same network is used by the printer and the device.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Computer or mobile device: Open the list of available networks and make sure it is connected to the correct network.") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Printer: Check the Wireless light on the control panel. If it is solid blue the printer is connected.") == True

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C59595413")
    def test_14_hpx_rebranding_C59595413(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/59595413
        """
        self.fc.select_device()
        self.__click_start_virtual_assist_btn()
        self.fc.fd["devices_support_pc_mfe"].click_vashowmorepc_btn()
        self.driver.swipe(direction="down", distance=15)
        self.fc.fd["devices_support_pc_mfe"].click_otherspc_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Type a question below or choose a popular topic.") == True
        # assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Please select below what you need help with:") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("How can I assist you?") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message("PC") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Printer") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Instant Ink") == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_va_message_contains("Great deals from HP") == True

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

    def __select_device(self, maxmized=False):
        self.__start_HPX(maxmized=maxmized)
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index()

    def __click_start_virtual_assist_btn(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()             