from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.android.hpps.hpps_flow import hppsFlow
from SAF.misc import saf_misc

import logging
from time import sleep

class Trap_Door(hppsFlow):
    """
    Trap_Door - deals with all elements after accessing HPPS through the Trap Door of an Android device
              - From Hp Smart or by click the share feature in 3rd party applications and selecting HPPS from
                the overlay
    """

    # Flow_name - Title of the ui map used in this class
    flow_name = "trap_door"

    ########################################################################################################################
    #                                                  Action Flows                                                        #
    ###################################################################################################################
    #########################################################################################################
    #                                           Search Printer Page                                    #
    ####################################################################################################
    def select_printer(self, printer_info, is_searched=True, timeout=120):
        """
        Select a printer on printer list or via searching
        :param printer_info: printer ip address or bonjour name
        :param is_searched: using search to select printer or printer list
        """
        if is_searched:
            self.select_search()
            self.search_and_select_printer_by_name(printer_info)
        else:
            self.driver.wait_for_object("printer_list_scroll_view", timeout=timeout)
            logging.info("Waiting for 10 seconds for loading completely...")
            sleep(10)       # Take
            self.driver.scroll("printer_name", format_specifier=[printer_info], timeout=timeout).click()

    def select_search(self):
        """
        select the serach button
        :return:
        """
        self.driver.wait_for_object("search_btn")
        self.driver.click("search_btn")

    def select_3dot_options(self):
        """
        select the 3 dotr button
        :return:
        """
        self.driver.click("3dot_btn")

    def search_and_select_printer_by_name(self, printer, tries=10):
        """
        search for printer and select result
        :param printer:
        :return:
        """
        found=False
        self.driver.wait_for_object("search_tf")
        self.driver.send_keys("search_tf", printer)
        for _ in range(tries):
            sleep(3)
            if self.driver.wait_for_object("_shared_printer_name", format_specifier=[printer], timeout=10, raise_e=False) is False:
                popup = self.driver.wait_for_object("no_printer_found_try_again_btn", timeout=10, raise_e=False)
                if popup is not False:
                    popup.click()
                if not self.driver.click("printer_list_refresh", timeout=10, raise_e=False):
                    self.driver.swipe(direction="up")
            else:
                found = True
                break
        if found is False:
            raise NoSuchElementException("Could not find printer: " + printer)
        self.driver.click("_shared_printer_name", format_specifier=[printer])

    def select_remote_printer(self):
        """
        select the first printer in searched results
        :return:
        """
        if self.driver.wait_for_object("remote_printer_subtitle", timeout=20, raise_e=False)is not False:
            self.driver.click("remote_printer_subtitle")
    ####################################################################################################
    #                                           Print Preview  Page                                    #
    ####################################################################################################

    def select_print(self):
        """
        selects the print button
        :return:
        """
        self.driver.click("print_btn")

    def change_number_of_copies_to(self, copies):
        """
        change the number of copies to the value given
        :param copies:
        :return:
        """
        copies = int(copies)
        if 10 > copies > 0:
            current_copies = int(self.driver.find_object("num_of_copies_txt").text)
            while current_copies != copies:
                if current_copies < copies:
                    self.driver.click("copies_increment_btn")
                else:
                    self.driver.click("copies_decrement_btn")
                current_copies = int(self.driver.find_object("num_of_copies_txt").text)

    def change_color_mode(self, color_mode):
        """
        Change the color mode to the value given
        :param color_mode:
        :return:
        """
        color_mode_obj_name = self.check_parameter_in_dict(color_mode)
        self.driver.click("color_list_btn")
        self.driver.wait_for_object(color_mode_obj_name, timeout=3)
        self.driver.click(color_mode_obj_name)

    def change_paper_size(self, paper_size):
        """
        Change the paper size to the value given
        :param paper_size:
        :return:
        """
        paper_size_obj_name = self.check_parameter_in_dict(paper_size)
        self.driver.scroll("paper_size_list_btn")
        self.driver.click("paper_size_list_btn")
        self.driver.wait_for_object(paper_size_obj_name, timeout=3)
        self.driver.click(paper_size_obj_name)

    def change_orientation(self, orientation):
        """
        change the orientation to the value given
        :param orientation:
        :return:
        """
        orientation_obj_name = self.check_parameter_in_dict(orientation)
        self.driver.scroll("orientation_list_btn")
        self.driver.click("orientation_list_btn")
        self.driver.wait_for_object(orientation_obj_name)
        self.driver.click(orientation_obj_name)

    def select_more_options(self):
        """
        clicks on the More Options button
        :return:
        """
        self.driver.scroll("more_option_btn", check_end=False)
        self.driver.click("more_option_btn")

    def flip_two_sided_preview(self, side, verify=False):
        """
        Selects the front or back button on the preview screen
        :param side: "front" or "back"
        :param verify: Verify the preview image changed
        """
        ui_obj = "double_sided_preview_{}_btn".format(side)
        if self.driver.get_attribute(ui_obj, "checked") == "true":
            logging.info("Already on {} image".format(side))
            return False
        if not verify:
            self.driver.click(ui_obj, change_check={"cc_type": "wait_for_attribute", "wait_obj": ui_obj, "wait_attribute": "checked"})
            return True
        init_img = saf_misc.load_image_from_base64(self.driver.screenshot_element("preview_img"))
        self.driver.click(ui_obj, change_check={"cc_type": "wait_for_attribute", "wait_obj": ui_obj, "wait_attribute": "checked"})
        sleep(3)
        assert saf_misc.img_comp(init_img, saf_misc.load_image_from_base64(self.driver.screenshot_element("preview_img")))
        return True

    def select_switch_paper_popup_btn(self, btn):
        """
        Select a button on the "Are you sure you want to switch paper?" popup
        :param btn: The button to select on the popup. "print", "switch" or "close"
        """
        self.driver.click("switch_paper_popup_{}_btn".format(btn), change_check={"wait_obj": "switch_paper_popup_title_txt", "invisible": True})

    def select_requires_two_sided_paper_popup_btn(self, btn):
        """
        Select a button on the "This print requires two-sided photo paper" popup
        :param btn: The button to select, "close" or "continue"
        """
        self.driver.click("double_sided_paper_popup_{}_btn".format(btn))

    def change_two_sided(self, two_sided):
        """
        change the 2-sided value to the value given
        :param two_sided:
        :return:
        """
        two_sided_obj_name = self.check_parameter_in_dict(two_sided)
        self.driver.scroll("double_sided_list_btn")
        self.driver.click("double_sided_list_btn")
        self.driver.wait_for_object(two_sided_obj_name, timeout=3)
        self.driver.click(two_sided_obj_name)

    def select_image_btn(self):
        """
        Click on Image on Preview Print button
        """
        self.driver.click("image_btn")

    def select_done_btn(self):
        """
        Click on Done button from Layout screen
        """
        self.driver.click("done_btn")

