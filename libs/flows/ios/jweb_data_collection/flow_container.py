import json
from time import sleep
from MobileApps.libs.ma_misc import ma_misc
from ios_settings.src.libs.ios_system_flow_factory import ios_system_flow_factory
from MobileApps.libs.flows.ios.jweb_data_collection.home import Home
from MobileApps.libs.flows.ios.jweb_data_collection.data_valve import DataValve
from MobileApps.libs.flows.ios.jweb_data_collection.weblet import Weblet
from MobileApps.libs.flows.ios.jweb_data_collection.data_collection_settings import DataCollectionSettings
from MobileApps.libs.flows.web.jweb.data_collection_plugin import IOSDataCollectionPlugin
from MobileApps.libs.flows.ios.smart.files import Files
from MobileApps.resources.const.ios import const as i_const
from MobileApps.resources.const.web import const as w_const

class FlowContainer(object):
    def __init__(self, driver, load_app_strings=False):
        self.driver = driver
        self.fd = {"ios_system": ios_system_flow_factory(driver),
                   "home": Home(driver),
                   "files": Files(driver),
                   "data_valve": DataValve(driver),
                   "data_collection_settings": DataCollectionSettings(driver),
                   "weblet": Weblet(driver),
                   "data_collection_plugin": IOSDataCollectionPlugin(driver, context={'url': w_const.WEBVIEW_URL.JWEB_DATA_COLLECTION})}
    @property
    def flow(self):
        return self.fd
    
    def get_data_collection_test_data(self, stack):
        """
        Get data collection test data based on stack
        :param stack: stack of the test data
        :return: test data
        """
        with open(ma_misc.get_abs_path("resources/test_data/jweb/data_collection_test_data.json")) as test_data:
            data_collection_test_data = json.loads(test_data.read())
            if stack in ["stage", "pie"]:
                data_collection_test_data = data_collection_test_data[stack]
            elif stack == "dev":
                data_collection_test_data = data_collection_test_data["pie"]
            else:
                raise ValueError("Stack must be one of 'stage', 'pie', or 'dev'. Received: {}".format(stack))
        return data_collection_test_data

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch app
        """
        pkg_name = i_const.BUNDLE_ID.JWEB_DATA_COLLECTION
        self.driver.restart_app(pkg_name)
        sleep(5)

    def launch_app(self):
        """
        launches App
        """
        self.driver.launch_app(i_const.BUNDLE_ID.JWEB_DATA_COLLECTION)

    def close_app(self):
        """
        closes App
        """
        self.driver.terminate_app(i_const.BUNDLE_ID.JWEB_DATA_COLLECTION)

    def restart_app(self):
        """
        restarts app
        """
        self.driver.restart_app(i_const.BUNDLE_ID.JWEB_DATA_COLLECTION)

    def select_stack(self, stack):
        """
        Selects the stack
        """
        self.fd["weblet"].select_info_button()
        self.fd["weblet"].select_open_settings_button()
        self.fd["data_collection_settings"].choose_stack(stack)
        self.launch_app()
        self.fd["home"].select_webview_tab()

    def filter_cdm_tree(self, file, tree):
        """
        in DataCollection, filter and test a cdm tree
        """
        self.fd["data_collection_plugin"].expand_data_collection_method("filterCDMTrees")
        self.fd["data_collection_plugin"].select_cdm_tree_file_selector()
        self.fd["files"].navigate_to_application_folder('Firefox')
        self.fd["files"].select_item_cell(file, scroll=True)
        self.fd["files"].select_open_file_btn(raise_e=False)
        self.fd["data_collection_plugin"].send_text_to_textbox('cdm_tree_gun_textbox', tree)
        self.fd["files"].select_done(raise_e=False)
        self.fd["data_collection_plugin"].select_simplified_cdm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_cdm_tree_test_button()

    def filter_multiple_cdm_trees(self, files, tree='com.hp.cdm.service.eventing.version.1.resource.notification,com.hp.cdm.service.eventing.version.1.resource.notification'):
        if not isinstance(files, list):
            raise ValueError("files parameter must be a list of trees")
        self.fd["data_collection_plugin"].expand_data_collection_method("filterCDMTrees")
        self.fd["data_collection_plugin"].select_cdm_tree_file_selector()
        self.fd["files"].navigate_to_application_folder('Firefox')
        self.fd["files"].select_multiple_item_cell(files)
        self.fd["data_collection_plugin"].send_text_to_textbox('cdm_tree_gun_textbox', tree)
        self.fd["data_collection_plugin"].select_simplified_cdm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_cdm_tree_test_button()

    def filter_ledm_tree(self, file):
        """
        in DataCollection, filter and test a ledm tree
        """
        self.fd["data_collection_plugin"].expand_data_collection_method("filterLEDMTrees")
        self.fd["data_collection_plugin"].select_ledm_tree_file_selector()
        self.fd["files"].navigate_to_application_folder('Firefox')
        self.fd["files"].select_item_cell(file, scroll=True)
        self.fd["files"].select_open_file_btn(raise_e=False)
        self.fd["data_collection_plugin"].select_simplified_ledm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_ledm_tree_test_button()

    def filter_multiple_ledm_trees(self, files):
        if not isinstance(files, list):
            raise ValueError("files parameter must be a list of trees")
        self.fd["data_collection_plugin"].expand_data_collection_method("filterLEDMTrees")
        self.fd["data_collection_plugin"].select_ledm_tree_file_selector()
        self.fd["files"].navigate_to_application_folder('Firefox')
        self.fd["files"].select_multiple_item_cell(files)
        self.fd["files"].select_open_file_btn(raise_e=False)
        self.fd["data_collection_plugin"].select_simplified_ledm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_ledm_tree_test_button()

    def upload_single_notification_file(self, file):
        """
        in DataCollection, upload single notification file for sendprebuiltnotification
        """
        self.fd["data_collection_plugin"].select_upload_notification_file_selector()
        self.fd["files"].navigate_to_application_folder('Firefox')
        self.fd["files"].select_item_cell(file, scroll=True)
        self.fd["files"].select_open_file_btn(raise_e=False)

    def upload_multiple_notification_files(self, files):
        """
        in DataCollection, upload multiple notification files for sendprebuiltnotification
        """
        if not isinstance(files, list):
            raise ValueError("files parameter must be a list of files")
        self.fd["data_collection_plugin"].select_upload_notification_file_selector()
        self.fd["files"].navigate_to_application_folder('Firefox')
        self.fd["files"].select_multiple_item_cell(files)
        self.fd["files"].select_open_file_btn(raise_e=False)