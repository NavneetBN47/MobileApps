import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

@pytest.mark.skip
class Test_07_Customers(object):

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

    def test_01_verify_customers_screen_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31175188
        self.customers.verify_page_title(page_title="Customers")
        self.customers.verify_customers_refresh_button()
        self.customers.verify_customers_search_box()
        self.customers.verify_customers_column_option_gear_button()
        self.customers.verify_customers_table_data_load()

    def test_02_verify_customers_contextual_footer(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30455274

        # Verify and wait for customers table data to load
        self.customers.verify_customers_table_data_load()

        self.customers.click_customer_checkbox()
        self.customers.verify_contextual_footer()
        self.customers.verify_contextual_footer_cancel_button()
        self.customers.verify_contextual_footer_selected_item_label()
        self.customers.verify_contextual_footer_select_action_dropdown()
        self.customers.verify_contextual_footer_continue_button()

    def test_03_verify_customers_contextual_footer_select_action_dropdown_options(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30455275

        expected_option="Set IDP"
        # Verify and wait for customers table data to load
        self.customers.verify_customers_table_data_load()

        self.customers.click_customer_checkbox()
        self.customers.verify_contextual_footer()
        self.customers.click_contextual_footer_select_action_dropdown()
        assert expected_option == self.customers.get_contextual_footer_select_action_dropdown_options()

    def test_04_verify_customers_contextual_footer_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30455276

        # Verify and wait for customers table data to load
        self.customers.verify_customers_table_data_load()

        self.customers.click_customer_checkbox()
        # self.customers.click_contextual_footer_select_action_dropdown()
        # self.customers.select_contextual_footer_set_idp_option()
        self.customers.click_contextual_footer_cancel_button()
        self.customers.verify_contextual_footer_is_not_displayed()

    def test_05_verify_customers_refresh_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31175219
        cur_time = self.customers.get_last_updated_datetime()
        sleep(1)
        self.customers.click_refresh_button()

        # Verify and wait for customers table data to load
        self.customers.verify_customers_table_data_load()

        new_time = self.customers.get_last_updated_datetime()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time

    def test_06_verify_customers_paginations(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31175224

        # Verify and wait for customers table data to load
        self.customers.verify_customers_table_data_load()

        self.customers.verify_all_page_size_options_new([25, 50, 75, 100])
        self.customers.verify_table_displaying_correctly_new(25, page=1)
        self.customers.verify_table_displaying_correctly_new(50, page=1)
        self.customers.verify_table_displaying_correctly_new(75, page=1)
        self.customers.verify_table_displaying_correctly_new(100, page=1)

    def test_07_verify_customers_search_functionality(self):
        # 

        # Verify and wait for customers table data to load
        self.customers.verify_customers_table_data_load()
        customer_details=self.customers.get_customer_table_entry_details()
        self.customers.search_customers(customer_details["customer_name"], timeout=20)

    def test_08_verify_customers_invalid_search_functionality(self):
        # 

        # Verify and wait for customers table data to load
        self.customers.verify_customers_table_data_load()
        self.customers.search_customers("Invalidcustomer", timeout=20)

    # IDP Settings is temporarily disabled, So Commenting IDP Settings related testcases
    # def test_09_verify_customer_idp_settings_screen_ui(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30455299

    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()
        
    #     self.customers.click_customer_checkbox()
    #     self.customers.click_contextual_footer_select_action_dropdown()
    #     self.customers.select_contextual_footer_set_idp_option()
    #     self.customers.click_contextual_footer_continue_button()

    #     self.customers.verify_page_title(page_title="Settings")
    #     self.customers.verify_settings_identity_providers_dropdown()
    #     self.customers.verify_settings_domain_field()

    # def test_10_verify_customer_idp_settings_identity_provider_dropdown_options(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30455300
    #     default_idp="HP"
    #     idp_options=["HP","Google","Azure"]
    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()
        
    #     self.customers.click_customer_checkbox()
    #     self.customers.click_contextual_footer_select_action_dropdown()
    #     self.customers.select_contextual_footer_set_idp_option()
    #     self.customers.click_contextual_footer_continue_button()
       
    #     #verify identity providers dropdown options
    #     # assert default_idp == self.customers.get_settings_idp_dropdown_default_option()
    #     assert idp_options == self.customers.get_settings_idp_dropdown_options()


    # def test_11_verify_customers_idp_settings_contextual_footer(self):
    #     #

    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()
        
    #     self.customers.click_customer_checkbox()
    #     self.customers.click_contextual_footer_select_action_dropdown()
    #     self.customers.select_contextual_footer_set_idp_option()
    #     self.customers.click_contextual_footer_continue_button()

    #     current_idp=self.customers.get_settings_current_idp_value()
    #     self.customers.change_settings_idp_value(current_idp)
       
    #     # Verify contextual footer
    #     self.customers.verify_settings_contextual_footer()
    #     self.customers.verify_settings_contextual_footer_cancel_button()
    #     self.customers.verify_settings_contextual_footer_save_button()
    #     self.customers.click_settings_contextual_footer_cancel_button()

    # def test_12_verify_customers_idp_settings_contextual_footer_cancel_button_functionality(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/30455302
        
    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()
    #     self.customers.click_customer_name()
    #     self.customers.click_customer_details_settings_button()
    #     current_idp=self.customers.get_settings_current_idp_value()

    #     # Updating IDP Settings
    #     self.customers.change_settings_idp_value(current_idp)
    #     self.customers.enter_domain_name("company.com")
    #     self.customers.click_settings_contextual_footer_cancel_button()

    #     # Verify Settings Not Saved Popup
    #     self.customers.verify_settings_not_saved_popup_title()
    #     self.customers.verify_settings_not_saved_popup_desc()
    #     self.customers.verify_settings_not_saved_popup_cancel_button()
    #     self.customers.verify_settings_not_saved_popup_leave_button()

    def test_13_verify_column_option_popup_ui(self):
        # 
        expected_options= ["Customer Name", "Country/Region"]
        self.customers.click_customers_column_option_settings_gear_button()
        self.customers.verify_column_options_popup_title()
        self.customers.verify_column_options_popup_reset_to_default_button()
        self.customers.verify_column_options_popup_cancel_button()
        self.customers.verify_column_options_popup_save_button()
        assert expected_options == self.customers.get_column_options_popup_options()

    # IDP Settings is temporarily disabled, So Commenting IDP Settings related testcases
    # def test_14_verify_settings_not_saved_popup_cancel_button_functionality(self):
    #     # 
    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()
    #     self.customers.click_customer_name()
    #     self.customers.click_customer_details_settings_button()
    #     current_idp=self.customers.get_settings_current_idp_value()

    #     # Updating IDP Settings
    #     self.customers.change_settings_idp_value(current_idp)
    #     self.customers.enter_domain_name("company.com")
    #     self.customers.click_settings_contextual_footer_cancel_button()

    #     # Click Settings not saved Cancel Button
    #     self.customers.click_settings_not_saved_popup_cancel_button()

    #     # Verify Settings screen is displayed
    #     self.customers.verify_page_title(page_title="Settings")

    # def test_15_verify_settings_not_saved_popup_leave_button_functionality(self):
    #     #
    #     # Verify and wait for customers table data to load
    #     self.customers.verify_customers_table_data_load()
    #     self.customers.click_customer_name()
    #     self.customers.click_customer_details_settings_button()
    #     current_idp=self.customers.get_settings_current_idp_value()

    #     # Updating IDP Settings
    #     self.customers.change_settings_idp_value(current_idp)
    #     self.customers.enter_domain_name("company.com")
    #     self.customers.click_settings_contextual_footer_cancel_button()

    #     # Click Settings not saved Leave Button
    #     self.customers.click_settings_not_saved_popup_leave_button()

    #     # Verify Customers screen is displayed
    #     self.customers.verify_page_title(page_title="Customers")
