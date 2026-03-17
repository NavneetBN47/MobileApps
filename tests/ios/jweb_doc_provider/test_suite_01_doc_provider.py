import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import BUNDLE_ID

pytest.app_info = "JWEB_DOC_PROVIDER"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_doc_provider_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_doc_provider_setup

        # Define flows
        cls.home = cls.fc.fd["home"] 
        cls.files = cls.fc.fd["files"] 
        cls.doc_provider = cls.fc.fd["doc_provider"]
        cls.weblet = cls.fc.fd["weblet"]
        cls.web_doc_provider = cls.fc.fd["web_doc_provider"]

        cls.b64_text_file = ma_misc.get_abs_path("resources/test_data/jweb/encoded_text_file.B64")
        cls.b64_png_file = ma_misc.get_abs_path("resources/test_data/jweb/encoded_png_file.B64")

    @pytest.fixture(scope="class", autouse="true")
    def load_necessary_files(self):
        """
        Send 1page.txt to iPhone, and delete file once tests are complete
        """
        if self.driver.push_file(BUNDLE_ID.FIREFOX, ma_misc.get_abs_path("resources/test_data/documents/txt/1page.txt")) is False: 
            raise Exception("Failed to push file {} to {}".format("1page.txt", BUNDLE_ID.FIREFOX))
        yield None
        self.driver.delete_file(BUNDLE_ID.FIREFOX, "1page.txt")

    def test_01_get_doc_set(self):
        """
        C30414530: Get New Doc Set
            - In the Doc Provider Plugin, create a new empty DocSet
            - Verify DocSet's creation in native portion Doc Provider before deleting DocSet
        """
        self.home.select_weblet_tab()
        self.weblet.select_file_system_doc_source_button()
        self.web_doc_provider.select_get_result_doc_set_test_btn()
        doc_set_result = self.web_doc_provider.get_result_from_get_doc_set_result_test()
        assert doc_set_result['docs'] == []
        doc_set_id = doc_set_result['id']
        assert len(doc_set_id) == 36
        self.files.select_done()
        self.home.select_doc_provider_tab()
        assert self.doc_provider.get_doc_set_id() == doc_set_id        
        self.doc_provider.delete_doc_set()

    def test_02_add_doc_to_result_set(self):
        """ 
        C30414532: Add Doc To Result Doc Set
            - In the Doc Provider Plugin, add txt Doc to DocSet using addDocToResultDocSet()
            - Check txt Doc is added within the native portion of Doc Provider 
        """
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
        self.files.select_done()
        self.home.select_doc_provider_tab()
        self.doc_provider.select_docs_button()
        assert self.doc_provider.get_doc_name() == '1_page.txt'
        self.doc_provider.select_back_from_docs()
        self.doc_provider.delete_doc_set()

    def test_03_remove_doc_from_result_set(self):
        """
        C30414535: Remove Doc From Result Doc Set
            - In the Doc Provider Plugin, add png Doc to DocSet
            - In removeDocsFromResultDocSet() enter a docSetId and select Test
            - Verify "File(s) removed" message is displayed 
        """
        self.home.select_weblet_tab()
        self.weblet.select_doc_source_button()
        self.web_doc_provider.enter_file_name_doc_result_textbox("hp_logo.png")
        self.web_doc_provider.enter_media_type_doc_result_textbox("png")
        with open(self.b64_png_file) as file:
            self.web_doc_provider.enter_base_encoded_doc_result_textbox(file.read(), split_text=True)
        self.web_doc_provider.select_add_doc_to_result_test_btn()
        add_doc_result = self.web_doc_provider.get_result_from_add_doc_to_result()
        doc_id = add_doc_result['id']
        self.web_doc_provider.enter_doc_id_to_remove_from_result_textbox(doc_id)
        self.web_doc_provider.select_remove_doc_from_result_test_btn()
        assert "removed" in self.web_doc_provider.get_result_from_remove_doc_from_result()
        self.files.select_done()
        self.home.select_doc_provider_tab()
        assert 0 == self.doc_provider.get_doc_count()
        self.doc_provider.delete_doc_set()
        
    def test_04_get_doc_data(self):
        """
        C30414531: Get Result Doc Set
            - In the native Doc Provider tab, create a new DocSet with 1page.txt 
            - In the Doc Provider Plugin, use getDocSet() and docSetId to verify file information
        C30414536: Get Data From Doc Set
            - In the Doc Provider Plugin, use getDocData() and docSetId to verify text file data
        """
        self.home.select_doc_provider_tab()
        self.doc_provider.select_services_button()
        self.doc_provider.select_file_system_doc_source_option()
        self.files.navigate_to_application_folder('Firefox')
        self.files.select_item_cell('1page', scroll=True)
        self.files.select_open_file_btn(raise_e=False)
        doc_set_id = self.doc_provider.get_doc_set_id()
        self.doc_provider.select_docs_button()
        self.doc_provider.select_doc_from_list("1page.txt")
        doc_info = self.doc_provider.get_doc_info()
        doc_id = doc_info['id']
        assert doc_info['media_type'] == 'text/plain'
        assert doc_info['filename'] == '1page.txt'
        self.files.select_done()
        self.doc_provider.select_back_from_docs()
        self.home.select_weblet_tab()
        self.weblet.select_file_system_doc_source_button()
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
        self.files.select_done()
        self.home.select_doc_provider_tab()
        self.doc_provider.delete_doc_set()
        self.doc_provider.delete_doc_set()