import logging
from MobileApps.libs.flows.web.wex.login import Login
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.wex.home import Home
from MobileApps.libs.flows.web.wex.fleet_management_devices import Devices
from MobileApps.libs.flows.web.wex.fleet_management_printproxies import PrintProxies
from MobileApps.libs.flows.web.wex.fleet_management_policies import Policies
from MobileApps.libs.flows.web.wex.fleet_management_dashboard import Dashboard 
from MobileApps.libs.flows.web.wex.devices_pendingprinters import PendingPrinters
from MobileApps.libs.flows.web.wex.pcs_groups import Groups
from MobileApps.libs.flows.web.wex.remediations_policies_pcs import PolciesPCS
from MobileApps.libs.flows.web.wex.remediations_secrets import RemediationsSecrets
from MobileApps.libs.flows.web.wex.remediations_activity import RemediationsActivity
from MobileApps.libs.flows.web.wex.help_and_support import HelpAndSupport
from MobileApps.libs.flows.web.wex.user_profile import UserProfile
from MobileApps.libs.flows.web.wex.workforce_settings import WorkforceSettings
from MobileApps.libs.flows.web.wex.accounts_overview import AccountsOverview
from MobileApps.libs.flows.web.wex.employee_pulses import EmployeePulses
from MobileApps.libs.flows.web.wex.upgrades_integrations import UpgradesIntegrations
from MobileApps.libs.flows.web.wex.upgrades_alerts import UpgradesAlerts
from MobileApps.libs.flows.web.wex.upgrades_scripts import UpgradesScripts
from MobileApps.libs.flows.web.wex.upgrades_labs import UpgradesLabs
from MobileApps.libs.flows.web.wex.printers_groups import PrinterGroups
from MobileApps.resources.const.web.const import WEX_URLS

class CannotGoHomeException(Exception):
    pass

class CannotChooseCustomerException(Exception):
    pass

class FlowContainer(object):
    stack_url = {
        "pie": WEX_URLS.PIE,
        "stage": WEX_URLS.STAGE,
        "production": WEX_URLS.PRODUCTION,
        "test": WEX_URLS.TEST
    }

    def __init__(self, driver):
        self.driver = driver
        self.fd = {"login": Login(driver),
                   "hpid": HPID(driver),
                   "home": Home(driver),
                   "fleet_management_devices": Devices(driver),
                   "fleet_management_printproxies": PrintProxies(driver),
                   "fleet_management_policies": Policies(driver),
                   "fleet_management_dashboard": Dashboard(driver),
                   "devices_pendingprinters": PendingPrinters(driver),
                    "pcs_groups": Groups(driver),
                    "remediations_policies_pcs": PolciesPCS(driver),
                    "remediations_secrets": RemediationsSecrets(driver),
                    "remediations_activity": RemediationsActivity(driver),
                    "help_and_support": HelpAndSupport(driver),
                    "user_profile": UserProfile(driver),
                    "workforce_settings": WorkforceSettings(driver),
                    "accounts_overview": AccountsOverview(driver),
                    "employee_pulses": EmployeePulses(driver),
                    "upgrades_integrations": UpgradesIntegrations(driver),
                    "upgrades_alerts": UpgradesAlerts(driver),
                    "upgrades_scripts": UpgradesScripts(driver),
                    "upgrades_labs": UpgradesLabs(driver),
                    "printers_groups": PrinterGroups(driver)
                   }
    @property
    def flow(self):
        return self.fd

    def navigate(self, stack):
        return self.driver.navigate(self.stack_url[stack])

    def login(self, email, pwd):
        self.fd["hpid"].handle_privacy_popup()
        return self.fd["login"].login_wex(email, pwd)

    def go_home(self, stack, email, pwd, retry=3, raise_e=False):
            for _ in range(retry):
                self.navigate(stack)
                if self.fd["home"].verify_home_page_title(timeout=10, raise_e=False) is False:
                    try:
                        self.login(email, pwd)
                        self.fd["hpid"].handle_privacy_popup()
                    except:
                        if raise_e:
                            raise
                        else:
                            logging.info("Login code failed, this is somewhat expected")
                else:
                    return True

                if self.fd["home"].verify_home_page_title(timeout=30, raise_e=False) is not False:
                    return True
            raise CannotGoHomeException("After: " + str(retry) + " tries still cannot go home")  