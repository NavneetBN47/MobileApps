from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare
import time
import logging


class HP123(OWSFlow):
    """
    Contains All methods for https://123.hp.com, https://123-stage.hpoobe.com, https://123-test.hpoobe.com
    """
    file_path = __file__
    flow_name = "123_hp"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def __init__(self, driver, window_name=None):
        super(HP123, self).__init__(driver)
        self.wn = window_name if window_name is not None else logging.warning("123 page flow init without window_name, please add it in before using it")
        self.stack = self.driver.session_data["stack"]
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        self.url_123 = "https://123-{}.hpoobe.com/{}".format(self.stack, self.locale) if self.stack != "prod" else "https://123.hp.com"


########################################################################################################################
#                                                                                                                      #
#                                               Action Flows                                                           #
#                                                                                                                      #
########################################################################################################################

    def click_deskjet_nav_header(self):
        """
        Clicks on the "deskjet_nav" element in the header navigation.
        """
        self.driver.click("deskjet_nav")
    
    def click_envy_nav_header(self):
        """
        Clicks on the envy_nav header element.
        """
        self.driver.click("envy_nav")
    
    def mouse_hover_on_country_selector(self, seconds=1):
        """
        Mouse hover on country selector on 123 site
        """
        self.driver.perform_mouse_hover_action("country_selector_hover_button", pause_seconds=seconds)

    def click_canada_country_selector_overlay(self):
        """
        This is a tooltip webelement not interactable so click won't perform so instead verify href property which has the re-direct url
        """
        assert "123" and "ca/en" in self.driver.get_attribute("canada_en", "href", displayed=False), "Re-direct URL is either not 123 or not canada region"
        if self.stack != "prod":
            self.driver.navigate(f"https://123-{self.stack}.hpoobe.com/ca/en")
        else:
            self.driver.navigate("https://123.hp.com/ca/en")

    def input_search_text(self, search_text, press_enter=False):
        """
        Input search text in search bar
        """
        self.driver.send_keys("enter_product_name", search_text, press_enter=press_enter)
        
    def click_close_button_search_bar(self):
        """
        Clicks the close button on the search bar
        """
        self.driver.click("close_button_search_bar")
    
    def select_first_suggestion_after_entering_printer_name(self):
        """
        Click on the first suggestion after entering the printer name
        """        
        self.driver.click("first_suggestion_after_entering_printer_name")

    def clear_search_text(self):
        """
        Clear the search text in the search bar
        """
        self.driver.clear_text("enter_product_name")
    
    def click_next_button(self):
        """
        Clicks the next button on the page.
        """
        self.driver.click("next_button")

    def click_wheres_the_product_name_hyperlink(self):
        """
        Clicks the "Where's the product name?" link
        """
        self.driver.click("wheres_the_product_name_hyperlink")
    
    def click_my_device_is_not_listed_hyperlink(self):
        """
        Clicks the "My device is not listed" hyperlink
        """
        self.driver.click("my_device_is_not_listed_hyperlink")
    
    def click_install_hp_easy_start(self):
        self.driver.click("install_hp_easy_start")

    def click_solve_setup_issues_hyperlink(self):
        self.driver.click("solve_setup_issues_hyperlink")

    def click_hp_support_hyperlink(self):
        self.driver.click("hp_support_hyperlink")

    def click_continue_with_computer_drop_down_arrow(self):
        self.driver.click("continue_with_computer_drop_down_arrow")

    def click_next_arrow_on_find_product_name_modal_and_verify_image(self):
        """
        Clicks the next arrow on the find product name modal and verifies the image shown to the user
        """
        image_list = ["3m_printer_image", "vasari_printer_image", "horizon_printer_image", "taccola_printer_image", "printer_name_box"]
        for i in image_list:
            self.driver.process_screenshot(self.file_path, file_name=i, root_obj=i)
            if i != "printer_name_box":
                self.driver.click("find_product_name_modal_next_slide")
            assert self.url_123 in self.driver.get_current_url(), "URL chnaged with clicking right arrow on modal"
        for i in reversed(image_list):
            self.driver.wait_for_object(i)
            self.driver.click("find_product_name_modal_prev_slide")
        
    def click_close_button_on_find_product_name_modal(self):
        """
        Clicks the close button on the find product name modal
        """
        self.driver.click("find_product_name_modal_close_button")


