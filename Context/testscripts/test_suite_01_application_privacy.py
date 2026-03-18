import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
 
pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_01_Application_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.css = request.cls.fc.fd["css"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.device_card = request.cls.fc.fd["device_card"]
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_app_only_consents_screen_shown_if_app_consents_are_not_set_C53304023(self):
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_close_app_privacy_btn()
        self.app_consents.click_close_app_privacy_btn()
        self.fc.reset_myHP_app_through_command(launch_app=True)
        self.css.maximize_hp()
        self.app_consents.verify_app_only_consents_screen()

    @pytest.mark.regression
    def test_02_app_only_consents_screen_is_not_shown_if_app_consents_already_set_C53304024(self):
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_accept_all_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.profile.click_close_hpx_btn()
        self.fc.launch_myHP_command()
        self.css.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"

    @pytest.mark.regression
    def test_03_verify_necessary_notice_displays_C53304028(self):
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen"

    @pytest.mark.regression
    def test_04_validate_app_only_consents_screen_content_for_US_C53304029(self):
        self.app_consents.verify_your_data_and_privacy_title()
        self.app_consents.verify_app_only_consents_screen()
        assert self.app_consents.verify_necessary_text(), "Failed to verify necessary text in app consent screen for US region"

    @pytest.mark.regression
    def test_05_app_only_consents_screen_not_displayed_on_managed_device_C67872404(self):
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=True)
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_accept_all_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.device_card.verify_bell_icon_present(), "Bell icon is not present on device card"
        device_name = self.fc.get_windows_system_name()
        logging.info(f"Device Name: '{device_name}'")
        self.devicesMFE.verify_sign_in_button_show_up()
        self.devicesMFE.verify_bell_icon_show_up()

    @pytest.mark.regression
    def test_06_app_only_consents_screen_displayed_on_unmanaged_device_C67872405(self):
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=False)
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.verify_necessary_text()
