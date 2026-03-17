import json

from MobileApps.libs.flows.windows.jweb_doc_provider.jweb_doc_provider_flow import JwebDocProviderFlow

class DocProviderPlugin(JwebDocProviderFlow):
    flow_name = "doc_provider_plugin"

    def swipe_to_object(self, obj, direction="down"):
        """
        Within Data Collection Plugin, swipe to an object given a direction
        """
        for _ in range(10):
            if not self.driver.wait_for_object(obj, raise_e=False, timeout=1):
                self.driver.swipe(anchor_element="doc_provider_header", direction=direction)
            else:
                return True
        else:
            return False

    def select_navigate_back_btn(self, raise_e=True):
        """
        Selects the back arrow button in the top left of the window
        """
        self.driver.click("navigate_back_btn", raise_e=raise_e)

    def select_get_result_doc_set_test_btn(self):
        """
        in getResultDocSet(), select the test button which returns a the result DocSet
        """
        self.swipe_to_object("get_result_doc_set_test_btn")
        self.driver.click("get_result_doc_set_test_btn")

    def get_result_from_get_doc_set_result_test(self):
        """
        in getResultDocSet(), return the json after selecting the test button
        """
        return json.loads(self.driver.get_attribute("get_result_doc_set_result", "text", displayed=False))

    def enter_file_name_doc_result_textbox(self, text):
        """
        in addDocToResultDocSet(), enter text into fileName textbox
        """
        self.swipe_to_object("file_name_doc_result_textbox")
        self.driver.send_keys("file_name_doc_result_textbox", text)

    def enter_media_type_doc_result_textbox(self, text):
        """
        in addDocToResultDocSet(), enter text into mediaType textbox
        """
        self.swipe_to_object("media_type_doc_result_textbox")
        self.driver.send_keys("media_type_doc_result_textbox", text)

    def enter_base_encoded_doc_result_textbox(self, text, split_text=False):
        """
        in addDocToResultDocSet(), enter Base64-encoded doc content into Base64 textbox
        """
        self.swipe_to_object("base_encoded_doc_result_textbox")
        self.driver.send_keys("base_encoded_doc_result_textbox", text)

    def select_add_doc_to_result_test_btn(self):
        """
        in addDocToResultDocSet(), select the test button adding doc to the result DocSet
        """
        self.driver.click("add_doc_to_result_test_btn")

    def get_result_from_add_doc_to_result(self):
        """
        in addDocToResultDocSet(), return the json after selecting the test button
        """
        return json.loads(self.driver.get_attribute("get_result_add_doc_to_result_doc_set", "text", displayed=False))

    def enter_doc_id_to_remove_from_result_textbox(self, text):
        """
        in removeDocsFromResultDocSet(), enter text into docIds textbox
        """
        self.driver.send_keys("remove_docs_from_result_textbox", text)

    def select_remove_doc_from_result_test_btn(self):
        """
        in removeDocsFromResultDocSet(), select the test button removing docs to the result DocSet
        """
        self.swipe_to_object("remove_docs_from_result_test_btn")
        self.driver.click("remove_docs_from_result_test_btn")

    def get_result_from_remove_doc_from_result(self):
        """
        in removeDocsFromResultDocSet(), return the Result text found after clicking the test button 
        """
        return self.driver.get_attribute("get_remove_docs_from_doc_set_result_text", "text", displayed=False)

    def enter_doc_set_id_text(self, text):
        """
        in getDocSet(), enter text into the docSetId textbox
        """
        self.swipe_to_object("doc_set_id_textbox", direction="up")
        self.driver.send_keys("doc_set_id_textbox", text)

    def select_get_doc_set_test_btn(self):
        """
        in getDocSet(), select the test button which returns a requested DocSet 
        """
        self.driver.click("get_doc_set_test_btn")

    def get_result_from_get_doc_set_test(self):
        """
        in getDocSet(), return the json after selecting the test button
        """
        return json.loads(self.driver.get_attribute("get_doc_set_result", "text", displayed=False))

    def enter_doc_id_get_doc_data_textbox(self, text):
        """
        in getDocData(), enter text into docId textbox
        """
        self.swipe_to_object("get_doc_data_doc_id_textbox", direction="down")
        self.driver.send_keys("get_doc_data_doc_id_textbox", text)

    def enter_doc_set_id_get_doc_data_textbox(self, text):
        """
        in getDocData(), enter text into docSetId textbox
        """
        self.swipe_to_object("get_set_id_data_doc_id_textbox", direction="down")
        self.driver.send_keys("get_set_id_data_doc_id_textbox", text)

    def select_get_doc_data_test_btn(self):
        """
        in getDocData(), select the test button retrieving the Doc data
        """
        self.swipe_to_object("get_doc_data_test_btn", direction="down")
        self.driver.click("get_doc_data_test_btn")

    def get_result_from_get_doc_data_test(self):
        """
        in getDocData(), return Result json result after selecting the test button
        """
        return json.loads(self.driver.get_attribute("get_doc_data_result_text", "text", displayed=False))