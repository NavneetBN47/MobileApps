from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.ma_misc import ma_misc
import logging

class TrafficDirector(OWSFlow):
    """
        PSW = Printer Setup Website is same as TD = Traffic Director
        Contains all of the elements and flows associated Printer Setup Website
        pie, stage: https://onboardingcenter.<stack>.portalshell.int.hp.com/<printer sku>
        Prod: https://start.hp.com/<printer sku>
        
        kebin profile: 537P6A (Elion), marconi: 403x0a (Base), moreto: 40Q50A (Hi), Victoria: 714N5A (Plus)
    """
    file_path = __file__
    flow_name = "traffic_director"
    printer_sku = {"marconi_paas":"4V2L9A", "marconi_base":"4V2M9C", "marconi_base_yeti":"403X2A",
                   "marconi_hi":"404K5C", "marconi_hi_yeti":"404M0A","moreto_base": "405W2C", 
                   "moreto_base_yeti":"405T6A","moreto_hi":"68K75B", "moreto_hi_yeti":"40Q35A","eddington":"537P5C", 
                   "eddington_yeti":"537P6A","elion":"53N94C","elion_yeti":"53N95B", "victoria_base":"714J7B",
                   "victoria_plus":"714D5C", "cherry":"8X3E3A","lotus":"8X3G2A", "trillium_standard":"38Q66C", "trillium_ink_advantage":"AJ4Y5A",
                   "trillium_uia":"89F94A", "trillium_plus_standard":"A24JLC", "trillium_plus_ink_advantage":"89G05C", "trillium_plus_uia":"B3ZF3A"
                   }
    
    friendly_url ={"victoria_base_IA":"dj6100", "victoria_paas":"envy6100r", "victoria_base":"envy6100", "victoria_yeti":"envy6100e",
                   "victoria_plus_IA":"dj6500", "victoria_plus":"envy6500", "victoria_plus_yeti":"envy6500e", 
                   "cherry_ams_row": "LJP4006", "cherry_emea": "LJP4007", "cherry_chin": "LJP4008",
                   "cherry_big_deal": "LJP4009", "lotus_ams_row": "LJP4112", "lotus_emea": "LJP4113",
                   "lotus_chin": "LJP4114","lotus_big_deal": "LJP4115", "trillium":"dj2900",
                   "trillium_standard": "dj2900", "trillium_ink_advantage": "djia2900",
                   "trillium_uia": "djia5100", "trillium_plus_standard": "dj4300",
                   "trillium_plus_ink_advantage": "djia4300", "trillium_plus_uia": "djia5800"
                }

    def __init__(self, driver, printer_profile):
        super(TrafficDirector, self).__init__(driver)
        self.stack = driver.session_data["stack"]
        self.sku = self.printer_sku.get(printer_profile, None)
        self.endpoint = self.friendly_url.get(printer_profile, None)
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        if self.stack != "prod":
            self.td_url = "https://onboardingcenter.{}.portalshell.int.hp.com/{}/{}".format(self.stack, self.locale, self.sku if self.sku else self.endpoint)    
        else:
            self.td_url = "https://start.hp.com/{}/{}".format(self.locale, self.sku)


    def normalize_profile(self, printer_profile):
        """Normalize printer profile to base name for Spec file lookups"""
        if printer_profile.startswith("marconi_base"):
            return "MarconiBase"
        elif printer_profile.startswith("marconi_hi"):
            return "MarconiHi"
        elif printer_profile.startswith("moreto"):
            return "MoretoBase"
        elif printer_profile.startswith("victoria_base"):
            return "VictoriaBase"
        elif printer_profile.startswith("victoria_plus"):
            return "VictoriaPlus"
        elif printer_profile.startswith("eddington"):
            return "Eddington"
        elif printer_profile.startswith("elion"):
            return "Elion"
        elif printer_profile.startswith(("cherry", "lotus", "trillium")):
            return printer_profile
        else:
            raise ValueError(f"Unknown printer profile prefix in '{printer_profile}'")

    
