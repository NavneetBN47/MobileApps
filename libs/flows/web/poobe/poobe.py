import logging
from socket import timeout
from time import sleep
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare
from selenium.webdriver.common.keys import Keys

class PortalOOBE(OWSFlow):
    """
        Contains all of the elements and flows associated poobe screen
        /activate, /connect, /onboard
        "E2E_production": "https://hpsmart.com/activate",
        "Flex_production": "https://hpsmart.com/connect"
    """
    file_path = __file__
    flow_name = "portal_OOBE_screen"
    def __init__(self, driver, endpoint, window_name="main"):
        super(PortalOOBE, self).__init__(driver, window_name=window_name)
        self.endpoint = endpoint
        self.stack = driver.session_data["stack"]
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        self.poobe_url = "https://smb.{}.portalshell.int.hp.com/{}/{}".format(self.stack, self.locale, self.endpoint)
    
########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################
    def click_go_btn(self):
        """
        Click Go btn on Access Beta Screen
        """
        self.driver.click("go_btn")
    
    def click_setup_printer_for_personal_overlay_install_hp_smart_btn(self):
        self.driver.click("setup_printer_for_personal_overlay_install_hp_smart_btn")
    
    def click_continue_btn(self, raise_e=True):
        """
        Click Continue button
        """
        self.driver.click("continue_btn", raise_e=raise_e)
    

    def click_sign_in_btn(self):
        """
        click create or sign in btn on how do you want setup your printer screen
        """
        self.driver.click("sign_in_btn")
    
    def click_skip_btn(self, timeout=10):
        """
        Click Skip button on enter printer name and printer location.
        """
        self.driver.click("skip_btn", displayed=False, timeout=timeout)
    
    def skip_install_drivers_page(self, platform):
        """
        Click Skip button on install drivers page based on the browser OS(platform)
        """
        self.driver.click("install_drivers_page_skip_btn" if platform == "windows" else "install_dirvers_page_skip_btn_nonwindows")
    
    def click_checkbox(self):
        """
        Click Hp terms and condition checkbox
        """
        self.driver.click("checkbox", displayed=False)

    def click_learn_more(self, stack=None):
        """
        Click Learn more on landing page.
        """
        if stack == "production":
            return self.driver.click("learn_more")
        else:
            return self.driver.click("learn_more", change_check={'wait_obj':"benefits_container"}, retry=5)

    def click_try_again_btn(self):
        """
        Click try again button on activation error overlay
        """
        self.driver.click("try_again_btn")


    def click_confirm_hp_plus_activation_button(self):
        """
        click Confirm button on HP+ Smart Printer Requirments Terms and condiations Page
        """
        self.driver.click("confirm_hp_plus_activation")


    def click_activating_printer_page(self):
        """
        Click Printer Activation in progress title on Printer Activation Page. strange element to click its for resume session modal  feature.
        """
        self.driver.click("printer_activation_page")
    
    def click_close_fw_overlay(self):
        """
        click Close (x) on top right corner of overlay.
        """
        self.driver.click("close_popup_x")
    
    def click_open_hp_smart_admin_btn(self):
        """
        click Open Hp smart admin button on go-to-dashboard page
        """
        self.driver.click("open_hp_smart_admin")
    
    
    def click_set_up_print_send_test_page_btn(self):
        """
        click set up print and send a test page button on finish printer setup page
        """
        self.driver.click("set_up_print_send_test_page_btn")

    def click_invite_users_and_admin_btn(self):
        """
        click invite users and admin button on finish printer setup page
        """
        self.driver.click("invite_users_and_admin_btn")

    def click_done_btn(self):
        """
        click done button on Set up Print and test page Overlay screen can be seen after clicking on corrosponding Set up button
        """
        self.driver.click("done_btn")

    def click_already_have_driver_btn(self):
        """
        click already have a driver button on Set up Print and send test page Overlay screen seen after clicking on corresponding set up button
        """
        self.driver.click("already_have_driver_button")

    def click_set_up_scan_destinations_btn(self):
        """
        click Set up button on finish printer setup page
        """
        self.driver.click("set_up_scan_destinations_btn")


    def click_go_to_hp_smart_dashboard_btn(self):
        """"
        Click Go to Hp smart button on printer setup page.
        """
        self.driver.click("go_to_hp_smart_btn")

    def get_printer_type_and_number_from_left_panel(self):
        """
        Get printer type and number from left panel
        """
        return self.driver.get_attribute("printer_type_number_left_panel", "text")
    
    def click_scan_to_email_modal_done_btn(self):
        """
        Click Done on the Scan to Email Enabled Modal Done button that shows up only after successfull flowers printer activation
        """
        self.driver.click("scan_to_email_modal_done_btn")

    def click_scan_setup_complete_modal_close_btn(self):
        """
        Click Close button on the Scan to Email Enabled Modal that shows up only after successfull flowers printer activation
        """
        self.driver.click("scan_setup_complete_modal_close_btn")


