from MobileApps.libs.flows.windows.hpx_rebranding.hpx_rebranding_flow import HPXRebrandingFlow
import logging

class ForYouPage(HPXRebrandingFlow):
    flow_name = "for_you_page"

# *********************************************************************************
#                                VERIFICATION FLOWS                               *
# *********************************************************************************

    def verify_shop_nav_pill(self):
        return self.driver.wait_for_object("shop_nav_pill")

    def verify_top_recommended_for_you(self):
        return self.driver.wait_for_object("top_recommended_for_you")

    def verify_shop_now(self):
        for _ in range(25):
            if self.driver.wait_for_object("shop_now", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        self.driver.wait_for_object("shop_now")
        return True

    def verify_shortcuts_section(self):
        for _ in range(25):
            if self.driver.wait_for_object("shortcuts_section",raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        self.driver.wait_for_object("shortcuts_section")
        return True

    def verify_your_digital_buddy(self):
        for _ in range(25):
            if self.driver.wait_for_object("your_digital_buddy", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("your_digital_buddy")

    def verify_looking_for_more(self):
        for _ in range(25):
            if self.driver.wait_for_object("looking_for_more", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("looking_for_more")

    def verify_visit_hpcom(self):
        for _ in range(25):
            if self.driver.wait_for_object("visit_hp_com", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("visit_hp_com")

    def verify_shop_by_product(self):
        for _ in range(25):
            if self.driver.wait_for_object("shop_by_product", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("shop_by_product")

    def verify_printers(self):
        for _ in range(25):
            if self.driver.wait_for_object("printers", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("printers")

    def verify_accessories(self):
        for _ in range(25):
            if self.driver.wait_for_object("accessories", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("accessories")

    def verify_laptops(self):
        for _ in range(25):
            if self.driver.wait_for_object("laptops", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("laptops")

    def verify_monitors(self):
        for _ in range(25):
            if self.driver.wait_for_object("monitors", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("monitors")

    def verify_featured_offers(self):
        for _ in range(25):
            if self.driver.wait_for_object("featured_offers", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("featured_offers")

    def verify_noise_free_sound(self):
        return self.driver.wait_for_object("noise_free_sound")

    def verify_do_more_with_pen(self):
        return self.driver.wait_for_object("do_more_with_pen")

    def verify_shop_now_webview_title(self):
        if self.driver.wait_for_object("get_shop_now_webview_title", timeout=20, raise_e=False) != False:
            logging.info("Webview page is opened")
            logging.info("Web Page Title: " + self.driver.wait_for_object("get_shop_now_webview_title").get_attribute("Name"))
            return True
        else:
            logging.error("Webview page is NOT opened")
            return False

    def verify_learn_more_webview_page(self):
        if self.driver.wait_for_object("get_learn_more_webview_title", timeout=20, raise_e=False) != False:
            logging.info("Webview page is opened")
            logging.info("Web Page Title: " + self.driver.wait_for_object("get_learn_more_webview_title").get_attribute("Name"))
            return True
        else:
            logging.error("Webview page is NOT opened")
            return False

    def verify_order_now_webview_page(self):
        if self.driver.wait_for_object("get_order_now_webview_title", timeout=20, raise_e=False) != False:
            logging.info("Webview page is opened")
            logging.info("Web Page Title: " + self.driver.wait_for_object("get_order_now_webview_title").get_attribute("Name"))
            return True
        else:
            logging.error("Webview page is NOT opened")
            return False

    def verify_order_yours_today_webview_page(self):
        if self.driver.wait_for_object("get_order_yours_today_webview_title", timeout=20, raise_e=False) != False:
            logging.info("Webview page is opened")
            logging.info("Web Page Title: " + self.driver.wait_for_object("get_order_yours_today_webview_title").get_attribute("Name"))
            return True
        else:
            logging.error("Webview page is NOT opened")
            return False

    def verify_order_yours_today_link(self):
        for _ in range(25):
            if self.driver.wait_for_object("order_yours_today_link", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("order_yours_today_link")

    def verify_hp_ai_assistant(self):
        return self.driver.wait_for_object("hp_ai_assistant")

    def verify_create_account(self):
        return self.driver.wait_for_object("create_account")

    def verify_sign_in_btn(self):
        return self.driver.wait_for_object("sign_in_btn")

    def verify_unlock_more_with_your_hp_account(self):
        return self.driver.wait_for_object("unlock_more_with_your_hp_account")

    def verify_laptops_image_show_up(self):
        for _ in range(25):
            if self.driver.wait_for_object("laptops_image", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("laptops_image")

    def verify_printers_image_show_up(self):
        for _ in range(25):
            if self.driver.wait_for_object("printers_image", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("printers_image")

    def verify_accessories_image_show_up(self):
        for _ in range(25):
            if self.driver.wait_for_object("accessories_image", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("accessories_image")

    def verify_monitors_image_show_up(self):
        for _ in range(25):
            if self.driver.wait_for_object("monitors_image", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("monitors_image")

    def verify_order_now_link(self):
        for _ in range(25):
            if self.driver.wait_for_object("order_now_link", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("order_now_link")

    def verify_learn_more_link(self):
        for _ in range(25):
            if self.driver.wait_for_object("learn_more_link", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("learn_more_link")

    def verify_visit_hpcom_webview_page(self):
        if self.driver.wait_for_object("get_visit_hpcom_webview_title", timeout=20, raise_e=False) != False:
            logging.info("Webview page is opened")
            logging.info("Web Page Title: " + self.driver.wait_for_object("get_visit_hpcom_webview_title").get_attribute("Name"))
            return True
        else:
            logging.error("Webview page is NOT opened")
            return False

    def verify_try_feature(self):
        for _ in range(25):
            if self.driver.wait_for_object("try_feature", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("try_feature")

    def verify_work_smarter_with_hp_shortcuts(self):
        for _ in range(25):
            if self.driver.wait_for_object("work_smarter_with_hp_shortcuts", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("work_smarter_with_hp_shortcuts")

    def verify_work_smarter_with_shortcuts_image(self):
        for _ in range(25):
            if self.driver.wait_for_object("work_smarter_with_shortcuts_image", raise_e=False) is False:
                self.driver.swipe()
            else:
                break
        return self.driver.wait_for_object("work_smarter_with_shortcuts_image")

    def verify_digital_buddy_title(self):
        return self.driver.wait_for_object("digital_buddy_title")

    def verify_digital_buddy_description(self):
        return self.driver.wait_for_object("digital_buddy_description")

    def verify_digital_buddy_image(self):
       return self.driver.wait_for_object("digital_buddy_image")

    def verify_digital_buddy_close_btn(self):
        return self.driver.wait_for_object("digital_buddy_close_btn")
    
    def verify_digital_buddy_back_btn(self):
        return self.driver.wait_for_object("digital_buddy_back_btn")

# *********************************************************************************
#                                ACTION FLOWS                                     *
# *********************************************************************************

    def click_printers(self):
        self.driver.click("printers")

    def click_accessories(self):
        self.driver.click("accessories")

    def click_laptops(self):
        self.driver.click("laptops")

    def click_monitors(self):
        self.driver.click("monitors")

    def click_shop_now(self):
        self.driver.click("shop_now")

    def click_hp_ai_assistant(self):
        self.driver.click("hp_ai_assistant")

    def click_shop_nav_pill(self):
        self.driver.click("shop_nav_pill")

    def click_order_now_link(self):
        self.driver.click("order_now_link")

    def click_learn_more_link(self):
        self.driver.click("learn_more_link")

    def click_order_yours_today_link(self):
        self.driver.click("order_yours_today_link")

    def click_visit_hpcom(self):
        self.driver.click("visit_hp_com")

    def click_shortcuts_section(self):
        self.driver.click("shortcuts_section")

    def click_your_digital_buddy_section(self):
        self.driver.click("your_digital_buddy")  

    def click_digital_buddy_close_btn(self):
        self.driver.click("digital_buddy_close_btn")
