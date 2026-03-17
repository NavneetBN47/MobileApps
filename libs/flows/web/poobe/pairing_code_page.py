from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare, string_validation
from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.web.hp_id.hp_id import HPID


class PairingCodePage(OWSFlow):
    """
        Contains all of the elements and flows associated with Portal OOBE Account Type Page giving user option to select how to setup the printer 
        Business or Personal
    """
    file_path = __file__
    flow_name = "pairing_code_page"

    def __init__(self, driver, *args, **kwargs):
        super(PairingCodePage, self).__init__(driver, *args, **kwargs)
        self.hpid = HPID(driver)

########################################################################################################################
#                                                  Action Flows                                                        #
########################################################################################################################

    def input_pairing_code(self, code):
        """
        Takes pairing code element and index for each individual box
        As per the pairing code page design each letter of code to be entered individually 
        """
        for index, value in enumerate(code, 1):
            self.driver.send_keys("pairing_code_box_{}".format(index), value)
        return code

    def get_pairing_code_value(self):
        """
        Get value of each pairing code box
        """
        code = ""
        for index in range(1, 9):
            res = code + self.driver.get_attribute("pairing_code_box_{}".format(index), "value")
        return res

    def clear_entered_code(self):
        """
        Clear each character from each individual character box
        """
        for i in range(1,9):
            self.driver.send_keys("pairing_code_box_{}".format(i), Keys.BACKSPACE)

    def click_cant_find_pairing_code_btn(self):
        self.hpid.handle_privacy_popup(timeout=5)
        self.load_ows_shared_ui()
        self.driver.click("cant_find_the_pairing_code_btn")

    def click_cant_find_pairing_code_modal_close_btn(self):
        self.driver.click("can_t_find_pairing_code_modal_close_button_text")
    
    def click_get_help_finding_pairing_code_modal_close_btn(self):
        self.driver.click("get_help_finding_pairing_code_modal_close_btn")

    def click_ecp_smb_hp_support_from_cat_find_pairing_code_modal(self):
        self.driver.click("cant_find_pairing_code_modal_hp_support")

    def click_lf_hp_support_from_cat_find_pairing_code_modal(self):
        self.driver.click("cant_find_pairing_code_modal_hp_support_lf")
    
    def click_continue_btn(self):
        self.driver.click("continue_button_text", change_check={"wait_obj": "continue_button_text", "invisible": True})

########################################################################################################################
#                                            Verification Flows                                                        #
########################################################################################################################

    @screenshot_compare(root_obj="full_page_pairing_code_page", include_param=["--printer-profile", "--printer-biz-model"])
    @screenshot_compare(root_obj="pairing_code_page", include_param=["--printer-profile", "--printer-biz-model"])
    def verify_pairing_code_screen(self, raise_e=True, timeout=10):
        """
        Verify pairing code page
        """
        self.load_ows_shared_ui()
        self.driver.wait_for_object("pairing_code_page", raise_e=raise_e, timeout=timeout)

    @string_validation("header")
    @string_validation("description")
    @string_validation("pairing_input_label")
    @string_validation("notes")
    def verify_pairing_code_page_header_description(self, raise_e=False):
        self.driver.wait_for_object("header")
    
    def verify_cant_find_pairing_code_madal_btn(self):
        """
        Can't find the pairing code ? button is present on Pairing Code page just under the Input box.
        """
        self.driver.wait_for_object("cant_find_the_pairing_code_btn")

    @screenshot_compare(root_obj="cant_find_pairing_code_modal", include_param=["--printer-profile", "--printer-biz-model"])
    def verify_get_help_finding_pairing_code_modal(self, timeout=15):
        self.driver.wait_for_object("get_help_finding_pairing_code_modal_header", timeout=timeout)
        self.driver.wait_for_object("get_help_finding_pairing_code_modal_body")
        self.driver.wait_for_object("get_help_connect_printer_to_network_to_get_pairing_code_btn")
        self.driver.wait_for_object("get_help_get_pairing_code_ews_btn")

    def verify_single_sku_pairing_code_page_follow_steps(self):
        self.driver.wait_for_object("single_sku_pairing_code_page_follow_steps")
    
    @string_validation("cant_find_pairing_code_title")
    @string_validation("can_t_find_pairing_code_modal_body")
    @string_validation("can_t_find_pairing_code_modal_close_button_text")
    def verify_cant_find_pairing_code_modal(self, raise_e=False):
        self.driver.wait_for_object("cant_find_pairing_code_title")
        self.driver.wait_for_object("can_t_find_pairing_code_modal_body")
        self.driver.wait_for_object("can_t_find_pairing_code_modal_close_button_text")
    
    def verify_ecp_smb_hp_support_from_cat_find_pairing_code_modal(self):
        self.driver.wait_for_object("cant_find_pairing_code_modal_hp_support")

    def verify_lf_hp_support_from_cat_find_pairing_code_modal(self):
        self.driver.wait_for_object("cant_find_pairing_code_modal_hp_support_lf")
    
    def verify_invalid_pairing_code_error_msg(self):
        """
        Verify "Invalid Code. Please Try Again" message after inputing invalid code on Enter your printers's pairing code page
        """
        self.driver.wait_for_object("invalid_pairing_code")

    def validate_retry_warning_string(self, warning_msg):
        """
        Verify Retry Warning message after 3 unsuccessful attempts to enter pairing code
        """
        web_str = self.driver.get_attribute("retry_warning_text", "text")
        return self.checking_web_str_against_spec_string(warning_msg, web_str, "retry_warning_text", raise_e=False)
    
    def validate_retry_limit_string(self, limit_msg):
        """
        Verify Retry Limit message after 5 unsuccessful attempts to enter pairing code
        """
        web_str = self.driver.get_attribute("retry_limit_text", "text")
        return self.checking_web_str_against_spec_string(limit_msg, web_str, "retry_limit_text", raise_e=False)