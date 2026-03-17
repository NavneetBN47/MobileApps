import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "ECP"

@pytest.mark.skip
class Test_08_ECP_My_Organization(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.my_organization = self.fc.fd["my_organization"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_my_organization(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_user_icon_top_right()
        self.my_organization.click_my_organization_link()
        self.my_organization.verify_my_organization_page_title()
        return self.home.click_user_icon_top_right()

    def test_01_verify_my_organization_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31448108
        self.my_organization.verify_page_title(page_title="My Organization")
        self.my_organization.verify_my_organization_filter_button()
        # self.my_organization.verify_my_organization_settings_button()
        self.my_organization.verify_my_organization_column_option_gear()

    def test_02_verify_my_organization_paginations(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31448113
        self.my_organization.verify_all_page_size_options_new([25, 50, 75, 100])
        self.my_organization.verify_table_displaying_correctly_new(25, page=1)
        self.my_organization.verify_table_displaying_correctly_new(50, page=1)
        self.my_organization.verify_table_displaying_correctly_new(75, page=1)
        self.my_organization.verify_table_displaying_correctly_new(100, page=1)

    @pytest.mark.parametrize('column_option', ["User Name","Email Address","Status","Role"])
    def test_03_validate_column_option_functionality(self,column_option):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31684215
        self.my_organization.click_my_organization_column_option_gear()
        self.my_organization.click_column_option(column_option)
        self.my_organization.click_column_options_popup_save_button()

        # Verify Organization table Domain Column
        self.my_organization.verify_my_organization_tabel_column(column_option,displayed=False)

        # Reverting the Column option changes
        self.my_organization.click_my_organization_column_option_gear()
        self.my_organization.click_column_option(column_option)
        self.my_organization.click_column_options_popup_save_button()
        self.my_organization.verify_my_organization_tabel_column(column_option)
    
    def test_04_verify_my_organization_details(self):
        #https://hp-testrail.external.hp.com/index.php?/tests/view/692849579
        organization_details=self.my_organization.get_organization_table_entry_details()
        self.my_organization.click_organization_name()
        assert organization_details == self.my_organization.get_organization_details()
        self.my_organization.verify_my_organization_details_personal_info_card()
        self.my_organization.verify_my_organization_details_organization_info_card()

    # IDP Settings is temporarily disabled, So Commenting IDP Settings related testcases
    # def test_05_verify_my_organization_idp_settings_screen_ui(self):
    #     # https://hp-testrail.external.hp.com/index.php?/tests/view/692849587
    #     self.my_organization.click_my_organization_settings_button()

    #     #verify settings screen
    #     self.my_organization.verify_page_title(page_title="Settings")
    #     self.my_organization.verify_settings_identity_providers_dropdown()
    #     self.my_organization.verify_settings_domain_field()
    
    # def test_06_verify_my_organization_idp_settings_identity_provider_dropdown_options(self):
    #     #
    #     idp_options=["HP","Google","Azure"]
    #     self.my_organization.click_my_organization_settings_button()

    #     #verify identity providers dropdown options
    #     assert idp_options == self.my_organization.get_settings_idp_dropdown_options()

    # Disabling the IDP Tests for now, will resume them once we get our IDP configuration
    # def test_07_verify_my_organization_idp_settings_end_to_end_functionality(self):
    #     # https://hp-testrail.external.hp.com/index.php?/tests/view/692849587
    #     self.my_organization.click_my_organization_settings_button()

    #     current_idp=self.my_organization.get_settings_current_idp_value()
    #     current_domain=self.my_organization.get_settings_current_domain_value()

    #     # Updating IDP Settings
    #     self.my_organization.change_settings_idp_value(current_idp)
    #     self.my_organization.enter_domain_name("company.com")
    #     self.my_organization.click_settings_contextual_footer_save_button()
    #     self.my_organization.check_toast_successful_message("Your changes have been saved.")

    #     # Verify the updated idp settings
    #     assert current_idp != self.my_organization.get_settings_current_idp_value()
    #     assert current_domain != self.my_organization.get_settings_current_domain_value()

    #     # Reverting IDP Settings 
    #     self.my_organization.select_settings_idp_dropdown_option(current_idp)
    #     self.my_organization.enter_domain_name(current_domain.split("@")[1])
    #     self.my_organization.dismiss_toast()
    #     self.my_organization.click_settings_contextual_footer_save_button()
    #     self.my_organization.check_toast_successful_message("Your changes have been saved.")