class HPCONNECT():
    STAGE1_URL = "https://hpc-stage1.hpconnectedstage.com/us/en"
    PIE_URL = "https://hpc-pie1.hpconnectedpie.com/us/en"

class TEST_DATA():
    #Used as relative paths from MobileApps, these are not absolute paths
    GMAIL_TOKEN_PATH = "/qama/framework/data/gmail.token"
    JWEB_ACCOUNT = "/resources/test_data/jweb/results.json"
    DOC_PROVIDER = "/resources/test_data/jweb/doc_provider.json"
    SERVICE_ROUTING = "/resources/test_data/jweb/service_routing.json"
    HPID_ACCOUNT = "/resources/test_data/hpid/account.json"
    OWS_DEFAULT_VALUES = "resources/test_data/ows/default_values.json"
    PORTAL_OOBE_LOCALES = "/resources/test_data/poobe/portal_oobe_locales.json"
    ISO_LANGUAGE_LIST = ['aa', 'ab', 'af', 'ak', 'sq', 'am', 'ar', 'an', 'hy', 'as', 'av', 'ae', 'ay', 'az', 'ba', 'bm', 'eu', 'be', 'bn',
                     'bh', 'bi', 'bo', 'bs', 'br', 'bg', 'my', 'ca', 'cs', 'ch', 'ce', 'zh', 'cu', 'cv', 'kw', 'co', 'cr', 'cy', 'cs',
                     'da', 'de', 'dv', 'nl', 'dz', 'el', 'en', 'eo', 'et', 'eu', 'ee', 'fo', 'fa', 'fj', 'fi', 'fr', 'fy', 'ff', 'ga',
                     'de', 'gd', 'ga', 'gl', 'gv', 'el', 'gn', 'gu', 'ht', 'ha', 'he', 'hz', 'hi', 'ho', 'hr', 'hu', 'hy', 'ig', 'is',
                     'io', 'ii', 'iu', 'ie', 'ia', 'id', 'ik', 'is', 'it', 'jv', 'ja', 'kl', 'kn', 'ks', 'ka', 'kr', 'kk', 'km', 'ki',
                     'rw', 'ky', 'kv', 'kg', 'ko', 'kj', 'ku', 'lo', 'la', 'lv', 'li', 'ln', 'lt', 'lb', 'lu', 'lg', 'mk', 'mh', 'ml',
                     'mi', 'mr', 'ms', 'mi', 'mk', 'mg', 'mt', 'mn', 'mi', 'ms', 'my', 'na', 'nv', 'nr', 'nd', 'ng', 'ne', 'nl', 'nn',
                     'no', 'oc', 'oj', 'or', 'om', 'os', 'pa', 'fa', 'pi', 'pl', 'pt', 'ps', 'qu', 'rm', 'ro', 'ro', 'rn', 'ru', 'sg', 
                     'sa', 'si', 'sk', 'sk', 'sl', 'se', 'sm', 'sn', 'sd', 'so', 'st', 'es', 'sq', 'sc', 'sr', 'ss', 'su', 'sw', 'sv', 
                     'ty', 'ta', 'tt', 'te', 'tg', 'tl', 'th', 'bo', 'ti', 'to', 'tn', 'ts', 'tk', 'tr', 'tw', 'ug', 'uk', 'ur', 'uz', 
                     've', 'vi', 'vo', 'cy', 'wa', 'wo', 'xh', 'yi', 'yo', 'za', 'zh', 'zu']

def get_hpid_webview_url(stack):
    webview_dict = {("pie", "stage"): "login3.stg.cd.id.hp.com", ("production"): "login3.id.hp.com"}
    return next(value for key, value in webview_dict.items() if stack in key)

def get_smart_welcome_webview_url(platform):
    webview_dict = {"ios": "in-app/ios", "android": "login3.id.hp.com"}
    return next(value for key, value in webview_dict.items() if platform.lower() in key)

class WEBVIEW_URL():
    HPID = get_hpid_webview_url
    SMART_WELCOME = get_smart_welcome_webview_url
    LINK_TOU = "tou"
    REDACTION = "redaction-react-webapp"
    SCRIBBLE = "scribble"
    JWEB = 'jweb-reference-weblet/latest/index.html'
    SOFTFAX_OFFER = "in-app/mobile-fax"
    SOFTFAX = "sws"
    VALUE_PROP = "ucde/account-prop"
    TEXT_EXTRACT = "text-react-webapp"
    CEC = "/cec.hpsmart"
    JWEB_SECURITY = 'https://chrisgeohringhp.github.io/'
    JWEB_SERVICE_ROUTING = 'https://static.hpsmart.com/jarvis/jweb-reference-weblet/latest/index.html#/service_routing'
    JWEB_DATA_COLLECTION = 'index.html#/data_collection'
    DEDICATED_SUPPLY_LEVEL = 'supplystatus'
    PRINTABLES = "/printables"

