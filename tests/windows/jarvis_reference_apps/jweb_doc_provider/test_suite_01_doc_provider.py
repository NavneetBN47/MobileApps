import pytest
import json
from MobileApps.libs.ma_misc import ma_misc
from time import sleep

pytest.app_info = "JWEB_DOC_PROVIDER"

class Test_Suite_01_Data_Collection_Services(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, jweb_doc_provider_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_doc_provider_test_setup
        cls.home = cls.fc.fd["home"]
        cls.doc_provider_plugin = cls.fc.fd["doc_provider_plugin"]
        cls.files = cls.fc.fd["files"]
        cls.b64_text_file = ma_misc.get_abs_path("resources/test_data/jweb/encoded_text_file.B64")
        
        cls.home.click_maximize()
        cls.driver.ssh.send_file(ma_misc.get_abs_path("resources/test_data/documents/txt/1page.txt"), "/Users/exec/Downloads/1page.txt")
        yield None
        cls.driver.ssh.remove_file_with_suffix("/Users/exec/Downloads/", ".txt")

    def test_01_get_doc_set(self):
        """
        C30414530: Get New Doc Set
            - In the Doc Provider Plugin, create a new empty DocSet
            - Verify DocSet's creation in native portion Doc Provider before deleting DocSet
        """
        self.fc.load_doc_source_weblet()
        self.doc_provider_plugin.select_get_result_doc_set_test_btn()
        doc_set_result = self.doc_provider_plugin.get_result_from_get_doc_set_result_test()
        assert doc_set_result['docs'] == [], "DocSet not empty"
        doc_set_id = doc_set_result['id']
        assert len(doc_set_id) == 36, "DocSet ID not 36 characters"
        self.doc_provider_plugin.select_navigate_back_btn()
        assert self.home.get_doc_set_id() == doc_set_id, "DocSet ID not found in Doc Provider"

    def test_02_add_and_remove_doc_to_result_set(self):
        """ 
        C30414532: Add Doc To Result Doc Set
            - In the Doc Provider Plugin, add txt Doc to DocSet using addDocToResultDocSet()
            - Check txt Doc is added within the native portion of Doc Provider 
        C30414535: Remove Doc From Result Doc Set
            - In removeDocsFromResultDocSet() enter a docSetId and select Test
            - Verify "File(s) removed" message is displayed 
        """
        self.fc.load_doc_source_weblet()
        self.doc_provider_plugin.enter_file_name_doc_result_textbox("1_page.txt")
        self.doc_provider_plugin.enter_media_type_doc_result_textbox("txt")
        with open(self.b64_text_file) as file:
            self.doc_provider_plugin.enter_base_encoded_doc_result_textbox(file.read())
        self.doc_provider_plugin.select_add_doc_to_result_test_btn()
        add_doc_result = self.doc_provider_plugin.get_result_from_add_doc_to_result()
        assert add_doc_result['mediaType'] == 'txt', "Media type not txt"
        assert add_doc_result['fileName'] == '1_page.txt', "File name not 1_page.txt"
        doc_id = add_doc_result['id']
        self.doc_provider_plugin.select_navigate_back_btn()
        assert '1_page.txt' in self.home.get_doc_info(), "1_page.txt not found in newly created Docs:"
        self.fc.load_doc_source_weblet(reset_app=False)
        self.home.select_use_selected_doc_set()
        self.doc_provider_plugin.enter_doc_id_to_remove_from_result_textbox(doc_id)
        self.doc_provider_plugin.select_remove_doc_from_result_test_btn()
        assert "removed" in self.doc_provider_plugin.get_result_from_remove_doc_from_result(), "Doc not removed"
        self.doc_provider_plugin.select_navigate_back_btn()
        assert not self.home.get_doc_info(raise_e=False), "Doc not removed from Doc Provider"

    def test_03_get_doc_data(self):
        """
        C30414531: Get Result Doc Set
            - In the native Doc Provider tab, create a new DocSet with 1page.txt 
            - In the Doc Provider Plugin, use getDocSet() and docSetId to verify file information
        C30414536: Get Data From Doc Set
            - In the Doc Provider Plugin, use getDocData() and docSetId to verify text file data
        """
        self.fc.load_doc_source_weblet(enable_launch_as_web_service=False)
        self.home.select_add_document()
        self.files.click_downloads_list_item()
        self.files.send_text_file_name_textbox("1page.txt")
        self.files.click_open_btn()
        self.home.select_close_btn()
        doc_set_info = self.home.get_doc_info()
        assert '1page.txt' in doc_set_info, "1page.txt not found in newly created Docs:"
        one_page_txt_doc_id = doc_set_info.split(":")[0].lower()
        doc_set_id = self.home.get_doc_set_id()
        self.fc.load_doc_source_weblet(reset_app=False)
        self.home.select_use_selected_doc_set()
        self.doc_provider_plugin.enter_doc_set_id_text(doc_set_id)
        self.doc_provider_plugin.select_get_doc_set_test_btn()
        get_doc_set_result = self.doc_provider_plugin.get_result_from_get_doc_set_test()
        assert get_doc_set_result['docs'][0]['id'] == one_page_txt_doc_id, f"1page.txt Doc ID not found in {get_doc_set_result['docs']}"
        assert get_doc_set_result['docs'][0]['fileName'] == '1page.txt', f"1page.txt not found in {get_doc_set_result['docs']}"
        assert get_doc_set_result['docs'][0]['mediaType'] == 'text/plain', f"1page.txt mediaType not found in {get_doc_set_result['docs']}"
        self.doc_provider_plugin.enter_doc_id_get_doc_data_textbox(one_page_txt_doc_id)
        self.doc_provider_plugin.enter_doc_set_id_get_doc_data_textbox(doc_set_id)
        self.doc_provider_plugin.select_get_doc_data_test_btn()
        doc_data_result = self.doc_provider_plugin.get_result_from_get_doc_data_test()
        with open(self.b64_text_file) as file:
            assert doc_data_result['data'] == file.read(), "1page.txt data does not match stored data"
        assert doc_data_result['docId'] == one_page_txt_doc_id, "Doc ID not found"
        assert doc_data_result['docSetId'] == doc_set_id, "Doc Set ID not found"
