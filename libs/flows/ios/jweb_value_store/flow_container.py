from MobileApps.libs.flows.ios.jweb_value_store.home import Home
from MobileApps.libs.flows.ios.jweb_value_store.native import Native
from MobileApps.libs.flows.web.jweb.value_store import IOSValueStorePlugin
from MobileApps.resources.const.web.const import *


class FlowContainer(object):
    def __init__(self, driver, load_app_strings=False):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "native": Native(driver),
                   "value_store_plugin": IOSValueStorePlugin(driver, context={"url":WEBVIEW_URL.JWEB})}

    @property
    def flow(self):
        return self.fd
    
    def put_key_value_pair(self, key, value):
        self.fd["value_store_plugin"].send_text_to_set_put_keys(key)
        self.fd["value_store_plugin"].send_text_to_put_value(value)
        self.fd["value_store_plugin"].select_put_value_btn()
        assert "result" in self.fd["value_store_plugin"].get_value_store_set_result(), "no 'result' in return value. Returned Result: {}".format(self.fd["value_store_plugin"].get_value_store_set_result())
        return self.fd["value_store_plugin"].get_value_store_set_result()["result"]
    
    def return_and_close_subscriber_alert_text(self):
        text = self.fd["value_store_plugin"].get_subscriber_alert_text()
        self.fd["value_store_plugin"].select_subscriber_alert_close_btn()
        return text