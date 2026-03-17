# coding: utf-8
import requests
import logging
import json
from APILib.request_util import ApiRequest, ApiResponse
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from MobileApps.libs.flows.android.hpbridge.utility.random_utility import RandomUtility
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrinterInfo, PrintSetting, SupplyInfo, Cartridge, SupplyStatus
import time


class APIUtility(object):

    timeout = 120
    encoding = "utf-8"

    def __init__(self):
        stack = utlitiy_misc.load_stack_info()
        user = utlitiy_misc.load_user_device()[0]
        self.test_stack = stack["stack"]
        self.host = stack["host"]
        self.client = stack["client"]
        self.user_id = user["hpid"][self.test_stack.lower()]
        self.access_token = self.get_user_token()

    def get_user_token(self):
        """
        Using hpbridge user id to get the user access token
        :return:
        """
        response = ApiRequest\
            .get(self.host["management"])\
            .add_path("token-management/oauth2/token")\
            .add_param("userId", self.user_id) \
            .add_param("grant_type", "user_token") \
            .set_token("basic " + self.client) \
            .send()\
            .assert_status(200)\
            .json()
        user_token = response["token_type"] + " " + response["access_token"]
        return user_token

    def get_bound_printers(self):
        """
        Get all bound printers for the given user
        :return: the bound printer list
        """
        return ApiRequest\
            .get(self.host["management"])\
            .add_path("device-management/mydevices")\
            .set_token(self.access_token)\
            .send()\
            .assert_status(200)\
            .json()

    def get_printer_amount(self):
        """
        Get the user's bound printers' amount
        :return: the printers' amount
        """
        return len(self.get_bound_printers())

    def get_printer_status(self, printer_id):
        """
        Get the printe's status
        :param printer_id: the printer id in HP Bridge DB
        :return:
        """
        response = ApiRequest\
            .get(self.host["management"])\
            .add_path("device-status/device/{}/status".format(printer_id))\
            .set_token(self.access_token)\
            .send()
        if response.status == 200:
            return response.json()["connection_state"], response.json()["printer_state"]
        else:
            logging.warning("Failed to get the printer's status with reqeust status = %s" % response.status)
            return None

    def get_printer_id_by_name(self, printer_name):
        """
        Using the customised printer name to get the printer id from DB,
        only can get the printers which are bound with the user
        :param printer_name: the customised printer name
        :return:
        """
        printer_list = self.get_bound_printers()
        for printer in printer_list:
            if printer["device_personality"]["device_name"] == printer_name:
                return printer["device_basic_data"]["device_id"]

        raise KeyError("Failed to find the match printer with the given name: %s " % printer_name)

    def get_printer_info_by_id(self, printer_id):
        """
        Using the printer id to get the printer's detail information
        :param printer_id: the printer's id
        :return:
        """
        return ApiRequest\
            .get(self.host["management"]) \
            .add_path("device-management/devices/{}".format(printer_id)) \
            .add_param("return_type", "eprint") \
            .set_token(self.access_token)\
            .send()\
            .assert_status(200) \
            .json()

    def get_dbt_by_qrcode(self, printer_id, is_return=True):
        """
        Generate qr code by using the printer's email, sku and cloud id
        :param printer_id: the printer's id
        :return:
        """

        api_response = ApiRequest \
            .post(self.host["management"]) \
            .add_path("device-management/devices/{}/qrcode".format(printer_id)) \
            .set_token(self.access_token) \
            .send()\
            .assert_status(200)\
            .json()
        if is_return:
            return api_response["content"].split("&dbt=")[1]
        else:
            return api_response


    def unbind_printer(self, printer_id):
        """
        Unbind the printer from the user
        :param printer_id: the printer id need to be unbound
        :return:
        """
        ApiRequest\
            .delete(self.host["management"])\
            .add_path("device-management/mydevices/{}".format(printer_id))\
            .set_token(self.access_token)\
            .send()\
            .assert_status(204)

    def unbind_all_printers(self):
        """
        Unbind all the bound printers under the user
        """
        printer_list = self.get_bound_printers()
        for printer in printer_list:
            self.unbind_printer(printer["device_basic_data"]["device_id"])

        logging.info("Unbind all the printers under the user for clean up")

    def bind_printer(self, printer_id, dbt, custom_printer_name, default_device=True, device_group="QA room", optimize_printer=False, scene=None):
        """
        For some cases' request, we need bind some printers before test, and the bind printer steps is not the key step
         for these test cases, im order to save time, we use bind printer API to satisfy the cases' precondition
        :param printer_id: The printer's device ID in HP Bridge DB
        :param custom_printer_name: customise the printer's name
        :param default_device: if true, set the device as user's default device
        :param device_group: set the device's group
        :param optimize_printer: Horizon printer special param, if optimizePrinter is true，we will call wpp to set qos
        polling interval  from 6min to 10s.
        :param dbt: the device's dbt(device binding token)
        :param scene:
        :return:
        """

        body = {"optimize_printer": optimize_printer, "default_device": default_device,
                "device_name": custom_printer_name, "device_group": device_group}
        response = ApiRequest\
            .post(self.host["management"])\
            .add_path("device-management/mydevices/{}".format(printer_id))\
            .add_param("dbt", dbt)\
            .add_param("scene", scene)\
            .set_token(self.access_token)\
            .set_body(body)\
            .send()\
            .assert_status(200)
        logging.info("Succeed to bind a printer to the user with customised printer name: " + custom_printer_name)
        return response.json()

    def get_dbt(self, printer_id):
        """
        Get the printer's BDT, which used to bind the printer
        :param printer_id: the printer's id
        :return:
        """
        return ApiRequest\
            .post(self.host["management"])\
            .add_path("device-management/devices/{}/dbt".format(printer_id))\
            .set_token(self.access_token)\
            .send()\
            .assert_status(200) \
            .json()["token"]

    def bind_default_printer(self, printer_name=None):
        """
        From the test printers.json file to load the default printer info, and bind the printer to the user
        :return:
        """
        printer = utlitiy_misc.load_printer(printer_name, stack=self.test_stack, api_used=True)
        custom_printer_name = RandomUtility.generate_digit_letter_strs(10)

        dbt = self.get_dbt_by_qrcode(printer["printer_id"])
        return self.bind_printer(printer["printer_id"], dbt, custom_printer_name)


    def get_printer_info(self, printer_id):
        """
        Using the device id to get the bound device's default print setting
        :param printer_id: the printer id
        :return:
        """
        return ApiRequest \
            .get(self.host["management"]) \
            .add_path("device-management/devices/{}".format(printer_id)) \
            .set_token(self.access_token) \
            .send() \
            .assert_status(200) \
            .json()

    def get_supply_info(self, printer_id):
        """
        Get the supply information for Gen1 printers, for Gen2 printers, the API will return "not support" message
        :param printer_id: the printer's device id in bridge DB
        :return:
        """

        response = ApiRequest \
            .get(self.host["management"]) \
            .add_path("device-status/devices/{}/supplies".format(printer_id)) \
            .set_token(self.access_token) \
            .send()

        if response.status == 404 and response.json()["error_code"] == "40416":
            return SupplyStatus.NotSupport
        elif response.status == 200:
            return response.json()
        else:
            return SupplyStatus.Error

    def get_print_jobs(self, printer_id, page=0, size=5):
        """
        Get current user's print job history, only get the last five jobs
        :return:
        """
        return ApiRequest \
            .get(self.host["iot"]) \
            .add_path("iot/users/{}/printjobs".format(printer_id)) \
            .add_param("page", page) \
            .add_param("size", size) \
            .set_token(self.access_token) \
            .send() \
            .assert_status(200) \
            .json()

    def wait_last_print_job_complete(self, timeout=180):
        """
        Get the the user's last job's status. wait for it complete, no matter it succeed or failed
        :param timeout: the timeout
        :return:
        """
        job_status = self.get_print_jobs()[0]["printJobStatus"]
        start_time = time.time()
        time_cost = 0
        while job_status in [1, 2, 3] and time_cost <= timeout:
            job_status = self.get_print_jobs()[0]["printJobStatus"]
            time.sleep(5)
            time_cost = time.time() - start_time

        if time_cost > timeout:
            raise TimeoutError("Print job not finised in %s seconds" % timeout)

        return True

    def download_qrcode(self, printer_id):
        """
        generate QRcode and then download QRCode
        :param printer_id:
        :return:
        """
        pass
