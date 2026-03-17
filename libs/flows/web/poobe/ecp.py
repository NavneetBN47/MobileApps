from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare, string_validation

class ECP(OWSFlow):
    """
        Contains all of the elements associated with ECP:
        url: https://onboardingcenter.pie.portalshell.int.hp.com/pn
        Beam, Enterprise, Jupiter
    """
    file_path = __file__
    flow_name = "ecp"

    def __init__(self, driver, endpoint):
        super(ECP, self).__init__(driver)
        self.stack = driver.session_data["stack"]
        self.endpoint = endpoint
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        self.url = "https://onboardingcenter.{}.portalshell.int.hp.com/{}/{}".format(self.stack, self.locale, self.endpoint)


########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################

    def click_not_right_now_button(self, change_check=False):
        return self.driver.click("not_right_now_button", change_check=change_check)
    
    def click_connect_button(self):
        self.driver.click("connect_button")

    def click_hp_command_center_terms_of_use(self):
        self.driver.click("hp_command_center_terms_of_use")

    def click_connect_to_partner_button(self):
        self.driver.click("buttons_partner_link_label")

    def click_hp_command_center_button(self):
        self.driver.click("buttons_hp_command_center_label")

    def click_get_drivers_button(self):
        """
        Clicks the Get Drivers button on the ECP Finish Setup page This will open a new tab go to new tab verify and close it
        """
        self.driver.click("buttons_get_drivers_label")
            
    def click_command_center_btn_partner_link_page(self):
        self.driver.click("command_center_btn_partner_link_page")
        
    def enter_username_hp_command_center_login(self, username):
        self.driver.send_keys("username_field", username)

    def click_hp_command_center_login_continue_btn(self):
        self.driver.click("command_center_login_page_continue_btn")

########################################################################################################################
#                                                                                                                      #
#                                                  Verification Flows                                                  #
#                                                                                                                      #
########################################################################################################################

    def verify_partner_link_page(self, timeout=5, raise_e=True):
        return self.driver.wait_for_object("partner_link_page", timeout=timeout, raise_e=raise_e)

    def verify_not_right_now_button(self):
        self.driver.wait_for_object("not_right_now_button")

    def verify_connect_button(self, clickable=False, raise_e=True):
        return self.driver.wait_for_object("connect_button", clickable=clickable, raise_e=raise_e)
    
    def verify_ecp_finish_setup_page(self, timeout=5, raise_e=True):
        return self.driver.wait_for_object("finish_setup_page", timeout=timeout, raise_e=raise_e)

    @string_validation("buttons_get_drivers_label")
    @string_validation("action_list_get_drivers_description")
    @string_validation("action_list_get_drivers__title")
    def verify_get_software_and_drivers(self):
        self.driver.wait_for_object("get_software_and_drivers")

    @screenshot_compare(root_obj="finish_setup_page")
    @screenshot_compare(root_obj="whole_page_finish_setup_page")
    def verify_finish_setup_ecp_header(self):
        self.driver.wait_for_object("header")

    @string_validation("header")
    @string_validation("subheader")
    def verify_finish_setup_ecp_subheader(self):
        self.driver.wait_for_object("subheader")

    @string_validation("buttons_partner_link_label")
    @string_validation("action_list_partner_link__title")
    @string_validation("action_list_partner_link_description")
    def verify_connect_to_hp_partner_link_pay_per_use(self):
        self.driver.wait_for_object("connect_to_hp_partner_link_pay_per_use")   
    
    @string_validation("buttons_hp_command_center_label")
    @string_validation("action_list_hp_command_center_description")
    @string_validation("action_list_hp_command_center_description")
    def verify_hp_command_center_finish_setup_page(self):
        self.driver.wait_for_object("hp_command_center")
    
    def verify_hp_command_center_page(self):
        self.driver.wait_for_object("command_center_page")

    def verify_command_center_terms_of_use(self):
        self.driver.wait_for_object("hp_command_center_terms_of_use")

    def verify_command_center_login_page(self):
        self.driver.wait_for_object("command_center_login_page")
        self.driver.wait_for_object("command_center_login_terms")