from time import sleep
import json
from MobileApps.libs.flows.android.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class DataValve(JwebDataCollectionFlow):
    flow_name = "data_valve"

    def select_reset_bindings_button(self):
        """
        Selects the Reset Bindings button from the cached bindings screen
        """
        self.driver.click("reset_bindings")

    def get_v1bindings_text(self, expect_value=True): 
        """
        From the Bindings tab, return the v1/bindings json at the bottom of the page as raw text
        """
        if expect_value:
            for _ in range(5):
                if len(self.driver.get_attribute("v1bindings_json", "text")) == 0:
                    sleep(5)
                else:
                    break
        return self.driver.get_attribute("v1bindings_json", "text")

    def get_bindings_filter(self, expect_value=True):
        """
        From the bindings tab, return the Bindings Filter JSON at the top of the page as JSON
        """
        if expect_value:
            for _ in range(5):
                if len(self.driver.get_attribute("request_json", "text")) == 0:
                    sleep(5)
                else:
                    break
            return json.loads(self.driver.get_attribute("request_json", "text"))
        else:
            return self.driver.get_attribute("request_json", "text")