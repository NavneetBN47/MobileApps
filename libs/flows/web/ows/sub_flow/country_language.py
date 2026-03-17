from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow, AndroidOWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.ma_misc import ma_misc

class CountryLanguage(OWSFlow):
    flow_name = "country_language"
    flow_url = "language-country"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)
    
    def validate_country_language_screen(self):
        return self.driver.wait_for_object("l_c_title")
    
    @screenshot_compare(root_obj="l_c_popup")
    def validate_success_popup(self):
        return self.driver.wait_for_object("l_c_successful_popup")
    
    def click_continue(self):
        return self.driver.click("l_c_continue_btn")

    def click_set_this_later_btn(self, timeout=180):
        """
        wait 180s or more untill set this later btn appears and then click
        """
        self.driver.wait_for_object("skip_installing_btn", timeout= timeout)
        return self.driver.click("skip_installing_btn")

class CountryLanguageIOS(CountryLanguage):
    platform = "ios"