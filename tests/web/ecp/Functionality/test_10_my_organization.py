import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "ECP"
@pytest.mark.skip
class Test_10_ECP_My_Organization(object):

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

    def test_01_verify_my_organization_refresh_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31684218
        cur_time = self.my_organization.get_sync_time_info()
        sleep(1)
        self.my_organization.click_refresh_button()
        new_time = self.my_organization.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1].replace("&nbsp;", " "), self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time
    
    def test_02_verify_my_organization_invalid_search_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31448109
        self.my_organization.search_user("invaliduser",raise_e=False)

    def test_03_verify_my_organization_search_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31448109
        self.my_organization.search_user(self.hpid_username)

    def test_04_verify_column_option_popup_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31684216
        self.my_organization.click_my_organization_column_option_gear()
        self.my_organization.click_column_option("Role")
        self.my_organization.click_column_options_popup_cancel_button()

        # Verify Organization table Domain Column
        self.my_organization.verify_my_organization_tabel_column("ROLE")

    @pytest.mark.parametrize('filter_name', ["Active","Expired","Pending","Admin","Technician"])
    def test_05_verify_filter_functionality(self,filter_name):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31448715
        self.my_organization.click_my_organization_filter_button()
        self.my_organization.select_filter(filter_name)
        self.my_organization.verify_filter_in_my_organization_table(filter_name)

    # IDP Settings is temporarily disabled, So Commenting IDP Settings related testcases
    # def test_06_verify_my_organization_idp_settings_contextual_footer(self):
    #     #
    #     self.my_organization.click_my_organization_settings_button()

    #     current_idp=self.my_organization.get_settings_current_idp_value()
    #     self.my_organization.change_settings_idp_value(current_idp)
       
    #     # Verify contextual footer
    #     self.my_organization.verify_settings_contextual_footer()
    #     self.my_organization.verify_settings_contextual_footer_cancel_button()
    #     self.my_organization.verify_settings_contextual_footer_save_button()
    #     self.my_organization.click_settings_contextual_footer_cancel_button()

    # def test_07_validate_domain_field_in_idp_settings_screen(self):
    #     #
    #     self.my_organization.click_my_organization_settings_button()
        
    #     # Verify Domain field error message
    #     self.my_organization.verify_settings_domain_field()
    #     self.my_organization.clear_settings_domain_field()
    #     self.my_organization.verify_settings_domain_field_error_message()
    #     self.my_organization.enter_domain_name("invalid")
    #     self.my_organization.verify_settings_invalid_domain_error_message()

    # def test_08_verify_my_organization_idp_settings_contextual_footer_save_button_functionality(self):
    #     #
    #     self.my_organization.click_my_organization_settings_button()

    #     current_idp=self.my_organization.get_settings_current_idp_value()
    #     self.my_organization.change_settings_idp_value(current_idp)

    #     #Verify Save Button
    #     self.my_organization.verify_settings_contextual_footer_save_button_status("disabled")
    #     self.my_organization.enter_domain_name("gmail.com")
    #     self.my_organization.verify_settings_contextual_footer_save_button_status("enabled")
  
    # def test_09_verify_my_organization_idp_settings_contextual_footer_cancel_button_functionality(self):
    #     #
    #     self.my_organization.click_my_organization_settings_button()
    #     current_idp=self.my_organization.get_settings_current_idp_value()

    #     # Updating IDP Settings
    #     self.my_organization.change_settings_idp_value(current_idp)
    #     self.my_organization.enter_domain_name("company.com")
    #     self.my_organization.click_settings_contextual_footer_cancel_button()

    #     # Verify Settings Not Saved Popup
    #     self.my_organization.verify_settings_not_saved_popup_title()
    #     self.my_organization.verify_settings_not_saved_popup_desc()
    #     self.my_organization.verify_settings_not_saved_popup_cancel_button()
    #     self.my_organization.verify_settings_not_saved_popup_leave_button()

    # def test_10_verify_settings_not_saved_popup_cancel_button_functionality(self):
    #     #
    #     self.my_organization.click_my_organization_settings_button()
    #     current_idp=self.my_organization.get_settings_current_idp_value()

    #     # Updating IDP Settings
    #     self.my_organization.change_settings_idp_value(current_idp)
    #     self.my_organization.enter_domain_name("company.com")
    #     self.my_organization.click_settings_contextual_footer_cancel_button()

    #     # Click Settings not saved Cancel Button
    #     self.my_organization.click_settings_not_saved_popup_cancel_button()

    #     # Verify Settings screen is displayed
    #     self.my_organization.verify_page_title(page_title="Settings")

    # def test_11_verify_settings_not_saved_popup_leave_button_functionality(self):
    #     #
    #     self.my_organization.click_my_organization_settings_button()
    #     current_idp=self.my_organization.get_settings_current_idp_value()

    #     # Updating IDP Settings
    #     self.my_organization.change_settings_idp_value(current_idp)
    #     self.my_organization.enter_domain_name("company.com")
    #     self.my_organization.click_settings_contextual_footer_cancel_button()

    #     # Click Settings not saved Leave Button
    #     self.my_organization.click_settings_not_saved_popup_leave_button()

    #     # Verify Organization screen is displayed
    #     self.my_organization.verify_page_title(page_title="My Organization")