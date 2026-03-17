from MobileApps.libs.flows.common.gotham.gotham_flow import GothamFlow
import MobileApps.resources.const.windows.const as w_const
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import re
import time

class PersonalizeTiles(GothamFlow):
    flow_name = "personalize_tiles"
    sortedtiles_path = w_const.TEST_DATA.GOTHAM_APP_LOG_PATH + '\\' + 'SortedTiles.xml'

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def check_sorted_tiles_path(self):
        assert self.driver.ssh.check_file(self.sortedtiles_path) is True

    def check_sorted_tiles_data(self, check_event):
        time.sleep(3)
        f = self.driver.ssh.remote_open(self.sortedtiles_path)
        data = f.read().decode("utf-8").replace('\n', '')
        f.close()
        if not re.search(check_event, data):
            raise NoSuchElementException(
                    "Fail to found {}".format(check_event))
        
    def get_personalize_tile_name(self, name):
        return self.driver.get_attribute(name, attribute="Name")
    
    def get_personalize_tile_index(self, i):
        if self.driver.wait_for_object("dynamic_tile_option_image", timeout=1, format_specifier=[i], raise_e=False):
            return self.driver.get_attribute('dynamic_tile_option_get_supplies', format_specifier=[i], attribute="Name")
        else:
            return self.driver.get_attribute('dynamic_tile_option', format_specifier=[i], attribute="Name")

    def click_tile_toggle(self, name):
        self.driver.click(name)

    def drag_and_drop_tile_option(self, name1, name2, duration=20000):
        self.driver.drag_and_drop(self.driver.wait_for_object(name1), self.driver.wait_for_object(name2), duration=duration)
    
    def hover_tile(self, num):
        self.driver.hover('dynamic_tile', format_specifier=[num])

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_personalize_tile(self, name, raise_e=False):
        return self.driver.wait_for_object(name, raise_e=raise_e)

    def send_key_to_get_personalize_tile(self, name):
        el = self.driver.wait_for_object(name, timeout=2)
        el.send_keys(Keys.DOWN)

    def verify_personalize_tile_off(self, name):
        assert self.driver.wait_for_object(name).get_attribute("Toggle.ToggleState") == "0"

    def verify_personalize_tile_on(self, name):
        assert self.driver.wait_for_object(name).get_attribute("Toggle.ToggleState") == "1"

    def verify_printables_personalize_tile(self):
        return self.driver.wait_for_object("printables_option")

    def verify_personalize_tiles_screen(self, hpid_region=True):
        self.driver.wait_for_object("get_supplies_option")
        self.driver.wait_for_object("scan_option")      
        self.driver.wait_for_object("printables_option")
        self.driver.wait_for_object("print_documents_option")
        self.driver.wait_for_object("help_support_option")
        assert self.driver.wait_for_object("play_learn_option", raise_e=False) is False
        assert self.driver.wait_for_object("get_supplies_toggle").get_attribute("Toggle.ToggleState") == "1"
        assert self.driver.wait_for_object("scan_toggle").get_attribute("Toggle.ToggleState") == "1"
        assert self.driver.wait_for_object("printables_toggle").get_attribute("Toggle.ToggleState") == "1"
        assert self.driver.wait_for_object("print_documents_toggle").get_attribute("Toggle.ToggleState") == "1"
        assert self.driver.wait_for_object("help_support_toggle").get_attribute("Toggle.ToggleState") == "1"
        
        for _ in range(5):
            self.driver.swipe()
            time.sleep(1)
        self.driver.wait_for_object("print_photos_option")
        self.driver.wait_for_object("printer_settings_option") 
        assert self.driver.wait_for_object("print_photos_toggle").get_attribute("Toggle.ToggleState") == "1"
        assert self.driver.wait_for_object("printer_settings_toggle").get_attribute("Toggle.ToggleState") == "1"
        if hpid_region:
            self.driver.wait_for_object("shortcuts_option")
            self.driver.wait_for_object("mobile_fax_option")
            assert self.driver.wait_for_object("shortcuts_toggle").get_attribute("Toggle.ToggleState") == "1"
            assert self.driver.wait_for_object("mobile_fax_toggle").get_attribute("Toggle.ToggleState") == "1"
        else:
            assert self.driver.wait_for_object("shortcuts_option", raise_e=False) is False
            assert self.driver.wait_for_object("mobile_fax_option", raise_e=False) is False
