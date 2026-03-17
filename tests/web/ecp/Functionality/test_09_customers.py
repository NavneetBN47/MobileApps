import pytest
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

@pytest.mark.skip
class Test_09_Customers(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.customers = self.fc.fd["customers"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_customers(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_customers_menu_btn()
        return self.customers.verify_customers_page()

    def test_01_verify_customer_details(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30455284

        # Verify and wait for customers table data to load
        self.customers.verify_customers_table_data_load()
        customer_details=self.customers.get_customer_table_entry_details()
        self.customers.click_customer_name()
        assert customer_details == self.customers.get_customer_details()

    # IDP Settings is temporarily disabled, So Commenting IDP Settings related testcases
    # def test_02_validate_domain_field_in_idp_settings_screen(self):
    #     # 

    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()

    #     self.customers.click_customer_checkbox()
    #     self.customers.click_contextual_footer_select_action_dropdown()
    #     self.customers.select_contextual_footer_set_idp_option()
    #     self.customers.click_contextual_footer_continue_button()
       
    #     # Verify Domain field error message
    #     self.customers.verify_settings_domain_field()
    #     self.customers.clear_settings_domain_field()
    #     self.customers.verify_settings_domain_field_error_message()
    #     self.customers.enter_domain_name("invalid")
    #     self.customers.verify_settings_invalid_domain_error_message()

    # def test_03_verify_customers_idp_settings_contextual_footer_save_button_functionality(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30455303

    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()
        
    #     self.customers.click_customer_checkbox()
    #     self.customers.click_contextual_footer_select_action_dropdown()
    #     self.customers.select_contextual_footer_set_idp_option()
    #     self.customers.click_contextual_footer_continue_button()

    #     current_idp=self.customers.get_settings_current_idp_value()
    #     self.customers.change_settings_idp_value(current_idp)

    #     #Verify Save Button
    #     self.customers.verify_settings_contextual_footer_save_button_status("disabled")
    #     self.customers.enter_domain_name("gmail.com")
    #     self.customers.verify_settings_contextual_footer_save_button_status("enabled")

    # Disabling the IDP Tests for now, will resume them once we get our IDP configuration
    # def test_04_verify_customer_idp_settings_end_to_end_unctionality(self):
    #     # 

    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()
        
    #     self.customers.click_customer_checkbox()
    #     self.customers.click_contextual_footer_select_action_dropdown()
    #     self.customers.select_contextual_footer_set_idp_option()
    #     self.customers.click_contextual_footer_continue_button()

    #     current_idp=self.customers.get_settings_current_idp_value()
    #     current_domain=self.customers.get_settings_current_domain_value()

    #     # Updating IDP Settings
    #     self.customers.change_settings_idp_value(current_idp)
    #     self.customers.enter_domain_name("company.com")
    #     self.customers.click_settings_contextual_footer_save_button()
    #     self.customers.verify_settings_toast_message()

    #     # Verify the updated idp settings
    #     assert current_idp != self.customers.get_settings_current_idp_value()
    #     assert current_domain != self.customers.get_settings_current_domain_value()

    #     # Reverting IDP Settings 
    #     self.customers.select_settings_idp_dropdown_option(current_idp)
    #     self.customers.enter_domain_name(current_domain.split("@")[1])
    #     self.customers.dismiss_toast()
    #     self.customers.click_settings_contextual_footer_save_button()
    #     self.customers.verify_settings_toast_message()

    def test_05_verify_column_option_popup_save_button_functionality(self):
        # 

        self.customers.click_customers_column_option_settings_gear_button()
        self.customers.click_column_option("COUNTRY/REGION")
        self.customers.click_column_options_popup_save_button()

        # Verify Customers table Domain Column
        self.customers.verify_customers_tabel_column("COUNTRY/REGION",displayed=False)

        # Reverting the Column option changes
        self.customers.click_customers_column_option_settings_gear_button()
        self.customers.click_column_option("COUNTRY/REGION")
        self.customers.click_column_options_popup_save_button()
        self.customers.verify_customers_tabel_column("COUNTRY/REGION")

    def test_06_verify_column_option_popup_cancel_button_functionality(self):
        # 

        self.customers.click_customers_column_option_settings_gear_button()
        self.customers.click_column_option("COUNTRY/REGION")
        self.customers.click_column_options_popup_cancel_button()

        # Verify Customers table Domain Column
        self.customers.verify_customers_tabel_column("COUNTRY/REGION")

    # Disabling the IDP Tests for now, will resume them once we get our IDP configuration
    # def test_07_verify_customer_details_settings_button_end_to_end_functionality(self):
    #     # 
    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()
    #     self.customers.click_customer_name()
    #     self.customers.click_customer_details_settings_button()

    #     current_idp=self.customers.get_settings_current_idp_value()
    #     current_domain=self.customers.get_settings_current_domain_value()

    #     # Updating IDP Settings
    #     self.customers.change_settings_idp_value(current_idp)
    #     self.customers.enter_domain_name("company.com")
    #     self.customers.click_settings_contextual_footer_save_button()
    #     self.customers.verify_settings_toast_message()

    #     # Verify the updated idp settings
    #     assert current_idp != self.customers.get_settings_current_idp_value()
    #     assert current_domain != self.customers.get_settings_current_domain_value()

    #     # Reverting IDP Settings 
    #     self.customers.select_settings_idp_dropdown_option(current_idp)
    #     self.customers.enter_domain_name(current_domain.split("@")[1])
    #     self.customers.dismiss_toast()
    #     self.customers.click_settings_contextual_footer_save_button()
    #     self.customers.verify_settings_toast_message()

    # Disabling the IDP Tests for now, will resume them once we get our IDP configuration
    # def test_08_verify_customer_details_domain_edit_button_end_to_end_functionality(self):
    #     # 
    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()
    #     self.customers.click_customer_name()
    #     self.customers.click_customer_details_domain_edit_button()

    #     current_idp=self.customers.get_settings_current_idp_value()
    #     current_domain=self.customers.get_settings_current_domain_value()

    #     # Updating IDP Settings
    #     self.customers.change_settings_idp_value(current_idp)
    #     self.customers.enter_domain_name("company.com")
    #     self.customers.click_settings_contextual_footer_save_button()
    #     self.customers.verify_settings_toast_message()

    #     # Verify the updated idp settings
    #     assert current_idp != self.customers.get_settings_current_idp_value()
    #     assert current_domain != self.customers.get_settings_current_domain_value()

    #     # Reverting IDP Settings 
    #     self.customers.select_settings_idp_dropdown_option(current_idp)
    #     self.customers.enter_domain_name(current_domain.split("@")[1])
    #     self.customers.dismiss_toast()
    #     self.customers.click_settings_contextual_footer_save_button()
    #     self.customers.verify_settings_toast_message()
