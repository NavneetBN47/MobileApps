import pytest
from MobileApps.libs.ma_misc import conftest_misc as c_misc
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from time import sleep


pytest.app_info = "HPX"
class Test_Suite_17_Sanity_Printer_Settings_General(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        
        cls.printer_name=cls.p.get_printer_information()["model name"]


    @pytest.mark.smoke
    def test_01_verify_more_info_and_reports_screen_c53558260(self):
        """
        Verify "More information and reports" screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/53558260
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.add_a_printer(self.p)
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].verify_more_info_and_reports_info()
        self.fc.fd["devicesDetailsMFE"].click_more_info_and_reports_listitem()
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].verify_printer_info_simple_page()
        self.fc.fd["printersettings"].click_top_back_arrow()
        self.fc.fd["devicesDetailsMFE"].verify_more_info_and_reports_info()

    @pytest.mark.smoke
    def test_02_verify_printer_settings_screen_c53526321_c53558384(self):
        """
        Verify Printer Settings screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/53526321


        Verify "View all" navigation

        https://hp-testrail.external.hp.com/index.php?/cases/view/53558384
        """
        self.fc.fd["devicesDetailsMFE"].click_view_all_button() 
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].verify_status_tile()
        self.fc.fd["printersettings"].verify_information_tile()
        self.fc.fd["printersettings"].verify_settings_tile()
        self.fc.fd["printersettings"].verify_tools_tile()

    @pytest.mark.smoke
    def test_03_verify_printer_information_screen_c53568979(self):
        """
        Verify "Printer information" screen in instance 2

        https://hp-testrail.external.hp.com/index.php?/cases/view/53568979
        """
        self.fc.fd["printersettings"].select_printer_information()
        self.fc.fd["printersettings"].verify_printer_info_simple_page()

    @pytest.mark.smoke
    def test_04_verify_network_information_screen_c53567880(self):
        """
        Verify "Network information" screen

        https://hp-testrail.external.hp.com/index.php?/cases/view/53567880
        """
        self.fc.fd["printersettings"].select_network_information()
        self.fc.fd["printersettings"].verify_network_info_simple_page()

    ################################################################
    # One Simulator printer does not support EWS. So skip this case.
    ################################################################
    # @pytest.mark.smoke
    # def test_05_verify_print_quality_tools_screen_c53556506(self):
    #     """
    #     Verify "Print quality tools" screen.

    #     https://hp-testrail.external.hp.com/index.php?/cases/view/53556506
    #     """
    #     self.fc.fd["printersettings"].select_print_quality_tools()
    #     self.fc.fd["printersettings"].verify_print_quality_tools_page()

    # def test_06_verify_advanced_settings_screen_c57378024(self):
    #     """
    #     Verify "Advanced Settings" in the Printer settings flyout

    #     https://hp-testrail.external.hp.com/index.php?/cases/view/57378024
    #     """
    #     self.fc.fd["printersettings"].select_advanced_settings_item()
    #     if self.fc.fd["printersettings"].verify_continuing_to_your_printer_settings_dialog():
    #         self.fc.fd["printersettings"].click_the_pin_ok_btn()
    #     self.fc.fd["printersettings"].verify_ews_page()

    @pytest.mark.smoke
    def test_07_verify_supply_status_screen_c53526392(self):
        """
        Verify Supply Status screen under Printer settings

        https://hp-testrail.external.hp.com/index.php?/cases/view/53526392
        """
        self.fc.fd["printersettings"].click_top_back_arrow()
        self.fc.fd["devicesDetailsMFE"].win_scroll_element("device_details_page_device_name", direction="up", distance=20)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)

        self.fc.fd["devicesDetailsMFE"].click_supply_levels_link()
        if self.fc.fd["printersettings"].verify_supply_status_page(timeout=10):
            self.fc.fd["printersettings"].click_top_back_arrow()
        elif self.fc.fd["printersettings"].verify_lets_finish_setting_up_page(timeout=10):
            self.fc.fd["printersettings"].click_top_back_arrow()
        else:
            self.web_driver.add_window_and_switch("supply_levels")
            sleep(2)
            current_url = self.web_driver.get_current_url()
            assert "https://www.hp.com/" in current_url
            sleep(2)
            self.web_driver.set_size('min')

        self.driver.swipe(direction="up", distance=6)
        self.fc.fd["devicesDetailsMFE"].verify_printer_device_page(self.printer_name)