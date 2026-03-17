from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow

class Account(HPConnectFlow):

    flow_name="account"

    def __init__(self,driver, context=None):
        super(Account, self).__init__(driver, context=context)


    ###############################################################################
    #                             Action flows
    ###############################################################################

    def click_account_btn(self):
        """
        Click on the expand arrow beside Account to expand menu on HP Smart menu screen
        """
        self.driver.click("account_btn")

    def click_account_profile_btn(self, delay=None):
        """
        Click on Account Profile button on Account menu screen
        """
        self.driver.click("account_profile_btn", delay=delay)

    def click_view_notifications_btn(self):
        """
        Click on View Notifications button on Account menu screen
        """
        self.driver.click("view_notifications_btn")

    def click_shipping_billing_btn(self):
        """
        Click on Shipping & Billing button on Account menu screen
        """
        self.driver.click("shipping_billing_btn")

    def click_users_btn(self):
        """
        Click on Users button on Account menu screen
        """
        self.driver.click("users_btn")
    
    def click_sign_in_btn(self):
        """
        Click on Sign in button on Sign in to use Shortcuts screen
        """
        self.driver.click("sign_in_btn")

    def click_create_account_btn(self):
        """
        Click on create_account_button on Sign in to use Shortcuts screen
        """
        self.driver.click("create_account_btn")

    def click_sign_in_to_use_shortcuts_string(self):
        """
        Click on Sign in to use Shortcuts string 
        """
        self.driver.click("sign_in_to_use_shortcuts_string")

    ###############################################################################
    #                            Verification flows
    ###############################################################################

    def verify_account_menu_screen(self):
        """
        Verify Account menu screen via:
        - Account Profile
        - View Notifications
        """
        self.driver.wait_for_object("account_profile_btn")
        self.driver.wait_for_object("view_notifications_btn")

    def verify_view_notifications_screen(self):
        """
        Verify View Notifications screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("view_notifications_title")
        self.driver.wait_for_object("view_notifications_container")

    def verify_notification_settings_screen(self):
        """
        Verify Notification Settings screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("notification_settings_title")
        self.driver.wait_for_object("notification_settings_container")

    def verify_shipping_billing_screen(self, timeout=20):
        """
        Verify Shipping & Billing screen via:
         - title
          - Message
        """
        self.driver.wait_for_object("shipping_billing_title", timeout=timeout)

    def verify_profile_screen(self, timeout=10):
        """
        Verify Profile screen  via:
        - Profile title
        """
        self.driver.wait_for_object("account_profile_title", timeout=timeout)
    
    def verify_tiles_not_signed_in_page(self, timeout=10):
        """
        Verify the tile not signed in via:
        - Sign in
        """
        self.driver.wait_for_object("sign_in_btn", timeout=timeout)
        self.driver.wait_for_object("create_account_btn", timeout=timeout)
        self.driver.wait_for_object("close_btn", timeout=timeout)

    def verify_sign_in_btn(self, timeout=10):
        """
        Verify Sign in button:
        """
        return self.driver.wait_for_object("sign_in_btn", timeout=timeout)

    def verify_create_account_btn(self, timeout=10):
        """
        Verify Create Account button:
        """
        return self.driver.wait_for_object("create_account_btn", timeout=timeout)
