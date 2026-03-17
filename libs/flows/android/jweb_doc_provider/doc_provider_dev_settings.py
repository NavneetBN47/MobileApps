from MobileApps.libs.flows.android.jweb_doc_provider.jweb_doc_provider_flow import JwebDocProviderFlow
from MobileApps.resources.const.android.const import PACKAGE, LAUNCH_ACTIVITY

class DocProviderDevSettings(JwebDocProviderFlow):
    flow_name = "doc_provider_dev_settings"

    def open_select_settings_page(self):
        """
        Launch Select Settings Page Screen
        """
        self.driver.start_activity(PACKAGE.JWEB_DOC_PROVIDER, LAUNCH_ACTIVITY.JWEB_DOC_PROVIDER_DEV_SETTINGS)

    def select_stack(self, stack):
        """
        Set JWeb Doc Provider App to Stack to :stack:
        """
        stack = stack.title()
        if stack not in ["Production", "Stage", "Pie", "Dev"]:
            raise ValueError("Stack must be one of Production, Stage, Pie, or Dev. Received: {}".format(stack))
        self.driver.scroll("server_stack_btn", click_obj=True)
        self.driver.click("stack_option", format_specifier=[stack])