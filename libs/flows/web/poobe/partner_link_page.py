from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow

class PartnerLinkPage(OWSFlow):
    """
        Contains all of the elements associated with ECP:
        url: https://onboardingcenter.pie.portalshell.int.hp.com/pn
        Beam, Enterprise, Jupiter
    """
    file_path = __file__
    flow_name = "partner_link_page"


########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################

    def enter_partner_link_id(self, partner_link_id):
        self.driver.send_keys("partner_link_id_input_box", partner_link_id)

    def click_connect_button(self):
        self.driver.click("connect_button")

########################################################################################################################
#                                                                                                                      #
#                                                  Verification Flows                                                  #
#                                                                                                                      #
########################################################################################################################

    def verify_partner_link_page(self, timeout=5, raise_e=True):
        return self.driver.wait_for_object("partner_link_page", timeout=timeout, raise_e=raise_e)
    
    def verify_partner_link_id_input_box(self):
        self.driver.wait_for_object("partner_link_id_label")
        self.driver.wait_for_object("partner_link_id_input_box")