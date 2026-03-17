import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_03_Welcome_Screen(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.web_driver = utility_web_session
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]

    @pytest.mark.regression
    def test_01_verify_the_window_title_displays_hp_C60030507(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        assert self.profile.verify_myhp_logo(), "Window title does not display 'HP' in opened module"
        assert self.devices_details_pc_mfe.click_energy_consumption_card(), "Unable to click Energy Consumption card"
        assert self.profile.verify_myhp_logo(), "Window title does not display 'HP' in opened module"

        
