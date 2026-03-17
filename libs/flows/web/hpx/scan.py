
import logging
from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import time
from selenium.webdriver.common.keys import Keys

class Scan(HPXFlow):
    flow_name = "scan"

    SOURCE = "source"
    GLASS = "Scanner Glass"
    ADF = "Document Feeder"

    PRESET = "preset"
    DOCUMENTS = "Documents"
    PHOTO = "Photo"
    ADVPRESETS = "advanced_presets"
    BOOK = "Book"
    MULTI_ITEM = "Multi-Item"
    ID_CARD = "ID_Card"
    
    AREA = "scan_area"
    PAGESIZE = "page_size"
    ENTIRE_SCAN_AREA = "Entire scan area"
    LETTER = "Letter (8.5 x 11 in)"
    A4 = "A4 (210 x 297mm)"
    LEGAL = "Legal (8.5 x 14 in)"
    X46 = "4 x 6 in (10 x 15 cm)"
    X57 = "5 x 7 in (13 x 18 cm)"

    OUTPUT = "output"
    COLOR = "Color"
    GRAYSCALE = "Grayscale"

    DPI = "resolution"
    DPI_75 = "75 dpi"
    DPI_150 = "150 dpi"
    DPI_300 = "300 dpi"
    DPI_600 = "600 dpi"
    DPI_1200 = "1200 dpi"
    
    FILETYPE = "file_type"

    BASIC_PDF = "Basic PDF"
    IMAGE_JPG = "Image(*.jpg)"
    SEARCHABLE_PDF = "Searchable PDF"
    PLAIN_TEXT = "Plain Text (*.txt)"
    WORD_DOCUMENT = "Word Document (*.docx)"

    COMPRESSION_NONE = "None"
    COMPRESSION_LOW = "Low"
    COMPRESSION_MEDIUM = "Medium"
    COMPRESSION_HIGH = "High"

    LANGUAGE_EN = "English(US)"


    HELP_CENTER = ["support.hp.com"]

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    # ---------------- Scanning ---------------- # 
    def click_preview_btn(self):
        self.driver.click("preview_btn")

    def click_scan_btn(self):
        sleep(2)
        self.driver.click("scan_btn", change_check={"wait_obj": "scan_btn", "invisible": True}, retry=2, delay=1)
    
    def click_scan_btn_on_back_card_screen(self):
        self.driver.click("scan_btn_on_back_card", change_check={"wait_obj": "scan_btn_on_back_card", "invisible": True}, retry=2, delay=1)

    def select_import_text(self):
        self.driver.click("text_4_scanner")

    def click_start_scan_text(self):
        self.driver.click("start_scan_text")

    def select_auto_enhancement_icon(self):
        """
        Click on auto enhancement icon located on 
        top right of scanner screen below the title bar close to gear icon -> auto enhancement panel shows
        """
        self.driver.click("auto_enhancement_icon", change_check={"wait_obj": "auto_enhancements_text"}, retry=2, delay=1, raise_e=False)
    
    def click_cancel_btn(self):
        el = self.driver.wait_for_object("cancel_btn", interval=0.2, timeout=2)
        el.click()

    def click_exit_btn(self):
        self.driver.click("exit_btn")

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

    def select_different_file_from_scan_area(self, filename):
        self.select_import_text()
        self.verify_file_picker_dialog()
        self.input_file_name(filename)
        self.verify_import_screen()
        self.click_import_done_btn()
        self.verify_scan_result_screen(timeout=120)

    def click_import_full_option(self):
        self.driver.click("import_screen_full_group")

    def click_detect_edges_checkbox(self):
        self.driver.click("detect_edges_checkbox")
    
    # ---------------- New Scan Auto-Enhancements dialog ---------------- #
    def click_auto_enhancement_cancel_btn(self):
        self.driver.click("auto_enhancement_cancel_btn")

    def click_get_started_btn(self, timeout=3):
        self.driver.click("auto_enhancement_get_started_btn", timeout=timeout)

    def click_learn_more_link(self):
        self.driver.click("learn_more_link")

    # ---------------- Scanner Settings ---------------- #
    def select_source_dropdown(self):
        self.driver.click("source_dropdown", change_check={"wait_obj": "source_list"}, retry=3, delay=2)

    def select_source_scanner_glass(self):
        self.driver.click("source_scanner_glass")

    def select_source_document_feeder(self):
        self.driver.click("source_document_feeder")

    def select_presets_dropdown(self):
        self.driver.click("presets_dropdown", change_check={"wait_obj": "presets_list"}, retry=2, delay=1)

    def select_scan_area_dropdown(self):
        self.driver.click("scan_area_dropdown", change_check={"wait_obj": "scan_area_list"}, retry=2, delay=1)

    def select_page_size_dropdown(self):
        self.driver.click("page_size_dropdown", change_check={"wait_obj": "page_size_list"}, retry=2, delay=1)

    def select_output_dropdown(self):
        self.driver.click("output_dropdown", change_check={"wait_obj": "output_list"}, retry=2, delay=1)

    def select_resolution_dropdown(self, close=False):
        if not close:
            self.driver.click("resolution_dropdown", change_check={"wait_obj": "resolution_list"}, retry=2, delay=1)
        else:
            self.driver.click("resolution_dropdown")

    def select_dropdown_listitem(self, dropdown, name):
        """
        @param dropdown:
            - source
            - preset
            - scan_area
            - output
            - resolution
            - advanced_presets
        @param name:
            name of the listitem
        """
        if dropdown == "source":
            self.select_source_dropdown()
        elif dropdown == "preset":
            self.select_presets_dropdown()
        elif dropdown == "advanced_presets":
            self.select_advanced_presets_dropdown()
        elif dropdown == "file_type":
            self.select_file_type_dropdown()
            if self.driver.driver_type.lower() == "windows":
                if name in [self.WORD_DOCUMENT, self.PLAIN_TEXT]:
                    self.driver.swipe("file_type_list", direction='down', distance=2)
                elif name in [self.BASIC_PDF, self.SEARCHABLE_PDF, self.IMAGE_JPG]:
                    self.driver.swipe("file_type_list", direction="up", distance=2)
        elif dropdown == "scan_area":
            self.select_scan_area_dropdown()
            if self.driver.driver_type.lower() == "windows":
                if name in [self.X46, self.X57]:
                    self.driver.swipe("scan_area_list", distance=2)
                elif name in [self.ENTIRE_SCAN_AREA, self.LETTER]:
                    self.driver.swipe("scan_area_list", direction="up", distance=2)
        elif dropdown == "page_size":
            self.select_page_size_dropdown()
            if self.driver.driver_type.lower() == "windows":
                if name in [self.X46, self.X57, self.LEGAL]:
                    self.driver.swipe("page_size_list", distance=2)
                elif name in [self.ENTIRE_SCAN_AREA, self.LETTER, self.A4]:
                    self.driver.swipe("page_size_list", direction="up", distance=2)  
        elif dropdown == "output":
            self.select_output_dropdown()
        elif dropdown == "resolution":
            self.select_resolution_dropdown()
            if self.driver.driver_type.lower() == "windows":
                if name in [self.DPI_600, self.DPI_1200]:
                    self.driver.swipe("resolution_list", distance=2)
                elif name in [self.DPI_75, self.DPI_150]:
                    self.driver.swipe("resolution_list", direction="up", distance=2)

        sleep(1)
        # self.verify_dropdown_listitem(name)
        # self.click_dropdown_listitem(name)

        if dropdown == "file_type" and self.verify_file_type_list(raise_e=False):
                self.click_dropdown_listitem(name)
        else:
            self.click_dropdown_listitem(name)

        if dropdown == "source" and self.verify_source_list_items(raise_e=False):
            if name == self.GLASS:
                self.select_source_scanner_glass()
            elif name == self.ADF:
                self.select_source_document_feeder()

        if dropdown == "scan_area" and self.verify_scan_area_list(raise_e=False):
            self.click_dropdown_listitem(name)

        if dropdown == "page_size" and self.verify_page_size_list(raise_e=False):
            self.click_dropdown_listitem(name)

        if dropdown == "resolution" and self.verify_resolution_list(raise_e=False):
            self.click_dropdown_listitem(name)

    def click_dropdown_listitem(self, name, timeout=30):
        self.driver.click("dynamic_listitem", format_specifier=[name], timeout=timeout)

    def get_scan_resolution_value(self, raise_e=True):
        return self.driver.wait_for_object("resolution_dropdown", raise_e=raise_e).text

    def get_scan_source_value(self, raise_e=True):
        return self.driver.wait_for_object("source_dropdown", raise_e=raise_e).text

    def get_scan_presets_value(self, raise_e=True):
        return self.driver.wait_for_object("presets_dropdown", raise_e=raise_e).text

    def get_scan_area_value(self, raise_e=True):
        return self.driver.wait_for_object("scan_area_dropdown", raise_e=raise_e).text

    def get_scan_page_size_value(self, raise_e=True):
        return self.driver.wait_for_object("page_size_dropdown", raise_e=raise_e).text

    def get_scan_output_value(self, raise_e=True):
        return self.driver.wait_for_object("output_dropdown", raise_e=raise_e).text

    def get_all_scan_settings(self):
        scan_settings = []
        source = self.get_scan_source_value()
        scan_settings.append(source)
        advanced_presets = self.get_scan_presets_value()
        scan_settings.append(advanced_presets)
        if self.driver.wait_for_object("source_scanner_glass", raise_e=False):
            scan_area = self.get_scan_area_value()
            scan_settings.append(scan_area)
        else:
            page_size = self.get_scan_page_size_value()
            scan_settings.append(page_size)
        output = self.get_scan_output_value()
        scan_settings.append(output)
        resolution = self.get_scan_resolution_value()
        scan_settings.append(resolution)
        logging.info(scan_settings)
        return scan_settings

    def click_2_sided_item(self):
        self.driver.click("2_sided_item")
    
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
    def click_import_auto_option(self):
        self.driver.click("import_screen_auto_group") 

    def click_import_full_option(self):
        self.driver.click("import_screen_full_group") 

    def click_import_done_btn(self):
        self.driver.click("import_done_btn", change_check={"wait_obj": "import_done_btn", "invisible": True}, retry=2, delay=2) 

    def click_import_flatten_btn(self):
        self.driver.click("detect_edges_flatten_text") 
    
    # ---------------- Scan Preview screen ---------------- # 
    def click_image_edit_btn(self):
        sleep(2)
        if self.driver.click("image_edit_btn", change_check={"wait_obj": "image_edit_btn", "invisible": True}, retry=2, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("image_edit_btn", timeout=2)
            el.send_keys(Keys.ENTER)
            
    def click_image_rotate_btn(self):
        self.driver.click("image_rotate_btn")

    def click_image_replace_btn(self):
        if self.driver.click("image_replace_btn", change_check={"wait_obj": "image_replace_btn", "invisible": True}, retry=2, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("image_replace_btn", timeout=2)
            el.send_keys(Keys.ENTER)

    def click_image_delete_btn(self):
        if self.driver.click("image_delete_btn", change_check={"wait_obj": "delete_title_delete_btn"}, retry=2, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("image_delete_btn", timeout=2)
            el.send_keys(Keys.ENTER)

    def click_gallery_view_icon(self):
        self.driver.click("gallery_image")  

    def click_thumbnail_view_icon(self):
        self.driver.click("thumbnail_image", change_check={"wait_obj": "thumbnail_select_all_btn"}, retry=2, delay=1)

    def hover_thumbnail_view_icon(self):
        self.driver.hover("thumbnail_image")

    def hover_gallery_view_icon(self):
        self.driver.hover("gallery_image")

    def select_gallery_item(self, num):
        self.driver.click("dynamic_item_btn", format_specifier=[str(num)])

    # ----------------  Thumbnail view ---------------- #  
    def click_thumbnail_edit_btn(self):
        self.driver.click("thumbnail_edit_btn")

    def click_thumbnail_redact_btn(self):
        self.driver.click("thumbnail_redact_btn")

    def click_thumbnail_scribble_btn(self):
        self.driver.click("thumbnail_scribble_btn")

    def click_thumbnail_text_extract_btn(self):
        self.driver.click("thumbnail_text_extract_btn")

    def click_thumbnail_rotate_btn(self):
        self.driver.click("thumbnail_rotate_btn")

    def click_thumbnail_delete_btn(self):
        if self.driver.click("thumbnail_delete_btn", change_check={"wait_obj": "delete_title_delete_btn"}, retry=2, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("thumbnail_delete_btn", timeout=2)
            el.send_keys(Keys.ENTER)

    def click_thumbnail_select_all_btn(self):
        self.driver.click("thumbnail_select_all_btn", change_check={"wait_obj": "thumbnail_deselect_all_btn"}, retry=2, delay=1)

    def click_thumbnail_deselect_all_btn(self):
        self.driver.click("thumbnail_deselect_all_btn", change_check={"wait_obj": "thumbnail_select_all_btn"}, retry=2, delay=1)

    def select_thumbnail_item(self, num):
        self.driver.click("myhp_window")
        sleep(1)
        self.driver.click("dynamic_item_btn", format_specifier=[str(num)])
    
    def get_thumbnail_edit_state(self):
        return self.driver.get_attribute("thumbnail_edit_btn", attribute="IsEnabled")

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
    
    def click_edit_id_card_btn(self):
        '''
        Click on the Edit button on Scanner screen with ID card advanced presets
        '''
        self.driver.click("edit_btn")

    def click_replace_btn(self):
        '''
        Click on the Replace button on Scanner screen with ID card advanced presets
        '''
        self.driver.click("replace_btn")
    
    def click_checkmark_btn(self):
        self.driver.click("checkmark_btn")
        
    def click_save_btn(self):
        self.driver.click("save_btn")

    def click_print_btn(self):
        if self.driver.click("print_btn", change_check={"wait_obj": "simple_print_dialog_print_btn", "flow_change": "print"}, retry=3, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("print_btn", timeout=2)
            el.send_keys(Keys.ENTER)

    def click_shortcuts_btn(self):
        self.driver.click("shortcuts_btn") 

    def click_share_btn(self):
        self.driver.click("share_btn") 

    def click_fax_btn(self):
        self.driver.click("fax_btn") 

    def click_dialog_close_btn(self):
        self.driver.click("close_btn", change_check={"wait_obj": "open_file_btn", "invisible": True}, retry=2, delay=1)

    def click_close_on_scan_canceled_dialog(self):
        self.driver.click("scan_canceled_close_btn", change_check={"wait_obj": "scan_canceled_close_btn", "invisible": True}, retry=4, delay=1)

    def click_add_pages_btn(self):
        self.driver.click("add_pages_btn", change_check={"wait_obj": "save_btn", "invisible": True}, retry=2, delay=1)

    def click_new_scan_btn(self):
        self.driver.click("new_scan_btn")

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
        obj = self.driver.wait_for_object("pic_item", format_specifier=[index])
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
        obj = self.driver.wait_for_object("pic_item_thumbnail_view", format_specifier=[index])
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
            self.driver.click("yes_btn", retry=3, delay=1, change_check={"wait_obj": "yes_btn", "invisible": True}, raise_e=False)
        else:
            self.driver.click("scribble_yes_btn")

    def click_no_btn(self):
        self.driver.click("no_btn") 

    # ---------------- save/share/"Delete selected images?" dialog ---------------- #     
    def click_dialog_delete_btn(self):
        if self.driver.click("delete_title_delete_btn", change_check={"wait_obj": "delete_title_delete_btn", "invisible": True}, retry=2, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("delete_title_delete_btn", timeout=2)
            el.send_keys(Keys.ENTER)

    def click_dialog_cancel_btn(self):
        if self.driver.click("dialog_cancel_btn", change_check={"wait_obj": "dialog_cancel_btn", "invisible": True}, retry=2, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("dialog_cancel_btn", timeout=2)
            el.send_keys(Keys.ENTER)

    def click_dialog_share_btn(self):
        self.driver.click("dialog_share_btn", change_check={"wait_obj": "share_picker_popup"}, retry=2, delay=1)

    def click_dialog_save_btn(self):
        self.driver.click("dialog_save_btn", change_check={"wait_obj": "save_btn_on_save_as_dialog"}, retry=2, delay=1)

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

    def click_language_dropdown_listitem(self):
        self.driver.click("language_dropdown_listitem")
        
    # ---------------- save as dialog (windows popup)---------------- #   
    def click_save_as_dialog_save_btn(self):
        self.driver.click("save_btn_on_save_as_dialog") 

    def click_save_as_dialog_cancel_btn(self):
        self.driver.click("dialog_cancel_btn") 

    def get_the_saved_file_path(self):
        """
        get the saved file fath
        """
        return self.driver.get_attribute("file_saved_link", attribute="Name")

    def select_file_type_listitem(self, name):
        # if verfiy adv scan save dialog, the dialog is at the bottom, need swipe up to find file type.
        if self.driver.wait_for_object("filename_text",raise_e=False) is False and self.driver.driver_type.lower() == "windows":
            self.driver.swipe("filename_text", direction="up", distance=3)
        sleep(2)
        self.select_file_type_dropdown()
        self.driver.click("filetype_list_item", format_specifier=[name], change_check={"wait_obj": "filetype_list", "invisible": True}, retry=2, delay=1)

    def enter_folder_save_path(self, path):
        self.driver.send_keys("folder_edit", path) 
        sleep(2)

    # ---------------- share picker popup---------------- # 
    def dismiss_share_picker_popup(self):
        if self.verify_share_email_dialog(raise_e=False):
            self.click_share_email_dialog_close_btn()
        else:
            self.driver.send_keys("share_picker_popup", Keys.ESCAPE)

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
        self.driver.click("file_type_searchable_pdf")

    def select_file_type_dropdown(self):
        self.driver.click("file_type_dropdown", change_check={"wait_obj": "filetype_list"}, retry=4, delay=1)

    def select_advanced_presets_dropdown(self):
        self.driver.click("advanced_presets_dropdown", change_check={"wait_obj": "advanced_presets_list"}, retry=2, delay=1)

    def select_compression_dropdown(self):
        self.driver.click("compression_dropdown", change_check={"wait_obj": "compression_list"}, retry=2, delay=1)

    def get_compression_dropdown_value(self, raise_e=True):
        return self.driver.wait_for_object("compression_dropdown", raise_e=raise_e).text

    def select_compression_listitem(self, name):
        """
        @param dropdown:
            - None
            - Low
            - Medium
            - High
        """
        self.select_compression_dropdown()
        self.verify_dropdown_listitem(name).click()

    def click_save_text(self):
        self.driver.click("save_title")

    def click_install_new_language_btn(self):
        self.driver.click("install_language_btn")

    def click_install_new_language_link(self):
        self.scroll_to_element("install_new_language_link", direction="down", distance=6)
        self.driver.click("install_new_language_link")

    def choose_new_language_option(self):
        self.driver.click("click_new_language_option")

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
            self.driver.click("smart_file_name_toggle")
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

    # ---------------- add password on save dialog ---------------- #
    def click_add_password_toggle(self):
        if self.driver.driver_type.lower() == "windows" and self.driver.wait_for_object("add_password_protection_toggle", raise_e=False):
            self.driver.swipe("file_name_combo_box_edit", direction="down", distance=10)
        self.driver.click("toggle_switch")

    def input_password(self, password):
        self.driver.send_keys("input_password_box", password)

    def select_edge_to_open_file(self):
        if self.driver.wait_for_object("select_app_open_file_title", raise_e=False):
            self.driver.click("select_edge")
            self.driver.click("just_once")

    def input_password_with_password_pdf(self, password):
        self.driver.send_keys("password_pdf_input_box", password)

    def open_password_file(self):
        self.driver.click("open_password_file_btn")

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

    def click_edit_cancel_btn(self):
        self.driver.click("edit_cancel_btn")

    def click_crop_item_btn(self, value):
        self.driver.click("dynamic_crop_item", format_specifier=[value])

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

    def click_redo_btn(self):
        sleep(3)
        self.driver.click("redo_btn")

    def click_crop_item_btn(self, value):
        self.driver.click("dynamic_crop_item", format_specifier=[value])

    def change_adjust_contrast_edit_value(self, value):
        self.driver.click("adjust_contrast_edit")
        self.driver.send_keys("adjust_contrast_edit", value, press_enter=True)
        self.verify_adjust_contrast_edit_value(value)

    def click_filters_item(self):
        self.driver.click("filters_item")

    def swipe_filter_item(self, filter):
        swipe_dict = {"Noir": "noir_opt", "Seafarer": "seafarer_opt"}

        for key, value in swipe_dict.items():
            if filter == key:
                self.driver.swipe(value, distance=2)
                break

    def click_dynamic_text_item(self, value, raise_e=True):
        return self.driver.click("dynamic_text_item", format_specifier=[value], raise_e=raise_e)
   
    def change_filter_intensity_vaule(self, value):
        self.driver.click("filter_intensity_edit")
        self.driver.send_keys("filter_intensity_edit", value, press_enter=True)
        self.verify_filter_intensity_value(value)

    def click_reset_filters_btn(self):
        self.driver.click("reset_filters_btn")

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
            self.click_crop_item_btn('Letter')

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

    def click_center_image(self):
        self.driver.click("canvas_image")

    def click_edit_up_rotate_btn(self):
        self.driver.click("canvas_image")
        sleep(1)
        # self.driver.click("up_rotate_image")
        el = self.driver.wait_for_object("canvas_image")
        self.driver.click_by_coordinates_with_offset(el, x_offset=0.251, y_offset=0.99)

    def click_edit_down_rotate_btn(self):
        self.driver.click("canvas_image")
        sleep(1)
        # self.driver.click("down_rotate_image")
        el = self.driver.wait_for_object("canvas_image")
        self.driver.click_by_coordinates_with_offset(el, x_offset=0.327, y_offset=0.993)

    def click_edit_left_rotate_btn(self):
        self.driver.click("canvas_image")
        sleep(1)
        # self.driver.click("left_rotate_image")
        el = self.driver.wait_for_object("canvas_image")
        self.driver.click_by_coordinates_with_offset(el, x_offset=0.674, y_offset=0.993)

    def click_edit_right_rotate_btn(self):
        self.driver.click("canvas_image")
        sleep(1)
        # self.driver.click("right_rotate_image")
        el = self.driver.wait_for_object("canvas_image")
        self.driver.click_by_coordinates_with_offset(el, x_offset=0.756, y_offset=0.993)

    def add_some_text(self, input_t):
        self.driver.click("add_text_btn")
        # set Font Color to red
        self.driver.click("dynamic_front_color", format_specifier=['red'])
        # set Background Color to black
        self.driver.click("dynamic_background_color", format_specifier=['black'])
        self.driver.click("font_size_edit")
        self.driver.send_keys("font_size_edit", '100', press_enter=True)
        # click Pencil icon to edit
        # el = self.driver.wait_for_object("canvas_image")
        # self.driver.click_by_coordinates_with_offset(el, x_offset=0.441, y_offset=0.370)
        # self.verify_input_text_dialog()
        # self.driver.click("input_text_edit")
        # self.driver.send_keys("input_text_edit", input_t, press_enter=True)
        # self.driver.click("text_done_btn")
        self.driver.click("myhp_window")
        sleep(1)
        
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

    # ------------File Format Error popup-------------- #
    def click_file_format_error_close_btn(self):
        self.driver.click("file_format_error_close_btn", change_check={"wait_obj": "file_format_error_title", "invisible": True}, retry=2, delay=1) 

    def click_start_new_scan_btn(self):
        self.driver.click("start_new_scan_btn", change_check={"wait_obj": "start_new_scan_btn", "invisible": True}, retry=2, delay=1) 

    # ------------Share email dialog popup-------------- #
    def click_share_email_dialog_close_btn(self):
        self.driver.click("share_email_dialog_close_btn")

    # ------------Adv scan Text Extract-------------- #
    def click_text_extract_btn(self):
        self.driver.click("text_extract_btn")

    def click_copy_all_btn(self):
        self.driver.click("copy_all_btn")

    # ------------adv_scan with scribble function...-------------- # 
    def click_add_mark_btn(self):
        self.driver.click("add_mark_btn")

    def click_adv_scribble_btn(self):
        self.driver.click("scribble_btn", change_check={"wait_obj": "scribble_btn", "invisible": True})

    def click_done_btn_on_scribble_screen(self):
        self.driver.click("scribble_done_btn")

    # ------------add new mark screen-------------- #
    def click_mark_line_image(self):
        self.driver.click("mark_line_image")

    def click_thin_btn(self):
        self.driver.click("thin_btn")

    def click_medium_btn(self):
        self.driver.click("medium_btn")

    def click_thick_btn(self):
        self.driver.click("thick_btn")

    def click_text_btn(self):
        self.driver.click("text_btn")

    def click_new_mark_done_btn(self):
        self.driver.click("new_mark_done_btn")

    def click_new_mark_cancel_btn(self): 
        self.driver.click("new_mark_cancel_btn")

    def enter_anything_in_signature_input_box(self, text):
        self.driver.send_keys("signature_input", text, press_enter=True, slow_type=True)

    # ------------Text Edit screen-------------- #
    def edit_input_area(self, text, action="clear"):
        """
        Edit text in the input area with different actions.
        action (str): The action to perform - "add", "clear"
        """
        input_element = self.driver.wait_for_object("edit_input_area", timeout=10)
        
        if action == "clear":
            # delete all existing text
            input_element.clear()
            sleep(1)
        elif action == "add":
            # Add text to existing content
            self.driver.send_keys("edit_input_area", text, slow_type=True)

    # ------------save type list item-------------- #   

    def click_open_file_btn(self):
        self.driver.click("open_file_btn")
   
    def scroll_to_element(self, el=False, direction="down", distance=1):
        if self.driver.driver_type.lower() == "windows":
            if el:
                self.driver.swipe(el, direction=direction, distance=distance)
            else:
                self.driver.swipe(direction=direction, distance=distance)
            time.sleep(1)
    
    def click_next_btn(self):
        """
        ID Card next screen
        """
        self.driver.click("next_btn")

    def click_start_button(self):
        self.driver.click("start_button")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_scan_btn(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("scan_btn", timeout=timeout, raise_e=raise_e)

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

    def verify_scanner_screen(self, timeout=20, card=False, adv_scan=False, raise_e=True):
        """
        Verify the current screen is Scanner screen.
        """
        self.driver.wait_for_object("_shared_hpx_title_text", raise_e=raise_e, timeout=timeout)
        if self.driver.session_data['request'].config.getoption("--stack") not in ["rebrand_production"]:
            self.driver.wait_for_object("_shared_app_version_text", raise_e=raise_e, timeout=timeout)
        if card:
            self.verify_card_scan_preview_screen()
        else:
            self.driver.wait_for_object("text_1_scanner", raise_e=raise_e, timeout=timeout)
            self.driver.wait_for_object("text_2_scanner", raise_e=raise_e)
            self.driver.wait_for_object("text_3_scanner", raise_e=raise_e)
            self.driver.wait_for_object("text_4_scanner", raise_e=raise_e)
            self.driver.wait_for_object("text_5_scanner", raise_e=raise_e)
        self.driver.wait_for_object("gear_icon", raise_e=raise_e)
        self.driver.wait_for_object("auto_enhancement_icon", raise_e=raise_e)
        self.driver.wait_for_object("source_item", raise_e=raise_e)
        self.driver.wait_for_object("source_dropdown", raise_e=raise_e)
        if adv_scan:
            self.driver.wait_for_object("advanced_presets_list", raise_e=raise_e)
            self.driver.wait_for_object("advanced_presets_dropdown", raise_e=raise_e)
        else:
            self.driver.wait_for_object("presets_item", raise_e=raise_e)
            self.driver.wait_for_object("presets_dropdown", raise_e=raise_e)
        self.driver.wait_for_object("output_item", raise_e=raise_e)
        self.driver.wait_for_object("output_dropdown", raise_e=raise_e)
        # self.driver.wait_for_object("compression_item", raise_e=raise_e)
        # self.driver.wait_for_object("compression_dropdown", raise_e=raise_e)
        self.driver.wait_for_object("resolution_item", raise_e=raise_e)
        self.driver.wait_for_object("resolution_dropdown", raise_e=raise_e)
        self.driver.wait_for_object("reset_settings_btn", raise_e=raise_e)
        self.driver.wait_for_object("scan_btn", raise_e=raise_e)
        if self.driver.wait_for_object("source_scanner_glass", raise_e=False):
            self.driver.wait_for_object("scan_area_item", raise_e=raise_e)
            self.driver.wait_for_object("scan_area_dropdown", raise_e=raise_e)
            self.verify_detect_edges_item()
            self.verify_preview_button()
        if self.driver.wait_for_object("source_document_feeder", raise_e=False):
            self.driver.wait_for_object("page_size_item", raise_e=raise_e)
            self.driver.wait_for_object("page_size_dropdown", raise_e=raise_e)
            if not self.verify_2_sided_item(raise_e=False):
                logging.info("Printer does not support ADF 2 Sided scan")
            self.verify_preview_button(invisible=True)

    def get_scan_job_num(self):
        return int(self.driver.get_attribute("total_num", attribute="Name"))
            
    def verify_preview_button(self, invisible=False, raise_e=True):
        return self.driver.wait_for_object("preview_btn", invisible=invisible, raise_e=raise_e)

    def verify_source_list_items(self, timeout=2, raise_e=True):
        """
        Verify the list item display after clicking source combobox.
        """
        return self.driver.wait_for_object("source_list", timeout=timeout, raise_e=raise_e)

    def verify_scan_area_list(self, timeout=2, raise_e=True):
        """
        Verify the list item display after clicking scan area combobox.
        """
        return self.driver.wait_for_object("scan_area_list", timeout=timeout, raise_e=raise_e)

    def verify_page_size_list(self, timeout=2, raise_e=True):
        """
        Verify the list item display after clicking page size combobox.
        """
        return self.driver.wait_for_object("page_size_list", timeout=timeout, raise_e=raise_e)
    
    def verify_file_type_list(self, timeout=2, raise_e=True):
        """
        Verify the list item display after clicking file type combobox on save dialog.
        """
        return self.driver.wait_for_object("file_type_list", timeout=timeout, raise_e=raise_e)

    def verify_file_type_list_item_display(self, name, timeout=2, raise_e=True):
        """
        Verify the list item display after clicking file type combobox.
        """
        return self.driver.wait_for_object("filetype_list_item",format_specifier=[name], timeout=timeout, raise_e=raise_e)
    
    def verify_resolution_list(self, timeout=2, raise_e=True):
        """
        Verify the list item display after clicking resolution combobox.
        """
        return self.driver.wait_for_object("resolution_list", timeout=timeout, raise_e=raise_e)

    def verify_resolution_list_items(self, glass_scan=True, raise_e=True):
        """
        Verify the list item display after clicking resolution combobox.
        """
        self.driver.wait_for_object("resolution_list_item_300dpi", raise_e=raise_e)
        if glass_scan:
            self.driver.wait_for_object("resolution_list_item_600dpi", raise_e=raise_e)
            self.driver.wait_for_object("resolution_list_item_1200dpi", raise_e=raise_e)
            self.driver.swipe("resolution_list", direction="up", distance=2)
        self.driver.wait_for_object("resolution_list_item_75dpi", raise_e=raise_e)
        self.driver.wait_for_object("resolution_list_item_150dpi", raise_e=raise_e)

    def verify_2_sided_item(self, raise_e=True):
        """
        Verify the 2-Sided item display
        """
        return self.driver.wait_for_object("2_sided_item", raise_e=raise_e) and \
                self.driver.wait_for_object("2_sided_checkbox", raise_e=raise_e)

    def verify_detect_edges_item(self, raise_e=True):
        """
        Verify the Detect Edges item display
        """
        return self.driver.wait_for_object("detect_edges_item", raise_e=raise_e) and \
                self.driver.wait_for_object("detect_edges_checkbox", raise_e=raise_e)

    def verify_all_the_button_on_preview(self):
        """
        Verify all the button on Preview screen.
        """
        self.driver.wait_for_object("print_btn", timeout=30)
        self.driver.wait_for_object("save_btn", timeout=30)
        self.driver.wait_for_object("share_btn", timeout=30)

    def verify_source_dropdown_enabled(self):
        """
        Verify the source dropdown enabled status.
        """
        return self.driver.wait_for_object("source_dropdown").is_enabled()

    def verify_rotate_button_display(self):
        """
        Verify Rotate button on Preview screen
        """
        return self.driver.wait_for_object("rotate_icon")

    def verify_resolution_value(self, value):
        """
        Verify the resolution dropdown display
        """
        if not self.driver.wait_for_object("dynamic_resolution_value", format_specifier=[value], raise_e=False):
            el = self.driver.wait_for_object("resolution_list")
            el.send_keys(Keys.PAGE_DOWN)
            self.driver.wait_for_object("dynamic_resolution_value", format_specifier=[value])

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

    def verify_dropdown_listitem(self, name, timeout=30, raise_e=True):
        return self.driver.wait_for_object("dynamic_listitem", format_specifier=[name], displayed=False, raise_e=raise_e)

    def verify_auto_enhancement_panel(self):
        """
        Verify "Auto-Enhancement" panel.
        """
        self.driver.wait_for_object("auto_enhancements_text")
        self.driver.wait_for_object("auto_enhancements_sub_text")
        self.driver.wait_for_object("auto_enhancements_toggle")
        self.driver.wait_for_object("auto_orientation_text")
        self.driver.wait_for_object("auto_orientation_sub_text")
        self.driver.wait_for_object("auto_orientation_toggle")

    def verify_auto_enhancement_panel_setting_by_default(self):
        """
        Verify both "Auto-Enhancement" toggle is 'on' and "Auto-Orientation" toggle is 'off' by default.
        """
        self.verify_auto_enhancement_panel()
        assert self.verify_auto_enhancement_state() == "1"
        assert self.verify_auto_orientation_state() == "0"

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

    def verify_auto_orientation_state(self):
        """
        Verify "Auto-Orientation" toggle is 'on' or 'off'
        """
        toggle_1 = self.driver.wait_for_object("auto_orientation_toggle")
        return toggle_1.get_attribute("Toggle.ToggleState")

    def verify_auto_enhancement_state(self):
        """
        Verify "Auto-Enhancement" toggle is 'on' or 'off'
        """
        toggle_1 = self.driver.wait_for_object("auto_enhancements_toggle")
        return toggle_1.get_attribute("Toggle.ToggleState")

    def verify_auto_heal_is_on(self):
        """
        Verify "Auto-Heal" toggle is 'on'
        """
        toggle_1 = self.driver.wait_for_object("auto_heal_toggle")
        assert toggle_1.get_attribute("Toggle.ToggleState") == "1"

    def verify_detect_edges_checkbox_status(self, off=True):
        """
        Verify Detect Edges checkbox status
        """
        return self.driver.get_attribute("detect_edges_checkbox", attribute="Toggle.ToggleState")

    def verify_2_sided_checkbox_status(self, off=True):
        """
        Verify 2-Sided checkbox status
        """
        toggle= self.driver.wait_for_object("2_sided_checkbox")
        if off:
            assert toggle.get_attribute("Toggle.ToggleState") == "0"
        else:
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

    def verify_keep_resolution_box_behavior(self, behavior):
        """
        Verify keep resolution box behavior
        """
        toggle = self.driver.wait_for_object("keep_resolution_box", displayed=False)
        if behavior == "unchecked":
            assert toggle.get_attribute("Toggle.ToggleState") == "0"
        elif behavior == "checked":
            assert toggle.get_attribute("Toggle.ToggleState") == "1"

    def verify_scanner_preview_screen(self, timeout=5, raise_e=True):
        """
        Verify the Scanner preview screen after clicking Preview btn on scanner screen
        """
        # preview image cannot locate now, will update when available.
        # self.driver.wait_for_object("scanner_preview_image", timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("text_1_scanner", timeout=timeout, invisible=True, raise_e=raise_e)
        self.driver.wait_for_object("text_2_scanner", invisible=True, raise_e=raise_e)
        self.driver.wait_for_object("text_3_scanner", invisible=True, raise_e=raise_e)
        self.driver.wait_for_object("text_4_scanner", invisible=True, raise_e=raise_e)
        self.driver.wait_for_object("text_5_scanner", invisible=True, raise_e=raise_e)
 
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

    def verify_scan_canceled_dialog(self, timeout=40,raise_e=True):
        """
        Verify the current screen is scan canceled dialog
        """
        return self.driver.wait_for_object("scan_canceled_title", timeout=timeout,raise_e=raise_e) and\
            self.driver.wait_for_object("close_btn", timeout=timeout,raise_e=raise_e)

    def verify_scanning_screen(self, timeout=60, invisible=True, raise_e=True):
        """
        Verify the current screen is scanning screen
        Note: This screen only shows for  about 3 seconds with simulator printer.
        """
        if invisible:
            # Wait for screen to disappear
            return self.driver.wait_for_object("scanning_text", timeout=timeout, invisible=invisible, raise_e=raise_e) and \
                    self.driver.wait_for_object("cancel_btn", invisible=invisible, raise_e=raise_e)
        else:
            # For checking if screen is visible
            short_timeout = min(5, timeout)
            return self.driver.wait_for_object("scanning_text", timeout=short_timeout, invisible=invisible, interval=0.5, raise_e=raise_e) and \
                    self.driver.wait_for_object("cancel_btn", timeout=short_timeout, invisible=invisible, interval=0.5, raise_e=raise_e)
 

    def verify_back_arrow(self, timeout=10, raise_e=True):
        """
        Verify Back arrow
        """
        return self.driver.wait_for_object("back_arrow", timeout=timeout, raise_e=raise_e)

    def verify_previewing_screen(self, timeout=30, raise_e=True):
        """
        Verify the current screen is previewing screen
        """
        return self.driver.wait_for_object("previewing_text", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("cancel_btn", raise_e=raise_e)

    def verify_scan_result_screen(self, timeout=60, raise_e=True):
        """
        Verify the current screen is scan result
        """
        return self.driver.wait_for_object("save_btn", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("add_pages_btn", raise_e=raise_e)

    def verify_image_preview(self):
        """
        Verify the Gallery view screen shows
        """
        self.driver.wait_for_object("image_edit_btn")
        self.driver.wait_for_object("image_rotate_btn")
        self.driver.wait_for_object("image_replace_btn")
        self.driver.wait_for_object("image_delete_btn")
    
    def verify_preview_with_single_image(self):
        self.verify_image_preview()
        assert self.driver.wait_for_object("gallery_image", raise_e=False) is False
        assert self.driver.wait_for_object("thumbnail_image", raise_e=False) is False
    
    def verify_preview_with_multi_image(self, num=0):
        """
        Verify the Gallery view screen shows
        """
        self.verify_image_preview()
        self.verify_gallery_icon()
        self.verify_thumbnail_icon()
        for i in range(num):
            self.driver.wait_for_object("dynamic_item_btn", format_specifier=[str(i+1)])

    def verify_delete_selected_images_dialog(self, raise_e=True):
        """
        Verify the current screen is "Delete selected images?"dialog
        """
        return self.driver.wait_for_object("delete_title_delete_btn", raise_e=raise_e) and\
            self.driver.wait_for_object("cancel_btn", raise_e=raise_e) 

    def verify_gallery_icon(self, raise_e=True):
        """
        Verify Gallery icon shows or not.
        """
        return self.driver.wait_for_object("gallery_image", raise_e=raise_e)

    def verify_thumbnail_icon(self, raise_e=True):
        """
        Verify Thumbnail icon shows or not.
        """
        return self.driver.wait_for_object("thumbnail_image", raise_e=raise_e)
    
    def verify_thumbnail_view_screen(self, num=0):
        """
        Verify the current screen is thumbnail view 
        """
        self.driver.wait_for_object("thumbnail_edit_btn")
        # self.driver.wait_for_object("thumbnail_redact_btn")
        # self.driver.wait_for_object("thumbnail_scribble_btn")
        # self.driver.wait_for_object("thumbnail_text_extract_btn")
        self.driver.wait_for_object("thumbnail_rotate_btn")
        self.driver.wait_for_object("thumbnail_delete_btn")
        self.driver.wait_for_object("thumbnail_select_all_btn")
        for i in range(num):   
            self.verify_thumbnail_item(num=i+1)

    def verify_thumbnail_scribble_btn_status(self, enabled=True):
        """
        Verify Thumbnail Scribble button status with multi pages.
        """
        button = self.driver.wait_for_object("thumbnail_scribble_btn")
        if enabled:
            assert button.get_attribute("IsEnabled").lower() == "true"
        else:
            assert button.get_attribute("IsEnabled").lower() == "false"

    def verify_thumbnail_select_all_btn_attr(self):
        assert self.driver.wait_for_object("thumbnail_deselect_all_btn", raise_e=False) is False
        assert self.driver.get_attribute("thumbnail_select_all_btn", attribute="IsEnabled").lower() =="true"
    
    def verify_thumbnail_deselect_all_btn_attr(self):
        assert self.driver.wait_for_object("thumbnail_select_all_btn", raise_e=False) is False
        assert self.driver.get_attribute("thumbnail_deselect_all_btn", attribute="IsEnabled").lower() =="true"

    def verify_thumbnail_item(self, num, check=False):
        self.driver.click("myhp_window")
        sleep(1)
        if check:
            value = 'Checkmark ' + str(num)
        else:
            value = str(num)
        self.driver.wait_for_object("dynamic_item_btn", format_specifier=[value])
    
    def verify_file_saved_dialog(self):
        """
        Verify File has been saved
        """
        self.driver.wait_for_object("file_saved_link")
        self.driver.wait_for_object("open_file_btn")
        self.driver.wait_for_object("close_btn")

    def verify_start_a_new_scan_without_saving_dialog(self, raise_e=True):
        """
        Preview -> New Scan  -> "Start a new scan without saving?"
        """
        return self.driver.wait_for_object("start_a_new_scan_title", raise_e=raise_e) and \
            self.driver.wait_for_object("start_a_new_scan_body", raise_e=raise_e) and \
            self.driver.wait_for_object("start_new_scan_btn", raise_e=raise_e) and \
            self.driver.wait_for_object("cancel_btn", raise_e=raise_e)

    def verify_pro_scan_result_screen(self, timeout=30, raise_e=True):
        """
        Verify the current screen is scan result for pro account
        """
        return self.driver.wait_for_object("redact_btn", timeout=timeout, raise_e=raise_e)

    def verify_processing_scan_dialog(self, timeout=30):
        """
        Verify the current screen is Processing Scan dialog
        """
        self.driver.wait_for_object("processing_scan_title", timeout=timeout)
        self.driver.wait_for_object("cancel_btn", timeout=timeout)
        self.driver.wait_for_object("processing_scan_title", timeout=timeout, invisible=True)

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
    
    def verify_save_dialog(self, invisible=False, timeout=3, adv_scan=False):
        """
        Verify the current screen is Save dialog
        """
        self.driver.wait_for_object("save_title", invisible=invisible, timeout=timeout)
        self.driver.wait_for_object("dialog_cancel_btn", invisible=invisible)
        self.driver.wait_for_object("dialog_save_btn", invisible=invisible)
        self.driver.wait_for_object("filename_text", invisible=invisible)
        self.driver.wait_for_object("filetype_text", invisible=invisible)
        sleep(2)
        if adv_scan:
            self.driver.click("save_title")
            self.scroll_to_element(direction="down", distance=6)
            self.driver.wait_for_object("compression_item", invisible=invisible)
            self.driver.wait_for_object("select_language_combobox", invisible=invisible)
            self.driver.wait_for_object("install_new_language_link", invisible=invisible)
            self.driver.wait_for_object("add_password_protection_toggle", invisible=invisible)

    def verify_share_dialog(self, invisible=False, timeout=3):
        """
        Verify the current screen is Share dialog
        """
        self.driver.wait_for_object("share_title", invisible=invisible, timeout=timeout)
        self.driver.wait_for_object("dialog_cancel_btn", invisible=invisible)
        self.driver.wait_for_object("dialog_share_btn", invisible=invisible)
        self.driver.wait_for_object("filename_text", invisible=invisible)
        self.driver.wait_for_object("filetype_text", invisible=invisible)
        self.driver.wait_for_object("compression_item", invisible=invisible)

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
        logging.info(file_name)
        return file_name

    def get_save_as_dialog_current_file_name(self):
        """
        Get current File Name 
        """
        file_name = self.driver.get_attribute("file_name_combo_box_edit", attribute="Value.Value")
        return file_name

    def get_save_as_dialog_current_file_type(self):
        """
        Get current File Type
        """
        file_tpye = self.driver.get_attribute("file_type", attribute="Value.Value")
        return file_tpye

    def verify_detecting_edges_screen(self, raise_e=True):
        """
        Verify the current screen is Detect Edges
        """
        return self.driver.wait_for_object("detecting_edges_text", timeout=30, invisible=True, raise_e=raise_e)

    def verify_import_screen(self, timeout=60, raise_e=True):
        """
        Verify the current screen is Import screen and wait for import_done_btn to be enabled
        """
        self.driver.wait_for_object("import_done_btn", clickable=True, timeout=timeout, raise_e=raise_e)
        self.driver.wait_for_object("import_screen_options_text", raise_e=raise_e)
        self.driver.wait_for_object("import_screen_auto_group", raise_e=raise_e)
        self.driver.wait_for_object("import_screen_full_group", raise_e=raise_e)
        
    def verify_exit_without_saving_dialog(self, raise_e=True):
        """
        Verify the current screen is Exit without saving dialog
        """
        return self.driver.wait_for_object("exit_without_saving_title", raise_e=raise_e) and \
        self.driver.wait_for_object("yes_btn", raise_e=raise_e) and \
        self.driver.wait_for_object("no_btn", raise_e=raise_e)


    def verify_file_format_error_dialog(self):
        """
        Verify the current screen is File Format Error dialog
        """
        self.driver.wait_for_object("file_format_error_title")
        self.driver.wait_for_object("file_format_error_body")
        self.driver.wait_for_object("file_format_error_close_btn")
        

    def verify_large_file_error_dialog(self):
        """
        Verify the current screen is The file could not be opened dialog
        """
        assert self.driver.get_attribute("error_title", timeout=10, attribute="Name") =="The file could not be opened."

    def verify_multi_pages_scan_result_screen(self, page_num):
        """
        Verify the preview screen when multiple pages are scanned.
        """
        for i in range(page_num):
            self.driver.wait_for_object("multi_add_pages_btn", format_specifier=[i+1])

    def verify_all_the_button_can_be_used(self):
        """
        Verify that all features are in normal use
        """
        assert self.driver.get_attribute("delete_btn", attribute="IsEnabled").lower() =="true"
        assert self.driver.get_attribute("rotate_right_btn", attribute="IsEnabled").lower() =="true"
        assert self.driver.get_attribute("rotate_left_btn", attribute="IsEnabled").lower() =="true"

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

    def verify_the_saved_file_name_is_correct(self, file_name, multi_i=False):
        """
        Verify The saved file name is correct
        """
        file_path = self.driver.get_attribute("file_saved_link", attribute="Name")
        if not multi_i:
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
        self.driver.wait_for_object("edit_done_btn")   
        self.driver.wait_for_object("edit_cancel_btn")

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
        assert self.verify_filter_intensity(raise_e=False) is False

    def verify_filter_intensity(self, raise_e=True):
        return self.driver.wait_for_object("filter_intensity_text", raise_e=raise_e) and\
        self.driver.wait_for_object("filter_intensity_slider", raise_e=raise_e) and\
        self.driver.wait_for_object("reset_filters_btn", raise_e=raise_e)

    def verify_filter_intensity_value(self, value):
        assert self.driver.get_attribute("filter_intensity_edit", attribute="Value.Value") == value

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
        self.driver.wait_for_object("scanned_number_on_scanner")
        self.driver.wait_for_object("text_1_replace")
        self.driver.wait_for_object("text_2_scanner")
        self.driver.wait_for_object("text_3_replace")
        self.driver.wait_for_object("text_4_scanner")
        self.driver.wait_for_object("text_5_scanner")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("scan_and_replace_button")
    
    def verify_replace_screen_with_id_card(self):
        """
        Verify the current screen is Replace screen with advanced scan
        """
        self.verify_scan_btn()
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("text_2_scanner")
        self.driver.wait_for_object("text_4_scanner")
        self.driver.wait_for_object("id_card_replace_image")
        self.driver.wait_for_object("id_card_replace_text_1")
        self.driver.wait_for_object("id_card_replace_text_2")

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

    def verify_left_arrow_btn_display(self, raise_e=True):
        """
        Verify left arrow button display
        """
        return self.driver.wait_for_object("left_arrow_btn", raise_e=raise_e)

    def verify_right_arrow_btn_display(self, raise_e=True):
        """
        Verify right arrow button display
        """
        return self.driver.wait_for_object("righ_arrow_btn", raise_e=raise_e)

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

    def get_file_type(self):
        return self.driver.get_attribute("file_type_dropdown", attribute="Name")

    def verify_file_type(self, file_type):
        """
        Verify the JPG is selected as default file type if the files are recognized as photo.
        Verify the PDF is selected as default file type if the files are recognized as document.
        @param file_type:
            - jpg
            - pdf
        """
        if file_type == "jpg":
            assert self.get_file_type() == "Image(*.jpg)"

        if file_type == "pdf":
            assert self.get_file_type() == "Basic PDF"

    
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

    def verify_downloading_language_dialog(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("downloading_language_dialog_title", timeout=timeout, raise_e=raise_e)
    
    def verify_language_failed_to_download(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("failed_to_download_title", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("retry_btn", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("cancel_btn", timeout=timeout, raise_e=raise_e)

    def verify_doc_language_text_not_display(self):
        if self.driver.wait_for_object("doc_language_text", raise_e=False):
            raise NoSuchElementException("Document Language option does show")
        return True

    def verify_smart_file_name_text_not_display(self):
        if self.driver.wait_for_object("smart_file_name", raise_e=False):
            raise NoSuchElementException("Smart File Name does show")
        return True

    def verify_smart_file_name_changes(self,name_part):
        filename = self.driver.get_attribute("filename_group", attribute="Name")
        assert name_part in filename

    def verify_redaction_webview_screen(self):
        self.driver.wait_for_object("redaction_text")

    def verify_processing_pages_dialog(self):
        self.driver.wait_for_object("processing_pages_title")

    def verify_adjust_contrast_edit_value(self, value='0'):
        assert self.driver.get_attribute("adjust_contrast_edit", attribute="Value.Value") == value

    def verify_adjust_setting_default_value(self):
        assert self.driver.get_attribute("adjust_brigthtness_edit", attribute="Value.Value") == "0"
        assert self.driver.get_attribute("adjust_saturation_edit", attribute="Value.Value") == "0"
        self.verify_adjust_contrast_edit_value()
        assert self.driver.get_attribute("adjust_clarity_edit", attribute="Value.Value") == "0"
        assert self.driver.get_attribute("adjust_exposure_edit", attribute="Value.Value") == "0"
        assert self.driver.get_attribute("adjust_shadows_edit", attribute="Value.Value") == "0"
        assert self.driver.get_attribute("adjust_highlights_edit", attribute="Value.Value") == "0"
        assert self.driver.get_attribute("adjust_whites_edit", attribute="Value.Value") == "0"

    def verify_edit_text_setting_screen(self):
        self.driver.wait_for_object("add_text_btn", displayed=False)
        self.driver.wait_for_object("font_family_text", displayed=False)
        self.driver.wait_for_object("font_size_text", displayed=False)
        self.driver.wait_for_object("font_size_edit", displayed=False)
        self.driver.wait_for_object("alignment_text", displayed=False)
        self.driver.wait_for_object("font_color_text", displayed=False)
        self.driver.wait_for_object("background_color_text", displayed=False)
        self.driver.wait_for_object("line_spacing_text", displayed=False)
        self.driver.wait_for_object("line_spacing_slider", displayed=False)
        self.driver.wait_for_object("line_spacing_edit", displayed=False)

    def verify_add_text_dialog(self):
        self.driver.wait_for_object("pencil_image", displayed=False)
        self.driver.wait_for_object("doc_copy_alt_image", displayed=False)
        self.driver.wait_for_object("trash_image", displayed=False)

    def verify_input_text_dialog(self):
        self.driver.wait_for_object("input_text_title", displayed=False)
        self.driver.wait_for_object("input_text_edit", displayed=False)
        self.driver.wait_for_object("text_done_btn", displayed=False)
        self.driver.wait_for_object("text_cancel_btn", displayed=False)

    def verify_dynamic_text_item(self, value, timeout=3, raise_e=True):
        return self.driver.wait_for_object("dynamic_text_item", format_specifier=[value], timeout=timeout, raise_e=raise_e)

    def verify_font_family_combo_value(self, value):
        assert self.driver.get_attribute("font_family_combo", attribute="Value.Value") == value

    def verify_font_size_edit_value(self, value):
        assert self.driver.get_attribute("font_size_edit", attribute="Value.Value") == value

    def verify_line_spacing_edit_value(self, value):
        assert self.driver.get_attribute("line_spacing_edit", attribute="Value.Value") == value

    def verify_edit_makup_setting_screen(self):
        self.driver.wait_for_object("highlight_btn")
        self.driver.wait_for_object("white_out_btn")
        self.driver.wait_for_object("black_pen_btn")
        self.driver.wait_for_object("blue_pen_btn")
        self.driver.wait_for_object("red_pen_btn")
        self.driver.wait_for_object("reset_markup_btn")
        assert self.driver.get_attribute("markup_size", attribute="Value.Value") == "8"

    def verify_scanner_not_found_dialog(self, raise_e=True):
        return self.driver.wait_for_object("scanner_not_found_title", raise_e=raise_e) and\
        self.driver.wait_for_object("close_btn", raise_e=raise_e)
       
    def verify_scanner_problem_dialog(self):
        self.driver.wait_for_object("close_btn")
        assert self.driver.get_attribute("scan_canceled_title", attribute="Name") == 'Scanner Problem'
    
    def verify_thumbnail_view_images_display(self):
        self.driver.wait_for_object("thumbnail_view_images")

    def verify_mobile_fax_btn_does_not_show(self):
        if self.driver.wait_for_object("fax_btn", raise_e=False):
            raise NoSuchElementException("Mobile Fax button displays")
        return True

    def verify_shortcuts_btn_display(self, raise_e=True):
        return self.driver.wait_for_object("shortcuts_btn", raise_e=raise_e)

    def verify_shortcuts_order(self, name_1, name_2):
        """
        Check shortcuts name order
        """
        assert self.driver.get_attribute("shortcuts_order_1", attribute="Name") == "Start "+ name_2
        assert self.driver.get_attribute("shortcuts_order_2", attribute="Name") == "Start "+ name_1

    def verify_camera_tab_not_display(self):
        assert self.driver.wait_for_object("camera_text", raise_e=False) is False

    def verify_exit_without_saving_dialog_for_edit_screen(self, raise_e=True):
        """
        Verify the current screen is Exit without saving dialog in Edit screen
        """
        return self.driver.wait_for_object("exit_without_saving_title", raise_e=raise_e) and\
        self.driver.wait_for_object("edit_screen_exit_without_saving_text", displayed=False, raise_e=raise_e)  and\
        self.driver.wait_for_object("exit_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e)

    def verify_share_email_dialog(self, raise_e=True):
        return self.driver.wait_for_object("share_email_dialog_close_btn", raise_e=raise_e)

    def verify_share_picker_popup(self, invisible=False):
        self.driver.wait_for_object("share_picker_popup", invisible=invisible)

    # ------------We're having trouble...-------------- #
    def verify_we_are_having_trouble_dialog(self, timeout=60):
        self.driver.wait_for_object("ipp_we_are_having_text", timeout=timeout)
        self.driver.wait_for_object("ipp_try_again_btn", timeout=timeout)
        self.driver.wait_for_object("ipp_cancel_btn", timeout=timeout)

    # ------------printer not available-------------- #
    def verify_printer_not_available_screen(self, timeout=20):
        self.driver.wait_for_object("printer_not_available_title", timeout=timeout)
        self.driver.wait_for_object("import_your_file_btn", timeout=timeout)

    # ------------File picker dialog for import flow-------------- #
    def verify_file_picker_dialog(self, timeout=30):
        self.driver.wait_for_object("file_picker_dialog", timeout=timeout)
    
    def input_file_name(self, _file):
        self.driver.send_keys("file_picker_dialog_file_name_combo_box_edit", _file, press_enter=True)

    def select_file_picker_dialog_print_btn(self):
        self.driver.click("file_picker_dialog_print_btn")

    def select_file_picker_dialog_cancel_btn(self):
        self.driver.click("file_picker_dialog_cancel_btn")

    def check_dialog_file_name_text(self, file_name):
        if file_name =="photo":
            assert "Photo_" in self.get_current_file_name() 
        if file_name =="document":
            assert "Document_" in self.get_current_file_name()
        if file_name =="receipt":
            assert "Receipt_" in self.get_current_file_name() 
        if file_name =="businessCard":
            assert "BusinessCard_" in self.get_current_file_name()
        if file_name =="handwritten":
            assert "Handwritten_" in self.get_current_file_name() 

    # ------------Adv scan Searchable PDF.-------------- #
    def verify_file_type_listitem_options(self):
        self.select_file_type_dropdown()
        self.driver.wait_for_object("file_type_basic_pdf")
        self.driver.wait_for_object("file_type_image")
        self.driver.wait_for_object("file_type_searchable_pdf")
        self.driver.wait_for_object("file_type_plain_text")
        if self.driver.driver_type.lower() == "windows":
            self.driver.swipe("file_type_plain_text", direction="down", distance=2)
        self.driver.wait_for_object("file_type_word_document")

        # ------------adv_scan with scribble function...-------------- # 
    def verify_adv_scribble_btn_display(self, raise_e=True):
        return self.driver.wait_for_object("scribble_btn", raise_e=raise_e)

    def verify_preview_scribble_btn_enable(self):
        assert self.driver.get_attribute("scribble_btn", attribute="IsEnabled").lower() =="true"

    def verify_add_mark_btn_display(self, raise_e=True):
        return self.driver.wait_for_object("add_mark_btn", raise_e=raise_e)
    
    def verify_scribble_screen(self, timeout=30, raise_e=True):
        # Verify the Scribble screen elements are displayed
        elements = ["add_mark_btn", "scribble_done_btn", "new_mark_cancel_btn"]
        for element in elements:
            self.driver.wait_for_object(element, timeout=timeout, raise_e=raise_e)
        return True
    
# ------------add new mark screen-------------- #
    def verify_add_new_mark_screen(self, raise_e=True):
        # Verify the Add New Mark screen elements are displayed
        elements = [
            "thin_btn", "medium_btn", "thick_btn", "text_btn", 
            "new_mark_cancel_btn", "top_preview_arrow", "top_preview_text",
            "save_your_mark_text", "draw_your_mark_text"
        ]
        
        for element in elements:
            self.driver.wait_for_object(element, raise_e=raise_e)
            
        # Verify done button exists and is disabled before adding the marks.
        done_btn = self.driver.wait_for_object("new_mark_done_btn", raise_e=raise_e)
        if done_btn:
            assert done_btn.get_attribute("IsEnabled").lower() == "false"
        
        return True

    # ------------Select language dialog-------------- #
    def verify_select_language_dialog(self):
        # The dialog shows after clikcing Text Extract btn.
        self.driver.wait_for_object("select_language_title")
        self.driver.wait_for_object("install_new_language_link")
        self.driver.wait_for_object("select_language_combobox")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("continue_btn")

    # ------------Edit screen-------------- #
    def verify_edit_text_extract_screen(self):
        """
        Verify the Edit screen after clicking continue btn on select language dialog with text extract advanced scan function.
        """
        self.driver.wait_for_object("editable_text_area")
        self.driver.wait_for_object("options_heading") 
        self.driver.wait_for_object("copy_all_btn")  
        self.driver.wait_for_object("edit_done_btn")

    # ------------Text was not detected dialog-------------- #
    def verify_text_not_detected_dialog(self):
        # The dialog shows when clicking Text Extract btn if no text detected in the scanned/import file.
        self.driver.wait_for_object("not_detected_dialog_title")
        self.driver.wait_for_object("not_detected_dialog_body")
        self.driver.wait_for_object("not_detected_dialog_ok_btn")

    # ------------Advanced scan preview screen-------------- #
    def verify_adv_scan_preview_screen(self):
        # Verify the Advanced Scan preview screen elements are displayed.
        elements = [
            "redact_btn", "scribble_btn",
            "add_pages_btn", "new_scan_btn",
            "print_btn", "save_btn",
            "share_btn", "shortcuts_btn", "fax_btn",
            "text_extract_btn"
        ]
        
        for element in elements:
            self.driver.wait_for_object(element)

    # ------------Extracting text dialog-------------- #
    def verify_extracting_text_dialog(self):
        # The dialog shows when clicking continue btn on select language dialog.
        self.driver.wait_for_object("extracting_text_title")
        self.driver.wait_for_object("cancel_btn")

    # ------------Text Edit screen-------------- #
    def verify_are_you_sure_dialog(self, invisible=False):
        # The dialog shows when clicking done btn when delete all text.
        self.driver.wait_for_object("are_you_sure_dialog_title", invisible=invisible)
        self.driver.wait_for_object("restore_text_btn", invisible=invisible)
        self.driver.wait_for_object("start_new_scan_btn", invisible=invisible)
        self.driver.wait_for_object("close_btn", invisible=invisible)

    # ------------searchable_pdf file content-------------- #
    def verify_search_btn_on_pdf_file(self, raise_e=True):
        """
        Verify the search button is displayed on the opened searchable PDF file.
        """
        return self.driver.wait_for_object("search_btn", raise_e=raise_e)
    
    def verify_searchable_pdf_content(self, expected_text):
        """
        Verify the saved searchable PDF can be searched and search results are accurate.
        Confirms that searching for expected_text returns results (no_result_text should NOT appear).
        
        Args:
            expected_text (str): The text to search for in the PDF
        """
        # Check if app selection dialog shows, if so, select Edge and click Just Once
        self.driver.click("search_btn")
        self.driver.send_keys("search_textbox", expected_text, press_enter=True)
        
        #Search is successful and "no results" message does NOT appear
        no_result_found = self.driver.wait_for_object("no_result_text", raise_e=False, timeout=15)
        assert no_result_found is False, f"Search failed: Expected to find '{expected_text}' but 'No results' message appeared"
    
    # ------------ID Card-------------- #

    def verify_card_scan_preview_screen(self, raise_e=False):
        """
        Verify ID card screen.
        """
        self.driver.wait_for_object("id_card_image", raise_e=raise_e)
        self.driver.wait_for_object("card_body_text1", raise_e=raise_e)
        self.driver.wait_for_object("card_body_text2", raise_e=raise_e)
        self.driver.wait_for_object("card_body_text3", raise_e=raise_e)
    
    def verify_back_of_id_card_screen(self, raise_e=False):
        """
        Verify Place the back of your ID card screen.
        """
        self.driver.wait_for_object("id_card_back_image", raise_e=raise_e)
        self.driver.wait_for_object("skip_btn", raise_e=raise_e)
        self.driver.wait_for_object("scan_btn", raise_e=raise_e)

    def verify_id_card_next_screen(self, raise_e=False, timeout=30):
        """
        Verify ID Card Next screen.
        """
        self.driver.wait_for_object("id_card_next_btn", raise_e=raise_e, timeout=timeout)

    # ------------Scan pdf Password_Protection-------------- #
    def show_save_adv_scan_dialog(self, invisible=False, timeout=3):
        self.verify_scan_btn(timeout=30)
        self.click_scan_btn()
        self.verify_scanning_screen()
        self.verify_scan_result_screen(timeout=60)
        self.click_save_btn()
        self.verify_save_adv_scan_dialog_elements()
    
    def verify_save_adv_scan_dialog_elements(self, invisible=False, timeout=3):
        """
        Verify the current screen is Save dialog
        """
        self.driver.wait_for_object("save_title", invisible=invisible, timeout=timeout)
        self.driver.wait_for_object("features_and_file_types_title", invisible=invisible)
        self.driver.wait_for_object("filename_text", invisible=invisible)
        self.driver.wait_for_object("filetype_text", invisible=invisible)
        self.driver.wait_for_object("smart_file_name_title", invisible=invisible)
        self.driver.wait_for_object("smart_file_name_toggle_btn", invisible=invisible)
        self.scroll_to_element(direction="down", distance=6)
        self.driver.wait_for_object("compression_dropdown", invisible=invisible)
        self.driver.wait_for_object("select_language_combobox", invisible=invisible)
        self.driver.wait_for_object("install_new_language_link", invisible=invisible)
        self.driver.wait_for_object("password_protection_title", invisible=invisible)
        self.driver.wait_for_object("add_password_protection_toggle", invisible=invisible)
        self.driver.wait_for_object("dialog_cancel_btn", invisible=invisible)
        self.driver.wait_for_object("dialog_save_btn", invisible=invisible)
    
    def get_file_type_value(self, raise_e=True):
        return self.driver.wait_for_object("file_type_dropdown", raise_e=raise_e).text
    
    def verify_password_protection_display(self, raise_e=True):
        return self.driver.wait_for_object("password_protection_title", raise_e=raise_e)
    
    def check_password_protection_display(self,fileTypeSelectValue):
        """
        Check password protection display based on file type selection
        """
        self.select_file_type_listitem(fileTypeSelectValue)
        assert self.get_file_type_value() == fileTypeSelectValue
        if fileTypeSelectValue in [self.BASIC_PDF, self.SEARCHABLE_PDF]:
            assert self.verify_password_protection_display(), "Password protection option should be displayed for selected file type."
        else:
            assert self.verify_password_protection_not_display(), "Password protection option should NOT be displayed for selected file type."

    
    def verify_smart_file_name_toggle_btn_status(self, by_default=True):
        """
        Verify "smart file name" option is ON or OFF
        """
        toggle = self.driver.wait_for_object("smart_file_name_toggle_btn")
        if by_default:
            assert toggle.get_attribute("Toggle.ToggleState") == "0"
        else:
            assert toggle.get_attribute("Toggle.ToggleState") == "1"
    
    def verify_compression_dropdown_selected_val(self, exp_value, raise_e=True):
        resVal=self.get_compression_dropdown_value()
        assert resVal == exp_value, f"Expected compression dropdown value: {exp_value}, but got: {resVal}"
    
    def get_language_dropdown_value(self, raise_e=True):
        return self.driver.wait_for_object("select_language_combobox", raise_e=raise_e).text

    def verify_language_dropdown_selected_val(self, exp_value, raise_e=True):
        resVal=self.get_language_dropdown_value()
        assert resVal == exp_value, f"Expected compression dropdown value: {exp_value}, but got: {resVal}"
    
    def verify_password_protection_textbox_shows(self, raise_e=True):
        return self.driver.wait_for_object("password_protection_textbox", raise_e=raise_e)
    
    def enter_password_protection(self, password):
        self.driver.send_keys("password_protection_textbox", password)
    
    def password_textbox_note_show(self, raise_e=True):
        return self.driver.wait_for_object("password_textbox_note", raise_e=raise_e)
    
    def password_textbox_note_space_show(self, raise_e=True):
        return self.driver.wait_for_object("password_textbox_note_space", raise_e=raise_e)
    
    def password_textbox_note_too_long_show(self, raise_e=True):
        return self.driver.wait_for_object("password_textbox_note_too_long", raise_e=raise_e)
    
    def password_textbox_note_too_short_show(self, raise_e=True):
        return self.driver.wait_for_object("password_textbox_note_too_short", raise_e=raise_e)
    
    def password_textbox_note_too_short_space_show(self, raise_e=True):
        return self.driver.wait_for_object("password_textbox_note_too_short_space", raise_e=raise_e)

    def password_textbox_note_too_long_space_show(self, raise_e=True):
        return self.driver.wait_for_object("password_textbox_note_too_long_space", raise_e=raise_e)

    def verify_open_file_btn(self, raise_e=True):
        return self.driver.wait_for_object("open_file_btn", raise_e=raise_e)

    def click_open_file_btn_pdf_success(self,password):
        self.driver.click("open_file_btn")
        self.select_edge_to_open_file()
        self.driver.send_keys("password_pdf_input_box", password)
        self.driver.wait_for_object("open_password_file_btn", clickable=True, timeout=10)
        self.driver.click("open_password_file_btn",change_check={"wait_obj":"open_password_file_btn", "invisible": True})

    def click_open_file_btn_pdf_failed(self,password):
        self.driver.click("open_file_btn")
        self.select_edge_to_open_file()
        self.driver.send_keys("password_pdf_input_box", password)
        self.driver.wait_for_object("open_password_file_btn", clickable=True, timeout=10).click()
        return self.driver.wait_for_object("password_pdf_error_message",raise_e=False, timeout=10)

    def verify_scan_result_dcoument_screen(self):
        """
        Verify the current screen is Scan Result document screen
        """
        self.driver.wait_for_object("scan_result_document_image")
        self.driver.wait_for_object("scan_result_document_text1")
        self.driver.wait_for_object("scan_result_document_text2")
        self.driver.wait_for_object("scan_result_document_text3")

    def verify_shortcuts_screen_dialog(self, raise_e=False):
        return self.driver.wait_for_object("shortcuts_screen_dialog_email", raise_e=raise_e, timeout=20)
    
    def get_file_name_text(self, raise_e=False,timeout=20):
        return self.driver.get_attribute("filename_text", attribute="Name",raise_e=raise_e, timeout = timeout)
    
    def verify_shortcuts_screen_successfull(self, raise_e=False):
        self.driver.wait_for_object("done_button", raise_e=raise_e, timeout=10)
        self.driver.wait_for_object("view_status_btn", raise_e=raise_e, timeout=10)
        return self.driver.wait_for_object("shortcuts_button", raise_e=raise_e, timeout=10)

    def verify_start_button(self, raise_e=False):
        return self.driver.wait_for_object("start_button", raise_e=raise_e, timeout=10)
