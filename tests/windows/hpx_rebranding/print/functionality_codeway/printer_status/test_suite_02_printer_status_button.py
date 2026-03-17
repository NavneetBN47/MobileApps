import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_02_Printer_Status_Button(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.printer_feature = {'II': None}
        cls.printer_name = cls.p.get_printer_information()["model name"]
        cls.serial_number = cls.p.get_printer_information()['serial number']


    @pytest.mark.regression
    def test_01_add_printer_and_enable_printer_status(self):
        """
        Add a printer 
        enable the IORefs
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.__go_to_printer_status_screen()
        self.fc.fd["printersettings"].select_printer_information()
        self.fc.fd["printer_status"].enable_printer_status(self.serial_number, ['65537', '65538', '65557','65579', '65790', '65553'])
        self.fc.fd["printersettings"].select_printer_status_item()
        sleep(2)
        self.fc.fd["printer_status"].verify_ps_ioref_list()

    @pytest.mark.regression
    def test_02_check_get_more_help_webpage_url_c52826690(self):
        """
        (+) Click on "Get more help" link on a printer status message, verify SFS url

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826690
        """
        self.fc.fd["printer_status"].click_ps_ioref_item('65579')
        self.fc.fd["printer_status"].click_ps_body_btn('Get More Help')
        self.web_driver.add_window_and_switch("get_more_help")
        sleep(2)
        current_url = self.web_driver.get_current_url()
        assert "https://support.hp.com/us-en" in current_url
        sleep(2)

    @pytest.mark.regression
    def test_03_check_get_more_help_webpage_chatbot_c52826691(self):
        """
        (+) Click on "Get more help" link on a printer status message, verify Chatbot url

        https://hp-testrail.external.hp.com/index.php?/cases/view/52826691
        """
        self.fc.fd["printer_status"].click_webpage_dialog_close_btn()
        self.fc.fd["printer_status"].verify_webpage_chatbot()
        sleep(2)
        
    @pytest.mark.regression
    def test_04_go_to_printer_status_screen(self):
        """
        Go to Printer device screen
        Trigger the IORef in printer status screen
        65537: Cartridges Missing
        65538: Cartridge Failure
        65557: Cartridges Low
        65790: Replace Cartridge Now
        65553: Single Cartridge Mode
        """
        self.web_driver.set_size('min')
        if self.driver.session_data['request'].config.getoption("--stack") in ["rebrand_pie", "rebrand_stage", "rebrand_production"]:
            self.fc.fd["printersettings"].select_supply_status_option()
            if self.fc.fd["printersettings"].verify_supply_status_page(timeout=10):
                self.fc.fd["printersettings"].click_top_back_arrow()
                self.printer_feature['II'] = True
            elif self.fc.fd["printersettings"].verify_lets_finish_setting_up_page(timeout=10):
                self.fc.fd["printersettings"].click_top_back_arrow()
                self.printer_feature['II'] = None
            else:
                self.printer_feature['II'] = False
                self.web_driver.add_window_and_switch("supply_levels")
                sleep(2)
                current_url = self.web_driver.get_current_url()
                assert "https://www.hp.com/" in current_url
                sleep(2)
                self.web_driver.set_size('min')

            self.fc.fd["devicesDetailsMFE"].verify_view_all_button()
        else:
            pytest.skip("Beta 1 has no this feature")
        
    @pytest.mark.parametrize("ioref", ['65537', '65538', '65557', '65790', '65553'])
    @pytest.mark.regression
    def test_05_check_get_supplies_button_with_II_printer_c52826695_c52826689(self, ioref):
        """
        Click "Get Supplies" button on the supported printer status message (II eligible), verify DSP page opens within the Gotham app
        
        Test Steps:
        Check all the supplies related messages for "Get Supplies" button
        Click on the "Get Supplies" button

        Expected Result:
        Verify DSP screen should launch within the Gotham app
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/52826695

        Click back arrow on Supply Status screen, verify Main UI show
        
        Test Steps:
        Generate a supported status with Estimated Supplies levels button.
        Click "Get Supplies" on the status message
        Click back arrow on the Supply Status screen.
        
        Expected Result:
        - Verify PDP screen shows after clicking the back arrow.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/52826689
        """
        if self.printer_feature['II'] is False:
            pytest.skip("Printer is not II eligible, skipping test")
        self.__go_to_printer_status_screen()
        self.fc.fd["printer_status"].click_ps_ioref_item(ioref)
        if self.driver.session_data['request'].config.getoption("--stack") in ["rebrand_pie", "rebrand_stage", "rebrand_production"]:
            self.fc.fd["printer_status"].click_ps_body_btn('Get Supplies')
            self.fc.fd["printersettings"].verify_supply_status_page(timeout=10)
            self.fc.fd["printersettings"].click_top_back_arrow()
            self.fc.fd["devicesDetailsMFE"].verify_view_all_button()
        else:
            pytest.skip("Beta 1 has no this feature")
        
    @pytest.mark.parametrize("ioref", ['65537', '65538', '65557', '65790', '65553'])
    @pytest.mark.regression
    def test_06_check_get_supplies_button_with_non_II_printer_c52826696(self, ioref):
        """
        Click "Get Supplies" button on the supported printer status message (non-II eligible), verify legacy supply status shows
        
        Test Steps:
        Click on the "Get Supplies" button
        
        Expected Result:
        Verify legacy supply status screen shows.
        
        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/52826696
        """
        if self.printer_feature['II'] is True:
            pytest.skip("Printer is not non-II eligible, skipping test")
        self.__go_to_printer_status_screen()
        self.fc.fd["printer_status"].click_ps_ioref_item(ioref)
        if self.driver.session_data['request'].config.getoption("--stack") in ["rebrand_pie", "rebrand_stage", "rebrand_production"]:
            self.fc.fd["printer_status"].click_ps_body_btn('Get Supplies')
            self.web_driver.add_window_and_switch("supply_levels")
            sleep(2)
            current_url = self.web_driver.get_current_url()
            assert "https://www.hp.com/" in current_url
            sleep(2)
            self.web_driver.set_size('min')
            self.fc.fd["devicesDetailsMFE"].verify_view_all_button()
        else:
            pytest.skip("Beta 1 has no this feature")

    def __go_to_printer_status_screen(self):
        self.web_driver.set_size('min')
        if self.fc.fd["devicesDetailsMFE"].verify_view_all_button(raise_e=False) is False:
            self.fc.fd["printersettings"].click_top_back_arrow()
        self.web_driver.set_size('min')
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].select_printer_status_item()
        