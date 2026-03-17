from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare


class AccountTypePage(OWSFlow):
    """
        Contains all of the elements and flows associated with Portal OOBE Account Type Page giving user option to select how to setup the printer 
        Business or Personal
    """
    file_path = __file__
    flow_name = "account_type_page"

########################################################################################################################
#                                                  Action Flows                                                        #
########################################################################################################################

    def click_personal_or_business_printer(self, p_type):
        """
        verify and click on personal printer radio btn
        """
        if p_type == "personal":
            self.driver.click("cards[1]_select_button")
        elif p_type == "company":
            self.driver.click("cards[0]_select_button")
        else:
            raise KeyError("Only takes value 'personal' or 'company' for printer type")

########################################################################################################################
#                                            Verification Flows                                                        #
########################################################################################################################

    @screenshot_compare(root_obj="select_account_type_page")
    def verify_select_account_type_page(self):
        """
        Verify How do you want to setup ypur printer page
        """
        self.driver.wait_for_object("select_account_type_page", timeout=30)