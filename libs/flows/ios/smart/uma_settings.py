import logging
import pytest
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.resources.const.web import const as w_const
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
from MobileApps.resources.const.ios import const as i_const


class UMASettings(SmartFlow):
    flow_name = "uma_settings"
    
    def enable_uma_flag(self, app):
        """
        Enable UMA flag
        """
        stacks = {
            i_const.BUNDLE_ID.SMART: {
                "app_name": "HP Smart AH"
            }
        }
        app_name = stacks[app]["app_name"]
        self.search_for_menu_option(app_name)
        self.driver.click("search_option", format_specifier=[app_name])
        self.driver.scroll("stack_cell_menu_option", check_end=False, timeout=45)
        self.driver.swipe(direction="down")
        self.driver.click("hpx_flag",timeout=5)
        self.driver.click("enable_uma_links",timeout=5)
        self.driver.click("uma_site",timeout=5)
    
    def search_for_menu_option(self, option):
        self.driver.swipe(direction="up", per_offset=0.8)
        time.sleep(0.5)
        self.driver.send_keys("settings_search_field", option)
        