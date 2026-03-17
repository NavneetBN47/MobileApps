import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("function_setup_to_reset_and_launch_myhp")
class Test_Suite_02_App_Consents_For_China(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.getfixturevalue("class_setup_fixture_ota_regression")
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        request.cls.fc.change_system_region_to_china()
        request.cls.fc.close_and_restart_myhp_app()
        yield
        request.cls.fc.change_system_region_to_united_states()      

    @pytest.mark.regression
    def test_01_verify_manage_choices_page_for_china_C53303871(self):
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_choices_title_for_china()
        assert self.app_consents.verify_your_data_and_privacy_title_china(), "Your data and privacy title is not visible"

    @pytest.mark.regression
    def test_02_verify_back_button_on_manage_choices_consents_for_china_C53303872(self):
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_manage_privacy_back_btn()
        self.app_consents.click_manage_privacy_back_btn()
        self.app_consents.verify_we_value_your_privacy_title()
        assert self.app_consents.verify_manage_choices_btn(), "Manage choices button is not visible"

    @pytest.mark.regression
    def test_03_verify_transfer_consent_for_china_C53303873(self):
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.click_manage_choices_btn()
        assert self.app_consents.verify_data_transfer_consent_for_china(), "Data transfer consent is not visible"

    @pytest.mark.regression
    def test_04_verify_manage_choices_content_for_china_C67872401(self):
        assert self.app_consents.verify_manage_choices_btn(), "Manage choices button is not visible"
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_data_transfer_consent_for_china()
        self.app_consents.verify_product_improvement_btn_for_china()
        self.app_consents.verify_advertising_btn_for_china()
        self.app_consents.verify_advertising_here_link()
        self.app_consents.verify_terms_of_use_link()
        self.app_consents.verify_end_user_license_agreement_link()
        self.app_consents.verify_hp_privacy_statement_link()

    @pytest.mark.regression
    def test_05_verify_manage_choices_consents_toggle_C67872402(self):
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_data_transfer_consent_for_china()
        assert self.app_consents.verify_product_improvement_china_is_enabled() is False, "Product improvement button is clickable"
        assert self.app_consents.verify_advertising_china_is_enabled() is False, "Advertising button is clickable"
        self.app_consents.click_data_transfer_consent_for_china()
        assert self.app_consents.verify_product_improvement_china_is_enabled() is True, "Product improvement button is not clickable"
        assert self.app_consents.verify_advertising_china_is_enabled() is True, "Advertising button is not clickable"

    @pytest.mark.regression
    def test_06_verify_common_consents_screen_on_managed_device_C67872403(self):
        self.app_consents.verify_accept_all_button_show_up()
        self.app_consents.click_accept_all_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.fc.launch_myHP_command()
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up(), "Device details page not loaded"

    @pytest.mark.regression
    def test_07_verify_common_consents_screen_content_for_china_C67872400(self):
        self.app_consents.verify_your_data_and_privacy_title_china()
        self.app_consents.verify_terms_of_use_link()
        self.app_consents.verify_end_user_license_agreement_link()
        self.app_consents.verify_hp_privacy_statement_link()
        self.app_consents.verify_manage_choices_btn()
        assert self.app_consents.verify_accept_all_button_show_up(), "Accept all button is not visible"
        assert self.app_consents.verify_decline_optional_data(), "Decline optional data is not visible"