from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare
import logging


class ResumeSession(OWSFlow):
    """
        Contains all of the elements and flows associated with Resume Session Modal
        /activate, /connect, /onboard
    """
    file_path = __file__
    flow_name = "resume_session_modal"
    
########################################################################################################################
#                                                  Action Flows                                                        #
########################################################################################################################

    def click_resume_btn(self):
        """
        Click on Resume Button
        """
        self.driver.click("resume_btn")

    def click_start_new_session_btn(self):
        """
        Click on Start New Session Button
        """
        self.driver.click("start_new_session_btn")

########################################################################################################################
#                                            Verification Flows                                                        #
########################################################################################################################

    @screenshot_compare(root_obj="resume_session_modal")
    def verify_resume_session_modal(self, raise_e=True):
        """
        Verify Resume Session Modal
        """
        return self.driver.wait_for_object("resume_session_modal",timeout=15, raise_e=raise_e)
    
    def verify_resume_session_modal_elements(self, raise_e=True):
        """
        Verify Resume Session Modal elements
        """
        self.driver.wait_for_object("header", raise_e=raise_e)
        self.driver.wait_for_object("body", raise_e=raise_e)
        self.driver.wait_for_object("resume_btn", raise_e=raise_e)
        return self.driver.wait_for_object("start_new_session_btn", raise_e=raise_e)