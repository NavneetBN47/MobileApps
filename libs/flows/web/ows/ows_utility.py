import json
import base64
import logging
import requests
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.web.const import SIM_API_URLS
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

PROFILES = {
    'limo': {'modelName': 'HP'},
    'palermo': {'modelName': 'HP Envy 7100 All-in-One Printer'},
    'ellis': {'modelName': 'HP'},
    'verona': {'modelName': 'HP Envy 5030'},
    'palermolow': {'modelName': 'HP Envy 7100 All-in-One Printer'},
    'palermolowder1': {'modelName': 'HP Envy 7100 All-in-One Printer'},
    'infinitybaseder2': {'modelName': 'HP TANGO'},
    'skyreach': {'modelName': 'HP LaserJet MFP'},
}
SERVER_STACKS = {
    'pie': {
        'dcs_base_uri': 'https://deviceclaim.pie.avatar.ext.hp.com/dcs-api'
    },
    'stage': {
        'dcs_base_uri': 'https://deviceclaim.stage.avatar.ext.hp.com/dcs-api',
    },
}
PROXIES = {
    'http': 'http://proxy-txn.austin.hpicorp.net:8080',
    'https': 'http://proxy-txn.austin.hpicorp.net:8080'
}

def get_dag_url(stack, endpoint_type):
    """Helper function to get DAG URLs based on stack and endpoint type"""
    if stack == 'stage':
        if endpoint_type == 'device_code':
            return SIM_API_URLS.DAG_DEVICE_CODE_STAGE
        elif endpoint_type == 'token':
            return SIM_API_URLS.DAG_TOKEN_STAGE
    else:  # pie
        if endpoint_type == 'device_code':
            return SIM_API_URLS.DAG_DEVICE_CODE_PIE
        elif endpoint_type == 'token':
            return SIM_API_URLS.DAG_TOKEN_PIE

def get_dag_client_id(stack):
    """Helper function to get DAG client ID based on stack"""
    if stack == 'stage':
        return SIM_API_URLS.DAG_CLIENT_ID_STAGE
    else:  # pie
        return SIM_API_URLS.DAG_CLIENT_ID_PIE

def create_simulated_gen2_printer(stack='pie', profile='skyreach', model_sku=False, offer=0, include_postcard=True, biz_model='E2E',
                                  include_fingerprint=True, country=False, language=False):
    # https://rndwiki.corp.hpicorp.net/confluence/pages/viewpage.action?title=Printer+Simulator+APIs&spaceKey=IWSWebPlatform
    # Supported Stacks
    #    pie
    #    stage
    # Supported Profiles
    # | profile          | model number |
    # +------------------+--------------+
    # | limo             | A7W94A       |
    # | palermo          | K7R96A       |
    # | ellis            | Y0S19A       |
    # | verona           | M2U75A       |
    # | palermolow       | K7G18A       |
    # | palermolowder1   | K7G93A       |
    # | infinitybaseder2 | 2RY54A       |
    # | skyreach         | 6GX01A       |
    #SMB Printer Profiles
    #hulk, storm, yoshino, lochsa, ulysses,selene

    """  Single SKU: Offer=1 and Dual SKU: Offer=0         """

    printer_data = {}
    create_payload = {"stack": stack,
                      "profile": profile,
                      "biz_model": biz_model,
                      "offer": offer
                      }
    if profile in ['skyreach', 'manhattan_yeti', 'storm', 'hulk', 'yoshino','lochsa', 'ulysses', 'selene', 'marconi', 'kebin', 'beam', 'zelus', 'euthinia', 'lotus', 'cherry']:
        create_payload.update({"fipsflag": "true"})
    if model_sku:
        create_payload.update({"derivative_model":model_sku})
    if country and language:
        create_payload.update({"country_region_name": country, "language": language})
    # create printer
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(SIM_API_URLS.SIMULATOR_PRINTERS, 
                         headers=headers, 
                         data=json.dumps(create_payload), 
                         verify=False, 
                         proxies=PROXIES)

    if resp.status_code != 201:
        logging.info("Failed: {} Retrying after 10s".format(resp.status_code))
        sleep(10)
        resp = requests.post(SIM_API_URLS.SIMULATOR_PRINTERS,
                            headers=headers, 
                            data=json.dumps(create_payload), 
                            verify=False, 
                            proxies=PROXIES)
        if  resp.status_code != 201:
            time_delay(resp.status_code)
            raise Exception('Create printer - Failed: {}'.format(resp.status_code))
    logging.debug("Create printer - Success")
    body = resp.json()
    serial_number = body['entity_id']
    uuid = body['uuid']
    printer_data['serial_number'] = serial_number
    printer_data['uuid'] = uuid
    printer_data['model_number'] = body['model_number']
    logging.info("Serial Number: {} uuid: {} SKU: {}".format(printer_data['serial_number'], printer_data['uuid'], printer_data['model_number']))
    # register printer
    logging.debug("Register printer - Started")
    resp = requests.post(SIM_API_URLS.SIMULATOR_PRINTERS_REGISTER.format(serial_number),
                         headers=headers,
                         verify=False,
                         proxies=PROXIES)
    if resp.status_code != 200:
        logging.info("Failed: {} Retrying after 10s".format(resp.status_code))
        sleep(10)
        resp = requests.post(SIM_API_URLS.SIMULATOR_PRINTERS_REGISTER.format(serial_number), headers=headers, verify=False, proxies=PROXIES)
        if resp.status_code != 200:
            time_delay(resp.status_code)
            raise Exception('Register printer - Failed: {} Response Text:{}'.format(resp.status_code, resp.text))
    logging.debug("Register printer - Success Cloud ID:{}".format(json.loads(resp.text)['cloud_id']))
    
    
    # create claimPostcard
    if include_postcard:
        logging.debug("Create claimPostcard - Started")
        resp = requests.post(SIM_API_URLS.SIMULATOR_PRINTERS_CLAIM_POSTCARD.format(serial_number),
                             headers=headers,
                             verify=False,
                             proxies=PROXIES)
        if resp.status_code != 200:
            time_delay(resp.status_code)
            raise Exception('Create claimPostcard - Failed: {}'.format(resp.status_code))

        logging.debug("Create claimPostcard - Success")
        printer_data['claim_postcard'] = resp.content.decode("utf-8")

    # get fingerprint
    if include_fingerprint:
        logging.debug("Get fingerprint - Started")
        resp = requests.get(SIM_API_URLS.SIMULATOR_PRINTERS_FINGERPRINT.format(serial_number),
                            headers=headers,
                            verify=False,
                            proxies=PROXIES)
        if resp.status_code != 200:
            time_delay(resp.status_code)
            raise Exception('Get fingerprint - Failed: {}'.format(resp.status_code))

        logging.debug("Get fingerprint - Success")
        fingerprint = resp.content
        printer_data['fingerprint'] = fingerprint.decode("utf-8")

    return printer_data

