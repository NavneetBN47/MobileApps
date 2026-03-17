from MobileApps.libs.flows.windows.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow
import json
from time import sleep

class VerboseLogs(JwebDataCollectionFlow):
    flow_name = "verbose_logs"

    def get_verbose_logs_response_error(self, get_json=True):
        """
        Navigate to verbose logs tab, verify the response error
        """
        for _ in range(2):
            if '' in self.driver.get_attribute("verbose_logs_response_error", "Name", displayed=False):
                sleep(5)
        
        if get_json:
            return json.loads(self.driver.get_attribute("verbose_logs_response_error", "Name", displayed=False))
        else:
            return self.driver.get_attribute("verbose_logs_response_error", "Name", displayed=False)