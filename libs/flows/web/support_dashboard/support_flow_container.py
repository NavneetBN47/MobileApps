import logging
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.support_dashboard.home import Home
from MobileApps.libs.flows.web.support_dashboard.dashboard import Dashboard

class SupportFlowContainer(object):
    root_url = {
            "pie": "https://uat.support.hp.com/us-en/dashboard",
            "stage": "https://support.hp.com/us-en/dashboard",
            "production": "https://support.hp.com/us-en/dashboard"}
            
    def __init__(self, driver,  window_name="main"):
        self.driver = driver
        self.fd = {"hpid" : HPID(driver, window_name=window_name), 
                    "home": Home(driver, window_name=window_name), 
                    "dashboard": Dashboard(driver, window_name=window_name)}

    @property
    def flow(self):
        return self.fd

    def navigate(self, stack):
        self.driver.navigate(self.root_url[stack])

    def click_sign_in_btn(self):
        self.fd["home"].click_sign_in_btn()

    def login(self, username, password):
        self.fd['hpid'].login(username, password)    

    def add_device(self, sn):
        self.fd["dashboard"].click_add_device_btn()
        self.fd["dashboard"].input_device(sn)
        self.fd["dashboard"].click_submit_btn()  

    def sign_out(self):
        self.fd["dashboard"].click_sign_in_icon()
        self.fd["dashboard"].click_sign_out_btn()  
        self.fd["home"].verify_sign_in_btn()

    def clear_chrome_browsing_data(self):
        self.fd["home"].clear_chrome_browsing_data()