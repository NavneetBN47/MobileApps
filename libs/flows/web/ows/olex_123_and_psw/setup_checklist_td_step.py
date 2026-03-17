from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.ma_misc import ma_misc

class SetupChecklistTrafficDirector(OWSFlow):
    """
    Contains all of the elements and flows associated with Set Up Checklist step of Traffic Director Live UI step
    URL: https://onboardingcenter.stage.portalshell.int.hp.com/us/en/setup-checklist
    """
    flow_name = "setup_checklist"
    flow_url = "setup-checklist"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def click_use_printer_offline_btn(self):
        """
        click Use Printer Offline Button at the end of checklist details for User.
        """
        self.driver.click("use_usb_instead")
    
    def click_wireless_drop_down_option(self):
        """
        By Default Ethernet option is open to see details for wireless click wireless option.
        """
        self.driver.click("wireless_header")

    def click_connect_printer_to_internet_overlay_close_btn(self):
        self.driver.click("connect_printer_to_internet_overlay_close_btn")

    def click_connect_printer_to_internet_continue_with_usb_btn(self):
        self.driver.click("connect_printer_to_internet_continue_with_usb_btn")
    
    def verify_account_type_header(self):
        self.driver.wait_for_object("account_type_header")
    
    def verify_personal_use_checklist_page(self):
        """
        Verify Checklist page for Personal use can be seen after selecting For personal use in previous step.
        """
        self.driver.wait_for_objct("setup_checklist_page")
        self.driver.wait_for_object("personal_use_icon")
        self.driver.verify_object_string("sub_header")

    def verify_ethernet_info_option(self):
        """
        On This page user is show Checklist items like connection check and tips one of the drop-down checklist id ethernet.
        Bt Default when user arrives on this page Ethernet Drop-down is already open.
        """
        self.driver.verify_object_string("ethernet_header")

    def verify_ethernet_tips(self):
        """
        Verification of ethernet connection tips for user. Both Locator and String verification.
        """
        self.driver.verify_object_string("ethernet_content")

    def verify_wireless_info_option(self):
        """
        Verification of Wireless Drop-Down tips title.
        """
        self.driver.verify_object_string("wireless_header")

    def verify_wireless_info_tips_personal(self):
        """
        Verification of Wireless Drop-Down tips details.
        """
        self.driver.verify_object_string("wireless_content_personal")


    def verify_checklist_page(self, personal=False):
        """
        Verify Checklist page for Business use can be seen after selecting For Business use in previous step.
        """
        self.driver.wait_for_object("setup_checklist_page")
        self.driver.wait_for_object("setup_checklist_header")
        if personal:
            self.driver.wait_for_object("personal_use_icon")
        else:
            self.driver.wait_for_object("business_use_icon")
        self.driver.wait_for_object("header")

    def verify_wireless_info_tips_business(self):
        """
        Verification of Wireless Drop-Down tips details.
        """
        self.driver.verify_object_string("wireless_content_business")

    def verify_connect_printer_to_internet_overlay_modal(self):
        self.driver.wait_for_object("connect_printer_to_internet_overlay_modal", displayed=False)
        self.driver.wait_for_object("connect_printer_to_internet_continue_with_usb_btn")
        self.driver.wait_for_object("connect_printer_to_internet_overlay_close_btn")