def get_pairing_code(printer_profile, stack, finger_print, post_card, model_number, uuid):

    # Get Pairing Code - Currently only used for portal OOBE printers
    # the pairing code expires so best to request when reach the pairing code page
    client_id = get_dag_client_id(stack)
    url = get_dag_url(stack, 'device_code')
    if printer_profile in ["selene", "ulysses", "marconi", "kebin", "marconi_pdl", "beam", "jupiter", "zelus", "euthinia", 'lotus', 'cherry']:
        finger_print = finger_print.lstrip('"').rstrip('"')
        post_card = post_card.lstrip('"').rstrip('"')
    else:
        finger_print = base64.b64encode(finger_print.encode('utf-8')).decode('utf-8')
        post_card = base64.b64encode(post_card.encode('utf-8')).decode('utf-8')
    logging.debug("Get Pairing Code - Started")
    payload = 'client_id={}&device_postcard={}&device_model={}&device_uuid={}&finger_print={}'.format(client_id,
                                                                                                     post_card,
                                                                                                     model_number,
                                                                                                     uuid,
                                                                                                     finger_print)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    resp_body = requests.post(url, headers=headers, data=payload, verify=False, proxies=PROXIES)

    if resp_body.status_code != 200:
        logging.info("Failed: {} Retrying after 10s".format(resp_body.status_code))
        sleep(10)
        resp_body = requests.post(url, headers=headers, data=payload, verify=False, proxies=PROXIES)
        if resp_body.status_code !=200:
            time_delay(resp_body.status_code)
            raise Exception('Paring code (DAG) - Failed: {}_{}'.format(resp_body.status_code, resp_body.text))
    
    device = resp_body.json()
    logging.debug("Pairing code (DAG) - Success")
    logging.debug("Pairing Code: {}".format(device['user_code']))
    
    return device

def send_complete_pairing_code(stack, device_code, uuid):
    """
    This request to be sent after input pairing code is success.
    """
    logging.debug("Send complete pairing code - Started")
    client_id = get_dag_client_id(stack)
    url = get_dag_url(stack, 'token')
    
    device_grant_auth = 'urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Adevice_code'
    payload = 'client_id={}&grant_type={}&device_code={}&device_uuid={}'.format(client_id, device_grant_auth, device_code, uuid)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    res = requests.post(url, headers=headers, data=payload, verify=False, proxies=PROXIES)
    if res.status_code != 200:
        logging.info("Failed: {} Retrying after 10s".format(res.status_code))
        sleep(10)
        re = requests.post(url, headers=headers, data=payload, verify=False, proxies=PROXIES)
        if  re.status_code != 200:
            raise Exception('Complete Paring code (DAG) - Failed: {} & {}'.format(re.status_code, re.text))
    
    logging.debug("Complete pairing code (DAG) - Success")

