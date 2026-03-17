import pytest
import time
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx_rebranding.utility.registry_utilities import RegistryUtilities


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"


class Test_Suite_PC_Device_Functional_DisplayControl_Wellbeing(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)      
        cls.re = RegistryUtilities(cls.driver.ssh)    
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.launch_myHP()
            time.sleep(10)
            cls.fc.ota_app_after_update()
        else:
            time.sleep(5)
            cls.fc.launch_myHP()
        

    @pytest.mark.ota
    @pytest.mark.function
    def test_01_verify_wellbeing_card_on_pc_device_C42902494(self):
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_wellbeing_card_lone_page_show(), "wellbeing card is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_wellbeing_card()
        assert self.fc.fd["wellbeing"].verify_screen_time_title_show_up(), "Screen time title is not displayed"
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        time.sleep(5)
        self.fc.swipe_window(direction="down", distance=4)
        assert self.fc.fd["devices_details_pc_mfe"].verify_wellbeing_card_lone_page_show(), "wellbeing card is not displayed"
        self.fc.swipe_window(direction="up", distance=4)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_02_verify_display_control_card_on_pc_device_C42902487(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(), "Display control is not displayed"
        self.fc.fd["devices_details_pc_mfe"].click_display_control_lone_page()
        display_title = self.fc.fd["display_control"].verify_display_control_text_ltwo_page()
        assert display_title == "Display","Display Text is not matching."
        self.fc.fd["devicesMFE"].restore_app()
        time.sleep(2)
        self.fc.fd["devicesMFE"].maximize_the_hpx_window()
        time.sleep(2)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        self.fc.swipe_window(direction="down", distance=2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_display_control_lone_page(), "Display control is not displayed"
        self.fc.swipe_window(direction="up", distance=2)
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
    
    @pytest.mark.ota
    @pytest.mark.function
    def test_03_verify_system_module_name_C42902505(self):
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["devicesMFE"].click_back_button_rebranding()
        time.sleep(2)
        system_name = self.fc.get_windows_system_module_name()
        time.sleep(2)
        assert self.fc.fd["devices_details_pc_mfe"].verify_system_module_name() == system_name, "System module name is not matching"


    @pytest.mark.ota
    @pytest.mark.function
    def test_04_verify_production_number_C42902497(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(2)
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\HP\\CommonInfo"
        
        system_production_number = self.re.get_registry_value(registry_path, "ProductNumber")
        time.sleep(2)
        pc_production_number = self.fc.fd["devices_details_pc_mfe"].get_pc_device_production_number()
        time.sleep(2)
        assert pc_production_number in system_production_number["stdout"], "Production number is not matching"
    

    @pytest.mark.ota
    @pytest.mark.function
    def test_05_verify_serial_number_C42902498(self):
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_device_card()
        time.sleep(3)
        self.fc.swipe_window(direction="down", distance=20)
        time.sleep(2)
        registry_path = "HKEY_LOCAL_MACHINE\\SOFTWARE\\HP\\CommonInfo"
        
        system_serial_number = self.re.get_registry_value(registry_path, "SerialNumber")
        time.sleep(2)
        pc_serial_number = self.fc.fd["devices_details_pc_mfe"].get_pc_device_serial_number()
        time.sleep(2)
        assert pc_serial_number in system_serial_number["stdout"], "Serial number is not matching"