import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import *

pytest.app_info = "JWEB_DOC_PROVIDER"

class Test_Suite_01_Doc_Provider(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_jweb_doc_provider_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_doc_provider_setup

        cls.home = cls.fc.fd["home"]
        cls.doc_provider = cls.fc.fd["doc_provider"]
        cls.weblet = cls.fc.fd["weblet"]
        cls.web_doc_provider = cls.fc.fd["web_doc_provider"]
        cls.files = cls.fc.fd["files"]

        cls.b64_text_file = ma_misc.get_abs_path("resources/test_data/jweb/encoded_text_file.B64")

    @pytest.fixture(scope="class", autouse="true")
    def load_necessary_files(self):
        """
        Send 1page.txt to Android Device, and delete file once tests are complete
        """
        self.driver.push_file(ma_misc.get_abs_path("resources/test_data/documents/txt/1page.txt"), "{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, "1page.txt"), overwrite=True)
        yield None
        self.driver.clean_up_device_folder(TEST_DATA.MOBILE_DOWNLOAD)

    def test_01_get_doc_set(self):
        """
        C30414530: Get New Doc Set
            - In the Doc Provider Plugin, create a new empty DocSet
            - Verify DocSet's creation in native portion Doc Provider before deleting DocSet
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.weblet.select_doc_source_button()
        self.web_doc_provider.select_get_result_doc_set_test_btn()
        doc_set_result = self.web_doc_provider.get_result_from_get_doc_set_result_test()
        assert doc_set_result['docs'] == []
        doc_set_id = doc_set_result['id'].upper()
        assert len(doc_set_id) == 36
        self.driver.press_key_back()
        self.home.select_doc_provider_tab()
        assert self.doc_provider.get_doc_set_id() == doc_set_id

    def test_02_add_and_remove_doc_to_result_set(self):
        """ 
        C30414532: Add Doc To Result Doc Set
            - In the Doc Provider Plugin, add txt Doc to DocSet using addDocToResultDocSet()
            - Check txt Doc is added within the native portion of Doc Provider 
        C30414535: Remove Doc From Result Doc Set
            - In removeDocsFromResultDocSet() enter a docSetId and select Test
            - Verify "File(s) removed" message is displayed 
        """
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab()
        self.weblet.select_doc_source_button()
        self.web_doc_provider.enter_file_name_doc_result_textbox("1_page.txt")
        self.web_doc_provider.enter_media_type_doc_result_textbox("txt")
        with open(self.b64_text_file) as file:
            self.web_doc_provider.enter_base_encoded_doc_result_textbox(file.read())
        self.web_doc_provider.select_add_doc_to_result_test_btn()
        add_doc_result = self.web_doc_provider.get_result_from_add_doc_to_result()
        assert add_doc_result['mediaType'] == 'txt'
        assert add_doc_result['fileName'] == '1_page.txt'
        doc_id = add_doc_result['id']
        self.driver.press_key_back()
        self.home.select_doc_provider_tab()
        self.doc_provider.select_docs_button()
        assert self.doc_provider.get_doc_name().lower() == '1_page.txt'
        self.driver.press_key_back()
        self.home.select_weblet_tab()
        self.weblet.select_doc_source_button()
        self.weblet.select_append_button()
        self.web_doc_provider.enter_doc_id_to_remove_from_result_textbox(doc_id)
        self.web_doc_provider.select_remove_doc_from_result_test_btn()
        assert "removed" in self.web_doc_provider.get_result_from_remove_doc_from_result()
        self.driver.press_key_back()
        self.home.select_doc_provider_tab()
        self.doc_provider.select_docs_button()
        assert self.doc_provider.get_doc_name() is False

    def test_03_get_doc_data(self):
        """
        C30414531: Get Result Doc Set
            - In the native Doc Provider tab, create a new DocSet with 1page.txt 
            - In the Doc Provider Plugin, use getDocSet() and docSetId to verify file information
        C30414536: Get Data From Doc Set
            - In the Doc Provider Plugin, use getDocData() and docSetId to verify text file data
        """
        self.fc.flow_load_home_screen()
        self.home.select_doc_provider_tab()
        self.doc_provider.select_services_button()
        self.doc_provider.select_file_system_doc_source_option()
        self.files.load_downloads_folder_screen()
        self.files.select_file("1page.txt", change_check=False)
        doc_set_id = self.doc_provider.get_doc_set_id().lower()
        self.doc_provider.select_docs_button()
        self.doc_provider.select_doc_from_list("1PAGE.TXT")
        doc_info = self.doc_provider.get_doc_info()
        self.driver.press_key_back()
        doc_id = doc_info['id']
        assert doc_info['media_type'] == 'text/plain'
        assert doc_info['filename'] == '1page.txt'
        self.driver.press_key_back()
        self.home.select_weblet_tab()
        self.weblet.select_doc_source_button()
        self.weblet.select_append_button()
        self.web_doc_provider.enter_doc_set_id_text(doc_set_id)
        self.web_doc_provider.select_get_doc_set_test_btn()
        get_doc_set_result = self.web_doc_provider.get_result_from_get_doc_set_test()
        assert get_doc_set_result['docs'][0]['fileName'] == '1page.txt'
        assert get_doc_set_result['docs'][0]['id'] == doc_id
        self.web_doc_provider.enter_doc_id_get_doc_data_textbox(doc_id)
        self.web_doc_provider.enter_doc_set_id_get_doc_data_textbox(doc_set_id)
        self.web_doc_provider.select_get_doc_data_test_btn()
        doc_data_result = self.web_doc_provider.get_result_from_get_doc_data_test()
        with open(self.b64_text_file) as file:
            assert doc_data_result['data'] == file.read()
        assert doc_data_result['docId'] == doc_id
        assert doc_data_result['docSetId'] == doc_set_id