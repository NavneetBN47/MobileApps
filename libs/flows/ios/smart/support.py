from datetime import datetime
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
import time


class Support(SmartFlow):
    flow_name = "support"

    def verify_warranty_status(self):
        """
        Verify warranty status on HPX Product Information Card
        :return:
        """
        self.driver.wait_for_object("warranty_status", raise_e=False)

    def verify_end_session_btn(self):
        """
        Verify End Session button btn
        """
        self.driver.wait_for_object("end_session_btn", raise_e=False)

    def verify_hpx_support_card_printers(self):
        """
        Verify HPX Support Card Printers
        :return:
        """
        self.driver.wait_for_object("support_card_printers", raise_e=False)
        self.driver.click("support_card_printers")

    def click_Go_to_support_hp_web(self):
        """
        Click Go to support hp
        :return:
        """
        self.driver.click("go_to_support_hp")

    def click_hpx_contact_support(self):
        """
        Click HPX Contact Support
        :return:
        """
        self.driver.click("hpx_contact_us_arrow")

    def click_hpx_support_change_region(self):
        """
        Click HPX Support Change Region
        :return:
        """
        self.driver.click("hpx_support_change_region")