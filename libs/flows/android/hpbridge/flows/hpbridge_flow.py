# coding: utf-8
from abc import ABCMeta

from selenium.common.exceptions import NoSuchElementException

from MobileApps.libs.flows.android.android_flow import AndroidFlow
from time import sleep
from MobileApps.resources.const.android.const import PACKAGE, LAUNCH_ACTIVITY
import logging
import time

from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
import pytest
from MobileApps.libs.flows.base_flow import find_context_for_method_name
import inspect
import types


def find_page_for_method_name(_class, method_name):
    _class_definition = _class.__class__
    # Check first if the class have a this page(window) defined
    instance_page = getattr(_class, "page", None)
    # Check if class definition overloaded this page(window)
    class_list = inspect.getmro(_class_definition)
    for _cls in class_list:
        if method_name in [key for key, value in _cls.__dict__.items() if type(value) == types.FunctionType]:
            definition_page = getattr(_cls, "page", None)
            break

    if definition_page is None:
        if instance_page is None:
            #If no defined context nor instance this page(window)  default is None
            return None
        else:
            #If no context is defined in the class use the this page(window)  in the instance
            return instance_page
    else:
        #If this page(window) is defined in the class use that one
        return definition_page

class QRCode(object):
    """
    this class used to define the QRCode path in test phone
    """
    valid = "a_printer"
    invalid ="a_qrcode_invalid"
    reset = "a_printer_reset"
    pa_stage = "a_pa_stage"
    pa_dev = "a_pa_dev"


class Stacks(object):
    DEV = "dev"
    STAGE = "stage"


class HPBridgeFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "hpbridge"
    current_context = "NATIVE_APP"
    current_page = None

    print_options_dict = {
        "draft": {
            "tag": "草稿",
            "element": "draft_selection"
        },
        "normal": {
            "tag": "一般",
            "element": "current_selection"
        },
        "best": {
            "tag": "最佳",
            "element": "best_selection"
        },
        "A4": "A4",
        "4x6": "4 x 6",
        "5x7": "5 x 7",
        "HPGlossy220": '照片纸',
        "Plain": "普通纸"
    }

    def __init__(self, driver):
        super(HPBridgeFlow, self).__init__(driver)
        self.load_shared_ui()

    def __getattribute__(self, attr):
        method = object.__getattribute__(self, attr)

        # except AttributeError:
        #    raise NameError("NameError: name '%s' is not defined" % attr)
        if type(method) == types.MethodType:
            if attr in self.func_ignore_methods:
                self.driver.current_project = self.project
                self.driver.current_flow = self.flow_name
                return method

            elif not inspect.isabstract(self) and callable(method):
                if self.driver.driver_class == "appium":
                    # If the flow have no context variable it is defaulted to always run NATIVE_APP.
                    context = find_context_for_method_name(self, attr)  # getattr(self, "context", "NATIVE_APP")
                    page = find_page_for_method_name(self, attr)

                    if context != HPBridgeFlow.current_context:
                        logging.info(" %%%%%%%%%%%%   ---  current contexts: " + str(self.driver.wdvr.contexts))
                        self.driver.switch_to_webview(webview_name=context)
                        HPBridgeFlow.current_context = context
                        logging.info(" %%%%%%%%%%%%   ---  change context to: " + context)
                    else:
                        logging.info(" %%%%%%%%%%%%   ---  remain context : " + context)

                    if page != HPBridgeFlow.current_page:
                        if page is None:
                            HPBridgeFlow.current_page = None
                            logging.info(" %%%%%%%%%%%%   ---  change window to: " + str(page))
                        else:
                            for window in self.driver.wdvr.window_handles:
                                self.driver.switch_to_window(window_handle=window)
                                if page in str(self.driver.wdvr.page_source):
                                    logging.info(" %%%%%%%%%%%%   ---  change window to: " + page)
                                    HPBridgeFlow.current_page = page
                                    break
                            else:
                                raise KeyError("Failed to find window with page index is: " + page)
                    else:
                        logging.info(" %%%%%%%%%%%%   ---  remain window: " + str(page))

                if self.driver.driver_class == "selenium" and hasattr(self, "wn"):
                    self.driver.switch_window(self.wn)
                self.driver.current_project = self.project
                self.driver.current_flow = self.flow_name
                if method.__name__ not in self.logging_ignore_methods:
                    logging.info("START - {}".format(method.__name__))
        return method

    def load_shared_ui(self):
        ui_map = self.load_ui_map(self.system, project=self.project, flow_name="shared_obj")
        self.driver.load_ui_map(self.project, "shared_obj", ui_map)

    # this used for windows local test temporary before AMS integrated

    @staticmethod
    def set_pytest_data(test_stack=Stacks.STAGE, test_mobile="HUAWEI P30"):
        pytest.test_mobile = test_mobile
        pytest.test_stack = test_stack
        user, device = utlitiy_misc.load_user_device()
        pytest.device_name = device["device_name"]
        pytest.platform_version = device["platform_version"]
        pytest.device_uuid = device["device_uuid"]
        pytest.test_user = user["nickname"]
        pytest.app_info = "hpbridge"

    def launch_wechat(self):
        if self.driver.wdvr.current_activity != LAUNCH_ACTIVITY.HPBRIDGE:
            self.driver.wdvr.terminate_app(PACKAGE.HPBRIDGE)
            self.driver.wdvr.start_activity(PACKAGE.HPBRIDGE, LAUNCH_ACTIVITY.HPBRIDGE)

    def click_top_back_arrow_icon(self):
        """
        Click on the back arrow icon on top left of the screen
        :return:
        """
        self.driver.wait_for_object("top_arrow_back_btn")
        self.driver.click("top_arrow_back_btn")

    def close_mp(self):
        """
        Close the mini program
        :return:
        """
        self.driver.click("close_mp_btn")

    def return_home_page(self):
        """
        Return to the home page in 3 dots menu
        :return:
        """
        return_home_btn = self.driver.find_object("back_home_page", raise_e=False)
        if return_home_btn is not False:
            return_home_btn.click()
        else:
            logging.log("You are on home page or unable to find the home page button")

    def check_parameter_in_dict(self, parameter):
        """
        Check if the print options user given exist in our dictionary or not
        :param parameter:
        :return:
        """
        find = False
        for key in self.print_options_dict:
            if isinstance(self.print_options_dict[key], dict):
                if key == parameter or self.print_options_dict[key]["tag"] == parameter:
                    return self.print_options_dict[key]["element"]
                    find = True
            else:
                if key == parameter:
                    return self.print_options_dict[key]
                    find = True
        if not find:
            raise KeyError("%s is not supported in the print setting options!" % parameter)

    def check_element_in_screen(self, obj_name, format_specifier=[], root_obj=None):
        """
        For some small screen phone, sometimes the element is out of the screen. this method is
        to check if the element is in current screen.
        :return: if the element is in screen ,return true, otherwise, return false
        """

        bounds = self.driver.get_attribute(obj_name, "bounds", format_specifier=format_specifier, root_obj=root_obj)
        height = int(str(bounds).split("][")[1].split(",")[1].split("]")[0]) - \
                 int(str(bounds).split("][")[0].split(",")[1])

        if height > 20:
            return True

    def swipe_to_element_shown(self, obj_name, format_specifier=[], root_obj=None, time_out=180, check_end=True):
        """
        This method used to swipe the screen till the object displays in the current screen. because there is
        no effective way to check if the object displayed or not, so we check the bounds attribute of the object,
        if the height of the object is too small, we think the object is still out of screen
        :return:
        """
        exist = self.driver.find_object(obj_name, format_specifier=format_specifier, root_obj=root_obj, raise_e=False)
        if exist:
            in_screen = self.check_element_in_screen(obj_name, format_specifier=format_specifier,
                                                   root_obj=root_obj)
        else:
            in_screen = False
        end = False
        start_time = time.time()
        time_cost = 0
        while not end and not in_screen and time_cost <= time_out:
            end = self.driver.swipe(check_end=check_end)[1]
            exist = self.driver.find_object(obj_name, format_specifier=format_specifier, root_obj=root_obj,
                                            raise_e=False)
            if exist:
                in_screen = self.check_element_in_screen(obj_name, format_specifier=format_specifier,
                                                         root_obj=root_obj)
            time_cost = time.time() - start_time

        if not exist:
            raise NoSuchElementException("Failed to find the element with the name: %s and format_specifier: %s"
                                         % (obj_name, format_specifier))

        if time_cost > time_out:
            raise TimeoutError("Swipe scrren to find the object timeout in %s second" % time_out)

    def switch_to_native_view(self):
        self.driver.switch_to_webview("NATIVE_APP")
        HPBridgeFlow.current_context == "NATIVE_APP"
        HPBridgeFlow.current_page == None