def get_tools_printer_code(serial_number, issuance_count=2, instant_ink=True, ownership_counter=2, version=1):
    """
    Get tools printer code from HP simulator API.
    
    Args:
        serial_number: Printer serial number
        issuance_count: Issuance count (default: 2)
        instant_ink: Enable instant ink (default: True)
        ownership_counter: Ownership counter (default: 2)
        version: API version (default: 1)
    
    Returns:
        Response JSON with printer code
    """
    logging.debug("Get tools printer code - Started")
    
    payload = {
        "version": version,
        "serial_number": serial_number,
        "issuance_count": issuance_count,
        "instant_ink": instant_ink,
        "ownership_counter": ownership_counter
    }
    
    headers = {'Content-Type': 'application/json'}
    
    resp = requests.post(SIM_API_URLS.TOOLS_PRINTER_CODE, headers=headers, json=payload, verify=False, proxies=PROXIES)
    
    if resp.status_code != 200:
        logging.info("Failed: {} Retrying after 10s".format(resp.status_code))
        sleep(10)
        resp = requests.post(SIM_API_URLS.TOOLS_PRINTER_CODE, headers=headers, json=payload, verify=False, proxies=PROXIES)
        if resp.status_code != 200:
            raise Exception('Get tools printer code - Failed: {} & {}'.format(resp.status_code, resp.text))
    
    logging.debug("Get tools printer code - Success")
    return resp.json()

def remove_printer(serial_number):
    url = SIM_API_URLS.SIMULATOR_PRINTERS_REMOVE.format(serial_number)
    logging.debug("Remove Printer Request started {}".format(serial_number))
    response = requests.request("DELETE", url, verify=False, proxies=PROXIES)
    if response.status_code != 200:
        raise Exception('Removing Printer Failed:{} & {}'.format(response.status_code, response.text))
    logging.debug("Printer Removed Successfull {}".format(response.status_code))
    return response

def get_account_details(stack, access_token):
    """
    Get user account details with tenant information.
    
    Args:
        stack: 'stage' or 'pie'
        access_token: OAuth bearer token from get_access_token()
    
    Returns:
        Response JSON with user and tenant details
    """
    logging.debug("Get account details - Started")
    
    url = SIM_API_URLS.ACCOUNT_DETAILS_PATTERN.format(stack)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    
    resp = requests.get(url, headers=headers, verify=False, proxies=PROXIES)
    
    if resp.status_code != 200:
        logging.info("Failed: {} Retrying after 10s".format(resp.status_code))
        sleep(10)
        resp = requests.get(url, headers=headers, verify=False, proxies=PROXIES)
        if resp.status_code != 200:
            raise Exception('Get account details - Failed: {} & {}'.format(resp.status_code, resp.text))
    
    logging.debug("Get account details - Success")
    return resp.json()

def claim_printer_to_account(stack, access_token, tenant_id, user_id, printer_code, printer_name="Test printer name", version="1.1"):
    """
    Claim printer to user account.
    
    Args:
        stack: 'stage' or 'pie'
        access_token: OAuth bearer token from get_access_token()
        tenant_id: Tenant ID
        user_id: User ID
        printer_code: Printer code from get_tools_printer_code()
        printer_name: Display name for printer (default: "Test printer name")
        version: API version (default: "1.1")
    
    Returns:
        Response JSON with ownership details
    """
    logging.debug("Claim printer to account - Started")
    
    url = SIM_API_URLS.CLAIM_PRINTER_PATTERN.format(stack)
    
    payload = {
        "version": version,
        "tenant_id": tenant_id,
        "user_id": user_id,
        "name": printer_name,
        "printer_code": printer_code
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    
    resp = requests.post(url, headers=headers, json=payload, verify=False, proxies=PROXIES)
    
    if resp.status_code != 200:
        logging.info("Failed: {} Retrying after 10s".format(resp.status_code))
        sleep(10)
        resp = requests.post(url, headers=headers, json=payload, verify=False, proxies=PROXIES)
        if resp.status_code != 200:
            raise Exception('Claim printer to account - Failed: {} & {}'.format(resp.status_code, resp.text))
    
    logging.debug("Claim printer to account - Success")
    return resp.json()

def load_product_config_dyn(product, uuid):
    file_path = ma_misc.get_abs_path("resources/test_data/ows/" + product + "_pcd.xml")
    fh = open(file_path)
    xml = fh.read()
    fh.close()
    return base64.b64encode(xml.format(uuid).encode("utf-8")).decode("utf-8")

def patch_credential(url, payload):
    resp = requests.patch(url, json=payload)
    if resp.status_code != 204:
        raise Exception('Patch credential - Failed: {}'.format(resp.status_code))
    else:
        return True

def time_delay(status_code):
    # Time delay for server errors
    if status_code in [503,504,500]:
        sleep(180)