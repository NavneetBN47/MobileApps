from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest
import time
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_PC_Connect(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.fc.launch_myHP()


    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_platform(["london"])
    def test_01_verify_5g_status_disconnect_C36256474(self):
        time.sleep(3)
        self.fc.restart_myHP()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_5G_module()

        if self.fc.fd["pc_connect"].get_toggle_notification_state()=="1":       
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()

        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        assert self.fc.fd["devices"].get_cellular_text() == "5G Disconnected"

    
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.require_platform(["london"])
    def test_01_verify_5g_status_connect_C36256473(self):
        time.sleep(3)
        self.fc.restart_myHP()

        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_5G_module()
        if self.fc.fd["pc_connect"].get_toggle_notification_state()=="0":       
            self.fc.fd["pc_connect"].click_toggle_5G_connectivity()

        time.sleep(2)
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        time.sleep(2)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert self.fc.fd["devices"].get_cellular_text() == "5G Connected"
