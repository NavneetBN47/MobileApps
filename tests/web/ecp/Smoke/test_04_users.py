import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import random

pytest.app_info = "ECP"

#Generate test user email id
test_user_email = "autotestuser_"+str(random.randint(1000,9999))+"@gmail.com"

class Test_04_ECP_Users_Page(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.users = self.fc.fd["users"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        # self.customer = self.account["customer"]
    
    def test_01_verify_users_section(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093096
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.verify_users_menu_btn()
        self.home.click_users_menu_btn()
        self.users.verify_page_title("Users")

    def test_02_verify_contextual_footer(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29106547
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()
       
        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())
        
        self.users.click_users_checkbox()
        self.users.verify_contextual_footer()
        self.users.verify_contextual_footer_cancel_button()
        self.users.verify_contextual_footer_remove_user_dropdown()
        self.users.verify_contextual_footer_delete_button()
        self.users.click_contextual_footer_cancel_button()
    
    def test_03_verify_users_refresh_button_functionality(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093611
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()
        cur_time = self.users.get_sync_time_info()
        sleep(1)
        self.users.click_refresh_button()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())

        new_time = self.users.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last Updated ")[1], self.driver.get_timezone(), "%b %d, %Y %I:%M:%S %p") == True
        assert new_time != cur_time

    def test_04_verify_remove_user_popup(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093097
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())

        self.users.click_users_checkbox()
        self.users.click_contextual_footer_remove_user_dropdown()
        self.users.select_contextual_footer_remove_user_option()
        self.users.click_contextual_footer_delete_button()
        self.users.verify_removeuser_popup_title()
        self.users.verify_removeuser_popup_description()
        self.users.verify_removeuser_popup_cancel_button()
        self.users.verify_removeuser_popup_remove_button()
        self.users.click_removeuser_popup_cancel_button()
    
    def test_05_verify_invite_single_recipient(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29106549
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.click_invite_add_button()
        self.users.click_send_invitation_button()
        self.users.verify_email_invitation_sent_message() 
        self.users.click_all_users_tab()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())

        self.users.search_users(test_user_email, timeout=10)
    
    @pytest.mark.parametrize('search_string', ["invalidtestuser", test_user_email])
    def test_06_verify_users_search_functionality(self,search_string ):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093627
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())

        self.users.search_users(search_string, timeout=20)
        self.users.click_search_clear_button()
    
    @pytest.mark.parametrize('search_string', [test_user_email])
    def test_07_verify_resend_invitation(self,search_string):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31423395
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())
        self.users.resend_invitation(search_string)
        self.users.verify_email_invitation_sent_message()

    @pytest.mark.parametrize('search_string', [test_user_email])
    def test_08_verify_assign_role(self,search_string):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())
        user_role=self.users.get_user_role(test_user_email)
        self.users.assign_role_to_user(search_string,user_role)

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())
        assert user_role != self.users.get_user_role(test_user_email)
    
    @pytest.mark.parametrize('search_string', [test_user_email])
    def test_09_remove_single_user(self, search_string): 
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093037
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())

        self.users.verify_remove_single_user(search_string, timeout=20) 
    
    def test_10_verify_pagination(self): 
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29106960
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())

        self.users.verify_all_page_size_options_new([25, 50, 75, 100])
        self.users.verify_table_displaying_correctly_new(25, page=1)
        self.users.verify_table_displaying_correctly_new(50, page=1)
        self.users.verify_table_displaying_correctly_new(75, page=1)
        self.users.verify_table_displaying_correctly_new(100, page=1)
    
    def test_11_verify_invite_screen(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29087719
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.home.verify_page_title("Invite Users")
        self.users.verify_invite_user_role_label()
        self.users.verify_invite_user_role_dropdown()
        self.users.verify_invite_user_email_address_label()
        self.users.verify_invite_user_email_address_text_box()
        self.users.verify_invite_user_add_button_is_disabled()
        self.users.verify_invite_user_idp_message()
        self.users.verify_invite_user_table()
        self.users.verify_invite_user_table_column_email_address()
        self.users.verify_invite_user_table_column_role()
        self.users.verify_invite_user_table_is_empty()
    
    def test_12_verify_add_functionality_in_invite_user(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29135322
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.verify_invite_user_add_button()
        self.users.click_invite_add_button()
        self.users.verify_invite_recipient_count(1)
        self.users.verify_send_invitation_button()

        #verify invite user email address in invite user table
        invited_user_email = self.users.get_invite_user_email_address_in_invite_user_table()
        assert invited_user_email == test_user_email

        #verify edit & delete recipient button are displayed
        self.users.verify_invite_edit_recipient_button()
        self.users.verify_invite_delete_recipient_button()
    
    def test_13_verify_default_sort(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/29122386
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()
        self.users.verify_users_page()
        self.users.click_table_header_by_name("status")
        self.users.verify_users_page()
        self.users.verify_table_sort("status",["Active","Expired","Pending"])
    
    def test_14_verify_sort_change(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/29122386
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()
        self.users.verify_users_page()
        self.users.click_table_header_by_name("status")
        self.users.click_table_header_by_name("status")
        self.users.verify_users_page()
        self.users.verify_table_sort("status",["Pending","Expired","Active"])
        
    def test_15_verify_import_users_popup(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()

        # Verify import users poup
        self.users.click_invite_user_import_button()
        self.users.verify_import_users_popup()
        self.users.verify_import_users_popup_title()
        self.users.verify_import_users_popup_description()
        self.users.verify_import_users_popup_browse_label()
        self.users.verify_import_users_popup_sample_file_download_link()
        self.users.verify_import_users_popup_cancel_button()
        self.users.verify_import_users_popup_import_button_status("disabled")
        self.users.click_import_users_popup_cancel_button()
        self.users.verify_import_users_popup(displayed=False)

    @pytest.mark.parametrize('filter_name', ["Active","Expired","Pending","IT Admin","End User"])
    def test_16_verify_filter_functionality(self,filter_name):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31423364
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())
        self.users.click_users_filter_button()
        self.users.select_filter(filter_name)
        self.users.verify_filter_in_users_table(filter_name)

    def test_17_verify_column_option_popup_ui(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31423366
        expected_options= ["User Name","Email Address", "Role", "Status"]
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()
        self.users.click_users_column_options_gear_button()
        self.users.verify_column_options_popup_title()
        self.users.verify_column_options_popup_reset_to_default_button()
        self.users.verify_column_options_popup_cancel_button()
        self.users.verify_column_options_popup_save_button()
        assert expected_options == self.users.get_column_options_popup_options()

    def test_18_verify_column_option_popup_save_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31423368
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())
        self.users.click_users_column_options_gear_button()
        self.users.click_column_option("EMAIL ADDRESS")
        self.users.click_column_options_popup_save_button()

        # Verify Users table Email Address Column
        self.users.verify_users_tabel_column("email",displayed=False)

        # Reverting the Column option changes
        self.users.click_users_column_options_gear_button()
        self.users.click_column_option("EMAIL ADDRESS")
        self.users.click_column_options_popup_save_button()
        self.users.verify_users_tabel_column("email")

    def test_19_verify_column_option_popup_cancel_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31423369
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
       # self.fc.select_customer(self.customer)
        self.home.click_users_menu_btn()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())
        self.users.click_users_column_options_gear_button()
        self.users.click_column_option("EMAIL ADDRESS")
        self.users.click_column_options_popup_cancel_button()

        # Verify Users table Email Address Column
        self.users.verify_users_tabel_column("email")