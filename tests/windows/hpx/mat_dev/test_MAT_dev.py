import time
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from SAF.misc import saf_misc
import pytest

pytest.app_info = "HPX"
class Test_Suite_MAT_DEV(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup 
        cls.fc = FlowContainer(cls.driver)
        cls.request = request
    
    def test_01_close_app(self, install_app):
        self.fc.close_app()
        time.sleep(5)
        self.fc.launch_app()
        time.sleep(15)
        self.fc.fd["navigation_panel"].click_close_btn()
        is_open = self.fc.is_app_open()
        assert is_open == False
    
    def test_02_navigation(self):
        is_open = self.fc.is_app_open()
        if is_open == False:
            self.fc.launch_app()
            time.sleep(15)
        self.fc.fd["navigation_panel"].navigate_to_settings()
        settings_header_display = self.fc.fd["settings"].verify_settings_header()
        assert settings_header_display == "Settings"
        self.fc.fd["navigation_panel"].click_hamburger_navigation()
        self.fc.fd["navigation_panel"].navigate_to_devices()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        pcdevice_header_display = self.fc.fd["devices"].verify_actions_header()
        assert pcdevice_header_display is not False
