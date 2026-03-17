import logging
import collections
from socket import timeout
from time import sleep
import time
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow
from pytz import timezone
from selenium.webdriver.common.action_chains import ActionChains
from MobileApps.libs.ma_misc import ma_misc

class UserSearchException(Exception):
    pass

class FailedEmailMismatchException(Exception):
    pass

class UnexpectedItemPresentException(Exception):
    pass

class RecipientCountMismatchException(Exception):
    pass

class UnableToFindActiveUserException(Exception):
    pass

class FilterValueException(Exception):
    pass

class Users(ECPFlow):
    """
        Contains all of the elements and flows associated in Users section for ECP
    """
    flow_name = "users"

    def verify_users_page(self):
        return self.driver.wait_for_object("user_table_entries", timeout=10)

    def verify_userspage_title(self, timeout=20):
        #Verify Users page/section title
        self.driver.wait_for_object("users_title", timeout=timeout)
        return self.driver.verify_object_string("users_title")
       
    def verify_userspage_desc(self):
        #verify users section descriion 
        return self.driver.verify_object_string("users_section_desc")

    def verify_role_by_email(self, email, role):
        self.search_users(email, validate_results=False)
        email_column = self.get_header_index("email")
        role_column = self.get_header_index("role")
        email_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[email_column],multiple=True)
        role_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[role_column],multiple=True)

        for index in range(len(email_list)):
            if email.lower() != email_list[index].text.lower():
                continue
            if role.lower() == role_list[index].text.lower():
                return True
            else:
                return False

        raise UserSearchException(f"Cannot find '{usr_info}' with role: {serial_number}")
        
    def search_users(self, usr_info, raise_e=True, timeout=10, validate_results=True):
        """
            Search users in user table by using either user name or Email id 
            Should display list of users based on search string, if search string match
            else should display No items found message.
        """
        self.driver.wait_for_object("search_user_inputbox",timeout=timeout, raise_e=raise_e)
        # self.driver.send_keys("search_user_inputbox", usr_info)
        # Press enter parameter is added , due to search enhancement.
        search = self.driver.send_keys("search_user_inputbox", usr_info,press_enter=True)
        
        if not validate_results:
            return search # use search field only, don't validate results

        if self.driver.find_object("table_entry_noitemsfound_warning_message",raise_e=False) is not False:
            table_entry_users=self.driver.find_object("table_entry_noitemsfound_warning_message")
            logging.info(table_entry_users.text)
            return False
        else:
            
            table_entry_emails = self.driver.find_object("table_entry_email",multiple=True)

            for i in range(len(table_entry_emails)):
                if usr_info.lower() in table_entry_emails[i].text.lower():
                    logging.info("email: " + table_entry_emails[i].text + " contains the searched string: " + usr_info)
                    continue
                else:
                    raise UserSearchException("email: " + table_entry_emails[i].text + " does not contain the searched string: " + usr_info)
        return True

    def get_sync_time_info(self):
        return self.driver.wait_for_object("table_reload_date_and_time_text", timeout=30).text

    def click_refresh_button(self):
        return self.driver.click("reload_btn")
    
    def click_search_clear_button(self):
        return self.driver.click("search_clear_btn")
    
    def click_remove_user(self):
        return self.driver.click("remove_user_btn")

    def verify_remove_user_success_notification(self, no_of_users):
        #verify positive  toast notification alert message 
        if no_of_users == 1:
            expected_text = "Successfully removed {} user." 
        else:
            expected_text = "Successfully removed {} users." 
        expected_alert_message= expected_text.format(no_of_users)
        actual_alert_message = self.get_toast_notification_text()
        self.compare_strings(expected_alert_message, actual_alert_message)
       
    def verify_email_invitation_sent_message(self):
        return self.driver.verify_object_string("success_alert")
       
    def get_toast_notification_text(self):
        self.driver.wait_for_object("success_alert")
        return self.driver.get_text("success_alert")

    def verify_remove_single_user(self, usr_info, timeout=10):
        """
            - This is method used to remove a specific user
            - If user doed not found it returns False
        """
        if self.search_users(usr_info, timeout=timeout):
            self.click_users_checkbox()
            sleep(5) #Wait for the contextual footer remove user dropdown to be clickable
            self.click_contextual_footer_remove_user_dropdown()
            self.select_contextual_footer_remove_user_option()
            self.click_contextual_footer_delete_button()
            self.click_removeuser_popup_remove_button()
            self.verify_remove_user_success_notification(1)

            # Auto clear is implemented,so commenting the below line.
            self.click_search_clear_button()

            # Verify and wait for users table data load
            self.wait_for(self.users_table_data_checkbox_load())

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
        self.driver.wait_for_object("table_entry_contextual-menu", timeout=timeout)
        obj = self.driver.find_object("table_entry_contextual-menu")
        ac.context_click(obj).perform()
        return True
    
    #######################    Contextual footer    ###############################
    def users_table_data_checkbox_load(self):
        return self.driver.wait_for_object("table_entry_checkbox")

    def click_users_checkbox(self):
        return self.driver.click("table_entry_checkbox")

    def verify_contextual_footer(self):
        return self.driver.wait_for_object("contextual_footer")
    
    def verify_contextual_footer_cancel_button(self):
        return self.driver.wait_for_object("contextual_footer_cancel_btn")

    def click_contextual_footer_cancel_button(self):
        return self.driver.click("contextual_footer_cancel_btn")

    def verify_contextual_footer_delete_button(self):
        return self.driver.wait_for_object("contextual_footer_delete_btn")

    def click_contextual_footer_delete_button(self):
        return self.driver.click("contextual_footer_delete_btn")

    def verify_contextual_footer_remove_user_dropdown(self):
        return self.driver.wait_for_object("contextual_footer_remove_user_dropdown")

    def click_contextual_footer_remove_user_dropdown(self):
        return self.driver.click("contextual_footer_remove_user_dropdown")


    ################ Remove user popup ##############################################
    def verify_removeuser_popup_title(self):
        return self.driver.verify_object_string("removeuser_popup_title")

    def verify_removeuser_popup_description(self):
        return self.driver.verify_object_string("removeuser_popup_desc")
        # return self.driver.verify_object_string("invite_remove_recipients_popup_desc_end_part")

    def verify_removeuser_popup_cancel_button(self):
        return self.driver.wait_for_object("removeuser_popup_cancel_btn")

    def verify_removeuser_popup_remove_button(self):
        return self.driver.wait_for_object("removeuser_popup_remove_btn")

    def click_removeuser_popup_cancel_button(self):
        return self.driver.click("removeuser_popup_cancel_btn")

    def click_removeuser_popup_remove_button(self):
        return self.driver.click("removeuser_popup_remove_btn")

    ########################### Invite Page ###########################
    #Will split these out info a different flow if needed 
    def select_option_from_role_dropdown(self, option):
        #Option is a number that matches the drop down in order (starting from 1)
        self.driver.click("invite_select_role_drop_down")
        self.driver.wait_for_object("invite_select_role_drop_down_option", format_specifier=[option])
        return self.driver.click("invite_select_role_drop_down_option", format_specifier=[option])

    def enter_emails_to_invite_txt_box(self, emails):
        return self.driver.send_keys("invite_email_address_text_box", emails)

    def click_send_invitation_button(self):
        return self.driver.click("invite_send_invitations_btn")

    def click_invite_button(self, timeout=30): 
        return self.driver.click("invite_btn", timeout=timeout)

    def click_invite_add_button(self):
        return self.driver.click("invite_user_add_btn")

    def click_all_users_tab(self):
        return self.driver.click("invite_all_users_breadcrumb")

    def click_invite_delete_recipient_button(self):
        return self.driver.js_click("invite_recipients_delete_button")

    def click_invite_edit_recipient_button(self):
        return self.driver.js_click("invite_recipients_edit_button") 

    ################################ Verify Invite User Screen ######################################################

    def verify_invite_user_tab(self):
        return self.driver.wait_for_object("invite_user_tab")
        
    def verify_invite_user_intro_txt(self):
        return self.driver.verify_object_string("invite_user_intro_txt",timeout=10)

    def verify_invite_user_role_label(self):
        return self.driver.verify_object_string("invite_user_role_label")
            
    def verify_invite_user_role_dropdown(self):
        return self.driver.wait_for_object("invite_select_role_drop_down")

    def verify_invite_user_email_address_label(self):
        return self.driver.verify_object_string("invite_user_email_address_label")

    def verify_invite_user_email_address_text_box(self):
        return self.driver.wait_for_object("invite_email_address_text_box")

    def verify_invite_user_add_button_is_disabled(self):
        if self.driver.find_object("invite_user_add_btn").is_enabled():
            raise UnexpectedItemPresentException("Add button is enabled")
        return True

    def verify_invite_user_add_button(self):
        return self.driver.wait_for_object("invite_user_add_btn")

    def verify_invite_user_total_recipient_is_zero(self):
        expected_value = "Total Recipients  |  0"
        actual_value = self.driver.find_object("invite_user_total_recipient_label").text
        self.compare_strings(expected_value, actual_value)
       
    def verify_invite_user_table(self):
        return self.driver.wait_for_object("invite_user_table")

    def verify_invite_user_table_column_email_address(self):
        return self.driver.wait_for_object("invite_user_table_heading_email")

    def verify_invite_user_table_column_role(self):
        return self.driver.wait_for_object("invite_user_table_heading_role")
        
    def verify_invite_user_table_is_empty(self):
        return self.driver.verify_object_string("invite_user_table_no_item")

    def verify_send_invitation_button_is_disabled(self): 
        if self.driver.find_object("invite_send_invitations_btn").is_enabled():
            raise UnexpectedItemPresentException(" Send button is enabled")
        return True

    def verify_send_invitation_button(self):
        return self.driver.wait_for_object("invite_send_invitations_btn")

    def get_invite_user_email_address_in_invite_user_table(self):
        return self.driver.get_text("invite_user_table_email_address")

    def verify_invite_user_add_button(self):
        return self.driver.wait_for_object("invite_user_add_btn")
   
    def verify_invite_edit_recipient_button(self):
        return self.driver.wait_for_object("invite_recipients_edit_button") 
    
    def verify_invite_delete_recipient_button(self):
        return self.driver.wait_for_object("invite_recipients_delete_button")

