import re
import json
import pytest
import string
import random
import logging
import datetime
import MobileApps.resources.const.web.const as w_const

from time import sleep, time
from selenium.common.exceptions import WebDriverException, ElementClickInterceptedException
from SAF.exceptions.saf_exceptions import WindowNotFound
from SAF.misc import saf_misc
from SAF.decorator.saf_decorator import screenshot_capture
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.web_flow import WebFlow
from MobileApps.resources.const.android.const import TEST_DATA

from MobileApps.libs.flows.email.gmail_api import GmailAPI, CONST

class EmailVerificationFailed(Exception):
    pass

class HPID(WebFlow):
    project = "hp_id"
    flow_name="hp_id"

    def verify_hpid(self, timeout=10):
        return self.driver.wait_for_object("hpid_header", timeout=timeout)

    def verify_create_account_link(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("create_account_link", timeout=timeout, raise_e=raise_e)

    def verify_hpid_popup_window(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("hpid_popup_window", timeout=timeout, raise_e=raise_e)

    def verify_privacy_link(self, timeout=10, invisible=False):
        return self.driver.wait_for_object("privacy_link", timeout=timeout, invisible=invisible)

    def verify_hpid_password_textbox(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("sign_in_password_txt_box", raise_e=True, timeout=timeout)

    def verify_hpid_next_button(self, raise_e=True, timeout=10):
        return self.driver.wait_for_object("sign_in_next_btn", raise_e=raise_e, timeout=timeout)

    def click_hpid_next_button(self):
        return self.driver.click("sign_in_next_btn")

    @screenshot_capture(file_name="signin.png")
    def verify_hp_id_sign_in(self, raise_e=True, skip_hpid_popup=False, timeout=45):
        """
        Based on version 09/11 of sign in screen via Chrome browser, not sure for element "sign_in_page_identify_object"
        :param raise_e:
        :return:
        """
        if not skip_hpid_popup and pytest.platform != "MAC":
            self.handle_privacy_popup()
        return self.driver.wait_for_object("sign_in_username_txt_box", timeout=timeout, raise_e=raise_e)

    def handle_privacy_popup(self, timeout=3, delay=None):
        if self.driver.wait_for_object("privacy_pop_up", timeout=timeout, raise_e=False) is not False:
            self.driver.click("privacy_accept_btn", timeout=timeout, delay=delay)
        if self.driver.wait_for_object("more_pop_up", timeout=timeout, raise_e=False) is not False:
            self.driver.click("more_pop_up", timeout=timeout, delay=delay)
        if self.driver.wait_for_object("privacy_pop_up", timeout=timeout, raise_e=False) is not False:
            self.driver.click("privacy_accept_btn", timeout=timeout, delay=delay)
        return True
    
    def verify_privacy_popup(self, timeout=10, accept=True):
        self.driver.wait_for_object("privacy_pop_up", timeout=timeout)
        self.driver.wait_for_object("privacy_more_options_btn", timeout=timeout)
        if accept:
            self.driver.click("privacy_accept_btn", timeout=timeout)

    @screenshot_capture(file_name="signup.png")
    def verify_hp_id_sign_up(self, timeout=10, raise_e=True):
        self.handle_privacy_popup()
        return self.driver.wait_for_object("sign_up_form_firstname_txtbx", timeout=timeout, raise_e=raise_e)

    def login(self, username=None, password=None, clear_username_textbox=False, email_verification_timeout=120, send_before_click=True):
        """
        Login to an account
        Note: Tested the flow of version 09/11 on via Chrome browser
        :param username: Username of the account, if None uses driver.session_data["hpid_user"]
            Must pass username and password together or leave both blank
        :param password: Password for the account, if None uses driver.session_data["hpid_pass"]
            Must pass username and password together or leave both blank
        :param change_check: change_check dictionary for clicking the sign in button
        :return:
        """
        if username is None and password is None:
            username = self.driver.session_data["hpid_user"]
            password = self.driver.session_data["hpid_pass"]
        elif username is None or password is None:
            raise ValueError("Must pass username and password or leave both as None")
        if self.driver.wait_for_object("sign_in_password_txt_box", interval=0.2, timeout=2, raise_e=False):
            if not self.driver.wait_for_object("entered_username_text", format_specifier=[username], timeout=2, raise_e=False):
                self.driver.click("back_btn")
                clear_username_textbox = True
        if self.driver.wait_for_object("sign_in_username_txt_box", interval=0.2, timeout=60, raise_e=False):
            if send_before_click:
                try:
                    self.driver.click("sign_in_username_txt_box", interval=0.2)
                except ElementClickInterceptedException:
                    logging.debug("ElementClickInterceptedException caught, clicking the label which basically has the desired effect")
                    self.driver.click("sign_in_text_box_label", interval=0.2)
            if clear_username_textbox and pytest.platform != "MAC":
                self.driver.selenium.js_clear_text("sign_in_username_txt_box")
            elif clear_username_textbox:
                self.driver.js_clear_text("sign_in_username_txt_box")
            self.driver.send_keys("sign_in_username_txt_box", username)
            self.driver.click("sign_in_next_btn", interval=0.2)
            if self.driver.wait_for_object("use_password_btn", interval=0.2, timeout=2, raise_e=False):
                self.driver.click("use_password_btn", interval=0.2)
        
        self.driver.performance.time_stamp("t7")
        self.driver.wait_for_object("sign_in_password_txt_box", interval=0.2, timeout=60)
        self.driver.performance.time_stamp("t8")
        self.driver.click("sign_in_password_txt_box", interval=0.2)
        self.driver.send_keys("sign_in_password_txt_box", password)
        self.driver.click("sign_in_button", interval=0.2)
        if pytest.platform != "MAC":
            self.email_verification(username, email_verification_timeout=email_verification_timeout)
        sleep(1)
        try:
            if pytest.platform != "MAC":
                self.handle_login_dialog_continue()
        except WebDriverException:
            logging.debug("Handling IOS failing here")
        self.dismiss_login_dialog_continue_popup(timeout=3)
        self.driver.performance.start_timer("hpid_login")
        self.driver.performance.time_stamp("t9")
        if self.driver.driver_type == "windows":
            self.verify_privacy_link(invisible=True)


    def handle_relogin_with_pwd(self, password=None):
        self.driver.wait_for_object("sign_in_password_txt_box", interval=1, timeout=10)
        self.driver.performance.time_stamp("t8")
        self.driver.click("sign_in_password_txt_box")
        self.driver.send_keys("sign_in_password_txt_box", password)
        self.driver.click("sign_in_button")
        self.handle_login_dialog_continue()

    def handle_login_dialog_continue(self):
        if pytest.platform.lower() == "android" and pytest.app_info.lower() == "smart":
            sleep(2)
            hpid_url = w_const.WEBVIEW_URL.HPID(self.driver.session_data["request"].config.getoption("--stack"))
            if self.driver.wait_for_context(hpid_url, timeout=5, raise_e=False) != (None, None):
                self.driver.performance.time_stamp("t9.1")
                self.dismiss_login_dialog_continue_popup()
                self.driver.performance.time_stamp("t9.2")
        return True

    def click_create_account_link(self):
        #Clicking the don't have an account link at the enter account page
        self.driver.wait_for_object("create_account_link", timeout=20)
        self.driver.click("create_account_link", change_check={"wait_obj": "create_account_link", "invisible": True})

    def click_create_account_button(self):
        self.driver.click("create_account_link")
    
    def click_sign_in_link_from_create_account(self):
        self.driver.wait_for_object("sign_in_link_from_create_account").click()

    def click_back_button(self):
        """
        Back button is present after having inputing an email to the hpid login page and selecting next
        """
        self.driver.click("back_btn")

    def create_account(self, firstname="test", lastname="test", email=None, password="123456aA", gmail=None, email_verification_timeout=120):
        """
        This method is for when you are at the HP ID sign up screen walk through the sign up form
        Required param of printer_serial and stack is for updating in the database for proper clean up
        @param gmail: GmailAPI -> used for another gmail token besides default one
        """
        self.driver.wait_for_object("enter_email_address")
        if not email:
            username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]
            domain = username.split("@")[1]
            # use + to create sub email from main email account
            # Adding a tiny salt to avoid collision further
            salt = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6)) 
            email = "{}+{:%Y_%m_%d_%H_%M_%S}_{}@{}".format(username[0:username.rfind("@")], datetime.datetime.now(), salt, domain)
        logging.info("Sign up email: " + email)
        self.driver.send_keys("enter_email_address", email, check_key_sent=True)
        self.driver.wait_for_object("next_btn")
        self.driver.click("next_btn", change_check={"wait_obj": "next_btn", "invisible": True})
        self.driver.wait_for_object("first_name_box")
        self.driver.send_keys("first_name_box", firstname)
        self.driver.send_keys("last_name_box", lastname)
        self.driver.click("use_password_btn", change_check={"wait_obj": "use_password_btn", "invisible": True})
        self.driver.send_keys("sign_up_form_create_password", password)
        #V3 version have confirm password
        if self.driver.wait_for_object("sign_up_form_confirm_password", timeout=3, raise_e=False):
            self.driver.send_keys("sign_up_form_confirm_password", password)
        logging.info("Sign up password: " + password)
        if pytest.platform.lower() == "windows":
            self.driver.click("sign_up_form_email_txtbx")
        captcha_iframe = self.driver.wait_for_object("captcha_iframe", timeout=3, raise_e=False)
        if captcha_iframe is not False:
            self.driver.wdvr.switch_to_frame(captcha_iframe)    
            self.driver.click("captcha_check_box")
            self.driver.wdvr.switch_to_default_content()  
        if pytest.platform.lower() == "windows" and self.verify_hpid_popup_window(raise_e=False):
                self.driver.swipe("sign_up_form_create_account_button")      
        self.driver.click("sign_up_form_create_account_button", change_check={"wait_obj": "sign_up_form_create_account_button", "invisible": True})

        self.driver.performance.start_timer("hpid_create_account")
        try:
            self.driver.wait_for_object("sign_up_form_create_account_button", invisible=True, timeout=3)
        except WebDriverException:
            sleep(3)
        self.email_verification(email, email_verification_timeout=email_verification_timeout, gmail=None)
        if pytest.platform != "IOS":  # flow not in IOS
            if self.driver.wait_for_object("country_region_label", raise_e=False):
                self.driver.click("continue_btn", change_check={"wait_obj": "continue_btn", "invisible": True}, timeout=10)
        self.dismiss_login_dialog_continue_popup(timeout=5)
        return email, password

    def email_verification(self, email, gmail=None, raise_e=False, timeout=3, email_verification_timeout=120, retry=3):
        verified = False
        verify_required = False
        for _ in range(retry):
            try:
                #Edit Email button exists on Verify Email address screen for both Existing and New HPID account. Once developer add unique ID for tile "Verify email address". We can verify title string
                verify_required = self.driver.wait_for_object("edit_email_btn", timeout=timeout, raise_e=False) is not False
                break
            except (WebDriverException, WindowNotFound):
                logging.debug("Possible the window closed for mobile testing so catching it here")
                return False

        if verify_required:
            self.driver.click("send_email_btn", timeout=3, raise_e=False)
            sent_time = round(time()) - 600
            gmail_api = GmailAPI(credential_path=TEST_DATA.GMAIL_TOKEN_PATH) if not gmail else gmail
            if pytest.platform.lower() == "web":
                code = gmail_api.get_content_from_email(CONST.HPID_VERIFICATION_EMAIL, email, sent_time, q_from="HP ID Support", timeout=65, raise_e=False)
                if code is False:
                    logging.info("clicking resend verification code btn")
                    self.driver.click("resend_verification_code_btn")
                    code = gmail_api.get_content_from_email(CONST.HPID_VERIFICATION_EMAIL, email, sent_time, q_from="HP ID Support", timeout=60)
            else:
                code = gmail_api.get_content_from_email(CONST.HPID_VERIFICATION_EMAIL, email, sent_time, q_from="HP ID Support", timeout=email_verification_timeout) 
            self.driver.wait_for_object("verification_code_txt_box", timeout=3)
            self.driver.send_keys("verification_code_txt_box", code)
            if pytest.platform.lower() == "windows" and self.verify_hpid_popup_window(raise_e=False):
                self.driver.swipe("verification_code_submit_btn")
            self.driver.click("verification_code_submit_btn", change_check={"wait_obj": "verification_code_txt_box", "invisible": True})
            verified = True

        
        if not verified and raise_e is True:
            raise EmailVerificationFailed("Expecting the email verification but the text box did not show up")

        return verified

    def dismiss_account_verification_again(self, gmail=None, timeout=10):
        """
        Dismiss Account Verification by sending email again:
            - Click on Send Email button
            - Using dismiss_verification_email_screen() to verify account
        @param gmail: GmailAPI
        """
        if self.driver.wait_for_object("send_email_msg_txt", timeout=timeout, raise_e=False):
            gmail = GmailAPI(credential_path=TEST_DATA.GMAIL_TOKEN_PATH) if not gmail else gmail
            email = re.search("\S+@\S+", self.driver.find_object("send_email_msg_txt").text).group(0)[:-1]
            # Delete all previous emails for verification code which have the same 'to' email
            gmail.delete_hpid_verification_code_email(to=email)
            self.driver.click("send_email_btn")
            self.dismiss_verification_email_screen(gmail, to=email)
    
    def dismiss_login_dialog_continue_popup(self, timeout=15):
        """
        Login Continue Dialog  popup displays when user use chrome browser to Sign In which the chrome browser version is 99 or above. Details can refer user story: https://hp-jira.external.hp.com/browse/AIOA-13177
        """
        if pytest.platform != "IOS":
            if self.driver.wait_for_object("login_help_dialog_continue_btn", timeout=timeout, raise_e=False):
                self.driver.click("login_help_dialog_continue_btn", change_check={"wait_obj": "login_help_dialog_continue_btn", "invisible": True})

    def create_account_and_save_credentials(self, key_name, file_path):
        """
        A utility function. Not required to be used in test runs. 
        This function just creates a HPID acc and saves Credentials to already existing file.
        Function Only updates already exisiting file (r+) and will not create a new file if the file does not already exists(w+).
        """ 
        email, password = self.create_account()
        credentials = {"username":email, "password":password}
        f = open(file_path)
        data = json.load(f)
        data[key_name] = credentials
        f.close()
        fw = open(file_path, "r+")
        fw.write(json.dumps(data, indent=4))
        fw.close()
    
    def click_dialog_close_btn(self):
        self.driver.click("dialog_close_btn")

    def click_popup_close_btn(self):
        self.driver.click("popup_close_btn", displayed=False)

    def click_sign_up_link(self):
        """
        From the sign in page, select the 'Sign Up' link found below the sign in prompt
        """
        self.driver.click("sign_up_link")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************

    def verify_invalid_credential_msg(self):
        """
        Verify invisible invalid credential message after logging in with invalid account
        """
        self.driver.wait_for_object("invalid_credential_msg", timeout=10)

    def verify_create_an_account_page(self, timeout=3, visible=False):
        """
        verify the create an HP account page
        """
        if self.driver.wait_for_object("create_your_hp_account_button", raise_e=False, timeout=timeout) is True:
            return True
        else:
            return self.driver.wait_for_object("create_your_hp_account_button", raise_e=False, displayed=visible, timeout=timeout) is not False

    def verify_login(self, username=None, password=None):
        self.login(username, password)
        self.verify_privacy_link(invisible=True)

    def verify_unable_to_create_account(self, email, firstname="test", lastname="test", password="123456aA"):
        """
        Verifies that the user cannot create a new account with the 
        credential of an existing account
        """
        self.verify_create_an_account_page()
        self.driver.wait_for_object("sign_up_form_firstname_txtbx")
        self.driver.send_keys("sign_up_form_firstname_txtbx", firstname)
        self.driver.send_keys("sign_up_form_lastname_txtbx", lastname)
        self.driver.send_keys("sign_up_form_email_txtbx", email)
        self.driver.send_keys("sign_up_form_create_password", password)
        if pytest.platform.lower() == "windows" and self.verify_hpid_popup_window(raise_e=False):
            self.driver.swipe("sign_up_form_create_account_button")  
        self.driver.click("create_your_hp_account_button", raise_e=False, timeout=3)
        self.driver.wait_for_object("account_exists_alert")

    def click_sign_in_with_mobile_number_btn(self):
        self.driver.wait_for_object("sign_in_with_mobile_number_btn", timeout=10)
        self.driver.click("sign_in_with_mobile_number_btn")

    def enter_username(self, username):
        self.driver.send_keys("sign_in_username_txt_box", username)

    def enter_password(self, password=None):
        self.driver.send_keys("sign_in_password_txt_box", password)

    def click_sign_in_button(self):
        self.driver.wait_for_object("sign_in_button").click()

    def enter_mobile_number(self, mobile_number):
        self.driver.send_keys("mobile_number_txt_box", mobile_number)

    def verify_mobile_number_field_accepts_only_numbers(self):
        self.driver.wait_for_object("country_iso_code")
        self.driver.click("country_iso_code")
        self.driver.wait_for_object("search_for_country_iso_code")
        self.driver.send_keys("search_for_country_iso_code", "India")
        self.driver.wait_for_object("country_iso_code_india")
        self.driver.click("country_iso_code_india")
        self.driver.wait_for_object("mobile_number_txt_box")
        valid_input = "1234567890"
        self.enter_mobile_number(valid_input) # verifying valid number 1st
        entered_value = self.driver.wait_for_object("mobile_number_txt_box").text #(222) 222-2222
        entered_digits = re.sub(r"[()\-\s]","" ,entered_value)
        assert entered_digits.isdigit(), f"Mobile number field accepted non-numeric"
        self.driver.wait_for_object("mobile_number_txt_box").clear()
        invalid_inputs = ["abc", "123abc", "!@#"]
        for value in invalid_inputs:
            self.enter_mobile_number(value)
            entered_value = self.driver.wait_for_object("mobile_number_txt_box").text
            if entered_value == value:
                assert False, f"Mobile number field accepted invalid input: {value}"
            self.driver.wait_for_object("mobile_number_txt_box").clear()

    def click_sign_up_form_create_account_button(self):
        self.driver.swipe("sign_up_form_create_account_button")
        self.driver.wait_for_object("sign_up_form_create_account_button")
        self.driver.click("sign_up_form_create_account_button")

    def enter_first_name(self, firstname="test"):
        self.driver.wait_for_object("sign_up_form_firstname_txtbx")
        self.driver.send_keys("sign_up_form_firstname_txtbx", firstname)
    
    def enter_last_name(self, lastname="test"):
        self.driver.wait_for_object("sign_up_form_lastname_txtbx")
        self.driver.send_keys("sign_up_form_lastname_txtbx", lastname)

    def enter_email_adress(self, email, timeout=20):
        self.driver.wait_for_object("enter_your_email_txtbx", timeout=timeout)
        self.driver.send_keys("enter_your_email_txtbx", email)
        
    def click_use_password_btn(self, timeout=20):
        self.driver.wait_for_object("use_password_btn", timeout=timeout)
        self.driver.click("use_password_btn")

    def verify_enter_your_first_name_error(self, timeout=20, raise_e=False):
        if self.driver.wait_for_object("enter_your_first_name_error", timeout=timeout, raise_e=raise_e):
            return True
        return False

    def verify_enter_your_last_name_error(self, timeout=20, raise_e=False):
        if self.driver.wait_for_object("enter_your_last_name_error", timeout=timeout, raise_e=raise_e):
            return True
        return False

    def verify_enter_your_email_error(self, timeout=20, raise_e=False):
        if self.driver.wait_for_object("enter_your_email_error", timeout=timeout, raise_e=raise_e):
            return True
        return False

    def verify_create_your_password_error(self, timeout=20, raise_e=False):
        if self.driver.wait_for_object("create_your_password_error", timeout=timeout, raise_e=raise_e):
            return True
        return False


    def verify_forgot_your_user_name_link(self):
        return self.driver.wait_for_object("forgot_your_user_name_link")

    def click_forgot_your_user_name_link(self):
        self.driver.click("forgot_your_user_name_link")

    def verify_and_recover_your_user_name(self, username_to_recover=None):
        self.driver.wait_for_object("recover_username")
        if username_to_recover is None:
            username_to_recover = self.driver.session_data["hpid_user"]
        self.driver.send_keys("recover_username", username_to_recover)

    def click_recover_username_next_btn(self):
        self.driver.wait_for_object("recover_username_next_btn").click()

    def verify_username_recovery_success(self):
        return self.driver.wait_for_object("username_recovery_success_msg")

    def verify_forgot_your_password_link(self):
        return self.driver.wait_for_object("forgot_your_password_link")

    def click_forgot_your_password_link(self):
        self.driver.click("forgot_your_password_link")

    def click_privacy_link(self):
        self.driver.click("privacy_link")

    def verify_privacy_policy_page(self):
        return self.driver.wait_for_object("privacy_statement_title",timeout=20)

    def validate_password_requirements(self, password):
        """
        Validates that the password meets the following requirements:
        - Minimum 8 characters
        - At least 1 uppercase letter
        - At least 1 lowercase letter
        - At least 1 number
        - At least 1 special character
         at least 3 out of the 4 requirements
        """

        if len(password) < 8:
            return False
        count = 0
        if re.search(r"[A-Z]", password):
            count += 1
        if re.search(r"[a-z]", password):
            count += 1
        if re.search(r"[0-9]", password):
            count += 1
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            count += 1
        if count >= 3:
            return True

    def validate_password(self, password):
        if self.validate_password_requirements(password):
            return True
        else:
            return False

    def navigate_to_password_form_on_create_account_page(self, email="hpx.windows_rcb@example.com", first_name="HPX", last_name="Windows"):
        """Navigate through create account page to password creation form."""
        self.enter_email_adress(email)
        self.click_hpid_next_button()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.click_use_password_btn()

class MacHPID(HPID):

    def click_create_account_link(self):
        if not self.driver.wait_for_object("create_account_link", timeout=20, raise_e=False):
            self.driver.click("back_btn")
        self.driver.click("create_account_link", change_check={"wait_obj": "create_account_link", "invisible": True})
