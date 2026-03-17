import time 
import math
import logging
from MobileApps.libs.flows.web.base_web_flow import BaseWebFlow
from MobileApps.libs.flows.web.web_flow import WebFlow
from MobileApps.libs.ma_misc import ma_misc
from bs4 import BeautifulSoup as bsoup
from time import sleep

class StringComparisonException(Exception):
    pass

class PaginationException(Exception):
    pass

class NoEntriesMissingException(Exception):
    pass

class SMBFlow(BaseWebFlow, WebFlow):
    project = "smb"

    def __init__(self, driver, context=None,  url=None):
        super(SMBFlow, self).__init__(driver, context=context, url=url)

    
    def compare_strings(self, expected_value, actual_value ):
        if expected_value.lower() == actual_value.lower():
            return True
        else:
            raise StringComparisonException("Does not match. expected_value: "+expected_value+ " , actual_value: " +actual_value)
    
    def get_header_index(self, header):
        self.verify_header_column_loaded()
        all_headers = self.driver.find_object("_shared_all_table_header_column", multiple=True)
        header = self.driver.find_object(header + "_table_header")
        return all_headers.index(header) + 1
    
     # Temporarily having below four copied method untill all the MFE are developed usinng the new verneer table pagination
    def verify_table_displaying_correctly_new(self, page_size, page=1, root_obj=None):
        """
            Param - page_size -> Select this page size (depends on the table)
                    page -> Which page to test (Pass in None if you want to test current page)
                    root_obj -> Sometimes needed to speficially specify a table within the webpage
        """
        self.select_page_size_new(page_size, root_obj=root_obj)
        if page != None:
            current_page = self.select_page(page, root_obj=root_obj)
        else:
            current_page = self.get_current_page(root_obj=root_obj)

        total_entries = self.get_total_entries(root_obj=root_obj)
        actual_max_page = self.get_max_page(root_obj=root_obj)
        page_size_btn_num = list(map(int, self.get_page_size_btn_txt(root_obj=root_obj).split(" - ")))

        if total_entries == 0:
            if self.driver.wait_for_object("_shared_no_items_found_img", root_obj=root_obj, raise_e=False) is False:
                raise NoEntriesMissingException("Total entry is 0. But 'No Items found' is not displayed")
            max_page = math.ceil(total_entries/page_size) + 1
            total_visible_entries = self.get_total_table_entries(root_obj=root_obj) -1
            expected_from = 0
        else:
            max_page = math.ceil(total_entries/page_size)
            total_visible_entries = self.get_total_table_entries(root_obj=root_obj)
            expected_from = current_page*page_size-total_visible_entries - (page_size - total_visible_entries) +1

        expected_to = current_page*page_size - (page_size - total_visible_entries)

        if actual_max_page != max_page:
            raise PaginationException("Expected total page: " + str(max_page) + " != Actual total page: " + str(actual_max_page))

        if page_size_btn_num != [expected_from, expected_to]:
            raise PaginationException("Entry indicator: " + str(page_size_btn_num) + " Expecting: " + str([expected_from, expected_to]))
        return True

    def verify_all_page_size_options_new(self, page_sizes, root_obj=None,timeout=50):
        actual_page_sizes = []
        self.verify_page_size_btn(root_obj=root_obj)
        self.click_page_size_btn(root_obj=root_obj)
        all_options = self.driver.find_object("_shared_page_size_menu_entry_new",multiple=True)
        for option in all_options:
            value = (int(option.text))
            actual_page_sizes.append(value)
        assert page_sizes == actual_page_sizes
        self.click_page_size_btn(root_obj=root_obj)
        return True

    def click_page_size_option_by_value_new(self, value, root_obj=None,timeout=30):
        all_options = self.driver.find_object("_shared_page_size_menu_entry_new",multiple=True)
        for option in all_options:
            if option.text == str(value):
                return option.click()
        raise PaginationException("Page size: " + str(value) + " is not avaliable")

    def select_page_size_new(self, page_size, root_obj=None,timeout=30):
        self.click_page_size_btn(root_obj=root_obj)
        self.click_page_size_option_by_value_new(page_size, root_obj=root_obj)
        time.sleep(3)
        return True

    def filter_and_load_file_path_based_on_language(self, root_path, language):
        # Loop through the directory and return all file paths
        file_path_list = ma_misc.loop_through_directory_and_return_file_path(root_path)
        # Filter the file paths based on the specified language
        file_list = [file for file in file_path_list if language in file]
        return file_list
    
    def load_files_and_create_single_layer_dict(self, specific_language_file_list):
        
        # This function takes a list of files (specific_language_file_list) as input.
        # It reads each file, creates a dictionary from it and merges it into a single dictionary.
        # The final single layer dictionary is then returned.

        all_spec_data = {}

        # Loop through each file in the specific_language_file_list
        for file in specific_language_file_list:
            spec_data = self.get_key_modified_dictionary_from_spec(file)
            all_spec_data.update(spec_data)
        return all_spec_data