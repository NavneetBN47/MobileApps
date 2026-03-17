from time import sleep

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class HPConnect(HPConnectFlow):
    flow_name="hp_connect_home"
    root_url = {"pie": "https://www.hpsmartpie.com/us/en",
                "stage": "https://www.hpsmartstage.com/us/en",
                "production": "https://www.hpsmart.com/us/en"}
    

    HELP_SUPPORT_LINK = "help_support_link"
    WIRELESS_PRINT_CENTER_LINK = "wireless_print_center_link"
    ENDER_USER_LICENSE_AGREEMENT_LINK = "end_user_license_agreement_link"
    HP_PRIVACY_LINK = "hp_privacy_link"
    HP_SMART_TERMS_OF_USE_LINK = "hp_smart_terms_of_use_link"
    
    def __init__(self, driver, context=None):
        super(HPConnect, self).__init__(driver, context=context)
        self.hp_id_web = HPID(driver, context=context)

    def navigate(self, stack):
        self.driver.navigate(self.root_url[stack])

    ###############################################################################
    #                             Home page flows                                 #
    ###############################################################################

    def accept_privacy_popup(self, delay=None):
        self.driver.click("privacy_popup_accept_btn", timeout=10, delay=delay, raise_e=False)

    def sign_in_from_home_page(self, username, password):
        self.verify_sign_in_btn()
        self.click_sign_in_btn()
        self.hp_id_web.login(username, password)
        self.driver.current_project = self.project
        self.driver.current_flow = self.flow_name
        self.driver.wait_for_object("my_printer_link")
        return True

    def verify_sign_up_btn(self):
        self.driver.wait_for_object("sign_up_btn")

    def click_sign_up_btn(self):
        self.driver.click("sign_up_btn")

    def verify_sign_in_btn(self):
        self.driver.wait_for_object("sign_in_link")

    def click_sign_in_btn(self):
        self.driver.click("sign_in_link")

    def verify_signed_in(self):
        return self.driver.wait_for_object("menu_avatar_btn", timeout=3, raise_e=False) is not False

    def sign_out(self):
        self.driver.click("menu_avatar_btn")
        self.driver.click("sign_out_btn")
        self.driver.performance.start_timer("hpid_logout")
        sleep(1)
        return True
        
    def is_submenu_expanded(self, submenu_title, account_type):
        """
        Verify if the specified Submenu is expanded
        :return: The element if its found, else it returns False
        """
        if account_type == "hp+":
            submenu_list = ["hp_instant_ink", "solutions", "account", "sustainability", "help_center"]
        elif account_type == "ucde":
            submenu_list = ["hp_oneprint", "account", "help_center"]
        else:
            raise ValueError(f"{account_type} is not a accont type: use hp+ or ucde")
        submenu_title = submenu_title.lower()
        if submenu_title not in submenu_list:
            raise ValueError(f"{submenu_title} is not a valid item")
        return self.driver.wait_for_object(f"is_{submenu_title}_submenu_expanded", timeout=2, raise_e=False)
    
    ###############################################################################
    #                             UCDE account flows                              #
    ###############################################################################

    def verify_UCDE_banner(self, timeout=30):
        self.driver.wait_for_object("ucde_banner", timeout=timeout)

    def click_menu_toggle(self, change_check={"wait_obj": "close_hamburger_menu_btn", "invisible": False}):
        #This button is for mobile only
        self.driver.click("menu_toggle_btn", change_check=change_check)

    def verify_account_profile_screen(self, timeout=10):
        """
        Verify Account Profile screen  via:
        - Account Profile title
        """
        self.driver.wait_for_object("account_profile_title", timeout=timeout)

    def verify_menu_toggle(self, invisible=False):
        self.driver.wait_for_object("menu_toggle_btn", invisible=invisible)

    def verify_terms_of_use_page(self, timeout=10):
        self.driver.wait_for_object("terms_of_use_and_end_user_agreement_page", timeout=timeout)

    def click_terms_of_use_and_end_user_agreement_continue_btn(self):
        self.driver.click("terms_of_use_and_end_user_agreement_continue_btn")

    ###############################################################################
    #                            HP+ account flows                                #
    ###############################################################################
    
    def verify_account_summary(self, timeout=10):
        """
        Verify HP Plus account status on Account Summary screen via:
        - Account & HP+Memeber
        """
        self.driver.wait_for_object("account_summary_title", timeout=timeout)
        self.driver.wait_for_object("account_status_content")
        
    def click_close_btn(self):
        """
        Click on Close button on Account Summary screen
        """
        self.driver.click("close_btn")
    
    def click_account_btn(self):
        """
        Click on Account on HP Smart menu screen
        """
        self.driver.click("account_btn")
        
    def click_help_center_btn(self):
        """
        Click on Help Center on HP Smart menu screen
        :return:
        """
        self.driver.click("help_center_btn")

    def click_users_btn(self):
        """
        Click on Users button on HP Smart menu screen
        :return:
        """
        if not self.is_submenu_expanded("account", "hp+"):
            self.click_account_btn()
        self.driver.click("users_btn", delay=2)
    
    def click_link(self, link):
        """
        Click on a link
        :param link: use class constants:
                HELP_SUPPORT_LINK 
                ENDER_USER_LICENSE_AGREEMENT_LINK 
                HP_PRIVACY_LINK
                HP_SMART_TERMS_OF_USE_LINK  
        """
        self.driver.selenium.js_click(link)

    def verify_standard_account_dashboard(self, timeout=10):
        """
        Verify Dashboard for standard account (Flex)
        """
        self.driver.wait_for_object("printers_card", timeout=timeout)
        self.driver.wait_for_object("account_dashboard_menu_nav", timeout=timeout)
        assert self.driver.wait_for_object("sustainability_menu", raise_e=False) is False

    def verify_smart_dashboard_menu_screen(self, timeout=15, invisible=False):
        """
        Verify Smart Dashboard menu screen via:
        - Account Dashboard (This item only shows for HP+ account)
        - HP+ Print Plans
        - Printers
        - Features
        - Account
        - Help Center
        """
        if not self.driver.wait_for_object("hp_instant_ink_btn", timeout=timeout, raise_e=False):
            self.driver.click("toggle_menu_btn")
        self.driver.wait_for_object("account_dashboard_btn", timeout=timeout, invisible=invisible)
        # self.driver.wait_for_object("hp_instant_ink_btn")
        self.driver.wait_for_object("printers_btn")
        #self.driver.wait_for_object("features_btn")
        self.driver.wait_for_object("account_btn")
        self.driver.wait_for_object("help_center_btn")

    def verify_hp_plus_consumer_account_dashboard(self, timeout=10):
        """
        Verify Dashboard for HP+ account
        """
        self.driver.wait_for_object("printers_card", timeout=timeout)
        self.driver.wait_for_object("account_dashboard_menu_nav", timeout=timeout)
        self.driver.wait_for_object("hp_instant_ink_btn")
        self.driver.wait_for_object("warrenty_card", timeout=timeout)
        self.driver.wait_for_object("sustaninability_card", timeout=timeout)
        self.driver.wait_for_object("sustainability_menu", timeout=timeout)
        self.driver.wait_for_object("hp_instant_ink_card", timeout=timeout)

    ###############################################################################
    #                             Virtual Agent                                   #
    ###############################################################################
    
    def verify_virtual_chat_popup(self, timeout=10):
        """
        Verify virtual chat pop up message is shown with 'Cancel' and 'Start Chat' buttons 
        """
        self.driver.wait_for_object("va_icon", timeout=timeout)
        self.driver.wait_for_object("va_cancel_btn")
        self.driver.wait_for_object("va_start_chat_btn")
    
    def select_start_chat(self):
        self.driver.click("va_start_chat_btn")
    
    def select_virtual_agent_cancel(self):
        self.driver.click("va_cancel_btn")
    
    def select_chat_with_virtual_agent(self):
        self.driver.click("chat_with_virtual_agent")

    #################################################################################
        #                             Delete Account                               #
    #################################################################################

    def select_no_keep_account_btn(self):
        """
        Click on No, keep account button on Delete HP Smart account screen
        """
        self.driver.click("no_keep_account_btn")

    def select_delete_account_btn(self):
        """
        Click on Delete Account button on Delete HP Smart account screen
        """
        self.driver.click("delete_account_btn")

    def select_done_btn(self):
        """
        Click on Done button on HP Smart account has been deleted screen
        """
        self.driver.selenium.js_click("done_btn", displayed=False)

    def select_open_dashboard_btn(self):
        """
        Click on Open Dashboard button on You must cancel service screen
        """
        self.driver.selenium.js_click("open_dashboard_btn", displayed=False)

    def verify_delete_hp_smart_account_screen(self, timeout=30):
        """
        Verify Delete HP Smart account screen
        """
        self.driver.wait_for_object("here_link", timeout=timeout)
        self.driver.wait_for_object("no_keep_account_btn", displayed=False)

    def verify_hp_smart_account_has_been_deleted_screen(self, timeout=20):
        """
        Verify Current screen is HP Smart account has been deleted screen
        :param timeout:
        """
        self.driver.wait_for_object("hp_smart_account_has_been_deleted_title", timeout=timeout)
        self.driver.wait_for_object("hp_smart_account_has_been_deleted_checkmark")

    def verify_you_must_be_cancel_service_screen(self, timeout=20):
        """
        Verify You must cancel service screen
        """
        self.driver.wait_for_object("you_must_cancel_service_title", timeout=timeout, displayed=False)
        self.driver.wait_for_object("open_dashboard_btn", displayed=False)

