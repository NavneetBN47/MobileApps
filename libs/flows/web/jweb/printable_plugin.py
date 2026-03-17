import json
from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow
from MobileApps.libs.flows.ios.jweb.jweb_plugin_flow import JwebPluginFlow

class PrintablePlugin(JwebFlow):
    flow_name = "printable_plugin"

    def select_orientation_drop_down_menu(self):
        """
        select orientation menu from the DocSourceType.url
        """
        self.driver.click("orientation_drop_down_menu")

    def select_orientation_from_plugin_page(self, option):
        """
        open orientation drop down menu if it is not already open, then select option
        """
        if not self.driver.wait_for_object("landscape_menu_option", timeout=3, raise_e=False):
            self.select_orientation_drop_down_menu()
        
        if option == 'landscape':
            self.driver.click("landscape_menu_option")
        elif option == 'portrait':
            self.driver.click("portrait_menu_option")
        elif option == 'no_option':
            self.driver.click("no_option_menu_option")
        else:
            raise ValueError("option:{} not present from orientation drop down menu selection".format(option))

    def get_text_from_event_url_text_field(self):
        """
        return the text found within the event url text field
        """
        return self.driver.get_attribute("event_url_text_field", "value")

    def get_print_text_result(self, timeout=10):
        """
        return the text result after printing, or checking printability
        """
        return json.loads(self.driver.wait_for_object("print_result_text", timeout=timeout).text)

    def insert_text_into_event_url_text_field(self, text):
        """
        send text to the event url text field
        """
        self.driver.selenium.js_clear_text("event_url_text_field")
        self.driver.send_keys("event_url_text_field", text)

    def select_open_print_page_btn(self):
        """
        click 'print' btn, from the DocSourceType.url, which opens the Android print page
        """
        self.driver.click("print_test_btn")

    def select_determine_printability_btn(self):
        """
        click 'determine printability' btn, from the DocSourceType.url
        """
        self.driver.click("determine_printability_btn")

    def verify_at_printable_plugin(self):
        """
        verify that we are currently on the printable plugin
        """
        el = self.driver.wait_for_object("printer_plugin_header_title", raise_e=False, timeout=5)
        return False if el is False else el.text == 'Printer'
