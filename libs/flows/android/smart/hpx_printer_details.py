from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow

class HPXPrinterDetails(SmartFlow):
    flow_name = "hpx_printer_details"

    def click_camera_scan_tile(self, timeout=10,raise_e=True, max_swipes=5):
        """
        It Swipes to find the camera scan tile and clicks on it.
        """
        for _ in range(max_swipes):
            if self.driver.wait_for_object("camera_scan_tile", raise_e=raise_e):
                self.driver.click("camera_scan_tile")
                return True
            self.driver.swipe()
        raise Exception("Unable to find and click on 'camera_scan_tile' after swiping.")

    def click_feature_unavailable_popup_if_exist(self,raise_e=False,timeout=20):
        if self.driver.wait_for_object("feature_unavailable_popup", timeout=timeout, raise_e=raise_e):
            self.driver.click("feature_unavailable_popup")
            return True

    def verify_camera_scan_tile(self, timeout=10, raise_e=True):
        """
        It verifies the camera scan tile is displayed.
        """
        return self.driver.wait_for_object("camera_scan_tile", timeout=timeout, raise_e=raise_e)
    
    def verify_print_photos_tile(self, timeout=10, raise_e=True):
        """
        It verifies the print photos tile is displayed.
        """
        return self.driver.wait_for_object("print_photos_tile", timeout=timeout, raise_e=raise_e)
    
    def verify_shortcuts_tile(self, timeout=10, raise_e=True):
            """
            It verifies the camera scan tile is displayed.
            """
            return self.driver.wait_for_object("shortcuts_tile", timeout=timeout, raise_e=raise_e)

    def click_scan_tile(self, timeout=10, raise_e=True, max_swipes=3):
        """
        It Swipes to find the scan tile and clicks on it.
        """
        for _ in range(max_swipes):
            if self.driver.wait_for_object("scan_tile", timeout=timeout, raise_e=raise_e):
                self.driver.click("scan_tile")
                return True 
            self.driver.swipe()
        raise Exception("Unable to find and click on 'scan_tile' after swiping.")

    def click_print_documents_tile(self, timeout=10,raise_e=True , max_swipes=3):
        """
        It Swipes to find the print documents tile and clicks on it.
        """
        for _ in range(max_swipes):
            if self.driver.wait_for_object("print_documents_tile", timeout=timeout, raise_e=raise_e):
                self.driver.click("print_documents_tile")
                return True 
            self.driver.swipe()
        raise Exception("Unable to find and click on 'print_documents_tile' after swiping.")

    def click_print_photos_tile(self, timeout=10,raise_e=True, max_swipes=3):
        """
        It Swipes to find the print photos tile and clicks on it.
        """
        for _ in range(max_swipes):
            if self.driver.wait_for_object("print_photos_tile", timeout=timeout, raise_e=raise_e):
                self.driver.click("print_photos_tile")
                return True 
            self.driver.swipe()
        raise Exception("Unable to find and click on 'print_photos_tile' after swiping.")

    def click_copy_tile(self, timeout=10,raise_e=True , max_swipes=3):
        """
        It Swipes to find the copy tile and clicks on it.
        """
        for _ in range(max_swipes):
            if self.driver.wait_for_object("copy_tile", timeout=timeout, raise_e=raise_e):
                self.driver.click("copy_tile")
                return True 
            self.driver.swipe()
        raise Exception("Unable to find and click on 'copy_tile' after swiping.")

    def click_mobilefax_tile(self, timeout=10,raise_e=True , max_swipes=3):
        """
        It Swipes to find the mobile fax tile and clicks on it.
        """
        for _ in range(max_swipes):
            if self.driver.wait_for_object("mobile_fax_tile", timeout=timeout, raise_e=raise_e):
                self.driver.click("mobile_fax_tile")
                return True 
            self.driver.swipe()
        raise Exception("Unable to find and click on 'mobile_fax_tile' after swiping.")

    def click_shortcuts_tile(self, timeout=10,raise_e=True, max_swipes=3):
        """
        It Swipes to find the shortcuts tile and clicks on it.
        """
        for _ in range(max_swipes):
            if self.driver.wait_for_object("shortcuts_tile", timeout=timeout, raise_e=raise_e):
                self.driver.click("shortcuts_tile")
                return True 
            self.driver.swipe()
        raise Exception("Unable to find and click on 'shortcuts_tile' after swiping.")

    def click_printable_apps_tile(self, timeout=10,raise_e=True, max_swipes=3):
        """
        It Swipes to find the printables tile and clicks on it.
        """
        for _ in range(max_swipes):
            if self.driver.wait_for_object("printables_tile", timeout=timeout, raise_e=raise_e):
                self.driver.click("printables_tile")
                return True 
            self.driver.swipe()
        raise Exception("Unable to find and click on 'printables_tile' after swiping.")
    
    def click_print_quality_tools_tile(self, timeout=10, raise_e=True, max_swipes=3):
        """
        It Swipes to find the print quality tools tile and clicks on it.
        """
        for _ in range(max_swipes):
            if self.driver.wait_for_object("print_quality_tools_tile", timeout=timeout, raise_e=raise_e):
                self.driver.click("print_quality_tools_tile")
                return True 
            self.driver.swipe()
        raise Exception("Unable to find and click on 'print_quality_tools_tile' after swiping.")
    
    def navigate_to_product_information_details(self, timeout=10, raise_e=True, max_swipes=5):
        """
        It navigates to the product information details screen.
        """
        for _ in range(max_swipes):
            if self.driver.wait_for_object("product_information_title", timeout=timeout, raise_e=raise_e):
                self.driver.click("product_information_title")
                return True 
            self.driver.swipe()
        raise Exception("Unable to find and click on 'product_information_title' after swiping.")
    
    def verify_product_number_title(self, timeout=10, raise_e=True):
        """
        It verifies the product number title is displayed.
        """
        return self.driver.wait_for_object("product_number_title", timeout=timeout, raise_e=raise_e)
    
    def verify_product_serial_number_title(self, timeout=10, raise_e=True):
        """
        It verifies the product serial number title is displayed.
        """
        return self.driver.wait_for_object("product_serial_number_title", timeout=timeout, raise_e=raise_e)
    
    def get_product_number_value(self, timeout=10, raise_e=True):
        """
        It gets the product number value.
        """
        if self.driver.wait_for_object("product_number_value", timeout=timeout, raise_e=raise_e):
            return self.driver.get_text("product_number_value", timeout=timeout, raise_e=raise_e)
    
    def get_product_serial_number_value(self, timeout=10, raise_e=True):
        """
        It gets the product serial number value.
        """
        if self.driver.wait_for_object("product_serial_number_value", timeout=timeout, raise_e=raise_e):
            return self.driver.get_text("product_serial_number_value", timeout=timeout, raise_e=raise_e)
    
    def click_more_information_and_reports_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the more information and reports button.
        """
        self.driver.click("more_information_and_reports_btn", timeout=timeout, raise_e=raise_e)
    
    def verify_printer_information_title(self, timeout=10, raise_e=True):
        """
        It verifies the printer information title is displayed.
        """
        return self.driver.wait_for_object("printer_information_title", timeout=timeout, raise_e=raise_e)
    
    def click_printer_information_general_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the printer information general button.
        """
        self.driver.click("printer_information_general_btn", timeout=timeout, raise_e=raise_e)
    
    def click_printer_information_network_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the printer information network button.
        """
        self.driver.click("printer_information_network_btn", timeout=timeout, raise_e=raise_e)
    
    def click_printer_information_reports_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the printer information reports button.
        """
        self.driver.click("printer_information_reports_btn", timeout=timeout, raise_e=raise_e)
    
    def click_reports_demo_page_print_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the reports demo page print button.
        """
        self.driver.click("reports_demo_page_print_btn", timeout=timeout, raise_e=raise_e)
    
    def verify_reports_print_progress_status(self, timeout=10, raise_e=True):
        """
        It verifies the reports print progress status.
        """
        return self.driver.wait_for_object("reports_print_progress_status", timeout=timeout, raise_e=raise_e)
    
    def verify_reports_print_success_status(self, timeout=10, raise_e=True):
        """
        It verifies the reports print success status.
        """
        return self.driver.wait_for_object("reports_print_success_status", timeout=timeout, raise_e=raise_e)
    
    def click_add_device_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the add device button.
        """
        if self.driver.wait_for_object("add_device_btn", timeout=timeout, raise_e=raise_e):
            self.driver.click("add_device_btn", timeout=timeout, raise_e=raise_e)
        else:
            self.driver.wdvr.execute_script("mobile: clickGesture", {"x": 341, "y": 957})

    def click_choose_an_available_printer_btn(self, timeout=20, raise_e=True):
        """
        It clicks on the choose an available printer button.
        """
        self.driver.wait_for_object("choose_an_available_printer_btn", timeout=timeout, raise_e=raise_e)
        self.driver.click("choose_an_available_printer_btn")

    def click_printer_device_card(self, timeout=10, raise_e=True):
        """
        It clicks on the printer device card.
        """
        self.driver.click("printer_device_card", timeout=timeout, raise_e=raise_e)

    def click_default_shortcuts(self, timeout=10, raise_e=True):
        """
        It clicks on the default shortcuts.
        """
        self.driver.click("default_shortcuts", timeout=timeout, raise_e=raise_e)

    def click_select_source_as_camera_scan_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the camera scan button.
        """
        self.driver.click("camera_scan_btn", timeout=timeout, raise_e=raise_e)

    def click_start_new_scan_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the start new scan button.
        """
        self.driver.click("start_new_scan_btn", timeout=timeout, raise_e=raise_e)

    def click_exit_scan_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the exit scan button.
        """
        self.driver.click("exit_scan_btn", timeout=timeout, raise_e=raise_e)

    def click_start_email_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the start email button.
        """
        self.driver.click("start_email_btn", timeout=timeout, raise_e=raise_e)

    def click_add_image_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the add image button.
        """
        self.driver.click("add_image_btn", timeout=timeout, raise_e=raise_e)

    def click_cancel_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the cancel button.
        """
        self.driver.click("cancel_btn", timeout=timeout, raise_e=raise_e)

    def click_add_device_btn_if_exist(self, raise_e=False, timeout=10):
        """
        It clicks on the add device button if it exists.
        """
        if self.driver.wait_for_object("add_run_shortcut_btn", timeout=timeout, raise_e=raise_e):
            self.driver.click("add_run_shortcut_btn")
            return True

    def click_rotate_btn(self, timeout=10, raise_e=True):
        """
        It clicks on the rotate button.
        """
        self.driver.click("rotate_btn", timeout=timeout, raise_e=raise_e)