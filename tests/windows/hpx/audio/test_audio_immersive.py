from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import MobileApps.resources.const.windows.const as w_const
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"
class Test_Suite_Audio_Immersive(object):
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
            cls.ssh = SSH(request.config.getoption('--mobile-device'), "exec")
            cls.remote_artifact_path = "{}\\{}\\LocalState\\".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
            cls.ssh.send_file(ma_misc.get_abs_path("/resources/test_data/hpx/properties.json"),cls.remote_artifact_path+"properties.json") 
            cls.fc.launch_myHP()
            time.sleep(5)
        yield
        if request.config.getoption("--ota-test") is not None:
            cls.fc.exit_hp_app_and_msstore()

    #suite support in contino
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_01_immersive_on_settings_C32568968(self):
        self.fc.restart_myHP()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        self.fc.fd["audio"].click_internal_speaker_output_device_thompson()
        self.fc.fd["audio"].click_preset_movie()
        time.sleep(2)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie is not selected"
        self.fc.fd["audio"].click_settings_audio()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_immersive_on_settings()) is True
        assert self.fc.fd["audio"].is_immersive_toggle_status_on_status() =="1", "Immersive toggle is not on"
        self.fc.close_myHP()
        
    def test_02_remember_immersive_settings_C32603508(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)

        self.fc.fd["audio"].click_preset_movie()
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie is not selected"
        time.sleep(2)

        self.fc.fd["audio"].click_settings_audio()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_immersive_on_settings()) is True
        

        self.fc.fd["audio"].turn_off_immersive_audio_toggle()
        time.sleep(2)
        assert self.fc.fd["audio"].is_immersive_toggle_status_off_status() =="0", "Immersive toggle is on"

        self.fc.close_myHP()
        time.sleep(5)
        self.fc.launch_myHP()
        time.sleep(5)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie is not selected"

        self.fc.fd["audio"].click_settings_audio()
        time.sleep(2)
        assert self.fc.fd["audio"].is_immersive_toggle_status_off_status() =="0", "Immersive toggle is on"

        self.fc.fd["audio"].turn_on_immersive_audio_toggle()

    @pytest.mark.require_sanity_check(["sanity"])
    def test_03_turn_on_off_immersive_audio_toggle_C34776281(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(2)

        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)

        self.fc.fd["audio"].click_preset_movie()
        time.sleep(2)
        assert self.fc.fd["audio"].is_movie_status_selected() == "1", "Movie is not selected"
        
        self.fc.fd["audio"].click_settings_audio()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_immersive_on_settings()) is True
        assert self.fc.fd["audio"].is_immersive_toggle_status_on_status() =="1", "Immersive toggle is not on"
        self.fc.fd["audio"].turn_off_immersive_audio_toggle()
        time.sleep(2)
        assert self.fc.fd["audio"].is_immersive_toggle_status_off_status() =="0", "Immersive toggle is on"
        
        self.fc.fd["audio"].turn_on_immersive_audio_toggle()
        time.sleep(2)
        assert self.fc.fd["audio"].is_immersive_toggle_status_on_status() =="1", "Immersive toggle is not on"
        self.fc.fd["audio"].close_audio_settings()


    @pytest.mark.consumer
    def test_04_verify_restore_button_work_with_immersive_audio_C37543542(self):
        time.sleep(2)
        self.fc.reset_myhp_app()
        time.sleep(3)
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()
        time.sleep(2)
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        time.sleep(2)

        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Immersive toggle is not on"
        assert bool(self.fc.fd["audio"].verify_settings_btn_show()) is False

        time.sleep(2)
        self.fc.fd["audio"].click_preset_movie()
        time.sleep(2)
        assert bool(self.fc.fd["audio"].verify_settings_btn_show()) is True

        time.sleep(2)
        self.fc.swipe_window(direction="down", distance=3)
        time.sleep(2)
        self.fc.fd["audio"].click_restore_button()
        time.sleep(2)
        self.fc.fd["audio"].click_continue_on_restore_dialog()
        time.sleep(4)
        self.fc.swipe_window(direction="up", distance=3)
        self.fc.fd["audio"].close_windows_camera()

        assert self.fc.fd["audio"].is_music_status_selected() == "1", "Music is not selected"
        assert bool(self.fc.fd["audio"].verify_settings_btn_show()) is False