import json
from time import time

from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow
from MobileApps.resources.const.web import const as w_const

class ValueStorePlugin(JwebFlow):
    flow_name = "value_store_plugin"

    def select_set_subscriber_btn(self):
        """
        In Set Value Store Event Subscriber tab, click on Set Subscriber button
        """
        self.driver.click("set_subscriber_btn")

    def verify_subscriber_result(self, text):
        """
        In Set Value Store Event Subscriber tab, Verify text in Subscriber Result
        :param text: text to verify
        """
        return self.driver.wait_for_object("subscriber_text_result", format_specifier=[text], timeout=2, raise_e=False)
    
    def get_subscriber_alert_text(self, raise_e=True):
        """
        From Subscriber Alert popup, return text result
        """
        return self.driver.get_attribute("subscriber_popup_alert", "text", timeout=3, raise_e=raise_e)
    
    def select_subscriber_alert_close_btn(self, raise_e=False):
        """
        From Subscriber Alert popup, click on Close button
        """
        self.driver.click("subscriber_close_alert_btn", raise_e=raise_e)

    def send_text_to_get_value_keys(self, text):
        """
        In ValueStore.get(), send text to Keys input field
        :param text: text to send
        """
        if self.driver.get_attribute("get_value_keys_textbox", "value") != "":
            self.clear_textbox("get_value_keys_textbox")
        self.driver.send_keys("get_value_keys_textbox", text)

    def select_get_value_btn(self):
        """
        In ValueStore.get(), click on Get Value button
        """
        self.driver.click("get_value_btn", change_check={"wait_obj": "get_value_result"})

    def get_value_store_get_result(self):
        """
        In ValueStore.get(), return result text
        :return: ValueStore.get() result
        """
        return json.loads(self.driver.get_attribute("get_value_result", "text"))

    def send_text_to_set_put_keys(self, text):
        """
        In ValueStore.set(), send text to Keys input field
        :param text: text to send
        """
        if self.driver.get_attribute("put_keys_textbox", "value") != "":
            self.clear_textbox("put_keys_textbox")
        self.driver.send_keys("put_keys_textbox", text)

    def send_text_to_put_value(self, text):
        """
        In ValueStore.set(), send text to Value input field
        :param text: text to send
        """
        if self.driver.get_attribute("put_values_textbox", "value") != "":
            self.clear_textbox("put_values_textbox")
        self.driver.send_keys("put_values_textbox", text)

    def select_put_value_btn(self):
        """
        In ValueStore.set(), click on Set Value button
        """
        self.driver.click("put_value_btn", change_check={"wait_obj": "put_value_result"})

    def get_value_store_set_result(self):
        """
        In ValueStore.set(), return result text
        :return: ValueStore.set() result
        """
        return json.loads(self.driver.get_attribute("put_value_result", "text"))

    def send_text_to_remove_value(self, text):
        """
        In ValueStore.remove(), send text to Keys input field
        :param text: text to send
        """
        if self.driver.get_attribute("remove_value_textbox", "value") != "":
            self.clear_textbox("remove_value_textbox")
        self.driver.send_keys("remove_value_textbox", text)

    def select_remove_btn(self):
        """
        In ValueStore.remove(), click on Remove button
        """
        self.driver.click("remove_value_btn", change_check={"wait_obj": "remove_value_result"})

    def get_remove_value_result(self):
        """
        In ValueStore.remove(), return result text
        :return: ValueStore.remove() result
        """
        return json.loads(self.driver.get_attribute("remove_value_result", "text"))

    def verify_weblet_view_buttons(self):
        """
        Verify the Get, Set, Remove buttons are present in the Value Store Weblet
        """
        self.driver.wait_for_object("get_value_btn")
        self.driver.wait_for_object("put_value_btn")
        self.driver.wait_for_object("remove_value_btn")

    def clear_textbox(self, object_id):
        self.driver.selenium.js_clear_text(object_id)

class IOSValueStorePlugin(ValueStorePlugin):
    context = "NATIVE_APP"

    def clear_textbox(self, object_id):
        """
        Clear any textbox found in the Value Store Plugin
        """
        self.driver.switch_to_webview(w_const.WEBVIEW_URL.JWEB)
        self.driver.click(object_id)
        self.driver.switch_to_webview()
        self.driver.click(object_id)
        self.driver.long_press(object_id)
        timeout = 45 + time()
        while self.driver.get_attribute(object_id, "text") != "" and time() < timeout:
            if object_id == "put_values_textbox":
                if not self.driver.wait_for_object("select_all_btn", timeout=1, raise_e=False):
                    if "15" in self.driver.driver_info['platformVersion']:
                        self.driver.click("more_options", timeout=1, raise_e=False)
                        self.driver.long_press(object_id)
                    else:
                        self.driver.click("done_btn", timeout=1, raise_e=False)
                        self.driver.long_press(object_id)
                self.driver.click("select_all_btn", raise_e=False)
            if not self.driver.wait_for_object("delete_btn", timeout=1, raise_e=False):
                self.driver.long_press(object_id)
            self.driver.click("delete_btn")
            self.driver.click("done_btn")
