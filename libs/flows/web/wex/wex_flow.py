import math
import logging
import time
from datetime import datetime
from itertools import groupby 
from SAF.misc import saf_misc
from SAF.decorator.saf_decorator import native_context
from MobileApps.libs.flows.web.web_flow import WebFlow

class DeviceSearchException(Exception):
    pass

class PaginationException(Exception):
    pass

class NoEntriesMissingException(Exception):
    pass

class WrongToastException(Exception):
    pass

class StringComparisonException(Exception):
    pass

class PageOutOfBound(Exception):
    pass

class WrongPageException(Exception):
    pass

class IncorrectSortException(Exception):
    pass

class WEXFlow(WebFlow):
    project = "wex"

    def __init__(self, driver, context=None,  url=None):
        super(WEXFlow, self).__init__(driver, context=context, url=url)
        self.func_ignore_methods.append("load_wex_shared_ui")
        self.load_wex_shared_ui()

    def load_wex_shared_ui(self):
        ui_map = self.load_ui_map(system="WEB", project="jshell", flow_name="shared_obj")
        self.driver.load_ui_map("wex", "shared_obj", ui_map)
        return True
    
    ######################## Common object verify ############################################

    def verify_all_page_size_options(self, page_sizes, root_obj=None):
        self.verify_page_size_btn(root_obj=root_obj)
        self.click_page_size_btn(root_obj=root_obj)
        for size in page_sizes:
            self.driver.wait_for_object("_shared_page_size_menu_entry", format_specifier=[str(size)], root_obj=root_obj)
            logging.info("Page size: " + str(size) + " is avaliable")
        self.click_page_size_btn(root_obj=root_obj)
        return True
    
    def verify_page_size_btn(self, root_obj=None):
        return self.driver.wait_for_object("_shared_page_size_btn", root_obj=root_obj)

    def verify_page_nav(self, root_obj=None):
        return self.driver.wait_for_object("_shared_all_pages_btn", root_obj=root_obj)

    def verify_no_items_found(self, raise_e=True):
        return self.driver.wait_for_object('_shared_no_items_found_img', raise_e=raise_e)

    def verify_search_results(self, search_text):
        model_name_index = self.get_header_index("model_name")
        all_devices = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[model_name_index], multiple=True)
        for device_entry in all_devices:
            if search_text.lower() in device_entry.text.lower():
                continue
            else:
                raise DeviceSearchException("Device entry: " + device_entry.text + " does not contain the search string: " + search_text)
        return True

    def verify_table_displaying_correctly(self, page_size, page=1, root_obj=None):
        """
            Param - page_size -> Select this page size (depends on the table)
                    page -> Which page to test (Pass in None if you want to test current page)
                    root_obj -> Sometimes needed to speficially specify a table within the webpage
        """
        self.select_page_size(page_size, root_obj=root_obj)
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

    def verify_all_page_size_options(self, page_sizes, root_obj=None):
        actual_page_sizes = []
        self.verify_page_size_btn(root_obj=root_obj)
        self.click_page_size_btn(root_obj=root_obj)
        all_options = self.driver.find_object("_shared_page_size_menu_entry_new",multiple=True)
        for option in all_options:
            if option.text.strip():  # Check if the text is not empty or just whitespace
                actual_page_sizes.append(int(option.text))
        assert page_sizes == actual_page_sizes
        self.click_page_size_btn(root_obj=root_obj)
        return True

    def verify_header_column_loaded(self):
        self.driver.wait_for_object("_shared_all_table_header_column")

    ######################## Common flows #############################################

    def compare_strings(self, expected_value, actual_value ):
        if expected_value.lower() == actual_value.lower():
            return True
        else:
            raise StringComparisonException("Does not match. expected_value: "+expected_value+ " , actual_value: " +actual_value)

    def check_toast_successful_message(self, expected_message):
        actual_message = self.driver.wait_for_object("_shared_bottom_toast_message", timeout=30).text
        if actual_message == expected_message:
            return True
        else:
            raise WrongToastException("The toast message is: " + actual_message + " expected message is: " + expected_message)
    
    def get_header_index(self, header):
        self.verify_header_column_loaded()
        # Get all header elements (should be <th> only)
        all_headers = self.driver.find_object("_shared_all_table_header_column", multiple=True)
        target_header = self.driver.find_object(header + "_table_header")
        header_index = all_headers.index(target_header)

        # Get all cells in the first row (could be <th> or <td>)
        all_first_row_cells = self.driver.find_object("_shared_table_first_row_all_cells", multiple=True)
        # If the first cell is a <td>, then headers are shifted by 1
        if all_first_row_cells and all_first_row_cells[0].tag_name.lower() == "td":
            # Checkbox is a <td>, so add 2 to the index
            return header_index + 2
        else:
            # Checkbox is a <th> (or not present), so normal index
            return header_index + 1
    
    def click_page_size_btn(self, root_obj=None):
        self.driver.click("_shared_page_size_btn", root_obj=root_obj)
        if self.driver.wait_for_object("_shared_page_size_menu_box", timeout=30, displayed=False, raise_e=False) is False:
            self.driver.click("_shared_page_size_btn", root_obj=root_obj)
        return True

    def select_page_size(self, page_size, root_obj=None):
        self.click_page_size_btn(root_obj=root_obj)
        self.click_page_size_option_by_value(page_size, root_obj=root_obj)
        time.sleep(3)
        return True

    def click_page_size_option_by_value(self, value, root_obj=None):
        all_options = self.driver.find_object("_shared_page_size_menu_entry_new",multiple=True)
        for option in all_options:
            if option.text == str(value):
                return option.click()
        raise PaginationException("Page size: " + str(value) + " is not avaliable")

    def select_page(self, page, root_obj=None):
        #First and last btn are the arrows
        self.verify_page_nav(root_obj=root_obj)  
        current_page = self.get_current_page(root_obj=root_obj)
        if page == current_page:
            return True      
        page_objects = self.driver.find_object("_shared_all_pages_btn", multiple=True, root_obj=root_obj)[1:-1]
        total_pages = int(page_objects[-1].text)
        if page > total_pages:
            raise PageOutOfBound("Total pages: " + str(total_pages) + " desired page: " + str(page))

        elif page >= int(total_pages/2):
            page_objects[-1].click()
            click_until_found = self.click_next_nav
            total_clicks = total_pages - page
        else:
            click_until_found = self.click_next_nav
            total_clicks = page -1

        for _ in range(total_clicks):
            click_until_found(root_obj=root_obj)

        current_page = self.get_current_page(root_obj=root_obj)
        if current_page == page:
            time.sleep(3)
            return current_page
        else:
            raise WrongPageException("Expected page: " + str(page) + " ended up on: " + str(current_page))

    def get_current_page_size(self, root_obj=None):
        self.click_page_size_btn(root_obj=root_obj)
        size = self.driver.wait_for_object("_shared_page_size_menu_selected_entry", root_obj=root_obj).text
        self.click_page_size_btn(root_obj=root_obj)
        return size

    def click_prev_nav(self, root_obj=None):
        return self.driver.click("_shared_page_prev_nav_btn", root_obj=root_obj)

    def click_next_nav(self, root_obj=None):
        return self.driver.click("_shared_page_next_nav_btn", root_obj=root_obj)
    
    def get_current_page(self, root_obj=None):
        return int(self.driver.wait_for_object("_shared_current_page", root_obj=root_obj).text)

    def get_total_table_entries(self,total_len=True, root_obj=None):
        entries = self.driver.find_object("_shared_table_entries", multiple=True, root_obj=root_obj)
        if total_len:
            return len(entries)
        else:
            return entries
    
    def get_total_entries(self, root_obj=None):
        return int(self.driver.wait_for_object("_shared_page_size_total_txt", root_obj=root_obj).text.split("of ")[1])

    def get_max_page(self, root_obj=None):
        #I can use -2 but this is to make it clear
        #strip the left/right nav then the last one after that is the max page
        return int(self.driver.find_object("_shared_all_pages_btn", multiple=True, root_obj=root_obj)[1:-1][-1].text)

    def get_page_size_btn_txt(self, root_obj=None):
        return self.driver.wait_for_object("_shared_page_size_btn", root_obj=root_obj).text

    def click_first_entry_link(self):
        self.verify_table_loaded()
        return self.driver.click("_shared_table_entries_with_link")
    
    def verify_table_loaded(self, timeout=30):
        #Only works with table with a link in it, which is most tables
        #30 second timeout is the maxium timeout do not change
        return self.driver.wait_for_object("_shared_table_entries_with_link", timeout=timeout)
    
    def dismiss_toast(self, raise_e=False):
        #If you REQUIRE a toast to be there to be dismissed then change raise_e=True
        #Currently doesn't handle if there are more than 1 toast, if needed it can be added
        return self.driver.click("_shared_toast_close_btn", raise_e=raise_e)

    def click_table_header_by_name(self, header):
        self.verify_header_column_loaded()
        return self.driver.click(header + "_table_header")

    def verify_table_sort(self, field, sort_order):
        #Params: field -> Which field to check the order for 
        #        sort_order -> The order the field should follow 
        header_index = self.get_header_index(field)
        all_field = [i.text for i in self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[header_index], multiple=True)]
        order_set = [i[0] for i in groupby(all_field)]

        if not saf_misc.list_is_sub(order_set, sort_order):
            raise IncorrectSortException("Expected sort order: " + str(sort_order), " Actual sort order: " + str(order_set))
        return True

    def verify_proxies_table_sort(self, field, sort_order):
        # Params: field -> Which field to check the order for 
        #         sort_order -> The order the field should follow 
        header_index = self.get_header_index(field)
        all_field = [i.text.lower() for i in self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[header_index], multiple=True)]

        # Check if the field is 'last_updated' to handle date and time sorting
        if field == 'last_updated':
            date_format = "%d %b, %Y %I:%M %p"
            all_field = [datetime.strptime(date, date_format) for date in all_field]
            sort_order = [datetime.strptime(date, date_format) for date in sort_order]

        if all_field != sort_order:
            raise IncorrectSortException("Expected sort order: " + str(sort_order), " Actual sort order: " + str(all_field))
        return True

    def verify_printers_table_sort(self, field, sort_order):
        # Params: field -> Which field to check the order for
        #         sort_order -> The expected order (from test using sorted())
        self.select_page_size(500)  # Ensure the page size is set to 500 for the printers table
        header_index = self.get_header_index(field)
        all_field = [i.text for i in self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[header_index], multiple=True)]
        
        # Apply lexicographical rules to expected order (handle empty/"--")
        # Detect direction from sort_order
        non_empty_expected = [x for x in sort_order if x and x != '--']
        if len(non_empty_expected) > 1:
            is_ascending = non_empty_expected[0] < non_empty_expected[-1]
        else:
            # Just compare directly if we can't detect direction
            if all_field != sort_order:
                raise IncorrectSortException("Expected sort order: " + str(sort_order), " Actual sort order: " + str(all_field))
            return True
        
        # Apply proper empty/"--" positioning to expected data
        if is_ascending:
            # Ascending: empty first, then A-Z, then "--" last
            expected = sorted(sort_order, key=lambda x: (0 if x == '' else (2 if x == '--' else 1), x))
        else:
            # Descending: "--" first, then z-a, then empty last
            expected = sorted(sort_order, key=lambda x: (2 if x == '--' else (0 if x == '' else 1), x), reverse=True)
        
        if all_field != expected:
            raise IncorrectSortException("Expected sort order: " + str(expected), " Actual sort order: " + str(all_field))
        return True

    def verify_printers_assessment_table_sort(self, field, sort_order):
        # Special verification for assessment column with custom sort key
        # Does NOT apply lexicographical rules - expects sort_order is already correctly sorted
        self.select_page_size(500)
        header_index = self.get_header_index(field)
        all_field = [i.text for i in self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[header_index], multiple=True)]
        
        if all_field != sort_order:
            raise IncorrectSortException("Expected sort order: " + str(sort_order), " Actual sort order: " + str(all_field))
        return True

    def verify_event_log_table_sort(self, field, sort_order):
        # Params: field -> Which field to check the order for
        #         sort_order -> The order the field should follow
        header_index = self.get_header_index(field)
        all_field = [i.text.lower() for i in self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[header_index], multiple=True)
                     if i.text.lower() != '']

        # Check if total entries count is greater than 100, if yes navigate to next page and capture logs
        total_entries = self.get_total_entries()
        
        if total_entries > 100:
            if self.driver.get_attribute("_shared_page_prev_nav_btn","tabindex", raise_e=False) == "0":
                self.driver.click("_shared_page_prev_nav_btn")
            else:
                self.driver.click("_shared_page_next_nav_btn")
            all_field.extend([i.text.lower() for i in self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[header_index], multiple=True)
                              if i.text.lower() != ''])
        
        # Check if the field is 'last_updated' to handle date and time sorting
        if field == 'last_updated':
            date_format = "%d %b, %Y %I:%M %p"
            all_field = [datetime.strptime(date, date_format) for date in all_field]
            sort_order = [datetime.strptime(date, date_format) for date in sort_order]
 
        if all_field != sort_order:
            raise IncorrectSortException("Expected sort order: " + str(sort_order), " Actual sort order: " + str(all_field))
        return True