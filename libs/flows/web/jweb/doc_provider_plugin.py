import json
from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

class DocProviderPlugin(JwebFlow):
    flow_name = "doc_provider_plugin"

    def expand_doc_provider_method(self, method, expand=False):
        """
        Select the doc provider method to expand or contract the method view 
        :param method: method name to expand. Must be present within list below
        :param expand: if we should expand or contract the method view 
        """
        if method not in ["getDocSetItem", "getResultDocSetItem", "addDocToResultDocSetItem", "addDocsToResultDocSetItem", "removeDocsFromResultDocSetItem", "getDocDataFromDocDataItem"]:
            raise Exception
        if str(expand).lower() != self.driver.wait_for_object("doc_provider_method", format_specifier=[method]).get_attribute('aria-expanded'):
            self.driver.click("doc_provider_method", format_specifier=[method])

    def enter_doc_set_id_text(self, text):
        """
        in getDocSet(), enter text into the docSetId textbox
        """
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
        return json.loads(self.driver.get_attribute("get_doc_set_result", "text"))
    
    def select_get_result_doc_set_test_btn(self):
        """
        in getResultDocSet(), select the test button which returns a the result DocSet
        """
        self.driver.click("get_result_doc_set_test_btn")

    def get_result_from_get_doc_set_result_test(self):
        """
        in getResultDocSet(), return the json after selecting the test button
        """
        return json.loads(self.driver.get_attribute("get_result_doc_set_result", "text"))

    def enter_file_name_doc_result_textbox(self, text):
        """
        in addDocToResultDocSet(), enter text into fileName textbox
        """
        self.driver.selenium.js_clear_text("file_name_doc_result_textbox")
        self.driver.send_keys("file_name_doc_result_textbox", text)

    def enter_media_type_doc_result_textbox(self, text):
        """
        in addDocToResultDocSet(), enter text into mediaType textbox
        """
        self.driver.selenium.js_clear_text("media_type_doc_result_textbox")
        self.driver.send_keys("media_type_doc_result_textbox", text)

    def enter_base_encoded_doc_result_textbox(self, text, split_text=False):
        """
        :split_text: send_keys() of text value in two chunks
        in addDocToResultDocSet(), enter Base64-encoded doc content into Base64 textbox
        """
        self.driver.selenium.js_clear_text("base_encoded_doc_result_textbox")
        if not split_text:
            self.driver.send_keys("base_encoded_doc_result_textbox", text)
        else:
            self.driver.send_keys("base_encoded_doc_result_textbox", text[:int(len(text)/2)])
            self.driver.send_keys("base_encoded_doc_result_textbox", text[int(len(text)/2):], clear_text=False)

    def select_add_doc_to_result_test_btn(self):
        """
        in addDocToResultDocSet(), select the test button adding doc to the result DocSet
        """
        self.driver.click("add_doc_to_result_test_btn")

    def get_result_from_add_doc_to_result(self):
        """
        in addDocToResultDocSet(), return the json after selecting the test button
        """
        return json.loads(self.driver.get_attribute("get_result_add_doc_to_result_doc_set", "text"))

    def enter_new_docs_path_textbox(self, text):
        """
        in addDocsToResultDocSet(), enter text into newDocsPaths textbox
        """
        self.driver.send_keys("add_docs_path_result_textbox", text)

    def select_add_docs_to_result_test_btn(self):
        """
        in addDocsToResultDocSet(), select the test button adding docs to the result DocSet
        """
        self.driver.click("add_docs_to_result_test_btn")

    def enter_doc_id_to_remove_from_result_textbox(self, text):
        """
        in removeDocsFromResultDocSet(), enter text into docIds textbox
        """
        self.driver.send_keys("remove_docs_from_result_textbox", text)

    def select_remove_doc_from_result_test_btn(self):
        """
        in removeDocsFromResultDocSet(), select the test button removing docs to the result DocSet
        """
        self.driver.click("remove_docs_from_result_test_btn")

    def get_result_from_remove_doc_from_result(self):
        """
        in removeDocsFromResultDocSet(), return the Result text found after clicking the test button 
        """
        return self.driver.get_attribute("get_remove_docs_from_doc_set_result_text", "text")

    def enter_doc_id_get_doc_data_textbox(self, text):
        """
        in getDocData(), enter text into docId textbox
        """
        self.driver.send_keys("get_doc_data_doc_id_textbox", text)

    def enter_doc_set_id_get_doc_data_textbox(self, text):
        """
        in getDocData(), enter text into docSetId textbox
        """
        self.driver.send_keys("get_set_id_data_doc_id_textbox", text)

    def select_get_doc_data_test_btn(self):
        """
        in getDocData(), select the test button retrieving the Doc data
        """
        self.driver.click("get_doc_data_test_btn")

    def get_result_from_get_doc_data_test(self):
        """
        in getDocData(), return Result json result after selecting the test button
        """
        return json.loads(self.driver.get_attribute("get_doc_data_result_text", "text"))
