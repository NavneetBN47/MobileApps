import json
import logging
from time import sleep  

from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow
from MobileApps.resources.const.web import const as w_const

class ValueStorePlugin(JwebFlow):
    flow_name = "value_store_plugin"

    def swipe_to_object(self, obj, direction="down"):
        """
        Within Data Collection Plugin, swipe to an object given a direction
        """
        for _ in range(10):
            if not self.driver.wait_for_object(obj, raise_e=False, timeout=1):
                self.driver.swipe(anchor_element="value_store_header", direction=direction)
            else:
                return True
        else:
            return False

    def select_set_subscriber_btn(self):
        """
        In Set Value Store Event Subscriber tab, click on Set Subscriber button
        """
        self.swipe_to_object("set_subscriber_btn", direction="up")
        self.driver.click("set_subscriber_btn")

    def verify_subscriber_result(self, text):
        """
        In Set Value Store Event Subscriber tab, Verify text in Subscriber Result
        :param text: text to verify
        """
        return self.driver.wait_for_object("subscriber_text_result", displayed=False, format_specifier=[text], timeout=2, raise_e=False)
    
    def get_subscriber_alert_text(self, raise_e=True):
        """
        From Subscriber Alert popup, return text result
        """
        return self.driver.get_attribute("subscriber_popup_alert", "text", displayed=False, timeout=3, raise_e=raise_e)
    
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
        self.driver.clear_text("get_value_keys_textbox")
        self.driver.send_keys("get_value_keys_textbox", text)

    def select_get_value_btn(self):
        """
        In ValueStore.get(), click on Get Value button
        """
        self.swipe_to_object("get_value_btn", direction="up")
        self.driver.click("get_value_btn", change_check={"wait_obj": "get_value_result", "displayed": False})

    def get_value_store_get_result(self, delay=3):
        """
        In ValueStore.get(), return result text
        :return: ValueStore.get() result
        """
        sleep(delay)
        return json.loads(self.driver.get_attribute("get_value_result", "Name", displayed=False))

    def send_text_to_set_put_keys(self, text):
        """
        In ValueStore.set(), send text to Keys input field
        :param text: text to send
        """
        self.swipe_to_object("put_keys_textbox")
        self.driver.clear_text("put_keys_textbox")
        self.driver.send_keys("put_keys_textbox", text)

    def send_text_to_put_value(self, text):
        """
        In ValueStore.set(), send text to Value input field
        :param text: text to send
        """
        self.driver.clear_text("put_values_textbox")
        self.driver.send_keys("put_values_textbox", text)

    def select_put_value_btn(self):
        """
        In ValueStore.set(), click on Set Value button
        """
        self.driver.click("put_value_btn", change_check={"wait_obj": "put_value_result", "displayed": False})

    def get_value_store_set_result(self, delay=3):
        """
        In ValueStore.set(), return result text
        :return: ValueStore.set() result
        """
        sleep(delay)
        self.driver.wait_for_object("put_value_result", displayed=False)
        return json.loads(self.driver.get_attribute("put_value_result", "Name", displayed=False))

    def send_text_to_remove_value(self, text):
        """
        In ValueStore.remove(), send text to Keys input field
        :param text: text to send
        """
        self.driver.clear_text("remove_value_textbox")
        self.driver.send_keys("remove_value_textbox", text)

    def select_remove_btn(self):
        """
        In ValueStore.remove(), click on Remove button
        """
        self.swipe_to_object("remove_value_btn")
        self.driver.click("remove_value_btn", change_check={"wait_obj": "remove_value_result", "displayed": False})

    def get_remove_value_result(self, delay=3):
        """
        In ValueStore.remove(), return result text
        :return: ValueStore.remove() result
        """
        sleep(delay)
        return json.loads(self.driver.get_attribute("remove_value_result", "Name", displayed=False))

    def verify_weblet_view_buttons(self):
        """
        Verify the Get, Set, Remove buttons are present in the Value Store Weblet
        """
        self.swipe_to_object("get_value_btn")
        self.driver.wait_for_object("get_value_btn")
        self.swipe_to_object("put_value_btn")
        self.driver.wait_for_object("put_value_btn")
        self.swipe_to_object("remove_value_btn")
        self.driver.wait_for_object("remove_value_btn")

    def clear_textbox(self, object_id):
        self.driver.clear_text(object_id)
