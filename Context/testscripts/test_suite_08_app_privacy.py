import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_08_App_Privacy(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_verify_no_consents_screen_managed_device_C67874089(self):
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=True)
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Accepted   ")
        self.fc.consent_allow_product_enhancement(self.driver.ssh, condition="Rejected")
        self.fc.consent_allow_support(self.driver.ssh,condition="Accepted")
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_accept_all_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=False)

    @pytest.mark.regression
    def test_02_verify_consents_displayed_when_not_preselected_C67874090(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.app_consents.verify_app_and_device_common_consents_screen()
        self.app_consents.verify_app_only_consents_screen()

    @pytest.mark.regression
    def test_03_verify_consents_page_shown_on_relaunch_C67874091(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.app_consents.verify_app_and_device_common_consents_screen()
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_screen()
        self.profile.click_close_hpx_btn()
        self.fc.launch_myHP_command()
        self.app_consents.verify_app_and_device_common_consents_screen()
        self.app_consents.verify_app_only_consents_screen()

    @pytest.mark.regression
    def test_04_verify_necessary_notice_first_use_flow_C67874092(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.app_consents.verify_app_and_device_common_consents_screen()
        self.app_consents.verify_app_only_consents_screen()
        self.app_consents.verify_necessary_text_from_app_and_device_consents_screen()
