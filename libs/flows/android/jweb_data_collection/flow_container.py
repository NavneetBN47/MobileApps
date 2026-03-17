import json
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.android.jweb_data_collection.home import Home
from MobileApps.libs.flows.android.jweb_data_collection.data_valve import DataValve
from MobileApps.libs.flows.android.jweb_data_collection.data_collection_settings import DataCollectionSettings
from MobileApps.libs.flows.android.jweb_data_collection.data_collection_dev_settings import DataCollectionDevSettings
from MobileApps.libs.flows.android.jweb_data_collection.data_collection_service import DataCollectionService
from MobileApps.libs.flows.web.jweb.data_collection_plugin import DataCollectionPlugin
from MobileApps.libs.flows.android.smart.local_files import LocalFiles
from MobileApps.resources.const.android.const import PACKAGE, LAUNCH_ACTIVITY
from MobileApps.resources.const.web.const import WEBVIEW_URL

class FlowContainer(object):
    def __init__(self, driver, load_app_strings=False):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "data_valve": DataValve(driver),
                   "data_collection_settings": DataCollectionSettings(driver),
                   "data_collection_dev_settings": DataCollectionDevSettings(driver),
                   "data_collection_service": DataCollectionService(driver),
                   "data_collection_plugin": DataCollectionPlugin(driver, context={'url':WEBVIEW_URL.JWEB_DATA_COLLECTION}),
                   "local_files": LocalFiles(driver)}
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

    #   --------------------  FROM DATA COLLECTION PLUGIN  --------------------------
    def filter_cdm_tree(self, file, tree='com.hp.cdm.service.eventing.version.1.resource.notification', cdm_btn_change_check=None):
        self.fd["data_collection_plugin"].expand_data_collection_method("filterCDMTrees")
        self.fd["data_collection_plugin"].select_cdm_tree_file_selector()
        self.fd["local_files"].load_downloads_folder_screen()
        self.fd["local_files"].select_file(file)
        self.fd["data_collection_plugin"].send_text_to_textbox('cdm_tree_gun_textbox', tree)
        self.fd["data_collection_plugin"].select_simplified_cdm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_cdm_tree_test_button(change_check=cdm_btn_change_check)

    def filter_multiple_cdm_trees(self, files, tree='com.hp.cdm.service.eventing.version.1.resource.notification,com.hp.cdm.service.eventing.version.1.resource.notification'):
        if not isinstance(files, list):
            raise ValueError("files parameter must be a list of trees")
        self.fd["data_collection_plugin"].expand_data_collection_method("filterCDMTrees")
        self.fd["data_collection_plugin"].select_cdm_tree_file_selector()
        self.fd["local_files"].load_downloads_folder_screen()
        for i, file in enumerate(files):
            self.fd["local_files"].select_file(file, long_press=True)
        self.fd["local_files"].select_select_button()
        self.fd["data_collection_plugin"].send_text_to_textbox('cdm_tree_gun_textbox', tree)
        self.fd["data_collection_plugin"].select_simplified_cdm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_cdm_tree_test_button()

    def filter_ledm_tree(self, file):
        self.fd["data_collection_plugin"].expand_data_collection_method("filterLEDMTrees")
        self.driver.swipe(direction="down")
        self.fd["data_collection_plugin"].select_ledm_tree_file_selector()
        self.fd["local_files"].load_downloads_folder_screen()
        self.fd["local_files"].select_file(file)
        self.fd["data_collection_plugin"].select_simplified_ledm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_ledm_tree_test_button()

    def filter_multiple_ledm_trees(self, files):
        if not isinstance(files, list):
            raise ValueError("files parameter must be a list of trees")
        self.fd["data_collection_plugin"].expand_data_collection_method("filterLEDMTrees")
        self.driver.swipe(direction="down")
        self.fd["data_collection_plugin"].select_ledm_tree_file_selector()
        self.fd["local_files"].load_downloads_folder_screen()
        for i, file in enumerate(files):
            self.fd["local_files"].select_file(file, long_press=True)
        self.fd["local_files"].select_select_button()
        self.fd["data_collection_plugin"].select_simplified_ledm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_ledm_tree_test_button()

    def upload_single_notification_file(self, file):
        """
        in webview tab, upload single notification file for sendprebuiltnotification
        """
        self.fd["data_collection_plugin"].select_upload_notification_file_selector()
        self.fd["local_files"].load_downloads_folder_screen()
        self.fd["local_files"].select_list_view_button()
        self.fd["local_files"].select_file(file)

    def upload_multiple_notification_files(self, files):
        """
        in webview tab, upload multiple notification files for sendprebuiltnotification
        """
        if not isinstance(files, list):
            raise ValueError("files parameter must be a list of trees")
        self.fd["data_collection_plugin"].select_upload_notification_file_selector()
        self.fd["local_files"].load_downloads_folder_screen()
        for i, file in enumerate(files):
            self.fd["local_files"].select_file(file, long_press=True)
        self.fd["local_files"].select_select_button()

    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch app
        """
        self.driver.press_key_home()
        self.driver.terminate_app(PACKAGE.JWEB_DATA_COLLECTION)
        self.driver.wdvr.start_activity(PACKAGE.JWEB_DATA_COLLECTION, LAUNCH_ACTIVITY.JWEB_DATA_COLLECTION)

    def select_stack(self, stack_name):
        """
        Selects the stack
        """
        self.fd["data_collection_service"].select_settings_button()
        self.fd["data_collection_settings"].select_data_valve_and_ingress_stack_values(stack_name=stack_name)
        self.fd["home"].select_webview_tab()