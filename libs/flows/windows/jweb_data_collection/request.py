from MobileApps.libs.flows.windows.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class Request(JwebDataCollectionFlow):
    flow_name = "request"

    def get_request_log_url(self, index=0):
        """
        From the Request Logs page, return the url found in the Data Valve request given the :index:
        XPath indexing begins at 1, returns the first url if no index is given
        """
        return self.driver.get_attribute("data_valve_request_url", format_specifier=[index+1], attribute="text", raise_e=False)

    def verify_data_valve_request_url(self, data_valve_request_url, filter_trees_options_request_url):
        """
        From the Request tab, comparing the data valve bindings details with the filter tree options from request url
        """
        for option in filter_trees_options_request_url:
            assert option in data_valve_request_url, "{} not found within Data Valve Request URL: {}".format(option, filter_trees_options_request_url)

    def verify_reqeust_log_url(self):
        """
        From the Request Logs page, return the representing presence of request url
        """
        return self.driver.wait_for_object("data_valve_request_url", format_specifier=[1], timeout=3, raise_e=False)

    def get_second_attempt_data_valve_controller_status_code(self):
        """
        From the Request Logs page, return the second attempt url found in the Data Valve request
        """
        return self.driver.get_attribute("data_valve_controller_second_attempt_status_code", "text")

    def get_first_attempt_data_valve_controller_status_code(self):
        """
        From the Request Logs page, return the first attempt url found in the Data Valve request
        """
        return self.driver.get_attribute("data_valve_controller_first_attempt_status_code", "text")

    def get_request_url_status_code(self, index=0):
        """
        From the Request Logs page, return the representing presence of request url status code
        """
        return self.driver.get_attribute("request_url_code", format_specifier=[index+1], attribute="text", raise_e=False)
        
    def verify_request_url_table(self):
        """
        From the Request Logs page, verify the request url table
        """
        request_url = self.get_request_log_url(index=0)
        if 'clientdatavalvecontroller' not in request_url:
            request_status_code = self.get_request_url_status_code(index=0)
            assert request_status_code in ['200', '400'], f"Unexpected status code: {request_status_code}"
        request_url = self.get_request_log_url(index=1)
        if 'clientdatavalvecontroller' not in request_url:
            request_status_code = self.get_request_url_status_code(index=1)
            assert request_status_code in ['200', '400'], f"Unexpected status code: {request_status_code}"
        request_url = self.get_request_log_url(index=2)
        if 'clienttelemetry' not in request_url:
            request_status_code = self.get_request_url_status_code(index=2)
            assert request_status_code in '200', f"Unexpected status code: {request_status_code}"