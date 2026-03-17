from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

class BrowserPlugin(JwebFlow):
    flow_name = "browser_plugin"

    SIGN_IN_RESULTS = {'token':'jwebsample://auth-browser?token=abc123dorayme'}

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_browser_open(self):
        """
        clicks the browser open item
        :return:
        """
        self.driver.click("browser_open_item")

    def enter_browser_url(self,option):
        """
        sends the browser_url to open
        :param option:
        :return:
        """
        self.driver.send_keys("browser_url_field_txt_box", option)

    def enter_web_scheme(self,option):
        """
        sends the web scheme
        :param option:
        :return:
        """
        self.driver.send_keys("browser_scheme_field_txt_box", option)

    def select_browser_test(self):
        """
        selects the test button
        :return:
        """
        self.driver.click("browser_test_btn")

    def select_browser_close(self):
        """
        selects the browser close button
        :return:
        """
        self.driver.click("browser_close_btn")

    def browser_sign_in_result(self):
        """
        :return: the browser sign in result
        """
        return self.driver.wait_for_object("browser_sign_in_result_txt").text

    def select_continue_on_data_sharing_pop_up(self):
        """
        Click continue on pop up after selecting select_browser_open
        """
        self.driver.wdvr.switch_to_window('NATIVE_APP')
        self.driver.click("pop_up_continue_btn")