############################### Invite Failure Toast Notification #######################################################

    def get_active_users(self):
        self.click_table_header_by_name("status")
        active_users = []
        table_entry_users = self.driver.find_object("table_entry_row_user_section", multiple=True)
        for table_user_section in table_entry_users[1:]:
            username = self.driver.find_object("table_entry_username", root_obj=table_user_section)
            email = self.driver.find_object("table_entry_email", root_obj=table_user_section)
            if username.text != "-":
                active_users.append(email.text)
        if active_users==[]:
            raise UnableToFindActiveUserException("Unable to find any active users, make sure the account have at least 1 active user")
        return active_users

    def verify_single_user_invite_failure_msg(self, username, timeout=20):
        expected_failure_msg = "We couldn't send the invite to "+username+"."
        actual_failure_msg = self.get_toast_notification_text()
        self.compare_strings(expected_failure_msg, actual_failure_msg)
      
    def verify_invite_negative_toast_notification(self, usercount, active_users, timeout=20):
        if usercount == 1:
            username = "".join(active_users)
            self.verify_single_user_invite_failure_msg(username)
        else:
            expected_txt = "Unable to send invites for {} emails."
            expected_failure_msg = expected_txt.format(usercount)
            actual_failure_msg = self.get_toast_notification_text()
            self.compare_strings(expected_failure_msg, actual_failure_msg)
         
    def click_invite_negative_toast_notification_retry_button(self, timeout=10):
        return self.driver.click("invite_negative_toast_notification_retry_btn", timeout=timeout)

    def verify_failed_email_addresses(self, active_users):
        invite_user_table_emails = []
        invite_user_table_email_objects = self.driver.find_object("invite_user_table_email_address", multiple=True)
        for email in invite_user_table_email_objects:
            invite_user_table_emails.append(email.text)
        if(collections.Counter(active_users)==collections.Counter(invite_user_table_emails)):
            return True
        else:
            raise FailedEmailMismatchException("All failed emails didnt populated back to total recipient table")
            
    def click_invite_negative_toast_notification_close_button(self):
        return self.driver.click("invite_negative_toast_notification_close_btn")

    ############################ Invite Remove Recipient Pop-Up ############################

    def verify_invite_remove_recipient_popup(self):
        return self.driver.wait_for_object("invite_remove_recipients_popup_title")

    def verify_invite_remove_recipient_popup_desc(self):
        return self.driver.verify_object_string("invite_remove_recipients_popup_desc")
        # return self.driver.verify_object_string("invite_remove_recipients_popup_desc_end_part")
    
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
        recipient_label=self.driver.wait_for_object("invite_total_recipients_label").text
        return int(recipient_label.split(" ")[0])

    ############################ Unsaved Changes Pop-Up ############################

    def verify_unsaved_changes_popup(self):
        return self.driver.verify_object_string("unsaved_changes_popup_title")

    def verify_unsaved_changes_popup_desc(self):
        return self.driver.verify_object_string("unsaved_changes_popup_desc")
       
    def verify_unsaved_changes_popup_cancel_button(self):
        return self.driver.verify_object_string("unsaved_changes_popup_cancel_button")

    def verify_unsaved_changes_popup_leave_button(self):
        return self.driver.verify_object_string("unsaved_changes_popup_leave_button")

    def click_unsaved_changes_popup_cancel_button(self):
        return self.driver.click("unsaved_changes_popup_cancel_button")

    def click_unsaved_changes_popup_leave_button(self):
        return self.driver.click("unsaved_changes_popup_leave_button")
    
    ############################### Edit Recipient popup #######################################################

    def invite_edit_recipient_clear_email_text(self):
        return self.driver.clear_text("invite_edit_recipient_popup_email_address")
    
    def invite_edit_recipient_enter_email(self,emails):
        return self.driver.send_keys("invite_edit_recipient_popup_email_address", emails)
    
    def click_invite_edit_recipient_cancel_button(self):
        return self.driver.click("invite_edit_recipient_popup_cancel_button")

    def click_invite_edit_recipient_save_button(self):
        return self.driver.click("invite_edit_recipient_popup_save_button")  

    ############################### Verify Edit Recipient popup #######################################################

    def verify_invite_edit_recipient_popup(self):
        return self.driver.wait_for_object("invite_edit_recipient_popup")
                   
    def verify_invite_edit_recipient_email_address(self,expected_emailaddress):
        actual_emailaddress = self.driver.get_text("invite_edit_recipient_popup_email_address")
        self.compare_strings(expected_emailaddress, actual_emailaddress)

    def verify_invite_edit_recipient_default_role_dropdown(self):
        return self.driver.wait_for_object("invite_edit_recipient_popup_role_dropdown")
    
    def verify_invite_edit_recipient_cancel_button(self):
        return self.driver.wait_for_object("invite_edit_recipient_popup_cancel_button")

    def verify_invite_edit_recipient_save_button_disabled(self):
        #verify save button is disable
        if self.driver.find_object("invite_edit_recipient_popup_save_button").is_enabled():
            raise UnexpectedItemPresentException("save button is enabled")
        return True
    
    def verify_invite_edit_recipient_empty_email_error_message(self):
        expected_empty_email_error_message="This field cannot be blank"
        actual_empty_email_error_message=self.driver.get_text("invite_edit_recipient_email_error_msg")  
        self.compare_strings(expected_empty_email_error_message, actual_empty_email_error_message)
       
    def verify_invite_edit_recipient_invalid_email_error_message(self):
        expected_invalid_email_error_message="Invalid email address"
        actual_invalid_email_error_message=self.driver.get_text("invite_edit_recipient_email_error_msg")  
        self.compare_strings(expected_invalid_email_error_message, actual_invalid_email_error_message)
       
    def verify_check_box_is_disabled(self):
        #verify searched admin user checkbox is disabled
        if self.driver.find_object("table_entry_checkbox_disabled").is_enabled():
            raise UnexpectedItemPresentException(" Checkbox is enabled")
        return True
    
    def verify_remove_user_button_is_not_displayed(self, timeout):
        # Right click on serached user and verify the remove user option should not be there.
        self.select_user_click_mouse_right_button(timeout)
        return self.driver.wait_for_object("remove_user_btn", invisible=True)

    def verify_invite_user_invalid_email_error_message(self):
        expected_invalid_email_error_message="One or more of the entered email addresses is invalid."
        actual_invalid_email_error_message=self.driver.get_text("invite_user_email_address_error_msg")  
        self.compare_strings(expected_invalid_email_error_message, actual_invalid_email_error_message)
      
    def verify_is_invited_user_display_in_user_table(self, users):
        for user in users:
            if self.search_users(user, timeout=10):
                 self.click_search_clear_button()
            else:
                raise UserSearchException("Invited User is not showing in users table: "+user)
        return True
   
    def verify_is_user_removed(self, users,timeout=10):
        for user in users:
            if self.search_users(user, timeout=timeout):
                raise UserSearchException("User is not  deleted: "+user)
            else:
                logging.info("User successfully deleted: "+user)
                self.click_search_clear_button()
        return True

    def select_contextual_footer_remove_user_option(self):
       return self.driver.click("contextual_footer_dropdown_remove_user_option") 

    def remove_multiple_users(self, users, timeout=20):
        #Search user and click on check box
        for user in users:
            if self.search_users(user, timeout=timeout):
                self.click_users_checkbox()
                self.click_search_clear_button()
            
        #Remove selected users by click on Continue button
        self.click_contextual_footer_remove_user_dropdown()
        self.select_contextual_footer_remove_user_option()
        self.click_contextual_footer_delete_button()
        self.click_removeuser_popup_remove_button()
        return True

    def wait_for(self, condition_function):
        # Verify and wait for an object
        # If object is not found with in 2 min of time, it will through the Exception
        start_time = time.time()
        while time.time() < start_time + 30:
            if condition_function:
                return True
            else:
                time.sleep(5)
        raise Exception('Timeout waiting for {}'.format(condition_function.__name__))

    ############################### users count ################################################

    def get_users(self,user_type):
        # This method returns the active, pending and total users count
        active_users = 0
        pending_users = 0
        expired_users = 0
        self.driver.wait_for_object("_shared_table_entries",timeout=30)
        self.select_page_size_new("100")
        max_pages=self.get_max_page()
        for page in range(max_pages):
            self.select_page(page+1)
            status_column = self.get_header_index("status")
            role_column = self.get_header_index("role")
            status_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[status_column],multiple=True)
            role_list = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[role_column],multiple=True)
            for index in range(len(status_list)):
                status = status_list[index].text
                role = role_list[index].text
                if 'Active' in status and user_type in role:
                    active_users+=1
                if 'Pending' in status and user_type in role:
                    pending_users+=1
                if 'Expired' in status and user_type in role:
                    expired_users+=1
        users_page_user_count = {"active" : active_users, "pending" : pending_users, "expired" : expired_users, "total_count" : active_users+pending_users+expired_users}
        return users_page_user_count

    def get_total_users_count(self):
        total_users=self.driver.wait_for_object("users_total_users_count").text
        return int(total_users.split("of ")[1])

    ################################## Filter Side Bar ##################################################

    def click_users_filter_button(self):
        return self.driver.click("my_organization_filter_button")

    def verify_filter_side_bar_title(self):
        return self.driver.verify_object_string("filter_side_bar_title")

    def click_filter_side_bar_close_button(self):
        return self.driver.click("filter_side_bar_close_btn")

    def select_filter(self,filter_name):
        filter_options = self.driver.find_object("built_in_filter_options", multiple = True)
        for i in range(len(filter_options)):
            if filter_options[i].text == filter_name:
                filter_options[i].click()

    def verify_filter_in_users_table(self,filter_name):
        if filter_name == "Active" or filter_name == "Pending" or filter_name == "Expired":
            header_index = self.get_header_index("status")
        else:
            header_index = self.get_header_index("role")

        if self.driver.wait_for_object("users_table_no_users_lbl",raise_e=False) is not False:
            return False
        else:
            table_entry_data = self.driver.find_object("users_table_data",format_specifier=[header_index],multiple=True)
            for i in range(len(table_entry_data)):
                if filter_name in table_entry_data[i].text:
                    continue
                else:
                    raise FilterValueException("Table value: " + table_entry_data[i].text+ " does not contains the filter value: " + filter_name)
        return True

    ############################### Import Users Popup ################################################

    def click_invite_user_import_button(self):
        return self.driver.click("invite_user_import_btn")

    def verify_import_users_popup(self,displayed=True):
        return self.driver.wait_for_object("import_user_popup_title", invisible=not displayed)

    def verify_import_users_popup_title(self):
        return self.driver.verify_object_string("import_user_popup_title")

    def verify_import_users_popup_description(self):
        return self.driver.verify_object_string("import_user_popup_description")

    def verify_import_users_popup_browse_label(self):
        return self.driver.verify_object_string("import_user_popup_browse_label")

    def verify_import_users_popup_sample_file_download_link(self):
        return self.driver.verify_object_string("import_user_popup_sample_file_download_link")

    def verify_import_users_popup_cancel_button(self):
        return self.driver.verify_object_string("import_user_popup_cancel_button")

    def click_import_users_popup_cancel_button(self):
        return self.driver.click("import_user_popup_cancel_button")

    def verify_import_users_popup_import_button_status(self,status):
        save_button=self.driver.wait_for_object("import_user_popup_import_button")
        if status == "disabled":
            if save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button  is enabled")
            return True
        else:
            if not save_button.is_enabled():
                raise UnexpectedItemPresentException(" Save button is disabled")
            return True

    ################################## Column Options Popup ##################################################

    def click_users_column_options_gear_button(self):
        return self.driver.click("users_column_option_gear_button",timeout=30)

    def verify_column_options_popup_title(self):
        return self.driver.verify_object_string("column_option_popup_title")

    def get_column_options_popup_options(self):
        actual_options = []
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        for option in options:
            actual_options.append(option.text)
        return actual_options

    def verify_column_options_popup_reset_to_default_button(self):
        return self.driver.verify_object_string("column_options_popup_reset_to_default_btn")

    def verify_column_options_popup_cancel_button(self):
        return self.driver.verify_object_string("column_options_popup_cancel_btn")

    def verify_column_options_popup_save_button(self):
        return self.driver.verify_object_string("column_options_popup_save_btn")

    def click_column_options_popup_cancel_button(self):
        return self.driver.click("column_options_popup_cancel_btn")

    def click_column_options_popup_save_button(self):
        return self.driver.click("column_options_popup_save_btn")

    def click_column_option(self,option):
        options = self.driver.find_object("column_option_popup_options", multiple = True)
        if option == "EMAIL ADDRESS":
            options[1].click()
        elif option == "ROLE":
            options[2].click()
        elif option == "STATUS":
            options[3].click()

    def verify_users_tabel_column(self,column_name,displayed=True):
        return self.driver.wait_for_object(column_name+"_table_header", invisible=not displayed)

    ######################### Resend Invitation popup #########################################

    def click_resend_invitation_option(self):
        return self.driver.click("resend_invitation_option")
    
    def verify_resend_invitation_popup_title(self):
        return self.driver.verify_object_string("resend_invitation_popup_title")

    def verify_resend_invitation_popup_desc(self):
        return self.driver.verify_object_string("resend_invitation_popup_desc")

    def verify_resend_invitation_popup_cancel_button(self):
        return self.driver.verify_object_string("resend_invitation_popup_cancel_btn")

    def verify_resend_invitation_popup_send_invitation_button(self):
        return self.driver.verify_object_string("resend_invitation_popup_send_invitation_btn")

    def click_resend_invitation_popup_cancel_button(self):
        return self.driver.click("resend_invitation_popup_cancel_btn")

    def click_resend_invitation_popup_send_invitation_button(self):
        return self.driver.click("resend_invitation_popup_send_invitation_btn")

    def resend_invitation(self,usr_info):
        if self.search_users(usr_info):
            self.click_users_checkbox()
            #Resend invitaion to selected user
            self.click_contextual_footer_remove_user_dropdown()
            self.click_resend_invitation_option()
            self.click_contextual_footer_delete_button()

            # Verify Resend invitaion popup UI
            self.verify_resend_invitation_popup_title()
            # self.verify_resend_invitation_popup_desc()
            self.verify_resend_invitation_popup_cancel_button()
            self.verify_resend_invitation_popup_send_invitation_button()
            self.click_resend_invitation_popup_send_invitation_button()
        else:
            raise UserSearchException("No user found with email: "+usr_info)

    ############################### Assign Role popup #########################################

    def click_assign_role_option(self):
        return self.driver.click("assign_role_option")

    def verify_assign_role_popup_title(self):
        return self.driver.verify_object_string("assign_role_popup_title")

    def verify_assign_role_popup_desc(self):
        return self.driver.verify_object_string("assign_role_popup_desc")

    def verify_assign_role_popup_select_role_dropdown(self):
        return self.driver.wait_for_object("assign_role_popup_select_role_dropdown")

    def verify_assign_role_popup_cancel_button(self):
        return self.driver.verify_object_string("assign_role_popup_cancel_btn")

    def verify_assign_role_popup_confirm_button(self):
        return self.driver.verify_object_string("assign_role_popup_confirm_btn")

    def click_assign_role_popup_cancel_button(self):
        return self.driver.click("assign_role_popup_cancel_btn")

    def get_user_role(self,user):
        if self.search_users(user):
            return self.driver.wait_for_object("table_entry_role").text
        else:
            raise UserSearchException("User is not showing in users table: "+user)

    def click_assign_role_popup_select_role_dropdown(self):
        return self.driver.click("assign_role_popup_select_role_dropdown")

    def update_user_role(self, user_role):
        self.click_assign_role_popup_select_role_dropdown()
        if user_role == "IT Admin":
            return self.driver.click("assign_role_popup_select_role_dropdown_end_user_option")
        return self.driver.click("assign_role_popup_select_role_dropdown_it_admin_option")

    def click_assign_role_popup_confirm_button(self):
        return self.driver.click("assign_role_popup_confirm_btn")

    def verify_assign_role_success_toast_notification(self, no_of_users):
        if no_of_users == 1:
            expected_text = "Successfully assigned role to {} user. " 
        else:
            expected_text = "Successfully assigned roles to {} users." 
        expected_alert_message= expected_text.format(no_of_users)
        actual_alert_message = self.get_toast_notification_text()
        self.compare_strings(expected_alert_message, actual_alert_message)

    def assign_role_to_user(self,usr_info,user_role):
        if self.search_users(usr_info):
            self.click_users_checkbox()

            #Assign Role to selected user
            self.click_contextual_footer_remove_user_dropdown()
            self.click_assign_role_option()
            self.click_contextual_footer_delete_button()

            # Verify Assign role popup UI
            self.verify_assign_role_popup_title()
            self.verify_assign_role_popup_desc()
            self.verify_assign_role_popup_cancel_button()
            self.update_user_role(user_role)
            self.click_assign_role_popup_confirm_button()
            self.verify_assign_role_success_toast_notification(1)
        else:
            raise UserSearchException("No user found with email: "+usr_info)
    
    def verify_invite_user_idp_message(self):
        return self.driver.verify_object_string("invite_user_idp_message")