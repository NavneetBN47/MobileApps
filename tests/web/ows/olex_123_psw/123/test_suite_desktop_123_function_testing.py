import pytest
import time

pytest.app_info = "POOBE"

class Test_123_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_test_setup, request):
        self = self.__class__
        self.driver, self.fc, self.hpid = olex_123_test_setup
        self.stack = request.config.getoption("--stack")
        self.browser_type = request.config.getoption("--browser-type")
        self.hp_123 = self.fc.fd["hp_123"]
        
        """
        testRail:  https://hp-testrail.external.hp.com/index.php?/suites/view/3624&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=117965
        """
    def test_02_123_unsupported_region_or_language(self):
        self.navigate_and_verify_home_page()
        self.hp_123.mouse_hover_on_country_selector()
        self.hp_123.click_canada_country_selector_overlay()
        self.hp_123.verify_123_hp_page()
        assert "ca/en" in self.driver.get_current_url(), "URL is not as expected"
        self.hp_123.verify_selected_country("Canada")
        self.hp_123.verify_selected_country_flag("flag-ca")
        self.fc.clear_browsing_data_and_relaunch_flow(self.browser_type, url = self.hp_123.url_123.replace("us/en", "mo/fr"))
        assert "fr/fr" in self.driver.get_current_url(), "URL is not as expected"
        self.hp_123.input_search_text("HP Color LaserJet Enterprise MFP M480 series")
        self.hp_123.select_first_suggestion_after_entering_printer_name()
        self.hp_123.click_next_button()
        self.hp_123.verify_hp_easy_start_setup_content()
        self.hp_123.verify_app_store_images()
        self.hp_123.verify_install_hp_easy_start()

        # Add validation that a Software is being downloaded


    def test_03_download_hp_smart_on_win10_and_mac(self):
        self.navigate_and_verify_home_page(clear_browsing_data=True)
        self.hp_123.input_search_text("HP ENVY 6000 All-in-One Printer series")
        self.hp_123.select_first_suggestion_after_entering_printer_name()
        self.hp_123.click_next_button()
        self.hp_123.verify_install_hp_smart_button()
        self.hp_123.verify_header_nav()
        self.hp_123.click_deskjet_nav_header()
        self.hp_123.verify_deskjet_printer_family_page()
        self.driver.click_browser_back_button()
        self.hp_123.verify_apple_store_icon()
        self.hp_123.verify_android_store_icon()
        self.hp_123.verify_support_item_links()
        self.hp_123.click_solve_setup_issues_hyperlink()
        self.driver.add_window("setup_issues")
        self.driver.switch_window("setup_issues")
        assert "printer-setup" in self.driver.get_current_url(), "Current url is not printer-setup website"
        self.driver.close_window("setup_issues")
        self.hp_123.verify_support_item_links()
        self.hp_123.click_hp_support_hyperlink()
        self.driver.add_window("hp-support")
        self.driver.switch_window("hp-support")
        assert "support" in self.driver.get_current_url(), "user is not re-directed to Hp Support Website"
        self.driver.close_window("hp-support")
        self.navigate_and_verify_home_page(clear_browsing_data=True)
        self.hp_123.input_search_text("HP ENVY 6000e All-In-One Printer series")
        self.hp_123.select_first_suggestion_after_entering_printer_name()
        self.hp_123.click_next_button()
        time.sleep(1)
        self.hp_123.verify_hpplus_logo()
        self.hp_123.click_continue_with_computer_drop_down_arrow()
        self.hp_123.verify_install_hp_smart_button()

    def test_04_welcome_page(self):
        self.navigate_and_verify_home_page(clear_browsing_data=True)
        self.hp_123.verify_hp_logo_home_page()
        self.hp_123.verify_header_nav()
        self.hp_123.click_envy_nav_header()
        self.hp_123.verify_envy_printer_family_page()

        # Test search functionality with different printer family names
        printer_families = ["deskjet", "laserjet", "officejet"]
        for printer in printer_families:
            self.hp_123.input_search_text(printer)
            assert not self.hp_123.verify_printer_search_suggestions_list(raise_e=False), f"Search Suggestions is shown when {printer} is entered on Envy family page"
            assert not self.hp_123.verify_next_button(clickable=True, raise_e=False), f"Next button is clickable when {printer} is entered on Envy family page"
            self.hp_123.clear_search_text()
        
        self.hp_123.clear_search_text()
        self.hp_123.input_search_text("envy")
        self.hp_123.verify_printer_search_suggestions_list()
        self.driver.click_browser_back_button()
        assert self.hp_123.url_123 in self.driver.get_current_url(), "User is not re-directed to 123.hp.com page"
        self.hp_123.verify_123_hp_page_main_content()
        self.hp_123.click_wheres_the_product_name_hyperlink()
        self.hp_123.verify_find_product_name_modal()
        self.hp_123.verify_carousel_screen_owl_dots()
        self.hp_123.click_next_arrow_on_find_product_name_modal_and_verify_image()
        self.hp_123.click_close_button_on_find_product_name_modal()
        assert self.hp_123.verify_home_page_with_find_product_name_modal(raise_e=False) is False, "Find Product Name Modal is not closed"
        self.hp_123.click_my_device_is_not_listed_hyperlink()
        assert "other-printers" in self.driver.get_current_url(), "User is not re-directed to other-printers page"
        self.driver.click_browser_back_button()
        assert self.hp_123.url_123 in self.driver.get_current_url(), "User is not re-directed to 123.hp.com page"
        self.hp_123.input_search_text("^&*&*&")
        assert self.hp_123.verify_next_button(clickable=True, raise_e=False) is False, "Next button is clickable when a different printer family name is entered on Envy family page"
        self.hp_123.input_search_text("envy")
        self.hp_123.click_close_button_search_bar()
        self.hp_123.input_search_text("HP ENVY 6000e All-In-One Printer series", press_enter=True)
        assert "envy6000eseries" in self.driver.get_current_url(), "User is not re-directed to envy6000eseries page"


    ################## Private Function ##########################

    def navigate_and_verify_home_page(self, clear_browsing_data=False):
        if clear_browsing_data:
            self.fc.clear_browsing_data_and_relaunch_flow(self.browser_type, url = self.hp_123.url_123)
        self.hp_123.verify_123_hp_page_header()
        self.hp_123.verify_123_hp_page_main_content()
        self.hp_123.verify_123_hp_page()
        self.hp_123.verify_country_selector()
