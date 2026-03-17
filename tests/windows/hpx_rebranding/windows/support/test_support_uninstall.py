from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
from SAF.misc import windows_utils
import pytest
import logging

pytest.app_info = "HPX"
class Test_Suite_Uninstall(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.request = request
        cls.driver = windows_test_setup

        cls.logger=logging.getLogger()
        cls.fc = FlowContainer(cls.driver)
        cls.wmi = WmiUtilities(cls.driver.ssh)

        cls.process_util = ProcessUtilities(cls.driver.ssh)
        cls.task_util = TaskUtilities(cls.driver.ssh)
        cls.registry = RegistryUtilities(cls.driver.ssh)

        cls.stack = request.config.getoption("--stack")

    def test_01_hpx_rebranding(self):
        self.fc.close_app()
        self.fc.uninstall_app()
        file_path = '"C:\\Program Files (x86)\\HP\\HPX Support"'
        file_exist = windows_utils.check_path_exist(self.driver.ssh, file_path)
        assert file_exist is False, "'C:\\Program Files (x86)\\HP\\HPX Support' folder still exists"