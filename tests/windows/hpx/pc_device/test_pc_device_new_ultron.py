from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_PCDevice_new_ui(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
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
            cls.fc.launch_myHP()
        time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    @pytest.mark.require_stack(["production"])
    @pytest.mark.ota
    def test_01_presence_detection_visible_C50762631(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        self.fc.fd["devices"].verify_presenceOf_custom_deviceName()
        time.sleep(2)
        assert self.fc.fd["devices"].verify_presence_detection_card_on_pcdevice_page() is True, "presence detection module is not visible."
        self.fc.fd["devices"].click_presence_detection_card()
        assert self.fc.fd["vision_ai"].verify_presence_detection_title() == "Presence detection", "presence detection title is not visible."
        self.fc.fd["smart_experience"].click_smart_experience_to_pcdevice_nav()
        assert self.fc.fd["devices"].verify_presence_detection_card_on_pcdevice_page() is True, "presence detection module is not visible."

    @pytest.mark.function
    @pytest.mark.require_stack(["production"])
    @pytest.mark.ota
    def test_02_check_back_button_with_all_modules_C38474883(self):
        self.fc.restart_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        self.fc.fd["devices"].verify_presenceOf_custom_deviceName()
        time.sleep(2)
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header."
        # verify navigation to privacy alert from pcdevice
        assert self.fc.fd["devices"].verify_presence_detection_card_on_pcdevice_page() is True, "presence detection module is not visible."
        self.fc.fd["devices"].click_presence_detection_card()
        assert bool(self.fc.fd["vision_ai"].verify_presence_detection_title()) is True, "presence detection title is not visible."
        self.fc.fd["smart_experience"].click_smart_experience_to_pcdevice_nav()
        assert self.fc.fd["devices"].verify_presence_detection_card_on_pcdevice_page() is True, "presence detection module is not visible."
        self.fc.fd["navigation_panel"].click_PC_device_menu()
        self.fc.fd["navigation_panel"].navigate_pc_programmable_key_module()
        assert bool(self.fc.fd["devices"].verify_pc_device_top_title_on_hppk_module()) is True, "The hppk module is not visible on pc device header." 
        assert self.fc.fd["hppk"].get_prog_key_nav_text() == "Programmable key", "The Programmable Key text Mismatch." 
        time.sleep(2)
        self.fc.fd["devices"].click_pc_device_title_from_programmable_key_title()
        assert bool(self.fc.fd["devices"].verify_device_name_show_on_device_page_header()) is True, "The device name is not visible on header."
