from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare

class DriverDownloadTrafficDirector(OWSFlow):
    """
    Contains all of the elements and flows associated with Set Up Checklist step of Traffic Director Live UI step
    URL: https://onboardingcenter.stage.portalshell.int.hp.com/us/en/driver-download
    """
    flow_name = "driver_download"
    flow_url = "driver-download"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)


    def verify_driver_download_card(self):
        self.driver.wait_for_object("header")
        self.driver.wait_for_object("driver_download_card")
        self.driver.wait_for_object("driver_download_card_body")
        self.driver.wait_for_object("card_image")

    def verify_driver_after_page(self):
        self.driver.wait_for_object("driver_after_page")
    
    def verify_hp_support_link(self):
        self.driver.wait_for_object("hp_support_href")