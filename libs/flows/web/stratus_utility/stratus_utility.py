
from selenium.webdriver.common.keys import Keys
from time import sleep
from MobileApps.libs.flows.web.web_flow import WebFlow
from selenium.common.exceptions import NoSuchElementException


class StratusUtility(WebFlow):
    project = "stratus_utility"
    flow_name = "stratus_utility"

# ----------------unclaimed printer---------------- # 
    def unclaimed_printer_flow(self, printer_uuid):
        """
        https://stratusqav2.cso-hp.com/qaprinterstatus
        """
        try:
            # Open specified link 
            self.driver.navigate("https://stratusqav2.cso-hp.com/qaprinterstatus")
            # "Your connection is not private" webpage shows 
            if self.driver.click("details_btn", timeout=15, raise_e=False):
                self.driver.click("proceed_link")

            # "Please sign in" webpage shows   
            if self.driver.wait_for_object("username_edit", timeout=10, raise_e=False):
                self.driver.send_keys("username_edit", "sandyl@hp.com")
                self.driver.send_keys("password_edit", "Test.0311")
                self.driver.click("sign_in_btn")
            
            # clear printer UUID and claim info
            self.driver.wait_for_object("printer_uuid_edit_box", timeout=20)
            el = self.driver.wait_for_object("stack_combobox")
            el.send_keys(Keys.ENTER, Keys.DOWN, Keys.ENTER)
            sleep(2)
            self.driver.send_keys("printer_uuid_edit_box", printer_uuid)
            for _ in range(3):
                self.driver.click("search_btn")
                con_1 = self.driver.wait_for_object("unClaim_and_remove_uuid_btn", timeout=30, raise_e=False)
                con_2 = self.driver.wait_for_object("search_btn", timeout=30, raise_e=False)
                if con_1 or not con_2:
                    break
            for _ in range(3):
                if not con_2:
                    break
                if con_1:
                    self.driver.click("unClaim_and_remove_uuid_btn")
                    con_3 = self.driver.wait_for_object("search_btn", timeout=30, raise_e=False)     
                    if not con_3:
                        break  
            else:
                raise NoSuchElementException("Fail to remove printer UUID")
        finally:
            self.clear_chrome_browsing_data()