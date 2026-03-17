import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.resources.const.windows.const import CONSENT_PARAGRAPH_COPY

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression", "function_setup_to_reset_and_launch_myhp")
class Test_Suite_06_App_Consents(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.app_consents = request.cls.fc.fd["app_consents"]
        request.cls.fc.change_system_region_to_united_states()
        yield
        request.cls.fc.change_system_region_to_united_states()

    @pytest.mark.app_consents
    def test_01_verify_paragraph_1_basic_data_collection_text_C80186817(self):
        expected_text = CONSENT_PARAGRAPH_COPY.CONSENT_PARA_1
        actual_text = self.app_consents.get_paragraph_1_basic_data_collection_text()
        assert actual_text == expected_text, "Paragraph 1 basic data collection consent text mismatch."

    @pytest.mark.app_consents
    def test_02_verify_paragraph_2_optional_data_collection_text_C80186822(self):
        expected_text = CONSENT_PARAGRAPH_COPY.CONSENT_PARA_2
        actual_text = self.app_consents.get_paragraph_2_optional_data_collection_text()
        assert actual_text == expected_text, "Paragraph 2 optional data collection consent text mismatch."

    @pytest.mark.app_consents
    def test_03_verify_paragraph_3_accept_all_text_C80186830(self):
        expected_text = CONSENT_PARAGRAPH_COPY.CONSENT_PARA_3
        actual_text = self.app_consents.get_paragraph_3_accept_all_text()
        assert actual_text == expected_text, "Paragraph 3 accept all consent text mismatch."

    @pytest.mark.app_consents
    def test_04_verify_paragraph_4_manage_choices_text_C80186838(self):
        expected_text = CONSENT_PARAGRAPH_COPY.CONSENT_PARA_4
        actual_text = self.app_consents.get_paragraph_4_manage_choices_text()
        assert actual_text == expected_text, "Paragraph 4 manage choices guidance text mismatch."

    @pytest.mark.app_consents
    def test_05_verify_paragraph_5_privacy_update_text_C80186846(self):
        expected_text = CONSENT_PARAGRAPH_COPY.CONSENT_PARA_5
        actual_text = self.app_consents.get_paragraph_5_privacy_update_text()
        assert actual_text == expected_text, "Paragraph 5 privacy update reminder text mismatch."


