from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
from time import sleep
import logging
from selenium.common.exceptions import NoSuchElementException


class Print(GothamFlow):
    flow_name = "print"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    # ---------------- Supported Document File Types dialog ---------------- #
    def select_do_not_show_this_message_checkbox(self, uncheck=False):
        self.driver.check_box("supported_document_file_types_dialog", uncheck=uncheck)

    def select_supported_document_file_types_dialog_ok_btn(self):
        self.driver.click("supported_document_file_types_dialog_ok_btn")
    # ---------------- Supported Document File Types dialog ---------------- #


    # ---------------- File picker dialog ---------------- #
    def input_file_name(self, _file):
        self.driver.send_keys("file_name_combo_box_edit", _file, press_enter=True)

    def select_file_picker_dialog_print_btn(self):
        self.driver.click("file_picker_dialog_print_btn")

    def select_file_picker_dialog_cancel_btn(self):
        self.driver.click("file_picker_dialog_cancel_btn")
    # ---------------- File picker dialog ---------------- #


    # ---------------- Simple print dialog ---------------- #
    def select_printer_combo_box(self):
        self.driver.click("simple_print_dialog")

    def select_printer(self, _printerhost):
        self.select_printer_combo_box()
        for i in range(3):
            if not self.driver.click("printer_list_item", format_specifier=[_printerhost], timeout=2, raise_e=False):
                self.driver.swipe()
                sleep(1)
            else:
                break
        else:
            raise NoSuchElementException("Fail to found the printer")
            
    def change_orientation_setting(self, orientation):
        """
        Change the orientation to the value given
        :param orientation = Portrait/Landscape
        :return:
        """
        self.driver.swipe("orientation_setting", direction="up")
        sleep(2)
        self.driver.click("orientation_setting")
        self.driver.click("orientation_setting_{}".format(orientation))

    def change_output_quality_setting(self, output_quality):
        """
        Change the Output Quality to the value given
        :param output_quality = Fast/Normal/HighQuality
        :return:
        """
        self.driver.swipe("output_quality_setting")
        sleep(2)
        self.driver.click("output_quality_setting")
        self.driver.click("output_quality_setting_{}".format(output_quality))

    def select_combo_box_close_btn(self):
        self.driver.click("combo_box_close_btn")

    def select_more_settings_link(self):
        self.driver.swipe("more_settings_link")
        self.driver.click("more_settings_link")

    def select_more_settings_menu_dialog_ok_btn(self):
        self.driver.click("more_settings_menu_dialog_ok_btn")

    def select_print_dialog_print_btn(self):
        self.driver.click("print_dialog_print_btn", change_check={"wait_obj": "print_dialog_print_btn", "invisible": True}, timeout=10, delay=2)

    def select_print_dialog_cancel_btn(self):
        self.driver.click("print_dialog_cancel_btn", change_check={"wait_obj": "print_dialog_cancel_btn", "invisible": True}, timeout=10, delay=2)
    # ---------------- Simple print dialog ---------------- #


    # ---------------- IPP Print screen ---------------- #
    def change_ipp_print_quality(self, quality):
        """
        Change the Quality to the value given
        :param quality = Normal/Best/Draft
        :return:
        """
        self.driver.click("quality_combo_box")
        self.driver.click("quality_item_{}".format(quality))

    def select_ipp_print_screen_print_btn(self):
        self.driver.click("ipp_print_screen_print_btn")
    # ---------------- IPP Print screen ---------------- #

    # ---------------- Optimize for Faster Remote Printing dialog---------------- #
    def select_dialog_cancel_print_btn(self):
        self.driver.click("dialog_cancel_print_btn")

    def select_dialog_optimize_and_print_btn(self):
        self.driver.click("dialog_optimize_and_print_btn")
    # ---------------- Optimize for Faster Remote Printing dialog---------------- #

    # ---------------- File Send dialog---------------- #
    def select_file_sent_dialog_job_status_btn(self):
        self.driver.click("file_sent_dialog_job_status_btn")

    # ---------------- File Send dialog---------------- #

    # ---------------- Password needed dialog ---------------- #
    def input_password(self, password):
        self.driver.send_keys("password_edit", password)

    def verify_password_incorrect_text(self, raise_e=True):
        self.driver.wait_for_object("password_incorrect_text", raise_e=raise_e)
    # ---------------- Password needed dialog ---------------- #

    def select_dialog_cancel_btn(self):
        """
        Click Cancel button on Password needed / Sending File... Dialog
        """
        self.driver.click("dialog_cancel_btn")

    def select_dialog_ok_btn(self):
        """
        Click OK button on Password needed / File format error / File Send dialog
        """
        self.driver.click("dialog_ok_btn")

    # ---------------- Private Pickup---------------- #
    def click_private_pickup_combo_box(self):
        self.driver.click("private_pickup_combo_box")

    def select_private_pickup_state(self, set_on=False):
        if set_on:
            self.driver.click("dynamic_private_pickup_toggle_text", format_specifier=['On'])
        else:
            self.driver.click("dynamic_private_pickup_toggle_text", format_specifier=['Off'])

    # *********************************************************************************
    #                               VERIFICATION FLOWS                                *
    # *********************************************************************************
    def verify_supported_document_file_types_dialog(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("supported_document_file_types_dialog", timeout=timeout, raise_e=raise_e)

    def verify_file_picker_dialog(self, timeout=30):
        self.driver.wait_for_object("file_picker_dialog", timeout=timeout)

    def verify_password_needed_dialog(self):
        """
        Password needed dialog shows if select a password-protected file for print.
        """
        self.driver.wait_for_object("password_needed_dialog")
        self.driver.wait_for_object("enter_a_password_text")
        self.driver.wait_for_object("password_edit")
        self.driver.wait_for_object("dialog_cancel_btn")
        self.driver.wait_for_object("dialog_ok_btn")

    def verify_file_format_error_dialog(self, remote_printer=False, file_path=None):
        """
        File format error dialog shows if select a corrupt or has an incorrecct format file for print.
        """
        if not remote_printer:
            self.driver.wait_for_object("file_format_error_dialog")
            self.driver.wait_for_object("the_file_could_not_be_opened_text")
        else:
            self.driver.wait_for_object("file_format_error_dialog_remote")
            self.driver.wait_for_object("the_file_could_not_be_opened_text_remote")
            self.driver.wait_for_object("file_path_text_remote", format_specifier=[file_path])
        self.driver.wait_for_object("dialog_ok_btn")

    def verify_password_protected_pdf_dialog(self, file_path):
        """
        Password protected PDF dialog shows if select password-protected PDF file for print.
        """
        self.driver.wait_for_object("password_protected_pdf_text")
        self.driver.wait_for_object("password_protected_pdf_files_are_not_suppported_text")
        self.driver.wait_for_object("file_path_text_remote", format_specifier=[file_path])
        self.driver.wait_for_object("dialog_ok_btn")

    def verify_getting_remote_printer_status_text(self, timeout=30, invisible=False, raise_e=True):
        return self.driver.wait_for_object("getting_remote_printer_status_text", timeout=timeout, invisible=invisible, raise_e=raise_e)
    
    def verify_creating_preview_text(self, timeout=30, invisible=False, raise_e=True):
        return self.driver.wait_for_object("creating_preview_text", timeout=timeout, invisible=invisible, raise_e=raise_e)
    
    def verify_ipp_print_screen(self, raise_e=True):
        return self.driver.wait_for_object("paper_source_combo_box", raise_e=raise_e)

    def verify_ipp_print_screen_no_preview_image(self, raise_e=True):
        return self.driver.wait_for_object("ipp_print_screen_no_preview_image", raise_e=raise_e)

    def verify_ipp_print_screen_document_preview_image(self, raise_e=True):
        return self.driver.wait_for_object("ipp_print_screen_document_preview_image", raise_e=raise_e)

    def verify_ipp_print_screen_photo_preview_image(self, raise_e=True):
        return self.driver.wait_for_object("ipp_print_screen_photo_preview_image", raise_e=raise_e)

    def verify_ipp_print_screen_two_sided_printing_item(self, raise_e=True):
        return self.driver.wait_for_object("two_sided_printing_combo_box", raise_e=raise_e)

    def verify_optimize_for_faster_remote_printing_dialog(self, timeout=5, raise_e=True):
        return self.driver.wait_for_object("optimize_for_faster_remote_printing_dialog", timeout=timeout, raise_e=raise_e)

    def verify_sending_file_dialog(self, raise_e=True):
        return self.driver.wait_for_object("sending_file_dialog_title", raise_e=raise_e)  and \
                self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e)

    def verify_print_job_canceled_dialog(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("print_job_canceled_dialog", timeout=timeout, raise_e=raise_e)  and \
                self.driver.wait_for_object("dialog_ok_btn", timeout=timeout, raise_e=raise_e)

    def verify_print_job_failed_dialog(self, timeout=30, raise_e=True):
        return self.driver.wait_for_object("print_job_failed_text", timeout=timeout, raise_e=raise_e)  and \
                self.driver.wait_for_object("dialog_ok_btn", timeout=timeout, raise_e=raise_e)

    def verify_file_send_dialog(self, timeout=60, raise_e=True):
        return self.driver.wait_for_object("file_sent_dialog_job_status_btn", timeout=timeout, raise_e=raise_e)  and \
                self.driver.wait_for_object("dialog_ok_btn", timeout=timeout, raise_e=raise_e) and \
                self.driver.wait_for_object("file_sent_dialog_title", timeout=timeout, raise_e=raise_e)

    def verify_print_dialog_print_btn_enabled(self):
        return self.driver.wait_for_object("print_dialog_print_btn").get_attribute("IsEnabled")
        
    def check_private_pickup_box_value(self, toggle):
        if toggle.lower() == 'on':
            self.driver.wait_for_object("private_pickup_combo_box")
            self.driver.wait_for_object("dynamic_private_pickup_toggle_text", format_specifier=['Required'])
        elif toggle.lower() == 'off':
            self.click_private_pickup_combo_box()
            self.driver.wait_for_object("dynamic_private_pickup_toggle_text", format_specifier=['On'])
            self.driver.wait_for_object("dynamic_private_pickup_toggle_text", format_specifier=['Off'])
            self.click_private_pickup_combo_box()

    def verify_ipp_print_screen_btn_text(self, toggle):
        if toggle.lower() == 'on':
            assert self.driver.get_attribute("ipp_print_screen_btn_text", "Name") == 'Send File'
        elif toggle.lower() == 'off':
            assert self.driver.get_attribute("ipp_print_screen_btn_text", "Name") == 'Print'

    def verify_ipp_print_screen_print_btn(self, raise_e=True):
        return self.driver.wait_for_object("ipp_print_screen_print_btn", raise_e=raise_e)

    def verify_dialog_cancel_btn(self, raise_e=True):
        return self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e)

    def verify_print_job_failed_dialog(self, raise_e=True):
        return self.driver.wait_for_object("printjobfailed_dialog", raise_e=raise_e)
    
    # ---------------- Simple print dialog ---------------- #
    def verify_simple_print_dialog(self, timeout=30, invisible=False, raise_e=True):
        return self.driver.wait_for_object("simple_print_dialog", timeout=timeout, invisible=invisible, raise_e=raise_e)

    def verify_simple_photo_print_dialog(self):
        """
        Check the settings items on Simple Photo print dialog.
        """
        if "11" not in self.driver.ssh.send_command("Get-CimInstance Win32_Operatingsystem | Select-Object -expand Caption")['stdout']:
            self.driver.wait_for_object("orientation_text", timeout=20)
            self.driver.wait_for_object("paper_size_text")
            self.driver.wait_for_object("photo_size_text")
            self.driver.wait_for_object("select_a_layout_text")
            self.driver.wait_for_object("borderless_printing_text", timeout=3, raise_e=False)
            self.driver.wait_for_object("scaling_text")
            self.driver.swipe("copies_text")
            self.driver.wait_for_object("paper_type_text")
            self.driver.wait_for_object("output_quality_text")
            self.driver.wait_for_object("copies_text")
            self.driver.swipe("orientation_setting", direction="up")

        self.driver.wait_for_object("orientation_setting", timeout=20)
        self.driver.wait_for_object("paper_size_setting")
        self.driver.wait_for_object("photo_size_setting")
        self.driver.wait_for_object("select_a_layout_setting")
        self.driver.wait_for_object("borderless_printing_setting", timeout=3, raise_e=False)
        self.driver.swipe("more_settings_link")
        self.driver.wait_for_object("more_settings_link")
        self.driver.wait_for_object("scaling_setting")
        self.driver.wait_for_object("paper_type_setting")
        self.driver.wait_for_object("output_quality_setting")
        self.driver.wait_for_object("copies_number_box")
        self.driver.wait_for_object("copies_number_minus_btn")
        self.driver.wait_for_object("copies_number_plus_btn")

        self.driver.wait_for_object("print_dialog_print_btn")
        self.driver.wait_for_object("print_dialog_cancel_btn")

    def verify_simple_pdf_print_dialog(self):
        """
        Check the settings items on Simple PDF print dialog.
        """
        if "11" not in self.driver.ssh.send_command("Get-CimInstance Win32_Operatingsystem | Select-Object -expand Caption")['stdout']:
            self.driver.wait_for_object("orientation_text", timeout=20)
            self.driver.wait_for_object("paper_size_text")
            self.driver.wait_for_object("paper_type_text")
            self.driver.wait_for_object("output_quality_text")
            self.driver.wait_for_object("copies_text")
            self.driver.wait_for_object("duplex_printing_text", timeout=3, raise_e=False)
            self.driver.swipe("page_range_text")
            self.driver.wait_for_object("page_range_text")

        self.driver.wait_for_object("orientation_setting", timeout=20)
        self.driver.wait_for_object("paper_size_setting")
        self.driver.wait_for_object("paper_type_setting")
        self.driver.wait_for_object("output_quality_setting")
        self.driver.wait_for_object("copies_number_box")
        self.driver.wait_for_object("copies_number_minus_btn")
        self.driver.wait_for_object("copies_number_plus_btn")
        self.driver.swipe("more_settings_link")
        self.driver.wait_for_object("more_settings_link")
        self.driver.wait_for_object("duplex_printing_setting", timeout=3, raise_e=False)
        self.driver.wait_for_object("page_range_setting")
        self.driver.wait_for_object("print_dialog_print_btn")
        self.driver.wait_for_object("print_dialog_cancel_btn")

    def verify_orientation_setting(self):
        self.driver.swipe("orientation_setting", direction="up")
        sleep(2)
        self.driver.click("orientation_setting")
        self.driver.wait_for_object("orientation_setting_portrait")
        self.driver.wait_for_object("orientation_setting_landscape")
        self.driver.click("combo_box_close_btn")

    def verify_paper_size_setting(self):
        self.driver.click("paper_size_setting")
        self.driver.wait_for_object("paper_size_setting_letter")
        self.driver.wait_for_object("paper_size_setting_executive")
        self.driver.wait_for_object("paper_size_setting_a4")
        self.driver.wait_for_object("paper_size_setting_a5")
        self.driver.click("combo_box_close_btn")

    def verify_photo_size_setting(self):
        self.driver.click("photo_size_setting")
        self.driver.wait_for_object("photo_size_setting_full_page")
        self.driver.wait_for_object("photo_size_setting_35x5in")
        self.driver.wait_for_object("photo_size_setting_4x6in")
        self.driver.wait_for_object("photo_size_setting_5x7in")
        self.driver.wait_for_object("photo_size_setting_8x10in")
        self.driver.wait_for_object("photo_size_setting_9x13cm")
        self.driver.wait_for_object("photo_size_setting_10x15cm")
        self.driver.wait_for_object("photo_size_setting_13x18cm")
        self.driver.click("combo_box_close_btn")

    def verify_select_a_layout_setting(self):
        self.driver.click("select_a_layout_setting")
        self.driver.wait_for_object("select_a_layout_setting_one_photo")
        self.driver.wait_for_object("select_a_layout_setting_multiple_photos")
        self.driver.click("combo_box_close_btn")

    def verify_borderless_printing_setting(self):
        if self.driver.wait_for_object("borderless_printing_text", timeout=3, raise_e=False):
            self.driver.click("borderless_printing_setting")
            self.driver.wait_for_object("borderless_printing_setting_off")
            self.driver.wait_for_object("borderless_printing_setting_on")
            self.driver.click("combo_box_close_btn")
        else:
            logging.info("Printer does not support Borderless Printing")

    def verify_scaling_setting(self):
        self.driver.swipe("scaling_setting")
        sleep(2)
        self.driver.click("scaling_setting")
        self.driver.wait_for_object("scaling_setting_crop")
        self.driver.wait_for_object("scaling_setting_shrink_to_fit")
        self.driver.click("combo_box_close_btn")
        
    def verify_paper_type_setting(self):
        self.driver.click("paper_type_setting")
        self.driver.wait_for_object("paper_type_setting_plain")
        self.driver.click("combo_box_close_btn")

    def verify_output_quality_setting(self):
        self.driver.click("output_quality_setting")
        self.driver.wait_for_object("output_quality_setting_fast", timeout=3, raise_e=False)
        self.driver.wait_for_object("output_quality_setting_normal")
        self.driver.wait_for_object("output_quality_setting_highquality")
        self.driver.click("combo_box_close_btn")

    def verify_duplex_printing_setting(self):
        if self.driver.wait_for_object("duplex_printing_setting", timeout=3, raise_e=False):
            sleep(2)
            self.driver.click("duplex_printing_setting")
            self.driver.wait_for_object("duplex_printing_setting_one_side")
            self.driver.wait_for_object("duplex_printing_setting_two_sides_long")
            self.driver.wait_for_object("duplex_printing_setting_two_sides_short")
            self.driver.click("combo_box_close_btn")
        else:
            logging.info("Printer does not support Duplex Printing")

    def verify_page_range_setting(self):
        self.driver.swipe("page_range_setting")
        sleep(2)
        self.driver.click("page_range_setting")
        self.driver.wait_for_object("page_range_setting_all_pages")
        self.driver.wait_for_object("page_range_setting_current_page")
        self.driver.wait_for_object("page_range_setting_in_range")
        self.driver.click("combo_box_close_btn")

    def verify_more_settings_menu_dialog(self, timeout=20, invisible=False):
        return self.driver.wait_for_object("more_settings_menu_dialog_ok_btn", timeout=timeout, invisible=invisible)
    # ---------------- Simple print dialog ---------------- #

    # *********************************************************************************
    #                               FLOWS                                
    # *********************************************************************************
    def start_a_remote_print(self, type, pa=True):
        self.verify_ipp_print_screen_no_preview_image(raise_e=False)
        self.verify_getting_remote_printer_status_text(timeout=45, invisible=True)
        self.verify_creating_preview_text(timeout=45, invisible=True)
        if type.lower() == 'doc':
            self.verify_ipp_print_screen_document_preview_image()
        if type.lower() == 'photo':
            self.verify_ipp_print_screen_photo_preview_image()
        self.select_ipp_print_screen_print_btn()
        if self.verify_optimize_for_faster_remote_printing_dialog(timeout=3, raise_e=False):
            self.select_dialog_optimize_and_print_btn()
        self.verify_sending_file_dialog()
        if pa:
            self.verify_file_send_dialog(timeout=120)
        else:
            self.verify_print_job_failed_dialog(timeout=120)
        self.select_dialog_ok_btn()
