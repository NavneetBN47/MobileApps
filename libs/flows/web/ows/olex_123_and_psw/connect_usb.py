from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare

class ConnectUSBTrafficDirector(OWSFlow):
    """
    Contains all of the elements and flows associated with Set Up Checklist step of Traffic Director Live UI step
    URL: https://onboardingcenter.stage.portalshell.int.hp.com/us/en/connect-usb
    """
    flow_name = "connect_usb"
    flow_url = "connect-usb"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)


    def verify_connect_usb_page(self):
        self.driver.wait_for_object("connect_printer_with_usb_card")
        self.driver.wait_for_object("connect_printer_with_usb_images")
        self.driver.wait_for_object("card_body")

    def verify_select_usb_connect_later_on_printer(self):
        self.driver.wait_for_object("select_usb_connect_later_on_printer")


class USBPrinterDisplayTrafficDirector(OWSFlow):
    """
    Contains all of the elements and flows associated with /usb-printer-display page of traffic director
    """
    flow_name = "connect_usb"
    flow_url = "usb-printer-display"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def verify_continue_usb_setup_printer_display_modal(self):
        self.driver.wait_for_object("continue_usb_setup_printer_display_modal")
        self.driver.wait_for_object("connect_printer_with_usb_images") # OLEX Request to add unique locators
        self.driver.wait_for_object("card_body") # OLEX Request to add unique locators