import logging
import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
from MobileApps.libs.flows.mac.smart.utility import smart_utilities

class Photos(SmartFlow):
    flow_name = "photos"

    RECENT_PHOTOS_TEXT = "recents_btn_txt"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_allow_access_to_photos_popup(self, allow_access=True, raise_e=False, timeout=3):
        """
        verifies the photos access popup, if it is there it will give access based on parameter value:
        :param allow_access: True default, if you want to check no access screen , set_to = False:
        :return:
        """
        if pytest.platform == "MAC":
            if allow_access:
                smart_utilities.handle_photos_access_popup(self.driver, 3)
            else:
                smart_utilities.handle_photos_access_popup(self.driver, 2)
        elif self.driver.wait_for_object("photos_access_popup_txt", timeout=10, raise_e=raise_e):
            if allow_access:
                self.driver.click("allow_access_btn")
            else:
                self.driver.click("do_not_allow_access_btn")
        else:
            logging.info("Current Screen did NOT contain the Allow Access photos pop up")

    def select_home_btn(self):
        """
        Selects the Home button
        """
        self.driver.click("home_btn")

    def select_all_files(self):
        """
        Selects all photos
        :return:
        """
        self.driver.click("all_files_btn")

    def select_albums_tab(self):
        """
        Selects Albums Tab from Photos & Files screen
        """
        self.driver.click("albums_tab")

    def verify_albums_tab(self):
        """
        Verify Albums Tab from Photos & Files screen
        """
        self.driver.wait_for_object("albums_tab")

    def select_close_btn(self):
        """
        Click on Close button on Choose your Printer screen
        """
        self.driver.click("close_btn")

    def select_recents_or_first_option(self):

        if self.driver.wait_for_object("recents_btn_txt", raise_e=False):
            self.driver.click("recents_btn_txt")
        else:
            self.driver.click("my_photos_first_option")

    def select_automation_text_album(self):
        self.driver.click("automation_text_album")

    def select_add_account(self):
        """
            Selects add Account
        """
        self.driver.click("add_account_btn")

    def select_remove_facebook(self):
        """
        Removes facebook from photos accounts
        :return:
        """
        cell_list = self.driver.find_object("album_cell_list")
        cells = cell_list.find_object("album_cell")
        logging.info("number of cells: {}".format(len(cells)))
        found = False
        for cell in cells:
            album_name = cell.find_object("cell_text")[0]
            logging.info("cell name: {}".format(album_name.get_attribute("name")))
            if album_name.get_attribute("name") == "Facebook":
                logging.info("Facebook Album found. Clicking X button!")
                cell.find_object("delete_btn").click()
                logging.info("Confirming Remove album accepted.")
                found = True
                break

        if not found:
            logging.info("Facebook delete button was not located on the screen")

    def select_photos_select_option(self):
        """
        Select the album detials select button
        :return:
        """
        self.driver.click("select_btn")

    def select_all_photos_option_select_all(self):
        """
        Select the album detials select button
        :return:
        """
        self.driver.click("select_all_btn")

    def select_multiple_photos(self, start=0, end=2):
        if self.driver.wait_for_object("select_btn", raise_e=False):
            self.driver.click("select_btn")
        all_photos_list = self.driver.find_object("all_photos", multiple=True)
        if len(all_photos_list) <= 0:
            raise NoSuchElementException
        for i in range(start, end):
            if i < len(all_photos_list):
                self.driver.click("all_photos", index=i)

    def select_next_button(self, change_check=None, raise_e=True):
        self.driver.click("next_btn", change_check=change_check, raise_e=raise_e)

    def select_photo_by_index(self, index=0):
        """
        selects the photo by index given
        :param index: int , 0 = first photo
        :return:
        """
        self.driver.wait_for_object("photos_lv")
        self.driver.click("photos_lv_xpath", index=index)

    def return_photos_count(self):
        """
        :return: returns the number of photos on Recents screen
        """
        return len(self.driver.find_object("photos_lv_xpath", multiple=True))
    
    def click_select_photos_option(self):
        if pytest.platform == "IOS":
            self.driver.click("select_photos")
        else:
            smart_utilities.handle_photos_access_popup(self.driver, 4)

    def select_access_btn(self):
        self.driver.click("access_btn")
    
    def select_set_photos_access_btn(self):
        self.driver.click("set_photo_access_btn")
    
    def select_show_selected_photos_btn(self):
        self.driver.click("show_selected_photos_btn")
    
    def select_screenshots_folder(self):
        self.driver.click("screenshot_folder")

    def select_first_printer_in_popup(self):
        """
        Chooses First printer in list and return the printer's name
        """
        printer_name = self.driver.get_attribute("first_printer_in_list_name", attribute="name")
        self.driver.click("first_printer_in_list")
        return printer_name
    
    def select_photos_to_access(self, index=1, count=None):
        """
        Selects the photos to access
        :param index: The index of the photo to select or to start from if count is provided
        :param count: The number of photos to select. If not provided, only one photo will be selected
        """
        if count is None:
            if index >= 12:
                number_of_swipes = index // 12
                for i in range(number_of_swipes):
                    self.driver.swipe(per_offset=0.89)
                # Adding 4 to the index because the first 4 photos are not on the screen
                index = (index % 12) + 4
            self.driver.click("photo_path_on_select_photos_screen", format_specifier=[index])
        else:
            for i in range(index, index + count):
                temp_index = i
                if i != 0 and i % 12 == 0:
                    self.driver.swipe(per_offset=0.89)
                    temp_index += 4
                self.driver.click("photo_path_on_select_photos_screen", format_specifier=[temp_index])

    def get_number_from_photo_selected_screen(self):
        """
        Get number of selected photos
        :return: number of selected photos
        """
        photo_selected_value = self.driver.get_attribute("number_of_photos_selected", attribute="value")
        return int(photo_selected_value[0])
        
