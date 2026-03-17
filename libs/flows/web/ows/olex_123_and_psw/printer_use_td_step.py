from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.ma_misc import ma_misc

class PrinterUseTrafficDirector(OWSFlow):
    """Contains all of the elements and flows associated with Printer Use step of Traffic Director Live UI step
    URL: https://onboardingcenter.stage.portalshell.int.hp.com/us/en/printer-use
    """
    flow_name = "printer_use"
    flow_url = "printer-use"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)
        
    def select_business_use_option(self):
        """
        This step will ask user to select if the Printer is to be used fr personal or business purposes 
        based on the selection flow changes.
        """
        self.driver.click("Select_business_use_btn")

    def select_personal_use_option(self):
        """
        Select For Personal Use option when user is asked to select either this printer is going to be used for 
        personal or business purposes.
        """
        self.driver.click("Select_personal_use_btn")
    
    def verify_printer_use_step(self):
        """
        Verify Printer Use step.
        """
        self.driver.wait_for_object("header")
        self.driver.wait_for_object("subheader")

    def verify_personal_card_option(self):
        """
        Verify screen shows For personal use Card title, Body and select button.
        """
        self.driver.wait_for_object("card_header_personal")
        self.driver.wait_for_object("card_body_personal")
        self.driver.wait_for_object("Select_personal_use_btn")

    def verify_business_card_option(self):
        """
        Verify screen shows For Business use Card title, Body and select button.
        """
        self.driver.wait_for_object("card_header_business")
        self.driver.wait_for_object("card_body_business")
        self.driver.wait_for_object("Select_business_use_btn")

    def verify_personal_use_more_info(self):
        """
        verify Personal use more infomation by clicking 'i' icon on top right corner of card.
        """
        self.driver.click("personal_use_more_info_btn")
        self.driver.wait_for_object("personal_info_modal_header")
        self.driver.wait_for_object("personal_info_modal_body")
        self.driver.click("info_overlay_close_btn")

    def verify_business_use_more_info(self):
        """
        Verify Business Use more Information by clicking 'i' icon on top right corner of card.
        """
        self.driver.click("business_use_more_info_btn")
        self.driver.wait_for_object("business_info_modal_header")
        self.driver.wait_for_object("business_info_modal_body")
        self.driver.click("info_overlay_close_btn")