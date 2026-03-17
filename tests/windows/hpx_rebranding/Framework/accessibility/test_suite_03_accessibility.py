import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression")
class Test_Suite_01_Accessibility(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.profile= request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.accessibility = request.cls.fc.fd["accessibility"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]

    @pytest.mark.regression
    def test_01_hp_app_appears_in_windows_task_manager_C61083683(self):
        self.fc.launch_myHP_and_skip_fuf()
        self.accessibility.open_app_from_start_menu("Task Manager", open_app=True)
        assert self.accessibility.verify_hp_app_icon_in_windows_settings(), "HP app icon not present in Windows Task Manager"
        self.profile.title_bar_close_myhp()

    @pytest.mark.regression
    def test_02_hp_app_name_in_windows_taskbar_C60030453(self):
        self.fc.launch_myHP_and_skip_fuf()
        self.accessibility.verify_myhp_app_icon_on_taskbar()
        hpicon = self.driver.find_object("myhp_app_icon_on_taskbar")
        self.driver.click_by_coordinates(hpicon, right_click=True)
        assert self.accessibility.verify_hp_app_icon_in_windows_settings(), "HP app icon not present in Windows Taskbar context menu"