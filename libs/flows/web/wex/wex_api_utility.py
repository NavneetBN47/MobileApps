import base64
import requests
import json
import random 
import string  
import logging
import socket
import os
from MobileApps.libs.ma_misc import ma_misc

# PROXIES = {
#     'http': 'http://manual-proxy.us.hpicorp.net:8080',
#     'https': 'http://manual-proxy.us.hpicorp.net:8080'
# }

def get_active_proxies():
    # If running in Azure Pipeline (TF_BUILD) or explicitly disabled, don't use the hardcoded proxy
    if os.getenv('TF_BUILD') or os.getenv('AGENT_NAME') or os.getenv('WEX_DISABLE_PROXY'):
        return None
    
    # If standard proxy env vars are set, use them
    if os.getenv('HTTP_PROXY') or os.getenv('HTTPS_PROXY'):
        return {
            'http': os.getenv('HTTP_PROXY'),
            'https': os.getenv('HTTPS_PROXY')
        }

    # Default to corporate proxy for local HP network development
    return {
        'http': 'http://manual-proxy.us.hpicorp.net:8080',
        'https': 'http://manual-proxy.us.hpicorp.net:8080'
    }

PROXIES = get_active_proxies()

def get_authorization_token(stack, client_id, client_secret):
    account = ma_misc.get_wex_account_info(stack)
    if stack == 'stage':
        CLIENT_ID = client_id
        CLIENT_SECRET = client_secret
    elif stack == 'pie':
        CLIENT_ID = client_id
        CLIENT_SECRET = client_secret
    elif stack == 'test':
        CLIENT_ID = client_id
        CLIENT_SECRET = client_secret

    auth_value = f'{CLIENT_ID}:{CLIENT_SECRET}'
    auth_value_bytes = auth_value.encode('ascii')
    auth_value_b64 = base64.b64encode(auth_value_bytes).decode('ascii')

    tokendata = {
        "grant_type": "client_credentials",
        # "scope":"openid offline_access billinginfo.wpp.api.hp.com/get",
        "response_type": "code"
    }
    
    tokenHeaders = {
        "Accept": "*/*",
        "Authorization": f'Basic {auth_value_b64}',
        # "User-Agent":"POSTMAN/Prod ArrakisApiClient Arrakis/Windows 7",
        "Content-Type": "application/x-www-form-urlencodedn",
        "charset": "ISO-8859-1"
    }
    
    if stack == "stage":
        token_url = "https://stage.authz.wpp.api.hp.com/openid/v1/token"
    elif stack == "pie":
        token_url = "https://stage.authz.wpp.api.hp.com/openid/v1/token"
    elif stack == "test":
        token_url = "https://stage.authz.wpp.api.hp.com/openid/v1/token"
    
    response = requests.post(token_url, headers=tokenHeaders, params=tokendata)
    if response.status_code != 200:
        logging.info("Authorization Token generation Failed: {} ".format(response.status_code))
        raise Exception('Authorization Token - Failed: {} Response Text:{}'.format(response.status_code, response.text))
    else:
        return response.json()["access_token"]
    
    
