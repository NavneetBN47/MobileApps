from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.ma_misc import ma_misc


class PrinterConnectionTrafficDirector(OWSFlow):
    """
    Contains all elements and web operations associated with Printer-network step.
    URL: https://onboardingcenter.stage.portalshell.int.hp.com/us/en/printer-network 
    """
    flow_name = "hp_software"
    flow_url = "hp-software"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)
    
    def verify_personal_use_hp_software_page(self, printer_profile):
        self.driver.wait_for_object("hp_software")
        self.driver.wait_for_object("install_hp_smart_btn")
        if "paas" not in printer_profile:                               # Paas Printer SKU "Use USB instead" button on HP software page was removed by design see: https://hp-jira.external.hp.com/browse/OLEX-1061
            self.driver.wait_for_object("use_usb_instead_btn")
        else:
            assert self.driver.wait_for_object("use_usb_instead_btn", raise_e=False) is False, "Use USB instead button should not be present for Paas printers"
        self.driver.wait_for_object("trouble_installing_get_tips_btn")
    
    def verify_printer_network_page(self):
        """
        Verify Its the Printer newwork page in the flow last step.
        """
        self.driver.wait_for_object("printer_network_card")
        self.driver.wait_for_object("printer_network_page_title")

    def verify_hp_software_page(self, timeout=10):
        self.driver.wait_for_object("hp_software", timeout=timeout)

    def verify_install_hp_smart_btn(self):
        """
        Verify Install HP Smart button on Printer network page.
        """
        self.driver.wait_for_object("install_hp_smart_btn")
    
    @screenshot_compare(root_obj="card_image")
    def verify_printer_network_card_image(self):
        """
        Verify Printer network card has assoiciated Image.
        """
        self.driver.wait_for_object("card_image")

    def verify_printer_network_card_instruction(self):
        """
        Verify Printer Network card has instruction.
        """
        self.driver.verify_object_string("card_instruction")

    def verify_already_connected_to_network_btn(self):
        """
        Verify Already connected to network button on Printer network page.
        """
        self.driver.wait_for_object("already_connected_to_the_network_btn")

    def verify_connect_printer_to_internet_modal(self):
        """
        Verify Connect printer to internet modal on Printer network page.
        """
        self.driver.wait_for_object("connect_printer_to_internet_modal")
        self.driver.wait_for_object("connect_printer_to_internet_continue_with_usb_btn")
        self.driver.wait_for_object("connect_printer_to_internet_modal_close_btn")
    
    def click_connect_printer_to_internet_continue_with_usb_btn(self):
        """
        Click on Continue with USB button on Connect printer to internet modal.
        """
        self.driver.click("connect_printer_to_internet_continue_with_usb_btn")
    
    def click_connect_printer_to_internet_modal_close_btn(self):
        """
        Click on Close button on Connect printer to internet modal.
        """
        self.driver.click("connect_printer_to_internet_modal_close_btn")
    
    def click_install_hp_smart_btn(self):
        """
        Click on Install HP Smart button on Printer network page.
        """
        self.driver.click("install_hp_smart_btn")
    
    def click_use_usb_instead_btn(self):
        """
        Click on Use USB instead button on Printer network page.
        """
        self.driver.click("use_usb_instead_btn")

    def click_trouble_installing_get_tips_btn(self):
        """
        Click on Get tips button on Printer network page.
        """
        self.driver.click("trouble_installing_get_tips_btn")

    def click_trobleshooting_modal_close_btn(self):
        """
        Click on Close button on Troubleshooting modal.
        """
        self.driver.click("trouble_installing_get_tips_close_btn")


class FinishSetupBusinessTrafficDirector(OWSFlow):
    """
    Contains all elements and web operations associated with /finish-setup-business page.
    URL: https://onboardingcenter.stage.portalshell.int.hp.com/us/en/finish-setup-business
    """
    flow_name = "hp_software"
    flow_url = "finish-setup-business"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def verify_finish_printer_setup_business(self):
        self.driver.wait_for_object("finish_printer_setup_page")
        self.driver.wait_for_object("page_image")
        self.driver.wait_for_object("card_body")
        self.driver.wait_for_object("business_use_icon")

class UnsupportedOSTrafficDirector(OWSFlow):
    """
    Contains all elements and web operations associated with /unsupported-os page.(Linux Platform)
    URL: https://onboardingcenter.stage.portalshell.int.hp.com/us/en/unsupported-os
    """
    flow_name = "hp_software"
    flow_url = "unsupported-os"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def verify_unsupported_os_page(self):
        self.driver.wait_for_object("unsupported_os_page_content")
        self.driver.wait_for_object("unsupported_os_card_image")
        self.driver.wait_for_object("unsupported_os_qr_code")
        self.driver.wait_for_object("unsupported_os_card_body")
