from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow

class EventServicePlugin(JwebFlow):
    project = "jweb"
    flow_name = "event_service_plugin"

    def swipe_to_object(self, obj, format_specifier=[], direction="down"):
        """
        Within Event Service Plugin, swipe to an object given a direction
        """
        for _ in range(5):
            if not self.driver.wait_for_object(obj, raise_e=False, format_specifier=format_specifier, timeout=1):
                self.driver.swipe(anchor_element="event_service_header_title", direction=direction)
            else:
                return True
        else:
            return False

    def enter_create_subscriber_id_text(self, text):
        """
        from createSubscriber() tab, send text into the Subscriber Id textbox
        """
        self.driver.send_keys("create_subscriber_id_textbox", text)

    def enter_create_publisher_id_text(self, text):
        """
        from createPublisher() tab, send text into the Publisher Id textbox
        """
        self.driver.send_keys("create_publisher_id_textbox", text)

    def select_create_subscriber_btn(self):
        """
        from createSubscriber() tab, select 'Create' button to create a new subscriber
        """
        self.driver.click("create_subscriber_btn")

    def select_first_subscriber(self):
        """
        from Subscribers Generated tab, select the first subscriber 
        """
        if not self.driver.click("first_generated_subscriber", raise_e=False):
            self.swipe_to_object("first_generated_subscriber")
            self.driver.click("first_generated_subscriber")
    
    def select_first_publisher(self):
        """
        from the Publishers Generated tab, select the first publisher
        """
        if not self.driver.click("first_generated_publisher", raise_e=False):
            self.swipe_to_object("first_generated_publisher")
            self.driver.click("first_generated_publisher")

    def get_toast_text(self):
        """
        get text from pop up toast notification
        """
        return self.driver.wait_for_object("toast_notification", displayed=False).text

    def select_create_publisher_btn(self):
        """
        from createPublisher() tab, select 'Create' button to create a new publisher
        """
        self.swipe_to_object("create_publisher_btn")
        if not self.driver.click("create_publisher_btn", raise_e=False):
            self.swipe_to_object("create_publisher_btn")
            self.driver.click("create_publisher_btn")

    def enter_publisher_event_name_text(self, text):
        """
        after selecting publisher, insert text into event name textbox
        """
        self.driver.send_keys("publisher_event_name_textbox", text)

    def enter_publisher_event_data_text(self, text):
        """
        after selecting publisher, insert text into event data textbox
        """
        self.driver.send_keys("publisher_event_data_textbox", text)

    def select_publish_btn(self):
        """
        after selecting publisher, select publish btn
        """
        self.driver.click("publish_btn")

    def enter_subscribe_event_name_text(self, text):
        """
        after selecting subscriber, insert text into event name textbox
        """
        self.driver.send_keys("subscribe_event_name_textbox", text)

    def enter_subscribe_publisher_id_text(self, text):
        """
        after selecting subscriber, insert text into publisher id textbox
        """
        self.driver.send_keys("subscribe_publisher_id_textbox", text)

    def select_subscribe_btn(self):
        """
        after selecting subscriber, select subscribe button
        """
        self.swipe_to_object("subscribe_btn", direction="up")
        self.driver.click("subscribe_btn")

    def select_unsubscribe_btn(self):
        """
        after selecting subscriber, select ;unsubscribe button
        """
        self.driver.click("unsubscribe_btn")

    def get_subscription_generated_event_name_text(self, index=0, raise_e=False):
        """
        after selecting subscriber, and selecting subscribe btn, get generated event name text
        trims off "publisherID:" from returning text
        """
        event_name_result = self.driver.wait_for_object("subscription_generated_event", index=index, raise_e=raise_e)
        if event_name_result is False: 
            self.swipe_to_object("subscription_generated_event")
            event_name_result = self.driver.wait_for_object("subscription_generated_event", index=index, raise_e=raise_e, displayed=False)
        if event_name_result is False and raise_e is False:
            return False
        return event_name_result.text.replace(" Actions", "").split("eventName: ")[-1]

    def get_subscription_generated_publisher_id_text(self, index=0, raise_e=True):
        """
        after selecting subscriber, and selecting subscribe btn, get generated publisher id text
        """
        self.swipe_to_object("subscription_generated_event")
        publisher_id_result = self.driver.wait_for_object("subscription_generated_event", index=index, raise_e=raise_e)
        if publisher_id_result is False: 
            self.swipe_to_object("subscription_generated_event")
            publisher_id_result = self.driver.wait_for_object("subscription_generated_event", index=index, raise_e=raise_e)
        if publisher_id_result is False and raise_e is False:
            return False
        return publisher_id_result.text.replace("publisherId: ", "").split(" eventName:")[0]

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

    def select_delete_first_publisher_btn(self):
        """
         from publisher Generated tab, select delete publisher button 
        """
        if not self.driver.click("delete_first_publisher_btn", raise_e=False):
            self.swipe_to_object("delete_first_publisher_btn")
            self.driver.click("delete_first_publisher_btn")

    def select_first_delete_subscriber_btn(self):
        """
        from Subscribers Generated tab, select the first delete subscriber button
        """
        if not self.driver.click("delete_first_subscriber_btn", raise_e=False):
            self.swipe_to_object("delete_first_subscriber_btn")
            self.driver.click("delete_first_subscriber_btn")

    def select_persistent_drop_down_menu(self):
        """
        Select persistent id drop down menu in event service plugin
        """
        self.swipe_to_object("persistent_dropdown")
        self.driver.click("persistent_dropdown")

    def select_persistent_option_false_from_menu(self):
        """
        After opening Persistent id drop down menu, select any one option false
        """
        self.driver.click("persistent_false")

    def select_persistent_option_true_from_menu(self):
        """
        After opening Persistent id drop down menu, select any one option true
        """
        self.driver.click("persistent_true")

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