class IOSHPConnect(HPConnect):

    context = "NATIVE_APP"

    def click_link_native(self, link, timeout=15, scroll=False):
        """
        Click on a link
        :param link: use class constants:
                HELP_SUPPORT_LINK 
                ENDER_USER_LICENSE_AGREEMENT_LINK 
                HP_PRIVACY_LINK
                HP_SMART_TERMS_OF_USE_LINK 
                HERE_LINK
        """
        if scroll:
            self.driver.scroll(link, timeout=timeout)
        self.driver.click(link, timeout=timeout)

    ###############################################################################
    #                             Delete Account                                  #
    ###############################################################################

    def select_no_keep_account_btn(self, timeout=10):
        self.driver.scroll("no_keep_account_btn", click_obj=True, check_end=False, timeout=timeout)

    def select_delete_account_btn(self, delay=0):
        if not self.driver.wait_for_object("delete_account_btn", raise_e=False):
            self.driver.scroll("delete_account_btn")
        self.driver.click("delete_account_btn", delay=delay)

    def verify_hp_smart_account_has_been_deleted_title(self, timeout=30):
        self.driver.wait_for_object("hp_smart_account_has_been_deleted_title", timeout=timeout)

    def select_done_btn(self, delay=0):
        if self.driver.wait_for_object("session_expired_cancel_btn", timeout=3, raise_e=False):
            self.driver.click("session_expired_cancel_btn")
        self.driver.click("done_btn", delay=delay)

    def verify_delete_hp_smart_account_screen(self, timeout=50):
        self.driver.wait_for_object("delete_hp_smart_account_title", timeout=timeout)
        self.driver.wait_for_object("here_link")
        self.driver.wait_for_object("no_keep_account_btn", displayed=False)


