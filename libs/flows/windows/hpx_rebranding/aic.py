import logging
from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from SAF.decorator.saf_decorator import screenshot_compare


class Aic(HPXRebrandingFlow):
    flow_name = "aic"

    def verify_ask_me_anything_text_box_ltwo(self):
        return self.driver.wait_for_object("ask_me_anything_text_box_ltwo", raise_e=False, timeout=20)
    
    def click_aic_window(self,iteration=1):
        time.sleep(5)
        el = self.driver.wait_for_object("aic_windows", timeout=10)
        for _ in range(iteration):
            el.send_keys(Keys.TAB)
    
    def enter_text_in_search_box(self,text):
        time.sleep(5)        
        self.driver.send_keys("ask_me_anything_text_box_ltwo", text)
  
    def click_ask_me_anything_searchbox_arrow_button_ltwo(self):
        self.driver.click("ask_me_anything_searchbox_arrow_button_ltwo", timeout=10)

    def click_wheel_of_fun_button_ltwo(self):
        self.driver.click("wheel_of_fun_button_ltwo", timeout=10)

    def click_wheel_of_fun_item_on_home_page(self,element):
        time.sleep(5)
        el = self.driver.wait_for_object(element, raise_e=False, timeout=10)
        el.send_keys(Keys.TAB)
        el.send_keys(Keys.ENTER)

    def click_wheel_of_fun_item_on_result_page(self,element):
        time.sleep(3)
        el = self.driver.wait_for_object(element, raise_e=False, timeout=10)
        el.send_keys(Keys.TAB)
        el.send_keys(Keys.ENTER)

    def focus_collapse_expand_chevron_lthree_page(self):
        el=self.driver.wait_for_object("aic_windows", timeout=10)
        for _ in range(7):
            el.send_keys(Keys.TAB)
            el.send_keys(Keys.ENTER)

    def click_collapse_expand_chevron_lthree_page(self):
        self.driver.click("collapse_chevron_lthree_page", timeout=10)

    def click_copy_button(self,index=0):
        self.driver.click("copy_button",index=index, timeout=30)

    def scroll_up_down(self, distance=1,direction="down"):
        el=self.driver.wait_for_object("aic_windows", timeout=10)
        for _ in range(distance):
            if direction == "down":
                el.send_keys(Keys.PAGE_DOWN)
            elif direction == "up":
                el.send_keys(Keys.PAGE_UP)

    def get_hello_text(self):
        return self.driver.get_attribute("hello_text_on_aic_home_page", "Name", timeout=15)
    
    def get_how_can_i_help_you_text(self):
        return self.driver.get_attribute("how_can_help_you_text_on_aic_home_page", "Name", timeout=15)
    
    def verify_wheel_of_fun_present_root_page(self):
        return self.driver.wait_for_object("wheel_of_fun_item_on_home_page", raise_e=False, timeout=20)
    
    def is_arrow_button_enabled(self):
        self.driver.wait_for_object("ask_me_anything_searchbox_arrow_button_ltwo",raise_e=False, timeout=10)
        return self.driver.get_attribute("ask_me_anything_searchbox_arrow_button_ltwo", "IsEnabled", raise_e=False, timeout=10)
    
    def verify_response_page(self):
        return self.driver.wait_for_object("response_card_1", raise_e=False, timeout=20)

    def press_enter_on_arrow_button_ltwo(self):
        # Try direct click first
        try:
            self.driver.click("ask_me_anything_searchbox_arrow_button_ltwo", timeout=10)
            time.sleep(1)
        except:
            # Fallback to keyboard navigation if direct click fails
            try:
                search_box = self.driver.wait_for_object("ask_me_anything_text_box_ltwo", timeout=10)
                search_box.send_keys(Keys.TAB)  # TAB to move focus to arrow button
                time.sleep(0.5)
                search_box.send_keys(Keys.ENTER)  # Press ENTER on the focused arrow button
                time.sleep(1)
            except:
                # Final fallback - try clicking arrow button with ActionChains
                arrow_button = self.driver.wait_for_object("ask_me_anything_searchbox_arrow_button_ltwo", timeout=10)
                ActionChains(self.driver.driver).click(arrow_button).perform()
                time.sleep(1)

    def click_stop_icon_button_ltwo(self):
        self.driver.click("stop_icon_button_ltwo", timeout=10)

    def get_copy_text(self):
        return self.driver.get_attribute("copy_button", "Name", timeout=15)   

    def get_response_intent_title(self):
        return self.driver.get_attribute("intent_response_page", "Name", timeout=15)

    def press_keyboard_to_close_app(self):
        el = self.driver.wait_for_object("aic_windows", timeout=10)
        try:
            ActionChains(self.driver.driver).key_down(Keys.ALT).send_keys(Keys.F4).key_up(Keys.ALT).perform()
            time.sleep(2)
        except:
            # Method 2: Alternative approach - focus element and try Alt+F4 directly
            el.click()  # Focus the window first
            time.sleep(1)
            el.send_keys(Keys.ALT, Keys.F4)  # Send keys separately
            time.sleep(2)

    def get_response_intent_results(self):
        return self.driver.get_attribute("response_result", "Name", timeout=15)
    
    def validate_brightness_response_pattern(self):    
        response_text = self.get_response_intent_results()
        if "Your displays brightness" in response_text:
            return True
        else:
            logging.warning(f"Brightness response validation failed. Actual text: '{response_text}'")
            return False    

    def validate_different_response_card(self):
        time.sleep(5)
        el1 = self.driver.wait_for_object("response_card_1", timeout=10)
        el2 = self.driver.wait_for_object("response_card_2", timeout=10)
        if not el1 or not el2:
            logging.warning("Response card is not present.")
            return False
        return el1, el2

    def click_search_box_result_page(self, iteration=1):
        time.sleep(5)
        el = self.driver.wait_for_object("search_box_result_page", timeout=10)
        for _ in range(iteration):
            el.send_keys(Keys.TAB)

    def verify_aic_app_in_lzero_header(self):
        return self.driver.wait_for_object("aic_button_on_lzero_header", raise_e=False, timeout=20)     

    def get_response_body(self):
        el = self.driver.wait_for_object("response_body", raise_e=True, timeout=20)
        logging.info(f"Response body element text: {el.text}")
        logging.info(f"Response body element Name attribute: {el.get_attribute('Name')}")
        return self.driver.get_attribute("response_body", "Name", timeout=15)

    def click_input_box(self, locator, iteration=1):
        time.sleep(5)
        el = self.driver.wait_for_object(locator, timeout=10)
        for _ in range(iteration):
            el.send_keys(Keys.TAB)
            logging.info(f"Sent TAB key {el.get_attribute('Name')}")
            logging.info(f"Sent TAB key {el.text}")
    
    @screenshot_compare(root_obj="search_box_result_page",include_param=["machine_type"],pass_ratio=0.02)
    def verify_perform_aic_ltwo_page(self,machine_type,raise_e=True):
        return self.driver.wait_for_object("search_box_result_page", raise_e=raise_e, timeout=10)