from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.wmi_utilities import WmiUtilities
from MobileApps.libs.flows.windows.hpx.utility.process_utilities import ProcessUtilities
from MobileApps.libs.flows.windows.hpx.utility.task_utilities import TaskUtilities
from MobileApps.libs.flows.windows.hpx.utility.registry_utilities import RegistryUtilities
import pytest
import logging

pytest.app_info = "HPX"
class Test_Suite_Upgrade(object):
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
        self.__reinstall_HPX()
        self.__upgrade_HPX()
        self.fc.select_device()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __reinstall_HPX(self):
        self.fc.uninstall_app()
        self.fc.remove_file("C:/Users/exec/AppData/Local/Packages/AD2F1837.myHP_v10z8vjag6ke6")
        self.fc.remove_file("C:/Program Files (x86)/HP/HPX Support")
        if self.request.config.getoption("--app-update") is not None:
            local_build = self.request.config.getoption("--app-update")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(local_build)
            else:
                self.fc.install_app(local_build)  

    def __upgrade_HPX(self):
        if self.request.config.getoption("--local-build") is not None:
            upgrade_before_ver = self.request.config.getoption("--local-build")
            if self.request.config.getoption("--appbundle-install") is not None:
                self.fc.install_bundle(upgrade_before_ver)
            else:
                self.fc.install_app(upgrade_before_ver)

    def __start_HPX(self):
        self.fc.restart_app()
        self.fc.maximize_window()
        if self.fc.fd["hpx_fuf"].verify_accept_all_button_show_up():
            self.fc.fd["hpx_fuf"].click_accept_all_button()
        if self.fc.fd["hpx_fuf"].verify_continue_as_guest_button_show_up():
            self.fc.fd["hpx_fuf"].click_continue_as_guest_button()
        if self.fc.fd["hpx_fuf"].verify_what_is_this_dialog_show():
            self.fc.fd["hpx_fuf"].click_what_is_new_skip_button()

    def __select_device(self):
        self.__start_HPX()
        if self.stack not in ["dev", "itg"]:
            self.fc.fd["devicesMFE"].click_device_card_by_index()