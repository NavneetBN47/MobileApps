import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
 
@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_02_Application_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_app_only_consents_screen_shown_during_first_use_flow_C53304022(self):
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.verify_close_app_privacy_btn()

    @pytest.mark.regression
    def test_02_verify_continue_button_on_manage_choice_screen_C53304035(self):
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_privacy_continue_btn()
        self.app_consents.click_manage_privacy_continue_btn()
        if self.app_consents.verify_continue_as_guest_button_show_up() is False:
            logging.info("Continue as guest button did not appear")
            raise AssertionError("Continue as guest button is not present when expected")
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        device_name = self.fc.get_windows_system_name()
        logging.info(f"Device Name: '{device_name}'")
        self.devicesMFE.verify_sign_in_button_show_up()
        self.devicesMFE.verify_bell_icon_show_up()
