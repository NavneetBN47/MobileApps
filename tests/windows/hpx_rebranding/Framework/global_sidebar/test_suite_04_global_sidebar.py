import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import HPX_ACCOUNT
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_myhp_launch")
class Test_Suite_04_Global_Sidebar(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.web_driver = utility_web_session
        request.cls.profile = cls.fc.fd["profile"]
        request.cls.hpx_support = cls.fc.fd["hpx_support"]
        request.cls.fc.web_password_credential_delete()
        yield
        if request.config.getoption("--ota-test") is not None:
            request.cls.fc.uninstall_app()

    @pytest.mark.regression
    def test_01_verify_open_hp_smart_external_browser_C61716544(self):
        self.profile.click_add_device_button()
        self.profile.click_smart_app_link()
        assert self.hpx_support.verify_browser_pane(), "Browser pane not opened after clicking HP Smart link"
        actual_tab_name = self.hpx_support.get_browser_tab_name()
        print(f"Actual Browser tab name: {actual_tab_name}")
        expected_tab_name = "HP Smart | Microsoft Store"
        print(f"expected text in tab name: {expected_tab_name}")
        assert expected_tab_name in actual_tab_name, f"Expected tab name: {expected_tab_name}, but got: {actual_tab_name}"
 
 