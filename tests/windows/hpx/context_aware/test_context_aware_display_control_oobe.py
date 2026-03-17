import pytest
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import time
import logging


pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
soft_assertion = SoftAssert()
oobe_app_list = {"disney+" : "Disney+", "tencent" : "腾讯视频", "iqiyi" : "爱奇艺"}

class Test_Suite_Context_Aware_Oobe(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        region = "China"
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)

        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()
        else:
            if region == "China":
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
        
        yield "change_system_region_to_united_states"
        time.sleep(2)
        cls.fc.change_system_region_to_united_states()
        time.sleep(2)
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()
    
    @pytest.mark.ota
    def test_01_verify_context_aware_display_control_oobe_C38203795(self):
        global oobe_app_present
        self.fc.restart_myHP()
        if self.fc.fd["hp_registration"].verify_skip_button_show():
            self.fc.fd["hp_registration"].click_skip_button()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        for oobe_app in oobe_app_list:
            if self.fc.fd["context_aware"].verify_application_icon(oobe_app):
                logging.info(oobe_app.capitalize() + " is present")
                oobe_application_flag = True
                oobe_app_present = oobe_app
                break
        soft_assertion.assert_equal(oobe_application_flag, True, "Oobe applications are not present")
        soft_assertion.raise_assertion_errors()
    
    @pytest.mark.ota
    def test_02_verify_context_aware_oobe_app_delete_C38203797(self):
        global oobe_app_present
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        self.fc.fd["context_aware"].click_application(oobe_app_present)
        self.fc.fd["context_aware"].click_delete_application_button(oobe_app_present)
        self.fc.fd["context_aware"].click_delete_continue_application_button()
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application(oobe_app_present)), False, oobe_app_present.capitalize() + " is not deleted")
        soft_assertion.raise_assertion_errors()
    

    @pytest.mark.ota
    def test_03_verify_context_aware_oobe_add_default_app_C40497636(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        self.fc.fd["context_aware"].click_add_application()
        self.fc.fd["context_aware"].click_add_application_search_box()
        self.fc.fd["context_aware"].search_application(oobe_app_present)
        soft_assertion.assert_equal(bool(self.fc.fd["context_aware"].verify_application(oobe_app_present)), True, oobe_app_present + " is not present")
        self.fc.fd["context_aware"].click_application(oobe_app_present)
        self.fc.fd["context_aware"].click_add_application_add_button()
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_application_icon(oobe_app_present), oobe_app_list[oobe_app_present], oobe_app_present + " is not added")
        soft_assertion.raise_assertion_errors()

    @pytest.mark.ota
    def test_04_re_visable_after_reset_hpx_C38203928(self):
        self.fc.restart_myHP()
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(3)
        self.fc.fd["navigation_panel"].navigate_to_pc_device_menu()
        state = self.fc.fd["navigation_panel"].check_PC_device_menu_arrow()
        self.fc.fd["navigation_panel"].verify_PC_device_menu(state)
        time.sleep(5)
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        soft_assertion.assert_equal(self.fc.fd["devices"].verify_display_control(), "Display Control Action Item", "Display Control is not visible at PC Device")
        self.fc.fd["devices"].click_display_control()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        soft_assertion.assert_true(bool(self.fc.fd["context_aware"].verify_disney_plus_app_show()), "Disney is not present")
        soft_assertion.assert_true(bool(self.fc.fd["context_aware"].verify_iqiyi_app_show()), "iqiyi is not present")
        soft_assertion.assert_true(bool(self.fc.fd["context_aware"].verify_tencent_video_app_show()), "tencent video is not present")
        soft_assertion.raise_assertion_errors()
    
    @pytest.mark.ota
    def test_05_set_region_to_china_C38426305(self):
        time.sleep(2)
        self.fc.change_system_region_to_china()
        time.sleep(2)
        self.fc.restart_myHP()
        time.sleep(3)
        self.fc.fd["navigation_panel"].verify_navigationicon_show() is True
        self.fc.fd["navigation_panel"].navigate_pc_display_control_module()
        time.sleep(5)
        soft_assertion.assert_equal(self.fc.fd["context_aware"].verify_context_aware(), "Add Application", "Context Aware is not present")
        soft_assertion.assert_true(bool(self.fc.fd["context_aware"].verify_disney_plus_app_show()), "Disney is not present")
        soft_assertion.assert_true(bool(self.fc.fd["context_aware"].verify_iqiyi_app_show()), "iqiyi is not present")
        soft_assertion.assert_true(bool(self.fc.fd["context_aware"].verify_tencent_video_app_show()), "tencent video is not present")
        soft_assertion.raise_assertion_errors()

        self.fc.uninstall_videos_app_from_ms_store("Disney+")
        time.sleep(5)
        self.fc.uninstall_videos_app_from_ms_store("爱奇艺") 
        time.sleep(5)
        self.fc.uninstall_videos_app_from_ms_store("腾讯视频")
        time.sleep(5)   
        self.fc.close_myHP()         
        #To switch back to US region
        self.fc.change_system_region_to_united_states()

