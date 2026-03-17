import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_01_Printer_Status_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()['serial number']
        cls.trigger_status = {'status': False}

    
    @pytest.mark.regression
    def test_01_verify_ps_ready_screen_c52826670_c52826671(self):
        """
        Make sure printer is idle, go to Printer Status, verify Ready status shows

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826670

        Printer Status (Ready) UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826671
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button() 
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].select_printer_status_item()
        if self.fc.fd["printer_status"].verify_ps_ready_screen(raise_e=False) is False:
            pytest.skip("Skip this test as the printer status is not Ready")
    ##############################################################
    #    One simulator printer can't trigger offline status      #
    ##############################################################    
    # Can't turn off the printer in the lab environment for the one simulator printer, so skip this case temporarily.
    # @pytest.mark.regression
    # def test_02_verify_ps_offline_screen_c52826672_c52826673(self):
    #     """
    #     Turn off printer, go to Printer Status, verify Printer Offline status shows

    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52826672

    #     Printer Status (Offline) UI

    #     https://hp-testrail.external.hp.com/index.php?/cases/view/52826673
    #     """
    #     self.fc.fd["printersettings"].select_printer_information()
    #     self.fc.trigger_printer_offline_status(self.p)
    #     self.fc.fd["printersettings"].select_printer_status_item()
    #     self.fc.fd["printer_status"].verify_ps_offline_screen()
    #     self.fc.restore_printer_online_status(self.p)

    @pytest.mark.regression
    def test_03_click_back_arrow_c52826674(self):
        """
        Click back arrow on title bar on Printer Status screen at any point of time, verify main UI shows

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826674
        """
        self.fc.fd["printersettings"].click_top_back_arrow()
        self.fc.fd["devicesDetailsMFE"].click_view_all_button() 
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].select_printer_status_item()

    @pytest.mark.regression
    def test_04_trigger_printer_status_c52826694(self):
        """
        Trigger the IORef in printer status screen
        Check Supported message button, verify "Estimated Supplies Levels" button is removed from the all messages

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826694
        """
        status = ['65536', '65548', '65550']
        self.fc.fd["printersettings"].select_printer_information()
        self.fc.fd["printer_status"].enable_printer_status(self.serial_number, status)
        self.fc.fd["printersettings"].select_printer_status_item()
        sleep(2)
        self.fc.fd["printer_status"].verify_ps_ioref_list()
        self.trigger_status['status'] = True

    @pytest.mark.regression
    def test_05_verify_error_condition_ui_c52826675_c52826676(self):
        """
        Generate an (Error) printer condition, verify correct message shows in Printer Status

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826675

        Printer Status (Error) UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826676
        """
        self.__verify_printer_status(ioref='65536')

    @pytest.mark.regression
    def test_06_verify_warning_condition_ui_c52826679_c52826680(self):
        """
        Generate a (Warning) printer condition, verify correct message shows in Printer Status

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826679

        Printer Status (Warning) UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826680
        """
        self.__verify_printer_status(ioref='65548')

    @pytest.mark.regression
    def test_07_verify_info_condition_ui_c52826683_c52826684(self):
        """
        Generate an (Info) printer condition, verify correct message shows in Printer Status

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826683

        Printer Status (Info) UI

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826684
        """
        self.__verify_printer_status(ioref='65550')

    def __verify_printer_status(self, ioref):
        if self.trigger_status['status']:
            self.fc.fd["printer_status"].click_ps_ioref_item(ioref)
            self.fc.fd["printer_status"].verify_ps_content(ioref, [ioref])
