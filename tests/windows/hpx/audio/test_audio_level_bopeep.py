from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import pytest
import time
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow
import logging

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Audio_Level(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request,windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        cls.fc.launch_myHP()
        time.sleep(2)
    
    def test_01_change_active_input_device_verify_that_active_input_device_changes_to_selected_device_C31680837(self):
        assert bool(self.fc.fd["navigation_panel"].verify_navigationicon_show()) is True
        self.fc.fd["navigation_panel"].navigate_to_pc_audio()
        self.fc.fd["audio"].click_microphone_array_in_all_devices()
        time.sleep(3)
        command = '(Get-AudioDevice -List | Where-Object { $_.Name -eq \'Headset Microphone (Plantronics C320-M)\' -and $_.Default }).Name'
        output = self.driver.ssh.send_command(command, raise_e=False, timeout=20)
        logging.info(f"Raw PowerShell output: {output}")
        microphone_name = output.get('stdout', '').strip()
        print(f"Microphone Name Output: {microphone_name}")
        expected_microphone_name = "Headset Microphone (Plantronics C320-M)"
        assert microphone_name != expected_microphone_name, (f"Expected microphone name '{expected_microphone_name}', but got '{microphone_name}'")
        self.fc.fd["audio"].click_headset_usb_input()
        time.sleep(3)
        command = '(Get-AudioDevice -List | Where-Object { $_.Name -eq \'Headset Microphone (Plantronics C320-M)\' -and $_.Default }).Name'
        output = self.driver.ssh.send_command(command, raise_e=False, timeout=20)
        logging.info(f"Raw PowerShell output: {output}")
        microphone_name = output.get('stdout', '').strip()
        print(f"Microphone Name Output: {microphone_name}")
        expected_microphone_name = "Headset Microphone (Plantronics C320-M)"
        assert microphone_name == expected_microphone_name, (f"Expected microphone name '{expected_microphone_name}', but got '{microphone_name}'")