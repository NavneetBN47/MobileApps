import pytest
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_ota_regression")
class Test_Suite_01_Accessibility(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        request.cls.driver = windows_test_setup
        request.cls.fc = FlowContainer(request.cls.driver)
        cls.profile= request.cls.fc.fd["profile"]
        cls.css = request.cls.fc.fd["css"]
        cls.devicesMFE = request.cls.fc.fd["devicesMFE"]
        cls.hpx_settings = request.cls.fc.fd["hpx_settings"]
        cls.accessibility = request.cls.fc.fd["accessibility"]
        cls.device_card = request.cls.fc.fd["device_card"]
        cls.devices_details_pc_mfe = request.cls.fc.fd["devices_details_pc_mfe"]
        yield
        request.cls.fc.close_myHP()

    @pytest.fixture(scope="function", autouse=True)
    def function_setup_myhp_launch(self):
        self.accessibility.dismiss_open_windows_overlays()
        if self.fc.is_app_open():
            self.fc.close_myHP()
        self.accessibility.open_app_from_start_menu("HP", unpin_from_start_menu=True, unpin_from_taskbar_start_menu=True)
        self.accessibility.dismiss_open_windows_overlays()

    @pytest.mark.regression
    def test_01_open_app_from_start_menu_C67872389(self):
        self.accessibility.open_app_from_start_menu("HP", open_app=True)
        self.css.maximize_hp()
        self.fc.is_app_open()
        self.profile.title_bar_close_myhp()

    @pytest.mark.regression
    def test_02_pin_myhp_to_start_menu_C67872391(self):
        self.accessibility.open_app_from_start_menu("HP", pin_to_start_menu=True)
        self.accessibility.click_start_menu_button()
        self.accessibility.verify_myhp_pinned_to_start_menu()
        self.accessibility.open_app_from_start_menu("HP")
        self.accessibility.click_unpin_hp_from_start_menu()
        self.accessibility.click_start_menu_button()

    @pytest.mark.regression
    def test_03_verify_scroll_bar_functionality_C67872392(self):
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name on homepage not loaded/visible"
        self.accessibility.verify_scroll_bar()
        self.accessibility.click_scroll_bar()
        self.fc.close_myHP()

    @pytest.mark.regression
    def test_04_verify_app_invoke_C53304175(self):
        self.accessibility.open_app_from_start_menu("HP", pin_to_start_menu=True)
        self.accessibility.click_start_menu_button()
        self.accessibility.open_app_from_start_menu("HP", pin_to_taskbar_menu=True)
        self.accessibility.click_start_menu_button()
        self.accessibility.verify_myhp_pinned_to_start_menu()
        self.accessibility.verify_myhp_app_icon_on_taskbar()
        self.accessibility.open_app_from_start_menu("HP", unpin_from_start_menu=True, unpin_from_taskbar_start_menu=True)
        self.accessibility.click_start_menu_button()

    @pytest.mark.regression
    def test_05_app_window_operations_C53304174(self):
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        self.accessibility.hover_to_maximize_button()
        self.fc.close_myHP()

    @pytest.mark.regression
    def test_06_pin_myhp_to_taskbar_C67872390(self):
        self.accessibility.open_app_from_start_menu("HP", pin_to_taskbar_menu=True)
        self.accessibility.verify_myhp_app_icon_on_taskbar()
        self.accessibility.dismiss_open_windows_overlays()
        self.accessibility.open_app_from_start_menu("HP", unpin_from_taskbar_start_menu=True)
        self.accessibility.click_start_menu_button()

    @pytest.mark.regression
    def test_07_verify_app_resize_scenarios_C53304178(self):
        self.fc.launch_myHP_and_skip_fuf(terminate_hp_background_apps=True)
        self.devicesMFE.restore_app()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.device_card.verify_bell_icon_present()
        self.css.verify_sign_in_button_show_up()
        self.profile.maximize_hp()
        assert self.devices_details_pc_mfe.verify_pc_device_name_show_up(), "PC name not present on device details page"
        self.device_card.verify_bell_icon_present()
        self.css.verify_sign_in_button_show_up()
        self.fc.close_myHP()

    @pytest.mark.regression
    def test_08_hp_app_appears_in_windows_programs_and_feature_C60030522(self):
        self.accessibility.open_app_from_start_menu("Settings", open_app=True)
        self.accessibility.click_apps_button()
        self.accessibility.click_installed_apps_button()
        self.accessibility.click_search_for_installed_apps()
        assert self.accessibility.verify_hp_app_icon_in_windows_settings()
        self.profile.title_bar_close_myhp()

    @pytest.mark.regression
    def test_09_hp_app_appears_in_windows_task_manager_C60030617(self):
        self.fc.launch_myHP_and_skip_fuf()
        self.accessibility.open_app_from_start_menu("Task Manager", open_app=True)
        assert self.accessibility.verify_hp_app_icon_in_windows_settings()
        self.profile.title_bar_close_myhp()

    @pytest.mark.regression
    def test_10_hp_app_appears_in_windows_start_menu_C61082852(self):
        self.accessibility.open_app_from_start_menu("HP", open_app=True)
        assert self.accessibility.verify_hp_app_icon_in_windows_settings()
        self.profile.title_bar_close_myhp()

    @pytest.mark.regression
    def test_11_hp_app_appears_in_windows_programs_C61082932(self):
        self.accessibility.open_app_from_start_menu("Settings", open_app=True)
        if self.fc.is_app_open():
            self.fc.close_myHP()
        self.accessibility.open_app_from_start_menu("HP", open_app=True)
        assert self.accessibility.verify_hp_app_icon_in_windows_settings()
        self.accessibility.dismiss_open_windows_overlays()
        self.profile.title_bar_close_myhp()

    @pytest.mark.regression
    def test_12_hp_app_appears_in_ms_store_C61083738(self):
        self.accessibility.open_app_from_start_menu("Microsoft Store", open_app=True)
        self.accessibility.click_library_button_on_msstore()
        assert self.accessibility.verify_hp_app_icon_in_windows_settings()

    @pytest.mark.regression
    def test_13_hp_app_appears_title_bar_C61085157(self):
        self.fc.launch_myHP_and_skip_fuf()
        assert self.device_card.verify_hp_app_window_title()
        self.profile.title_bar_close_myhp()
        
    @pytest.mark.regression
    def test_14_hp_app_appears_in_windows_task_bar_C61082893(self):
        self.fc.launch_myHP_and_skip_fuf()
        self.accessibility.verify_myhp_app_icon_on_taskbar()
        el = self.driver.find_object("myhp_app_icon_on_taskbar")
        self.driver.click_by_coordinates(el, right_click=True)
        assert self.accessibility.verify_hp_app_icon_in_windows_settings()