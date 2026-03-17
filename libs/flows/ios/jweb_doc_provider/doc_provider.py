import re

from MobileApps.libs.flows.ios.jweb_doc_provider.jweb_doc_provider_flow import JwebDocProviderFlow

class DocProvider(JwebDocProviderFlow):
    flow_name = "doc_provider"

    def select_services_button(self):
        """
        Selects the services button in the top right of the Doc Provider page
        """
        self.driver.click("services_btn")

    def select_file_system_doc_source_option(self):
        """ 
        After clicking Services button, select FileSystemDocSource service
        """
        self.driver.click("file_system_doc_source_option")

    def select_doc_transformer_option(self):
        """ 
        After clicking Services button, select DocTransformer service
        """
        self.driver.click("doc_transformer_option")

    def select_doc_destination_option(self):
        """ 
        After clicking Services button, select DocDestination service
        """
        self.driver.click("doc_destination_option")

    def select_docs_button(self):
        """
        Select the Docs button for the first DocSet in the list
        """
        self.driver.click("docs_button")

    def get_doc_name(self):
        """
        Returns the str value of the first document name in the DocSet 
        """
        return self.driver.wait_for_object("doc_item", format_specifier=["."]).text

    def select_doc_from_list(self, doc_name):
        """
        Select the doc via doc_name after selecting the docs button for a DocSet
        """
        self.driver.click("doc_item", format_specifier=[doc_name])

    def get_doc_info(self):
        """
        After selecting on a doc within the docset, return resulting data as json
        """
        result_str, result_dict = self.driver.wait_for_object("doc_item_data").text.split("\n"), {}
        for r in result_str:
            key, value = r.split(":")
            key = key.lower().replace(" ", "_")
            result_dict[key] = value.lstrip()
        return result_dict

    def select_back_from_docs(self):
        """
        Return to Doc Provider page after selecting Docs button
        """
        self.driver.click("return_docs_button")

    def get_doc_set_id(self):
        """
        Returns the DocSet id of the first DocSet in the list 
        """
        return self.driver.wait_for_object("doc_set").get_attribute('value').split(' ')[-1]

    def get_doc_count(self):
        """
        Returns the number of documents from the first DocSet in the list
        """
        return int(re.sub("[^0-9]", "", self.driver.wait_for_object("doc_set_document_count").text))

    def delete_doc_set(self):
        """
        Deletes the first DocSet in the list
        """
        self.driver.swipe(swipe_object='doc_set', direction='right')
        self.driver.click("delete_button")