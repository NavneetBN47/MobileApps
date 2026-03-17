from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare


class ConnectedPrintingServices(OWSFlow):
    flow_name = "connected_printing_services"
    flow_url = "hpsmart_printer-data"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)
    
    @screenshot_compare(root_obj="printer_consents_container")
    def verify_connected_printing_services(self, raise_e=True):
        if self.driver.wait_for_object("cloudflare_error_message", raise_e=False):
            self.driver.refresh()
        self.driver.wait_for_object("connected_printing_services_continue_btn", timeout=45, raise_e=raise_e)
        self.driver.wait_for_object("printer_consents_content", timeout=20, raise_e=raise_e)
        return self.driver.wait_for_object("connected_printing_services_title", timeout=15, raise_e=raise_e)

    def click_connected_printing_services(self):
        self.driver.click("connected_printing_services_continue_btn", timeout=10, change_check={"wait_obj":"connected_printing_services_continue_btn","invisible": True})
    
    def click_connected_printing_services_manage_options_btn(self):
        self.driver.click("connected_printing_services_manage_options_btn", timeout=10, change_check={"wait_obj":"manage_options_modal"})
    
    def click_connected_printing_services_learn_more_hyperlink(self):
        self.driver.click("learn_more_hyperlink", timeout=10)

    def click_connected_printing_services_manage_options_back_btn(self):
        self.driver.wait_for_object("manage_options_back_button")
        self.driver.click("manage_options_back_button")