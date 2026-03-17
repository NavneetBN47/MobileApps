from abc import ABCMeta
from MobileApps.libs.flows.windows.windows_flow import WindowsFlow
from MobileApps.libs.ma_misc import ma_misc
import logging


class HPXRebrandingFlow(WindowsFlow):
    __metaclass__ = ABCMeta
    project = "hpx_rebranding"

    def __init__(self,driver):
        super(HPXRebrandingFlow, self).__init__(driver)
        self.load_hpx_app_shared_ui

    def load_hpx_app_shared_ui(self):
        ui_map = self.load_ui_map(system="WINDOWS", project="hpx_rebranding", flow_name="shared_obj")
        self.driver.load_ui_map("hpx_rebranding", "shared_obj", ui_map)
        return True

    def clean_paragraph_text(self, text_value):
        if text_value is None:
            return ""
        return str(text_value).strip()

    def append_paragraph_segment(self, combined_text, segment_text):
        cleaned_combined_text = self.clean_paragraph_text(combined_text)
        cleaned_segment_text = self.clean_paragraph_text(segment_text)

        if not cleaned_segment_text:
            return cleaned_combined_text
        if not cleaned_combined_text:
            return cleaned_segment_text
        if cleaned_segment_text[0] in ",.;:!?\"'":
            return f"{cleaned_combined_text}{cleaned_segment_text}"
        return f"{cleaned_combined_text} {cleaned_segment_text}"

    def get_paragraph_text(self, locator_key, timeout=20):
        element = self.driver.wait_for_object(locator_key, timeout=timeout)
        return self.clean_paragraph_text(element.get_attribute("Name"))

    def get_combined_paragraph_text(self, locator_keys):
        combined_text = ""
        for locator_key in locator_keys:
            segment_text = self.get_paragraph_text(locator_key)
            combined_text = self.append_paragraph_segment(combined_text, segment_text)
        return self.clean_paragraph_text(combined_text)