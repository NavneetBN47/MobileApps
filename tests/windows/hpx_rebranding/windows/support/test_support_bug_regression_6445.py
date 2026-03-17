from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from MobileApps.libs.flows.web.support_document.support_flow_container import SupportFlowContainer
from datetime import datetime
import MobileApps.resources.const.windows.const as w_const
import tempfile
import os
import pytest
import time

pytest.app_info = "HPX"
class Test_Suite_Bug_Regression_6445(object):
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
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Name", "US")
        self.registry.update_value("HKEY_CURRENT_USER\\Control Panel\International\Geo", "Nation", 244)
        self.__set_prefered_language("en-US")
        self.fc.initial_environment()
        self.fc.ensure_web_password_credentials_cleared()
        if self.stack in ["itg"]:
            self.fc.set_proxy_on_remote_windows("web-proxy.corp.hp.com:8080")

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C82893088")
    def test_01_hpx_rebranding_C82893088(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/82893088
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPSACommand.dll")
        assert cert_is_valid, "Certificate for HPSACommand.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C82893089")
    def test_02_hpx_rebranding_C82893089(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/82893089
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HP.OCF.Common.dll")
        assert cert_is_valid, "Certificate for HP.OCF.Common.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C82893090")
    def test_03_hpx_rebranding_C82893090(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/82893090
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HP.OCF.StateData.dll")
        assert cert_is_valid, "Certificate for HP.OCF.StateData.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C82893094")
    def test_04_hpx_rebranding_C82893094(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/82893094
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HP.SupportFramework.Common.dll")
        assert cert_is_valid, "Certificate for HP.SupportFramework.Common.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C82893095")
    def test_05_hpx_rebranding_C82893095(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/82893095
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HP.SupportFramework.Localization.dll")
        assert cert_is_valid, "Certificate for HP.SupportFramework.Localization.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C82893096")
    def test_06_hpx_rebranding_C82893096(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/82893096
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HP.SupportFramework.UI.dll")
        assert cert_is_valid, "Certificate for HP.SupportFramework.UI.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C82893097")
    def test_07_hpx_rebranding_C82893097(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/82893097
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPSAAppLauncher.exe")
        assert cert_is_valid, "Certificate for HPSAAppLauncher.exe is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C82893098")
    def test_08_hpx_rebranding_C82893098(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/82893098
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPSALauncher.exe")
        assert cert_is_valid, "Certificate for HPSALauncher.exe is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C82893103")
    def test_09_hpx_rebranding_C82893103(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/82893103
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPSFReport.exe")
        assert cert_is_valid, "Certificate for HPSFReport.exe is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"]) 
    @pytest.mark.testrail("S57581.C82893104")
    def test_10_hpx_rebranding_C82893104(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/82893104
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPSFViewer.exe")
        assert cert_is_valid, "Certificate for HPSFViewer.exe is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046291")
    def test_11_hpx_rebranding_C83046291(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046291
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPNetworkCheck\\HPNDFInterface.dll")
        assert cert_is_valid, "Certificate for HPNDFInterface.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046293")
    def test_12_hpx_rebranding_C83046293(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046293
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPNetworkCheck\\HPNetworkCheck.exe")
        assert cert_is_valid, "Certificate for HPNetworkCheck.exe is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046295")
    def test_13_hpx_rebranding_C83046295(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046295
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPNetworkCheck\\Interop.HelpPane.dll")
        assert cert_is_valid, "Certificate for Interop.HelpPane.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046296")
    def test_14_hpx_rebranding_C83046296(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046296
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPNetworkCheck\\ManagedWifi.dll")
        assert cert_is_valid, "Certificate for ManagedWifi.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046297")
    def test_15_hpx_rebranding_C83046297(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046297
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPNetworkCheck\\Microsoft.mshtml.dll")
        assert cert_is_valid, "Certificate for Microsoft.mshtml.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046298")
    def test_16_hpx_rebranding_C83046298(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046298
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPOSCheck\\HPOSCheck.exe")
        assert cert_is_valid, "Certificate for HPOSCheck.exe is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046299")
    def test_17_hpx_rebranding_C83046299(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046299
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\FileSystemSDK.dll")
        assert cert_is_valid, "Certificate for FileSystemSDK.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046300")
    def test_18_hpx_rebranding_C83046300(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046300
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\Hp.Bridge.Client.BusinessLogic.CommonBL.dll")
        assert cert_is_valid, "Certificate for Hp.Bridge.Client.BusinessLogic.CommonBL.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046301")
    def test_19_hpx_rebranding_C83046301(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046301
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\Hp.Bridge.Client.BusinessLogic.PerfTuneupBL.dll")
        assert cert_is_valid, "Certificate for Hp.Bridge.Client.BusinessLogic.PerfTuneupBL.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046304")
    def test_20_hpx_rebranding_C83046304(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046304
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\Hp.Bridge.Client.SDKs.CDXConnectionSDK.dll")
        assert cert_is_valid, "Certificate for Hp.Bridge.Client.SDKs.CDXConnectionSDK.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046305")
    def test_21_hpx_rebranding_C83046305(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046305
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\HP.CDX.Utils.MgrTran.dll")
        assert cert_is_valid, "Certificate for HP.CDX.Utils.MgrTran.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046306")
    def test_22_hpx_rebranding_C83046306(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046306
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\HP.Vision.HW.Cntrl.dll")
        assert cert_is_valid, "Certificate for HP.Vision.HW.Cntrl.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046307")
    def test_23_hpx_rebranding_C83046307(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046307
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\HP.Vision.HW.Devices.dll")
        assert cert_is_valid, "Certificate for HP.Vision.HW.Devices.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046308")
    def test_24_hpx_rebranding_C83046308(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046308
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\HP.Vision.HW.PCim.dll")
        assert cert_is_valid, "Certificate for HP.Vision.HW.PCim.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046309")
    def test_25_hpx_rebranding_C83046309(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046309
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\HP.Vision.HW.SetupDI.dll")
        assert cert_is_valid, "Certificate for HP.Vision.HW.SetupDI.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046311")
    def test_26_hpx_rebranding_C83046311(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046311
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\HP.Vision.Models.dll")
        assert cert_is_valid, "Certificate for HP.Vision.Models.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046312")
    def test_27_hpx_rebranding_C83046312(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046312
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\HP.Vision.Utils.Excptns.dll")
        assert cert_is_valid, "Certificate for HP.Vision.Utils.Excptns.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046313")
    def test_28_hpx_rebranding_C83046313(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046313
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\HP.Vision.Utils.Logging.dll")
        assert cert_is_valid, "Certificate for HP.Vision.Utils.Logging.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046314")
    def test_29_hpx_rebranding_C83046314(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046314
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\HP.Vision.Utils.MgrFile.dll")
        assert cert_is_valid, "Certificate for HP.Vision.Utils.MgrFile.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046315")
    def test_30_hpx_rebranding_C83046315(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046315
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\HPPerformanceTuneup.exe")
        assert cert_is_valid, "Certificate for HPPerformanceTuneup.exe is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046317")
    def test_31_hpx_rebranding_C83046317(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046317
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\LauncherSDK.dll")
        assert cert_is_valid, "Certificate for LauncherSDK.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046325")
    def test_32_hpx_rebranding_C83046325(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046325
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\Logging.dll")
        assert cert_is_valid, "Certificate for Logging.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046332")
    def test_33_hpx_rebranding_C83046332(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046332
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\NativeRpcClient.dll")
        assert cert_is_valid, "Certificate for NativeRpcClient.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046339")
    def test_34_hpx_rebranding_C83046339(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046339
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\Newtonsoft.Json.dll")
        assert cert_is_valid, "Certificate for Newtonsoft.Json.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046347")
    def test_35_hpx_rebranding_C83046347(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046347
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\RpcClient.dll")
        assert cert_is_valid, "Certificate for RpcClient.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046353")
    def test_36_hpx_rebranding_C83046353(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046353
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\SmbiosSDK.dll")
        assert cert_is_valid, "Certificate for SmbiosSDK.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046354")
    def test_37_hpx_rebranding_C83046354(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046354
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\WindowsNTSDK.dll")
        assert cert_is_valid, "Certificate for WindowsNTSDK.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046355")
    def test_38_hpx_rebranding_C83046355(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046355
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\WindowsRegistrySDK.dll")
        assert cert_is_valid, "Certificate for WindowsRegistrySDK.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046356")
    def test_39_hpx_rebranding_C83046356(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046356
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPPerformanceTuneup\\WMISDK.dll")
        assert cert_is_valid, "Certificate for WMISDK.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046358")
    def test_40_hpx_rebranding_C83046358(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046358
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPUpdate\\HP.DeviceUpdate.Contract.dll")
        assert cert_is_valid, "Certificate for HP.DeviceUpdate.Contract.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046365")
    def test_41_hpx_rebranding_C83046365(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046365
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPUpdate\\HP.SUDFClient.dll")
        assert cert_is_valid, "Certificate for HP.SUDFClient.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046369")
    def test_42_hpx_rebranding_C83046369(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046369
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPUpdate\\HP.UpdateClient.dll")
        assert cert_is_valid, "Certificate for HP.UpdateClient.dll is either expired or missing"

    @pytest.mark.require_stack(["dev", "itg", "production"])
    @pytest.mark.testrail("S57581.C83046370")
    def test_43_hpx_rebranding_C83046370(self):
        """
        https://hp-testrail.external.hp.com/index.php?/cases/view/83046370
        """
        self.fc.select_device()
        cert_is_valid = self.__check_expired_certificates_in_resources(w_const.TEST_DATA.HPX_SUPPORT_RESOURCES_PATH + "HPUpdate\\HPUpdate.exe")
        assert cert_is_valid, "Certificate for HPUpdate.exe is either expired or missing"
        
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

    def __click_profile_button(self):
        self.fc.click_profile_button()

    def __click_support_option(self):
        time.sleep(5)
        self.fc.fd["devices_support_pc_mfe"].select_support_option()

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

    def __check_expired_certificates_in_resources(self, file_path):
        """
        Checks the specified .dll or .exe file for expired or missing certificates.
        Returns True if the certificate is valid, False otherwise.
        Handles SSH command errors gracefully.
        """
        script_content = f'$file = "{file_path}";\n$cert = (Get-AuthenticodeSignature -FilePath $file).SignerCertificate;\nWrite-Host "$file|$($cert.NotAfter)|$($cert.Subject)"'
        remote_script_path = f'C:/Windows/Temp/cert_info_{hash(file_path)}.ps1'
        with tempfile.NamedTemporaryFile(delete=False, suffix='.ps1', mode='w', encoding='utf-8') as tmp_script:
            tmp_script.write(script_content)
            tmp_script_path = tmp_script.name
        self.driver.ssh.send_file(tmp_script_path, remote_script_path)
        os.remove(tmp_script_path)
        result = self.driver.ssh.send_command(f'powershell -ExecutionPolicy Bypass -File "{remote_script_path}"')
        output = result.get('stdout', '') if isinstance(result, dict) else str(result)
        for line in output.splitlines():
            parts = line.strip().split('|')
            if len(parts) == 3:
                file, not_after, subject = parts
                if not_after == '' or not_after.lower() == 'n/a' or subject == '' or subject.lower() == 'n/a':
                    return False
                else:
                    try:
                        try:
                            expiry_dt = datetime.strptime(not_after, '%m/%d/%Y %H:%M:%S')
                        except ValueError:
                            expiry_dt = datetime.strptime(not_after, '%m/%d/%Y %I:%M:%S %p')
                        if expiry_dt < datetime.now():
                            return False
                        else:
                            return True
                    except Exception:
                        return False
        return False