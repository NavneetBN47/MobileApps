from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow
from time import sleep

class DevicesDetailsPrinterMFE(SmartFlow):
    flow_name = "devices_details_printer_mfe"


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_product_information_mfe(self):
        return self.driver.wait_for_object("product_information_section")

    def verify_copy_product_number_btn(self, timeout=3):
        return self.driver.wait_for_object("copy_product_number_btn", timeout=timeout)
    
    def verify_copy_serial_number_btn(self):
        return self.driver.wait_for_object("copy_serial_number_btn")
    
    def verify_get_info_btn(self):
        return self.driver.wait_for_object("get_info_btn") 

    def verify_printer_scan_tile(self):
        sleep(2)
        self.driver.swipe(distance=6)
        return self.driver.wait_for_object("printer_scan_tile")
    
    def verify_print_documents_tile(self):
        return self.driver.wait_for_object("print_documents_tile")
    
    def verify_print_photo_btn(self):
        return self.driver.wait_for_object("print_photos_tile")
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_top_back_btn(self):
        self.driver.swipe(direction="up", distance=6)
        return self.driver.click("top_back_btn")
    
    def click_scan_tile(self):
        sleep(2)
        if self.driver.driver_type.lower() == "windows":
            self.driver.swipe(distance=6)
        return self.driver.click("printer_scan_tile")
    
    def click_camera_scan_tile(self, timeout=10,raise_e=True):
        """
        It Swipes to find the camera scan tile and clicks on it.
        """
        while True:
            if self.driver.wait_for_object("camera_scan_tile", timeout=timeout, raise_e=raise_e):
                self.driver.click("camera_scan_tile")
                break
            self.driver.swipe()

    def click_feature_unavailable_popup_if_exist(self,raise_e=False,timeout=20):
        if self.driver.wait_for_object("feature_unavailable_popup", timeout=timeout, raise_e=raise_e):
            self.driver.click("feature_unavailable_popup")
            return True
    
    def click_copy_product_number_btn(self):
        return self.driver.click("copy_product_number_btn")
    
    def click_copy_serial_number_btn(self):
        return self.driver.click("copy_serial_number_btn")
    
    def click_get_info_btn(self):
        return self.driver.click("get_info_btn")