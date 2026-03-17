from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare
from selenium.webdriver.common.keys import Keys


class HpPlusSmartPrinterRequirements(OWSFlow):
    """
        Contains all of the elements and flows associated with Portal OOBE Hp+ Requirments and Benefits Page as of 10/11/2023 only for /onboard flow users is show this offer to accept or decline hp+ offer just before printer activation page
    """
    file_path = __file__
    flow_name = "hp_plus_smart_printer_requirements"

########################################################################################################################
#                                                  Action Flows                                                        #
########################################################################################################################

    def click_confirm_hp_plus_activation_button(self):
        """
        Click Confirm HP+ Activation Button
        End of flow
        """
        self.driver.click("confirm_button_text")

    
########################################################################################################################
#                                            Verification Flows                                                        #
########################################################################################################################

    @screenshot_compare(root_obj="hp_plus_smart_printer_requirements_page")
    def verify_hp_plus_smart_printer_requirements_page(self):
        """
        Verify Hp+ Smart Printer Requirments terms and consitions Page
        """
        self.driver.wait_for_object("hp_plus_smart_printer_requirements_page")