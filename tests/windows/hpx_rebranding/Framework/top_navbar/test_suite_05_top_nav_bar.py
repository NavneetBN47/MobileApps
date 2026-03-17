import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
 
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_clear_sign_out")
class Test_Suite_05_Top_Nav_Bar(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()
 
    @pytest.mark.regression
    def test_01_verify_shop_icon_functionality_C66678139(self):
        assert self.devicesMFE.verify_shop_icon_show_up(), "Shop icon is not present"
        self.devicesMFE.click_shop_icon()
        assert self.devicesMFE.verify_shop_icon_preview(), "Shop icon preview is not correct"

    @pytest.mark.regression
    def test_02_device_back_button_functionality_C53304005(self):
        self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up()
        self.devices_details_pc_mfe.click_back_devices_button()
        assert self.devicesMFE.verify_device_card_show_up(), "Devices card is not present"
       
        
 