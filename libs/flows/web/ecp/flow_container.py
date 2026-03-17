import logging
from MobileApps.libs.flows.web.ecp.customers import Customers
from MobileApps.libs.flows.web.ecp.home import Home
from MobileApps.libs.flows.web.ecp.login import Login
from MobileApps.libs.flows.web.ecp.users import Users
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.ecp.devices import Devices
from MobileApps.libs.flows.web.ecp.account import Account
from MobileApps.libs.flows.web.ecp.reports import Reports
from MobileApps.libs.flows.web.ecp.endpoint_security import EndpointSecurity
from MobileApps.libs.flows.web.ecp.my_organization import MyOrganization
from MobileApps.libs.flows.web.ecp.solutions import Solutions
from MobileApps.libs.flows.web.ecp.proxies import Proxies
from time import sleep

class CannotGoHomeException(Exception):
    pass

class CannotChooseCustomerException(Exception):
    pass

class FlowContainer(object):
    stack_url = {

        "dev": "https://ecp.dev.portalshell.int.hp.com/",
        "pie": "https://ecp.pie.portalshell.int.hp.com/",
        "stage": "https://ecp.stage.portalshell.int.hp.com/",
        "production": "https://hp-commandcenter.com/"
        }

    def __init__(self, driver):
        self.driver = driver
        self.fd = {"login": Login(driver),
                   "hpid": HPID(driver),
                   "home": Home(driver),
                   "users": Users(driver), 
                   "devices": Devices(driver),
                   "account": Account(driver),
                   "reports": Reports(driver),
                   "customers": Customers(driver),
                   "my_organization": MyOrganization(driver),
                   "endpoint_security": EndpointSecurity(driver),
                   "solutions": Solutions(driver),
                   "proxies": Proxies(driver)}
    @property
    def flow(self):
        return self.fd

    def navigate(self, stack):
        return self.driver.navigate(self.stack_url[stack])

    def login(self, email, pwd):
        return self.fd["hpid"].login(email, pwd)

    def go_home(self, stack, email, pwd, retry=3, raise_e=False):
        for _ in range(retry):
            self.navigate(stack)
            self.fd["home"].click_access_denied_login_btn()
            if self.fd["home"].verify_home_menu_btn(timeout=10, raise_e=False) is False:
                try:
                    self.login(email, pwd)
                    self.fd["login"].select_an_organization_to_sign_in()
                except:
                    if raise_e:
                        raise
                    else:
                        logging.info("Login code failed, this is somewhat expected")
            else:
                return True

            if self.fd["home"].verify_home_menu_btn(timeout=30, raise_e=False) is not False:
                return True
        raise CannotGoHomeException("After: " + str(retry) + " tries still cannot go home")

    def select_customer(self,customer_name=None):
        if self.fd["home"].verify_customer_selected(timeout=30) is False:
            self.fd["home"].choose_customer(customer_name)
        else:
            return True
        sleep(5) # Adding wait to load the customer selection

        if self.fd["home"].verify_customer_selected(timeout=30) is not False:
            return True
        else:
            raise CannotChooseCustomerException("Unable to choose any customer")

    def navigate_endpoint_security_tab(self, stack, email, pwd, tab, retry=3):
        self.go_home(stack, email, pwd, retry=retry)
        self.fd["home"].click_solutions_menu_expand_btn()
        self.fd["home"].click_security_sub_menu_btn()  
        exec("self.fd['endpoint_security'].click_" + tab + "_tab()")
        self.fd["endpoint_security"].verify_selected_tab( tab + "_tab")
        return True
