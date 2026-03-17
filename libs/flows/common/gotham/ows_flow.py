import logging
from MobileApps.libs.flows.common.gotham.flow_container import FlowContainer
import MobileApps.resources.const.windows.const as w_const

class OwsFlow(object):   
    def __init__(self, driver, web_driver):
        '''
        This is initial method for class.
        '''
        self.driver = driver
        self.web_driver = web_driver
        self.fc = FlowContainer(driver, web_driver)

    def __palermo_gen2_inkjet_flow(self):
        '''
        This is a flow for Palermo in OWS.
        '''
        logging.debug("Go through OWS workflow for Palermo family printer... ")

        self.__go_through_enjoy_hp_acct()
        self.__skip_instant_ink_flow()
        self.__help_make_better_product_flow()
        self.__go_through_other_screen_to_main_ui()
 
    def __yeti_flow(self, yeti_type):
        '''
        This is a flow for vasari/novelli/malbec/manhattan in OWS.
        '''
        logging.debug("Go through OWS workflow for yeti printer... ")

        self.__go_through_activate_hp_plus_yeti_printer(yeti_type)
        self.__skip_instant_ink_flow()
        self.__go_through_live_ui()
        self.__go_through_other_screen_to_main_ui()

     # *********************************************************************************
     #                                ACTION FLOWS                                     *
     # *********************************************************************************
    def create_account_flow(self):
        '''
        This is a flow to create an account during ows
        '''
        self.fc.fd["moobe"].verify_create_or_sign_in_screen()
        self.fc.fd["moobe"].click_create_account_btn()
        self.fc.handle_web_login(create_account=True)

    def sign_in_flow(self, username, password):
        '''
        This is a flow to sign in during ows
        '''
        self.fc.fd["moobe"].verify_create_or_sign_in_screen()
        self.fc.fd["moobe"].click_sign_in_btn()
        self.fc.handle_web_login(username=username, password=password)

    def skip_account_activation_flow(self):
        '''
        This is a flow to skip create an account during ows
        '''
        self.fc.fd["moobe"].verify_create_or_sign_in_screen()
        self.fc.fd["moobe"].click_skip_account_activation_btn()
        self.fc.fd["moobe"].verify_do_not_miss_out_on_screen()
        self.fc.fd["moobe"].click_skip_account_activation_btn()

    def __go_through_enjoy_hp_acct(self, create_account=True, skip_accept_all=False):
        '''
        This is a flow from enjoy hp account then to hp id sign up dialog.
        '''
        if not skip_accept_all:
            self.fc.fd["moobe"].verify_connected_printing_services_screen()
            self.fc.fd["moobe"].click_accept_all()
        if self.fc.fd["moobe"].verify_create_or_sign_in_screen(raise_e=False):
            if create_account:
                self.create_account_flow()

    def __skip_instant_ink_flow(self):
        '''
        This is a flow from instant ink advertisement screen to reminder screen.
        '''
        self.fc.fd["moobe"].verify_hp_instant_ink_plan_load()
        self.fc.fd["moobe"].click_do_not_enable_ink_delivery_btn()
        self.fc.fd["moobe"].verify_want_to_skip_dialog()
        self.fc.fd["moobe"].click_skip_offer_btn()
            
    def __help_make_better_product_flow(self):
        '''
        This is a method to set up information on the help HP make better product screen
        '''
        self.fc.fd["moobe"].wait_for_help_hp_make_better_load()
        self.fc.fd["moobe"].set_postal_code(w_const.PRINTER_INFO.POSTAL_CODE)
        self.fc.fd["moobe"].click_continue_btn_help_better()

    def __go_through_live_ui(self):
        '''
        This is a flow from Live UI.
        '''
        if self.fc.fd["moobe"].verify_time_install_ink_screen(raise_e=False):
            self.fc.fd["moobe"].click_skip_installing_ink_btn()
            self.fc.fd["moobe"].verify_let_load_paper_screen()
            self.fc.fd["moobe"].click_skip_loading_paper_btn()
        else:
            self.fc.fd["moobe"].verify_let_load_paper_screen()
            self.fc.fd["moobe"].click_skip_loading_paper_btn()
            self.fc.fd["moobe"].verify_time_install_ink_screen()
            self.fc.fd["moobe"].click_skip_installing_ink_btn()
        self.fc.fd["moobe"].verify_printer_up_dates_screen()
        self.fc.fd["moobe"].select_notify_opt()
        self.fc.fd["moobe"].click_apply_btn()

    def __go_through_other_screen_to_main_ui(self):
        '''
        This is a method to Main UI scree
        '''
        self.fc.fd["moobe"].verify_print_from_other_devices()
        self.fc.fd["moobe"].select_skip_this_step()
        self.fc.fd["moobe"].verify_setup_complete_lets_print()
        self.fc.fd["moobe"].select_skip_printing_page()
        self.fc.fd["home"].verify_home_screen()

    def __go_through_activate_hp_plus_yeti_printer(self, yeti_type, create_account=True, skip_accept_all=False):
        '''
        This is a flow from Activate HP+ for smart printing capabilities screen.
        '''
        if not skip_accept_all:
            self.fc.fd["moobe"].verify_connected_printing_services_screen()
            self.fc.fd["moobe"].click_accept_all()
        if self.fc.fd["moobe"].verify_select_your_country_or_region(raise_e=False):
            self.fc.fd["moobe"].select_us_country_or_region()
        if self.fc.fd["moobe"].verify_activate_hp_puls_for_screen(raise_e=False):
            if yeti_type=="e2e":
                self.fc.fd["moobe"].select_continue()
                #todo
            elif yeti_type=="flex":
                self.fc.fd["moobe"].click_do_not_activate_hp_btn()
                self.fc.fd["moobe"].verify_decline_your_exclusive_screen()
                self.fc.fd["moobe"].click_decline_hp_plus_btn()
                self.fc.fd["moobe"].verify_printer_dynamic_security_notice_screen()
                self.fc.fd["moobe"].select_continue()
        if self.fc.fd["moobe"].verify_create_or_sign_in_screen(raise_e=False):
            if create_account:
                self.create_account_flow()

    def connected_printing_services_flow(self, printer_obj):
        '''
        Click buttons on printer dialog may pop up before or after "Connect printing..." screen
        '''
        self.fc.fd["moobe"].click_button_on_fp_from_printer(printer_obj)
        self.fc.fd["moobe"].verify_connected_printing_services_screen()
        self.fc.fd["moobe"].click_accept_all()
        self.fc.fd["moobe"].click_button_on_fp_from_printer(printer_obj)
 
    def find_printer_to_finish_awc_flow(self, ssid, password, printer_obj, printer_name):
        self.fc.fd["moobe"].verify_we_found_your_printer_screen()
        self.fc.fd["moobe"].select_continue()
        self.fc.fd["moobe"].verify_awc_flow(ssid, password, printer_obj)
        if self.fc.fd["moobe"].verify_connect_to_wifi_progress_screen():
            # Handle popup and click buttons on printer
            self.fc.fd["moobe"].click_button_on_fp_from_printer(printer_obj)
            self.fc.fd["moobe"].verify_connect_to_wifi_progress_screen(timeout=180, invisible=True)
        self.fc.fd["moobe"].verify_printer_connected_to_wifi_screen(printer_name, ssid)
        self.fc.fd["moobe"].select_continue()
    
    def before_register_you_printer(self, printer_ows_type, yeti_type):
        '''
        These are the follow before "Create an HP account or sign in to register your printer" screen
        printer_ows_type: The first three letters of the printer firmware version 
        yeti_type: e2e or flex
        '''
        if printer_ows_type == "PAL":
            self.__go_through_enjoy_hp_acct(create_account=False)
        elif printer_ows_type == "TAC":
            pass
            #todo
        elif printer_ows_type == "LEB":
            pass
            #todo
        else:
            self.__go_through_activate_hp_plus_yeti_printer(yeti_type, create_account=False)            

    def after_register_you_printer(self, printer_ows_type, install_driver=False):
        '''
        These are the follow after "Create an HP account or sign in to register your printer" screen
        '''
        if printer_ows_type == "PAL":
            self.__skip_instant_ink_flow()
            self.__help_make_better_product_flow()
        elif printer_ows_type == "TAC":
            pass
            #todo
        elif printer_ows_type == "LEB":
            pass
            #todo
        else:
            self.__skip_instant_ink_flow()
            self.__go_through_live_ui()
        if not install_driver:
            self.__go_through_other_screen_to_main_ui()

    def go_through_ows_flow(self, printer_ows_type, yeti_type=None):
        '''
        This is a method to go through OWS flow during the OOBE setup.
            1.On "Create an HP account..." screen, select "Create Account" button.
            2.If HP account is signed before ows flow, the "Create an HP account..." screen will not show.
        printer_ows_type: The first three letters of the printer firmware version 
        yeti_type: e2e or flex
        '''
        logging.debug("Go through OWS workflow... ")
        if printer_ows_type == "PAL":
            self.__palermo_gen2_inkjet_flow()
        elif printer_ows_type == "TAC":
            pass
            #todo
        elif printer_ows_type == "LEB":
            pass
            #todo
        else:
            self.__yeti_flow(yeti_type)

    def go_through_wireless_ows_flow(self, printer_ows_type, printer_obj, yeti_type):
        '''
        This is a method to go through OWS flow during the OOBE setup.
            1.On "Create an HP account..." screen, select "Sign In" button.
        printer_ows_type: The first three letters of the printer firmware version 
        yeti_type: e2e or flex
        '''
        logging.debug("Go through OWS workflow... ")
        self.connected_printing_services_flow(printer_obj)
        if printer_ows_type == "PAL":
            self.__go_through_enjoy_hp_acct(skip_accept_all=True)
            self.__skip_instant_ink_flow()
            self.__help_make_better_product_flow()
            self.__go_through_other_screen_to_main_ui()
        elif printer_ows_type == "TAC":
            pass
            #todo
        elif printer_ows_type == "LEB":
            pass
            #todo
        else:
            self.__go_through_activate_hp_plus_yeti_printer(yeti_type, skip_accept_all=True)
            self.__skip_instant_ink_flow()
            self.__go_through_live_ui()
            self.__go_through_other_screen_to_main_ui()

    def go_through_ows_sign_in_flow(self, printer_ows_type, username, password, yeti_type):
        '''
        This is a method to go through OWS flow during the OOBE setup.
            1.On "Create an HP account..." screen, select "Sign In" button.
        printer_ows_type: The first three letters of the printer firmware version 
        yeti_type: e2e or flex
        '''
        self.before_register_you_printer(printer_ows_type, yeti_type)
        self.sign_in_flow(username, password)
        self.after_register_you_printer(printer_ows_type)

    def go_through_ows_skip_flow(self, printer_ows_type, yeti_type, install_driver=False):
        '''
        This is a method to go through OWS flow during the OOBE setup.
            1.On "Create an HP account..." screen, select "Skip account activation" button.
        printer_ows_type: The first three letters of the printer firmware version 
        yeti_type: e2e or flex
        install_driver:
            1.False: Finish ows flow to main ui.
            2.True: The next step is to remove printer driver then check "Install driver to print" screen
        '''
        self.before_register_you_printer(printer_ows_type, yeti_type)
        self.skip_account_activation_flow()
        self.after_register_you_printer(printer_ows_type, install_driver)


