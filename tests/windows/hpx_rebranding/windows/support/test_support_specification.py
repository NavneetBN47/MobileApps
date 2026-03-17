from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
# from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.powershell_wmi_utilities import PowershellWmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.ma_misc import ma_misc
from datetime import datetime
import MobileApps.resources.const.windows.const as w_const
import pytest
import time
import re
# import wmi

pytest.app_info = "HPX"
class Test_Suite_Specification(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = PowershellWmiUtilities(cls.driver.ssh)

        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.task_util = TaskUtilities(cls.driver.ssh)
        cls.registry = RegistryUtilities(cls.driver.ssh)

        cls.stack = request.config.getoption("--stack")
        cls.__first_start_HPX(cls)

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.initial_environment()
        self.fc.ensure_web_password_credentials_cleared()

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C62718183")
    def test_01_hpx_rebranding_C62718183(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62718183
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        caption, architecture = self.wmi.get_os_caption_and_architecture()
        if caption:
            caption = caption.replace("Microsoft", "").strip()
        build_number = self.__get_build_number()
        ubr = self.__get_ubr()
        self.__click_maximize_btn()
        print (f"Caption: {caption}, Architecture: {architecture}, BuildNumber: {build_number}, UBR: {ubr}")
        operatingsystem_info = self.fc.fd["devices_support_pc_mfe"].get_operatingsystem_info()
        assert caption in operatingsystem_info
        assert architecture in operatingsystem_info
        assert build_number in operatingsystem_info
        assert ubr in operatingsystem_info

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C62719642")
    def test_02_hpx_rebranding_C62719642(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62719642
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        cpu_name = self.wmi.get_processor_name()
        self.__click_maximize_btn()
        assert cpu_name in self.fc.fd["devices_support_pc_mfe"].get_microprocessor_info()

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C62719671")
    def test_03_hpx_rebranding_C62719671(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62719671
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        self.__click_maximize_btn()
        ram_info = self.wmi.get_physical_memory_info()
        total_capacity_gb = 0
        index = 1
        for module in ram_info:
            capacity_bytes = int(module.get('Capacity', 0))
            capacity_gb = capacity_bytes // (1024 ** 3)
            total_capacity_gb += capacity_gb
            manufacturer = module.get('Manufacturer')
            clock_speed = module.get('ConfiguredClockSpeed')
            memoryslot_info = self.fc.fd["devices_support_pc_mfe"].get_memoryslot_info(index)
            assert f'{capacity_gb}' in memoryslot_info
            assert manufacturer in memoryslot_info
            print(f"Capacity: {capacity_gb} GB, Manufacturer: {manufacturer}, ConfiguredClockSpeed: {clock_speed}")
            index += 1
        print(f"System memory = {total_capacity_gb} GB")
        systemmemory_info = self.fc.fd["devices_support_pc_mfe"].get_systemmemory_info()
        assert f'{total_capacity_gb} GB' in systemmemory_info

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C62719673")
    def test_04_hpx_rebranding_C62719673(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62719673
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        self.__click_maximize_btn()
        product, version = self.wmi.get_baseboard_product_and_version()
        print(f"BaseBoard Product: {product}, Version: {version}")
        systemboard_info = self.fc.fd["devices_support_pc_mfe"].get_systemboard_info()
        assert product in systemboard_info
        assert version in systemboard_info

    @pytest.mark.require_stack(["dev", "itg", "production"])     
    @pytest.mark.testrail("S57581.C62720705")
    def test_05_hpx_rebranding_C62720705(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62720705
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        self.__click_maximize_btn()
        smbios_version = self.wmi.get_smbios_bios_version()
        print(f"SMBIOS BIOS Version: {smbios_version}")
        systembios_info = self.fc.fd["devices_support_pc_mfe"].get_systembios_info()
        assert smbios_version in systembios_info

    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C62722053")
    def test_06_hpx_rebranding_C62722053(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62722053
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        self.__click_maximize_btn()
        video_info = self.wmi.get_video_controller_info()
        index = 0
        for controller in video_info:
            caption = controller.get('Caption')
            hres = controller.get('CurrentHorizontalResolution')
            vres = controller.get('CurrentVerticalResolution')
            refresh = controller.get('CurrentRefreshRate')
            driver_date = self.__parse_driver_date(controller.get('DriverDate'))
            driver_version = controller.get('DriverVersion')
            print(f"Caption: {caption},\n "
                  f"CurrentHorizontalResolution: {hres}, \n"
                  f"CurrentVerticalResolution: {vres}, \n"
                  f"CurrentRefreshRate: {refresh}, \n"
                  f"DriverDate: {driver_date}, \n"
                  f"DriverVersion: {driver_version}")
            index += 1
            video_info = self.fc.fd["devices_support_pc_mfe"].get_video_device_info(index)
            video_resolution = self.fc.fd["devices_support_pc_mfe"].get_video_device_resolution_info(index)
            video_refresh = self.fc.fd["devices_support_pc_mfe"].get_video_device_refresh_rate_info(index)
            video_version = self.fc.fd["devices_support_pc_mfe"].get_video_device_version_info(index)
            assert caption in video_info
            assert f"{hres} x {vres}" in video_resolution
            assert driver_version in video_version
            assert str(refresh) in video_refresh
            
    @pytest.mark.require_stack(["dev", "itg", "production"])    
    @pytest.mark.testrail("S57581.C62723195")
    def test_07_hpx_rebranding_C62723195(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/62723195
        """
        self.fc.select_device()
        self.fc.fd["devices_support_pc_mfe"].click_product_info_btn()
        self.__click_maximize_btn()
        sound_info = self.wmi.get_sound_device_and_driver_info()
        index = 0
        for dev in sound_info:
            product_name = dev.get('ProductName')
            driver_name = dev.get('DriverName')
            driver_version = dev.get('DriverVersion')
            print(f"ProductName: {product_name}, DriverName: {driver_name}, DriverVersion: {driver_version}")
            index += 1
            audio_info = self.fc.fd["devices_support_pc_mfe"].get_audio_device_info(index)
            audio_driver = self.fc.fd["devices_support_pc_mfe"].get_audio_device_driver_info(index)
            audio_version = self.fc.fd["devices_support_pc_mfe"].get_audio_device_version_info(index)
            assert self.__normalize_audio_name(product_name) in self.__normalize_audio_name(audio_info)
            assert driver_version in audio_version
            assert driver_name in audio_driver
       
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

    def __sign_in_HPX(self, sign_in_from_profile=False):
         self.fc.sign_in("shhpxtest005@outlook.com", "hpsa@rocks_335", self.web_driver, sign_in_from_profile=sign_in_from_profile)        

    def __get_build_number(self):
        reg_output = self.registry.get_registry_value(
            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion",
            "CurrentBuildNumber"
        )
        match = re.search("CurrentBuildNumber\s+REG_SZ\s+(\d+)", str(reg_output))
        if match:
            return match.group(1)
        return None
    
    def __get_ubr(self):
        reg_output = self.registry.get_registry_value(
            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion",
            "UBR"
        )
        # reg_output is a dict, get the 'stdout' string
        stdout = reg_output.get('stdout', '')
        # Match hex or decimal number after REG_DWORD
        match = re.search(r'UBR\s+REG_DWORD\s+(0x[0-9a-fA-F]+|\d+)', stdout)
        if match:
            value_str = match.group(1)
            # Convert hex string to int if needed
            if value_str.startswith('0x') or value_str.startswith('0X'):
                return str(int(value_str, 16))
            else:
                return value_str
        return None
    
    def __parse_driver_date(self, driver_date_str):
        # Handle Microsoft JSON date format /Date(milliseconds)/
        if driver_date_str and driver_date_str.startswith('/Date('):
            try:
                # Extract milliseconds from /Date(1234567890000)/
                match = re.search(r'/Date\((\d+)\)/', driver_date_str)
                if match:
                    milliseconds = int(match.group(1))
                    dt = datetime.fromtimestamp(milliseconds / 1000.0)
                    return dt.strftime("%-m/%-d/%Y")  # For Linux/macOS
            except (ValueError, AttributeError):
                pass
        # Handle YYYYMMDD format
        elif driver_date_str and len(driver_date_str) >= 8 and driver_date_str[:8].isdigit():
            date_part = driver_date_str[:8]
            dt = datetime.strptime(date_part, "%Y%m%d")
            return dt.strftime("%-m/%-d/%Y")  # For Linux/macOS
            # return dt.strftime("%#m/%#d/%Y")  # For Windows, if needed
        return driver_date_str
    
    def __normalize_audio_name(self, name):
        # Replace special chars and lowercase for comparison
        return name.replace("®", "r").lower().strip()
    
    def __click_maximize_btn(self):
        self.fc.fd["devices_support_pc_mfe"].click_maximize_btn()
        time.sleep(2)
        self.fc.fd["devices_support_pc_mfe"].click_maximize_btn()
        time.sleep(2)