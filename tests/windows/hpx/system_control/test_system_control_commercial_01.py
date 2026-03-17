from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
import MobileApps.resources.const.windows.const as w_const
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
from MobileApps.libs.ma_misc import ma_misc
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_System_control_commercial(object):
   @pytest.fixture(scope="class", autouse="true")
   def class_setup(cls, request,windows_test_setup):
      cls = cls.__class__
      cls.driver = windows_test_setup
      cls.fc = FlowContainer(cls.driver)
      cls.sf = SystemFlow(cls.driver)
      if request.config.getoption("--ota-test") is not None:
         time.sleep(10)
         cls.fc.fd["home"].click_to_install_signed_build()
         time.sleep(60)
         cls.fc.launch_myHP()
         time.sleep(5)
         cls.fc.ota_app_after_update()
      else:
         cls.fc.launch_myHP()
      yield 
      if request.config.getoption("--ota-test") is not None:
         cls.fc.exit_hp_app_and_msstore()
      time.sleep(2)

   @pytest.mark.commercial
   def test_01_bidirectional_sync_default_values_for_windows_settings_and_system_control_ui_C41754705(self):
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_balance_name()
      self.fc.close_windows_settings_panel()
      self.fc.launch_myHP()
      self.fc.fd["navigation_panel"].navigate_to_system_control()
      assert self.fc.fd["system_control"].verify_smart_sense_selected_commercial() =="true", "Smart Sense mode is not selected"
      self.fc.close_myHP()

   @pytest.mark.commercial
   def test_02_bidirectional_sync_with_win_os_for_system_control_smart_sense_v2_windows_settings_to_hpx_application_C41755527(self):
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_balance_name()
      self.fc.close_windows_settings_panel()
      self.fc.launch_myHP()
      self.fc.fd["navigation_panel"].navigate_to_system_control()
      assert self.fc.fd["system_control"].verify_smart_sense_selected_commercial() =="true", "Smart Sense mode is not selected"
      self.fc.close_myHP()
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_power_mode()
      self.fc.fd["system_control"].click_power_mode_dd_in_settings()
      self.fc.fd["system_control"].click_plug_in_combo_box()
      self.fc.fd["system_control"].verify_best_performance()
      self.fc.fd["system_control"].click_best_performance()
      self.fc.close_windows_settings_panel()
      self.fc.launch_myHP()
      time.sleep(4)
      self.fc.fd["navigation_panel"].navigate_to_system_control()
      assert self.fc.fd["system_control"].verify_performance_commercial_selected_commercial() =="true", "performance mode is not selected"
      self.fc.close_myHP()
      #reverting back the changes as reset dont work
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_power_mode()
      self.fc.fd["system_control"].click_power_mode_dd_in_settings()
      self.fc.fd["system_control"].click_plug_in_combo_box()
      self.fc.fd["system_control"].verify_balance_name()
      self.fc.fd["system_control"].click_balance_name()
      self.fc.close_windows_settings_panel()

   def test_03_bidirectional_sync_with_win_os_for_system_control_workstation_hpx_application_windows_settings_C41755811(self):
      self.fc.launch_myHP()
      self.fc.fd["navigation_panel"].navigate_to_system_control()
      assert self.fc.fd["system_control"].verify_smart_sense_selected_commercial() =="true", "Smart Sense mode is not selected"
      self.fc.fd["system_control"].click_performance_commercial()
      assert self.fc.fd["system_control"].verify_performance_commercial_selected_commercial() =="true", "performance mode is not selected"
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_best_performance()
      self.fc.close_windows_settings_panel()
      self.fc.close_myHP()
      #reverting back the changes as reset dont work
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_power_mode()
      self.fc.fd["system_control"].click_power_mode_dd_in_settings()
      self.fc.fd["system_control"].click_plug_in_combo_box()
      self.fc.fd["system_control"].verify_balance_name()
      self.fc.fd["system_control"].click_balance_name()
      self.fc.close_windows_settings_panel()

   def test_04_bidirectional_sync_with_win_os_for_system_control_workstation_hpx_application_windows_settings_C41756111(self):
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_power_mode()
      self.fc.fd["system_control"].click_power_mode_dd_in_settings()
      self.fc.fd["system_control"].click_plug_in_combo_box()
      self.fc.fd["system_control"].verify_best_performance()
      self.fc.fd["system_control"].click_best_performance()
      self.fc.close_windows_settings_panel()
      self.fc.launch_myHP()
      self.fc.fd["navigation_panel"].navigate_to_system_control()
      assert self.fc.fd["system_control"].verify_performance_commercial_selected_commercial() =="true", "performance mode is not selected"
      self.fc.close_myHP()
      #reverting back the changes as reset dont work
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_power_mode()
      self.fc.fd["system_control"].click_power_mode_dd_in_settings()
      self.fc.fd["system_control"].click_plug_in_combo_box()
      self.fc.fd["system_control"].verify_balance_name()
      self.fc.fd["system_control"].click_balance_name()
      self.fc.close_windows_settings_panel()

   def test_05_bidirectional_sync_for_best_power_efficiency_mode_C41756291(self):
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_power_mode()
      self.fc.fd["system_control"].click_power_mode_dd_in_settings()
      self.fc.fd["system_control"].click_plug_in_combo_box()
      self.fc.fd["system_control"].verify_best_power_efficiency()
      self.fc.fd["system_control"].click_best_power_efficiency()
      self.fc.close_windows_settings_panel()
      self.fc.launch_myHP()
      self.fc.fd["navigation_panel"].navigate_to_system_control()
      assert self.fc.fd["system_control"].verify_smart_sense_selected_commercial() =="true", "Smart Sense mode is not selected"
      self.fc.close_myHP()
      #reverting back the changes as reset dont work
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_power_mode()
      self.fc.fd["system_control"].click_power_mode_dd_in_settings()
      self.fc.fd["system_control"].click_plug_in_combo_box()
      self.fc.fd["system_control"].verify_balance_name()
      self.fc.fd["system_control"].click_balance_name()
      self.fc.close_windows_settings_panel()

   def test_06_bidirectional_sync_with_win_os_for_system_control_workstation_hpx_application_windows_settings_C41755065(self):
      self.fc.launch_myHP()
      self.fc.fd["navigation_panel"].navigate_to_system_control()
      assert self.fc.fd["system_control"].verify_smart_sense_selected_commercial() =="true", "Smart Sense mode is not selected"
      self.fc.close_myHP()
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_balance_name()
      self.fc.close_windows_settings_panel()
      self.fc.launch_myHP()
      self.fc.fd["navigation_panel"].navigate_to_system_control()
      assert self.fc.fd["system_control"].verify_smart_sense_selected_commercial() =="true", "Smart Sense mode is not selected"
      self.fc.fd["system_control"].click_performance_commercial()
      assert self.fc.fd["system_control"].verify_performance_commercial_selected_commercial() =="true", "performance mode is not selected"
      self.fc.close_myHP()
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_best_performance()
      self.fc.close_windows_settings_panel()
      #reverting back the changes as reset dont work
      self.fc.open_power_sleep()
      self.fc.fd["system_control"].verify_power_mode()
      self.fc.fd["system_control"].click_power_mode_dd_in_settings()
      self.fc.fd["system_control"].click_plug_in_combo_box()
      self.fc.fd["system_control"].verify_balance_name()
      self.fc.fd["system_control"].click_balance_name()
      self.fc.close_windows_settings_panel()

   @pytest.mark.require_sanity_check(["sanity"])
   @pytest.mark.ota
   def test_07_Optimize_oled_power_consumption_supported_platform_C33694775(self):
      self.fc.launch_myHP()
      self.fc.fd["navigation_panel"].navigate_to_system_control()
      self.fc.fd["system_control"].get_oled_toggle_text()
      assert self.fc.fd["system_control"].verify_oled_toggle_off() == "0","OLED toggle is on"
      self.fc.fd["system_control"].click_oled_toggle_on()
      assert self.fc.fd["system_control"].verify_oled_toggle_on() == "1","OLED toggle is off"
      self.fc.fd["system_control"].click_oled_toggle_off()
      assert self.fc.fd["system_control"].verify_oled_toggle_off() == "0","OLED toggle is on"