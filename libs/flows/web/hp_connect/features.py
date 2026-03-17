from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow

class Features(HPConnectFlow):

    flow_name="features"

    def __init__(self,driver, context=None):
        super(Features, self).__init__(driver, context=context)

    ###############################################################################
    #                             Action flows
    ###############################################################################

    def click_features_btn(self):
        """
        Click on Features button on HP Smart menu screen
        """
        self.driver.click("features_btn")
        
    def click_solutions_btn(self):
        """
        Click on Solutions button on HP Smart menu screen
        """
        self.driver.click("solutions_button_ios")

    def click_print_anywhere_btn(self):
        """
        Click on Print Anywhere button on Features menu screen
        """
        self.driver.click("print_anywhere_btn")

    def click_other_features_btn(self):
        """
        Click on Other Features button on Features menu screen
        """
        self.driver.click("other_features_btn")

    def click_smart_security_btn(self):
        """
        Click on Smart Security button on Features menu screen
        """
        self.driver.click("smart_security_btn")

    def click_hp_smart_advance_btn(self):
        """
        Click on HP Smart Advance button on Features menu screen
        """
        self.driver.click("hp_smart_advance_btn")

    def click_close_btn(self):
        """
        Click on Close button on Features menu screen
        """
        self.driver.click("close_potg_screen")

    ###############################################################################
    #                            Verification flows
    ###############################################################################

    def verify_features_screen(self):
        """
        Verify Features list screen via common:
        - Smart Security
        """
        self.driver.wait_for_object("smart_security_btn")

    def verify_print_anywhere_screen(self):
        """
        Verify Print Anywhere screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("print_anywhere_title")
        self.driver.wait_for_object("print_anywhere_container")

    def verify_other_features_screen(self):
        """
        Verify Other Features screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("other_features_title")
        self.driver.wait_for_object("other_features_container")

    def verify_smart_security_screen(self):
        """
        Verify Smart Security screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("smart_security_title")
        self.driver.wait_for_object("smart_security_container")

    def verify_hp_smart_advance_screen(self):
        """
        Verify HP Smart Advance screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("hp_smart_advance_title")
        self.driver.wait_for_object("hp_smart_advance_container")