########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_smb_dashboard(self):
        """
        Verify smb dashboard after selecting persoanl printer type
        """
        self.driver.wait_for_object("smb_dashboard")

    def verify_left_panel_printer_container(self, biz="_", printer_profile="_"):
        """
        Verify Printer Image and color container on left panel.
        """
        page_name = (self.driver.current_url.split("/"))[-1]
        self.driver.wait_for_object("left_panel_printer_container")
        self.driver.process_screenshot(self.file_path, ("{}_{}_{}_left_panel_printer_container").format(biz, printer_profile, page_name), root_obj="left_panel_printer_container")


    def verify_veneer_stepper_panel(self):
        """
        Verify Printer stepper panel on left side of the page.
        """
        page_name = (self.driver.current_url.split("/"))[-1]
        self.driver.wait_for_object("printer_stepper")
        self.driver.process_screenshot(self.file_path, ("{}_veneer_printer_stepper").format(page_name), root_obj="printer_stepper")

    @screenshot_compare(root_obj="hp_t&C_eula_page")
    def verify_hp_tC_eula_page(self):
        """
        Verify Getting most out of your account page after selecting Personal printer on How do you want to setup this printer ?
        """
        self.driver.wait_for_object("hp_t&C_eula_page")

    def verify_support_drivers_page(self):
        self.driver.wait_for_object("support_page", timeout=15)

    
    ####################### Account Type Page #########################
    
    @screenshot_compare(root_obj="select_account_type_page")
    def verify_select_account_type_page(self):
        """
        Verify How do you want to setup ypur printer page
        """
        self.driver.wait_for_object("select_account_type_page", timeout=30)    
    
    @screenshot_compare(root_obj="hp_logo")
    def verify_hp_logo(self):
        """
        Verify hp logo on landing page
        """
        self.driver.wait_for_object("hp_logo")

    ####################### Printer Activation page #########################

    @screenshot_compare(root_obj="printer_activation_page")
    def verify_activating_printer_page(self):
        """
        Verify hp+ Printer Activation in progress title on Printer Activation Page.
        """
        self.driver.wait_for_object("printer_activation_page")

    @screenshot_compare(root_obj="activated_checkmark")
    def verify_activated_printer_page(self):
        """
        Verify the printer activated page 
        """
        self.driver.wait_for_object("activated_checkmark", timeout=305)

    @screenshot_compare(root_obj="sucess_check_circle")
    def verify_printer_activation(self):
        """
        Verify the printer image on activated page
        """
        self.driver.wait_for_object("sucess_check_circle")

    def verify_setup_printer_btn(self):
        """
        Verify Setup Printer button on Finish setup page
        """
        self.driver.wait_for_object("set_up_printer")

    def verify_exit_setup_btn(self):
        """
        Verify Setup Printer button on Finish setup page
        """
        self.driver.wait_for_object("exit_setup")
    
    @screenshot_compare(root_obj="printer_setup_img")
    def verify_printer_setup_img(self):
        """
        Verify Printer Setup image on Finish Setup Page
        """
        self.driver.wait_for_object("printer_setup_img")
    
    @screenshot_compare(file_name="printer_stepper_pairing_code_page", root_obj="printer_stepper")
    def verify_printer_stepper(self):
        """
        Verify flow stepper for printer onboarding
        """
        self.driver.wait_for_object("printer_stepper")

    def verify_download_hp_easy_link(self):
        """
        Verfy 123.hp.com link
        """
        self.driver.wait_for_object("123_url", displayed = False)

    def verify_hp_smart_terms_conditions_url(self):
        """
        Verify Hp Smart Terms and Conditions hyperurl is present on the page.
        """
        self.driver.wait_for_object("hp_smart_terms_conditions_url")
    
    def verify_continue_btn(self, clickable=False, raise_e=True):
        """
        Verify continue button on page. pass clickable=True and raise_e=False to verify btn disabled
        """
        return self.driver.wait_for_object("continue_btn", clickable=clickable, raise_e=raise_e)
    
    ####################### Software Completion #########################

    def verify_toner_is_on_the_way_page(self):
        """
        Verify Your toner is on its way! page
        """
        self.driver.wait_for_object("checkmark_circle", timeout=15)
        self.driver.wait_for_object("hp_admin_link")

    ####################### Finish Printer Setup Page #########################
    
    def install_printer_drivers_page_content(self, platform, timeout=15, raise_e=True):
        """
        Verify Install printer drivers page content
        """
        return self.driver.wait_for_object("install_drivers_page_content" if platform == "windows" else "install_drivers_page_content_nonwindows", timeout=timeout, raise_e=raise_e)
    
    
    def verify_install_printer_driver_page(self, platform, timeout=15, raise_e=True):
        """
        Verify Install Printer Driver page.
        """
        return self.driver.wait_for_object("install_drivers_page" if platform == "windows" else "install_drivers_page_nonwindows", timeout=timeout, raise_e=raise_e)

    @screenshot_compare(root_obj="continue_to_hp_smart_admin_page")
    def verify_hp_smart_admin_page(self):
        """
        Verify Hp smart admin page on url: /finish-setup page after Install driver page.
        """
        self.driver.wait_for_object("continue_to_hp_smart_admin_page")

    @screenshot_compare(root_obj="scan_and_fax_tile_finish_printer_setup")
    def verify_hp_smart_scan_fax_tiles(self):
        """
        Verify Scan and fax tile on finsih printer setup page.
        """
        self.driver.wait_for_object("scan_and_fax_tile_finish_printer_setup")

    @screenshot_compare(root_obj="users_management_finish_printer_setup")
    def verify_hp_smart_users_management_finish_printer_setup(self):
        """
        Verify users tile on finsih printer setup page.
        """
        self.driver.wait_for_object("users_management_finish_printer_setup")

    @screenshot_compare(root_obj="fleet_control_finish_printer_setup")
    def verify_fleet_control_finish_printer_setup(self):
        """
        Verify Fleet management tile on finish printer setup page.
        """
        self.driver.wait_for_object("fleet_control_finish_printer_setup")

    @screenshot_compare(root_obj="subscriptions_tile_finish_printer_setup")
    def verify_subscriptions_tile(self):
        """
        Verify Subscriptions tile on finish printer setup page.
        """
        self.driver.wait_for_object("subscriptions_tile_finish_printer_setup")
    
    @screenshot_compare(root_obj="print_solutions_tile_finish_printer_setup")
    def verify_print_solutions_tile_finish_printer_setup(self):
        """
        Verify Print Solutions tile on finish printer setup page.
        """
        self.driver.wait_for_object("print_solutions_tile_finish_printer_setup")

    def verify_continue_to_hp_smart_admin_page(self, timeout=10):
        """
        Verify Continue to HP smart Admin page showing main features of HP smart such as Scan and Fax, users, subscriptions etc.
        """
        self.driver.wait_for_object("continue_to_hp_smart_admin_page", timeout=timeout)
    
    def verify_finish_printer_setup_page(self, timeout=10, raise_e=True):
        """
        Verify finish printer setup page after II instant Ink offer
        """
        self.verify_web_page(sub_url="go-to-dashboard")
        return self.driver.wait_for_object("go_to_hp_smart_btn", timeout=timeout, raise_e=raise_e)
    
    def verify_set_up_print_send_test_page(self):
        """
        Verify Set up print and send Test section on finish printer setup page
        """
        self.driver.wait_for_object("set_up_print_send_test_page_section")
        self.driver.wait_for_object("set_up_print_send_test_page_btn")

    def verify_set_up_print_overlay_page(self):
        """
        Verify set up print Overlay should be seen after clicking Set up print test button
        """
        self.driver.wait_for_object("set_up_print_page")

    def verify_install_print_driver_btn(self):
        """
        Verify Install Print Driver button on Set up Print and send test page Overlay screen seen after clicking on corresponding set up button
        """
        self.driver.wait_for_object("install_print_driver_btn")

    def verify_already_have_driver_btn(self):
        """
        Verify already have a driver button on Set up Print and send test page Overlay screen seen after clicking on corresponding set up button
        """
        self.driver.wait_for_object("already_have_driver_button")
    
    def verify_first_print_button(self):
        """
        Verify First print button on set up print and send a test page overlay screen cn seen after clicking on Corrosponding Set up button
        """
        self.driver.wait_for_object("print_btn")

    def verify_done_btn(self):
        """
        Verify done button on Set up Print and test page Overlay screen can be seen after clicking on corrosponding Set up button
        """
        self.driver.wait_for_object("done_btn")

    def verify_set_up_and_scan_destination(self):
        """"
        Verify setup and scan destination Section and button
        """
        self.driver.wait_for_object("set_up_scan_destinations_section")
        self.driver.wait_for_object("set_up_scan_destinations_btn")
    
    def verify_set_up_scan_overlay_screen(self):
        """
        Verify set up Scan Overlay should be seen after clicking Set up Scan to Destination button
        """
        self.driver.wait_for_object("scan_overlay_screen", timeout=15)

    def verify_scan_to_email_section(self):
        """
        Verify Scan to email section and setup button on Set up Scan overlay screen
        """
        self.driver.wait_for_object("scan_to_email_section", timeout=15)
        self.driver.wait_for_object("scan_to_email_btn", timeout=15)
        
    def verify_scan_to_cloud_section(self):
        """
        Verify Scan to cloud section and Setup button on Set up scan overlay screen
        """    
        self.driver.wait_for_object("scan_to_cloud_section")
        self.driver.wait_for_object("scan_to_cloud_btn")
    
    def verify_set_up_fax(self):
        """
        Verify Set up fax section
        """
        self.driver.wait_for_object("set_up_fax_section")
        self.driver.wait_for_object("set_up_fax_btn")
    
    def verify_invite_users_and_admin_section(self):
        """
        Verify Invite users and admin section on Finish Printer setup page
        """
        self.driver.wait_for_object("invite_users_and_admin_section")

    def verify_invite_users_and_admin_btn(self):
        """
        Verify invite users and admin button on finish printer setup page
        """
        self.driver.wait_for_object("invite_users_and_admin_btn")

    @screenshot_compare(root_obj="scan_to_email_enabled_modal")
    def verify_scan_to_email_enable_modal(self, raise_e=True, timeout=10):
        """
        Verify Scan to Email enable modal
        """
        return self.driver.wait_for_object("scan_to_email_enabled_modal", raise_e=raise_e)
    
    def verify_scan_to_email_body(self):
        self.driver.wait_for_object("scan_to_email_modal_body")