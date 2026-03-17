import logging
from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
from selenium.webdriver.common.keys import Keys

class Moobe(GothamFlow):
    flow_name = "moobe"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_accept_continue_btn(self):
        """
        Click accept&contiune button 
        """
        self.driver.click("accept_continue_btn")

    def select_continue(self, change_check=None, retry=3, check_kibana=False):
        """
        Click on Continue button
        It is used for all screens that have Continue button as name
        End of flow: next screen
        """
        if check_kibana:
            self.driver.click("printer_connected_continue_btn", change_check=change_check, retry=retry)
        else:
            self.driver.click("continue_btn", change_check=change_check, retry=retry)

    def click_access_wifi_password_dialog_no_thanks_btn(self):
        """
        Click No, Thanks button on Access Wi-Fi password dialog 
        """
        self.driver.click("access_wifi_password_dialog_no_thanks_btn")

    def click_connect_printer_to_wifi_screen_i_icon_btn(self):
        """
        Click i icon button on Connect printer to Wi-Fi screen 
        """
        self.driver.click("connect_printer_to_wifi_screen_i_icon_btn")

    def click_dialog_change_connection_btn(self):
        """
        Click Change Connection button on Need help connecting printer to Wi-Fi? dialog 
        """
        self.driver.click("help_dialog_change_connection_btn")

    def click_help_dialog_continue_btn(self):
        """
        Click Continue button on Need help connecting printer to Wi-Fi? dialog 
        """
        self.driver.click("help_dialog_continue_btn")

    def click_connect_printer_to_wifi_screen_change_network_link(self):
        """
        Click Change Network button on Connect printer to Wi-Fi screen 
        """
        self.driver.click("connect_printer_to_wifi_screen_change_network_link")

    def click_access_password_automatically_link(self):
        """
        Click Access Password Automatically link on Connect printer to Wi-Fi screen 
        """
        self.driver.click("access_password_automatically_link")

    def click_unable_to_access_wifi_password_dialog_ok_btn(self):
        """
        Click OK button on Unable to access Wi-Fi password 
        """
        self.driver.click("unable_to_access_wifi_password_dialog_ok_btn")

    def click_dialog_open_network_settings_btn(self):
        """
        Click Open Network Settings button on Change Wi-fi network dialog 
        """
        self.driver.click("dialog_open_network_settings_btn")

    def click_connect_printer_to_wifi_screen_connect_btn(self):
        """
        Click Connect button on Connect printer to Wi-Fi screen 
        """
        self.driver.click("connect_printer_to_wifi_screen_connect_btn")

    def click_try_again_btn(self):
        """
        Click Try Again button on Unable to connect printer to network dialog 
        """
        self.driver.click("unable_to_connect_printer_to_network_dialog_try_again_btn")
    
    def connect_printer_to_network(self, ssid, password):
        if self.verify_access_wifi_password_dialog(raise_e=False):
            self.select_continue()
        else:
            self.select_dropdown_listitem_for_wifi_name(ssid)
            self.input_password(password)
            self.select_continue()

    def go_through_connect_to_wifi_process(self):
        # if self.verify_accept_the_risk_dialog(raise_e=False):
        #     self.click_accept_continue_btn()
        self.verify_printer_connected_to_wifi_screen()
        self.select_continue()
       
    def select_dropdown_listitem_for_wifi_name(self, name):
        self.driver.click("wifi_networks_combox")
        self.driver.click("dynamic_listitem", format_specifier=[name])

    def input_password(self, content):
        self.driver.send_keys("connect_printer_to_wifi_screen_password_editbox", content)

    def handle_popup_on_connect_to_wifi_progress_screen(self, printer_obj):
        # Handle popup and click buttons on printer
        if self.verify_accept_the_risk_dialog(raise_e=False):
            self.click_accept_continue_btn()
        self.verify_printer_found_text(timeout=60)
        self.click_button_on_fp_from_printer(printer_obj)

    def click_button_on_fp_from_printer(self, printer_obj):
        if self.verify_press_info_btn_dialog(timeout=15, raise_e=False):    
            printer_obj.press_info_btn()
            logging.info("Done to click Info button on Printer")
        if self.verify_touch_checkmark_dialog(timeout=20, raise_e=False):
            getbuttonID = printer_obj.uc.getbuttonID()
            logging.info(getbuttonID)
            if "mdlg_action_button" in getbuttonID:
                printer_obj.click_front_panel_btn("mdlg_action_button")
            elif "fb_allow" in getbuttonID:
                printer_obj.click_front_panel_btn("fb_allow")
            else:
                raise Exception("No correct button shows on Printer front panel")
            logging.info("Done to click Allow button on Front Panel")

    # ---------------- Select your country or region ---------------- #
    def select_us_country_or_region(self):
        self.driver.click("country_or_region_item", format_specifier=[1])
        el = self.driver.wait_for_object("country_or_region_item", format_specifier=[1], timeout=2)
        el.send_keys(Keys.END)
        self.driver.click("country_or_region_item", format_specifier=[1])
        for i in range(15):
            if self.driver.click("unitec_states_item", raise_e=False):
                break
            else:
                el = self.driver.wait_for_object("country_or_region_item", format_specifier=[i], timeout=2)
                el.send_keys(Keys.UP)
        self.driver.click("continue_btn")

    # ---------------- Activate HP+ for smart printing capabilities ---------------- #
    def click_do_not_activate_hp_btn(self):
        self.driver.click("do_not_activate_hp_btn")

    # ---------------- Decline your exclusive HP+ offer? ---------------- #
    def click_decline_hp_plus_btn(self):
        self.driver.click("decline_hp_plus_btn")

    # ---------------- Printer dynamic security notice ---------------- #
    def click_printer_dynamic_continue_btn(self):
        self.driver.click("continue_btn")

    # ---------------- Create an HP account or sign in to register your printer ---------------- #
    def click_sign_in_button(self):
        self.driver.click("sign_in_btn")

    # ---------------- Let's load paper ---------------- #
    def click_let_us_continue_button(self):
        for _ in range(5):
            self.driver.click("next_group")
        self.driver.click("continue_btn")

    # ---------------- Need more time? ---------------- #
    def verify_need_more_time_dialog(self, raise_e=True):
        """
        Verify Need more time  dialog.
        """
        self.driver.wait_for_object("need_more_time_title", raise_e=raise_e)
    
    def click_dialog_try_again_btn(self):
        self.driver.click("try_again_btn")

    # ---------------- Are you sure you want to cancel? ---------------- #
    def verify_are_you_sure_you_want_to_cancel_dialog(self, raise_e=True):
        """
        Verify Are you sure you want to cancel?  dialog.
        """
        self.driver.wait_for_object("are_you_sure_you_want_to_cancel_text", raise_e=raise_e)
    
    def click_exit_setup_btn(self):
        self.driver.click("exit_setup_btn")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_we_found_your_printer_screen(self, title=False, timeout=10):
        """
        Verify We found your printer screen with:
         - title (Note - 1. Screen will not show the 'We found your printer' title when you are 
                    coming from the device picker with selected beaconing printer.
                2. Screen will show the 'We found your printer' title when you click
                    'My Printer Isn't Listed' btn and after finding one beaconing printer 
                    automatically, if more beaconing printers are available, will see a change 
                    printer link on the screen)
         - printer image
         - printer model name
         - desc: Time to connect, set up, and manage your HP printer!
         - button: Continue
        """
        if title:
            self.driver.wait_for_object("we_found_your_printer_screen_title", timeout=timeout)
        self.driver.wait_for_object("we_found_your_printer_screen_printer_image")
        self.driver.wait_for_object("we_found_your_printer_screen_printer_model")
        self.driver.wait_for_object("we_found_your_printer_screen_body")
        self.driver.wait_for_object("continue_btn")

    def verify_access_wifi_password_dialog(self, ssid, timeout=30):
        """
        Verify Access Wi-Fi password for {0} dialog with:
        - title
        - desc: This app can access your Wi-Fi password ad connec the printer to your network automatially.
                If you want the app to do this, select Continue. If prompt allow the app to make change to your device.
        - button: No, Thanks; Continue
        """
        self.driver.wait_for_object("access_wifi_password_dialog_title", format_specifier=[ssid], timeout=timeout)
        self.driver.wait_for_object("access_wifi_password_dialog_desc_1")
        self.driver.wait_for_object("access_wifi_password_dialog_desc_2")
        self.driver.wait_for_object("access_wifi_password_dialog_no_thanks_btn")
        self.driver.wait_for_object("continue_btn")

    def verify_accessing_wifi_password_text(self, raise_e=True):
        """
        Verify Accessing Wi-Fi Password text shows after clicking Continue btn on Access Wi-Fi password dialog.
        """
        self.driver.wait_for_object("accessing_wifi_password_text", raise_e=raise_e)

    def verify_unable_to_access_wifi_password_dialog(self, timeout=30, raise_e=True):
        """
        Verify Unable to access Wi-Fi password dialog with:
        - title
        - desc: Could not retrieve your Wi-Fi password automatically. Manually enter your Wi-Fi password to continue setup.
        - button: OK
        """
        return self.driver.wait_for_object("unable_to_access_wifi_password_dialog_title", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("unable_to_access_wifi_password_dialog_desc", raise_e=raise_e) and \
        self.driver.wait_for_object("unable_to_access_wifi_password_dialog_ok_btn", raise_e=raise_e)

    def verify_connect_printer_to_wifi_screen(self, printer_name, wifi_name, timeout=10):
        """
        Verify Connect printer to Wi-Fi screen with:
        - title
        - i icon button
        - printer image
        - printer name
        - wi-fi network text
        - wi-fi name
        - change network link
        - enter wifi password text
        - password edit box
        - access my wi-fi password automatically link
        - button: Connect
        """
        self.driver.wait_for_object("connect_printer_to_wifi_screen_title", timeout=timeout)
        self.driver.wait_for_object("connect_printer_to_wifi_screen_i_icon_btn")
        self.driver.wait_for_object("connect_printer_to_wifi_screen_printer_image")
        self.driver.wait_for_object("connect_printer_to_wifi_screen_wifi_network_text")
        self.driver.wait_for_object("connect_printer_to_wifi_screen_change_network_link")
        self.driver.wait_for_object("connect_printer_to_wifi_screen_enter_wifi_passwrod_text")
        self.driver.wait_for_object("connect_printer_to_wifi_screen_password_editbox")
        self.driver.wait_for_object("access_password_automatically_link")
        self.driver.wait_for_object("connect_printer_to_wifi_screen_connect_btn")

        assert printer_name in self.driver.wait_for_object("connect_printer_to_wifi_screen_printer_name").text
        assert wifi_name == self.driver.wait_for_object("connect_printer_to_wifi_screen_wifi_name").text

    def verify_oobe_select_wifi_password_screen(self, timeout=10):
        """
        Verify Connect printer to Wi-Fi screen with manually select wifi password with:
        """
        self.driver.wait_for_object("connect_printer_to_wifi_screen_title", timeout=timeout)
        self.driver.wait_for_object("connect_printer_to_wifi_screen_printer_image")
        self.driver.wait_for_object("choose_a_wifi_network_from_the_list_text")
        self.driver.wait_for_object("wifi_networks_combox")
        self.driver.wait_for_object("connect_printer_to_wifi_screen_refresh_network_list_link")
        self.driver.wait_for_object("enter_the_password_for_this_wifi_network_text")
        self.driver.wait_for_object("connect_printer_to_wifi_screen_password_editbox")
        self.driver.wait_for_object("connect_printer_to_wifi_screen_connect_btn")

    def verify_incorrect_password_text_shows(self, raise_e=True):
        return self.driver.wait_for_object("incorrect_password_text", raise_e=raise_e)

    def verify_need_help_connecting_printer_to_wifi_dialog(self):
        """
        Verify Need help connecting printer to Wi-Fi dialog with:
        - title
        - description
        - button: Change Connection, Continue
        """
        self.driver.wait_for_object("need_help_connecting_printer_to_wifi_dialog_title")
        self.driver.wait_for_object("need_help_connecting_printer_to_wifi_dialog_desc_1")
        self.driver.wait_for_object("need_help_connecting_printer_to_wifi_dialog_desc_2")
        self.driver.wait_for_object("need_help_connecting_printer_to_wifi_dialog_desc_3")
        self.driver.wait_for_object("help_dialog_change_connection_btn")
        self.driver.wait_for_object("help_dialog_continue_btn")

    def verify_change_wifi_network_dialog(self):
        """
        Verify Change Wi-Fi network dialog with:
        - title
        - description
        - button: Open Network Settings, Continue
        """
        self.driver.wait_for_object("change_wifi_network_dialog_title")
        self.driver.wait_for_object("change_wifi_network_dialog_desc_1")
        self.driver.wait_for_object("dialog_open_network_settings_btn")
        self.driver.wait_for_object("change_wifi_network_dialog_desc_2")
        self.driver.wait_for_object("continue_btn")

    def verify_connect_to_wifi_progress_screen(self, timeout=60, invisible=False):
        """
        Verify Connect to Wi-Fi screen with:
        - title
        - description
        """
        return self.driver.wait_for_object("connect_to_wifi_screen_title", timeout=timeout, invisible=invisible, raise_e=False) and\
        self.driver.wait_for_object("connect_to_wifi_screen_desc", timeout=timeout, invisible=invisible, raise_e=False)

    def verify_accept_the_risk_dialog(self, raise_e=True):
        return self.driver.wait_for_object("accept_continue_btn", raise_e=raise_e)

    def verify_printer_found_text(self, timeout=30):
        self.driver.wait_for_object("printer_found_text", timeout=timeout)

    def verify_unable_to_configure_the_printer_text(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("unable_to_configure_the_printer_text", timeout=timeout, raise_e=raise_e)

    def verify_printer_configured_text(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("printer_configured_text", timeout=timeout, raise_e=raise_e)

    def verify_printer_connected_to_wifi_screen(self, printer_name, wifi_name, timeout=300):
        """
        Verify Printer connected to Wi-Fi screen with:
         - title
         - desc: Let's continue our guided setup!
         - printer image
         - printer name
         - connect successful image
         - wifi signal image
         - wifi name
         - button: Continue
        """
        self.driver.wait_for_object("printer_connected_to_wifi_screen_title", timeout=timeout)
        self.driver.wait_for_object("printer_connected_to_wifi_screen_desc")
        self.driver.wait_for_object("printer_connected_to_wifi_screen_printer_image")
        self.driver.wait_for_object("printer_connected_to_wifi_screen_connect_image")
        self.driver.wait_for_object("printer_connected_to_wifi_screen_signal_image")
        self.driver.wait_for_object("continue_btn", timeout=30)

        assert printer_name in self.driver.wait_for_object("printer_connected_to_wifi_screen_printer_name").text
        assert wifi_name == self.driver.wait_for_object("printer_connected_to_wifi_screen_wifi_name").text


    def verify_press_info_btn_dialog(self, timeout=10, raise_e=True):
        return self.driver.wait_for_object("press_info_btn_title", timeout=timeout, raise_e=raise_e)

    def verify_touch_checkmark_dialog(self, timeout=10, raise_e=True):
        '''
        Touch the checkmark on your printer dialog display
        '''
        return self.driver.wait_for_object("touch_checkmark_text", timeout=timeout, raise_e=raise_e)

    def verify_unable_to_connect_printer_to_network_dialog(self, retry=False, timeout=30):
        """
        Verify Unable to Connect Printer to network dialog with:
         - title
         - desc: The printer could not connect to the Wi-Fi network. Restart your printer and try again.
         - button: Try Again
        """
        self.driver.wait_for_object("unable_to_connect_printer_to_network_dialog_title", timeout=timeout)
        self.driver.wait_for_object("unable_to_connect_printer_to_network_dialog_try_again_btn")
        if not retry:
            self.driver.wait_for_object("unable_to_connect_printer_to_network_dialog_desc")
        else:
            self.driver.wait_for_object("unable_to_connect_printer_to_network_dialog_desc_retry")
            self.driver.wait_for_object("continue_btn")
        
    # ---------------- Print from Other Devices Screen  ---------------- #
    def verify_print_from_other_devices(self):
        self.driver.wait_for_object("print_from_other_devices_txt")

    def select_skip_this_step(self):
        self.driver.click("skip_this_step")

    # ---------------- Setup complete!- Let's Print Screen  ---------------- #
    def verify_setup_complete_lets_print(self, timeout=30):
        self.driver.wait_for_object("setup_complete_lets_print_title", timeout=timeout)
        self.driver.wait_for_object("skip_printing_page")
        self.driver.wait_for_object("print_btn")

    def select_skip_printing_page(self):
        self.driver.click("skip_printing_page")

    def select_print_btn(self):
        self.driver.click("print_btn")

 # ---------------- Select your country or region ---------------- #
    def verify_select_your_country_or_region(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("select_your_country_title", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("continue_btn", timeout=timeout, raise_e=raise_e)

    # ---------------- Activate HP+ for smart printing capabilities ---------------- #
    def verify_activate_hp_puls_for_screen(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("do_not_activate_hp_btn", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("learn_more_btn", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("continue_btn", timeout=timeout, raise_e=raise_e)

    # ---------------- Decline your exclusive HP+ offer? ---------------- #
    def verify_decline_your_exclusive_screen(self):
        self.driver.wait_for_object("decline_hp_plus_btn")
        self.driver.wait_for_object("continue_with_hp_plus_btn")

    # ---------------- Printer dynamic security notice ---------------- #
    def verify_printer_dynamic_security_notice_screen(self):
        self.driver.wait_for_object("back_to_offer_btn")
        self.driver.wait_for_object("continue_btn")

    # ---------------- Create an HP account or sign in to register your printer ---------------- #
    def verify_create_or_sign_in_screen(self, timeout=25, raise_e=True):
        return self.driver.wait_for_object("skip_account_activation_btn", timeout=timeout, raise_e=raise_e) and \
        self.driver.wait_for_object("sign_in_btn", raise_e=raise_e) and \
        self.driver.wait_for_object("create_account_btn", raise_e=raise_e)

    def click_create_account_btn(self):
        self.driver.click("create_account_btn")

    def click_sign_in_btn(self):
        self.driver.click("sign_in_btn")

    def click_skip_account_activation_btn(self):
        self.driver.click("skip_account_activation_btn")

    # ---------------- Don't miss out on automatic printer and warranty registration! ---------------- #
    def verify_do_not_miss_out_on_screen(self):
        self.driver.wait_for_object("skip_account_activation_btn")
        self.driver.wait_for_object("back_to_account_btn")

    # ---------------- Printer updates ---------------- #
    def verify_printer_updates_screen(self, raise_e=True):
        return self.driver.wait_for_object("auto_update_option", raise_e=raise_e) and \
        self.driver.wait_for_object("notify_option", raise_e=raise_e) and \
        self.driver.wait_for_object("apply_btn", raise_e=raise_e)
    
    # ---------------- Connected printing services ---------------- #
    def verify_connected_printing_services_screen(self, timeout=30):
        """
        Verify current screen is "Connected printing services"
        """
        # self.driver.wait_for_object("title", timeout=timeout)
        self.driver.wait_for_object("accept_all_btn", timeout=timeout)
        self.driver.wait_for_object("decline_optional_data_btn", timeout=timeout)
        self.driver.wait_for_object("manage_option_btn", timeout=timeout)

    def click_accept_all(self):
        """"
        Click on Accept All button
        """
        self.driver.click("accept_all_btn")

    # ---------------- HP Instant Ink Screen  ---------------- #
    def verify_hp_instant_ink_plan_load(self):
        """
        Verify current screen is "HP Instant Ink" screen
        """
        self.driver.wait_for_object("do_not_enable_ink_delivery_btn")
        self.driver.wait_for_object("learn_more_btn")
        self.driver.wait_for_object("next_btn")

    def click_next_btn(self):
        """"
        Click on Next button
        """
        self.driver.click("next_btn")

    def click_do_not_enable_ink_delivery_btn(self):
        """"
        Click on Do not enable ink delivery button
        """
        self.driver.click("do_not_enable_ink_delivery_btn")

    # ---------------- Automatic printer updates  ---------------- #
    def verify_automatic_printer_updates_screen(self):
        """
        Verify current screen is "Automatic printer updates" screen
        """
        self.driver.wait_for_object("continue_btn")
        self.driver.wait_for_object("skip_instant_ink_btn")

    def click_skip_instant_ink_btn(self):
        """"
        Click on Skip Instant Ink button
        """
        self.driver.click("skip_instant_ink_btn")

    # ---------------- receive your ink ---------------- #
    def verify_receive_your_ink_screen(self):
        """
        Verify current screen is "Enter your details to receive your ink" screen
        """
        self.driver.wait_for_object("back_btn")
        self.driver.wait_for_object("skip_ink_benefit_btn")
        self.driver.wait_for_object("add_shipping_btn")

    def click_skip_ink_benefit_btn(self):
        """"
        Click on Skip Instant Ink button
        """
        self.driver.click("skip_ink_benefit_btn")

    # ---------------- Are you sure you want to skip Dialog---------------- #
    def verify_want_to_skip_dialog(self):
        """
        Verify current screen is "Are you sure you want to skip" screen
        """
        self.driver.wait_for_object("remind_me_later_btn")
        self.driver.wait_for_object("skip_offer_btn")
        self.driver.wait_for_object("try_it_months")

    def click_skip_offer_btn(self):
        """"
        Click on Skip Offerbutton
        """
        self.driver.click("skip_offer_btn")

    # ---------------- Time to install ink screen--------------- #
    def verify_time_install_ink_screen(self, raise_e=True):
        """
        Verify current screen is "Time to install ink" screen
        """
        return self.driver.wait_for_object("skip_installing_ink_btn", raise_e=raise_e)

    def click_skip_installing_ink_btn(self):
        """"
        Click on Skip installing ink button
        """
        self.driver.click("skip_installing_ink_btn")

    # ---------------- Let`s load paper --------------- #
    def verify_let_load_paper_screen(self):
        """
        Verify current screen is "Let`s load paper" screen
        """
        self.driver.wait_for_object("skip_loading_paper_btn")

    def click_skip_loading_paper_btn(self):
        """"
        Click on Skip loading paper button
        """
        self.driver.click("skip_loading_paper_btn")

    # ---------------- Printer up dates --------------- #
    def verify_printer_up_dates_screen(self):
        """
        Verify current screen is "Printer up dates" screen
        """
        self.driver.wait_for_object("apply_btn")

    def click_apply_btn(self):
        """"
        Click on Apply button
        """
        self.driver.click("apply_btn")

    def select_notify_opt(self):
        """"
        Select notify Option
        """
        self.driver.click("notify_option")

    # ---------------- Install driver to print --------------- #
    def verify_install_driver_to_print_screen(self):
        self.driver.wait_for_object("install_driver_to_print_title")
        self.driver.wait_for_object("install_launch_item") 
        self.driver.wait_for_object("launch_printers_and_scanners_text") 
        self.driver.wait_for_object("install_launch_image") 
        self.driver.wait_for_object("install_select_item") 
        self.driver.wait_for_object("depending_on_your_text") 
        self.driver.wait_for_object("install_select_image") 
        self.driver.wait_for_object("install_add_item") 
        self.driver.wait_for_object("choose_printer_then_click_text")
        self.driver.wait_for_object("install_add_image") 
        self.driver.wait_for_object("note_do_not_select_text") 
        self.driver.wait_for_object("driver_unavailble_btn") 
        self.driver.wait_for_object("printers_scanners_btn")
        self.driver.wait_for_object("continue_btn")

    def click_driver_unavailable_btn(self):
        """"
        Click on Driver Unavailable button
        """
        self.driver.click("printers_scanners_btn")
    
    def click_printers_scanners_btn(self):
        """"
        Click on Printers & Scanners button
        """
        self.driver.click("printers_scanners_btn")

    # ---------------- Remove and add the printer again --------------- #
    def verify_remove_and_add_screen(self):
        self.driver.wait_for_object("remove_and_add_title")
        self.driver.wait_for_object("circle_one") 
        self.driver.wait_for_object("remove_the_printer_text") 
        self.driver.wait_for_object("on_the_printers_text") 
        self.driver.wait_for_object("circle_two") 
        self.driver.wait_for_object("add_the_printer_again_text") 
        self.driver.wait_for_object("depending_on_your_2_text") 
        self.driver.wait_for_object("circle_three") 
        self.driver.wait_for_object("if_the_driver_installs_text")
        self.driver.wait_for_object("if_the_problem_persists_text") 
        self.driver.wait_for_object("on_your_computer_text") 
        self.driver.wait_for_object("for_additional_help_text")
        self.driver.wait_for_object("hp_support_link")
        self.driver.wait_for_object("back_btn")
        self.driver.wait_for_object("printers_scanners_btn")
        self.driver.wait_for_object("continue_btn")

    def click_back_btn(self):
        """"
        Click on Back button
        """
        self.driver.click("back_btn")

    def click_hp_support_link(self):
        """"
        Click on HP Support Link
        """
        self.driver.click("hp_support_link")

    # ---------------- Finish AWC fow --------------- #
    def verify_awc_flow(self, ssid, password, printer_obj):
        self.verify_access_wifi_password_dialog(ssid)
        self.select_continue()
        if self.verify_unable_to_access_wifi_password_dialog(raise_e=False):
            self.click_unable_to_access_wifi_password_dialog_ok_btn()
            self.input_password(password)
            self.select_continue()

    # ---------------- Unable to register the printer to your account  ---------------- #
    def verify_unable_to_register_the_printer_screen(self, timeout=30):
        self.driver.wait_for_object("unable_to_register_text", timeout=timeout)
        self.driver.wait_for_object("try_again_btn")
        self.driver.wait_for_object("exit_setup_btn")

    def click_exit_setup_button(self):
        self.driver.click("exit_setup_btn")

        
