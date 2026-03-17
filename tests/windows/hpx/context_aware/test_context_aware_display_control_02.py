import pytest
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Context_Aware_02(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        region = "China"
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.sf = SystemFlow(cls.driver)
        cls.fc = FlowContainer(cls.driver)
        time.sleep(5)

        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            if region == "China":
                time.sleep(5)
                cls.fc.change_system_region_to_united_states()
            cls.fc.install_video_apps_from_ms_store_for_disney("Disney+","disney_plus_app_ms_store")
            time.sleep(20)
            cls.fc.change_system_region_to_china()
            time.sleep(10)
            cls.fc.kill_msstore_process()
            time.sleep(15)
            cls.fc.install_video_apps_from_ms_store("腾讯视频","tencent_video_app_ms_store")
            time.sleep(15)
            cls.fc.install_video_apps_from_ms_store("爱奇艺","iqiyi_video_app_ms_store")
            time.sleep(15)
            cls.fc.kill_msstore_process()
            time.sleep(5)
            cls.fc.launch_myHP()
        yield "install hp privacy settings and change region to US"
        time.sleep(2)
        cls.fc.install_hp_privacy_settings_app()
        time.sleep(2)
        cls.fc.change_system_region_to_united_states()
        time.sleep(2)
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()



    @pytest.mark.ota
    def test_01_first_launch_context_aware_list_C36766917(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert bool(self.fc.fd["sanity_check"].verify_display_control_show()) is True, "Display module is not visible."

        assert self.fc.fd["context_aware"].verify_context_aware_show() is True, "Context aware module is not visible."
        assert self.fc.fd["context_aware"].verify_disney_plus_app_show() is True, "Disney plus application is visible."
        assert self.fc.fd["context_aware"].verify_add_application_button_show() is True, "Add application button is not visible."

    
    @pytest.mark.ota
    def test_02_uninstall_application_C36766924(self):
        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert bool(self.fc.fd["sanity_check"].verify_display_control_show()) is True, "Display module is not visible."

        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("hp privacy")
        assert bool(self.fc.fd["context_aware"].verify_application("privacy_setting")) == True, "The added privacy setting application is not visible."
        self.fc.fd["context_aware"].click_application("privacy_setting")
        self.fc.fd["context_aware"].click_add_application_add_button()

        self.fc.uninstall_hp_privacy_settings_app()

        time.sleep(3)
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert bool(self.fc.fd["sanity_check"].verify_display_control_show()) is True, "Display module is not visible."

        assert bool(self.fc.fd["context_aware"].verify_privacy_settings_button_show()) is True, "The added privacy setting application is not visible."

        self.fc.install_hp_privacy_settings_app()

    @pytest.mark.ota
    def test_03_uncheck_checkobox_delete_application_C36766922(self):
        time.sleep(3)
        self.fc.reset_myhp_app()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        assert bool(self.fc.fd["sanity_check"].verify_display_control_show()) is True, "Display module is not visible."

        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("hp privacy")
        assert bool(self.fc.fd["context_aware"].verify_application("privacy_setting")) == True, "The added privacy setting application is not visible."
        self.fc.fd["context_aware"].click_application("privacy_setting")
        self.fc.fd["context_aware"].click_add_application_add_button()

        time.sleep(2)
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application("calculator")
        assert bool(self.fc.fd["context_aware"].verify_application("calculator")) == True, "The added calculator application is not visible."
        self.fc.fd["context_aware"].click_application("calculator")
        self.fc.fd["context_aware"].click_add_application_add_button()

        time.sleep(2)

        self.fc.fd["context_aware"].click_application("privacy_setting")
        self.fc.fd["context_aware"].click_delete_application_button("privacy_setting")
        time.sleep(3)
        self.fc.fd["context_aware"].click_delete_continue_application_button()

        assert bool(self.fc.fd["context_aware"].verify_privacy_settings_button_show()) is False, "The added privacy setting application is not deleted."