class MacHPConnect(IOSHPConnect):

    def click_link_native(self, link, timeout=15, scroll=False):
        """
        Click on a link
        :param link: use class constants:
                HELP_SUPPORT_LINK 
                ENDER_USER_LICENSE_AGREEMENT_LINK 
                HP_PRIVACY_LINK
                HP_SMART_TERMS_OF_USE_LINK 
                HERE_LINK
        """
        if scroll:
            self.driver.scroll(link, timeout=timeout)
        self.driver.click_using_frame(link, timeout=timeout)
    
    ###############################################################################
    #                             Delete Account                                  #
    ###############################################################################

    def select_no_keep_account_btn(self, timeout=10):
        self.driver.swipe()
        self.driver.click_using_frame("no_keep_account_btn", timeout=timeout)

    def select_delete_account_btn(self):
        self.driver.swipe()                     
        self.driver.click_using_frame("delete_account_btn")

    def select_done_btn(self):
        self.driver.click_using_frame("done_btn")

class WinSmartDashboard(HPConnect):     

    context = "NATIVE_APP"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def get_smart_dashboard_title(self, timeout=30):
        return self.driver.get_attribute("dashboard_title", "Name")

    # ---------------- Delete Account Data Screen ---------------- #
    def select_delete_account_btn(self):
        self.driver.click("delete_account_btn")

    def select_no_keep_account_btn(self):
        self.driver.click("no_keep_account_btn")

    def select_done_btn(self):
        self.driver.click("done_btn")

    def select_solutions_btn(self):

        self.driver.click("solutions_btn")

    def select_hp_smart_advance_btn(self):
        self.driver.click("hp_smart_advance_btn")
    # ---------------- Delete Account Data Screen ---------------- #

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_my_account_page(self):
        self.accept_privacy_popup()
        # self.verify_smart_dashboard_menu_screen()
        assert self.get_smart_dashboard_title() == "My Account"

    def verify_delete_account_data_screen(self):
        self.verify_smart_dashboard_menu_screen()
        assert self.get_smart_dashboard_title() == "Delete Account Data"

    def verify_delete_hp_smart_account_screen(self, timeout=30):
        self.accept_privacy_popup()
        self.driver.wait_for_object("delete_hp_smart_account_title", timeout=timeout)
        self.driver.wait_for_object("here_link")
        self.driver.wait_for_object("delete_account_btn")
        self.driver.wait_for_object("no_keep_account_btn")

    def verify_hp_smart_advance_btn_not_display(self):
        assert self.driver.wait_for_object("hp_smart_advance_btn", raise_e=False) is False

    def verify_hp_smart_account_has_been_deleted_screen(self, timeout=30):
        self.driver.wait_for_object("hp_smart_account_has_been_deleted_title", timeout=timeout)
        self.driver.wait_for_object("done_btn")

    def verify_smart_security_btn_display(self):
        self.driver.wait_for_object("smart_security_btn")
        