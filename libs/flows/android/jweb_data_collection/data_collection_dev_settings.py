from MobileApps.libs.flows.android.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow
from MobileApps.resources.const.android.const import PACKAGE, LAUNCH_ACTIVITY

class DataCollectionDevSettings(JwebDataCollectionFlow):
    flow_name = "data_collection_dev_settings"

    def open_select_settings_page(self):
        """
        Launch Select Settings Page Screen
        """
        self.driver.start_activity(PACKAGE.JWEB_DATA_COLLECTION, LAUNCH_ACTIVITY.JWEB_DATA_COLLECTION_DEV_SETTINGS)

    def check_log_unloggables_toggle(self, value=True):
        """
        Set Log Unloggables toggle to :value: 
        """
        self.driver.check_box("log_unloggables_toggle", uncheck=not value)

    def select_stack(self, stack):
        """
        Set JWeb Data Collection App to Stack to :stack: Production Stack not supported via Automation
        """
        stack = stack.title()
        if stack not in ["Stage", "Pie", "Dev"]:
            raise ValueError("Stack must be one of Stage, Pie, or Dev. Received: {}".format(stack))
        self.driver.scroll("server_stack_btn", click_obj=True)
        self.driver.click("stack_option", format_specifier=[stack])