import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression","function_setup_myhp_launch")
class Test_Suite_01_Device_List(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        request.cls.fc.kill_hpx_process()
        request.cls.fc.kill_chrome_process()
        cls.profile= request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        request.cls.fc.web_password_credential_delete()
        cls.profile.minimize_chrome()

    @pytest.mark.regression
    @pytest.mark.ota
    @pytest.mark.smoke
    def test_01_verify_ui_of_device_details_page_C53303928(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=True)
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up()
        self.devices_details_pc_mfe.click_back_devices_button()
        assert self.devicesMFE.verify_device_card_show_up(raise_e=True)

    @pytest.mark.regression
    @pytest.mark.ota
    @pytest.mark.smoke
    def test_02_verify_nick_name_mycomputer_displayed_correctly_C53303929(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=True)
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up()
        self.devices_details_pc_mfe.click_back_devices_button()
        assert self.devicesMFE.verify_device_card_show_up(raise_e=True)
        assert self.devices_details_pc_mfe.verify_devices_name() == "My Computer"

    @pytest.mark.regression
    @pytest.mark.ota
    @pytest.mark.smoke
    def test_03_verify_device_model_name_C53303933(self):
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(raise_e=True)
        assert self.devices_details_pc_mfe.verify_back_devices_button_on_pc_devices_page_show_up()
        self.devices_details_pc_mfe.click_back_devices_button()
        assert self.devicesMFE.verify_device_card_show_up(raise_e=True)
        model_name = self.fc.get_windows_system_module_name()
        assert self.devices_details_pc_mfe.verify_system_module_name() == model_name, "System model name is not matching"
