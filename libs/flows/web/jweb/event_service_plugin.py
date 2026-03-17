from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow
from selenium.webdriver.common.keys import Keys
import json

class EventServicePlugin(JwebFlow):
    flow_name = "event_service_plugin"

    def __init__(self, driver, context=None, url=None, window_name="main"):
        super(EventServicePlugin, self).__init__(driver, context=context, url=url, window_name=window_name)
        if self.driver.driver_info['platform'].lower() == "ios":
            ui_map = self.load_ui_map(system="IOS", project="smart", flow_name="shared_obj")
            self.driver.load_ui_map(self.project, self.flow_name, ui_map, append=True)
        
    def enter_create_subscriber_id_text(self, text):
        """
        from createSubscriber() tab, send text into the Subscriber Id textbox
        """
        self.driver.send_keys("create_subscriber_id_textbox", text)
    
    def enter_create_publisher_id_text(self, text):
        """
        from createPublisher() tab, send text into the Publisher Id textbox
        """
        if self.driver.driver_info['platform'].lower() == "ios":
            self.driver.selenium.js_clear_text("create_publisher_id_textbox")
            self.driver.send_keys("create_publisher_id_textbox", text)
            self.driver.switch_to_webview("NATIVE")
            self.driver.click("_shared_done")
        elif self.driver.driver_info['platform'].lower() == "android":                      
            self.driver.send_keys("create_publisher_id_textbox", text)
        else:
            self.driver.send_keys("subscribe_event_name_textbox", text)

    def select_create_subscriber_btn(self):
        """
        from createSubscriber() tab, select 'Create' button to create a new subscriber
        """
        self.driver.click("create_subscriber_btn")

    def select_create_publisher_btn(self):
        """
        from createPublisher() tab, select 'Create' button to create a new publisher
        """
        self.driver.click("create_publisher_btn")

    def select_first_subscriber(self):
        """
        from Subscribers Generated tab, select the first subscriber 
        """
        self.driver.click("first_generated_subscriber", index=0, delay=3)

    def select_first_publisher(self):
        """
        From the Publishers Generated tab, select the first publisher
        """
        self.driver.click("first_generated_publisher", delay=3)

    def verify_first_subscriber_is_present(self):
        """
        from Subscribers Generated tab, ensure that the generated subscriber 'subscriber0' is present
        """
        el = self.driver.wait_for_object("first_generated_subscriber", index=0, raise_e=False)
        return False if el is False else el.text == "subscriber0"

    def enter_subscribe_event_name_text(self, text):
        """
        after selecting subscriber, insert text into event name textbox
        """
        if self.driver.driver_info['platform'].lower() == "ios":
            self.driver.selenium.js_clear_text("subscribe_event_name_textbox")
            self.driver.send_keys("subscribe_event_name_textbox", text)
            self.driver.switch_to_webview("NATIVE")
            self.driver.click("_shared_done")
        else:
            self.driver.send_keys("subscribe_event_name_textbox", text)

    def enter_subscribe_publisher_id_text(self, text):
        """
        after selecting subscriber, insert text into publisher id textbox
        """
        self.driver.send_keys("subscribe_publisher_id_textbox", text)

    def enter_publisher_event_name_text(self, text):
        """
        after selecting publisher, insert text into event name textbox
        """
        if self.driver.driver_info['platform'].lower() == "ios":
            self.driver.switch_to_webview("NATIVE")
            self.driver.long_press("publisher_event_name_textbox")
            self.driver.send_keys("publisher_event_name_textbox", Keys.BACKSPACE)
            self.driver.send_keys("publisher_event_name_textbox", text)
            self.driver.click("_shared_done")
        self.driver.send_keys("publisher_event_name_textbox", text)

    def enter_publisher_event_data_text(self, text):
        """
        after selecting publisher, insert text into publisher id textbox
        """
        if self.driver.driver_info['platform'].lower() == "ios":
            self.driver.switch_to_webview("NATIVE")
            self.driver.click("publisher_event_data_textbox")
            self.driver.long_press("publisher_event_data_textbox")
            if not self.driver.wait_for_object("_shared_select_all_btn", raise_e=False, timeout=3):
                self.driver.click("_shared_done")
                self.driver.long_press("publisher_event_data_textbox")
            else:
                self.driver.click("_shared_select_all_btn")
            self.driver.send_keys("publisher_event_data_textbox", Keys.BACKSPACE)
            self.driver.send_keys("publisher_event_data_textbox", text)
            self.driver.click("_shared_done")
        else:
            self.driver.send_keys("publisher_event_data_textbox", text)

    def select_publish_btn(self):
        """
        after selecting publisher, select publish btn
        """
        self.driver.click("publish_btn")

    def select_subscribe_btn(self):
        """
        after selecting subscriber, select subscribe button
        """
        self.driver.click("subscribe_btn")

    def enter_unsubscribe_event_name_text(self, text):
        """
        after selecting subscriber, insert text into unsubscribe Event Name textbox 
        """
        self.driver.send_keys("unsubscribe_event_name_textbox", text)

    def enter_unsubscribe_publisher_id_text(self, text):
        """
        after selecting subscriber, insert text into unsubscribe Publisher Id textbox 
        """
        self.driver.send_keys("unsubscribe_publisher_id_textbox", text)

    def select_unsubscribe_btn(self):
        """
        after selecting subscriber, select unsubscribe button
        """
        self.driver.click("unsubscribe_btn")

    def get_subscription_generated_event_name_text(self, index=0, raise_e=False):
        """
        after selecting subscriber, and selecting subscribe btn, get generated event name text
        trims off "publisherID:" from returning text
        """
        event_name_result = self.driver.wait_for_object("subscription_generated_event_name", index=index, raise_e=raise_e)
        if raise_e is False and event_name_result is False: 
            return False 
        text = event_name_result.text
        return text[text.index(":")+2:]

    def get_subscription_generated_publisher_id_text(self, index=0, raise_e=True):
        """
        after selecting subscriber, and selecting subscribe btn, get generated publisher id text
        """
        publisher_id_result = self.driver.wait_for_object("subscription_generated_publisher_id", index=index, raise_e=raise_e)
        if raise_e is False and publisher_id_result is False: 
            return False 
        text = publisher_id_result.text
        return text[text.index(":")+2:]

    def get_toast_text(self):
        """
        get text from pop up toast notification
        """
        return self.driver.wait_for_object("toast_notification").text

    def select_delete_subscriber_btn(self):
        """
         from Subscribers Generated tab, select delete subscriber button 
        """
        self.driver.click("delete_subscriber_btn")

    def select_delete_publisher_btn(self):
        """
         from Publisher Generated tab, select delete publisher button 
        """
        self.driver.click("delete_publisher_btn")

    def select_persistent_drop_down_menu(self):
        """
        Select persistent id drop down menu in event service plugin
        """
        self.driver.click("persistent_dropdown")

    def select_persistent_option_from_menu(self, option):
        """
        After opening Persisence id drop down menu, select any one option true or false
        """
        option.lower()
        if option == "true":
            self.driver.click("persistent_true")
        elif option == "false":
            self.driver.click("persistent_false")
        else:
            raise NameError("persistent option:{} not present from persitent drop down menu".format(option))
        
    def select_pause_btn(self):
        """
        after selecting subscriber, select the pause button
        """
        self.driver.click("pause_btn")

    def select_resume_btn(self):
        """
        after selecting subscriber, select the resume button
        """
        self.driver.click("resume_btn")

