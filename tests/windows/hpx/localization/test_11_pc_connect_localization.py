import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
from MobileApps.libs.ma_misc import conftest_misc

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

#Commenting these lines as 5G is only supporting en-US, could be use in future when 5G expanded to other region
# language_list_path = ma_misc.get_abs_path("resources/test_data/hpx/locale/language_list.txt")
# with open(language_list_path, "r+") as f:
#     languages = f.read().split(',')
languages=['en-US']    

@pytest.fixture(params=languages)
def language(request):
    return request.param

@pytest.fixture(scope="session", params=["pc_connect_screenshot"])
def screenshot_folder_name(request):
    return request.param


class Test_Suite_PC_Connect_Localization(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()
        cls.attachment_path = conftest_misc.get_attachment_folder()
        
    def test_01_pc_connect_module_C33045055(self,language, publish_hpx_localization_screenshot, screenshot_folder_name):
        self.fc.update_properties(language)
        self.fc.close_myHP()
        self.fc.launch_myHP()  
        time.sleep(6)
        if bool (self.fc.fd["hp_registration"].verify_registration_page_is_display()):
            self.driver.swipe(direction="down", distance=3)
            if self.fc.fd["hp_registration"].verify_skip_button_show():
                self.fc.fd["hp_registration"].click_skip_button()
            else:
                logging.info("skip button not available")
        else:
            logging.info("registration page not displayed")
        if bool (self.fc.fd["dropbox"].verify_dropbox_header_show()):
            self.fc.fd["dropbox"].click_skip_button() 
        else:
            logging.info("Dropbox page not displayed")  
        langSettings = ma_misc.load_json_file("resources/test_data/hpx/pc_connect_localization.json")[language]["translation"]["pCConnect"]    
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            time.sleep(5)
            self.fc.fd["devices"].maximize_app()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        pc_Device_Menu_text = self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        self.fc.fd["navigation_panel"].click_PC_device_menu()

        assert bool(self.fc.fd["pc_connect"].verify_5G_module_on_pcdevice_page()) is True, "5G card is not available"
        logging.info("5G card available")
        self.fc.fd["pc_connect"].click_5G_module_on_pcdevice_page()  
        #5G header
        five_g_header = self.fc.fd["pc_connect"].verify_5G_header()
        ma_misc.create_localization_screenshot_folder("pc_connect_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_connect_screenshot/{}_pc_connect01.png".format(language))
        assert five_g_header==langSettings["moduleTitle"],"5G is not visible at header title - {}".format(five_g_header)
        #5G Connectivity
        actual_5G_connectivity_text = self.fc.fd["pc_connect"].verify_5G_connectivity_text()
        assert actual_5G_connectivity_text == langSettings["5gConnectivity"], "5G Connectivity is not visible at 5G connectivity page - {}".format(actual_5G_connectivity_text)
        #eSim
        esim_text = self.fc.fd["pc_connect"].verify_esim_text()
        assert esim_text==langSettings["eSIM"],"eSIM is not visible at 5G connectivity page - {}".format(esim_text)
        #T=Mobile
        tmobile_text = self.fc.fd["pc_connect"].verify_tmobile_text()
        assert tmobile_text==langSettings["tmobile"],"T-Mobile is not visible at 5G connectivity page - {}".format(tmobile_text)
        #Sim Number
        sim_number_text = self.fc.fd["pc_connect"].verify_sim_number_text().replace(":","")
        assert sim_number_text==langSettings["simNumber"],"Sim Number is not visible at 5G connectivity page - {}".format(sim_number_text)
        #Usage Data
        usage_data_text = self.fc.fd["pc_connect"].verify_usage_data_text().replace(":","")
        assert usage_data_text==langSettings["usageData"],"Usage Data is not visible at 5G connectivity page - {}".format(usage_data_text)
        #Usage Data Tool tip
        self.fc.fd["pc_connect"].click_usage_data()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_connect_screenshot/{}_pc_connect_data_tooltips.png".format(language))
        assert self.fc.fd["pc_connect"].click_usage_data()==True,"Usage data tooltip text is not matching"
        #Usage Data Description
        usage_data_description = self.fc.fd["pc_connect"].verify_usage_datain_last_30_days_text()
        assert langSettings["inLast30days"] in usage_data_description,"inLast30days is not visible at 5G connectivity page - {}".format(usage_data_description)
        #Coverage Map
        coverage_map_text = self.fc.fd["pc_connect"].verify_coverage_map_text()
        assert coverage_map_text==langSettings["coverageMap"],"Usage Data is not visible at 5G connectivity page - {}".format(coverage_map_text)
        #Coverage Map Tool Tip
        self.fc.fd["pc_connect"].click_coverage_map()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_connect_screenshot/{}_pc_connect_coverage_coverage_tooltips.png".format(language))
        assert self.fc.fd["pc_connect"].click_coverage_map()==True,"coverage tooltip text is not matching"
        #Network & Internet settings
        self.driver.swipe(direction="down", distance=3)
        network_and_internet_settings_text = self.fc.fd["pc_connect"].verify_network_and_internet_settings_text()
        assert network_and_internet_settings_text==langSettings["networkAndInternetSettings"],"Network & Internet settings is not visible at 5G connectivity page - {}".format(network_and_internet_settings_text)
        #Connection pop-up
        self.driver.swipe(direction="up", distance=3)
        if self.fc.fd["pc_connect"].get_toggle_notification_state()=="0":
            logging.info("5G Toggle State {}".format(self.fc.fd["pc_connect"].get_toggle_notification_state()))           
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
        else:
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
            logging.info("5G Toggle State {}".format(self.fc.fd["pc_connect"].get_toggle_notification_state()))
        time.sleep(3)
        five_g_connectivity_text = self.fc.fd["pc_connect"].verify_5g_network_connection_alert()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_connect_screenshot/{}_pc_connect_coverage_connection.png".format(language))
        assert langSettings["toast"]["connectedTitle"] in five_g_connectivity_text,"Connection Pop up is not visible at 5G connectivity page - {}".format(five_g_connectivity_text)
        #Disconnection popup
        if self.fc.fd["pc_connect"].get_toggle_notification_state()=="1":
            logging.info("5G Toggle State {}".format(self.fc.fd["pc_connect"].get_toggle_notification_state()))           
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
        else:
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()
            logging.info("5G Toggle State {}".format(self.fc.fd["pc_connect"].get_toggle_notification_state())) 
        time.sleep(2)
        five_g_disconnectivity_text = self.fc.fd["pc_connect"].verify_5g_network_disconnected_alert()
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "pc_connect_screenshot/{}_pc_connect_coverage_disconnection.png".format(language))
        assert langSettings["toast"]["disconnectedTitle"] in five_g_disconnectivity_text,"Disconnection Pop up is not visible at 5G connectivity page - {}".format(five_g_disconnectivity_text)

        self.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        self.driver.ssh.remove_file_with_suffix(self.remote_artifact_path, ".json")
        self.fc.close_myHP()