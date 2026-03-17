import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import random
pytest.app_info = "SMB"

#Generate test user email id
test_user_email = "autotestuser_"+str(random.randint(100,999))+"@gmail.com"

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
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]

    def test_01_verify_users_section(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711404
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711495
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.verify_users_page_title()
        self.users.verify_users_page_description()
        self.users.verify_user_breadcrumb()

    def test_02_verify_users_refresh_button_functionality(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711405
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.verify_users_page_title()

        cur_time = self.users.get_sync_time_info()
        sleep(1)
        self.users.click_refresh_button()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        new_time = self.users.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split("Last updated ")[1], self.driver.get_timezone(), "%m/%d/%Y at %I:%M:%S %p") == True
        assert new_time != cur_time

    @pytest.mark.parametrize('role', ["User","Admin"])
    def test_03_verify_invite_single_recipient(self,role):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711214
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role(role)
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.click_invite_add_button()
        self.users.click_send_invitation_button()
        self.users.verify_email_invitation_sent_message() 
        self.users.click_all_users_tab()

        #search invited user in user list table
        self.users.users_table_data_checkbox_load()
        self.users.search_users(test_user_email, timeout=10)

        #remove invited user from user list table
        self.users.verify_remove_single_user(test_user_email, timeout=20)

    @pytest.mark.parametrize('search_string', ["invalidtestuser", test_user_email])
    def test_04_verify_users_search_functionality(self,search_string ):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711406
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        self.users.search_users(search_string, timeout=20)
        self.users.click_search_clear_button()

    def test_05_verify_contextual_footer(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711407
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        
        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        self.users.click_users_checkbox()

        # Verify contextual footer UI objects
        self.users.verify_contextual_footer()
        self.users.verify_contextual_footer_cancel_button()
        self.users.verify_contextual_footer_remove_user_dropdown()
        # self.users.verify_contextual_footer_continue_button()
        self.users.click_contextual_footer_cancel_button()

    def test_06_verify_cancel_functionality_on_users_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711414
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        self.users.click_users_checkbox()
        self.users.click_contextual_footer_cancel_button()
        self.users.verify_users_checkbox_is_not_checked()

    def test_07_verify_select_action_dropdown_options(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31075939
        expected_select_action_dropdown_options=["Assign Role","Resend Invitation","Remove User"]
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        self.users.click_users_checkbox()
        actual_select_action_dropdown_options=self.users.get_select_action_dropdown_options()
        assert expected_select_action_dropdown_options==actual_select_action_dropdown_options

    def test_08_pagination(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711408
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        self.users.verify_all_page_size_options_new([25, 50, 100])
        self.users.verify_table_displaying_correctly_new(25, page=1)
        self.users.verify_table_displaying_correctly_new(50, page=1)
        self.users.verify_table_displaying_correctly_new(100, page=1)
    
    def test_09_verify_remove_user_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711410
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711411
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        user_email = self.users.get_user_email()
        self.users.select_user_click_mouse_right_button(timeout=20)
        self.users.click_remove_user()

        # Verify Remove User popup
        self.users.verify_removeuser_popup_title(timeout=20)
        self.users.verify_removeuser_popup_desc()
        self.users.verify_removeuser_popup_cancel_button()
        self.users.verify_removeuser_popup_remove_button()

        # Verify the user will not remove after clicking cancel button
        self.users.click_removeuser_popup_cancel_button()
        self.users.verify_user_is_not_removed(user_email)

    def test_10_Verify_admin_user_cannot_remove_themselves(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711416
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        self.users.search_users(self.hpid_username, timeout=10)

        # Verify admin user checkbox is disabled
        self.users.verify_check_box_is_disabled()
        
        # Verify remove user button should not display after hover right click on the admin user
        # self.users.verify_remove_user_button_is_not_displayed(timeout=10)

    def test_11_verify_assign_role_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711417
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711418
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role("Users")
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.click_invite_add_button()
        self.users.click_send_invitation_button()
        self.users.verify_email_invitation_sent_message()

        #search invited user in user list table
        self.users.click_all_users_tab()
        self.users.users_table_data_checkbox_load()
        self.users.search_users(test_user_email, timeout=10)

        user_role = self.users.get_user_role(test_user_email)
        self.users.select_user_click_mouse_right_button(timeout=10)
        self.users.click_assign_role_option()

        # Verify Assign Role popup
        self.users.verify_assign_role_popup_title()
        self.users.verify_assign_role_popup_desc()
        self.users.verify_assign_role_popup_select_role_dropdown()
        self.users.verify_assign_role_popup_cancel_button()
        self.users.verify_assign_role_popup_confirm_button()

        #update user role
        self.users.click_assign_role_popup_select_role_dropdown()
        self.users.update_user_role(user_role)

        #verify user role not updated after clicking cancel button
        self.users.click_assign_role_popup_cancel_button()
        assert user_role==self.users.get_user_role(test_user_email)

    def test_12_verify_assign_role_to_single_user(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711482
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()
        user_role=self.users.get_user_role(test_user_email)
        self.users.assign_role_to_single_user(test_user_email,user_role)
        self.users.users_table_data_checkbox_load()
        assert user_role!=self.users.get_user_role(test_user_email)
    
    def test_13_verify_default_sort(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711415
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.verify_users_page()
        self.users.verify_table_sort("status",["Expired","Pending","Active"])
    
    def test_14_verify_sort_change(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711415
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.verify_users_page()
        self.users.click_table_header_by_name("status")
        self.users.verify_users_page()
        self.users.verify_table_sort("status",["Active","Expired","Pending"])

    def test_15_verify_resend_invitation_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711485
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711486
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        self.users.select_user_click_mouse_right_button(timeout=10)
        self.users.click_resend_invitation_option()

        #verify resend invitation popup
        self.users.verify_resend_invitation_popup_title()
        # self.users.verify_resend_invitation_popup_desc()
        self.users.verify_resend_invitation_popup_cancel_button()
        self.users.verify_resend_invitation_popup_send_invitation_button()

        self.users.click_resend_invitation_popup_cancel_button()

    def test_16_resend_invitation_to_single_user(self): 
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711494
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        self.users.verify_resend_invitation_to_single_user(test_user_email, timeout=10)

    def test_17_verify_columns_option_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711490
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711493
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        user_table_headers = self.users.get_user_table_headers_in_order()
        self.users.click_column_options_gear_icon()

        #Verify column options popup
        self.users.verify_column_options_popup_title()
        self.users.verify_column_options_popup_options()
        self.users.verify_user_checkbox_is_disabled_and_checked()
        self.users.verify_status_and_role_checkbox_are_enabled()
        self.users.verify_reset_to_default_button()
        self.users.verify_column_options_cancel_button()
        self.users.verify_column_options_save_button()

        #verify user table column headers are not changed after clicking on cancel
        self.users.click_column_options_cancel_button()
        assert user_table_headers==self.users.get_user_table_headers_in_order()

    def test_18_remove_single_user(self): 
        # https://hp-testrail.external.hp.com/index.php?/cases/view/30711409
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        self.users.verify_remove_single_user(test_user_email, timeout=20)

    def test_19_verify_invite_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119125
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119126
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.verify_invite_user_title()
        self.users.verify_invite_user_description()
        self.users.verify_invite_user_intro_txt()
        self.users.verify_invite_user_role_dropdown()
        self.users.verify_select_role_dropdown_options(["Admin","User"])
        self.users.verify_invite_user_email_address_text_box()
        self.users.verify_invite_user_add_button_is_disabled()
        self.users.verify_invite_user_total_recipient_is_zero()
        self.users.verify_invite_user_table()
        self.users.verify_invite_user_table_column_email_address()
        self.users.verify_invite_user_table_column_role()
        self.users.verify_invite_user_table_is_empty()
        self.users.verify_send_invitation_button_is_disabled()

    def test_20_verify_remove_recipient_popup(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119135
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119137
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role("User")
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.click_invite_add_button()
        self.users.click_invite_delete_recipient_button()

        # Verify remove recipient pop-up UI
        self.users.verify_invite_remove_recipient_popup()
        # self.users.verify_invite_remove_recipient_popup_desc()
        self.users.verify_invite_remove_recipient_popup_cancel_button()
        self.users.verify_invite_remove_recipient_popup_remove_button()

        # Verify the recipient will not remove afetr clicking cancel button
        self.users.click_invite_remove_recipient_popup_cancel_button()
        self.users.verify_invite_recipient_count(1)
    
    def test_21_verify_edit_recipient_popup_UI_on_recipients_table(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119130
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role("User")
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.click_invite_add_button()        
        self.users.click_invite_edit_recipient_button()

        #verify_edit_recipient_popup_UI
        self.users.verify_invite_edit_recipient_popup()        
        self.users.verify_invite_edit_recipient_email_address(test_user_email)
        self.users.verify_invite_edit_recipient_role_dropdown()        
        self.users.verify_invite_edit_recipient_cancel_button()
        self.users.verify_invite_edit_recipient_save_button_disabled()

    def test_22_verify_error_messages_on_edit_recipient_popup_on_recipients_table(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119132
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role("User")
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.click_invite_add_button()        
        self.users.click_invite_edit_recipient_button()

        #verify_empty_email_error_message
        self.users.invite_edit_recipient_clear_email_text()
        self.users.verify_invite_edit_recipient_empty_email_error_message()

        #verify invalid_email_error_message
        self.users.invite_edit_recipient_enter_email("invalidemail.com")
        self.users.verify_invite_edit_recipient_invalid_email_error_message()

    def test_23_verify_invite_user_functionality_for_invalid_email_address(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/31119129
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role("User")
        self.users.enter_emails_to_invite_txt_box("invalidemail.com")
        self.users.verify_invite_user_invalid_email_error_message()

    @pytest.mark.parametrize('role', ["User"])
    def test_24_verify_inviting_existing_recipient(self,role):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role(role)
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.click_invite_add_button()
        self.users.click_send_invitation_button()
        self.users.verify_email_invitation_sent_message() 
        self.users.click_all_users_tab()

        # Verify and wait for user table data load
        self.users.users_table_data_checkbox_load()

        # Verify invited user added to users table
        self.users.search_users(test_user_email, timeout=10)

        # Verify inviting the existing user from users table
        self.users.click_invite_button()
        self.users.select_role(role)
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.click_invite_add_button()

        # Verify error message of inviting the existing user
        self.users.verify_invite_recipient_error_msg("These users have already been invited and were not added to the recipient list:")
        assert test_user_email == self.users.verify_invite_recipient_error_mail()
        self.users.verify_invite_user_table_is_empty()
        
        #Invited user removed from the user table
        self.users.click_all_users_tab()
        self.users.users_table_data_checkbox_load()
        self.users.verify_remove_single_user(test_user_email, timeout=20)

    @pytest.mark.parametrize('role', ["User"])
    def test_25_verify_retry_invitation_and_failure_toast_notification(self,role):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/31119143
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_role(role)
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.click_invite_add_button()
        self.users.click_send_invitation_button()
        self.users.verify_email_invitation_sent_message() 

        # Verify inviting the existing user invited before
        self.users.select_role(role)
        self.users.enter_emails_to_invite_txt_box(test_user_email)
        self.users.click_invite_add_button()
        self.users.click_send_invitation_button()

        # self.users.check_toast_failure_message("Unable to send email invitation to user.")
        self.users.verify_invite_retry_button()
        self.users.verify_invite_recipient_error_msg("These users were removed from the recipient list because they were already invited:")
        assert test_user_email == self.users.verify_invite_recipient_error_mail()
        
        # Invited user removed from the table
        self.users.click_all_users_tab()
        self.users.users_table_data_checkbox_load()
        self.users.verify_remove_single_user(test_user_email, timeout=20)