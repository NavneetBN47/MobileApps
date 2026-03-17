from MobileApps.libs.flows.web.hpx.hpx_flow import HPXFlow
import MobileApps.resources.const.windows.const as w_const
from selenium.common.exceptions import NoSuchElementException
import time
import random
import logging
from datetime import datetime
from selenium.webdriver.common.keys import Keys

class Print(HPXFlow):
    flow_name = "print"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def check_driver_type_to_swipe(self, el=False, direction="down", distance=1):
        if self.driver.driver_type.lower() == "windows":
            if el:
                self.driver.swipe(el, direction=direction, distance=distance)
            else:
                self.driver.swipe(direction=direction, distance=distance)
            time.sleep(1)

    # ---------------- File Picker dialog ---------------- #
    def select_file_picker_dialog_print_btn(self):
        if not self.driver.click("file_picker_dialog_print_btn", raise_e=False):
            el = self.driver.wait_for_object("file_name_combo_box_edit")
            el.send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)  

    def select_file_picker_dialog_cancel_btn(self):
        # if not self.driver.click("file_picker_dialog_cancel_btn", raise_e=False):
        #     el = self.driver.wait_for_object("file_name_combo_box_edit")
        #     el.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)   
        self.driver.click("file_picker_dialog_cancel_btn") 

    def select_file_picker_dialog_close_btn(self, retry=2):
        self.driver.click("file_picker_dialog_close_btn", change_check={"wait_obj": "file_picker_dialog_print_btn", "invisible": True}, retry=retry, timeout=10)
     
    def input_file_name(self, _file, press_enter=True):
        time.sleep(5)
        self.driver.send_keys("file_name_combo_box_edit", _file, press_enter=press_enter)
        time.sleep(5)

    # ---------------- Simple PDF\photo print dialog ---------------- #
    def click_simple_print_window_outside(self):
        self.driver.click("simple_print_window")

    def expand_all_files_combo(self, expand=True):
        coll_state = self.driver.get_attribute("all_files_combo", attribute="ExpandCollapsePattern.ExpandCollapseState")
        if (expand and coll_state==0) or (expand is False and coll_state==1):
            self.driver.click("all_files_combo")
    
    def get_simple_print_window_size(self):
        return self.driver.get_attribute("simple_print_window", attribute="LogicalSize")

    def select_simple_print_dialog_close_btn(self):
        self.driver.click("simple_print_dialog_close_btn")

    def select_simple_print_dialog_print_btn(self, timeout=10, del_file=True):
        if not self.driver.wait_for_object("printer_list_item", format_specifier=["Microsoft Print to PDF"], raise_e=False):
            self.driver.click("simple_print_dialog_print_btn", change_check={"wait_obj": "simple_print_dialog_print_btn", "invisible": True}, retry=2, timeout=timeout)
        else:
            self.driver.click("simple_print_dialog_print_btn", change_check={"wait_obj": "file_name_edit_on_save_print_output_as_dialog"}, retry=2, timeout=timeout)
            file_name = "Print_Output_" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            self.driver.send_keys("file_name_edit_on_save_print_output_as_dialog", file_name, press_enter=True)
            time.sleep(5)
            if del_file:
                self.driver.ssh.send_command("Remove-Item -Path {} -Force".format(w_const.TEST_DATA.DOCUMENTS_FOLDER_PATH + '\\*.pdf'), raise_e=False)

    def del_print_output_file(self):
        path = w_const.TEST_DATA.DOCUMENTS_FOLDER_PATH
        # Use a more direct PowerShell command to get clean file names
        result = self.driver.ssh.send_command("Get-ChildItem -Path '{}' -Filter 'Print_Output_*.pdf' | Select-Object -ExpandProperty Name".format(path))
        file_name_list = result["stdout"].split('\r\n')
        for file_name in file_name_list:
            file_name = file_name.strip()  # Remove any leading/trailing whitespace
            if file_name and "Print_Output_" in file_name:  # Check if file_name is not empty
                full_path = path + '\\' + file_name
                self.driver.ssh.send_command('Remove-Item -Path "{}" -Force'.format(full_path), raise_e=False)
        # file_name_list = ((self.driver.ssh.send_command("Get-ChildItem " + path + "| Select-Object 'name'"))["stdout"]).split('\r\n')
        # for file_name in file_name_list:
        #     if "Print_Output_" in file_name:
        #         self.driver.ssh.send_command('Remove-Item -Path "{}" -Force -Recurse'.format(path + '\\' + file_name))


    def select_simple_print_dialog_cancel_btn(self, timeout=10):
        self.driver.click("simple_print_dialog_cancel_btn", timeout=timeout)

    def select_printer_combo_box(self):
        self.driver.click("printer_combo_box")

    def select_printer(self, _printerhost):
        if _printerhost not in self.driver.ssh.send_command('Get-Printer')['stdout']:
            _printerhost = "Microsoft Print to PDF"
            logging.info("Print via 'Microsoft Print to PDF'")
            pdf_dr = self.driver.ssh.send_command('get-Printer -Name "*Microsoft Print to PDF*"', timeout=20)
            if not pdf_dr["stdout"]:
                self.driver.ssh.send_command('dism /Online /Disable-Feature /FeatureName:"Printing-PrintToPDFServices-Features" /NoRestart', timeout=20)
                time.sleep(2)
                self.driver.ssh.send_command('dism /Online /Enable-Feature /FeatureName:"Printing-PrintToPDFServices-Features" /NoRestart', timeout=20)
        
        if not self.driver.wait_for_object("printer_combo_box", timeout=2, raise_e=False):
                self.check_driver_type_to_swipe("printer_combo_box", direction="up")
        self.select_printer_combo_box()
        
        if _printerhost != "Microsoft Print to PDF":
            if self.driver.wait_for_object("printer_list_item", format_specifier=[_printerhost], timeout=2, raise_e=False) is False:
                _printerhost = "Microsoft Print to PDF"
                logging.info("Print via 'Microsoft Print to PDF'")
        
        self.driver.click("printer_list_item", format_specifier=[_printerhost], timeout=2)
        return _printerhost

    def change_orientation_setting(self, value):
        """
        Change the orientation to the value given
        :param orientation = Portrait/Landscape
        """
        self.check_driver_type_to_swipe("orientation_setting", direction="up")
        self.driver.click("orientation_setting")
        self.driver.click("dynamic_orientation_value", format_specifier=[value])

    def click_orientation_combox(self):
        self.check_driver_type_to_swipe(direction="up")
        self.driver.click("orientation_setting")

    def change_paper_size_setting(self, value=None):
        """
        Change the Paper size to the value given
        :param Paper size = 'Tabloid/Legal/Statement/Executive/A3/A4/A5/Letter'
        """
        self.check_driver_type_to_swipe("paper_size_setting", direction="up")
        self.driver.click("paper_size_setting")
        if value:
            self.driver.click("dynamic_paper_size_value", format_specifier=[value])
        else:
            num = random.randint(1,6)
            select_size = self.driver.get_attribute("dynamic_paper_size_num", format_specifier=[num], attribute="Name")
            self.driver.click("dynamic_paper_size_num", format_specifier=[num])
            return select_size

    def change_copies_setting(self, value):
        """
        Change the Copies to the value given
        """
        self.check_driver_type_to_swipe("copies_number_box", direction="down")
        assert self.driver.get_attribute("copies_number_box", attribute="Value.Value") == "1"
        self.driver.send_keys("copies_number_box", value, press_enter=True)
        # self.driver.click("copies_text")
        assert self.driver.get_attribute("copies_number_box", attribute="Value.Value") == value

    def change_duplex_printing_setting(self, value):
        """
        Change the Duplex printing to the value given
        :param Paper size = 'Print on only one side of the page/Flip the long edge/Flip the short edge'
        """
        # self.check_driver_type_to_swipe("duplex_printing_setting", direction="down")
        if self.driver.click("duplex_printing_setting", raise_e=False):
            self.driver.click("dynamic_duplex_printing_value", format_specifier=[value])
        else:
            logging.info("Printer does not support Duplex Printing")

    def change_page_range_setting(self, value):
        """
        Change the Page Range to the value given
        :param Paper size = 'Print all pages/Print current page/Print pages in range'
        """
        self.check_driver_type_to_swipe("page_range_setting", direction="down")
        self.driver.click("page_range_setting")
        self.driver.click("dynamic_page_range_value", format_specifier=[value])

    def enter_page_range_value(self, value):
        self.driver.send_keys("page_range_edit", value)

    def change_output_quality_setting(self, value):
        """
        Change the Output Quality to the value given
        :param output_quality = Fast/Normal/HighQuality
        """
        self.driver.click("output_quality_setting")
        self.driver.click("dynamic_output_quality_value", format_specifier=[value])

    def change_photo_size_setting(self, value):
        """
        Change the photo size to the value given
        :param output_quality = Full Page/3.5x5/4x6/5x7/8x10/10x15/13x18
        """
        self.check_driver_type_to_swipe("photo_size_setting", direction="down")
        self.driver.click("photo_size_setting")
        self.driver.click("dynamic_photo_size_value", format_specifier=[value])

    def change_select_a_layout_setting(self, value):
        """
        Change the photo size to the value given
        :param output_quality = One photo per page/Multiple photos per page
        """
        self.check_driver_type_to_swipe("select_a_layout_setting", direction="down")
        self.driver.click("select_a_layout_setting")
        self.driver.click("dynamic_select_a_layout_value", format_specifier=[value])

    def change_select_scaling_setting(self,value):
        self.check_driver_type_to_swipe("scaling_setting", direction="down")
        self.driver.click("scaling_setting")
        self.driver.click("dynamic_scaling_value", format_specifier=[value])

    def change_select_output_quality_setting(self, value):
        self.check_driver_type_to_swipe("output_quality_setting", direction="down")
        self.driver.click("output_quality_setting")
        self.driver.click("dynamic_output_quality_value", format_specifier=[value])

    def change_paper_type_setting(self, value):
        self.check_driver_type_to_swipe("paper_type_setting", direction="down")
        self.driver.click("paper_type_setting")
        self.driver.click("dynamic_paper_type_value", format_specifier=[value])

    def select_more_settings_link(self):
        self.check_driver_type_to_swipe("more_settings_link", direction="down")
        self.driver.click("more_settings_link")

    def select_more_settings_menu_dialog_ok_btn(self):
        self.driver.click("more_settings_menu_dialog_ok_btn", change_check={"wait_obj": "more_settings_menu_dialog_ok_btn", "invisible": True}, retry=2, timeout=5)

    def input_copies_number(self, num):
        self.check_driver_type_to_swipe("copies_number_box", direction="down")
        self.driver.send_keys("copies_number_box", num)
    
    def get_total_page_num(self):
        num = self.driver.get_attribute("total_page_num", attribute="Name")
        return int(num)

    # ---------------- Password needed dialog ---------------- #
    def input_password(self, password):
        self.driver.click("password_edit")
        self.driver.send_keys("password_edit", password)

    def select_dialog_cancel_btn(self):
        """
        Click Cancel button on Password needed / Sending File... Dialog
        """
        if self.driver.click("dialog_cancel_btn", change_check={"wait_obj": "dialog_cancel_btn", "invisible": True}, retry=2, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("dialog_cancel_btn", timeout=2)
            el.send_keys(Keys.ENTER)

    def select_dialog_ok_btn(self):
        """
        Click OK button on Password needed / File format error / File Send dialog
        """
        if self.driver.click("dialog_ok_btn", change_check={"wait_obj": "dialog_ok_btn", "invisible": True}, retry=2, delay=1, raise_e=False) is False:
            el = self.driver.wait_for_object("dialog_ok_btn", timeout=2)
            el.send_keys(Keys.ENTER)

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_file_picker_dialog(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("file_name_combo_box_edit", timeout=timeout, raise_e=raise_e)

    def verfiy_file_picker_dialog_buttons(self, print_pdfs=True):
        self.driver.wait_for_object("file_picker_dialog_print_btn", displayed=False)
        self.driver.wait_for_object("file_picker_dialog_cancel_btn", displayed=False)
        if print_pdfs:
            assert self.driver.wait_for_object("file_picker_dialog_print_btn").text == "Print"
        else:
            assert self.driver.wait_for_object("file_picker_dialog_print_btn").text == "Select Photos to Print"

    def verify_files_format(self, file_format):
        return self.driver.wait_for_object("dynamic_file_item", format_specifier=[file_format], raise_e=False)

    # ---------------- Simple print dialog ---------------- #
    def verify_simple_print_dialog(self, raise_e=True):
        return self.driver.wait_for_object("simple_print_dialog_print_btn", raise_e=raise_e) and \
            self.driver.wait_for_object("simple_print_dialog_cancel_btn", raise_e=raise_e)

    def verify_common_detail_simple_print_dialog(self, pho_swipe=False):
        """
        common detail object
        """
        self.driver.wait_for_object("printer_combo_box", timeout=20)
        self.driver.wait_for_object("let_the_app_toggle")
        self.driver.wait_for_object("orientation_text", raise_e=False)
        self.driver.wait_for_object("orientation_setting")
        self.driver.wait_for_object("paper_size_text", raise_e=False)
        self.driver.wait_for_object("paper_size_setting")
        if pho_swipe:
            self.check_driver_type_to_swipe("paper_type_setting", direction="down")
        self.driver.wait_for_object("paper_type_text", raise_e=False)
        self.driver.wait_for_object("paper_type_setting")
        self.driver.wait_for_object("output_quality_text", raise_e=False)
        self.driver.wait_for_object("output_quality_setting")
        self.driver.wait_for_object("copies_text", raise_e=False)
        self.driver.wait_for_object("copies_number_box")
        self.driver.wait_for_object("copies_number_minus_btn")
        self.driver.wait_for_object("copies_number_plus_btn")
        self.check_driver_type_to_swipe("more_settings_link", direction="down")
        self.driver.wait_for_object("more_settings_link")
        self.driver.wait_for_object("simple_print_dialog_print_btn")
        self.driver.wait_for_object("simple_print_dialog_cancel_btn")

    def verify_detail_simple_pdf_print_dialog(self):
        """
        Simple PDF print dialog.
        """
        self.verify_common_detail_simple_print_dialog()
        if self.driver.wait_for_object("duplex_printing_text", raise_e=False):
            self.driver.wait_for_object("duplex_printing_setting")
        self.driver.wait_for_object("page_range_text", raise_e=False)
        self.driver.wait_for_object("page_range_setting")

    def verify_detail_simple_photo_print_dialog(self):
        """
        Simple Photo print dialog.
        """
        self.verify_common_detail_simple_print_dialog(pho_swipe=True)
        self.driver.wait_for_object("photo_size_text", raise_e=False)
        self.driver.wait_for_object("photo_size_setting")
        self.driver.wait_for_object("select_a_layout_text", raise_e=False)
        self.driver.wait_for_object("select_a_layout_setting")
        self.driver.wait_for_object("scaling_text", raise_e=False)
        self.driver.wait_for_object("scaling_setting")

    def verify_orientation_setting(self):
        value_list = ["Portrait", "Landscape"]
        self.check_driver_type_to_swipe("orientation_setting", direction="up")
        self.driver.click("orientation_setting")
        for value in value_list:
            self.driver.wait_for_object("dynamic_orientation_value", format_specifier=[value])
        self.driver.click("combo_box_close_btn")

    def verify_paper_size_setting(self):
        self.check_driver_type_to_swipe("paper_size_setting", direction="up")
        self.verify_display_text('Letter')
        self.driver.click("paper_size_setting")
        for num in [1, 6]:
            self.driver.wait_for_object("dynamic_paper_size_num", format_specifier=[num])
        self.driver.click("combo_box_close_btn")

    def verify_photo_size_setting(self):
        self.check_driver_type_to_swipe("photo_size_setting", direction="up")
        value_list = ["Full Page","3.5x5 in.","4x6 in.","5x7 in.","8x10 in.","9x13 cm","10x15 cm","13x18 cm"]
        time.sleep(2)
        self.driver.click("photo_size_setting")
        for value in value_list:
            self.driver.wait_for_object("dynamic_photo_size_value", format_specifier=[value])
        self.driver.click("combo_box_close_btn")

    def verify_select_a_layout_setting(self):
        value_list = ["One photo per page","Multiple photos per page"]
        self.driver.click("select_a_layout_setting")
        for value in value_list:
            self.driver.wait_for_object("dynamic_select_a_layout_value", format_specifier=[value])
        self.driver.click("combo_box_close_btn")

    def verify_scaling_setting(self):
        self.check_driver_type_to_swipe("scaling_setting", direction="down")
        value_list = ["Crop","Shrink to fit"]
        self.driver.click("scaling_setting")
        for value in value_list:
            self.driver.wait_for_object("dynamic_scaling_value", format_specifier=[value])
        self.driver.click("combo_box_close_btn")
        
    def verify_paper_type_setting(self):
        self.check_driver_type_to_swipe("paper_type_setting", direction="down")
        value_list = []
        for value in value_list:
            self.driver.wait_for_object("dynamic_paper_type_value", format_specifier=[value])
        self.driver.click("combo_box_close_btn")

    def verify_output_quality_setting(self):
        self.verify_display_text('Normal')
        value_list = ['Normal', 'Draft', 'High quality']
        self.driver.click("output_quality_setting")
        for value in value_list:
            self.driver.wait_for_object("dynamic_output_quality_value", format_specifier=[value])
        self.driver.click("combo_box_close_btn")

    def verify_duplex_printing_setting(self):
        self.check_driver_type_to_swipe("more_settings_link", distance=3)
        if self.driver.wait_for_object("duplex_printing_setting", raise_e=False, timeout=3):
            if not self.verify_display_text('Print on two sides', raise_e=False):
                self.verify_display_text('Print on one side')
                self.verify_display_text('Print on only one side of the page')
            value_list = ['Print on only one side of the page', 'Flip the long edge', 'Flip the short edge']
            self.driver.click("duplex_printing_setting")
            for value in value_list:
                self.driver.wait_for_object("dynamic_duplex_printing_value", format_specifier=[value])
            self.driver.click("combo_box_close_btn")
        else:
            logging.info("Printer does not support Duplex Printing")

    def verify_page_range_setting(self):
        self.check_driver_type_to_swipe("page_range_setting", distance=3)
        self.verify_display_text('Print all pages')
        value_list = ['Print all pages', 'Print current page', 'Print pages in range']
        self.driver.click("page_range_setting")
        for value in value_list:
            self.driver.wait_for_object("dynamic_page_range_value", format_specifier=[value])
        self.driver.click("combo_box_close_btn")

    def verify_page_range_edit(self, raise_e=True):
        return self.driver.wait_for_object("page_range_edit", raise_e=raise_e)

    def verify_more_settings_menu_dialog(self, timeout=20, invisible=False):
        return self.driver.wait_for_object("more_settings_menu_dialog_ok_btn", timeout=timeout, invisible=invisible)

    def verify_portrait_opt_display(self):
        self.driver.wait_for_object("portrait_text")

    def verify_landscape_opt_display(self):
        self.driver.wait_for_object("landscape_text")

    # ---------------- Password needed dialog ---------------- #
    def verify_password_needed_dialog(self, raise_e=True):
        """
        Password needed dialog shows if select a password-protected file for print.
        """
        return self.driver.wait_for_object("password_needed_dialog", raise_e=raise_e) and\
        self.driver.wait_for_object("enter_a_password_text", raise_e=raise_e) and\
        self.driver.wait_for_object("password_edit", raise_e=raise_e) and\
        self.driver.wait_for_object("dialog_cancel_btn", raise_e=raise_e) and\
        self.driver.wait_for_object("dialog_ok_btn", raise_e=raise_e)

    def verify_display_text(self, text, raise_e=True):
        return self.driver.wait_for_object("dynamic_text", format_specifier=[text], raise_e=raise_e)

    def verify_password_incorrect_text(self, raise_e=True):
        self.driver.wait_for_object("password_incorrect_text", raise_e=raise_e)