def get_api_response(stack, api_uri):
    account = ma_misc.get_wex_account_info(stack)
    if stack == 'stage':
        CLIENT_ID = account["client_id"]
        CLIENT_SECRET = account["client_secret"]
    elif stack == 'pie':
        CLIENT_ID = account["client_id"]
        CLIENT_SECRET = account["client_secret"]
    elif stack == 'test':
        CLIENT_ID = account["client_id"]
        CLIENT_SECRET = account["client_secret"]

    access_token = get_authorization_token(stack, CLIENT_ID, CLIENT_SECRET)
    headers= {
        'Authorization': 'Bearer ' + access_token,
        'User-Agent':'PostmanRuntime/7.32.2',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    
    api_url = api_uri
    response = requests.get(url=api_url, headers=headers, verify=True, proxies=PROXIES, timeout=30)
    return response

def get_fleet_proxy_verification_code(stack):
    # Generate Fleet Proxy verification user code
    account = ma_misc.get_wex_account_info(stack)
    if stack == 'stage':
        CLIENT_ID = account["oc_client_id"]
        api_url = "https://oauth-auth.stg.oc.hp.com/oauth2/v1/device/authorize"
    elif stack == 'pie':
        CLIENT_ID = account["oc_client_id"]
        api_url = "https://oauth-auth.stg.oc.hp.com/oauth2/v1/device/authorize"
    elif stack == 'test':
        CLIENT_ID = account["oc_client_id"]
        api_url = "https://oauth-auth.stg.oc.hp.com/oauth2/v1/device/authorize"
    
    data={
        "client_id": CLIENT_ID,
        "device_info": "Automation-"+socket.gethostname()
    }

    headers= {
        "Accept": "*/*",
        # "User-Agent":"POSTMAN/Prod ArrakisApiClient Arrakis/Windows 7",
        "Content-Type": "application/x-www-form-urlencodedn",
        "charset": "ISO-8859-1"
    }
    
    response = requests.post(url=api_url, headers=headers, params=data, verify=True, proxies=PROXIES)
    if response.status_code != 200:
        logging.info("fleet proxy verification code generation Failed: {} ".format(response.status_code))
        raise Exception('fleet proxy verification code generation - Failed: {} Response Text:{}'.format(response.status_code, response.text))
    else:
        return response.json()["user_code"]
    
def get_resourceid(stack, access_token, username):
    #Generate resourceid from the usermgtsvc/users a.
    headers= {
        'Authorization': 'Bearer ' + access_token,
        'User-Agent':'PostmanRuntime/7.32.2',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    data={
        "email": username
    }

    if stack == "stage":
        user_api_uri="https://stratus-stg.tropos-rnd.com/v3/usermgtsvc/users"
    elif stack == "pie":
        user_api_uri="https://stratus-pie.tropos-rnd.com/v3/usermgtsvc/users"
    elif stack == "test":
        user_api_uri="https://stratus-stg.tropos-rnd.com/v3/usermgtsvc/users"

    response = requests.get(url=user_api_uri, headers=headers, params=data, verify=True, proxies=PROXIES)
    return response.json()['resourceList'][0]['resourceId']

def get_tenantResourceId(stack, access_token, resourceid):
    #Generate the tenantResourceId
    headers= {
        'Authorization': 'Bearer ' + access_token,
        'User-Agent':'PostmanRuntime/7.32.2',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    if stack == "stage":
        usertenant_api_uri="https://stratus-stg.tropos-rnd.com/v3/usermgtsvc/usertenantdetails?userResourceId=" + resourceid
    elif stack == "pie":
        usertenant_api_uri="https://stratus-pie.tropos-rnd.com/v3/usermgtsvc/usertenantdetails?userResourceId=" + resourceid
    elif stack == "test":
        usertenant_api_uri="https://stratus-stg.tropos-rnd.com/v3/usermgtsvc/usertenantdetails?userResourceId=" + resourceid
    
    tenant_response = requests.get(url=usertenant_api_uri, headers=headers,verify=True, proxies=PROXIES)
    for i in range(tenant_response.json()["resourceList"].__len__()):
        if tenant_response.json()["resourceList"][i]["tenantType"] == "BusinessMPSCompany":
            tenantResourceId=tenant_response.json()["resourceList"][i]["tenantResourceId"]
            break
    return tenantResourceId

def get_user_token(stack):
    # Get service user token
    account = ma_misc.get_wex_account_info(stack)
    if stack == 'stage':
        CLIENT_ID = account["usermgt_clientId"]
        CLIENT_SECRET = account["usermgt_clientSecret"]
        username = account["it_admin_email"]
    elif stack == 'pie':
        CLIENT_ID = account["usermgt_clientId"]
        CLIENT_SECRET = account["usermgt_clientSecret"]
        username = account["it_admin_email"]
    elif stack == 'test':
        CLIENT_ID = account["usermgt_clientId"]
        CLIENT_SECRET = account["usermgt_clientSecret"]
        username = account["it_admin_email"]
    access_token = get_authorization_token(stack, CLIENT_ID, CLIENT_SECRET)
    
    #Generate resourceid from the usermgtsvc/users a.
    resourceid = get_resourceid(stack, access_token, username)
    
    #Generate the tenantResourceId
    tenantResourceId = get_tenantResourceId(stack, access_token, resourceid)

    #Generate the User token
    auth_value = f'{CLIENT_ID}:{CLIENT_SECRET}'
    auth_value_bytes = auth_value.encode('ascii')
    auth_value_b64 = base64.b64encode(auth_value_bytes).decode('ascii')
    userHeaders= {
        "Authorization": f'Basic {auth_value_b64}',
        'User-Agent':'PostmanRuntime/7.32.2',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        "Content-Type": "application/json"
    }
    data={
        'grant_type':'urn:ietf:params:oauth:grant-type:token-exchange',
        'subject_token': access_token,
        'subject_token_type': 'urn:ietf:params:oauth:token-type:access_token',
        'requested_user_type': 'hp:authz:params:oauth:user-id-type:stratusid',
        'requested_user': resourceid,
        'tenant_id': tenantResourceId
    }
    
    if stack == "stage":
        token_url = 'https://stage.authz.wpp.api.hp.com/openid/v1/token'
    elif stack == "pie":
        token_url = 'https://pie.authz.wpp.api.hp.com/openid/v1/token'
    elif stack == "test":
        token_url = 'https://stage.authz.wpp.api.hp.com/openid/v1/token'
    
    response = requests.post(token_url, headers=userHeaders, params=data)
    if response.status_code != 200:
        logging.info("User Token generation Failed: {} ".format(response.status_code))
        raise Exception('User Token - Failed: {} Response Text:{}'.format(response.status_code, response.text))
    else:
        return response.json()["access_token"]

def get_assessment_report(stack, api_uri):
    account = ma_misc.get_wex_account_info(stack)
    #get User Token
    user_token = get_user_token(stack)
    headers= {
        'Authorization': 'Bearer ' + user_token,
        'User-Agent':'PostmanRuntime/7.32.2',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    
    api_url = api_uri
    response = requests.get(url=api_url, headers=headers, verify=True, proxies=PROXIES)
    return response

def get_cloud_iot_base_v1_uri(stack):
        cloud_iot_base_dict = {
            "pie": "https://devices.pie-us1.api.ws-hp.com/devices/v1",
            "stage": "https://devices.stage-us1.api.ws-hp.com/devices/v1",
            "production": "https://devices.prod-us1.api.ws-hp.com/devices/v1",
            "test": "https://devices.stage-us1.api.ws-hp.com/devices/v1"
        }
        return cloud_iot_base_dict.get(stack, "Stack not found")
 
def get_cloud_iot_base_v2_uri(stack):
        cloud_iot_base_dict = {
            "pie": "https://devices.pie-us1.api.ws-hp.com/devices/v2",
            "stage": "https://devices.stage-us1.api.ws-hp.com/devices/v2",
            "production": "https://devices.prod-us1.api.ws-hp.com/devices/v2",
            "test": "https://devices.stage-us1.api.ws-hp.com/devices/v2"
        }
        return cloud_iot_base_dict.get(stack, "Stack not found")
 
def get_cloud_api_response(stack, api_uri):
    account = ma_misc.get_wex_account_info(stack)
    if stack == 'stage':
        CLOUD_CLIENT_ID = account["cloud_client_id"]
        CLOUD_CLIENT_SECRET = account["cloud_client_secret"]
    elif stack == 'pie':
        CLOUD_CLIENT_ID = account["cloud_client_id"]
        CLOUD_CLIENT_SECRET = account["cloud_client_secret"]
    elif stack == 'test':
        CLOUD_CLIENT_ID = account["cloud_client_id"]
        CLOUD_CLIENT_SECRET = account["cloud_client_secret"]
 
    access_token = get_authorization_token(stack, CLOUD_CLIENT_ID, CLOUD_CLIENT_SECRET)
    headers= {
        'Authorization': 'Bearer ' + access_token,
        'User-Agent':'PostmanRuntime/7.32.2',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
   
    api_url = api_uri
    response = requests.get(url=api_url, headers=headers, verify=True, proxies=PROXIES)
    return response

#Test code for debugging
if __name__ == "__main__":
    pass
    
def create_simulator(stack, profile, api_uri):
    #The create_simulator function is designed to create a simulator device in the G2 Simulator by sending a POST request to a specified API endpoint.
    # Parameters
    # - stack (str): The stack environment (e.g., "stage", "pie") to be used in the payload.
    # - profile (str): The profile to be used in the payload.
    # - api_uri (str): The API endpoint URI to which the POST request will be sent.
    PAYLOAD = {
        "stack": stack,
        "profile": profile,
        "fipsflag": "true",
        "biz_model": "Flex"
    }
    # The headers for the POST request are:
    HEADERS= {
        'User-Agent':'PostmanRuntime/7.40.0',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        "Content-Type": "application/json",
        'Connection': 'keep-alive'
    }
    try:
        response = requests.post(url=api_uri, headers=HEADERS, json=PAYLOAD, verify=False, proxies=PROXIES)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None

def registering_simulator(stack_name, api_uri):
    # The registering_simulator function is designed to register a simulator device in the G2 Simulator by sending a POST request to a specified API endpoint.
    # Parameters
    # stack (str): The stack environment (e.g., "stage", "pie") to be used in the payload.
    # api_uri (str): The API endpoint URI to which the POST request will be sent.
    PAYLOAD = {
        "stack": stack_name
    }
    # The headers for the POST request are:
    HEADERS= {
        'User-Agent':'PostmanRuntime/7.40.0',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        "Content-Type": "application/json",
        'Connection': 'keep-alive'
    }
    try:
        response = requests.post(url=api_uri, headers=HEADERS, json=PAYLOAD, verify=False, proxies=PROXIES)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None
    
def pre_registering_the_device(stack , entity_id, model_number, api_uri):
    # The pre_registering_the_device function is designed to pre-register a device in the G2 Simulator by sending a POST request to a specified API endpoint.
    # Parameters
    # stack (str): The stack environment (e.g., "stage", "pie") to be used for retrieving account information and generating the authorization token.
    # entity_id (str): The entity ID of the device to be pre-registered.
    # model_number (str): The model number of the device to be pre-registered.
    # api_uri (str): The API endpoint URI to which the POST request will be sent.
    account = ma_misc.get_wex_account_info(stack)
    if stack == 'stage':
        CLIENT_ID = account["cloud_client_id"]
        CLIENT_SECRET = account["cloud_client_secret"]
    elif stack == 'pie':
        CLIENT_ID = account["cloud_client_id"]
        CLIENT_SECRET = account["cloud_client_secret"]
    elif stack == 'test':
        CLIENT_ID = account["cloud_client_id"]
        CLIENT_SECRET = account["cloud_client_secret"]
    access_token = get_authorization_token(stack, CLIENT_ID, CLIENT_SECRET)
    # The headers for the POST request are:
    HEADERS= {
        'Authorization': 'Bearer ' + access_token,
        'User-Agent':'PostmanRuntime/7.32.2',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    PAYLOAD = {
         "deviceInfo": {
            "productNumber": model_number,
            "serialNumber": entity_id
        }
    }

    try:
        response = requests.post(url=api_uri, headers=HEADERS, json=PAYLOAD, verify=False, proxies=PROXIES)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None

def unregister_the_device(stack , entity_id, model_number, api_uri):
    # The unregister_the_device function is designed to unregister a device from the G2 Simulator by sending a DELETE request to a specified API endpoint.
    # Parameters
    # stack (str): The stack environment (e.g., "stage", "pie") to be used for authentication.
    # entity_id (str): The serial number of the device to be unregistered.
    # model_number (str): The model number of the device to be unregistered.
    # api_uri (str): The API endpoint URI to which the DELETE request will be sent.
    account = ma_misc.get_wex_account_info(stack)
    if stack == 'stage':
        CLIENT_ID = account["cloud_client_id"]
        CLIENT_SECRET = account["cloud_client_secret"]
    elif stack == 'pie':
        CLIENT_ID = account["cloud_client_id"]
        CLIENT_SECRET = account["cloud_client_secret"]
    elif stack == 'test':
        CLIENT_ID = account["cloud_client_id"]
        CLIENT_SECRET = account["cloud_client_secret"]
    access_token = get_authorization_token(stack, CLIENT_ID, CLIENT_SECRET)
    #The headers for the DELETE request are:
    HEADERS= {
        'Authorization': 'Bearer ' + access_token,
        'User-Agent':'PostmanRuntime/7.32.2',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    PAYLOAD = {
         "deviceInfo": {
            "productNumber": model_number,
            "serialNumber": entity_id
        }
    }

    try:
        response = requests.delete(url=api_uri, headers=HEADERS, json=PAYLOAD, verify=False, proxies=PROXIES)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return None