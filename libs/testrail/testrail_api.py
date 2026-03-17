"""TestRail API binding for Python 3.x.

(API v2, available since TestRail 3.0)

Compatible with TestRail 3.0 and later.

Learn more:

http://docs.gurock.com/testrail-api2/start
http://docs.gurock.com/testrail-api2/accessing

Copyright Gurock Software GmbH. See license.md for details.
"""
import json

import requests
from requests.auth import HTTPBasicAuth



class TestStatus:
    """status_id values for TestRail test results"""
    PASSED = 1
    BLOCKED = 2
    UNTESTED = 3
    RETEST = 4
    FAILED = 5

class APIError(Exception):
    pass

class TestRailAPI:
    def __init__(self, username, api_key, base_url):
        if not base_url.endswith('/'):
            base_url += '/'
        self.__url = base_url + 'index.php?/api/v2/'

        self.__s = requests.Session()
        self.__s.headers.update({"Content-Type": "application/json"})
        self.__s.auth = HTTPBasicAuth(username, api_key)

    # ------------------------------------------ RUNS ------------------------------------------
    def add_run(self, name, project_id, suite_id, milestone_id=None, description=None, case_ids=[]):
        """Creates a new test run
        
        Args:
            name: The name to give the run.
            project_id: The project id of the run.
            suite_id: The suite id of the run.
            description: The description for the run.
            cases: The ids of the test cases that are being tested.
        
        Returns:
            The response content of the request
        """
        body = {"name": name, "suite_id": suite_id}
        if milestone_id:
            body["milestone_id"] = milestone_id
        if description:
            body["description"] = description
        if len(case_ids) > 0:
            body["case_ids"] = case_ids
            body["include_all"] = False

        return self.send_post("add_run/{}".format(project_id), body)

    def close_run(self, run_id):
        return self.send_post("close_run/{}".format(run_id), {})

    def update_run(self, run_id, data):
        """
        Updates a run with the specified data
        :param run_id: The id of the run to updated.
        :param data: The data to update the run with.
        """
        self.send_post("update_run/{}".format(run_id), data=data)

    def get_run(self, run_id):
        """Gets a specific run by id
        
        Args:
            run_id: The id of the run
        """
        return self.send_get("get_run/{}".format(run_id))

    def get_runs(self, project_id, params):
        """Gets runs that match the specified params.
        
        Args:
            project_id: The project id of the run.
            params: Dictionary of query params to filter test runs. 
            See https://www.gurock.com/testrail/docs/api/reference/runs/#getruns for fields available.
        """
        return self.send_get("get_runs/{}".format(project_id), params=params)
    
    # ------------------------------------------ RESULTS ------------------------------------------
    def add_results(self, run_id, results):
        """Adds results to the specified run

        Args:
            run_id: the run_id that the results are to be added to
            results: A list of test results. Recommended to have FAILED results added after PASSED results to avoid false positives.
            [
                {"test_id": test_id, "status_id": TestStatus const, "comment": "Some text. Optional", "elapsed": "1h 2m 30s" Optional.},
                ...
            ]
        """
        return self.send_post("add_results/{}".format(run_id), {"results": results})

    # ------------------------------------------ TESTS ------------------------------------------
    def get_tests(self, run_id):
        """Get the test ids and corresponding case ids of the specified run_id"""
        return self.send_get("get_tests/{}".format(run_id))

    # ------------------------------------------ USERS ------------------------------------------
    def get_current_user(self):
        return self.send_get("get_current_user")

    # ------------------------------------------ SUITES -------------------------------------------
    def get_suite(self, suite_id):
        """Gets a suite
        
        Args:
            suite_id: The id of the desired suite.        
        """
        return self.send_get("get_suite/{}".format(suite_id))
    
    # ------------------------------------------ PROJECTS ------------------------------------------
    def get_projects(self):
        """Gets the projects in the testrail instance"""
        return self.send_get("get_projects")

    # -------------------------------- BASE API ---------------------------------------
    def send_get(self, uri, params=None, filepath=None):
        """Issue a GET request (read) against the API.

        Args:
            uri: The API method to call including parameters, e.g. get_case/1.
            filepath: The path and file name for attachment download; used only
                for 'get_attachment/:attachment_id'.
            params: Dictionary of query params to include in url

        Returns:
            A dict containing the result of the request.
        """
        return self.__send_request('GET', uri, data=filepath, params=params)

    def send_post(self, uri, data=None, params=None):
        """Issue a POST request (write) against the API.

        Args:
            uri: The API method to call, including parameters, e.g. add_case/1.
            data: The data to submit as part of the request as a dict; strings
                must be UTF-8 encoded. If adding an attachment, must be the
                path to the file.
            params: Dictionary of query params to include in url

        Returns:
            A dict containing the result of the request.
        """
        return self.__send_request('POST', uri, data=data, params=params)

    def __send_request(self, method, uri, data=None, params=None):
        url = self.__url + uri

        if method == 'POST':
            if uri[:14] == 'add_attachment':    # add_attachment API method
                files = {'attachment': (open(data, 'rb'))}
                response = self.__s.post(url, files=files, params=params)
                files['attachment'].close()
            else:
                payload = bytes(json.dumps(data), 'utf-8')
                response = self.__s.post(url, data=payload, params=params)
        else:
            response = self.__s.get(url, params=params)

        if response.status_code > 201:
            try:
                error = response.json()
            except:     # response.content not formatted as JSON
                error = str(response.content)
            raise APIError('TestRail API returned HTTP %s (%s)' % (response.status_code, error))
        else:
            if uri[:15] == 'get_attachment/':   # Expecting file, not JSON
                try:
                    open(data, 'wb').write(response.content)
                    return (data)
                except:
                    return ("Error saving attachment.")
            else:
                try:
                    return response.json()
                except: # Nothing to return
                    return {}
