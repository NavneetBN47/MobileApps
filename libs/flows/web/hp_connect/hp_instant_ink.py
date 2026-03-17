from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow

class HPInstantInk(HPConnectFlow):

    flow_name="hp_instant_ink"

    def __init__(self,driver, context=None):
        super(HPInstantInk, self).__init__(driver, context=context)


    ###############################################################################
    #                             Action flows
    ###############################################################################

    def click_hp_instant_ink_btn(self):
        """
        Click on HP Instant Ink button on HP Smart menu screen
        """
        self.driver.click("hp_instant_ink_btn")

    def click_plan_overview_btn(self):
        """
        Click on Plan Overview button on HP Instant Ink menu screen
        """
        self.driver.click("plan_overview_btn")

    def click_change_plan_btn(self):
        """
        Click on Change Plan button on HP Instant Ink menu screen
        """
        self.driver.click("change_plan_btn")

    def click_print_history_btn(self):
        """
        Click on Print History button on HP Instant Ink menu screen
        """
        self.driver.click("print_history_btn")

    def click_shipping_tracking_btn(self):
        """
        Click on Shipment Tracking button on HP Instant Ink menu screen
        """
        self.driver.click("shipping_tracking_btn")

    def click_plan_activity_btn(self):
        """
        Click on Plan Activity button on HP Instant Ink menu screen
        """
        self.driver.click("plan_activity_btn")

    ###############################################################################
    #                            Verification flows
    ###############################################################################

    def verify_hp_instant_ink_menu_screen(self):
        """
        Verify HP Instant Ink menu screen via:
        - Plan Overview
        - Change Plan
        - Print History
        - Shipment Tracking
        - Plan Activity
        """
        self.driver.wait_for_object("plan_overview_btn")
        self.driver.wait_for_object("change_plan_btn")
        self.driver.wait_for_object("print_history_btn")
        self.driver.wait_for_object("shipping_tracking_btn")

    def verify_plan_overview_screen(self, timeout=30):
        """
        Verify Plan Overview screen via:
        Page container
        """
        self.driver.wait_for_object("overview_page_title", timeout=timeout)

    def verify_change_plan_screen(self, timeout=30):
        """
        Verify Change Plan screen via:
        Page container
        """
        self.driver.wait_for_object("update_plan_page_title", timeout=timeout)

    def verify_print_history_screen(self, timeout=30):
        """
        Verify Print History screen via:
        Page container
        """
        self.driver.wait_for_object("print_history_page_title", timeout=timeout)

    def verify_shipping_tracking_screen(self, timeout=30):
        """
        Verify Shipment Tracking screen via:
        Page container
        """
        self.driver.wait_for_object("shipment_tracking_page_title", timeout=timeout)