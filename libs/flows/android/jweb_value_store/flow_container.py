from time import sleep

from MobileApps.libs.flows.android.jweb_value_store.home import Home
from MobileApps.libs.flows.android.jweb_value_store.native import Native
from MobileApps.libs.flows.android.jweb_value_store.value_store_dev_settings import ValueStoreDevSettings
from MobileApps.libs.flows.web.jweb.value_store import ValueStorePlugin
from MobileApps.resources.const.android.const import *
from MobileApps.resources.const.web.const import *

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "native": Native(driver),\
                   "value_store_dev_settings": ValueStoreDevSettings(driver),\
                   "value_store_plugin": ValueStorePlugin(driver, context={"url":WEBVIEW_URL.JWEB})}

    @property
    def flow(self):
        return self.fd

# *********************************************************************************
#                                ACTION FLOWS                                     *
# *********************************************************************************

    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch app
        """
        self.driver.press_key_home()
        self.driver.start_activity(PACKAGE.JWEB_VALUE_STORE, LAUNCH_ACTIVITY.JWEB_VALUE_STORE)
        sleep(2)

    def put_key_value_pair(self, key, value, get_result=True):
        self.fd["value_store_plugin"].send_text_to_set_put_keys(key)
        self.fd["value_store_plugin"].send_text_to_put_value(value)
        self.fd["value_store_plugin"].select_put_value_btn()
        if get_result:
            result_json = self.fd["value_store_plugin"].get_value_store_set_result()
            return result_json if "result" not in result_json else result_json["result"]

    def return_and_close_subscriber_alert_text(self):
        text = self.fd["value_store_plugin"].get_subscriber_alert_text()
        self.fd["value_store_plugin"].select_subscriber_alert_close_btn()
        return text