from _pytest import logging
from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Dropbox(SmartFlow):
    flow_name = "dropbox"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_file(self, file_name):
        """
        Select a file in a Box documents list using file name
        :param file_name: <path>/ file name or file name only
                        ex: /testdata_cloud/documents/pdf/<file_name>.pdf
        """
        names = file_name.split("/")
        for name in names:
            self.driver.wait_for_object("dropbox_tv")
            self.driver.scroll("dropbox_tv")
            self.driver.click(name)

    def select_open(self):
        """
        selects open on the window popup
        """
        self.driver.click("Open")

    def select_allow_popup(self):
        """
        selects the allow button
        """
        self.driver.wait_for_object("allow_btn")
        self.driver.click("allow_btn")

    def select_allow(self):
        """
        selects the allow button
        """
        self.driver.click("allow_btn")

    def select_back_drop_box(self):
        """
        selects the back arrow button
        """
        self.driver.wait_for_object("back_btn")
        self.driver.click("back_btn")

    def is_dropbox_already_signed_in(self):
        try:
            self.select_allow()
        except TimeoutException:
            self.verify_dropbox_login_screen()
            self.driver.click("sign_in_with_google_btn")
            self.driver.click("sign_in_with_test_account")
            self.select_allow()

    def login_drop_box(self, email, password):
        """
        :param email:
        :param password:
        """
        self.driver.send_keys("email_tf", email)
        self.driver.send_keys("password_tf", password)
        self.driver.click("sign_in_and_link_btn")

########################################################################################################################
#                                                                                                                      #
#                                                  Verification Flows
#                                                                                                                      #
########################################################################################################################

    def verify_dropbox_album(self):
        """
        verifies that the current screen is in the dropbox album
        """
        self.driver.wait_for_object("dropbox_txt")

    def verify_dropbox_files_screen(self):
        """
        verifies that the dropbox screen was loaded in aio
        """
        self.driver.wait_for_object("dropbox_txt")

    def verify_dropbox_login_screen(self):
        """
        verify the dropbox pop from home screen
        """
        self.driver.wait_for_object("dropbox_sign_in_page")

    def verify_back_drop_box(self):
        """
        selects the back arrow button
        """
        self.driver.wait_for_object("back_btn")