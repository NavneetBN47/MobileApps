import time
import pytest
from MobileApps.libs.flows.web.web_flow import WebFlow


class HelpSupport(WebFlow):
    project = "help_support"
    flow_name = "help_support"

    CHAT_WITH_VIRTUAL_ASSISTANT_LINK = "chat_with_virtual_assistant_btn"
    CONTACT_HP_LINK = "contact_hp_btn"
    PRINTER_SUPPORT_LINK = "print_support_link"
    PRINT_ANYWHERE_ONLINE_SUPPORT_LINK = "print_anywhere_online_support_link"
    SHORTCUTS_ONLINE_SUPPORT_LINK = "shortcuts_online_supoort_link"
    HP_MOBILE_PRINTING_LINK = "hp_mobile_printing_link"
    DIAGNOSE_FIX_LINK = "diagnose_fix_link"
    DOWNLOAD_HERE_LINK = "download_here_link"

    FINDING_YOUR_PRINTER_ITEM = "finding_your_printer_item"
    CONNECTING_TO_YOUR_PRINTER_ITEM = "connecting_to_your_printer_item"
    PRINTING_ITEM = "printing_item"
    SCANNING_ITEM = "scanning_item"
    SHORTCUTS_ITEM = "shortcuts_item"
    FAX_ITEM = "fax_item"

    CHAT_WITH_VIRTUAL_ASSISTANT_URL = ["hpcloud.hp.com"]
    CONTACT_HP_URL = ["support.hp.com"]
    PRINTER_SUPPORT_URL = ["h20180.www2.hp.com/apps/Lookup"]
    PRINT_ANYWHERE_ONLINE_SUPPORT_URL = ["support.hp.com"]
    SHORTCUTS_ONLINE_SUPPORT_URL = ["support.hp.com"]
    HP_MOBILE_PRINTING_URL = ["https://support.hp.com/us-en/document/ish_2843711-2427128-16"]
    FAX_DRIVER_DOWNLOAD_URL = ["https://support.hp.com/us-en/drivers/hp-universal-fax-driver-series-for-windows/7529318?openCLC=true"]

    def verify_help_center_screen(self, timeout=30):
        """
        Verifying Help Center screen via title: "Welcome to HP Smart App Help and Support"
        """
        self.driver.wait_for_object("contact_hp_btn", timeout=timeout)

    def verify_help_center_printing_screen(self, timeout=30):
        """
        Verifying the printing screen after clicking printing item on Help Center screen.
        """
        self.driver.wait_for_object("diagnose_fix_link", timeout=timeout)

    def verify_chat_with_virtual_assistant_btn(self, timeout=10, raise_e=True):
        """
        Verifying Chat With Virtual Assistant button on Help Center screen
        """
        return self.driver.wait_for_object("chat_with_virtual_assistant_btn", timeout=timeout, raise_e=raise_e)

    def verify_chat_with_virtual_assistant_content(self, timeout=10, raise_e=True):
        """
        Verifying Chat With Virtual Assistant content on Help Center screen
        """
        return self.driver.wait_for_object("chat_with_virtual_assistant_content", timeout=timeout, raise_e=raise_e)

    def verify_chat_with_virtual_assistant_image(self, timeout=10, raise_e=True):
        """
        Verifying Chat With Virtual Assistant image on Help Center screen
        """
        return self.driver.wait_for_object("chat_with_virtual_assistant_image", timeout=timeout, raise_e=raise_e)

    def verify_hp_mobile_fax_screen(self):
        """
        Verifying HP Mobile Fax screen after click "Fax" option under the Printer Feature on the list view
        """
        self.driver.wait_for_object("hp_universal_fax_driver_text")

    def verify_accept_cookie_banner(self, timeout=10, raise_e=True):
        """
        Verifying Accept cookie banner on Help Center screen
        """
        return self.driver.wait_for_object("accept_cookies_btn", timeout=timeout, raise_e=raise_e)

    def select_chat_with_assistant_agent(self):
        self.driver.click("chat_with_virtual_assistant_btn")

    def select_contact_hp_btn(self):
        self.driver.click("contact_hp_btn")

    def select_accept_cookies(self):
        self.driver.click("accept_cookies_btn")

    def swipe_item(self, item):
        """
        Swipe to a link
        :param item: use class constants:
                PRINTER_SUPPORT_LINK
                Connecting to Your Printer ITEM 
                PRINT_ANYWHERE_ONLINE_SUPPORT_LINK
                SHORTCUTS_ONLINE_SUPPORT_LINK
                HP_MOBILE_PRINTING_LINK
                FINDING_YOUR_PRINTER_ITEM
                CONNECTING_TO_YOUR_PRINTER_ITEM
        """
        self.driver.swipe(item)

    def click_item(self, item):
        """
        Click on a item on Help & Support screen.
        :param item: use class constants
        """
        self.driver.click(item)

    def swipe_and_click_item(self, item):
        """
        Swipe and then click the item on Help & Support screen.
        :param item: use class constants
        """
        self.swipe_item(item)
        time.sleep(2)
        self.click_item(item)

    def verify_gettting_to_know_hp_smart(self):
        """
        Verifying Getting to Know HP Smart screen after we click on HP Support from any flow
        """
        self.driver.wait_for_object("getting_to_know_hp_smart_item")
        self.driver.wait_for_object("getting_to_know_hp_smart_message")


class IOSHelpSupport(HelpSupport):
    context = "NATIVE_APP"

    def __init__(self, driver, context=None, url=None, window_name="main"):
        super(IOSHelpSupport, self).__init__(driver, context=context, url=url, window_name=window_name)
        ui_map = self.load_ui_map(system="IOS", project="smart", flow_name="shared_obj")
        self.driver.load_ui_map(self.project, self.flow_name, ui_map, append=True)

    def native_verify_help_center_screen(self, timeout=30):
        """
        Verifying Help Center screen via title: "Welcome to HP Smart App Help and Support"
        """
        self.driver.wait_for_object("help_center_title", timeout=timeout)

    def native_select_chat_with_virtual_agent(self):
        self.driver.click("chat_with_virtual_assistant_btn")

    def native_select_accept_cookies(self):
        self.driver.click("accept_cookies_btn")
      
    def verify_virtual_agent(self):
        """
        verifies virtual agent in safari
        """
        self.driver.wait_for_object("virtual_agent", timeout=30)

    def select_navigate_back(self):
        self.driver.click("_shared_back_arrow_btn")
    
    def get_support_link(self,timeout=10):
        self.driver.wait_for_object("hp_support_url",timeout=10)
        return self.driver.get_text("hp_support_url")
    
    def get_hp_subscriptions_url(self):
        return self.driver.get_text("hp_subscriptions_url")


class MacHelpSupport(IOSHelpSupport):
    def select_close_btn(self):
        self.driver.click("close_btn")