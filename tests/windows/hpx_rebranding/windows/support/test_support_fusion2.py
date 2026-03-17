from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Fusion2(object):
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
        self.__restart_fusion_services()

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745836")
    def test_01_hpx_rebranding_C64745836(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745836
        """
        self.__stop_fusion_services()
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == False
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == False  
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745840")
    def test_02_hpx_rebranding_C64745840(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745840
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.62.3534.0_release\Fusion.1.62.3534.0.Comp.000C-W10W11SV2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.62.3534.0_release\Fusion.1.62.3534.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == False
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == False
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745841")
    def test_03_hpx_rebranding_C64745841(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745841
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.63.3600.0_release\Fusion.1.63.3600.0.Comp.000C-W10W11SV2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.63.3600.0_release\Fusion.1.63.3600.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == False
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == False
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745842")
    def test_04_hpx_rebranding_C64745842(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745842
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.64.3626.0_release\Fusion.1.64.3626.0.Comp.000C-W10W11SV2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.64.3626.0_release\Fusion.1.64.3626.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745843")
    def test_05_hpx_rebranding_C64745843(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745843
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.65.3659.0_release\Fusion.1.65.3659.0.Comp.000C-W10W11SV2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.65.3659.0_release\Fusion.1.65.3659.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745846")
    def test_06_hpx_rebranding_C64745846(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745846
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.66.3762.0_release\Fusion.1.66.3762.0.Comp.000C-W10W1124H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.66.3762.0_release\Fusion.1.66.3762.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745847")
    def test_07_hpx_rebranding_C64745847(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745847
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.70.3868.0_release\Fusion.1.70.3868.0.Comp.000C-W10W1122H224H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.70.3868.0_release\Fusion.1.70.3868.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745848")
    def test_08_hpx_rebranding_C64745848(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745848
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.73.4045.0_release\Fusion.1.73.4045.0.Comp.000C-W1124H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.73.4045.0_release\Fusion.1.73.4045.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745849")
    def test_09_hpx_rebranding_C64745849(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745849
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.76.4125.0_release\Fusion.1.76.4125.0.Comp.000C-W1124H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.76.4125.0_release\Fusion.1.76.4125.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745850")
    def test_10_hpx_rebranding_C64745850(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745850
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.77.4151.0_release\Fusion.1.77.4151.0.Comp.000C-W1124H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.77.4151.0_release\Fusion.1.77.4151.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745866")
    def test_11_hpx_rebranding_C64745866(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745866
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.78.4195.0_release\Fusion.1.78.4195.0.Comp.000C-W1124H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.78.4195.0_release\Fusion.1.78.4195.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True    

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745867")
    def test_12_hpx_rebranding_C64745867(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745867
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.79.4260.0_release\Fusion.1.79.4260.0.Comp.000C-W1124H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.79.4260.0_release\Fusion.1.79.4260.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True   

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745868")
    def test_13_hpx_rebranding_C64745868(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745868
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.80.4268.0_release\Fusion.1.80.4268.0.Comp.000C-W1124H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.80.4268.0_release\Fusion.1.80.4268.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True  

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745869")
    def test_14_hpx_rebranding_C64745869(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745869
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.81.4279.0_release\Fusion.1.81.4279.0.Comp.000C-W1124H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.81.4279.0_release\Fusion.1.81.4279.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True     

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745870")
    def test_15_hpx_rebranding_C64745870(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745870
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.82.4285.0_release\Fusion.1.82.4285.0.Comp.000C-W1124H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.82.4285.0_release\Fusion.1.82.4285.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True    

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64745871")
    def test_16_hpx_rebranding_C64745871(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64745871
        """
        ini_files = self.__remote_extract_zip_and_find_inf(
            r"C:\Users\exec\HPXBuild\Fusion\1.83.4311.0_release\Fusion.1.83.4311.0.Comp.000C-W1124H2-WHLK.zip",
            r"C:\Users\exec\HPXBuild\Fusion\1.83.4311.0_release\Fusion.1.83.4311.0"
        )
        self.__install_service_with_devcon(ini_files[0], "SWC\\HPIC000C")
        self.fc.select_device()
        assert self.fc.fd["devices_support_pc_mfe"].verify_start_virtual_assist_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_manual_guided_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_find_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_virtual_repair_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_product_support_center_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_specifications_button() == True
        self.__click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_chat_agent_btn() is not False
        assert self.fc.fd["devices_support_pc_mfe"].verify_case_history_title() == True         

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __first_start_HPX(self):
        self.fc.close_app()
        self.fc.launch_app()

    def __start_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        if self.fc.fd["hpx_fuf"].verify_accept_cookies_button_show():
            self.fc.fd["hpx_fuf"].click_accept_cookies_button()
        if self.fc.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fc.fd["hpx_fuf"].click_accept_all_button()
        if self.fc.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fc.fd["hpx_fuf"].click_continue_as_guest_button()
        if self.fc.fd["hpx_fuf"].verify_what_is_this_dialog_show():
            self.fc.fd["hpx_fuf"].click_what_is_new_skip_button()

    def __select_device(self):
        self.__start_HPX()
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index()

    def __click_contact_us_btn(self):
        time.sleep(5)
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()

    def __install_service_with_devcon(self, inf_path, hardware_id, timeout=60):
        """
        Installs a driver/service using devcon on the remote Windows machine.

        Args:
            inf_path (str): Full path to the INF file on the remote machine.
            hardware_id (str): Hardware ID for the device.
            timeout (int): Timeout for the install command.

        Returns:
            True if installation is successful, raises CommandFailedException otherwise.
        """
        cmd = f'powershell devcon install "{inf_path}" "{hardware_id}"'
        result = self.driver.ssh.send_command(cmd, timeout=timeout)
        stdout = result.get("stdout", "") if isinstance(result, dict) else str(result)
        stderr = result.get("stderr", "") if isinstance(result, dict) else ""
        print(f"Devcon stdout: {stdout}")
        print(f"Devcon stderr: {stderr}")
        if "is installed" in stdout.lower() or "successfully" in stdout.lower():
            return True
        else:
            print(f"Failed to install service with devcon: {inf_path}, {hardware_id}\nOutput: {stdout}")
            return False
        
    def __remote_extract_zip_and_find_inf(self, zip_path, extract_to):
        """
        Remotely extracts a zip file and finds all .inf files in the extracted directory.

        Args:
            zip_path (str): Path to the zip file on the remote machine.
            extract_to (str): Directory to extract files to on the remote machine.

        Returns:
            List of full paths to .inf files found in the extracted directory.
        """
        # Extract the zip file remotely using PowerShell
        extract_cmd = (
            f'powershell -Command "Expand-Archive -Path \'{zip_path}\' -DestinationPath \'{extract_to}\' -Force"'
        )
        self.driver.ssh.send_command(extract_cmd, timeout=120)

        # Find all .inf files recursively using PowerShell
        find_inf_cmd = (
            f'powershell -Command "Get-ChildItem -Path \'{extract_to}\' -Recurse -Filter *.inf | Select-Object -ExpandProperty FullName"'
        )
        result = self.driver.ssh.send_command(find_inf_cmd, timeout=60)
        stdout = result.get("stdout", "") if isinstance(result, dict) else str(result)
        inf_files = [line.strip() for line in stdout.splitlines() if line.strip()]
        return inf_files
    
    def __stop_fusion_services(self):
        self.fc.stop_hp_networkcap_exe()
        self.fc.stop_hp_apphelpercap_exe()
        self.fc.stop_hpsysinfo_fusion_services()

    def __start_fusion_services(self):
        self.fc.start_hp_networkcap_exe()
        self.fc.start_hp_apphelpercap_exe()
        self.fc.start_hpsysinfo_fusion_services()

    def __restart_fusion_services(self):
        self.__stop_fusion_services()
        self.__start_fusion_services()