from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.resources.const.android.const import WEBVIEW_CONTEXT


class UCDEPrivacy(OWSFlow):
    """
    url: https://oss.hpconnectedpie.com/ucde/terms-conditions/
    """
    flow_name = "ucde_privacy"

    @screenshot_compare()
    def verify_ucde_privacy_screen(self, timeout=10, raise_e=False):
        found = self.driver.wait_for_object("privacy_title", timeout=timeout, raise_e=raise_e)
        #End time for the IOS HP Smart Welcome flow create account
        self.driver.performance.stop_timer("hpid_create_account", raise_e=False)
        return found

    def verify_your_privacy_screen(self, timeout=10, raise_e=False):
        self.driver.wait_for_object("your_privacy_title", timeout=timeout, raise_e=raise_e)
        return True

    def skip_ucde_privacy_screen(self, timeout=10, raise_e=False):
        """
        Skip ucde privacy screen if it displays
        :param timeout: depends on scenario where this screen is loaded.
        """
        if self.verify_ucde_privacy_screen(timeout=timeout, raise_e=raise_e) is not False:
            self.driver.click("continue_btn", change_check={"wait_obj": "continue_btn", "invisible": True})

    def select_learn_more_link(self):
        """
        Clck on learn more link on ucde privacy screen
        """
        self.driver.click("learn_more_link")
    
    def select_i_accept_btn(self):
        """
        Clck on I ACCEPT button on Your Privacy screen
        """
        init_ctx = self.driver.context
        self.driver.switch_to_webview(WEBVIEW_CONTEXT.CHROME, timeout=30)
        self.driver.click("accept_btn")
        self.driver.switch_to_webview(init_ctx, timeout=10)

class MobileUCDEPrivacy(UCDEPrivacy):
    context = "NATIVE_APP"

    def select_learn_more_link_native(self):
        '''
            "Learn more" button is not clickable in webview
        '''
        self.driver.click("learn_more_link")
    
    def select_i_accept_btn_native(self):
        """
            Click on I ACCEPT button on Your Privacy screen (Native view) not in webview
        """
        self.driver.click("accept_btn")
    
    def verify_i_accept_btn_native(self, raise_e=True):
        return self.driver.wait_for_object("accept_btn", raise_e=raise_e)
    
    def verify_account_data_usage_title(self):
        self.driver.wait_for_object("hp_print_account_data_usage_notice")

    def verify_do_not_miss_account_title(self):
        self.driver.wait_for_object("do_not_miss_account_title")

    def click_skip_account_btn(self):
        self.driver.click("skip_account_btn")
