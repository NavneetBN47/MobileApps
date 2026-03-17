import logging
import time

from MobileApps.libs.flows.email.gmail_api import GmailAPI
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.smart.smart_welcome import SmartWelcome
from MobileApps.libs.flows.web.shortcuts.shortcuts_create_edit import MobileShortcutsCreateEdit
from MobileApps.resources.const.android import const as a_const
from MobileApps.resources.const.web import const as w_const
from MobileApps.libs.flows.android.hpx.hpx_additional_settings import HPXAdditionalSettings
from MobileApps.libs.flows.android.hpx.hpx_camera_scan  import HpxCameraScan
from MobileApps.libs.flows.android.hpx.hpx_home import HpxHome


class FLOW_NAMES():
    GMAIL_API = "gmail_api"
    HPID = "hpid"
    WEB_SMART_WELCOME = "web_smart_welcome"
    SHORTCUTS = "shortcuts_create_edit"
    PRINTABLES = "printables"
    HPX_ADDITIONAL_SETTINGS = "hpx_additional_settings"
    HPX_CAMERA_SCAN = "hpx_camera_scan"
    HPX_HOME = "hpx_home"

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.pkg_name = a_const.PACKAGE.HPX(self.driver.session_data["pkg_type"])
        self.driver.session_data["smart_state"] = {}  # need to check this for hpx
        self.stack = self.driver.session_data["request"].config.getoption("--stack")
        self.hpx_context = a_const.WEBVIEW_CONTEXT.HPX(self.driver.session_data["pkg_type"])
        self.hpid_url = w_const.WEBVIEW_URL.HPID(self.stack)
        
        self.fd = {
            FLOW_NAMES.GMAIL_API: GmailAPI(credential_path=a_const.TEST_DATA.GMAIL_TOKEN_PATH),
            FLOW_NAMES.HPID: HPID(driver, context={"url": self.hpid_url}),
            FLOW_NAMES.WEB_SMART_WELCOME: SmartWelcome(driver, context=self.hpx_context),
            FLOW_NAMES.SHORTCUTS: MobileShortcutsCreateEdit(driver, context=self.hpx_context),
            FLOW_NAMES.HPX_ADDITIONAL_SETTINGS: HPXAdditionalSettings(driver),
            FLOW_NAMES.HPX_CAMERA_SCAN: HpxCameraScan(driver),
            FLOW_NAMES.HPX_HOME: HpxHome(driver)
        }

    @property
    def flow(self):
        return self.fd

    # *********************************************************************************
    #                               HPX ACTION FLOWS                                  *
    # *********************************************************************************


    def launch_hpx(self):
        activity = a_const.LAUNCH_ACTIVITY.SMART_HPX
        return self.driver.start_activity(self.pkg_name, activity, wait_activity = None)

    def terminate_and_relaunch_hpx(self):
        """
        Terminate app and relaunch app
        """
        self.kill_hpx_app()
        time.sleep(5)
        self.launch_hpx()

    def kill_hpx_app(self):
        self.driver.terminate_app(self.pkg_name, a_const.LAUNCH_ACTIVITY.SMART_HPX)

    def kill_chrome(self):
        """
        Terminates Google Chrome app
        """
        self.driver.terminate_app(a_const.PACKAGE.GOOGLE_CHROME)

    def flow_change_hpx_app_stack_server(self, stack):
        """
        - Launch additional settings page of HPX app (its present in the HPX app settings - 'i' button when long press on hpx app)
        - Change stack server & web apps stack server based on input
        - Default stack for HPX google store debug builds is STAGE
        """
        stacks = {"production": self.fd[FLOW_NAMES.HPX_ADDITIONAL_SETTINGS].PRODUCTION_STACK,
                  "stage": self.fd[FLOW_NAMES.HPX_ADDITIONAL_SETTINGS].STAGE_STACK,
                  "pie": self.fd[FLOW_NAMES.HPX_ADDITIONAL_SETTINGS].PIE_STACK
        }
        webapp_stacks = {
                "pie": self.fd[FLOW_NAMES.HPX_ADDITIONAL_SETTINGS].WEBAPP_PIE_STACK,
                "stage": self.fd[FLOW_NAMES.HPX_ADDITIONAL_SETTINGS].WEBAPP_STAGE_STACK,
                "production": self.fd[FLOW_NAMES.HPX_ADDITIONAL_SETTINGS].WEBAPP_PRODUCTION_STACK
        }
        if self.driver.session_data["smart_state"].get("stack", None) != stack:
            self.fd[FLOW_NAMES.HPX_ADDITIONAL_SETTINGS].open_select_settings_page()
            time.sleep(5)
            self.fd[FLOW_NAMES.HPX_ADDITIONAL_SETTINGS].change_stack_server(stacks[stack], webapp_stacks[stack])
            self.driver.session_data["smart_state"]["stack"] = stack

    def reset_hpx_app(self, change_stack = False):
        self.driver.clear_app_cache(self.pkg_name)
        self.driver.session_data["smart_state"].clear()
        if change_stack:
            self.flow_change_hpx_app_stack_server(self.stack)