########################################################################################################################
#                                                                                                                      #
#                                              VERIFICATION  FLOWS                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_add_account_screen(self):
        """
        verify add account screen
        :return:
        """
        self.driver.wait_for_object("facebook_btn")
        title = self.driver.find_object("add_account_title")
        if not title.get_attribute("name") == "Add Account":
            logging.info("Current Screen is not Add Account")

    def verify_photos_screen(self):
        """
        Verify Photos screen loaded with photos
        """
        return self.driver.wait_for_object("photos_lv", raise_e=False)

    def verify_no_photos_selected_screen(self):
        """
        Verify no photos selected on the screen
        """
        self.driver.wait_for_object("no_photos_selected")
        self.driver.wait_for_object("cancel_btn")

    def verify_my_photos_screen(self):
        """
        Verify my photos screen
        """
        self.driver.wait_for_object("my_photos_title")

    def verify_all_files_screen(self, raise_e=True):
        """
        Verify All files detail Screen
        :return:
        """
        return self.driver.wait_for_object("all_files_title", raise_e=raise_e)

    def verify_screen_with_select_all_options(self):
        """
        verifies the facebook album multi select screen
        :return:
        """
        self.driver.wait_for_object("select_all_btn")
        self.driver.wait_for_object("select_print_btn")

    def verify_multi_selected_photos_screen(self):
        """
        verifies the facebook album multi select screen
        :return:
        """
        self.driver.wait_for_object("next_btn")
    
    def verify_access_btn(self, raise_e=True):
        return self.driver.wait_for_object("access_btn", raise_e=raise_e)
            
    def verify_select_photos_btn(self):
        self.driver.wait_for_object("select_photos")
    
    def verify_allow_photos_access_page(self):
        self.driver.wait_for_object("access_btn")
        self.driver.wait_for_object("set_photo_access_btn")
    
    def verify_set_photo_access_btn(self, raise_e=True):
        return self.driver.wait_for_object("set_photo_access_btn", raise_e=raise_e)

    def get_photos_count_on_view_and_print_screen(self):
        if self.driver.wait_for_object("no_of_photos_preview_label", raise_e=False) is not False:
            photos_count = str(self.driver.get_attribute("no_of_photos_preview_label", attribute="label"))
            photos_count = photos_count.split()
            photos_count = int(photos_count[1])
        else:
            photos_count = 0
        return photos_count
    
    def verify_allow_access_to_photos(self):
        self.driver.wait_for_object("allow_access_btn")

    def verify_dont_allow_access_to_photos(self):
        self.driver.click("do_not_allow_access_btn")
    
    def verify_select_photos_page_after_popup(self):
        self.driver.wait_for_object("select_photos_page_after_popup")

    def verify_recent_photo_title(self):
        return self.driver.wait_for_object("recent_photos_title", raise_e=False)

    def verify_0_selected_title(self, timeout=10):
        """
        Verify the 0 selected title is present in the select photos screen
        """
        return self.driver.wait_for_object("0_selected_title", timeout=timeout, raise_e=False)

    def verify_albums_screen(self, raise_e=False):
        """
        Verify Albums screen loaded with albums
        """
        return self.driver.wait_for_object("albums_title", raise_e=raise_e)
    
    def verify_choose_printer_popup(self):
        self.driver.wait_for_object("choose_printer_popup")
    
    def verify_photos_access_screen(self):
        return self.driver.wait_for_object("photos_access_screen")