########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################


    def click_start_setup_btn(self):
        """
        Click Start Setup button on onboarding center landing page.
        """
        self.driver.click("start_setup_button")
    
    def click_watch_video_button(self):
        self.driver.click("watch_video_button")
    
    def click_watch_video_modal_close_button(self):
        self.driver.click("watch_video_modal_close_button")
    
    def click_setup_tab(self):
        self.driver.click("setup_tab")

    def click_printer_features_btn(self):
        self.driver.click("printer_features_btn")
    
    def click_get_help_btn(self):
        self.driver.click("get_help_btn")

    def click_get_help_btn_sidemenu(self):
        self.driver.click("get_help_btn_sidemenu")

    def click_software_unable_to_find_printer_content(self):
        self.driver.click("software_unable_to_find_printer_content")
    
    def click_stay_near_the_printer(self):
        self.driver.click("stay_near_the_printer")
    
    def click_disconnect_from_vpn_drop_down(self):
        self.driver.click("disconnect_from_vpn_drop_down")

    def click_turn_on_bluetooth_and_location_drop_down(self):
        self.driver.click("turn_on_bluetooth_and_location_drop_down")

    def click_turn_on_wifi_during_setup(self):
        self.driver.click("turn_on_wifi_during_setup")
    
    def click_get_help_connectivity_subtab_content(self):
        self.driver.click("get_help_connectivity_subtab_content")

    def click_install_on_windows_drop_down(self):
        self.driver.click("install_on_windows_drop_down")
    
    def click_install_on_macOS_drop_down(self):
        self.driver.click("install_on_macOS_drop_down")
    
    def click_use_hp_smart_chromeos_drop_down(self):
        self.driver.click("use_hp_smart_chromeos_drop_down")
    
    def click_install_on_mobile_drop_down(self):
        self.driver.click("install_on_mobile_drop_down")
    
    def get_default_locale_from_selector(self):
        return self.driver.get_attribute("locale_selector_link", "data-locale")
    
    def click_locale_selector_link(self):
        self.driver.click("locale_selector_link")
    
    def click_locale_selector_close_btn(self):
        self.driver.click("language_selector_close_btn")
    
    def select_region_from_selector(self, region):
        self.driver.click("language_region_selector", format_specifier=[region])
    
    def click_get_help_subtab_connectivity(self):
        self.driver.click("get_help_connectivity")
    
    def click_get_help_subtab_hp_smart_installation(self):
        self.driver.click("get_help_hp_smart_installation")
    
    def click_supported_os_drop_down_on_subtab_hp_smart_installantion(self):
        self.driver.click("supported_os_for_hp_smart")

    def click_printer_features_btn_hp_plus_instant_ink(self):
        self.driver.click("learn_tab_hp_plus_instant_ink")

    def click_printer_features_btn_printer_features(self):
        self.driver.click("learn_tab_printer_features")

    def click_printer_features_btn_sidemenu(self):
        self.driver.click("printer_features_btn_sidemenu")
    
    def click_hp_plus_and_instant_ink_sidemenu_btn(self):
        self.driver.click("hp_plus_and_instant_ink_sidemenu_btn")
    
    def click_hp_support_button_tab(self):
        self.driver.click("hp_support_button_tab")
    
    def click_hp_plus_learn_more_url(self):
        self.driver.click("hp_plus_url")

    def click_instant_ink_learn_more_url(self):
        self.driver.click("instant_ink_url")

    def click_help_initial_setup(self):
        self.driver.click("help_initial_setup")

    def click_hp_support_product_page(self):
        self.driver.click("hp_support_product_page")
    
    def click_next_btn(self):
        """
        Click Next button for live UI steps.
        """
        self.driver.click("next_button_label")

    def click_back_btn(self):
        self.driver.click("back_button_label")
    
    def click_animation_card_next_btn(self):
        """
        Click Next forward btn right next to animation card on any live ui step.
        """
        self.driver.click("animation_card_next_arrow")
    
    def click_view_animations_button(self):
        self.driver.click("view_animations_button")
    
    def click_continue_online_setp_btn(self):
        """
        Click Continue Online setup button on onboarding center marconi page.
        """
        self.driver.click("continue_online_setup_btn") 

    def click_already_connected_to_network_button(self):
        """
        click Printer already conneted to the network on Connect printer to network instrauction page.
        """
        if self.verify_connect_printer_to_network is not False:
            self.driver.click("already_connected_to_the_network_btn")

    def click_veneer_stepper_step(self, step):
        """
        Click step 1 on veneer stepper on onboarding center marconi page.
        """
        self.driver.click("veneer_stepper_step_{}".format(step))

    def click_close_bnefits_overlay_modal_btn(self):
        """
        Click right top corner X button on HP Plus printer benefits overlay modal
        """
        self.driver.click("close_bnefits_overlay_modal_btn")

    def click_activate_hp_plus_btn(self):
        self.driver.click("activate_hp_plus")

    def click_printer_dynamic_security_notice_ok_btn(self):
        """
        Click Ok button on printer dynmaic security notice overlay seen after clicking decline hp plus offer btn on hp plus requirments page.
        """
        self.driver.click("printer_dynamic_security_notice_ok_btn")

    def click_hp_support_url(self):
        """
        Click HP Support url on onboarding center Landing  page.
        """
        self.driver.click("hp_support_url")

    def click_footer_steps(self):
        self.driver.click("footer")


