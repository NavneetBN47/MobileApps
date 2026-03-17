from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Adddevice(object):
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
        self.fc.ensure_web_password_credentials_cleared()

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63794938")
    def test_01_hpx_rebranding_C63794938(self):
        """
        https://hp-testrail.external.hp.com//index.php?/cases/view/63794938
        """
        self.__add_device("TH437CY0CH")
    
    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63794939")
    def test_02_hpx_rebranding_C63794939(self):
        """
        https://hp-testrail.external.hp.com//index.php?/cases/view/63794939
        """
        self.__verify_add_device("TH437CY0CH")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63794951")
    def test_03_hpx_rebranding_C63794951(self):
        """
        https://hp-testrail.external.hp.com//index.php?/cases/view/63794951
        """
        self.__verify_add_device("5CG14593SS")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63794952")
    def test_04_hpx_rebranding_C63794952(self):
        """
        https://hp-testrail.external.hp.com//index.php?/cases/view/63794952
        """
        self.__verify_add_device("5CD030KTTW")  

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63794953")
    def test_05_hpx_rebranding_C63794953(self):
        """
        https://hp-testrail.external.hp.com//index.php?/cases/view/63794953
        """
        self.__verify_add_device("8CG7200VNY")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63930608")
    def test_06_hpx_rebranding_C63930608(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63930608
        """
        self.__verify_add_device("4CE444B50B")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63930650")
    def test_07_hpx_rebranding_C63930650(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63930650
        """
        self.__verify_add_device("4CE444B50B")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63934682")
    def test_08_hpx_rebranding_C63934682(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63934682
        """
        self.__verify_add_device("CN463AP059")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63934745")
    def test_09_hpx_rebranding_C63934745(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63934745
        """
        self.__verify_add_device("PHA91106GW")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63934748")
    def test_10_hpx_rebranding_C63934748(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63934748
        """
        self.__verify_add_device("8CC102Z1BZ")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63934863")
    def test_11_hpx_rebranding_C63934863(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63934863
        """
        self.__verify_add_device("3CB0320023")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63934883")
    def test_12_hpx_rebranding_C63934883(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63934883
        """
        self.__verify_add_device("CZ72301111")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63936253")
    def test_13_hpx_rebranding_C63936253(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63936253
        """
        self.__verify_add_device("9CP13740NT")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63936345")
    def test_14_hpx_rebranding_C63936345(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63936345
        """
        self.__verify_add_device("5CG135Z0QJ")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63936379")
    def test_15_hpx_rebranding_C63936379(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63936379
        """
        self.__verify_add_device("2LTEWL")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63936949")
    def test_16_hpx_rebranding_C63936949(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63936949
        """
        self.__verify_add_device("EE6PWG")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C63936963")
    def test_17_hpx_rebranding_C63936963(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/63936963
        """
        self.__verify_add_device("214603463")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64746473")    
    def test_18_hpx_rebranding_C64746473(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746473
        """
        self.__add_device("TH19LCK092")
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(0)
        assert self.fc.fd["devices_details_pc_mfe"].return_nick_name_of_pc_device() == "My Computer", "Nick name is not matching"
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == True

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C64746473")    
    def test_19_hpx_rebranding_C64746473(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/64746473
        """
        self.__add_device("TH19LCK092")
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(1)
        assert self.fc.fd["devices_support_pc_mfe"].return_nick_name_of_remote_device() == "HP ENVY 6055e All-in-One Printer", "Nick name is not matching"
        assert self.fc.fd["devices_support_pc_mfe"].verify_support_diagnostic_title() == False

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C83399008")    
    def test_20_hpx_rebranding_C83399008(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83399008
        """
        self.fc.select_device()
        time.sleep(20)
        self.fc.click_profile_button()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_device_add_btn()  
        self.fc.fd["devices_support_pc_mfe"].click_search_by_sn_button()
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].input_sn("NLBVM3M0SR")
        time.sleep(5)
        self.fc.fd["add_device"].input_enter_product_number("Z5G79A")
        time.sleep(15)
        self.fc.fd["add_device"].click_add_device_hyperlink()
        assert self.fc.fd["add_device"].verify_newly_added_devicename(), "Newly added device name is not displayed"

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
        self.fc.select_device()
        # if self.stack not in ["dev", "itg"]:
        #     self.fc.fd["devicesMFE"].click_device_card_by_index()

    def __click_contact_us_btn(self):
        time.sleep(15)
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()

    def __click_top_profile_icon(self):
        time.sleep(10)
        self.fc.fd["devicesMFE"].click_top_profile_icon()

    def __click_support_option(self):
        time.sleep(5)
        self.fc.fd["devices_support_pc_mfe"].select_support_option()

    def __add_device(self, sn):
        self.fc.select_device()
        time.sleep(20)
        self.fc.click_profile_button()
        self.__click_support_option()
        self.fc.fd["devices_support_pc_mfe"].click_device_add_btn()  
        self.fc.fd["devices_support_pc_mfe"].click_search_by_sn_button()
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].input_sn(sn)
        time.sleep(15)
        self.fc.fd["devices_support_pc_mfe"].click_add_device_link()

    def __verify_add_device(self, sn):
        self.__add_device(sn)
        self.fc.fd["devices_support_pc_mfe"].click_support_device_card(1)
        assert self.fc.fd["devices_support_pc_mfe"].verify_contact_us_btn() == True
        assert self.fc.fd["devices_support_pc_mfe"].verify_warranty_info() == True
