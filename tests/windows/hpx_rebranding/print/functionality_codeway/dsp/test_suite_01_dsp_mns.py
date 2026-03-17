import pytest
from time import sleep
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "HPX"
class Test_Suite_01_Dsp_Mns(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()['serial number']

        
    @pytest.mark.regression
    def test_01_add_a_printer(self):
        """
        Add a printer to carousel.
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

    @pytest.mark.regression
    def test_02_check_click_ink_level_icon_log_c60641885(self):
        """
        (+) Click Ink level icon on the main UI, verify correct jump id show in the log

        https://hp-testrail.external.hp.com/index.php?/cases/view/60641885
        """
        self.fc.fd["devicesDetailsMFE"].click_supply_levels_link()
        if self.fc.fd["printersettings"].verify_supply_status_page(timeout=10) or self.fc.fd["printersettings"].verify_lets_finish_setting_up_page(timeout=10):
            self.fc.fd["printersettings"].click_top_back_arrow()
        else:
            self.web_driver.add_window_and_switch("supply_levels")
            sleep(2)
            current_url = self.web_driver.get_current_url()
            assert "https://www.hp.com/" in current_url
            sleep(2)
            self.web_driver.set_size('min')

        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()

        check_event = 'in_r11549_ii2_winhpx_dspsupplystatus_10012024'
        self.fc.fd["hpx_rebranding_common"].check_log_event(check_event)

    @pytest.mark.regression
    def test_03_check_click_get_supplies_btn_log_c60641888(self):
        """
        (+) Click "Get Supplies" button on an applicable message under the Printer Status, verify correct jump id show on the log

        https://hp-testrail.external.hp.com/index.php?/cases/view/60641888
        """
        self.fc.fd["printersettings"].select_printer_status_item()
        self.fc.fd["printersettings"].select_printer_information()
        self.fc.fd["printer_status"].enable_printer_status(self.serial_number, ['65537'])
        self.fc.fd["printersettings"].select_printer_status_item()
        sleep(2)
        self.fc.fd["printer_status"].verify_ps_ioref_list()
        self.fc.fd["printer_status"].click_ps_body_btn('Get Supplies')
        if self.fc.fd["printersettings"].verify_supply_status_page(timeout=10) or self.fc.fd["printersettings"].verify_lets_finish_setting_up_page(timeout=10):
            self.fc.fd["printersettings"].click_top_back_arrow()
        else:
            self.web_driver.add_window_and_switch("supply_levels")
            sleep(2)
            current_url = self.web_driver.get_current_url()
            assert "https://www.hp.com/" in current_url
            sleep(2)
            self.web_driver.set_size('min')

        check_event = 'in_r11549_ii2_winhpx_dspprinterstatus_10012024'        
        self.fc.fd["hpx_rebranding_common"].check_log_event(check_event)

    ##############################################################
    #    One simulator printer can't trigger offline status      #
    ##############################################################
    # @pytest.mark.regression
    # def test_04_check_supply_status_with_printer_offline_c60641949(self):
    #     """
    #     *(+) Go to Supply Status (printer offline), verify P2 page shows

    #     https://hp-testrail.external.hp.com/index.php?/cases/view/60641949
    #     """
    #     self.fc.trigger_printer_offline_status(self.p)
    #     sleep(5)
    #     self.fc.fd["devicesDetailsMFE"].click_view_all_button(send_key=True)
    #     self.fc.fd["printersettings"].verify_progress_bar()
    #     if self.driver.session_data['request'].config.getoption("--stack") in ["rebrand_pie"]:
    #         self.fc.fd["printersettings"].select_supply_status_option()
    #         if self.fc.fd["printersettings"].verify_supply_status_page(timeout=10) is False and self.fc.fd["printersettings"].verify_lets_finish_setting_up_page(timeout=3) is False:
    #             self.web_driver.add_window_and_switch("supply_levels")
    #             sleep(2)
    #             current_url = self.web_driver.get_current_url()
    #             assert "https://www.hp.com/" in current_url
    #             sleep(2)
    #             self.web_driver.set_size('min')
    #     else:
    #         pytest.skip("Beta 1 has no this feature")

    # @pytest.mark.regression
    # def test_05_restore_printer_online(self):
    #     """
    #     Connect network to printer.
    #     """
    #     self.fc.restore_printer_online_status(self.p)