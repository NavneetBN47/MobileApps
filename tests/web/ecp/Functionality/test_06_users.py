import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import random

pytest.app_info = "ECP"

#Generate multiple test user email id
test_user_email_list = [] 
for i in range(10):
    test_user_email = "autouser_"+str(random.randint(1000,9999))+"@gmail.com" # autotestuser email id was too long so changed to autouser
    test_user_email_list.append(test_user_email)

class Test_01_ECP_Web(object):

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
    
    def test_01_verify_send_functionality_on_invite_Screen(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29094216
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()

        # Verify and wait for users table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())
        self.users.click_invite_button()

        #verify send button is enabled
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()
        self.users.verify_send_invitation_button()

        #verify success message and also the total recipient number is zero
        self.users.click_send_invitation_button()
        self.users.verify_email_invitation_sent_message()
        self.users.verify_invite_user_table_is_empty()

        #remove newly invited user
        self.users.click_all_users_tab()

        # Verify and wait fors user table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())

        self.users.verify_remove_single_user(test_user_email_list[0], timeout=20) 

    # def test_02_verify_failure_negative_toast_notification_message_for_invite_users(self):
    #     #https://hp-testrail.external.hp.com/index.php?/cases/view/29094218
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
    #     self.home.click_users_menu_btn()

    #     # Verify and wait for users table data load
    #     self.users.wait_for(self.users.users_table_data_checkbox_load())

    #     #to get all active users from all users table
    #     active_users = self.users.get_active_users()
    
    #     self.users.click_invite_button()
    #     self.users.select_option_from_role_dropdown(0)
    #     self.users.enter_emails_to_invite_txt_box(",".join(active_users))
    #     self.users.click_invite_add_button()
    #     self.users.click_send_invitation_button()

    #     #verify failed invite users alert message
    #     self.users.verify_invite_negative_toast_notification(len(active_users), active_users)
    #     self.users.click_invite_negative_toast_notification_close_button()
    
    # def test_03_verify_retry_functionality_of_failed_invite_users(self):
    #     #https://hp-testrail.external.hp.com/index.php?/cases/view/29094224
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
    #     self.home.click_users_menu_btn()

    #     # Verify and wait for users table data load
    #     self.users.wait_for(self.users.users_table_data_checkbox_load())

    #     #to get all active users from all users table
    #     active_users = self.users.get_active_users()
        
    #     self.users.click_invite_button()
    #     self.users.select_option_from_role_dropdown(0)
    #     self.users.enter_emails_to_invite_txt_box(",".join(active_users))
    #     self.users.click_invite_add_button()
    #     self.users.click_send_invitation_button()

    #     #verify failed invite users alert message
    #     self.users.verify_invite_negative_toast_notification(len(active_users), active_users)
    #     self.users.click_invite_negative_toast_notification_retry_button()
    #     self.users.verify_failed_email_addresses(active_users)
    
    def test_04_verify_remove_recipient_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/29095744
        # https://hp-testrail.external.hp.com/index.php?/cases/view/29099221
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()
        self.users.click_invite_delete_recipient_button()

        # Verify remove recipient pop-up UI
        self.users.verify_invite_remove_recipient_popup()
        self.users.verify_invite_remove_recipient_popup_desc()
        self.users.verify_invite_remove_recipient_popup_cancel_button()
        self.users.verify_invite_remove_recipient_popup_remove_button()

        # Verify the recipient will not remove afetr clicking cancel button
        self.users.click_invite_remove_recipient_popup_cancel_button()
        self.users.verify_invite_recipient_count(1)

    def test_05_verify_remove_recipient(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/29097100
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()
        self.users.click_invite_delete_recipient_button()
        self.users.click_invite_remove_recipient_popup_remove_button()
        self.users.verify_invite_user_table_is_empty()

    def test_06_verify_unsaved_changes_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/29094215
        # https://hp-testrail.external.hp.com/index.php?/cases/view/29094269
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()

        # Verify Unsaved Changes pop-up UI
        self.users.click_all_users_tab()
        self.users.verify_unsaved_changes_popup()
        self.users.verify_unsaved_changes_popup_desc()
        self.users.verify_unsaved_changes_popup_cancel_button()
        self.users.verify_unsaved_changes_popup_leave_button()
        self.users.click_unsaved_changes_popup_cancel_button()

    def test_07_verify_leave_functionality_on_unsaved_changes_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/29094214
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()
        self.users.click_all_users_tab()
        self.users.click_unsaved_changes_popup_leave_button()

        # User should re-directed to Users screen without saving any data in the Invite screen.
        self.users.click_invite_button()
        self.users.verify_invite_user_table_is_empty()
    
    def test_08_verify_edit_recipient_popup_UI_on_recipients_table(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29094238
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()        
        self.users.click_invite_edit_recipient_button()

        #verify_edit_recipient_popup_UI
        self.users.verify_invite_edit_recipient_popup()        
        self.users.verify_invite_edit_recipient_email_address(test_user_email_list[0])
        self.users.verify_invite_edit_recipient_default_role_dropdown()        
        self.users.verify_invite_edit_recipient_cancel_button()
        self.users.verify_invite_edit_recipient_save_button_disabled()
    
    def test_09_verify_error_messages_on_edit_recipient_popup_on_recipients_table(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29096000
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()        
        self.users.click_invite_edit_recipient_button()

        #verify_empty_email_error_message
        self.users.invite_edit_recipient_clear_email_text()
        self.users.verify_invite_edit_recipient_empty_email_error_message()

        #verify invalid_email_error_message
        self.users.invite_edit_recipient_enter_email("invalidemail.com")
        self.users.verify_invite_edit_recipient_invalid_email_error_message()
    
    def test_10_verify_cancel_functionality_on_edit_recipient_popup_on_recipients_table(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29099226
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()        
        self.users.click_invite_edit_recipient_button()

        #verify_cancel_functionality
        update_email = "update_"+test_user_email_list[0]
        self.users.invite_edit_recipient_enter_email(update_email)
        self.users.click_invite_edit_recipient_cancel_button()
        invited_user_email = self.users.get_invite_user_email_address_in_invite_user_table()
        assert update_email != invited_user_email
    
    def test_11_verify_save_functionality_on_edit_recipient_popup_on_recipients_table(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29099227
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
        self.users.click_invite_add_button()        
        self.users.click_invite_edit_recipient_button()
        
        #verify_save_functionality
        update_email = "update_"+test_user_email_list[0]
        self.users.invite_edit_recipient_enter_email(update_email)
        self.users.click_invite_edit_recipient_save_button()
        invited_user_email = self.users.get_invite_user_email_address_in_invite_user_table()
        assert update_email == invited_user_email

    def test_12_verify_invite_user_functionality_for_invalid_email_address(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093219
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box("invalidemail.com")
        self.users.verify_invite_user_invalid_email_error_message()
       
    @pytest.mark.parametrize('recipients', [test_user_email_list]) 
    def test_13_verify_invite_10_recipients(self, recipients):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29092847
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(",".join(recipients))
        self.users.click_invite_add_button()
        self.users.click_send_invitation_button()
        self.users.verify_email_invitation_sent_message()
        self.users.click_all_users_tab()
        
        # Verify and wait for users table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())

        self.users.verify_is_invited_user_display_in_user_table(recipients)
    
    @pytest.mark.parametrize('recipients', [test_user_email_list])
    def test_14_remove_multiple_users(self, recipients): 
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093153
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer
        self.home.click_users_menu_btn()
        
        # Verify and wait for users table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())

        self.users.remove_multiple_users(recipients)
        self.users.verify_remove_user_success_notification(len(recipients))
        
         # Verify and wait for users table data load
        self.users.wait_for(self.users.users_table_data_checkbox_load())
        
        self.users.verify_is_user_removed(recipients)
    
    # This test case is no more valid. Hence test case is commented.
    # def test_15_verify_email_invitation_message_globally(self): 
    #     #https://hp-testrail.external.hp.com/index.php?/tests/view/490478065
    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
    #     self.home.click_users_menu_btn()
    #     self.users.click_invite_button()
    #     self.users.enter_emails_to_invite_txt_box(test_user_email_list[0])
    #     self.users.click_invite_add_button()
    #     self.users.click_send_invitation_button()

    #     # Verify email invitation message should display globally if user navigates to other component screens
    #     self.home.click_account_menu_btn()
    #     self.users.verify_email_invitation_sent_message()