from MobileApps.libs.flows.windows.jweb_value_store.home import Home
from MobileApps.libs.flows.windows.jweb_value_store.value_store import ValueStore
from MobileApps.libs.flows.windows.jweb_value_store.value_store_plugin import ValueStorePlugin
from MobileApps.libs.flows.windows.jweb.home import Home as WebletHome

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "weblet_home": WebletHome(driver),
                   "value_store": ValueStore(driver),
                   "value_store_plugin": ValueStorePlugin(driver)}
        
    def reset_application(self):
        self.driver.restart_app()
        self.fd["weblet_home"].select_webview_mode()
        self.fd["home"].select_weblet_tab_nav()

    def put_key_value_pair(self, key, value, get_result=True):
        self.fd["value_store_plugin"].send_text_to_set_put_keys(key)
        self.fd["value_store_plugin"].send_text_to_put_value(value)
        self.fd["value_store_plugin"].select_put_value_btn()
        if get_result:
            get_value_result = self.fd["value_store_plugin"].get_value_store_set_result()
            assert "result" in get_value_result, "no 'result' in return value. Returned Result: {}".format(self.fd["value_store_plugin"].get_value_store_set_result())
            return get_value_result["result"]
    
    def return_and_close_subscriber_alert_text(self):
        text = self.fd["value_store_plugin"].get_subscriber_alert_text()
        self.fd["value_store_plugin"].select_subscriber_alert_close_btn()
        return text