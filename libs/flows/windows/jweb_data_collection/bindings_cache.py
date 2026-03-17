from MobileApps.libs.flows.windows.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow
import json

class BindingsCache(JwebDataCollectionFlow):
    flow_name = "bindings_cache"

    def get_metadata_text(self):
        """
        From the Bindings tab, return the Metadata json at the top of the page
        """
        return json.loads(self.driver.wait_for_object("metadata_json").text)

    def verify_metadata_json(self, metadata, filter_trees_options_bindings_cache):
        """
        From the Bindings tab, comparing the metadata json details with the filter tree options from bindings cache
        """
        assert all(option in metadata for option in filter_trees_options_bindings_cache)

    def verify_metadata_text(self):
        """
        From the Bindings tab, return the representing presense of Metadata
        """
        return self.driver.wait_for_object("metadata_json", timeout=3, raise_e=False).text

    def binding_cache_metadata_text(self):
        """
        From the Bindings tab, return the representing presense of Metadata
        """
        return not self.driver.wait_for_object("metadata_json", timeout=3, raise_e=False) is False

    def get_bindings_time_to_expire_text(self):
        """
        From the Bindings tab, Time to expire should display "Expired" after clicked on "Cache Invalidated" button
        """
        return self.driver.wait_for_object("bindings_time_to_expire").text

    def verify_bindings_cache_response_text(self):
        """
        From the Bindings tab, return the response from bindings
        """
        return json.loads(self.driver.wait_for_object("bindings_cache_response").text)

    def verify_bindings_cache_response_displays(self):
        """
        From the Bindings tab, verify the response from bindings present or not
        """
        return not self.driver.wait_for_object("bindings_cache_response", timeout=3, raise_e=False) is False

    def select_bindings_invalidate_cache_btn(self):
        """
        From the Bindings tab, click on "Cache Invalidated" button
        """
        self.driver.click("bindings_invalidate_cache_btn")