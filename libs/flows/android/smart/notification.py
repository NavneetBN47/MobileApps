from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow

class Notification(SmartFlow):
    flow_name="notification"
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_mobile_fax(self):
        """
        Click on Mobile Fax button on Notifications screen
        """
        self.driver.click("mobile_fax_btn")

    def select_shortcuts(self):
        """
        Click on Shortcuts option on Notification screen
        """
        self.driver.click("shortcuts_btn")

    def select_supplies(self):
        """
        Click on Supplies option on Notification screen
        """
        self.driver.click("supplies_btn")

    def select_account(self):
        """
        click on Account option on Notification screen
        """
        self.driver.click("account_btn")

    def select_text_files(self):
        """
        Click on the Text Files button on the notification screen
        """
        self.driver.click("text_files_btn", change_check={"wait_obj": "text_files_title_txt", "invisible": False, "timeout": 10})

    # *********************************************************************************
    #                                Verification FLOWS                               *
    # *********************************************************************************
    def verify_mobile_fax_option(self):
        """
        Verify Mobile Fax option can be seen Under Activity(Default) tab in Notification Page
        """
        self.driver.wait_for_object("mobile_fax_btn")

    def verify_shortcuts_option(self):
        """
        Verify Smart Task option can be seen under Activity(Default) tab in Notification Page
        """
        self.driver.wait_for_object("shortcuts_btn")

    def verify_supplies_option(self):
        """
        Verify Supplies option can be seen under Activity(Default) tab in Notification Page
        """
        self.driver.wait_for_object("supplies_btn")

    def verify_account_option(self):
        """
        Verify account option can be seen under Activity(Default) tab in Notification Page
        """
        self.driver.wait_for_object("account_btn")

    def verify_notification_screen(self):
        """
        Verify Current screen is Notification screen
        """
        self.driver.wait_for_object("notification_title")