########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    @screenshot_compare()
    def verify_onboarding_center_page(self, timeout=30):
        """
        Verify onboarding center marconi page.
        """
        return self.driver.wait_for_object("onboarding_center_page", timeout=timeout)

    @screenshot_compare(root_obj="landing_page_title", include_param=["--printer-profile"])
    @screenshot_compare(root_obj="landing_page_image", include_param=["--printer-profile"])
    def verify_landing_page_title(self, raise_e=True):
        """
        Verify landing page title on onboarding center landing page.
        """
        return self.driver.wait_for_object("landing_page_title", raise_e=raise_e)
    
    @screenshot_compare(root_obj="landing_page_description", include_param=["--printer-profile"])
    def verify_landing_page_description(self):
        self.driver.wait_for_object("landing_page_description")
    
    @screenshot_compare(root_obj="setup_steps_content", include_param=["--printer-profile"])
    def verify_setup_steps_content(self, raise_e=True):
        """
        Verify setup steps content on onboarding center landing page.
        """
        return self.driver.wait_for_object("setup_steps_content", raise_e=raise_e)
    
    def verify_enter_delta_program_password(self):
        """
        Verify Delta pragram password page enter HPDELTA2022.
        """
        self.driver.wait_for_object("access_delta_program_security_word", timeout=30)
        self.driver.send_keys("access_delta_program_security_word", "HPDELTA2022")
        self.driver.click("go_btn")
    
    def verify_three_tabs_in_header(self):
        """
        Verifies if there are three tabs in the header.
        """
        self.driver.wait_for_object("three_tabs_header")
        assert self.driver.get_attribute("setup_tab", "aria-selected") == "true", "Set-up is not shown as default"
        assert self.driver.get_attribute("learn_tab", "aria-selected") == "false", "Learn Tab is shown as default"
        assert self.driver.get_attribute("get_help_btn", "aria-selected") == "false", "Get help is shown as default"

    def verify_get_help_tab(self):
        return self.driver.wait_for_object("get_help_tab")
    
    def verify_hp_plus_and_instant_ink_sidemenu_btn(self):
        self.driver.wait_for_object("hp_plus_and_instant_ink_sidemenu_btn")
    
    def verify_software_unable_to_find_printer_content(self, raise_e=True):
        return self.driver.wait_for_object("software_unable_to_find_printer_content", raise_e=raise_e)

    def verify_stay_near_the_printer(self):
        self.driver.wait_for_object("stay_near_the_printer")

    def verify_stay_near_the_printer_content(self, raise_e=True):
        return self.driver.wait_for_object("stay_near_the_printer_content", raise_e=raise_e)
    
    def verify_disconnect_from_vpn_drop_down(self):
        self.driver.wait_for_object("disconnect_from_vpn_drop_down")

    def verify_disconnect_from_vpn_content(self, raise_e=True):
        return self.driver.wait_for_object("disconnect_from_vpn_content", raise_e=raise_e)

    def verify_turn_on_bluetooth_and_location_drop_down(self):
        self.driver.wait_for_object("turn_on_bluetooth_and_location_drop_down")

    def verify_turn_on_bluetooth_and_location_content(self, raise_e=True):
        return self.driver.wait_for_object("turn_on_bluetooth_and_location_content", raise_e=raise_e)

    def verify_turn_on_wifi_during_setup(self):
        self.driver.wait_for_object("turn_on_wifi_during_setup")

    def verify_turn_on_wifi_during_setup_content(self, raise_e=True):
        return self.driver.wait_for_object("turn_on_wifi_during_setup_content", raise_e=raise_e)
    
    def verify_start_setup_btn(self, clickable=False,raise_e=True, timeout=15):
        """
        Verify Start Setup button on onboarding center landing page.
        """
        return self.driver.wait_for_object("start_setup_button", clickable=clickable, raise_e=raise_e, timeout=timeout)

    def verify_watch_video_btn(self, raise_e=True):
        """
        verify watch video button on onboarding center landing page.
        """
        return self.driver.wait_for_object("watch_video_button", raise_e=raise_e)

    def verify_watch_video_modal(self):
        self.driver.wait_for_object("watch_video_modal")
    
    def verify_watch_video_subtitle(self):
        self.driver.wait_for_object("watch_video_subtitle")

    def verify_footer_live_ui_steps(self):
        """
        Verify footer on live ui steps for traffic director marconi flow.
        """
        self.driver.wait_for_object("footer")
    
    def verify_country_language_selector_link(self, raise_e=True):
        return self.driver.wait_for_object("locale_selector_link", raise_e=raise_e)

    def verify_locale_selector_overlay(self, invisible=False):
        return self.driver.wait_for_object("locale_selector_overlay", invisible=invisible)
    
    def verify_language_region_selector(self):
        result = []
        region = ["EN_AU", "NL_BE", "FR_BE", "PT_BR", "EN_CA", "FR_CA", "CS_CZ", "DA_DK", "DE_DE", "ET_EE", "ES_ES", "FR_FR", "HR_HR", "ID_ID", "EN_IE",
                  "IT_IT", "LV_LV", "LT_LT", "FR_LU", "HU_HU", "EN_MT", "NL_NL", "EN_NZ", "NB_NO", "DE_AT", "PL_PL", "PT_PT", "RO_RO", "DE_CH", "SL_SI",
                  "SK_SK", "FR_CH", "FI_FI", "SV_SE", "TR_TR", "EN_GB", "EN_US", "VI_VN", "EL_GR", "BG_BG", "KK_KZ", "RU_RU", "SR_RS", "UK_UA", "HE_IL",
                  "AR_SA", "TH_TH", "KO_KR", "JA_JP", "ZH_CN", "ZH_HK", "ZH_TW"]
        for i in region:
            if not self.driver.wait_for_object("language_region_selector", format_specifier=[i], raise_e=False):
                result.append(False)
                logging.warning("this language/region is not listed in the overlay modal: {}".format(i))
        if False in result:
            raise AssertionError("One or multiple languages are not listed in the language overlay modal")
    
    def verify_default_region_flag(self, attribute):
        return self.driver.get_attribute("default_region_flag", attribute)
    
    def verify_china_region_flag(self):
        assert self.driver.get_attribute("china_region_flag", "id"), "China region Flag not shown"

    def verify_taiwan_region_flag_not_shown(self):
        assert self.driver.get_attribute("language_region_selector", "id", format_specifier=["ZH_TW"]) == "", "taiwan region Flag is shown"

    def verify_hongkong_region_flag_not_shown(self):
        assert self.driver.get_attribute("language_region_selector", "id", format_specifier=["ZH_HK"]) == "", "hongkong region Flag is shown"
    
    def verify_setup_tab(self):
        self.driver.wait_for_object("setup_tab")
    
    def verify_printer_features_btn(self):
        self.driver.wait_for_object("printer_features_btn")

    @screenshot_compare(root_obj="printer_hardware_content", include_param=["--printer-profile"])
    @screenshot_compare(root_obj="control_panel_content", include_param=["--printer-profile"])
    @screenshot_compare(root_obj="printer_front_hardware_image", include_param=["--printer-profile"])
    @screenshot_compare(root_obj="printer_back_hardware_image", include_param=["--printer-profile"])
    def verify_printer_parts(self):
        """
        Verify printer parts on printer features page.
        """
        self.driver.wait_for_object("printer_features_sidemenu")
        self.driver.wait_for_object("printer_hardware_title")
        self.driver.wait_for_object("printer_hardware_content")
        self.driver.wait_for_object("do_not_use_usb_for_setup")
        self.driver.wait_for_object("control_panel_content")

    def verify_learn_tab_printer_features_is_default_selected_shown(self):
        assert self.driver.get_attribute("learn_tab_printer_features", "aria-selected") == "true", "printer features tab is not shown by default"

    def verify_hp_plus_instant_ink_tab(self):
        self.driver.wait_for_object("instant_ink_info_tab")
        self.driver.wait_for_object("instant_ink_url")        
    
    def verify_hp_plus_page(self):
        self.driver.add_window("hp_plus")
        self.driver.switch_window("hp_plus")
        assert "hp-plus" in self.driver.current_url, "Expecting 'hp-plus' in url, got: {}".format(self.driver.current_url)
        self.driver.close_window("hp_plus")

    def verify_instant_ink_page(self):
        self.driver.add_window("instant_ink")
        self.driver.switch_window("instant_ink")
        assert "instantink" in self.driver.current_url, "Expecting 'instantink' in url, got: {}".format(self.driver.current_url)
        self.driver.close_window("instant_ink")

    def verify_instant_ink_subtab_content(self):
        self.driver.wait_for_object("learn_tab_instant_ink_content")
    
    def verify_learn_tab_content(self):
        self.driver.wait_for_object("learn_tab_content")
    
    def verify_learn_tab_print_features_content(self, raise_e=True):
        return self.driver.wait_for_object("learn_tab_print_features_content", raise_e=raise_e)
    
    def verify_learn_tab_instant_ink_content(self, raise_e=True):
        return self.driver.wait_for_object("learn_tab_instant_ink_content", raise_e=raise_e)
    
    def verify_get_help_btn(self):
        self.driver.wait_for_object("get_help_btn")
    
    def verify_get_help_connectivity_subtab_content(self):
        self.driver.wait_for_object("get_help_connectivity_subtab_content")
    
    def verify_get_help_hp_smart_installation_content(self):
        self.driver.wait_for_object("get_help_hp_smart_installation_content")
    
    def verify_hp_smart_installation_subtab(self):
        self.driver.wait_for_object("subtab_hp_smart_installation_hp_smart_btn")

    def verify_supported_os_drop_down_content(self):
        self.driver.wait_for_object("supported_os_for_hp_smart_content")

    def verify_install_on_windows_content(self):
        self.driver.wait_for_object("install_on_windows_content")

    def verify_install_on_windows_content(self):
        self.driver.wait_for_object("install_on_windows_content")

    def verify_install_on_macOS_content(self):
        self.driver.wait_for_object("install_on_macOS_content")

    def verify_install_on_mobile_content(self):
        self.driver.wait_for_object("install_on_mobile_content")

    def verify_use_hp_smart_chromeos_content(self):
        self.driver.wait_for_object("use_hp_smart_chromeos_content")

    def verify_hp_support_button_tab(self):
        self.driver.wait_for_object("hp_support_button_tab")
    
    def verify_help_initial_setup(self):
        self.driver.wait_for_object("help_initial_setup")
    
    def verify_hp_support_product_page(self):
        self.driver.wait_for_object("hp_support_product_page")

    def verify_hp_support_user_guide(self):
        self.driver.wait_for_object("hp_support_user_guide")
    
    def verify_next_btn(self, clickable=False, raise_e=True):
        """
        Verify Next button for live UI steps.
        """
        return self.driver.wait_for_object("next_button_label", clickable=clickable, raise_e=raise_e)

    def verify_back_btn(self):
        """
        Verify Back button for Live Ui steps marconi.
        """
        self.driver.wait_for_object("back_button_label")
    
    @screenshot_compare(root_obj="sidebar")
    def verify_sidebar(self):
        """
        Verify sidebar which had veneer stepper Highlighted step as user progresses such as Languange and Country/region, paper, ink etc.
        """
        self.driver.wait_for_object("sidebar")
    
    @screenshot_compare(root_obj="veneer_stepper")
    def verify_veneer_stepper(self):
        self.driver.wait_for_object("veneer_stepper")
    
    def verify_carasoul_slider(self):
        self.driver.wait_for_object("carasoul_slider")
    
    def verify_animation_card_next_btn(self, raise_e=True):
        """
        Verify Next forward btn right next to animation card on any live ui step.
        """
        return self.driver.wait_for_object("animation_card_next_arrow", raise_e=raise_e)
    
    def verify_animation_card_back_btn(self):
        """"
        verify Back Arrow btn left to cards with animation can be seen when there are multiple cards.
        """
        self.driver.wait_for_object("animation_card_prev_arrow")
    
    def verify_current_live_ui_step_in_sidebar(self, step):
        """
        Verify Current Live UI as per veneer Stepper. The Sidebar stepper will change as user moves back and forth step.
        """
        self.driver.wait_for_object("veneer_step_{}_current".format(step))
        
    def verify_current_carousal_dot(self, dot):
        """
        There are carousal dots under the cards turns blue when user switch between the cards. Locator for the blue dot changes to 'dot-0-currnet' from 'dot-o-'. 
        using this to verify the correct dots turns blue for correct card.
        """
        self.driver.wait_for_object("carasoul_dot_{}".format(dot))

    def verify_connect_printer_to_network(self):
        """
        Verify connect printer to network /printer-network page show instructions of how to connect printer to network page.
        """
        return self.driver.wait_for_object("connect_printer_to_network", raise_e=False)
    
    @screenshot_compare(root_obj="printer_dynamic_security_notice")
    def verify_printer_dynamic_security_notice(self):
        """
        Verify Printer Dynamic security notice overlay after clicking decline HP+ offer on HP Plus requirments page.
        """
        self.driver.wait_for_object("printer_dynamic_security_notice", displayed=False)

    def verify_printer_dynamic_security_notice_ok_btn(self):
        """
        verify Ok button on printer dynmaic security notice overlay seen after clicking decline hp plus offer btn on hp plus requirments page.
        """
        self.driver.wait_for_object("printer_dynamic_security_notice_ok_btn")

    def verify_incorrect_url_landing_page(self, timeout=10):
        """
        Verify Incorrect URL landing page.
        """
        self.driver.wait_for_object("unable_to_find_setup_instructions_header", timeout=timeout)
        self.driver.wait_for_object("unable_to_find_setup_instructions_subheader")
        self.driver.wait_for_object("unable_to_find_setup_instructions_start_setup_btn")
        self.driver.wait_for_object("unable_to_find_setup_instructions_tips_and_links")
        self.driver.wait_for_object("unable_to_find_setup_instructions_image")