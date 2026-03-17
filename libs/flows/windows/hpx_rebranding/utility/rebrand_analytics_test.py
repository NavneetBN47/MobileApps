
import requests
import json
import time
import logging
from MobileApps.libs.ma_misc import ma_misc

class RebrandAnalyticsTest:

    def validate_analytics_result(self, analytics_data):
        actual_count = analytics_data.get('actual_count')
        expected_count = analytics_data.get('expected_count')
        pass_rate = analytics_data.get('pass_rate')
        failed_records = analytics_data.get('failed_records', [])

        if actual_count != expected_count:
            if failed_records:
                logging.info("Field validation failures:")
                for record in failed_records:
                    logging.info(f"Record #{record['record_number']}:")
                    for mismatch in record['mismatched_fields']:
                        logging.info(f"  Field: {mismatch['field']}")
                        logging.info(f"  Expected: {mismatch['expected']}")
                        logging.info(f"  Actual: {mismatch['actual']}")
                logging.info(f"Count mismatch: Expected {expected_count}, got {actual_count}")
                return False
            else:
                logging.info(f"Count mismatch: Expected {expected_count}, got {actual_count}")
                return False

        return True

    def execute_analytics_test_and_validate_result(self, start_time, open_serach_filter_json, test_name, event_count):

        # This filter is how we filter out the data we want from Open Search.
        query_config_file = ma_misc.get_abs_path(open_serach_filter_json)
        with open(query_config_file, "r+") as f:
            query_config = json.load(f)

        base_url = 'http://ps0immshwin20.scs.rd.hpicorp.net:5002'
        max_wait_time = 8 * 60
        wait_interval = 60
        total_waited = 0
        minutes_range = 8

        # Based on the actions we have done compared to the number of events. 
        # event_count: expect to verify the number of events
        # start_time: the starting time for an open search query.
        # And also, we need to compare all values fields.["version", "viewHierarchy", "viewName", "viewModule", "action", "actionDetail", "actionAuxParams", "controlName", "controlLabel", "controlAuxParams"]
        # Once the event count is consistent, wait for an additional minute to ensure no new events are added.
        while total_waited <= max_wait_time:
            response = requests.post(
                f'{base_url}/test/{test_name}/{event_count}/{start_time}',
                headers={'Content-Type': 'application/json'},
                json=query_config,
                timeout=30
            )

            analytics_data = response.json()
            logging.info("Current response:")
            logging.info(json.dumps(analytics_data, indent=2))

            actual_count = analytics_data.get('actual_count')
            expected_count = analytics_data.get('expected_count')

            if actual_count > expected_count:
                self.validate_analytics_result(analytics_data)
                assert False, "Actual event count is greater than expected event count, please check the log for more details."

            if actual_count == expected_count:
                logging.info("Count matches! Waiting 1 minute for final check...")
                time.sleep(60)
                minutes_range += 1

                final_response = requests.post(
                    f'{base_url}/test//{test_name}/{event_count}/{start_time}',
                    headers={'Content-Type': 'application/json'},
                    json=query_config,
                    timeout=30
                )
                final_data = final_response.json()
                logging.info("Final response:")
                logging.info(json.dumps(final_data, indent=2))

                if self.validate_analytics_result(final_data):
                    logging.info("Test completed successfully!")
                    assert True
                else:
                    logging.info("Test failed in final validation!")
                    self.validate_analytics_result(final_data)
                    assert False, "Test failed in final validation! Please check the log for more details."
                break

            logging.info(f"Waiting for count to match... ({total_waited}/{max_wait_time} seconds)")
            time.sleep(wait_interval)
            total_waited += wait_interval

        else:
            self.validate_analytics_result(analytics_data)
            logging.info(f"Reached maximum wait ({max_wait_time} seconds) time without matching count.")
            logging.info("Test failed!")
            assert False, f"Reached maximum wait ({max_wait_time} seconds) time without matching count."
    
    def custom_filter_json_file(self, open_serach_filter_json, custom_values, custom_field_expetcted_values=None):
        # read JSON file
        new_filter_file = ma_misc.get_abs_path(open_serach_filter_json)
        with open(new_filter_file, 'r+') as f:
            data = json.load(f)

        # update JSON file
        for key, value in custom_values.items():
            if key == "viewHierarchy":
                # update viewHierarchy condition
                new_condition = {
                    "match_phrase": {
                        "fields.xray.bodyString": f'"{key}":{json.dumps(value)}'
                    }
                }
            elif key != "serial_number":
                new_condition = {
                    "match_phrase": {
                        "fields.xray.bodyString": f'"{key}":"{value}"'
                    }
                }

            updated = False
            for i, existing in enumerate(data["must"]):
                if new_condition["match_phrase"]["fields.xray.bodyString"].split(':')[0] in existing["match_phrase"]["fields.xray.bodyString"]:
                    data["must"][i] = new_condition
                    updated = True
                    break

            # if not updated, add new condition
            if not updated and value:  # only add new condition when custom value is not empty
                data["must"].append(new_condition)

        # replace the value of the last condition in must array with serial_number
        if data["must"]:
            last_condition = data["must"][-1]  # get the last condition
            if "match_phrase" in last_condition and "fields.xray.bodyString" in last_condition["match_phrase"]:
                last_condition["match_phrase"]["fields.xray.bodyString"] = custom_values["serial_number"]

        # if custom_field_expetcted_values is provided, add it to the same level as must, if not clear values for custom field
        if custom_field_expetcted_values is not None:
            data["custom_field_expetcted_values"] = custom_field_expetcted_values
        else:
            data["custom_field_expetcted_values"] = {}

        # write the updated data back to the original file
        with open(new_filter_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def create_custom_filter(self, serial_number, view_name, view_module, action, control_name, action_detail=""):
        if view_module != view_name:
            view_hierarchy = ["base:/", f"mfe:/{view_module}/{view_name}/"]
        else:
            view_hierarchy = ["base:/", f"mfe:/{view_module}/"]
        return {
            "version": "2.0.0",
            "viewHierarchy": view_hierarchy,
            "viewName": view_name,
            "viewMode": "",
            "viewModule": view_module,
            "action": action,
            "actionDetail": action_detail,
            "actionAuxParams": "",
            "controlName": control_name,
            "controlLabel": control_name,
            "controlAuxParams": "",
            "serial_number": serial_number,
        }

    def verify_analytics(self, json_file, custom_filter, query_start_time, feature_name, count):
        self.custom_filter_json_file(json_file, custom_filter)
        self.execute_analytics_test_and_validate_result(query_start_time, json_file, feature_name, count)