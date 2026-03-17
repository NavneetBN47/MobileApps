import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_03_App_Consents(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.devicesMFE = cls.fc.fd["devicesMFE"]
        yield
        request.cls.fc.app_managed_registry_key(request.cls.driver.ssh, condition=False)
        request.cls.fc.consent_managed_registry_key(request.cls.driver.ssh, condition=False)


    @pytest.mark.regression
    def test_01_verify_device_consents_not_dispalyed_once_set_C53303858(self):
        self.app_consents.verify_accept_all_button_show_up()
        self.app_consents.click_accept_all_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.fc.close_myHP()
        self.fc.launch_myHP_command()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"

    @pytest.mark.regression
    def test_02_verify_manage_choices_content_other_than_us_and_china_C53303865(self):
        self.fc.change_system_region_to_india()
        self.app_consents.verify_accept_all_button_show_up()
        assert self.app_consents.verify_manage_choices_btn(), "Manage choices button is not visible"
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_your_data_and_privacy_title()
        self.app_consents.verify_product_improvement_btn()
        assert self.app_consents.verify_adverstising_btn(), "Advertising button is not visible"
        self.app_consents.verify_advertising_here_link()

    @pytest.mark.regression
    def test_03_verify_manage_choices_page_C67872398(self):
        assert self.app_consents.verify_manage_choices_btn(), "Manage choices button is not visible"
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_your_data_and_privacy_title()
        self.app_consents.verify_product_improvement_btn()
        assert self.app_consents.verify_adverstising_btn(), "Advertising button is not visible"
        self.app_consents.verify_terms_of_use_link()
        self.app_consents.verify_end_user_license_agreement_link()
        self.app_consents.verify_hp_privacy_statement_link()

    @pytest.mark.regression
    def test_04_verify_declining_optional_data_on_consents_page_C67872399(self):
        self.app_consents.verify_accept_all_button_show_up()
        assert self.app_consents.verify_decline_optional_data(), "Decline optional data is not visible"
        self.app_consents.click_decline_optional_data_button()

    @pytest.mark.regression
    def test_05_verify_common_consents_is_shown_on_re_launch_if_not_set_C53303877(self):
        assert self.app_consents.verify_accept_all_button_show_up(), "Accept all button is not visible"
        self.app_consents.verify_decline_optional_data()
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.click_manage_choices_btn()
        self.fc.close_myHP()
        self.fc.launch_myHP_command()
        self.app_consents.verify_accept_all_button_show_up()
        assert self.app_consents.verify_decline_optional_data(), "Decline optional data is not visible"
        assert self.app_consents.verify_manage_choices_btn(), "Manage choices button is not visible"

    @pytest.mark.regression
    def test_06_verify_app_consents_not_shown_on_managed_devices_C60498993(self):
        self.fc.consent_allow_marketing(self.driver.ssh, condition="Unknown")
        self.fc.consent_managed_registry_key(self.driver.ssh, condition=False)
        self.fc.app_managed_registry_key(self.driver.ssh, condition=True)
        self.fc.restart_myHP()
        assert self.devicesMFE.verify_device_card_show_up(), "Device card is not displayed"

