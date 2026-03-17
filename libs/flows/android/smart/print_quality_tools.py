from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow

class PrintQualityTools(SmartFlow):

    flow_name = "print_quality_tools"

    def verify_print_quality_tools_title(self, timeout=10, raise_e=True):
        """
        It verifies the print quality tools tile is displayed.
        """
        return self.driver.wait_for_object("print_quality_tools_title", timeout=timeout, raise_e=raise_e)
    
    def click_print_quality_report_printer_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the print quality report printer button.
        """
        self.driver.click("print_quality_report_printer_btn")

    def click_view_all_print_quality_tools_arrow_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the view all print quality tools arrow button.
        """
        self.driver.click("view_all_print_quality_tools_arrow_btn")