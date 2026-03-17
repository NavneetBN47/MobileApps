from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

class SecurityGateway(JwebFlow):
    flow_name = "security_gateway"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_redirect_me(self):
        """
        clicks the redirect me to app link
        :return:
        """
        self.driver.click("redirect_me_link",timeout=20)