########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_select_printer_screen(self):
        """
        verify the select printer screen is visible
        :return:
        """
        self.driver.wait_for_object("select_printer_txt")

    def verify_search_printer_screen(self):
        """
        verify search text field screen is visible
        :return:
        """
        self.driver.wait_for_object("search_tf")

    def verify_printer_preview_screen(self, bonjour_name="", two_sided=False):
        """
        verify the pritner preview screen is visible
        :return:
        """
        self.driver.wait_for_object("print_btn", timeout=90)
        self.driver.wait_for_object("color_list_btn")
        self.driver.wait_for_object("copies_increment_btn")
        if bonjour_name:
            self.driver.wait_for_object("printer_name", format_specifier=[bonjour_name])
        if two_sided:
            self.driver.wait_for_object("double_sided_preview_front_btn")
            self.driver.wait_for_object("double_sided_preview_back_btn")

    def verify_selected_paper_size(self, paper_size):
        """
        Verify the selected printer paper size
        :param paper_size: The paper size to select. "4x6", "letter"
        """
        self.verify_printer_preview_screen()
        self.driver.wait_for_object(self.check_parameter_in_dict(paper_size))

    def verify_selected_color_mode(self, color_mode):
        """
        Verify the selected color mode
        :param color_mode: The color mode that is expected. "color" or "black_and_white"
        """
        self.verify_printer_preview_screen()
        self.driver.wait_for_object(self.check_parameter_in_dict(color_mode))

    def verify_switch_paper_popup(self):
        """
        Verify the "Are you sure you want to switch paper?" popup
         - Title text
         - "Print Two-Sided" button
         - "Switch Paper" button
        """
        self.driver.wait_for_object("switch_paper_popup_title_txt")
        self.driver.wait_for_object("switch_paper_popup_print_btn")
        self.driver.wait_for_object("switch_paper_popup_switch_btn")
        self.driver.wait_for_object("switch_paper_popup_close_btn")

    def verify_requires_two_sided_paper_popup(self):
        """
        Verify the "This print requires two-sided photo paper" popup
         - title text
         - body text
         - continue button
         - close button
        """
        self.driver.wait_for_object("double_sided_paper_popup_title_txt")
        self.driver.wait_for_object("double_sided_paper_popup_body_txt")
        self.driver.wait_for_object("double_sided_paper_popup_continue_btn")
        self.driver.wait_for_object("double_sided_paper_popup_close_btn")

    def verify_remote_preview_screen_with_print_button(self):
        """
        verify the remote printer print preview screen since bonjour name won't shown for remote print
        :return:
        """
        self.driver.wait_for_object("print_btn", timeout=90)

    def verify_image_layout_screen(self):
        """
        Verify Image layout screen after clicking on Image button
        """
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("done_btn")
        self.driver.wait_for_object("rotate_btn")
        self.driver.wait_for_object("resize_btn")

    def verify_paper_size_option_screen(self):
        """
        Verify paper size option screen
        """
        self.driver.scroll("paper_size_list_btn")
        self.driver.click("paper_size_list_btn")
        self.driver.wait_for_object("paper_ready_to_use_option")
        self.driver.wait_for_object("additional_paper_options")