from MobileApps.libs.flows.windows.hpx.hpx_flow import HPXFlow
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction


class HPPrivacySetting(HPXFlow):
    flow_name = "hp_privacysetting"

    def click_accept_all_button(self):
        self.driver.click("accept_all_btn")

    def click_decline_all_button(self):
        self.driver.click("decline_all_btn")
    
    def click_manage_options_button(self):
        self.driver.click("manage_options_btn")

    def verify_hp_privacy_subtitle_show(self):
        return self.driver.wait_for_object("privacy_subtitle_1", raise_e=False) is not False

    def verify_hp_privacy_show(self):
        return self.driver.wait_for_object("privacy_title", raise_e=False) is not False
    
    def check_privacy_title(self):
        return self.driver.get_attribute("privacy_title", "Name")
    
    def check_privacy_subtitle_1(self):
        return self.driver.get_attribute("privacy_subtitle_1", "Name")
    
    def check_privacy_subtitle_2(self):
        return self.driver.get_attribute("privacy_subtitle_2", "Name")
    
    def check_privacy_subtitle_3(self):
        return self.driver.get_attribute("privacy_subtitle_3", "Name")
    
    def verify_accept_button_show(self):
        return self.driver.wait_for_object("accept_all_btn", raise_e=False, timeout=30) is not False
    
    def verify_decline_button_show(self):
        return self.driver.wait_for_object("decline_all_btn") is not False
    
    def verify_manage_options_show(self):
        return self.driver.wait_for_object("manage_options_btn",raise_e=False,timeout=30) is not False
    
    def click_done_button(self):
        el = self.driver.find_object("done_button")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.66, height * 0.5)
    
    
    def click_yes_to_all(self):
        el = self.driver.find_object("privacy_consent_yes_to_all")
        width, height = el.rect["width"], el.rect["height"]
        self.driver.click_by_coordinates(el, width * 0.66, height * 0.5)

    def vreify_yes_to_all_btn(self):
        return self.driver.wait_for_object("privacy_consent_yes_to_all") is not False
    
    def click_hp_system_link(self):
        self.driver.click("hp_system_link")
        
    def check_localization_privacy_header_title(self):
        return self.driver.get_attribute("aboutprivacy_header", "Name")

    def check_localization_desc_customer_support(self):
        return self.driver.get_attribute("desc_customer_support", "Name")

    def check_localization_desc_learn_more(self):
        return self.driver.get_attribute("desc_learnmore_link", "Name")

    def check_localization_desc_news_offers(self):
        return self.driver.get_attribute("desc_news_offers", "Name")

    def check_localization_btn_accept_all(self):
        return self.driver.get_attribute("accept_all_btn", "Name")

    def check_localization_btn_decline_all(self):
        return self.driver.get_attribute("decline_all_btn", "Name")

    def check_localization_btn_manage_options(self):
        return self.driver.get_attribute("manage_options_btn", "Name")
    
    def verify_accept_all_btn_privacy(self):
        return self.driver.wait_for_object("accept_all_btn_privacy", raise_e=False, timeout=40) is not False
    
    def click_accept_all_btn_privacy(self):
        self.driver.click("accept_all_btn_privacy", raise_e=False, timeout=40)

