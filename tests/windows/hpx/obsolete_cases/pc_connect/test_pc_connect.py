from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_PC_Connect(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()

        
    def navigate_to_5g_module(self):
        self.driver.swipe(direction="down", distance=3) 
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        assert bool(self.fc.fd["navigation_panel"].verify_PC_device_menu(state)) is True
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        pcconnect_module = self.fc.fd["pc_connect"].verify_5G_module_on_pcdevice_page()
        assert pcconnect_module=="5G Action Item","5G is not visible at PC Device Page - {}".format(pcconnect_module)
        self.fc.fd["pc_connect"].click_5G_module_on_pcdevice_page() 

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_platform(["grogu"])
    def test_01_verify_all_the_components_on_5G_connectivity_page_C33697220(self):
        self.navigate_to_5g_module()
        five_g_header = self.fc.fd["pc_connect"].verify_5G_header()
        assert five_g_header=="5G","5G is not visible at header title - {}".format(five_g_header)

        five_g_connectivity_text = self.fc.fd["pc_connect"].verify_5G_connectivity_text()
        assert five_g_connectivity_text=="5G Connectivity","5G is not visible at header title -{}".format(five_g_connectivity_text)

        esim_text = self.fc.fd["pc_connect"].verify_esim_text()
        assert esim_text=="eSIM","eSIM is not visible at 5G connectivity page - {}".format(esim_text)

        tmobile_text = self.fc.fd["pc_connect"].verify_tmobile_text()
        assert tmobile_text=="T-Mobile","T-Mobile is not visible at 5G connectivity page - {}".format(tmobile_text)
        
        sim_number_text = self.fc.fd["pc_connect"].verify_sim_number_text()
        assert sim_number_text=="Sim Number:","Sim Number is not visible at 5G connectivity page - {}".format(sim_number_text)

        usage_data_text = self.fc.fd["pc_connect"].verify_usage_data_text()
        assert usage_data_text=="Usage data:","Usage Data is not visible at 5G connectivity page - {}".format(usage_data_text)
        self.fc.fd["pc_connect"].click_usage_data()
        assert self.fc.fd["pc_connect"].click_usage_data()==True,"Usage data tooltip text is not matching"

        usage_data_description = self.fc.fd["pc_connect"].verify_usage_datain_last_30_days_text()
        assert "last 30 days" in usage_data_description,"inLast30days is not visible at 5G connectivity page - {}".format(usage_data_description)
       
        coverage_map_text = self.fc.fd["pc_connect"].verify_coverage_map_text()
        assert coverage_map_text=="Coverage Map","Usage Data is not visible at 5G connectivity page - {}".format(coverage_map_text)
        self.fc.fd["pc_connect"].click_coverage_map()
        assert self.fc.fd["pc_connect"].click_coverage_map()==True,"coverage tooltip text is not matching"

        self.driver.swipe(direction="down", distance=3)
        network_and_internet_settings_text = self.fc.fd["pc_connect"].verify_network_and_internet_settings_text()
        assert network_and_internet_settings_text=="Network & Internet settings","Network & Internet settings is not visible at 5G connectivity page - {}".format(network_and_internet_settings_text)


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_platform(["grogu"])
    def test_02_turn_on_the_toggle_of_five_g_connectivity_to_check_the_fiveg_connectivity_C31866512(self):  
        self.navigate_to_5g_module()
        if self.fc.fd["pc_connect"].get_toggle_notification_state()=="0":
            logging.info("5G Toggle State {}".format(self.fc.fd["pc_connect"].get_toggle_notification_state()))           
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
        else:
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
            logging.info("5G Toggle State {}".format(self.fc.fd["pc_connect"].get_toggle_notification_state()))
        five_g_connectivity_text = self.fc.fd["pc_connect"].verify_5g_network_connection_alert()
        time.sleep(3)
        assert "5G connection established" in five_g_connectivity_text,"5G connection established pop up not visible - {}".format(five_g_connectivity_text)

    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_platform(["grogu"])
    def test_03_turn_off_the_toggle_of_five_g_connectivity_to_check_the_fiveg_connectivity_C31866574(self):
        self.navigate_to_5g_module()
        if self.fc.fd["pc_connect"].get_toggle_notification_state()=="1":
            logging.info("5G Toggle State {}".format(self.fc.fd["pc_connect"].get_toggle_notification_state()))           
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
        else:
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
            logging.info("5G Toggle State {}".format(self.fc.fd["pc_connect"].get_toggle_notification_state())) 
        five_g_disconnectivity_text = self.fc.fd["pc_connect"].verify_5g_network_disconnected_alert()
        time.sleep(3)
        assert "5G connection disconnected" in five_g_disconnectivity_text,"Disconnection Pop up is not visible at 5G connectivity page - {}".format(five_g_disconnectivity_text)

    @pytest.mark.require_platform(["grogu"])
    def test_04_click_the_network_and_Internet_settings_link_verify_it_opens_system_internet_setting_C32172955(self):
        self.navigate_to_5g_module()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["pc_connect"].click_network_and_internet_settings()
        network_and_internet_system_settings_text = self.fc.fd["pc_connect"].verify_system_network_and_internet_page()
        assert network_and_internet_system_settings_text=="Network & internet","Network & Internet settings is not visible at 5G connectivity page - {}".format(network_and_internet_system_settings_text)
        self.fc.fd["pc_connect"].click_system_close_button()

    @pytest.mark.require_platform(["grogu"])
    def test_05_turn_on_the_toggle_of_cellular_from_network_and_internet_check_the_fiveg_connectivity_page_C33139089(self):
        self.navigate_to_5g_module()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["pc_connect"].click_network_and_internet_settings()
        self.fc.fd["pc_connect"].verify_system_network_and_internet_page()
        self.fc.fd["pc_connect"].verify_cellular_text()
        if self.fc.fd["pc_connect"].system_cellular_network_toggle_state()=="0":
            logging.info("Cellular Toggle State {}".format(self.fc.fd["pc_connect"].system_cellular_network_toggle_state()))           
            self.fc.fd["pc_connect"].click_system_cellular_network_toggle()
        else:
            self.fc.fd["pc_connect"].click_system_cellular_network_toggle()
            self.fc.fd["pc_connect"].click_system_cellular_network_toggle()
        logging.info("Cellular Toggle State is On - {}".format(self.fc.fd["pc_connect"].system_cellular_network_toggle_state()))    
        self.fc.fd["pc_connect"].click_system_close_button()

    @pytest.mark.require_platform(["grogu"])
    def test_06_turn_off_the_toggle_of_cellular_from_network_and_internet_check_the_fiveg_connectivity_page_C33139090(self):
        self.navigate_to_5g_module()
        self.driver.swipe(direction="down", distance=3)
        self.fc.fd["pc_connect"].click_network_and_internet_settings()
        self.fc.fd["pc_connect"].verify_system_network_and_internet_page()
        self.fc.fd["pc_connect"].verify_cellular_text()
        if self.fc.fd["pc_connect"].system_cellular_network_toggle_state()=="1":
            logging.info("Cellular Toggle State {}".format(self.fc.fd["pc_connect"].system_cellular_network_toggle_state()))           
            self.fc.fd["pc_connect"].click_system_cellular_network_toggle()
        else:
            self.fc.fd["pc_connect"].click_system_cellular_network_toggle()
            self.fc.fd["pc_connect"].click_system_cellular_network_toggle()  
        logging.info("Cellular Toggle State is Off - {}".format(self.fc.fd["pc_connect"].system_cellular_network_toggle_state()))
        self.fc.fd["pc_connect"].click_system_close_button()  
        self.fc.close_myHP()
