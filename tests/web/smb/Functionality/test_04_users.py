import pytest
from MobileApps.libs.ma_misc import ma_misc
import random
pytest.app_info = "SMB"

#Generate multiple test user email id
test_user_email_list = [] 
for i in range(10):
    test_user_email = "autotestuser_"+str(random.randint(1000,9999))+"@gmail.com"
    test_user_email_list.append(test_user_email)

class Test_04_SMB_Users(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, smb_setup, request):
        self = self.__class__
        self.driver, self.fc = smb_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        #locale will be received in language_region format
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        self.spec_file = self.driver.session_data["language"]+"-"+self.driver.session_data["locale"].upper()
        self.home = self.fc.fd["home"]
        self.users = self.fc.fd["users"]
        self.account = self.fc.fd["account"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]

    @pytest.mark.parametrize('role', ["User","Admin"])
    @pytest.mark.parametrize('recipients', [test_user_email_list])
    def test_01_verify_invite_10_recipients(self, recipients,role):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119128
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role(role)
        self.users.enter_emails_to_invite_txt_box(",".join(recipients))
        self.users.click_invite_add_button()
        self.users.click_send_invitation_button()
        self.users.verify_email_invitation_sent_message(len(recipients))
        self.users.click_all_users_tab()

        # Verify and wait for users table data load
        self.users.users_table_data_checkbox_load()
        self.users.verify_is_invited_user_display_in_user_table(recipients,role=role)
        
        #remove invited multiple users
        self.users.remove_multiple_users(recipients)
        self.users.verify_is_user_removed(recipients)

    @pytest.mark.parametrize('recipients', [test_user_email_list])

    def test_02_resend_invitation_to_multiple_user(self, recipients):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711487
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role("User")
        self.users.enter_emails_to_invite_txt_box(",".join(recipients))
        self.users.click_invite_add_button()
        self.users.click_send_invitation_button()
        self.users.verify_email_invitation_sent_message(len(recipients))
        self.users.click_all_users_tab()    

        # Verify and wait for users table data load
        self.users.users_table_data_checkbox_load()

        self.users.verify_is_invited_user_display_in_user_table(recipients,role="User")
        # Verify resend invitation to multiple users
        self.users.resend_invitation_to_multiple_user(recipients)

    @pytest.mark.parametrize('recipients', [test_user_email_list])
    def test_03_assign_role_to_multiple_user(self, recipients): 
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711482
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        
        # Verify and wait for users table data load
        self.users.users_table_data_checkbox_load()
        self.users.assign_role_to_multiple_user(recipients,"User")
        self.users.verify_assign_role_success_toast_notification(len(recipients))

        # Verify and wait for users table data load
        self.users.users_table_data_checkbox_load()

        self.users.verify_is_invited_user_display_in_user_table(recipients,role="Admin")

    @pytest.mark.parametrize('recipients', [test_user_email_list])
    def test_04_remove_multiple_users(self, recipients): 
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711412
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        
        # Verify and wait for users table data load
        self.users.users_table_data_checkbox_load()

        self.users.remove_multiple_users(recipients)
        self.users.verify_remove_user_success_notification(len(recipients))
        
         # Verify and wait for users table data load
        self.users.users_table_data_checkbox_load()
        
        self.users.verify_is_user_removed(recipients)

    def test_05_verify_remove_recipient(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119136
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role("User")
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()
        self.users.click_invite_delete_recipient_button()
        self.users.click_invite_remove_recipient_popup_remove_button()
        self.users.verify_invite_recipient_count(0)

    def test_06_verify_cancel_functionality_on_edit_recipient_popup_on_recipients_table(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119133
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role("User")
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()        
        self.users.click_invite_edit_recipient_button()

        #verify_cancel_functionality
        update_email = "update_"+test_user_email_list[0]
        self.users.invite_edit_recipient_clear_email_text()
        self.users.invite_edit_recipient_enter_email(update_email)
        self.users.click_invite_edit_recipient_cancel_button()
        invited_user_email = self.users.get_invite_user_email_address_in_invite_user_table()
        assert update_email != invited_user_email
    
    def test_07_verify_save_functionality_on_edit_recipient_popup_on_recipients_table(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119134
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role("User")
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()        
        self.users.click_invite_edit_recipient_button()
        
        #verify_save_functionality
        update_email = "update_"+test_user_email_list[0]
        self.users.invite_edit_recipient_clear_email_text()
        self.users.invite_edit_recipient_enter_email(update_email)
        self.users.click_invite_edit_recipient_save_button()
        invited_user_email = self.users.get_invite_user_email_address_in_invite_user_table()
        assert update_email == invited_user_email

    def test_08_verify_role_dropdown_on_edit_recipient_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119131
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role("User")
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()        
        self.users.click_invite_edit_recipient_button()
        self.users.verify_invite_edit_recipient_role("User")
        self.users.verify_role_dropdown_options(["Admin","User"])
    
    def test_09_verify_column_option_popup_enable_and_disable_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711492
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()
        self.users.click_column_options_gear_icon()

        self.users.click_column_option("ROLE")
        self.users.click_column_options_save_button()

        # Verify Users table Role Column
        self.users.verify_users_table_column("role",displayed=False)

        # Reverting the Column option changes
        self.users.click_column_options_gear_icon()
        self.users.click_column_option("ROLE")
        self.users.click_column_options_save_button()
        self.users.verify_users_table_column("role")

        # Verify Cancel button functionality
        self.users.click_column_options_gear_icon()
        self.users.click_column_option("STATUS")
        self.users.click_column_options_cancel_button()

        # Verify Users table Status Column
        self.users.verify_users_table_column("status")

    def test_10_verify_columns_option_reset_to_default_functioanlity(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711491
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()
        user_table_headers = self.users.get_user_table_headers_in_order()
        self.users.click_column_options_gear_icon()

        self.users.click_column_option("ROLE")
        self.users.click_column_options_save_button()

        # Verify Users table Role Column
        self.users.verify_users_table_column("role",displayed=False)

        # Reverting the Column option changes
        self.users.click_column_options_gear_icon()
        self.users.click_reset_to_default_button()
        self.users.click_column_options_save_button()

        #verify user table column headers are reverted after clicking on Reset to Default
        assert user_table_headers==self.users.get_user_table_headers_in_order()