class WEBVIEW_NAME():
    JWEB_SERVICE_ROUTING = 'WEBVIEW_com.hp.jarvis.serviceroutingexample'

class PROXY():
    ECP = "web-proxy.austin.hpicorp.net:8080"
    SMB = "web-proxy.austin.hpicorp.net:8080"
    OWS = "web-proxy.corp.hp.com:8080"
    WEX = "web-proxy.austin.hpicorp.net:8080"

class WEX_URLS():
    """Workforce Experience base URLs for different environments"""
    PIE = "https://usdevms-workforce.hppipeline.com"
    STAGE = "https://usstagingms.workforceexperience.hp.com"
    PRODUCTION = "https://workforceexperience.hp.com"
    TEST = "https://ustestms.workforceexperience.hp.com"

class SIM_API_URLS():
    # Base URL for simulator
    SIM_BASE_URL = "https://g2sim.wpp.api.hp.com"
    
    # Simulator printer endpoints
    SIMULATOR_PRINTERS = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers"
    SIMULATOR_PRINTERS_REGISTER = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers/{}/register"
    SIMULATOR_PRINTERS_CLAIM_POSTCARD = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers/{}/claimpostcard"
    SIMULATOR_PRINTERS_FINGERPRINT = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers/{}/devicefingerprint"
    SIMULATOR_PRINTERS_REMOVE = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers/{}/remove"
    TOOLS_PRINTER_CODE = "https://g2sim.wpp.api.hp.com/wpp/tools/printercode"
    
    # Device Auth Grant API endpoints
    DAG_DEVICE_CODE_STAGE = "https://device-auth-grant-api-stratus.api.stg-thor-ue1.hpip-internal.com/deviceauthgrant/v1/devicecode"
    DAG_DEVICE_CODE_PIE = "https://device-auth-grant-api-stratus.api.itg-thor-ue1.hpip-internal.com/deviceauthgrant/v1/devicecode"
    DAG_TOKEN_STAGE = "https://device-auth-grant-api-stratus.api.stg-thor-ue1.hpip-internal.com/deviceauthgrant/v1/token"
    DAG_TOKEN_PIE = "https://device-auth-grant-api-stratus.api.itg-thor-ue1.hpip-internal.com/deviceauthgrant/v1/token"
    
    # Client IDs
    DAG_CLIENT_ID_STAGE = "1qTnmuPyFJTfgmQrPAkzgjGtX4ba1TKW"
    DAG_CLIENT_ID_PIE = "RULy59vR3mT3Ml5GkSpg4JZpKlSZCnMS"
    
    # User management service
    ACCOUNT_DETAILS_PATTERN = "https://{}-us1.api.ws-hp.com/v3/usermgtsvc/userwithtenantdetails/me"
    
    # Device claim service
    CLAIM_PRINTER_PATTERN = "https://deviceclaim.{}.avatar.ext.hp.com/dcs-api/v1/ownerships"

def get_connector_deviceconfigs_v1_uri(stack):
        deviceconfigs_dict = {
            "pie": "https://connector-device-settings-manager-stratus.api.itg-thor-ue1.hpip-internal.com/connector/v1/deviceconfigs",
            "stage": "https://connector-device-settings-manager-stratus.api.stg-thor-ue1.hpip-internal.com/connector/v1/deviceconfigs",
            "production": "https://connector-device-settings-manager-stratus.api.prod-thor-ue1.hpip-internal.com/connector/v1/deviceconfigs",
            "test": "https://connector-device-settings-manager-stratus.api.stg-thor-ue1.hpip-internal.com/connector/v1/deviceconfigs"
        }
        return deviceconfigs_dict.get(stack, "Stack not found")  # Default response if stack doesn't exist

def get_connector_deviceconfigs_v2_uri(stack):
        deviceconfigs_dict = {
            "pie": "https://connector-device-settings-manager-stratus.api.itg-thor-ue1.hpip-internal.com/connector/v2/deviceconfigs",
            "stage": "https://connector-device-settings-manager-stratus.api.stg-thor-ue1.hpip-internal.com/connector/v2/deviceconfigs",
            "production": "https://connector-device-settings-manager-stratus.api.prod-thor-ue1.hpip-internal.com/connector/v2/deviceconfigs",
            "test": "https://connector-device-settings-manager-stratus.api.stg-thor-ue1.hpip-internal.com/connector/v2/deviceconfigs"

        }
        return deviceconfigs_dict.get(stack, "Stack not found")

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