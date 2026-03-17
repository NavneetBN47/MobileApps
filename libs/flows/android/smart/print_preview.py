from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import time

class PrintPreview(SmartFlow):
    flow_name = "print_preview"

    # Page Range Options
    ALL_PAGE_OPTION = "all_page_option"
    SPECIFIC_RANGE_PAGE_OPTION = "specific_range_page_option"

    #2 sided Options
    TWO_SIDED_LONG_EDGE_OPTION = "2_sided_long_edge_option"
    TWO_SIDED_SHORT_EDGE_OPTION = "2_sided_short_edge_option"
    ONE_SIDED_OPTION = "1_sided_option"

    # Color Mode Options
    BLACK_WHITE_OPTION = "black_white_option"
    COLOR_OPTION = "color_option"

    # Paper Size Options
    PAPER_SIZE_5x7 = "paper_size_5x7"
    PAPER_SIZE_4x6 = "paper_size_4x6"
    PAPER_SIZE_LETTER = "paper_size_letter"
    PAPER_SIZE_A4 = "paper_size_a4"
    PAPER_SIZE_LEGAL = "paper_size_legal"

    # Orientation Options
    ORIENTATION_AUTO_OPTION = "orientation_auto_option"
    ORIENTATION_LANDSCAPE_OPTION = "orientation_landscape_option"
    ORIENTATION_PORTRAIT_OPTION = "orientation_portrait_option"

    # Quality Options
    QUALITY_AUTO_OPTION = "automatic_option"
    QUALITY_DRAFT_OPTION = "draft_option"
    QUALITY_NORMAL_OPTION = "normal_option"
    QUALITY_BEST_OPTION = "best_option"

    # SCALING Options
    SCALING_FIT_OPTION = "scaling_fit_option"
    SCALING_FILL_OPTION = "scaling_fill_option"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_print_btn(self):
        """
        Click on Print button on Print Preview screen
        """
        self.driver.click("print_btn", change_check={"wait_obj": "print_btn", "invisible": True},delay=3)

    def select_share_btn(self):
        """
        Click on Share button on Print Preview screen
        """
        self.driver.click("share_btn")

    def select_print_job_list_btn(self):
        """
        Click on Print Jobs button on Print Preview screen
        """
        self.driver.click("print_job_list_btn", change_check={"wait_obj": "print_job_list_btn", "invisible": True})

    def verify_print_preview_ui(self):
        """
        verify on Print ui
        """
        self.driver.wait_for_object("print_job_list_btn")
        self.driver.wait_for_object("copies_minus_btn")

    def verify_doument_options(self):
        """
        verify document options on Print Preview screen
        """
        self.driver.wait_for_object("quality_item")
        self.driver.wait_for_object("scaling_item")

    def click_on_fax(self, btn):
        """
        click on fax button
        """
        self.driver.click(btn)

    def verify_fax_page(self):
        """
        verify fax page
        """
        self.driver.wait_for_object("continue_to_fax_text")

    def verify_shortcuts_page(self):
        """
        verify shortcut page
        """
        self.driver.wait_for_object("shortcuts_image")
        self.driver.wait_for_object("shortcuts_image_text")

    def select_range_page_option(self, page_option, page_number):
        """
        Click on Page Range dropdown button, and select page option from the screen
        """
        self.driver.click("page_option_range")
        self.driver.click("select_page_option_range", format_specifier=[self.driver.return_str_id_value(page_option).replace("%d", page_number)])

    def select_print_quality_option(self, print_quality_option):
        """
        Click on Print Quality dropdown button on Print Preview screen, and select different options from the list.
        """
        self.driver.scroll("print_quality_dropdown_btn", click_obj=True)
        self.driver.click("page_option_cell", format_specifier=[self.driver.return_str_id_value(print_quality_option)])

    def get_print_quality_selected_value(self):
        """
        Get the Print Quality option value
        """
        return self.driver.get_attribute("print_quality_option_text", "text")

    def select_2_sided_option(self, duplex_option):
        """
        Click on 2 Sided dropdown button, and select duplex option
        """
        self.driver.click("2_sided_dropdown_btn")
        self.driver.click("page_option_cell", format_specifier=[self.driver.return_str_id_value(duplex_option)])

    def get_2_sided_selected_value(self):
        """
        Get the 2 Sided option value
        """
        return self.driver.get_attribute("2_sided_option_text", "text")

    def select_color_mode_option(self, color_option):
        """
        Click on Color Mode button, and select different color option
        """
        self.driver.click("color_mode_dropdown_btn")
        self.driver.click("page_option_cell", format_specifier=[self.driver.return_str_id_value(color_option)])

    def get_color_selected_value(self):
        """
        Get the Color option value
        """
        return self.driver.get_attribute("color_option_text", "text")

    def select_orientation_option(self, orientation_option):
        """
        Click on Orientation button, and select different options
        """
        self.driver.scroll("orientation_dropdown_btn", click_obj=True)
        self.driver.click("page_option_cell", format_specifier=[self.driver.return_str_id_value(orientation_option)])

    def get_orientation_selected_value(self):
        """
        Get the Orientation option value
        """
        return self.driver.get_attribute("orientation_option_text", "text")

    def select_more_options_btn(self):
        """
        Click on More Options button on Print Preview screen
        """
        self.driver.scroll("more_options_btn", click_obj=True)
    
    def verify_app_page_btn(self, timeout=10):
        """
        Verify the App button on Advanced Layout menu
        """
        self.driver.wait_for_object("app_page_btn", timeout=timeout)

    def click_app_page_btn(self, timeout=10):
        """
        Click on App button on Advanced Layout menu
        """
        self.driver.wait_for_object("app_page_btn", timeout=timeout).click()

    def verify_rotate_page_btn(self, timeout=10):
        """
        Verify the Rotate button on Advanced Layout menu
        """
        self.driver.wait_for_object("rotate_page_btn", timeout=timeout)

    def click_rotate_page_btn(self, timeout=10):
        """
        Click on Rotate button on Advanced Layout menu
        """
        self.driver.click("rotate_page_btn", timeout=timeout)

    def verify_exit_screen_dialog(self, timeout=10):
        """
        Verify the exit scan dialog on Print Preview screen
        """
        self.driver.wait_for_object("exit_scan_title", timeout=timeout)

    def click_start_new_scan_btn(self, timeout=10):
        """
        Click on Start New Scan button on exit scan dialog
        """
        self.driver.wait_for_object("start_new_scan_btn", timeout=timeout).click()

    def click_exit_scan_go_home_btn(self, timeout=10):
        """
        Click on Exit Scan button on exit scan dialog
        """
        self.driver.wait_for_object("exit_scan_go_home_btn", timeout=timeout).click()

    def click_no_add_images_btn(self, timeout=10):
        """
        Click on no Add Images button on Print Preview screen
        """
        self.driver.wait_for_object("no_add_images_btn", timeout=timeout).click()

    def verify_more_page_numbers_display(self, timeout=10, raise_e=False):
        """
        Verify more page numbers display on Print Preview screen when there are multiple images
        """
        if self.driver.wait_for_object("more_page_numbers_in_preview", timeout=timeout, raise_e=raise_e):
            return True
        else:
            return False

    def get_no_pages_from_print_preview(self, get_current_page=False):
        if self.driver.wait_for_object("more_page_numbers_in_preview", raise_e=False) is not False:
            page_count_label = str(self.driver.get_attribute("more_page_numbers_in_preview", attribute="text"))
            page_count_label = page_count_label.split('/')
            page_count = int(page_count_label[1])
            current_page = int(page_count_label[0])
            if get_current_page:
                return (page_count, current_page)
        else:
            page_count = 1
        return page_count

    def verify_popup_button(self):
        """
        verify Are you sure popup screen
        """
        self.driver.wait_for_object("leave_btn")
        self.driver.wait_for_object("cancel_button")

    def select_cancel_button(self):
        """
        Click on cancel button on Are you sure popup screen
        """
        self.driver.click("cancel_button")

    def select_leave_button(self):
        """
        Click on Leave button on Are you sure popup screen
        """
        self.driver.click("leave_btn")

    def verify_copy_capture_screen(self, invisible=True):
        """
        Verify copy capture screen 
        """
        self.driver.wait_for_object("x_button")
        self.driver.wait_for_object("flash_button_copy")
        self.driver.wait_for_object("auto_btn_copy", invisible=invisible)

    def click_on_image_selected_to_rotate(self, timeout=10):   
        """
        Click on the image selected for rotate on Print Preview screen
        """
        self.driver.click("rotate_image_selected", timeout=timeout)

    def verify_rotate_delete_btn(self, timeout=10):   
        """
        Verify the Rotate and Delete buttons on Print Preview screen
        """
        self.driver.wait_for_object("rotate_button", timeout=timeout)
        self.driver.wait_for_object("delete_button", timeout=timeout)

    def verify_delete_cancel_popup(self, timeout=10):   
        """
        Verify the delete and cancel popup screen
        """
        self.driver.wait_for_object("delete_button", timeout=timeout)
        self.driver.wait_for_object("cancel_button", timeout=timeout)

    def click_on_rotate_btn(self, timeout=10):   
        """
        Click on the Rotate button on Print Preview screen
        """
        self.driver.click("rotate_button", timeout=timeout)

    def click_on_delete_btn(self, timeout=10):   
        """
        Click on the Delete button on Print Preview screen
        """
        self.driver.click("delete_button", timeout=timeout)

    def verify_delete_btn(self, timeout=10):   
        """
        verify the Delete button on Print Preview screen
        """
        self.driver.click("delete_button", timeout=timeout)

    def verify_reset_enabled_btn(self, timeout=10):   
        """
        Verify the Reset button on Print Preview screen
        """
        self.driver.wait_for_object("reset_enabled_button", timeout=timeout)

    def verify_add_rotate_reorder_btn(self, timeout=10):
        """
        Verify the Add, Rotate and Reorder buttons on Print Preview screen
        """
        self.driver.wait_for_object("app_page_btn", timeout=timeout)
        self.driver.wait_for_object("rotate_page_btn", timeout=timeout)
        self.driver.wait_for_object("page_reorder_btn", timeout=timeout)

    def select_photo_btn(self):
        """
        Click on Photo tab on More Options screen
        """
        self.driver.click("photo_tab")

    def select_document_btn(self):
        """
        Click on Document tab on More Options screen
        """
        self.driver.click("document_tab")

    def select_quality_option(self, quality_option):
        """
        Click on Quality dropdown butotn, and select different options from the list.
        """
        self.driver.click("quality_dropdown_btn")
        self.driver.click("page_option_cell", format_specifier=[self.driver.return_str_id_value(quality_option)])

    def get_quality_selected_value(self):
        """
        Get the Quality option value
        """
        return self.driver.get_attribute("quality_option_text", "text")

    def select_borderless_switch(self, toggle=True):
        """
        Toggle on or off for Borderless switch
        """
        self.driver.check_box("borderless_toggle", uncheck=not toggle, change_check=False)

    def get_borderless_switch_value(self):
        """
        Get the borderless switch value
        """
        return self.driver.get_attribute("borderless_toggle", "checked")

    def select_scaling_option(self, scaling_option):
        """
        Click on Scaling dropdown butotn, and select different options from the list.
        """
        self.driver.click("scaling_dropdown_btn")
        self.driver.click("page_option_cell", format_specifier=[self.driver.return_str_id_value(scaling_option)])

    def get_scaling_selected_value(self):
        """
        Get the Scaling option value
        """
        return self.driver.get_attribute("scaling_option_text", "text")

    def select_back_btn(self):
        """
        Click on Back button on More Options screen
        """
        self.driver.click("back_btn")

    def select_paper_size_dropdown(self):
        """
        Click on Paper Size dropdown button on Print Preview screen
        """
        self.driver.scroll("paper_size_dropdown_btn", click_obj=True)

    def select_paper_size_option(self, paper_size_option):
        """
        Click on Paper Size dropdown button on Print Preview screen, and select different options from the list.
        """
        self.driver.click("page_option_cell", format_specifier=[self.driver.return_str_id_value(paper_size_option)], change_check={"wait_obj": "paper_ready_to_use_txt", "invisible": True})

    def click_print_btn(self, timeout=10):
        """
        Click on Print button on Print Preview screen
        :param timeout: The timeout to wait for the button to be clickable
        """
        self.driver.wait_for_object("print_btn", timeout=timeout).click()
    
    def verify_print_photo_preview_title(self, timeout=10):
        """
        Click on Print button on Print Preview screen and wait for the print job to be sent
        :param timeout: The timeout to wait for the print job to be sent
        """
        self.driver.wait_for_object("print_photo_preview_title", timeout=timeout)
    
    def print_photos_preivew_next_btn(self):
        """
        Click on Next button on Print Photos Preview screen
        """
        self.driver.click("print_photos_preview_next_btn", change_check={"wait_obj": "print_photos_preview_next_btn", "invisible": True})

    def click_print_photos_preview_next_btn(self, timeout=20):
        """
        Click on Next button on Print Photos Preview screen
        """
        self.driver.click("print_photos_preview_next_btn", timeout=timeout)
    
    def click_print_preview_done_btn(self, timeout=10):
        """
        Click on Done button on Print Preview screen
        """
        self.driver.click("print_preview_done_btn")
    
    def verify_print_preview_done_btn(self, timeout=10):
        """
        Verify the Done button on Print Preview screen
        """
        return self.driver.wait_for_object("print_preview_done_btn", timeout=timeout)
    
    def verify_view_print_job_list_btn(self, timeout=10):
        """
        Verify the View Print Job List button on Print Preview screen
        """
        return self.driver.wait_for_object("view_print_job_list_btn", timeout=timeout)
    
    def click_view_print_job_list_btn(self, timeout=10):
        """
        Click on View Print Job List button on Print Preview screen
        """
        self.driver.click("view_print_job_list_btn")
    
    def verify_print_jobs_title(self, timeout=10):
        """
        Verify the Print Jobs title on Print Preview screen
        """
        return self.driver.wait_for_object("print_jobs_title", timeout=timeout)
    
    def click_print_preview_share_photo_btn(self, timeout=10):
        """
        Click on Share Photo button on Print Preview screen
        """
        self.driver.click("print_preview_share_photo_btn")
    
    def click_print_btn(self):
        """
        Click on Print button on Print Preview screen
        """
        self.driver.click("print_btn")

    def verify_print_quality_selected_value(self, selected_value="automatic_option"):
        """
        verify the Print Quality option value
        """
        if self.driver.wait_for_object(selected_value):
            return True
        else:
            return False

    def click_printer_preview_swipe_up(self, timeout=10):
        """
        Click on Print preview swipe up button
        """
        self.driver.click("swipe_up_printer_setting", timeout=timeout)

    def verify_print_btn(self):
        """
        Verify the Print button on Print Preview screen
        """
        if self.driver.wait_for_object("print_btn"):
            return True
        else:
            return False
    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_print_preview_screen(self):
        """
        verify current screen is Print Preview screen
        """
        self.driver.wait_for_object("print_preview_title")
    
    def click_page_option_btn(self, timeout=10):
        """
        Click on Page Option button
        """
        self.driver.wait_for_object("page_option_btn", timeout=timeout).click()

    def verify_page_option_edit_btn(self, timeout=10):
        """
        verify Page Option Edit button on Print Preview screen
        """
        return self.driver.wait_for_object("page_option_edit_btn", timeout=timeout)

    def click_page_option_edit_btn(self, timeout=10):
        """
        Click on Page Option Edit button
        """
        self.driver.wait_for_object("page_option_edit_btn", timeout=timeout).click()

    def verify_page_option_replace_btn(self, timeout=10):
        """
        verify Page Option Replace button on Print Preview screen
        """
        return self.driver.wait_for_object("page_option_replace_btn", timeout=timeout)

    def click_page_option_replace_btn(self, timeout=10):
        """
        Click on Page Option Replace button
        """
        self.driver.wait_for_object("page_option_replace_btn", timeout=timeout).click()

    def verify_page_option_delete_btn(self, timeout=10):
        """
        verify Page Option Delete button on Print Preview screen
        """
        return self.driver.wait_for_object("page_option_delete_btn", timeout=timeout)

    def verify_yes_and_no_btn(self, timeout=10):
        """
        verify Yes and No buttons on Print Preview screen
        """
        self.driver.wait_for_object("yes_button", timeout=timeout)
        self.driver.wait_for_object("no_button", timeout=timeout)

    def click_page_reorder_btn(self, timeout=10):
        """
        click Page Reorder button on Print Preview screen
        """
        self.driver.click("page_reorder_btn", timeout=timeout)

    def verify_page_reorder_btn(self, timeout=10):
        """
        verify Page Reorder button on Print Preview screen
        """
        self.driver.wait_for_object("page_reorder_btn", timeout=timeout)

    def click_all_page_option(self, timeout=10):
        """
        verify All Page option on Print Preview screen
        """
        self.driver.wait_for_object("all_page_option", timeout=timeout).click()

    def click_print_preview_button(self, timeout=10):
        """
        Click on Print Preview button
        """
        self.driver.click("print_preview_button", timeout=timeout)

    def verify_printer_item(self):
        """
        verify Printer item on the Print Preview screen
        """
        self.driver.wait_for_object("printer_item")

    def verify_copies_item(self):
        """
        verify Copies item on the Print Preview screen
        """
        self.driver.wait_for_object("copies_item")

    def verify_2_sided_item(self, raise_e=True):
        """
        verify 2_Sided item on the Print Preview screen
        """
        self.driver.wait_for_object("2_sided_item", raise_e=raise_e)

    def verify_color_mode_item(self):
        """
        verify Color Mode item on the Print Preview screen
        """
        self.driver.scroll("color_mode_item")

    def verify_print_quality_item(self, invisible=True):
        """
        verify Print Quality item on the Print Preview screen
        """
        self.driver.wait_for_object("print_quality_item", invisible=invisible)

    def verify_orientation_item(self):
        """
        verify Orientation item on the Print Preview screen
        """
        self.driver.scroll("orientation_item")

    def verify_more_options_screen(self):
        """
        verify More Options screen
        """
        self.driver.wait_for_object("more_options_btn")
        self.driver.wait_for_object("photo_tab")
        self.driver.wait_for_object("document_tab")

    def verify_options_on_photo_tab(self):
        """
        verify Options on PHOTO tab
        """
        self.driver.wait_for_object("quality_item")
        self.driver.wait_for_object("borderless_item")
        self.driver.wait_for_object("scaling_item")

    def verify_paper_size_screen(self):
        """
        verify Paper Size screen after click on Paper Size dropdown button
        """
        self.driver.wait_for_object("paper_ready_to_use_txt")
        self.driver.wait_for_object("additional_paper_options_txt")

    def verify_paper_size_option(self, paper_size_option, invisible=False, raise_e=True):
        """
       Verify the paper size options on the paper size list screen
        """
        return self.driver.wait_for_object("page_option_cell", format_specifier=[self.driver.return_str_id_value(paper_size_option)], invisible=invisible, raise_e=raise_e)

    def verify_image_range_button(self, invisible=False):
        """
        verify Image page range button displays on Print Preview button
        """
        self.driver.wait_for_object("image_page_range_btn", invisible=invisible)

    def verify_print_preview_image_info(self, timeout=10, displayed=True, is_one_image=False):
        """
        Get the current image and total image count.
        if there is only one image, then the image numbe won't show on the screen
        :return: Returns a tuple of (current page, total pages)
        """
        if is_one_image:
            return self.driver.wait_for_object("image_page_range_btn", invisible=True)
        else:
            counter_parts = self.driver.get_attribute("image_page_range_txt", "text", timeout=timeout, displayed=displayed).strip().split("/")
            return (int(counter_parts[0]), int(counter_parts[-1]))
        
    def verify_paper_size_item(self, timeout=10):
        """
        verify Paper Size item on the Print Preview screen
        """
        self.driver.wait_for_object("paper_size_item", timeout=timeout)

    def verify_edit_screen_title(self,timeout=10):
        """
        verify Edit screen title
        """
        return self.driver.wait_for_object("edit_screen_title", timeout=timeout)

    def get_edit_screen_title(self, timeout=10):
        """
        Get the Edit screen title
        """
        return self.driver.get_attribute("edit_screen_title", "text", timeout=timeout)

    def click_crop_btn(self, timeout=10):
        """
        Click on Crop button
        """
        self.driver.wait_for_object("crop_btn", timeout=timeout).click()

    def click_img_rotate_btn(self, timeout=10):
        """
        Click on Rotate button
        """
        self.driver.wait_for_object("img_rotate_btn", timeout=timeout).click()

    def click_edit_screen_done_btn(self, timeout=10):
        """
        Click on Done button on Edit screen
        """
        self.driver.wait_for_object("edit_screen_done_btn", timeout=timeout).click()

    def click_crop_screen_done_btn(self, timeout=10):
        """
        Click on Done button on Crop screen
        """
        self.driver.wait_for_object("crop_screen_done_btn", timeout=timeout).click()

    def click_shortcut_btn(self, timeout=10):
        """
        Click on Shortcuts button
        """
        self.driver.wait_for_object("shortcut_btn", timeout=timeout).click()

    def edit_shortcut_name(self, shortcut_name, timeout=10):
        """
        Edit the shortcut name
        """
        self.driver.wait_for_object("shortcut_name_txt_btn", timeout=timeout).send_keys(shortcut_name)

    def get_shortcut_name(self, timeout=10):
        """
        Get the shortcut name
        """
        return self.driver.get_attribute("shortcut_name_txt_btn", "text", timeout=timeout)

    def verify_shortcut_name_txt_btn(self, timeout=10):
        """
        Verify the shortcut name text button
        """
        self.driver.wait_for_object("shortcut_name_txt_btn", timeout=timeout)

    def click_shortcut_info_btn(self, timeout=10):
        """
        Click on Shortcuts Info button
        """
        self.driver.wait_for_object("shortcut_info_btn", timeout=timeout).click()

    def verify_shortcut_info_title(self, timeout=10):
        """
        Verify the shortcut info title
        """
        self.driver.wait_for_object("shortcut_info_title", timeout=timeout)

    def click_edit_screen_crop_btn(self, timeout=10):
        """
        Click on Crop button on Edit screen
        """
        self.driver.wait_for_object("edit_screen_crop_btn", timeout=timeout).click()

    def click_edit_screen_adjust_btn(self, timeout=10):
        """
        Click on Adjust button on Edit screen
        """
        self.driver.wait_for_object("edit_screen_adjust_btn", timeout=timeout).click()

    def click_edit_screen_filter_btn(self, timeout=10):
        """
        Click on Filter button on Edit screen
        """
        self.driver.wait_for_object("edit_screen_filter_btn", timeout=timeout).click()

    def click_edit_screen_text_btn(self, timeout=10):
        """
        Click on Text button on Edit screen
        """
        self.driver.wait_for_object("edit_screen_text_btn", timeout=timeout).click()

    def click_edit_screen_markup_btn(self, timeout=10):
        """
        Click on Markup button on Edit screen
        """
        self.driver.wait_for_object("edit_screen_markup_btn", timeout=timeout).click()

    def click_edit_screen_cancel_btn(self, timeout=10):
        """
        Click on Cancel button on Edit screen
        """
        self.driver.wait_for_object("edit_screen_cancel_btn", timeout=timeout).click()

    def click_fax_btn(self, timeout=10):
        """
        Click on Fax button
        """
        self.driver.wait_for_object("fax_btn", timeout=timeout).click()

    def verify_compose_fax_page_title(self, timeout=15):
        """
        Verify the Compose Fax page title
        """
        self.driver.wait_for_object("compose_fax_page_title", timeout=timeout)

    def click_save_btn(self, timeout=10):
        """
        Click on Save button
        """
        self.driver.wait_for_object("save_btn", timeout=timeout).click()

    def click_close_btn(self, timeout=10):
        """
        Click on close button
        """
        self.driver.click("close_btn", timeout=timeout)

    def verify_save_and_share_option_title(self, timeout=10):
        """
        Verify the Save Option title
        """
        self.driver.wait_for_object("save_and_share_option_title", timeout=timeout)

    def verify_alert_message(self, timeout=10):
        """
        Returns the alert message text after print action using get_attribute for 'alert_message' with 'text'.
        Exceptions will propagate if the attribute is not found.
        """
        return self.driver.get_attribute("alert_message", "text", timeout=timeout)
    
    def verify_color_options_drop_down(self, timeout=10):
        """
        Verify the Color Options dropdown
        """
        self.driver.wait_for_object("color_options_dropdown", timeout=timeout)
    
    def click_cancel_print_job(self):
        """
        Click on Cancel Print Job button
        """
        self.driver.click("cancel_print_job_btn")

    def verify_print_job_canceled_message(self, timeout=10):
        """
        Verify the Print Job Canceled message
        """
        self.driver.wait_for_object("print_job_canceled_message", timeout=timeout)
    
    def select_pdf_file(self):
        """
        Select a PDF file from the list
        """
        self.driver.click("pdf_file")
    
    def click_paper_size_100x150mm(self):
        """
        Click on Paper Size 100x150mm option
        """
        self.driver.click("paper_size_100x150mm")

    def click_paper_size_4x12in(self):
        """
        Click on Paper Size 4x12in option
        """
        self.driver.click("paper_size_4x12in")

    def click_paper_size_4x6in(self):
        """
        Click on Paper Size 4x6in option
        """
        self.driver.click("paper_size_4x6in")

    def click_paper_size_5x7in(self):
        """
        Click on Paper Size 5x7in option
        """
        self.driver.click("paper_size_5x7in")

    def click_paper_size_ISOA4(self):
        """
        Click on Paper Size ISOA4 option
        """
        self.driver.click("paper_size_ISOA4")

    def click_paper_size_IndexCard3x5(self):
        """
        Click on Paper Size Index Card 3x5 option
        """
        self.driver.click("paper_size_IndexCard3x5")
    
    def click_paper_size_Letter(self):
        """
        Click on Paper Size Letter option
        """
        self.driver.click("paper_size_Letter")

    def click_paper_size_Legal(self):
        """
        Click on Paper Size Legal option
        """
        self.driver.click("paper_size_Legal")

    def click_paper_size_drop_down(self):
        """
        Click on Paper Size dropdown button on Print Preview screen
        """
        self.driver.click("paper_size_drop_down")
    
    def click_start_black_button(self): 
        """
        Click on Start Black button
        """
        self.driver.click("start_black_button")

    def click_start_color_button(self):
        """
        Click on Start Color button
        """
        self.driver.click("start_color_button")
    
    def verify_print_sent_text(self, timeout=10, raise_e=True):
        """
        Verify the Print Sent text on Print Preview screen
        """
        return self.driver.wait_for_object("print_sent_text", timeout=timeout, raise_e=raise_e)
    
    def click_recent_files_grid_view(self):
        """
        Click on Recent Files grid view
        """
        self.driver.click("recent_files_grid_view")

    def click_downloads_grid_view(self):
        """
        Click on Downloads grid view
        """
        self.driver.click("downloads_grid_view")

    def click_search_option_btn(self):
        """
        Click on Search option button
        """
        self.driver.click("search_option_btn")
    
    def enter_text_in_search_input_box(self, text):
        """
        Enter text in the Search input box
        """
        self.driver.send_keys("search_input_box", text)
    
    def click_xls_file_card(self):
        """
        Click on XLS file card
        """
        self.driver.click("xls_file_card")
    
    def click_pdf_file_card_dynamic(self):
        """
        Click on PDF file card (dynamic)
        """
        self.driver.click("pdf_file_card_dynamic")
    
    def click_paper_mode_btn(self):
        """
        Click on Paper mode button
        """
        self.driver.click("paper_mode_btn")

    def click_layout_mode_btn(self, timeout=20):
        """
        Click on Layout mode button
        """
        self.driver.click("layout_mode_btn", timeout=timeout)
    def click_adjust_mode_btn(self):
        """
        Click on Adjust mode button
        """
        self.driver.click("adjust_mode_btn")

    def click_text_mode_btn(self, timeout=10):
        """
        Click on Text mode button
        """
        self.driver.click("text_mode_btn", timeout=timeout)
    
    def select_5X7_paper_size(self, timeout=10):
        """
        Click on 5X7 paper size option
        """
        self.driver.click("paper_size_5x7", timeout=timeout)

    def verify_paper_size_load_error(self, timeout=10):
        """
        Verify the Paper Size Load Error message
        """
        self.driver.wait_for_object("paper_size_load_error", timeout=timeout)
    
    def verify_print_photos_tool_tip_msg(self, timeout=10, raise_e=True):
        """
        Verify the Print Photos tool tip message
        """
        self.driver.wait_for_object("print_photos_tool_tip_msg", timeout=timeout, raise_e=raise_e)
    
    def verify_tooltip_shows_and_disappears(self, timeout=10, disappear_time=8):
        """
        Verify tooltip shows and disappears after 8 seconds.
        Tooltip message: 'Tap once to resize, double tap to crop'
        """
        # Verify tooltip appears
        self.driver.wait_for_object("print_photos_tool_tip_msg", timeout=timeout)
        # Need to wait for tooltip to disappear so sleep for disappear_time seconds
        time.sleep(disappear_time)
        # Verify tooltip disappears
        self.driver.wait_for_object("print_photos_tool_tip_msg", raise_e=False)
    
    def click_print_photos_tool_tip_btn(self, timeout=10):
        """
        Click on Print Photos tool tip button
        """
        self.driver.click("print_photos_tool_tip_btn", timeout=timeout)
    
    def verify_printer_preview_tooltip(self, timeout=10):
        """
        Verify the Printer Preview tooltip message
        """
        self.driver.wait_for_object("printer_preview_tooltip_msg", timeout=timeout)
    
    def verify_printer_preview_tooltip_disappears(self, timeout=10):
        """
        Verify the Printer Preview tooltip message disappears
        """
        self.driver.wait_for_object("printer_preview_tooltip_msg", timeout=timeout, invisible=True)
    
    def click_print_preview_fit_btn(self, timeout=10, raise_e=True):
        """
        Verify the presence of the Fit button in the Print Preview screen
        """
        return self.driver.click("print_preview_fit_btn", timeout=timeout)

    def click_print_preview_fit_btn(self, timeout=10):
        """
        Click on the Fit button in the Print Preview screen
        """
        return self.driver.click("print_preview_fit_btn", timeout=timeout)

    def check_fit_btn_is_selected(self, timeout=10):
        """
        """
        return self.driver.get_attribute("print_preview_fit_btn", "selected", timeout=timeout)

    def click_print_preview_fill_btn(self, timeout=10):
        """
        Click on the Fill button in the Print Preview screen
        """
        return self.driver.click("print_preview_fill_btn", timeout=timeout)

    def check_fill_btn_is_selected(self, timeout=10, raise_e=True):
        """
        """
        return self.driver.get_attribute("print_preview_fill_btn", "selected", timeout=timeout, raise_e=raise_e)

    def click_print_preview_border_btn(self, timeout=10):
        """
        Click on the Border button in the Print Preview screen
        """
        return self.driver.click("print_preview_border_btn", timeout=timeout)

    def click_print_preview_crop_btn(self, timeout=10):
        """
        Click on the Crop button in the Print Preview screen
        """
        return self.driver.click("print_preview_crop_btn", timeout=timeout)

    def check_rotate_btn_is_selected(self, timeout=10):
        """
        """
        return self.driver.get_attribute("print_preview_crop_btn", "selected", timeout=timeout)

    def click_print_preview_rotate_btn(self, timeout=10):
        """
        Click on the Rotate button in the Print Preview screen
        """
        return self.driver.click("print_preview_rotate_btn", timeout=timeout)

    def check_rotate_btn_is_selected(self, timeout=10):
        """
        """
        return self.driver.get_attribute("print_preview_rotate_btn", "selected", timeout=timeout)

    def click_print_preview_flip_h_btn(self, timeout=10):
        """
        Click on the Flip Horizontal (Flip H) button in the Print Preview screen
        """
        return self.driver.click("print_preview_flip_h_btn", timeout=timeout)

    def check_rotate_btn_is_selected(self, timeout=10):
        """
        """
        return self.driver.get_attribute("print_preview_flip_h_btn", "selected", timeout=timeout)

    def click_print_preview_flip_v_btn(self, timeout=10):
        """
        Click on the Flip Vertical (Flip V) button in the Print Preview screen
        """
        return self.driver.click("print_preview_flip_v_btn", timeout=timeout)

    def click_image_editor_title(self):
        """
        """
        self.driver.click("image_editor_title")
    
    