import re
import logging

from MobileApps.libs.testrail.testrail_api import TestRailAPI, TestStatus
from MobileApps.libs.ma_misc import ma_misc


PYTEST_TO_TESTRAIL_STATUS = {
    "passed": TestStatus.PASSED,
    "failed": TestStatus.FAILED,
    "skipped": TestStatus.BLOCKED
}

class TestRailMisc:
    def __init__(self):
        testrail_cfg = ma_misc.load_system_config_file()["testrail_info"]
        self.api = TestRailAPI(testrail_cfg["username"], testrail_cfg["api_key"], testrail_cfg["instance_url"])

    def push_results_to_testrail(self, run_name, pytest_results, run_milestone=None, version=None, run_info=None, test_info=None, close_run=False):
        """
        Creates a test run(s) and pushes test results to it. Must mark test with pytest.mark.testrail to link it to a TestRail test case.
        :param run_name: The name for created TestRail runs.
        :param pytest_results: The test item and results to be pushed to TestRail. A dict of form {pytest Test Item: pytest Test Report,...}.
        :param version: Version of the application being tested.
        :param run_info: Dictionary of additional info to include in test run description.
        :param test_info: Dictionary of additional info to include in test result comments.
        :param close_run: Close the run(s) once the results are pushed to it.
        NOTE: A TestRail run will be created for each TestRail suite that needs results to be pushed.
        """
        tr_id_pattern = re.compile(r"S(?P<suite>\d+).C(?P<case>\d+)")

        if run_info is not None:
            run_info = "\n".join("{}: {}".format(k, v) for k, v in run_info.items())
        if test_info is not None:
            test_info = "\n".join("{}: {}".format(k, v) for k, v in test_info.items())

        #Gather/format test results and group by testrail suite
        test_results = dict()  # keys are suite_ids, values are lists of testrail results as defined below
        """Each testrail results is formatted as 
        {
            "case_id": TestRail case_id,
            "status_id": TestStatus const, 
            "comment": "", # comment to include on the  results for the test case. By default includes NodeID of pytest test(Includes comment_info if provided)
            "elapsed": "100s",  # 100 seconds 
            "defects": "AIOA-1234,OWS-1111"  # string containing comma separated list of defect ids. Optional and is only included if test failed
        }
        """
        for test, result in pytest_results.items():
            if (tr_marker := test.get_closest_marker("testrail")) == None:
                continue
            for tr_marker_val in tr_marker.args:
                defects = None
                if not isinstance(tr_marker_val, str):
                    id_str, defects = tr_marker_val
                else:
                    id_str = tr_marker_val
                tr_id = tr_id_pattern.match(id_str)
                tr_suite = int(tr_id["suite"])
                tr_case = int(tr_id["case"])
                tr_status = PYTEST_TO_TESTRAIL_STATUS[result.outcome]
                tr_result = {
                    "case_id": tr_case,
                    "status_id": tr_status,
                    "elapsed": "{}s".format(1 if result.duration < 1 else round(result.duration)),
                    "comment": "Test: {}".format(test.nodeid) + ("\n{}".format(test_info) if test_info else "")
                }
                if tr_status == TestStatus.FAILED and defects is not None:
                    tr_result["defects"] = defects if isinstance(defects, str) else ",".join(defects)
                if version:
                    tr_result["version"] = version
                if tr_suite not in test_results:
                    test_results[tr_suite] = [tr_result]
                elif tr_result["status_id"] != TestStatus.FAILED:
                    test_results[tr_suite] = [tr_result] + test_results[tr_suite]
                else:  # make sure failed tests are at end of results list to avoid false positive test results
                    test_results[tr_suite].append(tr_result)

        if len(test_results) == 0:
            logging.info("No collected tests have been linked to TestRail.")
            return False

        # Get project_ids for query of open runs
        project_ids = set()
        for suite_id in test_results:
            project_ids.add(self.api.get_suite(suite_id)["project_id"])

        # Get open runs
        user_id = self.api.get_current_user()["id"]
        open_runs = list()
        for project_id in project_ids:
            open_runs.extend(self.api.get_runs(project_id, {"is_completed": 0, "created_by": user_id}))

        for suite_id, results in test_results.items():
            # Find open run to push results to
            run_record = None
            for run in open_runs:
                if run_name == run["name"] and suite_id == run["suite_id"]:
                    run_record = run
                    break
            # Create new run if unable to find usable run
            if run_record == None:
                project_id = self.api.get_suite(suite_id)["project_id"]
                run_record = self.api.add_run(run_name, project_id, suite_id, run_milestone, description=run_info if run_info else "", case_ids=[r["case_id"] for r in results])
                test_records = self.api.get_tests(run_record["id"])
            else:
                # Make sure existing run has all case ids for collected results
                test_records = self.api.get_tests(run_record["id"])
                if self.add_cases_to_run(run_record["id"], {result["case_id"] for result in results}, test_records=test_records):
                    test_records = self.api.get_tests(run_record["id"])  # Get fresh test records if any cases were added
            
            # Overwrite case_ids with test_ids on results
            case_ids_to_test_ids = {test["case_id"]: test["id"] for test in test_records}
            for result in results:
                result["test_id"] = case_ids_to_test_ids[result["case_id"]]
                del result["case_id"]

            # Add results to test run
            self.api.add_results(run_record["id"], results)
            logging.info('Pushed test results to testrail run {}({}). Available at {}'.format(run_record["name"], run_record["id"], run_record["url"]))

            if close_run:
                self.api.close_run(run_record["id"])
                logging.info("Closed run {}".format(run_record["id"]))
        return True

    def add_cases_to_run(self, run_id, case_ids, test_records=None):
        """
        Adds additional test cases to an existing test run.
        :param run_id: The id of the run that will receive the new cases
        :param case_ids: Set of case ids that should be added to the run.
        :param test_records: The test records that are currently on the test. If None fresh test_records will be requested.
        :return: Returns True if run was updated. False if run was not updated.
        """
        if not test_records:
            test_records = self.api.get_tests(run_id)
        current_case_ids = {test["case_id"] for test in test_records}
        case_ids = case_ids.union(current_case_ids)

        if case_ids == current_case_ids:
            return False

        self.api.update_run(run_id, {"include_all": False, "case_ids": list(case_ids)})
        return True

    def close_runs_by_name(self, run_name, current_user=False):
        """
        Closes open testrail runs by name.
        :param run_name: Name of the run(s) to close
        :param current_user: Only close runs that were created by the current user
        :return: The records of the runs that were closed.
        """
        project_ids = [project_record["id"] for project_record in self.api.get_projects()]
        
        run_filter = {"is_completed": 0}
        if current_user:
            run_filter["created_by"] = self.api.get_current_user()["id"]

        closed_run_records = list()
        for project_id in project_ids:
            for run_record in self.api.get_runs(project_id, run_filter):
                if run_record["name"] == run_name:
                    self.api.close_run(run_record["id"])
                    closed_run_records.append(run_record)
        return closed_run_records
