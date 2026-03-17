import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_01_App_Consents_For_US(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        cls.css = request.cls.fc.fd["css"]
        cls.app_consents = request.cls.fc.fd["app_consents"]
        cls.device_card = request.cls.fc.fd["device_card"]
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.regression
    def test_01_verify_common_consents_screen_C53303850(self):
        assert self.app_consents.verify_we_value_your_privacy_title(), "We value your privacy title not visible"

    @pytest.mark.regression
    def test_02_verify_common_consents_screen_content_for_us_C53303851(self):
        self.app_consents.verify_we_value_your_privacy_title()
        assert self.app_consents.verify_terms_of_use_link(), "Terms of use link is not visible"
        assert self.app_consents.verify_end_user_license_agreement_link(), "End user license agreement link is not visible"
        assert self.app_consents.verify_hp_privacy_statement_link(), "HP Privacy statement link is not visible"
        assert self.app_consents.verify_manage_choices_btn(), "Manage choices button is not visible "
        assert self.app_consents.verify_accept_all_button_show_up(), "Accept all button is not visible"
        assert self.app_consents.verify_decline_optional_data(), "Decline optional data is not visible"

    @pytest.mark.regression
    def test_03_verify_manage_options_contents_on_consents_page_for_us_C53303852(self):
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.click_manage_choices_btn()
        assert self.app_consents.verify_product_improvement_btn(), "Product improvement button is not visible"
        assert self.app_consents.verify_adverstising_btn(), "Advertising button is not visible"

    @pytest.mark.regression
    def test_04_verify_manage_choices_content_for_us_C53303853(self):
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.click_manage_choices_btn()
        assert self.app_consents.verify_manage_choices_title(), "Manage choices title is not visible"
        self.app_consents.verify_product_improvement_btn()
        assert self.app_consents.verify_adverstising_btn(), "Advertising button is not visible"
        assert self.app_consents.verify_advertising_here_link(), "Advertising here link not visible"
        self.app_consents.verify_end_user_license_agreement_link()
        self.app_consents.verify_hp_privacy_statement_link()
        self.app_consents.verify_manage_choices_title()

    @pytest.mark.regression
    def test_05_verify_back_btn_on_manage_choices_for_us_C67872397(self):
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.click_manage_choices_btn()
        assert self.app_consents.verify_manage_privacy_back_btn(), "Manage privacy back button is not visible"
        self.app_consents.click_manage_privacy_back_btn()
        self.app_consents.verify_we_value_your_privacy_title()
        self.app_consents.verify_manage_choices_title()

    @pytest.mark.regression
    def test_06_verify_decline_optional_data_for_us_C53303855(self):
        self.app_consents.verify_decline_optional_data()
        self.app_consents.click_decline_optional_data_button()
        if self.app_consents.verify_continue_as_guest_button_show_up() is not False:
            self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up(), "Device details page not loaded"

    @pytest.mark.regression
    def test_07_verify_common_consents_are_shown_if_already_set_C53303857(self):
        self.app_consents.verify_accept_all_button_show_up()
        self.app_consents.click_accept_all_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        self.app_consents.click_continue_as_guest_button()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.fc.close_myHP()
        self.fc.launch_myHP_command()
        self.css.maximize_hp()
        assert self.device_card.verify_bell_icon_present(), "Bell icon is not present on device card"

    @pytest.mark.regression
    def test_08_verify_accept_all_btn_on_consent_page_for_us_C53303861(self):
        assert self.app_consents.verify_accept_all_button_show_up(), "Accept all button is not visible"

    @pytest.mark.regression
    def test_09_verify_continue_btn_on_manage_choices_screen_C53303859(self):
        self.app_consents.verify_accept_all_button_show_up()
        self.app_consents.verify_manage_choices_btn()
        self.app_consents.click_manage_choices_btn()
        self.app_consents.verify_product_improvement_btn()
        self.app_consents.verify_adverstising_btn()
        assert self.app_consents.verify_manage_privacy_continue_btn(), "Manage privacy continue button is not visible"

    @pytest.mark.regression
    def test_10_verify_hp_logo_in_welcome_page_C59423353(self):
        self.app_consents.verify_accept_all_button_show_up()
        self.app_consents.click_accept_all_button()
        self.app_consents.verify_continue_as_guest_button_show_up()
        assert self.profile.verify_myhp_logo(), "Window title does not display 'HP' in opened module"