from socket import timeout
from time import sleep
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class SUH(OWSFlow):
    flow_name = "ows_suh_error"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    @screenshot_compare(root_obj="something_unexpected_screen_header")
    def verify_something_unexpected_error_header(self):
        return self.driver.wait_for_object("something_unexpected_screen_header", displayed=False, timeout=33)

    @screenshot_compare(root_obj="something_unexpected_screen_body")
    def verify_something_unexpected_error_body(self):
        return self.driver.wait_for_object("something_unexpected_screen_body", timeout=33)

    @screenshot_compare(root_obj="cannot_resolve_error")
    def verify_unable_to_resolve_error(self):
        return self.driver.wait_for_object("cannot_resolve_error", timeout=60)

    def verify_suh_error_modal(self, recover=True):
        self.verify_something_unexpected_error_header()
        self.verify_something_unexpected_error_body()
        if recover == True:
            self.driver.wait_for_object("_shared_carousel_screen_continue_or_skip_btn")
            sleep(2)
            self.driver.click("_shared_carousel_screen_continue_or_skip_btn")
        else:
            self.driver.click("_shared_carousel_screen_continue_or_skip_btn")
            self.verify_unable_to_resolve_error()
            self.driver.click("_shared_carousel_screen_continue_or_skip_btn")
