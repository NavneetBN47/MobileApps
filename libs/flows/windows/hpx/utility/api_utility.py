# coding: utf-8
import requests
import uuid
import logging
import json
import base64
from io import BytesIO
from time import sleep
from urllib.parse import urlparse, parse_qs
from MobileApps.libs.flows.windows.hpx.utility import utlitiy_misc
# from APILib.request_util import ApiRequest, ApiResponse

PROXIES = {
    'http': 'http://web-proxy.corp.hp.com:8080',
    'https': 'http://web-proxy.corp.hp.com:8080'
}

class APIUtility(object):

    RESPONSE_TIMEOUT = 120
    encoding = "utf-8"

    def __init__(self, build_type):
        stack = utlitiy_misc.load_stack_info(build_type)
        self.test_stack = stack["stack"]
        self.host = stack["host"]
        self.user= stack["user"]
        self.pwd = stack["pwd"]
        self.key = stack["x-api-key"]
        self.authorization = None

    def get_access_token(self, username, password):
        s = requests.session()
        s.cookies.clear()
        base_url = '{}/oauth2/v1/auth?client_id={}&redirect_uri={}&response_type=code&state={}&config_id={}&code_challenge=8u7q-9VMFlxA-IAquRD_RQiGNp2Q6sZGLJpWwZGU7-0&code_challenge_method=S256'.format(
                            self.host['oauth_host'], 
                            self.host['client_id'], 
                            self.host['redirect_uri'], 
                            str(uuid.uuid4()), 
                            self.host['config_id'])
        resp_body = s.get(base_url,
                            allow_redirects=False,
                            verify=False,                           
                            proxies=PROXIES)
        if resp_body.status_code != 302:
            raise Exception('Get hpid login page - Failed: {}'.format(resp_body.status_code))

        resp_body = s.get(resp_body.headers['location'],
                                allow_redirects=False,
                                verify=False,
                                proxies=PROXIES)

        if resp_body.status_code != 302:
            raise Exception('Get hpid login page - Failed: {}'.format(resp_body.status_code))

        url_parse = urlparse(resp_body.headers['location'])
        flow = parse_qs(url_parse.query)['flow']
        hpid_env = flow[0].split('/directory')[1]
        # create_session_flow = flow

        payload = {"flow": flow[0]}
        resp_body = s.post('https://ui-backend{}/bff/v1/auth/session'.format(hpid_env), 
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(payload),
                    verify=False, 
                    proxies=PROXIES)
        if resp_body.status_code != 201:
            raise Exception('Get hpid login page - Failed: {}'.format(resp_body.status_code))      

        region_endpoint_url = resp_body.json()['regionEndpointUrl']
        csrf_token = resp_body.json()['csrfToken']
        cookies = resp_body.cookies.get_dict()
        payload = {"username":"{}@hpid".format(username), "password":password}
        resp_body = s.post('{}/session/username-password'.format(region_endpoint_url), 
                    headers={'csrf-token':csrf_token, 'Content-Type': 'application/json'},
                    data=json.dumps(payload),
                    cookies=cookies,
                    verify=False, 
                    proxies=PROXIES)
        if resp_body.status_code != 200:
            raise Exception('Get hpid login page - Failed: {}'.format(resp_body.status_code))   

        url_parse = urlparse(resp_body.json()['nextUrl'])
        code = parse_qs(url_parse.query)['code'][0]
        state = parse_qs(url_parse.query)['state'][0]

        resp_body = s.get('{}/oauth2/v1/callback?code={}&state={}'.format(self.host['oauth_host'], code, state),
                                allow_redirects=False,
                                verify=False, 
                                proxies=PROXIES)
        if resp_body.status_code != 303:
            raise Exception('Get hpid login page - Failed: {}'.format(resp_body.status_code)) 
   
        url_parse = urlparse(resp_body.headers['location'])
        code = parse_qs(url_parse.query)['code']
        payload='grant_type=authorization_code&code={}&code_verifier=Qnm0N8AKjp8RWBSwtPsUipg7wpWKzEbB9nr5mrWnfQzK5wgPtT7P6e2ajdZ7ATljrw0nN-BA_zQ7DzR0OB_sLOdPmFYDhTt5L-MRMa3jEtrX1Sj4h030mxuNps80WRpm&redirect_uri={}'.format(code[0], self.host['redirect_uri'])
        resp_body=s.post('{}/oauth2/v1/token'.format(self.host['oauth_host']),
                                headers={'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic ZmQ3MjQ2MjYtZTllMS00MmJkLThmZWUtMjQ4ZjA2ZGMyOTFmOg=='},
                                data=payload,
                                verify=False,
                                proxies=PROXIES)
        if resp_body.status_code != 200:
            raise Exception('Get hpid login page - Failed: {}'.format(resp_body.status_code)) 
        self.authorization = resp_body.json()["access_token"]
        return resp_body.json()['access_token']
    
    def get_user_token(self, access_code):
        finger_print = base64.b64encode('{}:{}'.format(self.user, self.pwd).encode('utf-8')).decode('utf-8')
        payload = 'code={}&grant_type=authorization_code&redirect_uri={}'.format(access_code, self.host['redirect'])       
        headers = { 'Content-Type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'Basic {}'.format(finger_print), 
                    'x-api-key': self.key}

        resp_body = requests.post('{}/token'.format(self.host['coptor']), 
                    headers=headers, 
                    data=payload, 
                    verify=False, 
                    proxies=PROXIES)

        if resp_body.status_code != 200:
            logging.info("Failed: {} Retrying after 10s".format(resp_body.status_code))
            sleep(10)
            resp_body = requests.post(self.host['coptor'], headers=headers, data=payload, verify=False)
            if resp_body.status_code != 200:
                time_delay(resp_body.status_code)
                raise Exception('Paring code (DAG) - Failed: {}_{}'.format(resp_body.status_code, resp_body.text))

        token = resp_body.json()
        logging.debug("Pairing code (DAG) - Success")
    
        return token

    def post_device_verify(self):
        base_url = '{}/devices/verify'.format(self.host['methome'])
        payload = {"Locale":"en-US","SerialNumber":"8CC74200BZ","ProductNumber":""}
        headers = {'Content-Type': 'application/json', 
                    'x-api-key': self.key}

        resp_body = requests.post(base_url, 
                headers=headers, 
                data=json.dumps(payload), 
                verify=False, 
                proxies=PROXIES)

        if resp_body.status_code != 200:
            logging.info("Failed: {} Retrying after 10s".format(resp_body.status_code))
            sleep(10)
            resp_body = requests.post(base_url, headers=headers, data=payload, verify=False)
            if resp_body.status_code != 200:
                time_delay(resp_body.status_code)
                raise Exception('Paring code (DAG) - Failed: {}_{}'.format(resp_body.status_code, resp_body.text))

        token = resp_body.json()
        logging.debug("Pairing code (DAG) - Success")
    
        return token
    
    def post_warranty(self):
        base_uri = '{}/devices/warranty/v3'.format(self.host['methome'])
        payload = {"ClientId":"hpsa9","Devices":{"SerialNumber":"8CC7361RFR","Country":"US","ProductNumber":"Z5N05AA"}}
        headers = {'Content-Type': 'application/json', 
                    'x-api-key': self.key}
    
        resp_body = requests.post(base_uri, 
            headers=headers, 
            data=json.dumps(payload), 
            verify=False, 
            proxies=PROXIES)

        if resp_body.status_code != 200:
            logging.info("Failed: {} Retrying after 10s".format(resp_body.status_code))
            sleep(10)
            resp_body = requests.post(base_uri, headers=headers, data=payload, verify=False)
            if resp_body.status_code != 200:
                time_delay(resp_body.status_code)
                raise Exception('Paring code (DAG) - Failed: {}_{}'.format(resp_body.status_code, resp_body.text))

        token = resp_body.json()
        logging.debug("Pairing code (DAG) - Success")
    
        return resp_body

    def post_warranty_confirm(self):
        base_uri = '{}/devices/warranty/confirm'.format(self.host['methome'])
        payload = {"ClientId":"hpsa9","Devices":{"SerialNumber":"8CC7361RFR","Country":"US","ProductNumber":"Z5N05AA"}}
        headers = {'Content-Type': 'application/json', 
                    'x-api-key': self.key}
    
        resp_body = requests.post(base_uri, 
            headers=headers, 
            data=json.dumps(payload), 
            verify=False, 
            proxies=PROXIES)

        if resp_body.status_code != 200:
            logging.info("Failed: {} Retrying after 10s".format(resp_body.status_code))
            sleep(10)
            resp_body = requests.post(base_uri, headers=headers, data=payload, verify=False)
            if resp_body.status_code != 200:
                time_delay(resp_body.status_code)
                raise Exception('Paring code (DAG) - Failed: {}_{}'.format(resp_body.status_code, resp_body.text))

        token = resp_body.json()
        logging.debug("Pairing code (DAG) - Success")
    
        return resp_body
    
    def post_device_unregister(self, deviceId):
        base_uri = '{}/devices/{}?unregister=ture'.format(self.host['methome'], deviceId)
        headers = {'Content-Type': 'application/json', 
                    'x-api-key': self.key, 
                    'Authorization': "bearer " + self.authorization}

        resp_body = requests.delete(base_uri, 
                                    headers=headers,
                                    timeout=self.RESPONSE_TIMEOUT)
        logging.info("status_code={}".format(resp_body.status_code))
        if resp_body.status_code != 200:
            logging.info("Failed: {} Retrying after 10s".format(resp_body.status_code))
            sleep(10)

        resp_text = resp_body.json()
        logging.info("resp_text={}".format(resp_text))
        logging.debug("Pairing code (DAG) - Success")  

    def post_device_register(self, sn, pn):
        base_uri = '{}/devices/register'.format(self.host['methome'])
        payload = {"SerialNumber":"{}".format(sn),"ProductNumber":"{}".format(pn),"NickName":"HPX support auto","UUID":"253459e0-2c17-4cdb-963a-9a9f3aad28a9"}
        headers = {'Content-Type': 'application/json', 
                    'x-api-key': self.key, 
                    'Authorization': "bearer " + self.authorization}

        resp_body = requests.post(base_uri, 
            headers=headers, 
            data=json.dumps(payload), 
            verify=False, 
            proxies=PROXIES)

        if resp_body.status_code != 200:
            logging.info("Failed: {} Retrying after 10s".format(resp_body.status_code))
            sleep(10)
            resp_body = requests.post(base_uri, headers=headers, data=payload, verify=False)
            if resp_body.status_code != 200:
                time_delay(resp_body.status_code)
                raise Exception('Paring code (DAG) - Failed: {}_{}'.format(resp_body.status_code, resp_body.text))

        token = resp_body.json()
        logging.debug("Pairing code (DAG) - Success")
    
        return  resp_body.json()['DeviceId']

    def post_get_work_hours(self, product_big_series_oid, product_name_oid, product_series_oid, lang_country="en-US"):  
        base_uri = '{}/helpandsupport/ContactCenters/ContactCenters.svc/GetWorkingHours'.format(self.host['ccls'])
        payload = {"AppVersion":"25.42310.87","BoD":"","Country":lang_country.split("-")[1],"DateTime":"2023-03-06T04:26:29.536Z","Install":0,"Language":lang_country.split("-")[0],"Modifier":"","Offset":"+0800","PrevSeq":0,"product_big_series_oid":product_big_series_oid,"ProductLine":"AN","product_name_oid":product_name_oid,"ProductNumber":"158U3AA","product_series_oid":product_series_oid,"ResponseFmt":1,"ServiceType":"All","Slc":"","UseCase":"HPX05","UseRequestTime":0,"WarrantyLevel":"IW","MiscParm":""}
        headers = {'Content-Type': 'application/json'}
    
        resp_body = requests.post(base_uri, 
            headers=headers, 
            data=json.dumps(payload), 
            verify=False, 
            proxies=PROXIES)

        if resp_body.status_code != 200:
            logging.info("Failed: {} Retrying after 10s".format(resp_body.status_code))
            sleep(10)
            resp_body = requests.post(base_uri, headers=headers, data=payload, verify=False)
            if resp_body.status_code != 200:
                time_delay(resp_body.status_code)
                raise Exception('Paring code (DAG) - Failed: {}_{}'.format(resp_body.status_code, resp_body.text))
        
        logging.debug("Pairing code (DAG) - Success")
    
        return resp_body

def time_delay(status_code):
    # Time delay for server errors
    if status_code in [503,504,500]:
        sleep(180)
