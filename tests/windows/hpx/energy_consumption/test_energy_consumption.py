import logging
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_energy_consumption(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            cls.fc.launch_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
        
    # Suite supposed to be run on Baymax, Longhornz and Ernesto 
    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_supported_platform_C42142055(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(5)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(5)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption()) is True, "Energy consumption module is  not visible"

    @pytest.mark.ota
    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_energy_consumption_invoking_C42142058(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(3)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
    
    def test_03_energy_consumption_consistency_C42142072(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(3)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        for _ in range(10):
            self.fc.restart_myHP()
            time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(3)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        for _ in range(10):
            self.fc.restart_myHP()
            time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(3)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        for _ in range(10):
            self.fc.restart_myHP()
            time.sleep(5)
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(3)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
    
    def test_04_version_on_app_ui_screen(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["energy_consumption"].verify_setting_module()
        self.fc.fd["energy_consumption"].click_setting_module()
        self.fc.fd["energy_consumption"].verify_about_button()
        self.fc.fd["energy_consumption"].click_about_button()
        assert bool(self.fc.fd["energy_consumption"].verify_app_version()) is True, "version doesnot show"
    
    def test_05_energy_consumption_enabling_the_fusion_C42142056(self):
        self.fc.stop_hpsysinfo_fusion_services()
        time.sleep(5)
        self.fc.start_hpsysinfo_fusion_services()
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        self.fc.fd["energy_consumption"].verify_energy_consumption()
        self.fc.fd["energy_consumption"].click_energy_consumption()
        time.sleep(3)
        assert bool(self.fc.fd["energy_consumption"].verify_energy_consumption_header()) is True, "Energy consumption header is  not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_data_consumption_header())is True, "Real date tme is  not visible"

    @pytest.mark.ota
    def test_06_energy_consumption_behaviour_disabling_stop_the_fusion_C42142057(self):
        self.fc.stop_hpsysinfo_fusion_services()
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        self.fc.fd["energy_consumption"].verify_energy_consumption() is False, "Energy consumption header is visible"
        self.fc.close_myHP()
        self.fc.start_hpsysinfo_fusion_services()
    
    def test_07_energy_consumption_card_more_helpful_links_42142070(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        self.fc.fd["energy_consumption"].click_energy_consumption()
        self.fc.swipe_window(direction="down", distance=6)
        assert bool(self.fc.fd["energy_consumption"].verify_product_carbon_footprint_link()) is True, "product carbon footprint link is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_energy_environment_link()) is True, "energy environment link is not visible"
        self.fc.fd["energy_consumption"].click_product_carbon_footprint_link_text()
        assert bool(self.fc.fd["energy_consumption"].verify_product_carbon_footprint_report_title()) is True, "product carbon footprint report title is not visible"
        #click app on task bar
        self.fc.fd["audio"].click_myhp_on_task_bar()
        self.fc.fd["energy_consumption"].click_energy_environment_link()
        assert bool(self.fc.fd["energy_consumption"].verify_epa_home_page_title()) is True, "epa home page title is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_energy_environment_report_title()) is True, "energy environment report title is not visible"
        #close browser
        self.fc.close_edge_browser()
    
    @pytest.mark.ota
    def test_08_consistency_check_for_dropdown_C42142060(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        self.fc.fd["energy_consumption"].click_energy_consumption()
        self.fc.fd["energy_consumption"].click_consumption_trend_dropdown()
        self.fc.fd["energy_consumption"].select_consumption_trend_6_days()
        assert bool(self.fc.fd["energy_consumption"].verify_power_consumption_measurement()) is True, "Power consumption measurement is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_data_consumption_header()) is True, "Data consumption header is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_consumption_trend_description()) is True, "Consumption trend description is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_daily_average_text()) is True, "Daily average text is not visible"
        self.fc.fd["energy_consumption"].click_consumption_trend_dropdown()
        self.fc.fd["energy_consumption"].select_consumption_trend_6_month()
        assert bool(self.fc.fd["energy_consumption"].verify_power_consumption_measurement()) is True, "Power consumption measurement is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_data_consumption_header()) is True, "Data consumption header is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_consumption_trend_description()) is True, "Consumption trend description is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_daily_average_text()) is True, "Daily average text is not visible"
        self.fc.fd["energy_consumption"].click_consumption_trend_dropdown()
        self.fc.fd["energy_consumption"].select_consumption_trend_12_hours()
        assert bool(self.fc.fd["energy_consumption"].verify_power_consumption_measurement()) is True, "Consumption graph is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_data_consumption_header()) is True, "Data consumption header is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_consumption_trend_description()) is True, "Consumption trend description is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_daily_average_text()) is True, "Daily average text is not visible"
    
    def test_9_consistency_check_for_dropdown_C42142066(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(3)
        self.fc.fd["energy_consumption"].click_energy_consumption()
        self.fc.fd["energy_consumption"].click_consumption_trend_dropdown()
        self.fc.fd["energy_consumption"].select_consumption_trend_6_days()
        assert bool(self.fc.fd["energy_consumption"].verify_power_consumption_measurement()) is True, "Power consumption measurement is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_data_consumption_header()) is True, "Data consumption header is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_consumption_trend_description()) is True, "Consumption trend description is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_daily_average_text()) is True, "Daily average text is not visible"
        self.fc.fd["energy_consumption"].click_consumption_trend_dropdown()
        self.fc.fd["energy_consumption"].select_consumption_trend_6_month()
        assert bool(self.fc.fd["energy_consumption"].verify_power_consumption_measurement()) is True, "Power consumption measurement is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_data_consumption_header()) is True, "Data consumption header is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_consumption_trend_description()) is True, "Consumption trend description is not visible"
        assert bool(self.fc.fd["energy_consumption"].verify_daily_average_text()) is True, "Daily average text is not visible"