class IOSEventServicePlugin(EventServicePlugin):
    context = "NATIVE_APP"
    
    def native_select_existing_subscriber_from_list(self):
        """
        select the existing_subscriber from the list
        """
        self.driver.click("native_select_existing_subscribe")

    def native_select_pause_events_btn(self):
        """
        select subscriber and select pause events button
        """
        self.driver.click("native_pause_events_btn")

    def native_select_resume_events_btn(self):
        """
        select subscriber and select resume events button
        """
        self.driver.click("native_resume_events_btn")
    
    def native_select_subscriptions_btn(self):
        """
        after selecting subscriber, select subscriptions button
        """
        self.driver.click("native_subscriptions_btn")

    def native_select_publisher(self, publisher_name):
        """
        after selecting Publisher tab, select publisher from the list
        """
        self.driver.click("native_select_publisher", format_specifier=[publisher_name])

    def native_select_publish_btn(self):
        """
        after selecting publisher tab, select publish button
        """
        self.driver.click("native_publish_btn")
    
    def native_select_add_subscription_btn(self):
        """
        after selecting subscription, select add button to add new subscription
        """
        self.driver.click("native_select_add_subscriptions_btn")

    def native_select_add_publisher_btn(self):
        """
        after selecting publisher tab, select add button to add new publisher
        """
        self.driver.click("native_select_add_publisher_btn")

    def native_select_subscription_btn(self):
        """
        after selecting add subscription, select subscription button
        """
        self.driver.click("native_select_subscriptions_btn")

    def native_enter_new_publisher_id_text(self, text):
        """
        Enter text into publisher id textbox
        """
        self.driver.send_keys("native_enter_new_publisher_id_textbox", text)

    def native_enter_new_event_name_text(self, text):
        """
        Enter text into publisher id textbox
        """
        self.driver.send_keys("native_enter_new_event_name_textbox", text)

    def native_click_create_publisher_btn(self):
        """
        after adding new publisher details, click on create publisher button
        """
        self.driver.click("native_create_publisher_btn")

    def native_persist_events_toggle(self):
        """
        after selecting subscriber, select persist events toggle
        """
        self.driver.click("native_persist_events_toggle")

    def native_select_add_new_subscriber_btn(self):
        """
        after selecting subscriber tab, select add button to add new subscriber
        """
        self.driver.click("native_select_add_new_subscriber_btn")

    def native_select_create_subscriber_btn(self):
        """
        after selecting subscriber tab, clicking on the add new subscriber button and click on create subscriber button from pop up modal
        """
        self.driver.click("native_create_subscriber_btn")
    
    def native_is_persist_yes_subscriber(self):
        """
        click on create subscriber button from pop up modal, click Yes in persist events pop up
        """
        self.driver.click("native_is_persist_yes_subscriber")

    def native_select_newly_created_subscriber(self):
        """
        click on create subscriber button from pop up modal, click on the newly created subscriber
        """
        self.driver.click("native_select_newly_created_subscriber")

    def native_verify_first_publisher_id(self, publisher_name, raise_e=False):
        """
        Click on Events tab and verify the logs
        """
        self.driver.wait_for_object("native_verify_first_publisher_id", format_specifier=[publisher_name], raise_e=raise_e)       

    def native_verify_second_publisher_id(self, publisher_name):
        """
        Click on Events tab and verify the logs
        """
        self.driver.wait_for_object("native_verify_second_publisher_id", format_specifier=[publisher_name])       

    def native_verify_third_publisher_id(self, publisher_name):
        """
        Click on Events tab and verify the logs
        """
        self.driver.wait_for_object("native_verify_third_publisher_id", format_specifier=[publisher_name])

    def native_verify_event_data_table_entry(self):
        """
        Click on Events tab and verify the logs
        """
        return self.driver.wait_for_object("native_verify_event_data_table", raise_e=False)

    def native_back_btn_to_subscriber(self):
        """
        Click on Events tab and verify the logs
        """
        self.driver.click("native_back_btn_navigate_back_to_subscriber")

    def native_is_persist_no_subscriber(self):
        """
        click on create subscriber button from pop up modal, click No in persist events pop up
        """
        self.driver.click("native_is_persist_no_subscriber")

    def native_verify_subscription_status(self, status):
        """
        Click on the subscriptions and verify the status
        """
        self.driver.wait_for_object("native_subscription_status", format_specifier=[status])
    
    def native_select_subscription_callback_btn(self):
        """
        Click on the subscription add button and select callback button
        """
        self.driver.wait_for_object("native_subscription_callback_btn")

    def native_verify_subscription_entries(self, publisher_name, raise_e=False):
        """
        Click on subscriptions and verify the subscription entry
        """
        self.driver.wait_for_object("native_verify_first_publisher_id", format_specifier=[publisher_name], raise_e=raise_e)

    def native_subscription_error_pop_up_msg(self):
        """
        Verify the error message pop up
        """
        return self.driver.wait_for_object("native_subscription_error_pop_up_text").text