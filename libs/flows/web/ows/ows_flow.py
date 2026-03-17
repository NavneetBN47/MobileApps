import time
from SAF.decorator.saf_decorator import native_context
from MobileApps.libs.flows.web.web_flow import WebFlow
from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.ma_misc import ma_misc
import logging
from bs4 import BeautifulSoup as bsoup
from collections import Counter

class UnexpectedURLError(Exception):
    pass

class OWSFlow(WebFlow):
    project = "ows"

    def __init__(self, driver, context=None, window_name="main",  url=None):
        super(OWSFlow, self).__init__(driver, context=context, window_name=window_name, url=url)
        self.func_ignore_methods.append("load_ows_shared_ui")
        self.load_ows_shared_ui()
        

    def load_ows_shared_ui(self):
        ui_map = self.load_ui_map(system="WEB", project="ows", flow_name="shared_obj")
        self.driver.load_ui_map("ows", "shared_obj", ui_map)
        return True    
    
    def get_total_carousel_pages(self):
        self.driver.wait_for_object("_shared_carousel_owl_dot", timeout=10)
        return len(self.driver.find_object("_shared_carousel_owl_dot", multiple=True))
    
    
    def scroll_carousel(self, direction="right"):
        if self.driver.wait_for_object("_shared_arrow_right", timeout=3, raise_e=False):
            return self.driver.click("_shared_arrow_right")

        carousel_obj = self.driver.find_object("_shared_carousel_obj")
        if direction == "right":
            offset = -100
        elif direction == "left":
            offset = 100
        else:
            raise ValueError("Unknown direction: " + str(direction))
        self.driver.drag_and_drop(carousel_obj, x_offset=offset+1)

    
    def verify_carousel_screen_header(self):
        return self.driver.wait_for_object("_shared_carousel_screen_header")
    
    def verify_carousel_screen_owl_dots(self):
        return self.driver.wait_for_object("_shared_carousel_screen_owl_dots")

    def verify_carousel_screen_continue_or_skip_btn(self):
        return self.driver.wait_for_object("_shared_carousel_screen_continue_or_skip_btn")   

    def verify_carousel_screen_card_content(self):
        return self.driver.wait_for_object("_shared_carousel_content", displayed=False)



    def verify_spinner_modal(self):
        return self.driver.wait_for_object("_shared_spinner_modal", timeout=30)
     
    @screenshot_compare(root_obj="_shared_error_modal")
    def verify_error_modal(self, invisible=False):
        return self.driver.wait_for_object("_shared_error_modal", invisible=invisible, timeout=15)

    def handle_partial_screenshot(self, bottle_type=''):
        self.verify_carousel_screen_header()
        self.driver.process_screenshot(self.file_path,("verify_carousel_screen_header_{}").format(bottle_type), root_obj="_shared_carousel_screen_header")
        
        for index in range(self.get_total_carousel_pages() - 1):
            self.verify_carousel_screen_owl_dots()
            self.driver.process_screenshot(self.file_path,("carousel_screen_owl_dots_{}"+ str(index+1)).format(bottle_type), root_obj="_shared_carousel_screen_owl_dots")
            self.verify_carousel_screen_card_content()
            self.driver.process_screenshot(self.file_path,("carousel_screen_card_content_{}"+ str(index+1)).format(bottle_type), root_obj="_shared_carousel_screen_card_content")
            if self.driver.wait_for_object("_shared_carousel_screen_continue_or_skip_btn", raise_e=False): 
                self.driver.process_screenshot(self.file_path,("carousel_screen_continue_or_skip_btn_{}"+ str(index+1)).format(bottle_type), root_obj="_shared_carousel_screen_continue_or_skip_btn")
            
            self.scroll_carousel()
            if self.driver.wait_for_object(f"_shared_carousel_screen_card_item_{index+2}", raise_e=False) is False:
                self.scroll_carousel()


    def string_validation_td_live_ui_steps(self, file_name, object, locale):
        """
        Method to Validate strings on Traffic Director Live UI Step.
        """
        web_str = self.driver.wait_for_object(object, timeout=15).text
        data = ma_misc.load_json_using_absolute_path(file_name)[locale]
        if object in data:
            if type(data[object]) is str:
                spec_str = data[object]
                self.checking_web_str_against_spec_string(spec_str, web_str)
            elif type(data[object]) is list:
                for i in range(0,5):
                    if str(i) in object:
                        spec_str = data["cards"][i]["instructions"]
                        self.checking_web_str_against_spec_string(spec_str, web_str)
                    else:
                        raise ValueError("Counld not find the correct key for the web_str: {} in the spec: {}".format(web_str, spec_str))

    def string_validation(self, spec_data, object, raise_e=True):
        web_str = self.driver.wait_for_object(object, timeout=15).text
        spec_strg = spec_data[object]
        return self.checking_web_str_against_spec_string(spec_strg, web_str, object, raise_e=raise_e)
    
    
    def checking_web_str_against_spec_string(self, spec_strg, web_str, object, raise_e=True):
        spec = bsoup(spec_strg, "html.parser")
        spec_string = spec.text
        """char = "<"
        if char in spec_strg:
            result = re.findall("<.*?>", spec_strg)
            for i in result:
                spec_strg = spec_strg.replace(i, "")
        spec_strg = spec_strg.replace("\u200b", "").strip()"""
        spec_string = spec_string.strip().replace("\xa0", " ").replace("\u200b", "").replace("<>", "").strip()
        time.sleep(2)
        if web_str == spec_string:
            return True
        elif web_str.replace("\n", "") == spec_string.replace("\n", ""):
            return True
        
        if raise_e:
            raise AssertionError("'{}' object String does not match '{}' string pulled from ImageBank for locator: {}".format(web_str, spec_string, object))
        else:
            logging.info("'{}' object String does not match '{}' string pulled from ImageBank for locator: {}".format(web_str, spec_string, object))
            return False
    
    def log_event_parse_kibana_format(self, requests_body, event_category):
        """
        Method to get event details from the requests body
        """
        kib_events = []
        for request in requests_body:
            response_code = self.driver.get_response_status_code(request)
            event_payload = self.driver.get_request_details(request)['body']['events']
            for i in range(len(event_payload)):
                if event_payload[i]['eventCategory'] == event_category and 'PortalOobe' in event_payload[i]['eventDetail']['screenPath']:
                    kib_events.append(self.get_events_in_kibana_format(event_payload[i]['eventDetail']))
                    logging.info("event:{} Response Code:{}".format(event_payload[i]['eventDetail'],response_code))
        return dict(Counter(kib_events))
    
    def get_events_in_kibana_format(self, simple_ui_event):
        """
        This method to get events from the network calls in kibana format
        """
        kib_format = ["action", "screenName", "screenPath", "controlName", "screenMode", "controlDetail", "activity"]
        simple_ui_event.pop('version')
        kibs = []
        for i in kib_format:
            if i in simple_ui_event.keys():
                kibs.append(simple_ui_event[i])
        return ",".join(kibs)
    
    def get_visituuid(self, events_requests):
        """
        This method will return the visituuid of the test run. 
        Visituuid will be used to get all the information about that session from (formerly) kibana/opensearch
        """
        visit_uuid = self.driver.get_request_details(events_requests[0])['body']['originator']['originatorDetail']['visitUuid']
        logging.info("visit_uuid: {}".format(visit_uuid))
        return visit_uuid
    
    def get_printer_profile(self):
        self.request = self.driver.session_data["request"]
        return self.request.config.getoption("--printer-profile")                
        
class AndroidOWSFlow(OWSFlow):

    def scroll_carousel(self, direction="right"):
        # Swipe() has native_context decorator.
        self.driver.swipe(direction=direction)