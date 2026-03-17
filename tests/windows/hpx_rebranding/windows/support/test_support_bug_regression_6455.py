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
class Test_Suite_Bug_Regression_6455(object):
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

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C83266066")
    def test_01_hpx_rebranding_C83266066(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266066
        """
        self.__verify_translations_for_hardware_issues_string("SA", 205, "ar-SA")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252874")
    def test_02_hpx_rebranding_C83266067(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266067
        """
        self.__verify_translations_for_hardware_issues_string("BG", 35, "bg")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252874")
    def test_03_hpx_rebranding_C83266068(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266068
        """
        self.__verify_translations_for_hardware_issues_string("CZ", 75, "cs")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_04_hpx_rebranding_C83266069(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266069
        """
        self.__verify_translations_for_hardware_issues_string("DK", 61, "da")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_05_hpx_rebranding_C83266070(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266070
        """
        self.__verify_translations_for_hardware_issues_string("DE", 94, "de-DE")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_06_hpx_rebranding_C83266071(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266071
        """
        self.__verify_translations_for_hardware_issues_string("GR", 98, "el")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_07_hpx_rebranding_C83266072(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266072
        """
        self.__verify_translations_for_hardware_issues_string("GB", 242, "en-GB")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_08_hpx_rebranding_C83266073(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266073
        """
        self.__verify_translations_for_hardware_issues_string("ES", 128, "es-ES")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_09_hpx_rebranding_C83266074(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266074
        """
        self.__verify_translations_for_hardware_issues_string("EE", 233, "et")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_10_hpx_rebranding_C83266075(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266075
        """
        self.__verify_translations_for_hardware_issues_string("FI", 77, "fi")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_11_hpx_rebranding_C83266076(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266076
        """
        self.__verify_translations_for_hardware_issues_string("CA", 39, "fr-CA")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_12_hpx_rebranding_C83266077(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266077
        """
        self.__verify_translations_for_hardware_issues_string("FR", 84, "fr-FR")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_13_hpx_rebranding_C83266079(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266079
        """
        self.__verify_translations_for_hardware_issues_string("IL", 117, "he")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_14_hpx_rebranding_C83266081(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266081
        """
        self.__verify_translations_for_hardware_issues_string("HR", 108, "hr-HR")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_15_hpx_rebranding_C83266082(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266082
        """
        self.__verify_translations_for_hardware_issues_string("HU", 109, "hu")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_16_hpx_rebranding_C83266083(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266083
        """
        self.__verify_translations_for_hardware_issues_string("IT", 118, "it-IT")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_17_hpx_rebranding_C83266084(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266084
        """
        self.__verify_translations_for_hardware_issues_string("JP", 122, "ja")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_18_hpx_rebranding_C83266085(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266085
        """
        self.__verify_translations_for_hardware_issues_string("KR", 134, "ko")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_19_hpx_rebranding_C83266086(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266086
        """
        self.__verify_translations_for_hardware_issues_string("LT", 141, "lt")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_20_hpx_rebranding_C83266087(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266087
        """
        self.__verify_translations_for_hardware_issues_string("LV", 140, "lv")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_21_hpx_rebranding_C83266088(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266088
        """
        self.__verify_translations_for_hardware_issues_string("NO", 177, "nb")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_22_hpx_rebranding_C83266089(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266089
        """
        self.__verify_translations_for_hardware_issues_string("NL", 176, "nl-NL")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_23_hpx_rebranding_C83266091(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266091
        """
        self.__verify_translations_for_hardware_issues_string("PL", 191, "pl")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_24_hpx_rebranding_C83266093(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266093
        """
        self.__verify_translations_for_hardware_issues_string("BR", 55, "pt-BR")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_25_hpx_rebranding_C83266094(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266094
        """
        self.__verify_translations_for_hardware_issues_string("PT", 193, "pt-PT")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_26_hpx_rebranding_C83266095(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266095
        """
        self.__verify_translations_for_hardware_issues_string("RO", 200, "ro")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_27_hpx_rebranding_C83266096(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266096
        """
        self.__verify_translations_for_hardware_issues_string("SK", 143, "sk")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_28_hpx_rebranding_C83266097(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266097
        """
        self.__verify_translations_for_hardware_issues_string("SI", 212, "sl")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_29_hpx_rebranding_C83266098(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266098
        """
        self.__verify_translations_for_hardware_issues_string("SE", 221, "sv-SE")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_30_hpx_rebranding_C83266099(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266099
        """
        self.__verify_translations_for_hardware_issues_string("TH", 227, "th")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_31_hpx_rebranding_C83266100(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266100
        """
        self.__verify_translations_for_hardware_issues_string("TR", 235, "tr")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_32_hpx_rebranding_C83266101(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266101
        """
        self.__verify_translations_for_hardware_issues_string("UA", 241, "uk")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_33_hpx_rebranding_C83266102(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266102
        """
        self.__verify_translations_for_hardware_issues_string("CN", 45, "zh-Hans-CN")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C73252874")
    def test_34_hpx_rebranding_C83266103(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266103
        """
        self.__verify_translations_for_hardware_issues_string("TW", 237, "zh-Hant-TW")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_35_hpx_rebranding_C83266104(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266104
        """
        self.__verify_translations_for_instant_ink_issues_string("SA", 205, "ar-SA")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_36_hpx_rebranding_C83266105(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266105
        """
        self.__verify_translations_for_instant_ink_issues_string("BG", 35, "bg")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_37_hpx_rebranding_C83266106(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266106
        """
        self.__verify_translations_for_instant_ink_issues_string("CZ", 75, "cs")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_38_hpx_rebranding_C83266107(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266107
        """
        self.__verify_translations_for_instant_ink_issues_string("DK", 61, "da")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_39_hpx_rebranding_C83266108(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266108
        """
        self.__verify_translations_for_instant_ink_issues_string("DE", 94, "de-DE")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_40_hpx_rebranding_C83266109(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266109
        """
        self.__verify_translations_for_instant_ink_issues_string("GR", 98, "el")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_41_hpx_rebranding_C83266110(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266110
        """
        self.__verify_translations_for_instant_ink_issues_string("GB", 242, "en-GB")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_42_hpx_rebranding_C83266111(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266111
        """
        self.__verify_translations_for_instant_ink_issues_string("ES", 128, "es-ES")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_43_hpx_rebranding_C83266112(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266112
        """
        self.__verify_translations_for_instant_ink_issues_string("EE", 233, "et")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_44_hpx_rebranding_C83266113(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266113
        """
        self.__verify_translations_for_instant_ink_issues_string("FI", 77, "fi")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_45_hpx_rebranding_C83266114(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266114
        """
        self.__verify_translations_for_instant_ink_issues_string("CA", 39, "fr-CA")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_46_hpx_rebranding_C83266115(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266115
        """
        self.__verify_translations_for_instant_ink_issues_string("FR", 84, "fr-FR")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_47_hpx_rebranding_C83266116(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266116
        """
        self.__verify_translations_for_instant_ink_issues_string("IL", 117, "he")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_48_hpx_rebranding_C83266117(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266117
        """
        self.__verify_translations_for_instant_ink_issues_string("HR", 108, "hr-HR")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_49_hpx_rebranding_C83266118(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266118
        """
        self.__verify_translations_for_instant_ink_issues_string("HU", 109, "hu")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_50_hpx_rebranding_C83266119(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266119
        """
        self.__verify_translations_for_instant_ink_issues_string("IT", 118, "it-IT")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_51_hpx_rebranding_C83266120(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266120
        """
        self.__verify_translations_for_instant_ink_issues_string("JP", 122, "ja")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_52_hpx_rebranding_C83266122(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266122
        """
        self.__verify_translations_for_instant_ink_issues_string("KR", 134, "ko")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_53_hpx_rebranding_C83266123(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266123
        """
        self.__verify_translations_for_instant_ink_issues_string("LT", 141, "lt")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_54_hpx_rebranding_C83266124(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266124
        """
        self.__verify_translations_for_instant_ink_issues_string("LV", 140, "lv")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_55_hpx_rebranding_C83266125(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266125
        """
        self.__verify_translations_for_instant_ink_issues_string("NO", 177, "nb")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_56_hpx_rebranding_C83266126(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266126
        """
        self.__verify_translations_for_instant_ink_issues_string("NL", 176, "nl-NL")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_57_hpx_rebranding_C83266127(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266127
        """
        self.__verify_translations_for_instant_ink_issues_string("PL", 191, "pl")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_58_hpx_rebranding_C83266128(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266128
        """
        self.__verify_translations_for_instant_ink_issues_string("BR", 55, "pt-BR")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_59_hpx_rebranding_C83266129(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266129
        """
        self.__verify_translations_for_instant_ink_issues_string("PT", 193, "pt-PT")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_60_hpx_rebranding_C83266130(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266130
        """
        self.__verify_translations_for_instant_ink_issues_string("RO", 200, "ro")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_61_hpx_rebranding_C83266131(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266131
        """
        self.__verify_translations_for_instant_ink_issues_string("SK", 143, "sk")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_62_hpx_rebranding_C83266132(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266132
        """
        self.__verify_translations_for_instant_ink_issues_string("SI", 212, "sl")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_63_hpx_rebranding_C83266133(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266133
        """
        self.__verify_translations_for_instant_ink_issues_string("SE", 221, "sv-SE")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_64_hpx_rebranding_C83266134(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266134
        """
        self.__verify_translations_for_instant_ink_issues_string("TH", 227, "th")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_65_hpx_rebranding_C83266135(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266135
        """
        self.__verify_translations_for_instant_ink_issues_string("TR", 235, "tr")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_66_hpx_rebranding_C83266136(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266136
        """
        self.__verify_translations_for_instant_ink_issues_string("UA", 241, "uk")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_67_hpx_rebranding_C83266137(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266137
        """
        self.__verify_translations_for_instant_ink_issues_string("CN", 45, "zh-Hans-CN")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_68_hpx_rebranding_C83266138(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83266138
        """
        self.__verify_translations_for_instant_ink_issues_string("TW", 237, "zh-Hant-TW")

    @pytest.mark.require_stack(["dev", "itg"]) 
    @pytest.mark.testrail("S57581.C73252874")
    def test_69_hpx_rebranding_C83326597(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83326597
        """
        self.__verify_translations_for_hardware_issues_string("RU", 203, "ru-RU")

    @pytest.mark.require_stack(["dev", "itg"])
    @pytest.mark.testrail("S57581.C61957136")
    def test_70_hpx_rebranding_C83326598(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83326598
        """
        self.__verify_translations_for_instant_ink_issues_string("RU", 203, "ru-RU")

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

    def __get_language_list(self):
        languages = self.registry.get_registry_value(
            "HKEY_CURRENT_USER\\Control Panel\\International\\User Profile", 
            "Languages"
            )
        if languages:
            languages = languages['stdout']
            languages = languages.strip()
            languages = languages.replace('\r\n', '')
            languages = languages.split('REG_MULTI_SZ')[1]
            languages = languages.strip()
            languages = languages.split('\\0')
            return languages
        return []
    
    def __set_language_list(self, language_list):
        reg_multi_sz_value = "@(" + ",".join([f'"{lang}"' for lang in language_list]) + ")"
        path = self.registry.format_registry_path("HKEY_CURRENT_USER\\Control Panel\\International\\User Profile")
        key_name = "Languages"
        key_value = reg_multi_sz_value
        self.driver.ssh.send_command('Set-Itemproperty -path \"{}\" -Name \"{}\" -Value {}'.format(path, key_name, key_value), raise_e=False)

    def __set_prefered_language(self, language):
        language_list = self.__get_language_list()
        if language in language_list:
            language_list.remove(language)
            language_list.insert(0, language)
        self.__set_language_list(language_list)

    def __verify_translations_for_hardware_issues_string(self, country_code, country_nation, language):
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", country_code)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", country_nation)
        self.__set_prefered_language(language)
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(3)
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_hardware_issue_btn().text != "Hardware issues"

    def __verify_translations_for_instant_ink_issues_string(self, country_code, country_nation, language):
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", country_code)
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", country_nation)
        self.__set_prefered_language(language)
        self.fc.select_device()
        self.__sign_in_HPX()
        self.fc.fd["devices_details_pc_mfe"].click_back_devices_button()
        self.fc.fd["devicesMFE"].click_device_card_by_index(3)
        self.fc.fd["devices_support_pc_mfe"].click_contact_us_btn()
        assert self.fc.fd["devices_support_pc_mfe"].verify_instant_ink_issue_btn().text != "Instant Ink issues"

    def __select_device(self, maxmized=False, index=0):
        self.__start_HPX(maxmized=maxmized)

    def __click_start_virtual_assist_btn(self):
        time.sleep(10)
        self.fc.fd["devices_support_pc_mfe"].click_start_virtual_assist_btn()  

    def __sign_in_HPX(self, sign_in_from_profile=False):
        self.fc.sign_in("iiqa.automated+adc+17964f10@gmail.com", "Test@123", self.web_driver, sign_in_from_profile=sign_in_from_profile)