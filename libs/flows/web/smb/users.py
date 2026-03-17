import logging
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from MobileApps.libs.flows.web.smb.smb_flow import SMBFlow
from time import sleep

class UserSearchException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class RecipientCountMismatchException(Exception):
    pass

class UserRoleException(Exception):
    pass

class WrongToastException(Exception):
    pass

class Users(SMBFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for SMB
    """
    flow_name = "users"

    def verify_users_page(self, timeout=10):
        return self.driver.wait_fro_object("users_page", timeout=timeout)
    
    def verify_users_page_title(self, timeout=40):
        return self.driver.verify_object_string("users_title", timeout=timeout)

    def verify_users_page_description(self):
        return self.driver.verify_object_string("users_section_desc")

    def users_table_data_checkbox_load(self):
        return  self.driver.wait_for_object("table_entry_checkbox", timeout=60)

    def search_users(self, usr_info, raise_e=True, timeout=10):
        """
            Search users in user table by using either user name or Email id 
            Should display list of users based on search string, if search string match
            else should display No items found message.
        """
        self.driver.wait_for_object("search_user_inputbox",timeout=timeout, raise_e=raise_e)
        # self.driver.send_keys("search_user_inputbox", usr_info)
        # Press enter parameter is added , due to search enhancement.
        self.driver.send_keys("search_user_inputbox", usr_info, press_enter=True)
        
        if self.driver.find_object("table_entry_noitemsfound_warning_message",raise_e=False) is not False:
            table_entry_users=self.driver.find_object("table_entry_noitemsfound_warning_message")
            logging.info(table_entry_users.text)
            return False
        else:
            table_entry_users = self.driver.find_object("user_table_entries",multiple=True)

            for i in range(len(table_entry_users)):
                if usr_info in table_entry_users[i].text:
                    logging.info("Username: " + table_entry_users[i].text + " contains the searched string: " + usr_info)
                    continue
                else:
                    raise UserSearchException("Username: " + table_entry_users[i].text + " does not contain the searched string: " + usr_info)
        return True

    def click_search_clear_button(self):
        return self.driver.click("search_clear_btn")

    def verify_users_checkbox_is_not_checked(self):
        if self.driver.find_object("table_entry_checkbox").is_selected():
            raise UnexpectedItemPresentException("Users checkbox is checked")
        return True

    def get_user_email(self):
        #This method will return the first user email from users table
        self.driver.wait_for_object("table_entry_email")
        return self.driver.get_text("table_entry_email")
    
    def get_user_status(self, user):
        user_emails = self.driver.find_object("table_entry_email",multiple=True)
        for i in range(len(user_emails)):
            if user in user_emails[i].text:
                self.driver.wait_for_object("user_status", format_specifier=[i+1])
                return self.driver.get_text("user_status", format_specifier=[i+1])
        else:
            raise UserSearchException("User is not showing in users table: "+user)

    ################################# Contextual footer ####################################################   

    def verify_contextual_footer(self):
        return self.driver.wait_for_object("contextual_footer")

    def verify_contextual_footer_cancel_button(self):
        return self.driver.wait_for_object("contextual_footer_cancel_btn")
        
    def click_contextual_footer_cancel_button(self):
        return self.driver.click("contextual_footer_cancel_btn")

    def verify_contextual_footer_remove_user_dropdown(self):
        return self.driver.wait_for_object("contextual_footer_select_action_dropdown")

    def verify_contextual_footer_continue_button(self):
        return self.driver.wait_for_object("contextual_footer_continue_btn")

    def click_contextual_footer_continue_button(self):
        return self.driver.click("contextual_footer_continue_btn")

    def get_select_action_dropdown_options(self):
        actual_options = []
        self.click_contextual_footer_select_action_dropdown()
        all_options = self.driver.find_object("contextual_footer_select_action_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        return actual_options

    ############################## Remove User Popup ##########################################

    def verify_removeuser_popup_title(self, timeout=20):
        return self.driver.verify_object_string("removeuser_popup_title", timeout=timeout)

    def verify_removeuser_popup_desc(self):
        return self.driver.verify_object_string("removeuser_popup_desc")
        
    def verify_removeuser_popup_cancel_button(self):
        return self.driver.wait_for_object("removeuser_popup_cancel_btn")

    def verify_removeuser_popup_remove_button(self):
        return self.driver.wait_for_object("removeuser_popup_remove_btn")

    def click_removeuser_popup_cancel_button(self):
        return self.driver.click("removeuser_popup_cancel_btn")

    def verify_user_is_not_removed(self, user_email):
        self.compare_strings(user_email, self.get_user_email())

    ############################### Assign Role popup #########################################

    def verify_assign_role_popup_title(self):
        return self.driver.verify_object_string("assign_role_popup_title")

    def verify_assign_role_popup_desc(self):
        return self.driver.verify_object_string("assign_role_popup_desc")

    def verify_assign_role_popup_select_role_dropdown(self):
        return self.driver.wait_for_object("assign_role_popup_select_role_dropdown")

    def verify_assign_role_popup_cancel_button(self):
        return self.driver.wait_for_object("assign_role_popup_cancel_btn")

    def verify_assign_role_popup_confirm_button(self):
        return self.driver.wait_for_object("assign_role_popup_confirm_btn")

    def click_assign_role_popup_cancel_button(self):
        return self.driver.click("assign_role_popup_cancel_btn")

    def assign_role_to_multiple_user(self,users,user_role,timeout=10):
        #Search user and click on check box
        for user in users:
            if self.search_users(user, timeout=timeout):
                self.click_users_checkbox()
                self.click_search_clear_button()
            
        #Resend invitaion to selected users
        self.click_contextual_footer_select_action_dropdown()
        self.select_contextual_footer_assign_role_option()
        # self.click_contextual_footer_continue_button()
        self.click_assign_role_popup_select_role_dropdown()
        self.update_user_role(user_role)
        self.click_assign_role_popup_confirm_button()
        return True

    def get_user_role(self,user):
        if self.search_users(user, timeout=10):
            return self.driver.wait_for_object("table_entry_role").text
        else:
            raise UserSearchException("User is not showing in users table: "+user)

    def click_assign_role_popup_select_role_dropdown(self):
        return self.driver.click("assign_role_popup_select_role_dropdown")

    def update_user_role(self, user_role):
        if user_role == "Admin":
            return self.driver.click("assign_role_popup_select_role_dropdown_user_option")
        return self.driver.click("assign_role_popup_select_role_dropdown_admin_option")

    def click_assign_role_popup_confirm_button(self):
        return self.driver.click("assign_role_popup_confirm_btn")

    def verify_role_updated(self, user_role_before_update):
        user_role_after_update = self.get_user_role()
        if user_role_before_update.lower() != user_role_after_update.lower():
            return True
        else:
            raise UserRoleException("User role din't got updated")

    def verify_assign_role_success_toast_notification(self, no_of_users):
        if no_of_users == 1:
            expected_text = "Successfully assigned role to {} user. " 
        else:
            expected_text = "Successfully assigned roles to {} users." 
        expected_alert_message= expected_text.format(no_of_users)
        actual_alert_message = self.get_toast_notification_text()
        self.compare_strings(expected_alert_message, actual_alert_message)

    def assign_role_to_single_user(self,user,user_role):
        if self.search_users(user, timeout=10):
            self.select_user_click_mouse_right_button(timeout=10)
            self.click_assign_role_option()
            self.click_assign_role_popup_select_role_dropdown()
            self.update_user_role(user_role)
            self.click_assign_role_popup_confirm_button()
            # self.verify_assign_role_success_toast_notification(1)
        else:
            raise UserSearchException("User is not showing in users table: "+user)

    ######################### Resend Invitation popup #########################################

    def click_resend_invitation_option(self):
        return self.driver.click("resend_invitation_option")
    
    def verify_resend_invitation_popup_title(self):
        return self.driver.verify_object_string("resend_invitation_popup_title",timeout=10)

    def verify_resend_invitation_popup_desc(self):
        return self.driver.verify_object_string("resend_invitation_popup_desc")

    def verify_resend_invitation_popup_cancel_button(self):
        return self.driver.wait_for_object("resend_invitation_popup_cancel_btn")

    def verify_resend_invitation_popup_send_invitation_button(self):
        return self.driver.wait_for_object("resend_invitation_popup_send_invitation_btn")

    def click_resend_invitation_popup_cancel_button(self):
        return self.driver.click("resend_invitation_popup_cancel_btn")

    def click_resend_invitation_popup_send_invitation_button(self):
        return self.driver.click("resend_invitation_popup_send_invitation_btn")

    ################################## Column Options Popup ##################################################

    def click_column_options_gear_icon(self):
        return self.driver.click("column_options_gear_icon")

    def get_user_table_headers_in_order(self):
        user_table_headers = []
        headers = self.driver.find_object("user_table_headers", multiple = True)
        for header in headers:
            user_table_headers.append(header.text)
        return user_table_headers

    def verify_column_options_popup_title(self):
        return self.driver.verify_object_string("column_options_popup_title")

    def verify_column_options_popup_options(self):
        expected_options = ["User", "Status", "Role"]
        actual_options = []
        options = self.driver.find_object("column_options_popup_options", multiple = True)
        for option in options:
            actual_options.append(option.text)
        assert expected_options==actual_options
    
    def click_column_option(self,option):
        options = self.driver.find_object("column_options_popup_options", multiple = True)
        if option == "STATUS":
            options[1].click()
        elif option == "ROLE":
            options[2].click()
    
    def verify_reset_to_default_button(self):
        return self.driver.wait_for_object("column_options_popup_reset_to_default_btn")
    
    def click_reset_to_default_button(self):
        return self.driver.click("column_options_popup_reset_to_default_btn")

    def verify_column_options_cancel_button(self):
        return self.driver.wait_for_object("column_options_popup_cancel_btn")

    def verify_column_options_save_button(self):
        return self.driver.wait_for_object("column_options_popup_save_btn")

    def click_column_options_save_button(self):
        return self.driver.click("column_options_popup_save_btn")

    def click_column_options_cancel_button(self):
        return self.driver.click("column_options_popup_cancel_btn")

    def verify_user_checkbox_is_disabled_and_checked(self):
        user_checkbox = self.driver.find_object("column_options_popup_user_checkbox")
        if user_checkbox.is_selected():
            if user_checkbox.is_enabled():
                raise UnexpectedItemPresentException("user checkbox is enabled")
            else:
                return True
        else:
            raise UnexpectedItemPresentException("user checkbox is not checked")

    def verify_status_and_role_checkbox_are_enabled(self):
        status_and_role_checkbox = self.driver.find_object("column_options_popup_status_and_role_checkbox", multiple = True)
        for checkbox in status_and_role_checkbox:
            if checkbox.is_enabled():
                return True
            else:
                raise UnexpectedItemPresentException("status/role checkbox is disabled")
    
    def verify_users_table_column(self,column_name,displayed=True):
        return self.driver.wait_for_object(column_name+"_table_header", invisible=not displayed)

    ########################### Invite Page ###########################

    def select_role(self, role):
        self.driver.click("invite_select_role_drop_down",timeout=30)
        sleep(3)
        if role == "Admin":
            return self.driver.click("invite_select_role_drop_down_option_admin",timeout=30)
        return self.driver.click("invite_select_role_drop_down_option_user",timeout=30)

    def enter_emails_to_invite_txt_box(self, emails):
        return self.driver.send_keys("invite_email_address_text_box", emails)

    def click_send_invitation_button(self):
        return self.driver.click("invite_send_invitations_btn")

    def verify_invite_btn(self):
        return self.driver.wait_for_object("invite_btn")
    
    def click_invite_button(self, timeout=30): 
        return self.driver.click("invite_btn", timeout=timeout)

    def click_invite_add_button(self):
        return self.driver.click("invite_user_add_btn",timeout=10)

    def click_all_users_tab(self):
        return self.driver.click("invite_all_users_breadcrumb")

    def verify_email_invitation_sent_message(self,no_of_users=1):
        if no_of_users == 1:
            expected_text = "Email invitation was successfully sent to {} user." 
        else:
            expected_text = "Email invitation was successfully sent to {} users." 
        expected_alert_message= expected_text.format(no_of_users)
        actual_alert_message = self.get_toast_notification_text()
        self.compare_strings(expected_alert_message, actual_alert_message)

    def get_toast_notification_text(self):
        return self.driver.wait_for_object("success_alert").text

    def verify_remove_single_user(self, usr_info, timeout=10):
        """
            - This is method used to remove a specific user
            - If user doed not found it returns False
        """
        if self.search_users(usr_info, timeout=timeout):
            self.select_user_click_mouse_right_button(timeout)
            self.click_remove_user()
            self.click_removeuser_popup_remove_button()
            # self.verify_remove_user_success_notification(1)
            self.click_search_clear_button()

            # Verify and wait for users table data load
            self.users_table_data_checkbox_load()

            if self.search_users(usr_info, timeout=timeout):
                raise UserSearchException("User is not  deleted: "+usr_info)
            else:
                logging.info("User successfully deleted: "+usr_info)
                return True
        else:
            logging.info("User does not found: "+usr_info)
            return False

    def select_user_click_mouse_right_button(self, timeout):
        #This method is used for Mouse right button click
        ac = ActionChains(self.wdvr)
        self.driver.wait_for_object("table_entry_contextual_menu", timeout=timeout)
        obj = self.driver.find_object("table_entry_contextual_menu")
        ac.context_click(obj).perform()
        return True

    def click_remove_user(self):
        return self.driver.click("remove_user_btn")

    def click_resend_invitation_option(self):
        return self.driver.click("resend_invitation_option")

    def click_assign_role_option(self):
        return self.driver.click("assign_role_option")

    def click_removeuser_popup_remove_button(self):
        return self.driver.click("removeuser_popup_remove_btn")

    def click_resend_invitation_popup_send_invitation_button(self):
        return self.driver.click("resend_invitation_popup_send_invitation_btn")

    def verify_remove_user_success_notification(self, no_of_users):
        #verify positive  toast notification alert message 
        if no_of_users == 1:
            expected_text = "Successfully removed {} user." 
        else:
            expected_text = "Successfully removed {} users." 
        expected_alert_message= expected_text.format(no_of_users)
        actual_alert_message = self.get_toast_notification_text()
        self.compare_strings(expected_alert_message, actual_alert_message)

    def remove_multiple_users(self, users, timeout=20):
        #Search user and click on check box
        for user in users:
            if self.search_users(user, timeout=timeout):
                self.click_users_checkbox()
                self.click_search_clear_button()
            
        #Remove selected users by click on Continue button
        self.click_contextual_footer_select_action_dropdown()
        self.select_contextual_footer_remove_user_option()
        # self.click_contextual_footer_continue_button()
        self.click_removeuser_popup_remove_button()
        return True

    def click_users_checkbox(self):
        return self.driver.click("table_entry_checkbox")

    def click_contextual_footer_select_action_dropdown(self):
        return self.driver.click("contextual_footer_select_action_dropdown")

    def select_contextual_footer_remove_user_option(self):
        return self.driver.click("contextual_footer_dropdown_remove_user_option")

    def select_contextual_footer_resend_invitation_option(self):
        return self.driver.click("contextual_footer_dropdown_resend_invitation_option") 

    def select_contextual_footer_assign_role_option(self):
        return self.driver.click("contextual_footer_dropdown_assign_role_option")

    def verify_is_user_removed(self, users,timeout=10):
        for user in users:
            if self.search_users(user, timeout=timeout):
                raise UserSearchException("User is not  deleted: "+user)
            else:
                logging.info("User successfully deleted: "+user)
                self.click_search_clear_button()
        return True

    def verify_is_invited_user_display_in_user_table(self, users,role=None):
        for user in users:
            if self.search_users(user, timeout=10):
                if role!=None:
                    self.verify_invited_user_role(role)
                self.click_search_clear_button()
            else:
                raise UserSearchException("Invited User is not showing in users table: "+user)
        return True

    def verify_invited_user_role(self,role):
        actual_role=self.driver.get_text("table_entry_role")
        self.compare_strings(role, actual_role)

    def verify_check_box_is_disabled(self):
        #verify searched admin user checkbox is disabled
        if self.driver.find_object("table_entry_checkbox_disabled").is_enabled():
            raise UnexpectedItemPresentException(" Checkbox is enabled")
        return True

    def verify_remove_user_button_is_not_displayed(self, timeout):
        # Right click on serached user and verify the remove user option should not be there.
        self.select_user_click_mouse_right_button(timeout)
        return self.driver.wait_for_object("remove_user_btn", invisible=True)

    def verify_resend_invitation_to_single_user(self,usr_info,timeout=10):
        if self.search_users(usr_info, timeout=timeout):
            self.select_user_click_mouse_right_button(timeout)
            self.click_resend_invitation_option()
            self.click_resend_invitation_popup_send_invitation_button()
            # self.verify_email_invitation_sent_message(1)
        else:
            raise UserSearchException("User is not showing in users table: "+usr_info)

    def resend_invitation_to_multiple_user(self,users,timeout=10):
        #Search user and click on check box
        for user in users:
            if self.search_users(user, timeout=timeout):
                self.click_users_checkbox()
                self.click_search_clear_button()
            
        #Resend invitaion to selected users
        self.click_contextual_footer_select_action_dropdown()
        self.select_contextual_footer_resend_invitation_option()
        # self.click_contextual_footer_continue_button()
        self.click_resend_invitation_popup_send_invitation_button()
        return True

    ################################ Verify Invite User Screen ######################################################

    def verify_invite_users_section(self, timeout=10):
        self.driver.wait_for_object("invite_user_title", timeout=timeout)
        self.driver.wait_for_object("invite_user_desc")
    
    def verify_invite_user_title(self):
        return self.driver.verify_object_string("invite_user_title")

    def verify_invite_user_description(self):
        return self.driver.verify_object_string("invite_user_desc")
        
    def verify_invite_user_intro_txt(self):
        return self.driver.verify_object_string("invite_user_intro_txt")
            
    def verify_invite_user_role_dropdown(self):
        return self.driver.wait_for_object("invite_select_role_drop_down")

    def verify_invite_user_email_address_text_box(self):
        return self.driver.wait_for_object("invite_email_address_text_box")

    def verify_invite_user_add_button_is_disabled(self):
        if self.driver.find_object("invite_user_add_btn").is_enabled():
            raise UnexpectedItemPresentException("Add button is enabled")
        return True

    def verify_invite_user_total_recipient_is_zero(self):
        return self.driver.verify_object_string("invite_user_total_recipient_label")
       
    def verify_invite_user_table(self):
        return self.driver.wait_for_object("invite_user_table")

    def verify_invite_user_table_column_email_address(self):
        return self.driver.wait_for_object("invite_user_table_heading_email")

    def verify_invite_user_table_column_role(self):
        return self.driver.wait_for_object("invite_user_table_heading_role")

    def click_invite_delete_recipient_button(self):
        return self.driver.click("invite_recipients_delete_button")
        
    def verify_invite_user_table_is_empty(self):
        expected_text = "No emails added yet. Enter user email addresses."
        actual_text = self.driver.get_text("invite_user_table_no_item")
        if actual_text == expected_text:
            return True
        else:
            raise UnexpectedItemPresentException("invite user table is not empty")

    def verify_send_invitation_button_is_disabled(self): 
        if self.driver.find_object("invite_send_invitations_btn").is_enabled():
            raise UnexpectedItemPresentException(" Send button is enabled")
        return True

    def verify_select_role_dropdown_options(self,expected_options):
        actual_options = []
        self.driver.click("invite_select_role_drop_down",timeout=10)
        all_options = self.driver.find_object("invite_select_role_drop_down_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        assert expected_options == actual_options

    def verify_invite_user_invalid_email_error_message(self):
        return self.driver.verify_object_string("invite_user_email_address_error_msg")

    ############################ Invite Remove Recipient Pop-Up ############################

    def verify_invite_remove_recipient_popup(self):
        return self.driver.wait_for_object("invite_remove_recipients_popup_title")

    def verify_invite_remove_recipient_popup_desc(self):
        return self.driver.verify_object_string("invite_remove_recipients_popup_desc")
      
    def verify_invite_remove_recipient_popup_cancel_button(self):
        return self.driver.wait_for_object("invite_remove_recipients_popup_cancel_button")

    def verify_invite_remove_recipient_popup_remove_button(self):
        return self.driver.wait_for_object("invite_remove_recipients_popup_remove_button")

    def click_invite_remove_recipient_popup_cancel_button(self):
        return self.driver.click("invite_remove_recipients_popup_cancel_button")

    def click_invite_remove_recipient_popup_remove_button(self):
        return self.driver.click("invite_remove_recipients_popup_remove_button")

    def verify_invite_recipient_count(self,expected_recipient_count):
        actual_recipient_count = self.get_invite_recipient_count()
        if expected_recipient_count == actual_recipient_count:
            return True
        else:
            raise RecipientCountMismatchException("Does not match expected recipient count: "+expected_recipient_count+", actual recipient count: "+actual_recipient_count)

    def get_invite_recipient_count(self):
        recipient_label=self.driver.find_object("invite_total_recipients_label").text
        return int(recipient_label[19:])

    ############################### users count ################################################

    def verify_users_page(self):
        return self.driver.wait_for_object("user_table_entries", timeout=10)

    def get_users(self):
        # This method returns the active, pending and total users count
        active_users = 0
        pending_users = 0
        expired_users = 0
        self.driver.wait_for_object("_shared_table_entries",timeout=30)
        self.select_page_size_new("100")
        max_pages=self.get_max_page()
        for page in range(max_pages):
            self.select_page(page+1)
            rows = self.driver.find_object("_shared_table_entries",multiple=True)
            for row in rows:
                s = row.text
                if 'Active' in s:
                    active_users+=1
                if 'Pending' in s:
                    pending_users+=1
                if 'Expired' in s:
                    expired_users+=1
        users_page_user_count = {"active" : active_users, "pending" : pending_users, "expired" : expired_users,  "total_count" : active_users + pending_users + expired_users}
        return users_page_user_count

    ############################### Verify Edit Recipient popup #######################################################

    def click_invite_edit_recipient_button(self):
        return self.driver.click("invite_recipients_edit_button", timeout=20) 

    def verify_invite_edit_recipient_popup(self):
        return self.driver.wait_for_object("invite_edit_recipient_popup")
                   
    def verify_invite_edit_recipient_email_address(self,expected_emailaddress):
        actual_emailaddress = self.driver.get_text("invite_edit_recipient_popup_email_address")
        self.compare_strings(expected_emailaddress, actual_emailaddress)

    def verify_invite_edit_recipient_empty_email_error_message(self):
        return self.driver.verify_object_string("invite_edit_recipient_email_error_msg")  

    def verify_invite_edit_recipient_role_dropdown(self):
        return self.driver.wait_for_object("invite_edit_recipient_popup_role_dropdown")
    
    def verify_invite_edit_recipient_cancel_button(self):
        return self.driver.wait_for_object("invite_edit_recipient_popup_cancel_button")

    def verify_invite_edit_recipient_save_button_disabled(self):
        #verify save button is disable
        if self.driver.find_object("invite_edit_recipient_popup_save_button").is_enabled():
            raise UnexpectedItemPresentException("save button is enabled")
        return True

    def invite_edit_recipient_clear_email_text(self):
        return self.driver.clear_text("invite_edit_recipient_popup_email_address")
    
    def invite_edit_recipient_enter_email(self,emails):
        return self.driver.send_keys("invite_edit_recipient_popup_email_address", emails)
    
    def click_invite_edit_recipient_cancel_button(self):
        return self.driver.click("invite_edit_recipient_popup_cancel_button")

    def click_invite_edit_recipient_save_button(self):
        return self.driver.click("invite_edit_recipient_popup_save_button")

    def verify_invite_edit_recipient_role(self,expected_role):
        actual_role = self.driver.get_text("invite_edit_recipient_popup_role")
        self.compare_strings(expected_role, actual_role)
       
    def verify_invite_edit_recipient_invalid_email_error_message(self):
        return self.driver.verify_object_string("invite_edit_recipient_email_error_msg_invalid")

    def get_invite_user_email_address_in_invite_user_table(self):
        return self.driver.get_text("invite_user_table_email_address")

    def verify_role_dropdown_options(self,expected_options):
        actual_options = []
        self.driver.click("invite_edit_recipient_popup_role_dropdown",timeout=10)
        all_options = self.driver.find_object("invite_edit_recipient_popup_role_dropdown_options",multiple=True)
        for option in all_options:
            actual_options.append(option.text)
        assert expected_options == actual_options

    ############################ Unsaved Changes Pop-Up ############################

    def verify_unsaved_changes_popup(self):
        return self.driver.wait_for_object("unsaved_changes_popup_title")

    def verify_unsaved_changes_popup_desc(self):
        return self.driver.verify_object_string("unsaved_changes_popup_desc")
       
    def verify_unsaved_changes_popup_cancel_button(self):
        return self.driver.wait_for_object("unsaved_changes_popup_cancel_button")

    def verify_unsaved_changes_popup_leave_button(self):
        return self.driver.wait_for_object("unsaved_changes_popup_leave_button")

    def click_unsaved_changes_popup_cancel_button(self):
        return self.driver.click("unsaved_changes_popup_cancel_button")

    def click_unsaved_changes_popup_leave_button(self):
        return self.driver.click("unsaved_changes_popup_leave_button")
    
    def verify_user_breadcrumb(self):
        self.driver.wait_for_object("breadcrumb")
        self.driver.verify_object_string("home_breadcrumb")
        return self.driver.verify_object_string("user_breadcrumb")

    def verify_invite_recipient_error_msg(self,expected_message):
        actual_message = self.driver.wait_for_object("invite_recipient_error_msg").text
        if actual_message == expected_message:
            return True
        else:
            raise UnexpectedItemPresentException("The error message is: " + actual_message + " expected message is: " + expected_message)

    def verify_invite_recipient_error_mail(self):
        return self.driver.get_text("invite_recipient_error_mail")

    def check_toast_failure_message(self, expected_message):
        actual_message = self.driver.wait_for_object("success_alert").text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)

    def verify_invite_retry_button(self):
        return self.driver.get_text("invite_recipient_retry_button")

    def verify_role_by_email(self, email, role):
        self.search_users(email)
        email_column = self.get_header_index("email")
        role_column = self.get_header_index("role")
        email_list = self.driver.find_object("_shared_table_user_col_by_index", format_specifier=[email_column],multiple=True)
        role_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[role_column],multiple=True)
        for index in range(len(email_list)):
            if email.lower() != email_list[index].text.lower():
                continue
            if role.lower() == role_list[index].text.lower():
                return True
            else:
                return False

        raise UserSearchException(f"Cannot find '{email}' with role: {role}")