########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    @screenshot_compare(root_obj="hp_plus_logo")
    def verify_hpplus_logo(self):
        self.driver.wait_for_object("hp_plus_logo")

    @screenshot_compare(root_obj="hp_logo")
    def verify_hp_logo_home_page(self):
        self.driver.wait_for_object("hp_logo")
    
    def verify_123_hp_page_header(self):
        self.driver.wait_for_object("123_hp_page_header")

    def verify_123_hp_page_main_content(self):
        self.driver.wait_for_object("123_hp_main_content")
        self.driver.process_screenshot(self.file_path, ("123_main_content"), root_obj="123_hp_main_content")
    
    @screenshot_compare(root_obj="123_home_page_printer_image")
    def verify_123_hp_page(self):
        self.driver.wait_for_object("123_hp_page")
        assert "officejet" in self.driver.get_attribute("enter_product_name", "placeholder").lower(), "Search bar placeholder Does not have the default family printer name"

    def verify_123_search_bar(self):
        self.driver.wait_for_object("search_bar")

    def verify_selected_country(self, country):
        assert self.driver.get_attribute("country_selector_hover_button", "text") == country, "Country Shown is not as expected"
    
    def verify_selected_country_flag(self, country_flag):
        assert country_flag in self.driver.get_attribute("country_selector_flag", "class") , "Country Flag is not as expected"
    
    def verify_next_button(self, clickable=False, raise_e=True):
        """
        Clicks the next button on the page. Also check for clickability of the next button
        """
        return self.driver.wait_for_object("next_button", clickable=clickable, raise_e=raise_e)
    
    @screenshot_compare(root_obj="home_page_with_find_product_name_modal")
    def verify_find_product_name_modal(self):
        self.driver.wait_for_object("find_product_name_modal")
        self.driver.process_screenshot(self.file_path, ("find_product_name_modal"), root_obj="find_product_name_modal")
        self.driver.wait_for_object("find_product_name_modal_next_slide")
        self.driver.wait_for_object("find_product_name_modal_prev_slide")
    
    def verify_home_page_with_find_product_name_modal(self, raise_e=True):
        return self.driver.wait_for_object("home_page_with_find_product_name_modal", raise_e=raise_e)    
    
    @screenshot_compare(root_obj="header_nav")
    def verify_header_nav(self):
        self.driver.wait_for_object("header_nav")
    
    def verify_printer_model_content_subline(self, printer_type):
        assert printer_type in self.driver.get_attribute("printer_model_content_subline", "text").lower(), "Content Subline does not have the correct printer type"
    
    def verify_printer_search_suggestions_list(self, raise_e=True):
        return self.driver.wait_for_object("printer_search_suggestions_list", raise_e=raise_e)
    
    @screenshot_compare(root_obj="printers_page_search_bar_section")
    def verify_printer_page_search_bar_section(self):
        self.driver.wait_for_object("printers_page_search_bar_section")
    
    @screenshot_compare(root_obj="home_page_content")
    def verify_home_page_content(self):
        self.driver.wait_for_object("home_page_content")
    
    def verify_printer_image(self, image_type):
        assert image_type in self.driver.get_attribute("printer_image"), "Image Shown to the user not as expected"
    
    def verify_123_bottom_section_content(self):
        self.driver.wait_for_object("bottom_section_content")

    def verify_addition_help_hp_support_hyperlink(self):
        self.driver.wait_for_object("addition_help_hp_support_hyperlink") 
    
    @screenshot_compare(root_obj="envy_printer_family_image")
    def verify_envy_printer_family_page(self):
        """
        Verify the Envy printer family page
        """
        assert "printers/envy" in self.driver.get_current_url(), "User did not get re-directed to Envy printers page"
        assert "envy" in self.driver.get_attribute("enter_product_name", "placeholder").lower(), "Search bar placeholder Does not have the Envy family printer name"
        self.verify_printer_model_content_subline("envy")
    
    @screenshot_compare(root_obj="deskjet_printer_family_image")
    def verify_deskjet_printer_family_page(self):
        """
        Verify the Envy printer family page
        """
        assert "printers/deskjet" in self.driver.get_current_url(), "User did not get re-directed to Envy printers page"
        assert "deskjet" in self.driver.get_attribute("enter_product_name", "placeholder").lower(), "Search bar placeholder Does not have the Envy family printer name"
        self.verify_printer_model_content_subline("deskjet")
    
    def verify_country_selector(self):
        self.driver.wait_for_object("country_selector_hover_button")

    def verify_hp_easy_start_setup_content(self):
        self.driver.wait_for_object("hp_easy_start_setup_content")

    def verify_app_store_images(self):
        self.driver.wait_for_object("app_store_images")

    def verify_install_hp_easy_start(self):
        self.driver.wait_for_object("install_hp_easy_start")

    def verify_install_hp_smart_button(self):
        self.driver.wait_for_object("install_hp_smart_button")

    def verify_apple_store_icon(self):
        self.driver.wait_for_object("apple_store_icon")

    def verify_android_store_icon(self):
        self.driver.wait_for_object("android_store_icon")

    def verify_support_item_links(self):
        self.driver.wait_for_object("support_item_links")