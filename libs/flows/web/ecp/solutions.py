import logging

from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class Solutions(ECPFlow):
    flow_name = "solutions"

    def verify_solutions_mfe(self):
        return self.driver.wait_for_object("solutions_mfe", timeout=10)
