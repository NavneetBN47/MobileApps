import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_myhp_launch")
class Test_Suite_01_Settings_General(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile = request.cls.fc.fd["profile"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]

    @pytest.mark.regression
    def test_01_verify_settings_option_is_available_in_global_side_bar_C58769223(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_subscriptions_link(), "Subscriptions link missing"
        assert self.profile.verify_support_device_btn(), "Support device button missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"

    @pytest.mark.regression
    def test_02_verify_menu_button_navigates_back_to_global_sidebar_C58769231(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_support_device_btn(), "Support device button missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_menu_back_btn_from_settings(), "menu back button in settings missing"
        self.hpx_settings.click_menu_back_btn_from_settings()
        assert self.profile.verify_profile_settings_btn(), "settings button invisible" 

    @pytest.mark.regression
    def test_03_verify_settings_button_present_in_manage_privacy_settings_page_C59395805(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_subscriptions_link(), "Subscriptions link missing"
        assert self.profile.verify_support_device_btn(), "Support device button missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_settings_side_panel(), "Settings side panel missing"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_manage_privacy_settings_page(), "Manage privacy settings page missing"
        assert self.hpx_settings.verify_manage_privacy_settings_back_btn(), "Manage privacy settings back button missing"

    @pytest.mark.regression
    def test_04_verify_back_button_present_in_the_computer_privacy_page_C59395806(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_subscriptions_link(), "Subscriptions link missing"
        assert self.profile.verify_support_device_btn(), "Support device button missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_settings_side_panel(), "Settings side panel missing"
        assert self.hpx_settings.verify_manage_privacy_btn(), "Manage privacy button missing"
        self.hpx_settings.click_manage_privacy_btn()
        assert self.hpx_settings.verify_manage_privacy_settings_page(), "Manage privacy settings page missing"
        self.hpx_settings.click_device_privacy_btn()
        assert self.hpx_settings.verify_device_privacy_consents(), "Device privacy consents missing"

    @pytest.mark.regression
    def test_05_verify_settings_page_content_matches_figma_design_C58769237(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_subscriptions_link(), "Subscriptions link missing"
        assert self.profile.verify_support_device_btn(), "Support device button missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_setting_page_content(), "Settings page content missing"

    @pytest.mark.regression
    def test_06_verify_the_copyright_description_in_setting_page_C59395790(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_subscriptions_link(), "Subscriptions link missing"
        assert self.profile.verify_support_device_btn(), "Support device button missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_setting_page_content(), "Settings page content missing"
        assert self.hpx_settings.verify_copyright_description_text(), "Copyrights text missing in settings page"

    @pytest.mark.regression
    def test_07_verify_arrow_icon_and_link_icons_are_present_in_settings_page_C59395804(self):
        assert self.devicesMFE.verify_profile_icon_show_up(), "Profile icon missing"
        self.devicesMFE.click_profile_button()
        assert self.profile.verify_sign_in_from_avatar_sideflyout(), "Sign in link missing"
        assert self.profile.verify_subscriptions_link(), "Subscriptions link missing"
        assert self.profile.verify_support_device_btn(), "Support device button missing"
        assert self.profile.verify_profile_settings_btn(), "settings button invisible"
        self.profile.click_profile_settings_btn()
        assert self.hpx_settings.verify_menu_back_btn_from_settings(), "menu back button in settings missing"
        assert self.hpx_settings.verify_manage_privacy_btn(), "manage privacy settings button missing"
        assert self.hpx_settings.verify_privacy_statement_link(), "HP privacy statement link missing"
        assert self.hpx_settings.verify_terms_of_use(), "Terms of use link missing"
        assert self.hpx_settings.verify_about_user_license_agreement(), "About user license agreement link missing"

    @pytest.mark.regression
    def test_08_verify_copied_app_instance_id_is_correct_and_is_a_10_digit_number_C61712873(self):
        self.profile.navigate_to_settings_from_home()
        self.hpx_settings.verify_app_instance_id()
        app_id_from_hpx_settings = self.hpx_settings.get_app_instance_id().lower()
        app_id_from_db_file = self.fc.get_app_instance_id()
        assert app_id_from_hpx_settings == app_id_from_db_file[:10], "App Instance ID from HPX Settings does not match with the one from AsyncStorage.db file"

    @pytest.mark.regression
    def test_09_verify_copied_version_number_matches_actual_app_version_C61662869(self):
        self.profile.navigate_to_settings_from_home()
        app_version = self.hpx_settings.get_app_version_copy_btn()
        instaled_app_path = self.fc.get_installed_app_path()
        assert app_version in instaled_app_path, "App Version from HPX Settings does not match with the installed app version"

    @pytest.mark.regression
    def test_10_keyboard_dismiss_alt_f4_C53304122(self):
        self.devicesMFE.verify_profile_icon_show_up()
        self.fc.close_hp_app_using_alt_f4()
        assert self.fc.fd["audio"].verify_global_icon_show_up() is False, "global icon is displayed since app is not be closed by ALT+F4"
