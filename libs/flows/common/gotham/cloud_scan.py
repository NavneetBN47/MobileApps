from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow


class CloudScan(GothamFlow):
    flow_name = "cloud_scan"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_back_arrow(self):
        self.driver.click("back_arrow")

    def click_refresh_icon(self):
        self.driver.click("refresh_icon")

    def click_hamburger_icon(self):
        self.driver.click("hamburger_icon")

    def click_x_button(self):
        self.driver.click("close_list_icon")

    def switch_printer_sync_toggle(self, num):
        self.driver.click("sync_toggle", format_specifier=[num])

    def get_sync_toggle_status(self, num, raise_e=False):
        return self.driver.get_attribute("sync_toggle", format_specifier=[num], attribute="Toggle.ToggleState", raise_e=raise_e)

    def get_printer_sync_text(self, index, num):
        """
        For index
        - 0: Sync is turned off
        - 1: Update sync schedule
        """
        btns = ["sync_is_turned_off_text", "update_sync_schedule_text"]
        return self.driver.get_attribute(btns[index], format_specifier=[num], attribute="Name")
            
    def select_sync_schedule(self, schedule):
        """
        - 1: 1 year
        - 2: 1 day
        - 3: custom
        """
        self.driver.click("sync_schedule_option", format_specifier=[schedule])

    def click_save_button(self):
        self.driver.click("sync_dialog_save_btn")

    def click_dialog_close_button(self):
        self.driver.click("sync_dialog_close_btn")
    
    
    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_my_hp_cloud_scans_screen(self, raise_e=True):
        return self.driver.wait_for_object("my_hp_cloud_scans_title", timeout=20, raise_e=raise_e) and\
        self.driver.wait_for_object("back_arrow", timeout=20, raise_e=raise_e) and\
        self.driver.wait_for_object("paper_image", timeout=20, raise_e=raise_e)
    
    def verify_cloud_scan_printers_list(self, raise_e=True):
        return self.driver.wait_for_object("cloud_scan_printers_list", timeout=20, raise_e=raise_e) and\
        self.driver.wait_for_object("close_list_icon", timeout=20, raise_e=raise_e) 

    def verify_set_up_your_sync_schedule_dialog(self):
        self.driver.wait_for_object("sync_schedule_dialog")
        self.driver.wait_for_object("sync_dialog_save_btn")

    def verify_sync_successful_dialog(self):
        self.driver.wait_for_object("sync_schedule_dialog")
        assert self.driver.get_attribute("sync_successfull_text", attribute="Name") == 'Sync successful'

    
    