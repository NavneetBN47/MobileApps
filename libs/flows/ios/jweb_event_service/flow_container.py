from MobileApps.libs.flows.ios.jweb_event_service.home import Home
from MobileApps.libs.flows.web.jweb.home import Home as WebHome
from MobileApps.libs.flows.web.jweb.event_service_plugin import EventServicePlugin
from MobileApps.libs.flows.web.jweb.event_service_plugin import IOSEventServicePlugin
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.web import const as w_const
from time import sleep

class FlowContainer(object):
    def __init__(self, driver, load_app_strings=False):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "web_home": WebHome(driver, context={'url':w_const.WEBVIEW_URL.JWEB}),
                   "event_service_plugin": EventServicePlugin(driver, context={'url':w_const.WEBVIEW_URL.JWEB}),
                   "native_event_service_plugin": IOSEventServicePlugin(driver, context={'url':w_const.WEBVIEW_URL.JWEB})}
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
        pkg_name = i_const.BUNDLE_ID.JWEB_EVENT_SERVICE
        self.driver.restart_app(pkg_name)
        sleep(5)

    def close_app(self):
        """
        closes App
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.JWEB_EVENT_SERVICE)

    #   -----------------------         FROM NATIVE SIDE       -----------------------------

    def native_add_subscription_for_existing_subscriber(self, publisher_id):
        """
        Load to Native Event Service Plugin screen:
            -Launch app
            -Navigate to subscriber tab
            -select existing subscriber
            -select subscriptions
        """
        self.flow_load_home_screen()
        self.fd["home"].select_subscribers_tab()
        self.fd["native_event_service_plugin"].native_select_existing_subscriber_from_list()
        self.fd["native_event_service_plugin"].native_select_subscriptions_btn()
        self.fd["native_event_service_plugin"].native_select_add_subscription_btn()
        self.fd["native_event_service_plugin"].native_enter_new_publisher_id_text(publisher_id)
        self.fd["native_event_service_plugin"].native_select_subscription_btn()

    def native_select_persist_events_toggle(self):
        """
        Selects Persist Events from subscriber tab
        """
        self.fd["home"].select_subscribers_tab()
        self.fd["native_event_service_plugin"].native_select_existing_subscriber_from_list()
        self.fd["native_event_service_plugin"].native_persist_events_toggle()
    
    def native_select_pause_events(self):
        """
        Selects Pause Events
        """
        self.fd["home"].select_subscribers_tab()
        self.fd["native_event_service_plugin"].native_select_existing_subscriber_from_list()
        self.fd["native_event_service_plugin"].native_select_pause_events_btn()

    def native_publish_an_event(self, publisher_id):
        """
        Publishes an event
        """
        self.fd["home"].select_publishers_tab()
        self.fd["native_event_service_plugin"].native_select_add_publisher_btn()
        self.fd["native_event_service_plugin"].native_enter_new_publisher_id_text(publisher_id)
        self.fd["native_event_service_plugin"].native_click_create_publisher_btn()
        self.fd["native_event_service_plugin"].native_select_publisher(publisher_id)
        self.fd["native_event_service_plugin"].native_select_publish_btn()

    def native_verify_event_received(self):
        """
        Verifies event received
        """
        self.fd["home"].select_events_tab()

    def native_select_resume_events(self):
        """
        Selects Resume Events
        """
        self.fd["home"].select_subscribers_tab()
        self.fd["native_event_service_plugin"].native_select_resume_events_btn()

    def native_create_new_subscriber_with_is_persist_yes(self):
        """
        Load to Native Event Service Plugin screen:
            -Launch app
            -Navigate to subscriber tab
            -Create new subscriber
            -Click on the is persist yes button
        """
        self.flow_load_home_screen()
        self.fd["home"].select_subscribers_tab()
        self.fd["native_event_service_plugin"].native_select_add_new_subscriber_btn()
        self.fd["native_event_service_plugin"].native_select_create_subscriber_btn()
        self.fd["native_event_service_plugin"].native_is_persist_yes_subscriber()

    def native_create_subscription_for_newly_created_subscriber(self, publisher_id):
        """
        Load to Native Event Service Plugin screen:
            -Launch app
            -Navigate to subscriber tab
            -Create new subscriber
            -Select newly created subscriber and add a subscriptions            
        """
        self.flow_load_home_screen()
        self.native_create_new_subscriber_with_is_persist_yes()
        self.fd["native_event_service_plugin"].native_select_newly_created_subscriber()
        self.fd["native_event_service_plugin"].native_select_subscriptions_btn()
        self.fd["native_event_service_plugin"].native_select_add_subscription_btn()
        self.fd["native_event_service_plugin"].native_enter_new_publisher_id_text(publisher_id)
        self.fd["native_event_service_plugin"].native_select_subscription_btn()

    def native_create_publisher(self, publisher_id):
        """
        Load to Native Event Service Plugin screen:
            -Launch app
            -Navigate to publisher tab
            -Create add button
            -Enter publisher id and create publisher         
        """
        self.fd["home"].select_publishers_tab()
        self.fd["native_event_service_plugin"].native_select_add_publisher_btn()
        self.fd["native_event_service_plugin"].native_enter_new_publisher_id_text(publisher_id)
        self.fd["native_event_service_plugin"].native_click_create_publisher_btn()

    def native_create_new_subscriptions(self, publisher_id):
        """
        - click on the subscription button
        - click on the add subscription button
        - enter the publisher id
        - click on the subscription button 
        """
        self.fd["native_event_service_plugin"].native_select_subscriptions_btn()
        self.fd["native_event_service_plugin"].native_select_add_subscription_btn()
        self.fd["native_event_service_plugin"].native_enter_new_publisher_id_text(publisher_id)
        self.fd["native_event_service_plugin"].native_select_subscription_btn()

    def native_create_new_subscriber_with_is_persist_no(self):
        """
        Load to Native Event Service Plugin screen:
            -Launch app
            -Navigate to subscriber tab
            -Create new subscriber
            -Click on the is persist no button
        """
        self.flow_load_home_screen()
        self.fd["home"].select_subscribers_tab()
        self.fd["native_event_service_plugin"].native_select_add_new_subscriber_btn()
        self.fd["native_event_service_plugin"].native_select_create_subscriber_btn()
        self.fd["native_event_service_plugin"].native_is_persist_no_subscriber()