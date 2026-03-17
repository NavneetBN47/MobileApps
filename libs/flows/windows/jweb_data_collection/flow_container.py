import json
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.jweb_data_collection.home import Home
from MobileApps.libs.flows.windows.jweb_data_collection.files import Files
from MobileApps.libs.flows.windows.jweb_data_collection.settings import Settings
from MobileApps.libs.flows.windows.jweb_data_collection.bindings_cache import BindingsCache
from MobileApps.libs.flows.windows.jweb_data_collection.request import Request
from MobileApps.libs.flows.windows.jweb_data_collection.verbose_logs import VerboseLogs
from MobileApps.libs.flows.windows.jweb_data_collection.data_collection_plugin import DataCollectionPlugin
from MobileApps.libs.flows.windows.jweb_data_collection.value_store import ValueStore

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "files": Files(driver),
                   "settings": Settings(driver),
                   "bindings_cache": BindingsCache(driver),
                   "request": Request(driver),
                   "verbose_logs": VerboseLogs(driver),
                   "value_store": ValueStore(driver),
                    "data_collection_plugin": DataCollectionPlugin(driver)}

    @property
    def flow(self):
        return self.fd
    
    def get_data_collection_test_data(self, stack):
        """
        Get data collection test data based on stack
        :param stack: stack of the test data
        :return: test data
        """
        stack = stack.lower()
        if stack == "staging":
            stack = "stage"
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

    def filter_cdm_tree(self, file, tree):
        """
        in DataCollection, filter and test a cdm tree
        """
        self.fd["data_collection_plugin"].select_cdm_file_tree_selector()
        self.fd["files"].click_downloads_list_item()
        self.fd["files"].send_text_file_name_textbox(file)
        self.fd["files"].click_open_btn()
        self.fd["data_collection_plugin"].swipe_to_object('cdm_tree_gun_textbox')
        self.fd["data_collection_plugin"].send_text_to_textbox('cdm_tree_gun_textbox', tree)
        self.fd["data_collection_plugin"].select_simplified_cdm_tree_result_checkbox(True)
        self.driver.swipe(direction="down")
        self.fd["data_collection_plugin"].select_filter_cdm_tree_test_button()

    def filter_multiple_cdm_trees(self, files, tree='com.hp.cdm.service.eventing.version.1.resource.notification,com.hp.cdm.service.eventing.version.1.resource.notification'):
        """
        in DataCollection, filter and test a multiple cdm trees
        """
        self.fd["data_collection_plugin"].select_cdm_file_tree_selector()
        self.fd["files"].click_downloads_list_item()
        self.fd["files"].send_text_file_name_textbox(' '.join(['"{}"'.format(file) for file in files]))
        self.fd["files"].click_open_btn()
        self.fd["data_collection_plugin"].swipe_to_object('cdm_tree_gun_textbox')
        self.fd["data_collection_plugin"].send_text_to_textbox('cdm_tree_gun_textbox', tree)
        self.fd["data_collection_plugin"].select_simplified_cdm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_cdm_tree_test_button()

    def filter_ledm_tree(self, file, uri):
        """
        in DataCollection, filter and test a ledm tree
        """
        self.fd["data_collection_plugin"].select_ledm_file_tree_selector()
        self.fd["files"].click_downloads_list_item()
        self.fd["files"].send_text_file_name_textbox(file)
        self.fd["files"].click_open_btn()
        self.fd["data_collection_plugin"].send_text_to_textbox('resource_uri_textbox', uri)
        self.fd["data_collection_plugin"].select_simplified_ledm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_ledm_tree_test_button()

    def filter_multiple_ledm_trees(self, files, uri='/DevMgmt/ProductConfigDyn.xml,/DevMgmt/ProductConfigDyn.xml'):
        """
        in DataCollection, filter and test a multiple ledm trees
        """
        self.fd["data_collection_plugin"].select_ledm_file_tree_selector()
        self.fd["files"].click_downloads_list_item()
        self.fd["files"].send_text_file_name_textbox(' '.join(['"{}"'.format(file) for file in files]))
        self.fd["files"].click_open_btn()
        self.fd["data_collection_plugin"].send_text_to_textbox('resource_uri_textbox', uri)
        self.fd["data_collection_plugin"].select_simplified_ledm_tree_result_checkbox(True)
        self.fd["data_collection_plugin"].select_filter_ledm_tree_test_button()

    def upload_single_notification_file(self, file):
        """
        in DataCollection, upload single notification file for sendprebuiltnotification
        """
        self.fd["data_collection_plugin"].select_upload_notification_file_selector()
        self.fd["files"].click_downloads_list_item()
        self.fd["files"].send_text_file_name_textbox(file)
        self.fd["files"].click_open_btn()

    def upload_multiple_notification_files(self, files):
        """
        in DataCollection, upload multiple notification files for sendprebuiltnotification
        """
        self.fd["data_collection_plugin"].select_upload_notification_file_selector()
        self.fd["files"].click_downloads_list_item()
        self.fd["files"].send_text_file_name_textbox(' '.join(['"{}"'.format(file) for file in files]))
        self.fd["files"].click_open_btn()

    def select_stack(self, stack):
        """
        in DataCollection, select stack
        """
        self.fd["home"].select_webview_engine("webview1_edge_engine")
        self.fd["home"].select_top_nav_button("settings_nav_btn")
        self.fd["settings"].disable_use_batching_policy_toggle(False)
        self.fd["settings"].select_data_valve_and_ingress_stack_values(valve_stack=stack, ingress_stack=stack)
        self.fd["home"].select_top_nav_button("weblet_page_nav_btn")

    def handle_toggle(self):
        """
        in DataCollection, handle toggle
        """
        self.fd["data_collection_plugin"].enable_use_custommetdatavalue_toggle(True)
        self.fd["settings"].disable_use_batching_policy_toggle(True)
        self.fd["settings"].enable_use_custom_batching_policy_toggle(True)
        self.fd["settings"].enable_verbose_logs_toggle(True)
        self.fd["settings"].click_settings_savebtn()
        self.fd["settings"].click_settings_closebtn()
