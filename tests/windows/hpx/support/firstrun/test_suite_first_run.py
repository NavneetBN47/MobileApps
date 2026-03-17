from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest
import logging
import time

pytest.app_info = "HPX"
class Test_Suite_First_Run(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.request = request
        cls.driver = windows_test_setup

        cls.logger=logging.getLogger()
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)
        cls.registry = RegistryUtilities(cls.driver.ssh)     
        cls.hpid = cls.fc.fd["hpid"]   
        cls.navigation_panel = cls.fc.fd["navigation_panel"]
        cls.hp_registration = cls.fc.fd["hp_registration"]
        cls.hp_privacy_setting = cls.fc.fd["hp_privacy_setting"]
        cls.support_home = cls.fc.fd["support_home"]
        cls.support_device = cls.fc.fd["support_device"]
        cls.support_va = cls.fc.fd["support_va"]

        cls.stack = request.config.getoption("--stack")
        cls.app_env = request.config.getoption("--app-env")

    # @pytest.fixture(scope="function", autouse="true")
    # def function_setup(self):
    #     self.fc.initial_hpx_support_env()

    #https://hp-jira.external.hp.com/browse/HPXSUP-2730
    @pytest.mark.parametrize("country_code, country_nation, country_name",
                             [
                                ("GB", "242", "United Kingdom"),
                                ("CA", "39", "Canada"),
                                ("SG", "215", "Singapore"),
                                ("AU", "12", "Australia"),
                                ("CN", "45", "China")
                            ])
    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C38196242")      
    def test_01_default_region(self, country_code, country_nation, country_name):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38196242
        """
        self.__test_region(country_code, country_nation, country_name)

    @pytest.mark.parametrize("country_code, country_nation, country_name",
                             [
                                ("RU", "188", "Russian Federation"),
                                ("BY", "26", "Belarus")
                             ])
    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C38196242")   
    def test_02_default_region(self, country_code, country_nation, country_name):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38196242
        if system region is Russia and Belarus, verify default support region is Kazakhstan.
        """    
        self.__test_region(country_code, country_nation, country_name)

    @pytest.mark.parametrize("country_code, country_nation, country_name", 
                             [
                                ("GU", "94", "Guam"),
                                ("CU", "53", "Cuba")
                            #   ("MF", "154", "Saint Martin"),
                            #   ("GU", "94", "Guam"),
                            #   ("AX", "1", "Aland Islands"),
                            #   ("SX", "211", "Sint Maarten"),
                            #   ("NR", "155", "Nauru"),
                            #   ("TV", "218", "Tuvalu"),
                            #   ("HM", "106", "Heard Island and McDonald Islands"),
                            #   ("BV", "29", "Bouvet Island"),
                            #   ("PS", "167", "Palestinian Territory"),
                            #   ("IO", "107", "British Indian Ocean Territory"),
                            #   ("PW", "170", "Palau"),
                            #   ("PN", "168", "Pitcairn"),
                            #   ("BY", "26", "Kazakhstan"),
                            #   ("JE", "110", "Jersey"),
                            #   ("FK", "72", "Falkland Islands"),
                            #   ("GS", "89", "South Georgia and the South Sandwich Islands"),
                            #   ("MP", "156", "Northern Mariana Islands"),
                            #   ("NF", "157", "Norfolk Island"),
                            #   ("SY", "214", "Syrian Arab Republic"),
                            #   ("KP", "120", "Korea, Democratic People's Republic of"),
                            #   ("MS", "153", "Montserrat"),
                            #   ("SJ", "203", "Svalbard and Jan Mayen"),
                            #   ("CU", "53", "Cuba"),
                            #   ("CU", "53", "Cuba"),
                            #   ("BQ", "25", "Bonaire, Sint Eustatius and Saba"),
                            #   ("UM", "221", "United States Minor Outlying Islands"),
                            #   ("FM", "69", "Micronesia, Federated States of"),
                            #   ("SD", "195", "Sudan"),
                            #   ("AQ", "10", "Antarctica"),
                            #   ("IR", "114", "Iran, Islamic Republic of"),
                            #   ("CW", "52", "Curaçao"),
                            #   ("CC", "41", "Cocos (Keeling) Islands"),
                            #   ("KI", "117", "Kiribati"),
                            #   ("CX", "46", "Christmas Island"),
                            #   ("GG", "88", "Guernsey"),
                            #   ("TK", "207", "Tokelau"),
                            #   ("VA", "223", "Holy See (Vatican City State)"),
                            #   ("CK", "42", "Cook Islands"),
                            #   ("BL", "22", "Saint Barthélemy"),
                            #   ("MH", "151", "Marshall Islands"),
                            #   ("SH", "197", "Saint Helena, Ascension and Tristan da Cunha"),
                            #   ("NU", "161", "Niue"),
                            #   ("SB", "192", "Solomon Islands")
                              ] )
    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C38196242")   
    def test_03_default_region(self, country_code, country_nation, country_name):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38196242
         if system region is others, verify it shows country flag of system region's.
        """
        self.__test_region(country_code, country_nation, country_name)

    @pytest.mark.require_priority(["High"])    
    @pytest.mark.require_stack(["pie", "production", "stage"])
    @pytest.mark.testrail("S57581.C38196242")   
    def test_04_default_region(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/38196242
        if user chooses a region from HPX, then it always shows this region and ignore system region.
        """
        self.__launch_HPX()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.fc.select_country("JP")
        time.sleep(5)
        self.__launch_HPX()
        self.support_home.select_device_card(self.wmi.get_serial_number())      
        self.support_device.verify_support_device_page()
        _country_name = self.support_device.get_country()
        assert _country_name == "Japan"

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __test_region(self, country_code, country_nation, country_name):
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", country_code)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", country_nation)
        self.__reinstall_HPX()
        self.fc.initial_feature()
        self.__launch_HPX()
        self.support_home.select_device_card(self.wmi.get_serial_number())
        self.support_device.verify_support_device_page()
        _country_code = self.support_device.get_country()
        logging.info("=====country_code: {}".format(_country_code))
        if country_code in ["RU", "BY"]:
            assert _country_code == "Kazakhstan"
        elif country_code in ["GU", "CU"]:
            assert _country_code == country_code
        else:
            assert _country_code == country_name

    def __launch_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        self.__click_accept_all_btn()
        self.__click_skip_btn()
        self.fc.navigate_to_support()
    
    def __click_skip_btn(self):
        if self.hp_registration.verify_skip_button_show():
            self.hp_registration.click_skip_button()

    def __click_accept_all_btn(self):
        if self.hp_privacy_setting.verify_accept_button_show():
            self.hp_privacy_setting.click_accept_all_button()

    def __reinstall_HPX(self):
        self.fc.uninstall_app()
        self.fc.remove_file("C:/Users/exec/AppData/Local/Packages/AD2F1837.myHP_v10z8vjag6ke6")
        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support")
        time.sleep(120)
        if self.request.config.getoption("--local-build") is not None:
            local_build = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build + "\\Install.ps1 -Force")  