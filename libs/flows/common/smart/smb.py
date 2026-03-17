from MobileApps.libs.flows.common.smart.smart_flow import SmartFlow


class Smb(SmartFlow):
    flow_name = "smb"
    folder_name = "smb"

    def __init__(self, driver):
        super(Smb, self).__init__(driver)


    # ***************************SMB Action Methods****************************************************

    def select_my_printers(self, raise_e=True, timeout=15):
        """
        Selects "My Printers" on the "Welcome back!" or the Account navbar popup
        """
        return self.driver.click("my_printers_txt", raise_e=raise_e, timeout=timeout)

    def select_continue(self, raise_e=True):
        """
        Selects the Continue button on the "Welcome back!" popup
        """
        return self.driver.click("continue_btn", raise_e=raise_e)

    def select_business_org_from_welcome(self, org_name):
        """
        Select any business org from Org welcome screen
        """
        self.driver.click("org_item_from_welcome_back", format_specifier=[org_name], timeout=15)

    def select_manage_hp_account(self):
        """
        Click on Manage HP Account button
        """
        self.driver.click("manage_hp_account_btn", timeout=10, change_check={"wait_obj": "manage_hp_account_btn", "invisible": True})

    def select_business_org_from_account(self, org_name, timeout=15):
        """
        Select any business org from Org welcome screen
        """
        self.driver.click("org_item_from_account", timeout=timeout, format_specifier=[org_name])

    def click_sign_out_btn(self):
        """
        Click on Sign Out button on Account menu screen
        """
        self.driver.click("_shared_sign_out", change_check={"wait_obj": "manage_hp_account_btn", "invisible": True})

    def click_cancel_btn(self):
        """
        Click on cancel button on Are you sure popup screen
        """
        self.driver.click("are_you_sure_cancel_btn", change_check={"wait_obj": "are_you_sure_cancel_btn", "invisible": True})

    def click_are_you_sure_sign_out_btn(self):
        """
        Click on Sign Out Are you sure popup screen
        """
        self.driver.click("are_you_sure_sign_out_btn", change_check={"wait_obj": "are_you_sure_sign_out_btn", "invisible": True})

    # ***************************SMB Verification Methods****************************************************

    def verify_welcome_back_screen(self, invisible=False, timeout=10):
        """
        Verify Welcome back screen via:
        - Title
        - Continue button
        """
        self.driver.wait_for_object("welcome_back_title", invisible=invisible, timeout=timeout)
        self.driver.wait_for_object("continue_btn", invisible=invisible)

    def verify_business_org_from_account_option(self, invisible=False):
        """
        Verify if business org displays on Account screen:
        - Title
        """
        self.driver.wait_for_object("org_item_from_account", invisible=invisible)

    def verify_account_menu(self):
        """
        Verify Account screen via:
        - Manage HP Account button
        """
        self.driver.wait_for_object("manage_hp_account_btn")

    def are_you_sure_sign_out_popup(self, displayed=True):
        """
        Verify Are you sure sign out screen via:
        - title
        - body message
        - Cancel button
        - Sign Out button
        """
        self.driver.wait_for_object("are_you_sure_popup_title", displayed=displayed, timeout=15)
        self.driver.wait_for_object("are_you_sure_popup_message", displayed=displayed)
        self.driver.wait_for_object("are_you_sure_cancel_btn")
        self.driver.wait_for_object("are_you_sure_sign_out_btn")

    def verify_no_smb_printer_screen(self, timeout=15):
        """
        Verify currently screen is no smb printer screen
        """
        self.driver.wait_for_object("add_smb_printer_title")
        self.driver.wait_for_object("no_smb_printer_txt", timeout=timeout)

class AndroidSmb(Smb):
    platform = "android"

class IOSSmb(Smb):
    platform = "ios"

    def select_business_org_from_account(self, org_name, timeout=15):
        """
        Select any business org from Org welcome screen
        """
        self.driver.click("org_item_from_account", timeout=timeout, format_specifier=[org_name])