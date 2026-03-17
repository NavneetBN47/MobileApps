import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
 
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_02_Accessibility(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.app_consents = request.cls.fc.fd["app_consents"]
 
    @pytest.mark.regression
    def test_01_verify_app_name_displays_as_hp_C53533726(self):
        self.app_consents.click_accept_all_button()
        assert self.app_consents.verify_hp_logo(), "HP logo is not displayed"
        assert self.app_consents.verify_continue_as_guest_button_show_up(), "Continue as Guest button is not displayed"