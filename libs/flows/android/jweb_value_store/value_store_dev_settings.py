from MobileApps.libs.flows.android.jweb_value_store.jweb_value_store_flow import JwebValueStoreFlow
from MobileApps.resources.const.android.const import PACKAGE, LAUNCH_ACTIVITY

class ValueStoreDevSettings(JwebValueStoreFlow):
    flow_name = "value_store_dev_settings"

    def open_select_settings_page(self):
        """
        Launch Select Settings Page Screen
        """
        self.driver.start_activity(PACKAGE.JWEB_VALUE_STORE, LAUNCH_ACTIVITY.JWEB_VALUE_STORE_DEV_SETTINGS)

    def check_log_unloggables_toggle(self, value=True):
        """
        Set Log Unloggables toggle to :value: 
        """
        self.driver.check_box("log_unloggables_toggle", uncheck=not value)

    def select_stack(self, stack):
        """
        Set JWeb Value Store App to Stack to :stack:
        """
        stack = stack.title()
        if stack not in ["Production", "Stage", "Pie", "Dev"]:
            raise ValueError("Stack must be one of Production, Stage, Pie, or Dev. Received: {}".format(stack))
        self.driver.scroll("server_stack_btn", click_obj=True)
        self.driver.click("stack_option", format_specifier=[stack])