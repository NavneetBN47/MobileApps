import pytest
from MobileApps.libs.flows.android.hpx.flow_container import FLOW_NAMES

pytest.app_info = "HPX"

@pytest.mark.usefixtures("function_setup_terminate_relaunch_hpx")
class Test_Suite_03_Camera_Scan(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, android_hpx_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_hpx_setup
        # cls.p = load_printers_session
        # cls.printer_ip=cls.p.get_printer_information()["ip address"]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.HPX_CAMERA_SCAN]
        cls.hpx_home = cls.fc.fd[FLOW_NAMES.HPX_HOME]
        
        yield
        cls.fc.kill_hpx_app()
        cls.fc.kill_chrome()

    @pytest.mark.regression
    def test_01_tap_x_button_on_camera_scan_screen_C44018896(self):
        self.hpx_home.click_camera_scan_tile()
        self.camera_scan.click_x_button_on_camera_scan()
        assert self.hpx_home.verify_homepage_bottom_devices_btn(), "Home page not loaded/delay in loading homepage"
        assert self.hpx_home.verify_homepage_bottom_shop_btn(), "Home page not loaded/delay in loading homepage"
        assert self.hpx_home.verify_camera_scan_tile(raise_e=False) == True, "Home page not loaded after clicking x button on camera scan"
