from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow

class PrintersUsers(HPConnectFlow):

    flow_name="printers_users"

    def __init__(self,driver, context=None):
        super(PrintersUsers, self).__init__(driver, context=context)

    ###############################################################################
    #                             Action flows
    ###############################################################################

    def click_users_btn(self):
        """
        Click on Users button on HP Smart menu screen
        """
        self.driver.click("users_btn")

    def click_printers_btn(self):
        """
        Click on Printers button on HP Smart menu screen
        """
        self.driver.click("printers_btn")

    ###############################################################################
    #                            Verification flows
    ###############################################################################

    def verify_users_screen(self):
        """
        Verify Users screen via:
        - Users title
        """
        self.driver.wait_for_object("users_title")

    def verify_printers_screen(self, timeout=10):
        """
        Verify Printers screen via:
        - printers title
        """
        self.driver.wait_for_object("printers_title", timeout=timeout)

    def verify_printer_connection_status(self, timeout=10):
        """
        Verify Printer connection status
        """
        self.driver.wait_for_object("printer_connection_status", timeout=timeout)

    def verify_printer_status(self, timeout=10):
        """
        Verify Printer status
        """
        self.driver.wait_for_object("printer_status", timeout=timeout)