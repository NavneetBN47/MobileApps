from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys

class Scan(GothamFlow):
    flow_name = "scan"

    SOURCE = "source"
    preset = "preset"
    AREA = "scan_area"
    OUTPUT = "output"
    DPI = "resolution"
    HELP_CENTER = ["support.hp.com"]

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_preview_btn(self):
        self.driver.click("preview_btn")

    def click_scan_btn(self):
        self.driver.click("scan_btn")

    def select_import_btn(self):
        self.driver.click("import_btn")

    def click_start_scan_text(self):
        self.driver.click("start_scan_text")

    def select_auto_enhancement_icon(self):
        """
        Click on auto enhancement icon located on 
        top right of scanner screen below the title bar close to gear icon -> auto enhancement panel shows
        """
        self.driver.click("auto_enhancement_icon")
    
    def click_cancel_btn(self):
        self.driver.click("cancel_btn")

    def click_multi_scan_btn(self):
        self.driver.click("multi_scan_btn")

    def click_reset_settings_btn(self):
        self.driver.click("reset_settings_btn")

    def click_gear_icon(self):
        self.driver.click("gear_icon")

    def click_detect_edges_box(self):
        self.driver.click("detect_edges_box")

    def click_scan_btn_with_doc_feeder(self):
        self.driver.click("doc_scan_btn")
    
    # ---------------- New Scan Auto-Enhancements dialog ---------------- #
    def click_auto_enhancement_cancel_btn(self):
        self.driver.click("auto_enhancement_cancel_btn")

    def click_get_started_btn(self, timeout=3):
        self.driver.click("auto_enhancement_get_started_btn", timeout=timeout)

    def click_learn_more_link(self):
        self.driver.click("learn_more_link")

    # ---------------- Scanner Settings ---------------- #
    def select_source_dropdown(self):
        self.driver.click("source_dropdown")

    def select_presets_dropdown(self):
        self.driver.click("presets_dropdown")

    def select_scan_area_dropdown(self):
        self.driver.click("scan_area_dropdown")

    def select_output_dropdown(self):
        self.driver.click("output_dropdown")

    def select_resolution_dropdown(self):
        self.driver.click("resolution_dropdown")

    def select_dropdown_listitem(self, dropdown, name):
        """
        @param dropdown:
            - source
            - preset
            - scan_area
            - output
            - resolution
        @param name:
            name of the listitem
        """
        if dropdown == "source":
            self.select_source_dropdown()
        elif dropdown == "preset":
            self.select_presets_dropdown()
        elif dropdown == "scan_area":
            self.select_scan_area_dropdown()
        elif dropdown == "output":
            self.select_output_dropdown()
        elif dropdown == "resolution":
            self.select_resolution_dropdown()

        self.verify_dropdown_listitem(name).click()

    def click_2_sided_box(self):
        self.driver.click("2_sided_box")
    
    # ---------------- auto enhancement panel ---------------- #
    def click_auto_enhancements_toggle(self):
        self.driver.click("auto_enhancements_toggle")

    def click_auto_heal_toggle(self):
         if self.driver.wait_for_object("auto_heal_text", raise_e=False):
            self.driver.click("auto_heal_toggle")

    def click_auto_orientation_toggle(self):
        self.driver.click("auto_orientation_toggle")

    def hover_resolution_icon(self):
        self.driver.hover("resolution_dropdown", x_offset = 0.95, y_offset = 0.22)
        

    # ---------------- Import dialog ---------------- #   
    def click_import_dialog_get_started_btn(self):
        self.driver.click("import_dialog_get_started_btn") 

    # ---------------- Import screen ---------------- #   
    def click_import_apply_btn(self):
        self.driver.click("import_apply_btn") 

    def click_import_flatten_btn(self):
        self.driver.click("detect_edges_flatten_text") 
    
    # ---------------- Scan Preview screen ---------------- #   
    def click_menu_btn(self):
        '''
        Click on the blue circle growing icon in the upper right corner of 
        the scanned page on the Preview screen 
        '''
        self.driver.click("menu_btn")

    def click_id_card_menu_btn(self):
        '''
        Click on the blue circle growing icon in the upper right corner of 
        the scanned page on the ID Card screen 
        '''
        self.driver.click("id_card_menu_btn")
    
    def click_save_btn(self):
        self.driver.click("save_btn") 
    
    def click_edit_btn(self):
        self.driver.click("edit_btn") 

    def click_print_btn(self):
        self.driver.click("print_btn") 

    def click_shortcuts_btn(self):
        self.driver.click("shortcuts_btn") 

    def click_share_btn(self):
        self.driver.click("share_btn") 

    def click_fax_btn(self):
        self.driver.click("fax_btn") 

    def click_dialog_close_btn(self):
        self.driver.click("dialog_close_btn")

    def click_add_pages_btn(self):
        self.driver.click("add_pages_btn")

    def click_multi_add_pages_btn(self):
        self.driver.click("multi_add_pages_btn")

    def click_multi_menu_btn(self):
        self.driver.click("multi_menu_btn")

    def click_multi_delete_btn(self):
        self.driver.click("multi_delete_btn")

    def click_thumbnail_view_icon(self):
        self.driver.click("thumbnail_view_icon")

    def hover_thumbnail_view_icon(self):
        self.driver.hover("thumbnail_view_icon")

    def click_text_extract_btn(self):
        self.driver.click("text_extract_btn")

    def click_scribble_btn(self):
        # self.driver.click("scribble_btn")
        self.driver.click("scribble_btn", change_check={"wait_obj": "scribble_btn", "invisible": True})

    def click_multi_scribble_btn(self):
        self.driver.click("multi_scribble_btn")

    def click_replace_btn(self):
        self.driver.click("replace_btn")

    def click_single_delete_btn(self):
        self.driver.click("single_delete_btn")

    def click_replace_cancel_btn(self):
        self.driver.click("replace_cancel_btn")

    def click_replace_scan_btn(self):
        self.driver.click("replace_scan_btn")

    def click_start_icon(self):
        self.driver.click("start_icon")

    def click_manage_btn(self):
        self.driver.click("manage_btn")

    def click_create_btn(self):
        self.driver.click("create_btn")

    def click_new_mark_cancel_btn(self):
        self.driver.click("new_mark_cancel_btn")

    def select_mart_text_opt(self):
        self.driver.click("mark_text_opt")

    def enter_mart_text(self):
        self.driver.send_keys("mark_text_edit", "good!") 

    def click_mart_done_btn(self):
        self.driver.click("new_mark_done_btn")

    def select_first_mart_text(self):
        self.driver.click("mark_text")

    def select_first_mart_box(self):
        self.driver.click("mark_text_box")

    def click_mark_delete_btn(self):
        self.driver.click("mark_delete_btn")
        
    def click_pic_item(self, index):
        self.driver.click("pic_item", format_specifier=[index])

    def click_left_arrow_btn(self):
        self.driver.click("left_arrow_btn")

    def click_righ_arrow_btn(self):
        self.driver.click("righ_arrow_btn")

    def right_click_pic_item(self, index):
        obj = self.driver.find_object("pic_item", format_specifier=[index])
        self.driver.click_by_coordinates(obj, right_click=True)

    def click_problem_shortcut_dialog_cancel_btn(self):
        self.driver.click("dialog_cancel_btn")

    def click_problem_shortcut_dialog_skip_printing_btn(self):
        self.driver.click("dialog_skip_printing_btn")

    def dismiss_are_you_enjoy_dialog(self): 
        if self.driver.wait_for_object("are_you_enjoy_text", raise_e=False):
            self.click_are_you_dialog_not_now_btn()
            self.verify_are_you_enjoying_dialog_disappear()
            self.verify_sorry_to_hear_dialog()
            self.click_sorry_to_dialog_not_now_btn()

    def click_redact_btn(self):
        self.driver.click("redact_btn")

    def click_multi_redact_btn(self):
        self.driver.click("multi_redact_btn")

    def click_processing_pages_cancel_btn(self):
        self.driver.click("processing_pages_cancel_btn")

    def click_pic_item_thumbnail_view(self, index):
        self.driver.click("pic_item_thumbnail_view", format_specifier=[index])

    def right_click_pic_item_thumbnail_view(self, index):
        obj = self.driver.find_object("pic_item_thumbnail_view", format_specifier=[index])
        # width, height = obj.rect["width"], obj.rect["height"]
        self.driver.click_by_coordinates(obj, right_click=True)
    

    # ---------------- Scan Canceled dialog ---------------- #   
    def click_scan_canceled_x_btn(self):
        self.driver.click("scan_canceled_x_btn") 

    # ---------------- printer dialog ---------------- #   
    def click_print_dialog_cancel_btn(self):
        sleep(3)
        self.driver.click("print_dialog_cancel_btn") 

    def click_print_dialog_print_btn(self):
        self.driver.wait_for_object("print_dialog_print_btn", clickable=True, timeout=60).click()
        if self.driver.wait_for_object("hp_smart_printing_dialog", timeout=5, raise_e=False):
            self.driver.click("hp_smart_printing_dialog_close_btn")
            
    def click_hp_printing_print_btn(self):
        self.driver.click("hp_printing_print_btn") 

    # ---------------- Exit_without saving dialog ---------------- #   
    def click_yes_btn(self, advance=False):
        if not advance:
            self.driver.click("yes_btn")
        else:
            self.driver.click("scribble_yes_btn")

    def click_no_btn(self):
        self.driver.click("no_btn") 

    # ----------------  Error dialog ---------------- #   
    def click_close_btn(self):
        self.driver.click("no_btn") 

    # ----------------  Delete dialog ---------------- #   
    def click_delete_btn_on_dialog(self):
        self.driver.click("delete_title_delete_btn") 

    def click_cancel_btn_on_dialog(self):
        self.driver.click("delete_title_cancel_btn")

    def click_delete_image_btn(self):
        self.driver.click("delete_image_btn")

    # ----------------  Thumbnail view ---------------- #   
    def click_rotate_btn(self):
        self.driver.click("rotate_btn") 

    def click_select_all_btn(self):
        self.driver.wait_for_object("select_all_btn")
        self.driver.click("select_all_btn") 
        
    def click_delete_btn(self):
        self.driver.click("delete_btn") 

    # ---------------- save dialog ---------------- #   
    def click_save_dialog_save_btn(self):
        self.driver.click("save_dialog_save_btn") 

    def click_password_protection_toggle(self):
        self.driver.click("password_protection_toggle")

    def find_password_protection_opt(self):
        self.driver.swipe("password_protection_title") 

    def enter_password(self, password):
        self.driver.send_keys("password_textbox", password)

    def clear_password(self):
        self.driver.clear_text("password_textbox")

    def click_language_item(self, num):
        self.driver.click("language_item", format_specifier=[num])

    def click_dialog_cancel_btn(self):
        self.driver.click("dialog_cancel_btn")

    def click_language_dropdown_listitem(self):
        self.driver.click("language_dropdown_listitem")
        
    # ---------------- save as dialog (windows popup)---------------- #   
    def click_save_as_dialog_save_btn (self):
        self.driver.click("save_as_dialog_save_btn") 

    def get_the_saved_file_path(self):
        """
        get the saved file fath
        """
        return self.driver.get_attribute("file_saved_link", attribute="Name")

    def select_file_type_listitem(self, name):
        self.select_file_type_dropdown()
        self.verify_dropdown_listitem(name).click()

    # --------Are you enjoying the HP Smart app?---------- #   
    def click_are_you_dialog_yes_btn (self):
        self.driver.click("are_you_enjoy_yes_btn") 

    def click_are_you_dialog_not_now_btn(self):
        self.driver.click("are_you_enjoy_no_btn")

    # --------Sorry to hear that!---------- #   
    def click_sorry_to_dialog_yes_btn (self):
        self.driver.click("sorry_to_hear_yes_btn") 

    def click_sorry_to_dialog_not_now_btn(self):
        self.driver.click("sorry_to_hear_no_now_btn")

    # --------review for HP Smart---------- # 
    def click_the_star(self):
        el = self.driver.wait_for_object("rate_star")
        el.send_keys(Keys.DOWN, Keys.DOWN, Keys.UP)   

    def click_the_first_star(self, raise_e=True):
        return self.driver.click("rate_first_star", raise_e=raise_e)

    def click_the_five_star(self, raise_e=True):
        return self.driver.click("rate_five_star", raise_e=raise_e)

    def write_review(self):
        self.driver.send_keys("review_a_title", "good!") 
        sleep(2)
        self.driver.send_keys("share_your_experience","123") 

    def click_review_submit_btn(self):
        self.driver.click("review_submit_btn") 

    def click_review_done_btn(self):
        self.driver.click("review_done_btn") 

    def close_review_dialog(self):
        self.driver.click("review_close_btn")

    def close_thank_you_dialog(self):
        self.driver.click("review_thank_you_close_btn")

    def select_searchable_type(self):
        self.driver.click("file_type_Searchable_pdf")

    def select_file_type_dropdown(self):
        self.driver.click("file_type_dropdown")

    def select_compression_dropdown(self):
        self.driver.click("compression_dropdown")

    def click_save_text(self):
        self.driver.click("save_title")

    def click_install_new_language_btn(self):
        self.driver.click("install_language_btn")

    def click_install_btn(self):
        self.driver.click("install_btn")

    def click_back_arrow(self):
        self.driver.click("back_arrow")

    def input_file_name(self, file_name):
        self.driver.send_keys("file_name_combo_box_edit", file_name, press_enter=True)

    def click_save_as_yes_btn(self):
        self.driver.click("save_as_yes_btn")

    def click_smart_file_name_toggle(self, operate):
        if operate == "open":
            self.driver.check_box("smart_file_name_toggle")
        elif operate == "close":
            self.driver.check_box("smart_file_name_toggle", uncheck=True)
        else:
            raise ValueError("Operation error, please enter the correct operation value.")

    def click_shortcuts_item(self):
        self.driver.click("shortcuts_item")

    def click_shortcuts_order_for_email(self, raise_e=True):
        return self.driver.click("shortcuts_order_for_email", raise_e=raise_e)

    # ---------------- Select Language Title ---------------- #   
    def click_continue_btn(self):
        self.driver.click("continue_btn") 

    # ---------------- Text Edit ---------------- #   
    def click_copy_all_btn(self):
        self.driver.click("copy_all_btn") 

    def click_done_btn(self):
        self.driver.click("done_btn") 
        
    def click_extract_ok_btn(self):
        self.driver.click("extract_ok_btn") 

    def clear_text_extract_content(self):
        self.driver.clear_text("text_extract_edit")

    def click_extract_start_new_scan_btn(self):
        self.driver.click("extract_start_new_scan_btn") 

    def click_extract_cancel_btn(self):
        self.driver.click("extract_cancel_btn") 

    # ---------------- Place Your Mark ---------------- #   
    def click_back_btn(self):
        self.driver.click("back_btn") 

    # ---------------- Text was not detected ---------------- #   
    def click_save_ok_btn(self):
        self.driver.click("save_not_detected_OK_btn") 

    # ---------------- Edit screen ---------------- #   
    def click_edit_done_btn(self):
        self.driver.click("edit_done_btn") 

    def click_crop_letter_btn(self):
        self.driver.click("crop_letter_btn")

    def click_reset_crop_btn(self):
        self.driver.click("reset_crop_btn")

    def click_adjust_item(self):
        self.driver.click("adjust_item")

    def click_reset_adjust_btn(self):
        sleep(3)
        self.driver.click("reset_adjust_btn")

    def click_undo_btn(self):
        sleep(3)
        self.driver.click("undo_btn")

    def change_adjust_contrast_edit_vaule(self, value):
        self.driver.send_keys("adjust_contrast_edit", value, press_enter=True)
        self.click_adjust_item()

    def click_filters_item(self):
        self.driver.click("filters_item")

    def click_reset_filters_btn(self):
        self.driver.click("reset_filters_btn")

    def click_filters_bw_btn(self):
        self.driver.click("filters_bw_btn")

    def click_filters_summer_btn(self):
        self.driver.click("filters_summer_btn")

    def click_text_item(self):
        self.driver.click("text_item")

    def click_markup_item(self):
        self.driver.click("markup_item")

    def click_reset_markup_btn(self):
        self.driver.click("reset_markup_btn")

    def click_red_pen_btn(self):
        self.driver.click("red_pen_btn")

    def edit_crop_item(self):
        self.driver.click("crop_item")
        if self.verify_edit_crop_screen() is not False:
            self.driver.send_keys("crop_size_w", '2000', press_enter=True)
            sleep(1)
            self.driver.send_keys("crop_size_h", '3000', press_enter=True)
            sleep(1)
            self.click_crop_letter_btn()

    def edit_adjust_item(self):
        self.click_adjust_item()
        if self.verify_edit_adjust_screen() is not False:
            self.change_adjust_item_vaule("50")

    def edit_filters_item(self):
        self.click_filters_item()
        if self.verify_edit_filters_screen() is not False:
            self.driver.click("filters_letter_btn")

    def edit_text_item(self):
        self.click_text_item()
        if self.verify_edit_text_screen() is not False:
            self.driver.send_keys("text_line_spacing", '2.0', press_enter=True)

    def edit_markup_item(self):
        self.click_markup_item()
        if self.verify_edit_markup_screen() is not False:
            self.driver.send_keys("markup_size", '15', press_enter=True)

    def click_start_btn(self):
        self.driver.click("start_btn")

    def click_rotate_icon(self):
        self.driver.click("rotate_icon")

    def select_keep_resolution_box(self):
        self.driver.click("resolution_checkbox", displayed=False)

    # ---------------- Text Edit ---------------- #   
    def click_more_option_btn(self):
        self.driver.click("more_option_btn") 

    def click_activity_btn(self):
        self.driver.click("activity_btn") 
        
    def click_home_btn(self):
        self.driver.click("home_btn") 

    # ---------------- Scanning Unavailable ---------------- # 
    def click_return_home_btn(self):
        self.driver.click("return_home_btn")

    def click_get_more_help_btn(self):
        self.driver.click("get_more_help_btn")

    # ------------We're having trouble...-------------- #
    def click_ipp_try_again_button(self):
        self.driver.click("ipp_try_again_btn")

    def click_ipp_cancel_button(self):
        self.driver.click("ipp_cancel_btn")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_scan_intro_page(self, is_remote_printer=False, timeout=30):
        # Test these locators, won't use these much identifier
        self.driver.wait_for_object("auto_enhancement_title", timeout=timeout)
        self.driver.wait_for_object("auto_enhancement_get_started_btn")
        if not is_remote_printer:
            self.driver.wait_for_object("start_scan_text")
            self.driver.wait_for_object("preview_btn")
            self.verify_scan_btn()
            
    def verify_scan_btn(self, timeout=10):
        return self.driver.wait_for_object("scan_btn", timeout=timeout)

    def verify_new_scan_auto_enhancements_dialog(self, raise_e=True, timeout=30):
        """
        Verify the current screen is New Scan Auto-Enhancements dialog.
        """
        return self.driver.wait_for_object("auto_enhancement_title", raise_e=raise_e, timeout=timeout)

    def verify_auto_enhancement_icon_display(self, raise_e=True):
        """
        Verify the auto enhancement icon display
        """
        return self.driver.wait_for_object("auto_enhancement_icon", raise_e=raise_e)

    def verify_scanner_screen(self, raise_e=True):
        """
        Verify the current screen is Scanner screen.
        """
        return self.driver.wait_for_object("scan_btn", raise_e=raise_e)

    def verify_all_the_button_on_preview(self):
        """
        Verify all the button on Preview screen.
        """
        self.driver.wait_for_object("print_btn")

    def verify_source_dropdown(self):
        """
        Verify the source dropdown display
        """
        return self.driver.wait_for_object("source_dropdown")

    def verify_rotate_button_display(self):
        """
        Verify Rotate button on Preview screen
        """
        return self.driver.wait_for_object("rotate_icon")

    def verify_resolution_dropdown(self):
        """
        Verify the resolution dropdown display
        """
        return self.driver.wait_for_object("resolution_dropdown")

    def verify_presets_dropdown(self):
        """
        Verify the presets dropdown display
        """
        return self.driver.wait_for_object("presets_dropdown")

    def verify_output_dropdown(self):
        """
        Verify the output dropdown display
        """
        return self.driver.wait_for_object("output_dropdown")

    def verify_dropdown_listitem(self, name, raise_e=True):
        return self.driver.wait_for_object("dynamic_listitem", format_specifier=[name], raise_e=raise_e)

    def verify_auto_enhancement_panel_setting_by_default(self):
        """
        Verify both "Auto-Enhancement" toggle is 'on' and "Auto-Orientation" toggle is 'off' by default.
        """
        self.driver.wait_for_object("auto_enhancements_text")
        self.driver.wait_for_object("auto_orientation_text")
        toggle_1 = self.driver.wait_for_object("auto_enhancements_toggle")
        toggle_2 = self.driver.wait_for_object("auto_orientation_toggle")
        assert toggle_1.get_attribute("Toggle.ToggleState") == "1"
        assert toggle_2.get_attribute("Toggle.ToggleState") == "0"

        if self.driver.wait_for_object("auto_heal_text", raise_e=False):
            toggle_3 = self.driver.wait_for_object("auto_heal_toggle")
            assert toggle_3.get_attribute("Toggle.ToggleState") == "1"
            return toggle_3
              
    def verify_auto_enhancement_is_off(self):
        """
        Verify "Auto-Enhancement" toggle is 'off'
        """
        toggle_1 = self.driver.wait_for_object("auto_enhancements_toggle")
        assert toggle_1.get_attribute("Toggle.ToggleState") == "0"

    def verify_auto_heal_is_off(self):
        """
        Verify "Auto-Heal" toggle is 'off'
        """
        if self.driver.wait_for_object("auto_heal_text", raise_e=False):
            toggle_1 = self.driver.wait_for_object("auto_heal_toggle")
            assert toggle_1.get_attribute("Toggle.ToggleState") == "0"

    def verify_auto_orientation_is_on(self):
        """
        Verify "Auto-Orientation" toggle is 'on'
        """
        toggle_1 = self.driver.wait_for_object("auto_orientation_toggle")
        assert toggle_1.get_attribute("Toggle.ToggleState") == "1"

    def verify_auto_enhancement_is_on(self):
        """
        Verify "Auto-Enhancement" toggle is 'on'
        """
        toggle_1 = self.driver.wait_for_object("auto_enhancements_toggle")
        assert toggle_1.get_attribute("Toggle.ToggleState") == "1"

    def verify_auto_heal_is_on(self):
        """
        Verify "Auto-Heal" toggle is 'on'
        """
        toggle_1 = self.driver.wait_for_object("auto_heal_toggle")
        assert toggle_1.get_attribute("Toggle.ToggleState") == "1"

    def verify_2_sided_box_is_off(self):
        """
        Verify 2-Sided is 'off'
        """
        toggle= self.driver.wait_for_object("2_sided_box")
        assert toggle.get_attribute("Toggle.ToggleState") == "0"

    def verify_keep_resolution_box_behavior(self, behavior):
        """
        Verify keep resolution box behavior
        """
        toggle = self.driver.wait_for_object("keep_resolution_box", displayed=False)
        if behavior == "unchecked":
            assert toggle.get_attribute("Toggle.ToggleState") == "0"
        elif behavior == "checked":
            assert toggle.get_attribute("Toggle.ToggleState") == "1"
  
    def verify_scanner_preview_screen(self):
        """
        Verify the Scanner preview screen after clicking Preview btn on scanner screen
        """
        self.driver.wait_for_object("scanner_preview_image", timeout=30)

    def verify_import_dialog(self):
        """
        Verify dialog "Import,edit,and share" displayed 
        """
        self.driver.wait_for_object("import_dialog_title")
        self.driver.wait_for_object("import_dialog_text")

    def crop_setting_value_item(self, name):
        return self.driver.wait_for_object("crop_setting_value_item", format_specifier=[name])

    def verify_no_content_gird_error_message_image(self, raise_e=True):
        return self.driver.wait_for_object("no_content_gird_error_message_image", raise_e=raise_e, timeout=120)

    def verify_no_content_gird_error_message_header(self, raise_e=True):
        return self.driver.wait_for_object("no_content_gird_error_message_header", raise_e=raise_e)

    def verify_no_content_gird_error_message_header_body(self, raise_e=True):
        return self.driver.wait_for_object("no_content_gird_error_message_header_body", raise_e=raise_e)

    def verify_return_home_btn(self, raise_e=True):
        return self.driver.wait_for_object("return_home_btn", raise_e=raise_e)  

    def verify_get_more_help_btn(self, raise_e=True):
        return self.driver.wait_for_object("get_more_help_btn", raise_e=raise_e)

    def verify_no_content_gird_error_message_footer_body(self, raise_e=True):
        return self.driver.wait_for_object("no_content_gird_error_message_footer_body", raise_e=raise_e)

    def verify_scanning_unavailable_screen(self):
        self.verify_no_content_gird_error_message_image()
        self.verify_no_content_gird_error_message_header()
        self.verify_return_home_btn()
        self.verify_get_more_help_btn()

    def verify_couldnt_connect_to_scanner_screen(self):
        """
        Verify Couldn't Connect to Scanner screen after clicking Scan tile with a remote printer.
        """
        self.verify_no_content_gird_error_message_image()
        assert self.verify_no_content_gird_error_message_header().text == self.get_text_from_str_id("couldnt_connect_to_scanner_header")
        assert self.verify_no_content_gird_error_message_header_body().text == self.get_text_from_str_id("couldnt_connect_to_scanner_header_body").replace("<Bold>", "").replace("</Bold>", "")
        assert self.verify_return_home_btn().text == self.get_text_from_str_id("return_home_btn")
        assert self.verify_get_more_help_btn().text == self.get_text_from_str_id("get_more_help_btn")
        assert self.verify_no_content_gird_error_message_footer_body().text == self.get_text_from_str_id("couldnt_connect_to_scanner_footer_body").replace("<Bold>", "").replace("</Bold>", "")

    def verify_scan_canceled_dialog(self, raise_e=True):
        """
        Verify the current screen is scan canceled dialog
        """
        return self.driver.wait_for_object("scan_canceled_title", raise_e=raise_e)

    def verify_scan_result_screen(self, timeout=30, raise_e=True):
        """
        Verify the current screen is scan result
        """
        return self.driver.wait_for_object("add_pages_btn", timeout=timeout, raise_e=raise_e)

    def verify_pro_scan_result_screen(self, timeout=30, raise_e=True):
        """
        Verify the current screen is scan result for pro account
        """
        return self.driver.wait_for_object("redact_btn", timeout=timeout, raise_e=raise_e)

    def verify_processing_scan_dialog(self, timeout=30, raise_e=True):
        """
        Verify the current screen is Processing Scan dialog
        """
        return self.driver.wait_for_object("processing_scan_cancel_btn", timeout=timeout, raise_e=raise_e)

    def verify_print_dialog(self, timeout=30, raise_e=True):
        """
        Verify the current screen is Print dialog
        """
        return self.driver.wait_for_object("print_dialog_cancel_btn", timeout=timeout, raise_e=raise_e)

    def verify_shortcuts_dialog(self, timeout=60, raise_e=True):
        """
        Verify the current screen is Shortcuts dialog
        """
        return self.driver.wait_for_object("shortcuts_title", timeout=timeout, raise_e=raise_e)

    def verify_shortcuts_item_displays(self):
        """
        Verify the current screen is Shortcuts dialog
        """
        self.driver.wait_for_object("shortcuts_item")
        self.driver.wait_for_object("i_icon")

    def verify_shortcuts_dialog_disappear(self):
        """
        Verify Shortcuts dialog disappear
        """
        assert self.driver.wait_for_object("shortcuts_title", raise_e=False) == False
 
    def verify_save_dialog(self, timeout=3):
        """
        Verify the current screen is Save dialog
        """
        self.driver.wait_for_object("save_title", timeout=timeout)
        assert self.driver.get_attribute("save_title", attribute="Name") =="Save"

    def verify_share_dialog(self):
        """
        Verify the current screen is Share dialog
        """
        assert self.driver.get_attribute("save_title", attribute="Name") =="Share"

    def verify_file_name_text_box_not_empty(self):
        """
        Verify File Name is Not empty
        """
        assert self.driver.get_attribute("filename_edit", attribute="Value.Value") != None

    def get_current_file_name(self):
        """
        Get current File Name 
        """
        file_name = self.driver.get_attribute("filename_edit", attribute="Value.Value")
        return file_name

    def verify_import_screen(self):
        """
        Verify the current screen is Detect Edges
        """
        self.driver.wait_for_object("import_apply_btn", timeout=30)
        self.driver.wait_for_object("auto_text")
        self.driver.wait_for_object("full_text")
       
    def verify_exit_without_saving_dialog(self, raise_e=True):
        """
        Verify the current screen is Exit without saving dialog
        """
        return self.driver.wait_for_object("exit_without_saving_text", raise_e=raise_e) and \
        self.driver.wait_for_object("exit_without_saving_title", raise_e=raise_e) and \
        self.driver.wait_for_object("yes_btn", raise_e=raise_e) and \
        self.driver.wait_for_object("no_btn", raise_e=raise_e)


    def verify_file_format_error_dialog(self):
        """
        Verify the current screen is File Format Error dialog
        """
        assert self.driver.get_attribute("error_title", attribute="Name") =="File Format Error"

    def verify_large_file_error_dialog(self):
        """
        Verify the current screen is The file could not be opened dialog
        """
        assert self.driver.get_attribute("error_title", timeout=10, attribute="Name") =="The file could not be opened."

    def verify_multi_pages_scan_result_screen(self, timeout=30, raise_e=True):
        """
        Verify the current screen is scan result
        """
        return self.driver.wait_for_object("multi_add_pages_btn", timeout=timeout, raise_e=raise_e)

    def verify_delete_dialog(self, timeout=10, raise_e=True):
        """
        Verify the current screen is Delete dialog
        """
        return self.driver.wait_for_object("delete_title", timeout=timeout, raise_e=raise_e)

    def verify_thumbnail_view_screen_displays(self , is_pro_account=False):
        """
        Verify the current screen is thumbnail view 
        """
        if is_pro_account:
            self.driver.wait_for_object("thumbnail_redact_btn")
        self.driver.wait_for_object("rotate_btn")
        self.driver.wait_for_object("thumbnail_add_btn")

    def verify_all_the_button_can_be_used(self):
        """
        Verify that all features are in normal use
        """
        assert self.driver.get_attribute("delete_btn", attribute="IsEnabled").lower() =="true"
        assert self.driver.get_attribute("rotate_right_btn", attribute="IsEnabled").lower() =="true"
        assert self.driver.get_attribute("rotate_left_btn", attribute="IsEnabled").lower() =="true"

    def verify_file_has_been_saved_dialog(self):
        """
        Verify Your file has been saved
        """
        self.driver.wait_for_object("file_has_been_saved_text")
        self.driver.wait_for_object("file_saved_link")

    def verify_are_you_enjoying_dialog(self, raise_e=True):
        """
        Verify "Are you enjoying the HP Smart app?" dialog
        """
        return self.driver.wait_for_object("are_you_enjoy_text", raise_e=raise_e) and \
        self.driver.wait_for_object("are_you_enjoy_yes_btn", raise_e=raise_e) and \
        self.driver.wait_for_object("are_you_enjoy_no_btn", raise_e=raise_e)

    def verify_are_you_enjoying_dialog_disappear(self, raise_e=False):
        """
        Verify "Are you enjoying the HP Smart app?" dialog disappear
        """
        assert self.driver.wait_for_object("are_you_enjoy_no_btn", raise_e=raise_e) == False

    def verify_sorry_to_hear_dialog(self):
        """
        Verify "Sorry to hear that!" dialog
        """
        self.driver.wait_for_object("sorry_to_hear_no_now_btn")
        self.driver.wait_for_object("sorry_to_hear_yes_btn")

    def verify_sorry_to_hear_dialog_disappear(self, raise_e=False):
        """
        Verify "Sorry to hear that!" dialog disappear
        """
        assert self.driver.wait_for_object("sorry_to_hear_no_now_btn", raise_e=raise_e) == False

    def verify_write_review_dialog(self, raise_e=True):
        """
        Verify "review for HP Smart" dialog
        """ 
        return self.driver.wait_for_object("review_a_title", timeout=25, raise_e=raise_e) and \
        self.driver.wait_for_object("share_your_experience", timeout=25, raise_e=raise_e) and \
        self.driver.wait_for_object("review_submit_btn", raise_e=raise_e) and \
        self.driver.wait_for_object("review_close_btn", raise_e=raise_e)

    def verify_review_thank_you_dialog(self, raise_e=True):
        """
        Verify "review for HP Smart" dialog
        """
        return self.driver.wait_for_object("review_done_btn", timeout=25, raise_e=raise_e)  and \
        self.driver.wait_for_object("review_close_btn", raise_e=raise_e)

    def verify_review_dialog_disappear(self, raise_e=False):
        """
        Verify "review for HP Smart" dialog disappear
        """
        assert self.driver.wait_for_object("review_dialog", timeout=25, raise_e=raise_e) == False

    def verify_id_card_message_display(self):
        """
        Verify ID Card message shows with front Card ID graphic.
        """
        self.driver.wait_for_object("id_card_title_text")
        self.driver.wait_for_object("id_card_text")
        self.driver.wait_for_object("id_card_front_image")

    def verify_another_scanner_screen(self):
        """
        Verify "Place the back of the ID Card on the scanner and select Scan" shows with 
        back Card ID graphic in another scanner screen 
        """
        self.driver.wait_for_object("id_card_back_image", timeout=30)
        self.driver.wait_for_object("skip_btn")
        self.driver.wait_for_object("scan_btn")
        
    def verify_id_card_front_screen(self):
        """
        Verify the current screen is ID Card Front screen
        """
        self.driver.wait_for_object("multi_scan_btn", timeout=30)
        assert self.driver.get_attribute("title_text", attribute="Name") =="ID Card Front"
   
    def verify_id_card_back_screen(self):
        """
        Verify the current screen is ID Card Back screen
        """
        self.driver.wait_for_object("multi_scan_btn", timeout=30)
        assert self.driver.get_attribute("title_text", attribute="Name") =="ID Card Back"

    def verify_scribble_scan_result_screen(self, timeout=60, raise_e=True):
        """
        Verify the current screen is scribble scan result
        """
        return self.driver.wait_for_object("scribble_btn", timeout=timeout, raise_e=raise_e)

    def verify_multi_scribble_scan_result_screen(self, timeout=30, raise_e=True):
        """
        Verify the current screen is scribble scan result
        """
        return self.driver.wait_for_object("multi_scribble_btn", timeout=timeout, raise_e=raise_e)

    def verify_book_message_display(self):
        """
        Verify Book message shows with scanner
        """
        self.driver.wait_for_object("book_title_text")
        self.driver.wait_for_object("book_text")
        self.driver.wait_for_object("book_image")

    def verify_multi_item_message_display(self):
        """
        Verify Multi Item message shows with scanner
        """
        self.driver.wait_for_object("multi_title_text")
        self.driver.wait_for_object("multi_text")
        self.driver.wait_for_object("multi_image")

    def verify_install_language_dialog(self):
        """
        Verify the current screen is Select Language to Install dialog 
        """
        assert self.driver.get_attribute("text_title", attribute="Name") =="Select Language to Install"
        self.driver.wait_for_object("install_btn")

    def verify_the_saved_file_name_is_correct(self, file_name):
        """
        Verify The saved file name is correct
        """
        file_path = self.driver.get_attribute("file_saved_link", attribute="Name")
        name_value = file_path.split("\\")[-1].split(".")[0]
        assert file_name == name_value
        return file_path

    def verify_select_language_dialog(self, raise_e=True, timeout=60):
        """
        Verify the current screen is Select Language dialog
        """
        return self.driver.wait_for_object("select_language_title", raise_e=raise_e)

    def verify_extracting_text_dialog(self, raise_e=True):
        """
        Verify the current screen is Extracting text dialog
        """
        return self.driver.wait_for_object("extracting_text_title", raise_e=raise_e)

    def verify_text_edit_screen(self):
        """
        Verify the current screen is Text Edit screen
        """ 
        self.driver.wait_for_object("copy_all_btn")
        self.driver.wait_for_object("done_btn")

    def verify_extract_are_you_sure_screen(self):
        """
        Verify the current screen is Text Edit screen
        """ 
        self.driver.wait_for_object("extract_start_new_scan_btn")
        self.driver.wait_for_object("extract_restore_text_btn")

    def verify_copie_text_message(self):
        """
        Verify the copie text message
        """
        self.driver.wait_for_object("copie_text", timeout=15)
        # assert self.driver.get_attribute("copie_text", attribute="Name") == "Text Copied to Clipboard"

    def verify_place_your_mark_screen(self):
        """
        Verify the current screen is Place Your Mark
        """
        self.driver.wait_for_object("place_your_mark_text")

    def verify_new_mark_screen(self):
        """
        Verify the current screen is New Mark
        """
        self.driver.wait_for_object("add_a_new_mark_text")
        self.driver.wait_for_object("new_mark_cancel_btn")
        self.driver.wait_for_object("new_mark_done_btn")

    def verify_mark_text_exist(self):
        """
        Verify the 'Place Your Mark' screen exists mark
        """
        return self.driver.wait_for_object("mark_text", raise_e=False)
        
    def verify_text_not_detected_dialog(self, raise_e=True):
        """
        Verify the current screen is Text was not detected dialog.
        """
        return self.driver.wait_for_object("not_detected_text_title", raise_e=raise_e)

    def verify_save_text_not_detected_dialog(self, raise_e=False):
        """
        login Pro account 
        Preview -> Save -> Smart File Name.
        """
        return self.driver.wait_for_object("save_not_detected_title", raise_e=raise_e)

    def verify_edit_screen(self):
        """
        Verify the current screen is Edit screen
        """
        self.driver.wait_for_object("reset_crop_btn")
        self.driver.wait_for_object("cancel_btn")   
        self.driver.wait_for_object("done_btn")

    def verify_edit_crop_screen(self, raise_e=False):
        """
        Preview screen: three blue dots -> Edit -> Edit screen
        """
        return self.driver.wait_for_object("crop_size_w", raise_e=raise_e)

    def verify_edit_adjust_screen(self, raise_e=False):
        """
        Preview screen: three blue dots -> Edit -> Edit screen
        """
        return self.driver.wait_for_object("adjust_contrast_edit", raise_e=raise_e)

    def verify_edit_filters_screen(self):
        """
        Preview screen: three blue dots -> Edit -> Edit screen
        """
        self.driver.wait_for_object("filters_document_text")
        self.driver.wait_for_object("filters_photo_text")
        self.driver.wait_for_object("reset_filters_btn")

    def verify_edit_text_screen(self, raise_e=False):
        """
        Preview screen: three blue dots -> Edit -> Edit screen
        """
        return self.driver.wait_for_object("text_line_spacing", raise_e=raise_e)   

    def verify_edit_markup_screen(self, raise_e=False):
        """
        Preview screen: three blue dots -> Edit -> Edit screen
        """
        return self.driver.wait_for_object("markup_size", raise_e=raise_e)   

    def verify_replace_screen(self):
        """
        Verify the current screen is Replace screen
        """
        self.driver.wait_for_object("replace_text", timeout=20)

    def verify_start_btn(self):
        """
        Verify shortcuts start button on scan flow
        """
        self.driver.wait_for_object("start_btn", timeout=30)

    def verify_hp_smart_printing_dialog(self, timeout=30, raise_e=True):
        """
        Verify the current screen is Hp Smart Printing dialog
        """
        return self.driver.wait_for_object("hp_printing_print_btn", timeout=timeout, raise_e=raise_e)

    def verify_your_shortcut_dialog(self):
        """
        Verify the current screen is Your Shortcut is on its way! dialog
        """
        self.driver.wait_for_object("more_option_btn", timeout=60)
        self.driver.wait_for_object("activity_btn")
        self.driver.wait_for_object("home_btn")

    def verify_continue_to_fax_btn_display(self, timeout=30, raise_e=True):
        """
        Verify the Continue to Fax Button display
        """
        return self.driver.wait_for_object("continue_to_fax_btn", timeout=timeout, raise_e=raise_e)

    def verify_thumbnail_icon_is_hidden(self):
        """
        Verify Thumbnail icon is hidden when only 1 scan result.
        """
        assert self.driver.wait_for_object("thumbnail_view_icon", raise_e=False) is False

    def verify_left_arrow_btn_display(self):
        """
        Verify left arrow button display
        """
        self.driver.wait_for_object("left_arrow_btn")

    def verify_right_arrow_btn_display(self):
        """
        Verify right arrow button display
        """
        self.driver.wait_for_object("righ_arrow_btn")

    def verify_pages_num_value(self, name=None):
        """
        Verify the message under the result files are now "x of y". (x is equal and less than y)
        """
        vaule = self.driver.get_attribute("pages_num", attribute="Name")
        vaule_1 =vaule.split(" of ")[0]
        vaule_2 =vaule.split(" of ")[1]
        assert vaule_1 <= vaule_2
        if name:
            assert vaule == name

    def verify_file_type(self, file_type):
        """
        Verify the JPG is selected as default file type if the files are recognized as photo.
        Verify the PDF is selected as default file type if the files are recognized as document.
        @param file_type:
            - jpg
            - pdf
        """
        name = self.driver.get_attribute("filename_edit", attribute="Value.Value")
        type = name.split("_")[0]
        if file_type == "jpg":
            assert type == "Photo"
            self.driver.get_attribute("file_type_dropdown", attribute="Selection.Selection") == "\"Image(*.jpg)\" list item"

        if file_type == "pdf":
            assert type != "Photo"
            self.driver.get_attribute("file_type_dropdown", attribute="Selection.Selection") == "\"Basic PDF\" list item"
    
    def verify_smart_file_name_toggle_is_hidden(self):
        """
        Verify Smart File Name icon is hidden.
        """
        assert self.driver.wait_for_object("smart_file_name_toggle", raise_e=False) is False

    def verify_id_card_replace_screen(self):
        """
        Verify the current screen is Replace screen for id card
        """
        self.driver.wait_for_object("replace_scan_btn", timeout=30)

    def verify_smart_file_name_toggle_is_off_by_default(self):
        """
        Verify "Smart File Name" option is Off by default.
        """
        toggle = self.driver.wait_for_object("smart_file_name_toggle")
        assert toggle.get_attribute("Toggle.ToggleState") == "0"

    def verify_smart_file_name_toggle_is_on(self):
        """
        Verify "Smart File Name" option is ON.
        """
        toggle = self.driver.wait_for_object("smart_file_name_toggle")
        assert toggle.get_attribute("Toggle.ToggleState") == "1"

    def verify_reset_settings_btn(self, enable=True):
        """
        Verify reset_settings button status
        """
        button = self.driver.wait_for_object("reset_settings_btn")
        if enable:
            assert button.get_attribute("IsEnabled").lower() == "true"
        else:
            assert button.get_attribute("IsEnabled").lower() == "false"
    
    def verify_resolution_tooltip(self, raise_e=True):
        return self.driver.wait_for_object("resolution_tooltip", raise_e=raise_e)

    def verify_id_card_front_replace_screen(self, raise_e=True):
        return self.driver.wait_for_object("id_card_front_replace_image", timeout=20)

    def verify_id_card_back_replace_screen(self, raise_e=True):
        return self.driver.wait_for_object("id_card_back_replace_image", timeout=60)

    def verify_resolution_info_less_than_300dpi_msg(self, raise_e=True):
        return self.driver.wait_for_object("resolution_info", raise_e=raise_e)

    def verify_number_icon_shows(self, num):
        """
        Verify number icon shows
        Verify number match to the scanned pages
        """
        self.driver.wait_for_object("number_icon")
        assert self.driver.get_attribute("number_icon", attribute="Name") == num

    def verify_flatten_btn_shows(self, raise_e=True):
        return self.driver.wait_for_object("detect_edges_flatten_text", raise_e=raise_e)

    def verify_start_test_tab_not_display(self):
        if self.driver.wait_for_object("start_icon", raise_e=False):
            raise NoSuchElementException("Shortcuts landing page display")
        return True

    def verify_print_btn_not_display(self):
        if self.driver.wait_for_object("print_btn", raise_e=False):
            raise NoSuchElementException("print button is available")
        return True

    def verify_problem_shortcut_dialog(self, print_destination_only=True):
        """
        Verify the current screen is There was a problem running your Shortcut dialog
        """
        self.driver.wait_for_object("problem_shortcut_dialog_title")
        self.driver.wait_for_object("dialog_cancel_btn")
        if print_destination_only:
            self.driver.wait_for_object("problem_shortcut_dialog_text_1")
        else:
            self.driver.wait_for_object("problem_shortcut_dialog_text_2")
            self.driver.wait_for_object("dialog_skip_printing_btn")

    def verify_password_protection_toggle_status(self, by_default=True):
        """
        Verify "password protection" option is ON or OFF
        """
        toggle = self.driver.wait_for_object("password_protection_toggle")
        if by_default:
            assert toggle.get_attribute("Toggle.ToggleState") == "0"
        else:
            assert toggle.get_attribute("Toggle.ToggleState") == "1"
    
    def verify_password_protection_not_display(self):
        if self.driver.wait_for_object("password_protection_title", raise_e=False):
            raise NoSuchElementException("password protection is available")
        return True
    
    def verify_password_space_error_shows(self, raise_e=True):
        return self.driver.wait_for_object("password_space_error", raise_e=raise_e)

    def verify_password_tooshort_error_shows(self, raise_e=True):
        return self.driver.wait_for_object("password_tooshort_error", raise_e=raise_e)

    def verify_password_toolong_error_shows(self, raise_e=True):
        return self.driver.wait_for_object("password_toolong_error", raise_e=raise_e)

    def verify_password_tooshortwithspace_error_shows(self, raise_e=True):
        return self.driver.wait_for_object("password_tooshortwithspace_error", raise_e=raise_e)

    def verify_password_toolongwithspace_error_shows(self, raise_e=True):
        return self.driver.wait_for_object("password_toolongwithspace_error", raise_e=raise_e)

    def verify_password_textbox_shows(self):
        self.driver.swipe("password_textbox")
        # return self.driver.wait_for_object("password_textbox", raise_e=raise_e)

    def verify_document_language_by_default(self):
        assert self.driver.get_attribute("language_dropdown_first_pot", "Name") == "English (US)"

    def verify_downloading_language_dialog(self):
        self.driver.wait_for_object("downloading_language_dialog_title")

    def verify_doc_language_text_not_display(self):
        if self.driver.wait_for_object("doc_language_text", raise_e=False):
            raise NoSuchElementException("Document Language option does show")
        return True

    def verify_smart_file_name_text_not_display(self):
        if self.driver.wait_for_object("smart_file_name", raise_e=False):
            raise NoSuchElementException("Smart File Name does show")
        return True

    def verify_redaction_webview_screen(self):
        self.driver.wait_for_object("redaction_text")

    def verify_processing_pages_dialog(self):
        self.driver.wait_for_object("processing_pages_title")

    def verify_adjust_contrast_edit_default_value(self):
        assert self.driver.get_attribute("adjust_contrast_edit", attribute="Value.Value") == "0"

    def verify_adjust_setting_default_value(self):
        assert self.driver.get_attribute("adjust_brigthtness_edit", attribute="Value.Value") == "0"
        assert self.driver.get_attribute("adjust_saturation_edit", attribute="Value.Value") == "0"
        self.verify_adjust_contrast_edit_default_value()
        assert self.driver.get_attribute("adjust_clarity_edit", attribute="Value.Value") == "0"
        assert self.driver.get_attribute("adjust_exposure_edit", attribute="Value.Value") == "0"
        assert self.driver.get_attribute("adjust_shadows_edit", attribute="Value.Value") == "0"
        assert self.driver.get_attribute("adjust_highlights_edit", attribute="Value.Value") == "0"
        assert self.driver.get_attribute("adjust_whites_edit", attribute="Value.Value") == "0"

    def verify_filter_intensity_value_is_100(self):
        assert self.driver.get_attribute("filter_intensity_edit", attribute="Value.Value") == "100"

    def verify_filter_intensity_value_is_50(self):
        assert self.driver.get_attribute("filter_intensity_edit", attribute="Value.Value") == "50"

    def verify_slider_adjected_to_100_for_doc_value(self):
        self.click_filters_bw_btn()
        self.verify_filter_intensity_value_is_100()

    def verify_slider_adjected_to_50_for_photo_value(self):
        self.click_filters_summer_btn()
        self.verify_filter_intensity_value_is_50()
    
    def verify_filter_intensity_does_not_show(self):
        if self.driver.wait_for_object("filter_intensity_text", displayed=False, raise_e=False):
            raise NoSuchElementException("Filter Intensity displays")
        return True

    def verify_edit_text_setting_screen(self):
        self.driver.wait_for_object("font_family_text", displayed=False)
        self.driver.wait_for_object("font_size_text", displayed=False)
        self.driver.wait_for_object("alignment_text", displayed=False)
        self.driver.wait_for_object("font_color_text", displayed=False)
        self.driver.wait_for_object("background_color_text", displayed=False)
        self.driver.wait_for_object("line_spacing_text", displayed=False)
        assert self.driver.get_attribute("font_size_edit", attribute="Value.Value") == "254"
        assert self.driver.get_attribute("text_line_spacing", attribute="Value.Value") == "1.0"

    def verify_edit_makup_setting_screen(self):
        self.driver.wait_for_object("highlight_btn")
        self.driver.wait_for_object("white_out_btn")
        self.driver.wait_for_object("black_pen_btn")
        self.driver.wait_for_object("blue_pen_btn")
        self.driver.wait_for_object("red_pen_btn")
        self.driver.wait_for_object("reset_markup_btn")
        assert self.driver.get_attribute("markup_size", attribute="Value.Value") == "8"

    def verify_scanner_not_found_dialog(self):
        self.driver.wait_for_object("return_home_btn" , timeout=60)
        self.driver.wait_for_object("get_more_help_btn")
        assert self.driver.get_attribute("scan_canceled_title", attribute="Name") == 'Scanner Not Found'

    def verify_scanner_problem_dialog(self):
        self.driver.wait_for_object("return_home_btn" , timeout=60)
        self.driver.wait_for_object("get_more_help_btn")
        assert self.driver.get_attribute("scan_canceled_title", attribute="Name") == 'Scanner Problem'
    
    def verify_thumbnail_view_images_display(self):
        self.driver.wait_for_object("thumbnail_view_images")

    def verify_mobile_fax_btn_does_not_show(self):
        if self.driver.wait_for_object("fax_btn", raise_e=False):
            raise NoSuchElementException("Mobile Fax button displays")
        return True

    def verify_shortcuts_btn_does_not_show(self):
        if self.driver.wait_for_object("shortcuts_btn", raise_e=False):
            raise NoSuchElementException("Shortcuts button displays")
        return True

    def verify_shortcuts_order(self, name_1, name_2):
        """
        Check shortcuts name order
        """
        assert self.driver.get_attribute("shortcuts_order_1", attribute="Name") == "Start "+ name_2
        assert self.driver.get_attribute("shortcuts_order_2", attribute="Name") == "Start "+ name_1

    def verify_2_sided_box_displays(self, raise_e=True):
        """
        Verify the 2-sided Box on scanner screen
        """
        return self.driver.wait_for_object("2_sided_box", raise_e=raise_e)

    def verify_camera_tab_not_display(self):
        assert self.driver.wait_for_object("camera_text", raise_e=False) is False

    def verify_exit_without_saving_dialog_for_edit_screen(self):
        """
        Verify the current screen is Exit without saving dialog in Edit screen
        """
        self.driver.wait_for_object("exit_without_saving_title")
        self.driver.wait_for_object("edit_screen_exit_without_saving_text", displayed=False)
        self.driver.wait_for_object("yes_btn")
        self.driver.wait_for_object("no_btn")

    # ------------We're having trouble...-------------- #
    def verify_we_are_having_trouble_dialog(self, timeout=60):
        self.driver.wait_for_object("ipp_we_are_having_text", timeout=timeout)
        self.driver.wait_for_object("ipp_try_again_btn", timeout=timeout)
        self.driver.wait_for_object("ipp_cancel_btn", timeout=timeout)
        